---
title: Split During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Absolute Split During Transaction allows you to split a payment among multiple merchants or entities during the transaction process. This is ideal for marketplace platforms where payment distribution needs to happen at the time of transaction with fixed, predetermined amounts.

## Prerequisites

Before integrating Absolute Split During Transaction, ensure you have:

1. **PayU Merchant Account**: An active PayU merchant account set up as an aggregator/marketplace
2. **Child Merchants Onboarded**: Child merchants must be registered and approved in the PayU system
3. **API Credentials**: Your merchant `key` and `salt` values from the PayU dashboard
4. **Transaction Logic**: A system to calculate the exact split amounts for each transaction

### Getting Your API Credentials

1. Log into your [PayU Dashboard](https://test.payu.in/merchant/dashboard).
2. Navigate to **Developer** → **API Keys**.
3. Copy your **Client ID** and **Client Secret** values.

<Image align="center" src="https://files.readme.io/b62366ef47b8fed510c8bbc95fa3cfeab71daf64b303ca07693a24e73a27fc0f-dashboard_developer_copy_client_id_secret.png" />

4. Note your Merchant ID for reference.


## Step 1: Prepare the Split Request

Create a JSON structure that defines how the transaction amount should be split among different merchants:

```json
{
  "type": "absolute",
  "splitInfo": {
    "MERCHANT_KEY_1": {
      "aggregatorSubTxnId": "SUB_TXN_ID_1",
      "aggregatorSubAmt": "600",
      "aggregatorCharges": "50"
    },
    "MERCHANT_KEY_2": {
      "aggregatorSubTxnId": "SUB_TXN_ID_2",
      "aggregatorSubAmt": "400"
    }
  }
}
```

**Parameters Explained**:

* `type`: Must be set to "absolute" for Absolute Split During Transaction
* `splitInfo`: Contains the split details for each merchant
  * `MERCHANT_KEY_x`: The merchant key of the child merchant
  * `aggregatorSubTxnId`: A unique ID for this sub-transaction
  * `aggregatorSubAmt`: The exact amount to be settled to this merchant
  * `aggregatorCharges`: (Optional) Platform fees or service charges

> 📘 Split calculation:
>
> The sum of all `aggregatorSubAmt` values plus any `aggregatorCharges` must equal the total transaction amount.

## Step 2: Generate the Payment Request

Create a payment request that includes the split information:

**HTML Form Example**:

```html
<form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="TXN_123456789" />
    <input type="hidden" name="amount" value="1000" />
    <input type="hidden" name="productinfo" value="Product Description" />
    <input type="hidden" name="firstname" value="Customer Name" />
    <input type="hidden" name="email" value="customer@example.com" />
    <input type="hidden" name="phone" value="9999999999" />
    <input type="hidden" name="surl" value="https://yourwebsite.com/success" />
    <input type="hidden" name="furl" value="https://yourwebsite.com/failure" />
    <input type="hidden" name="splitRequest" value='{"type":"absolute","splitInfo":{"MERCHANT_KEY_1":{"aggregatorSubTxnId":"SUB_TXN_ID_1","aggregatorSubAmt":"600","aggregatorCharges":"50"},"MERCHANT_KEY_2":{"aggregatorSubTxnId":"SUB_TXN_ID_2","aggregatorSubAmt":"400"}}}' />
    <input type="hidden" name="hash" value="GENERATED_HASH_VALUE" />
    <input type="submit" value="Pay Now" />
</form>
```

## Step 3: Handle the Response

After payment completion, PayU redirects to your success or failure URL with transaction details:

**Response Parameters**:

| Parameter                 | Description                                |
| ------------------------- | ------------------------------------------ |
| `status`                  | Payment status (success, failure, pending) |
| `txnid`                   | Transaction ID sent in the request         |
| `amount`                  | Transaction amount                         |
| `mihpayid`                | PayU payment ID                            |
| `splitInfo.splitStatus`   | Status of the split operation              |
| `splitInfo.splitSegments` | Array of split details                     |

**Example Response**:

```json
{
  "status": "success",
  "txnid": "TXN_123456789",
  "amount": "1000.00",
  "mihpayid": "403993715519672950",
  "error_code": "E000",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "MERCHANT_KEY_1",
        "amount": 600,
        "txnId": "SUB_TXN_ID_1"
      },
      {
        "merchantKey": "MERCHANT_KEY_2",
        "amount": 400,
        "txnId": "SUB_TXN_ID_2"
      }
    ]
  }
}
```

## Step 4: Verify the Transaction

Always verify the transaction status using the Verify Payment API to ensure data integrity:

**Python Example**:

```python
import requests
import hashlib

def verify_payment(txnid, mihpayid):
    # API endpoint
    url = "https://info.payu.in/merchant/postservice.php?form=2"
    
    # Required parameters
    key = "YOUR_MERCHANT_KEY"
    command = "verify_payment"
    
    # Generate hash
    hash_string = key + '|' + command + '|' + txnid + '|' + "YOUR_SALT"
    hash_value = hashlib.sha512(hash_string.encode()).hexdigest()
    
    # Create payload
    payload = {
        "key": key,
        "command": command,
        "hash": hash_value,
        "var1": txnid,
        "var2": mihpayid
    }
    
    # Make the API call
    response = requests.post(url, data=payload)
    return response.json()

# Usage
result = verify_payment("TXN_123456789", "403993715519672950")
print(result)
```

## Code Examples

### Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.security.MessageDigest;
import java.util.Map;
import java.util.HashMap;
import java.util.Base64;

public class PayUAbsoluteSplit {
    public static void main(String[] args) throws Exception {
        // Merchant details
        String key = "YOUR_MERCHANT_KEY";
        String salt = "YOUR_MERCHANT_SALT";
        String txnid = "TXN_" + System.currentTimeMillis();
        String amount = "1000";
        String productinfo = "Product Description";
        String firstname = "Customer Name";
        String email = "customer@example.com";
        String phone = "9999999999";
        String surl = "https://yourwebsite.com/success";
        String furl = "https://yourwebsite.com/failure";
        
        // Split information
        String splitRequest = "{\"type\":\"absolute\",\"splitInfo\":{\"MERCHANT_KEY_1\":{\"aggregatorSubTxnId\":\"SUB_TXN_ID_1\",\"aggregatorSubAmt\":\"600\",\"aggregatorCharges\":\"50\"},\"MERCHANT_KEY_2\":{\"aggregatorSubTxnId\":\"SUB_TXN_ID_2\",\"aggregatorSubAmt\":\"400\"}}}";
        
        // Generate hash
        String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                          firstname + "|" + email + "|||||||" + salt + "|" + splitRequest;
        
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes());
        String hash = Base64.getEncoder().encodeToString(digest);
        
        // Create request parameters
        Map<String, String> params = new HashMap<>();
        params.put("key", key);
        params.put("txnid", txnid);
        params.put("amount", amount);
        params.put("productinfo", productinfo);
        params.put("firstname", firstname);
        params.put("email", email);
        params.put("phone", phone);
        params.put("surl", surl);
        params.put("furl", furl);
        params.put("splitRequest", splitRequest);
        params.put("hash", hash);
        
        // Convert to form data
        StringBuilder formData = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) {
            if (formData.length() > 0) formData.append("&");
            formData.append(entry.getKey()).append("=").append(entry.getValue());
        }
        
        // Create HTTP request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData.toString()))
            .build();
        
        // Send request
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```

### PHP

```php
<?php
// Merchant details
$key = "YOUR_MERCHANT_KEY";
$salt = "YOUR_MERCHANT_SALT";
$txnid = "TXN_" . time();
$amount = "1000";
$productinfo = "Product Description";
$firstname = "Customer Name";
$email = "customer@example.com";
$phone = "9999999999";
$surl = "https://yourwebsite.com/success";
$furl = "https://yourwebsite.com/failure";

// Split information
$splitRequest = '{"type":"absolute","splitInfo":{' .
    '"MERCHANT_KEY_1":{"aggregatorSubTxnId":"SUB_TXN_ID_1","aggregatorSubAmt":"600","aggregatorCharges":"50"},' .
    '"MERCHANT_KEY_2":{"aggregatorSubTxnId":"SUB_TXN_ID_2","aggregatorSubAmt":"400"}' .
    '}}';

// Generate hash
$hashString = "$key|$txnid|$amount|$productinfo|$firstname|$email|||||||$salt|$splitRequest";
$hash = hash("sha512", $hashString);

// Create form data
$data = array(
    'key' => $key,
    'txnid' => $txnid,
    'amount' => $amount,
    'productinfo' => $productinfo,
    'firstname' => $firstname,
    'email' => $email,
    'phone' => $phone,
    'surl' => $surl,
    'furl' => $furl,
    'splitRequest' => $splitRequest,
    'hash' => $hash
);

// Send request using cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://test.payu.in/_payment");
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### cURL

```bash
#!/bin/bash
KEY="YOUR_MERCHANT_KEY"
TXNID="TXN_$(date +%s)"
AMOUNT="1000"
PRODUCTINFO="Product Description"
FIRSTNAME="Customer Name"
EMAIL="customer@example.com"
PHONE="9999999999"
SURL="https://yourwebsite.com/success"
FURL="https://yourwebsite.com/failure"
SALT="YOUR_MERCHANT_SALT"

# Split request
SPLIT_REQUEST='{"type":"absolute","splitInfo":{"MERCHANT_KEY_1":{"aggregatorSubTxnId":"SUB_TXN_ID_1","aggregatorSubAmt":"600","aggregatorCharges":"50"},"MERCHANT_KEY_2":{"aggregatorSubTxnId":"SUB_TXN_ID_2","aggregatorSubAmt":"400"}}}'

# Generate hash
HASH_STRING="$KEY|$TXNID|$AMOUNT|$PRODUCTINFO|$FIRSTNAME|$EMAIL|||||||$SALT|$SPLIT_REQUEST"
HASH=$(echo -n "$HASH_STRING" | sha512sum | awk '{print $1}')

# Send request
curl -X POST https://test.payu.in/_payment \
  -d "key=$KEY" \
  -d "txnid=$TXNID" \
  -d "amount=$AMOUNT" \
  -d "productinfo=$PRODUCTINFO" \
  -d "firstname=$FIRSTNAME" \
  -d "email=$EMAIL" \
  -d "phone=$PHONE" \
  -d "surl=$SURL" \
  -d "furl=$FURL" \
  -d "splitRequest=$SPLIT_REQUEST" \
  -d "hash=$HASH"
```

### Python

```python
import requests
import hashlib
import time
import json

# Merchant details
key = "YOUR_MERCHANT_KEY"
salt = "YOUR_MERCHANT_SALT"
txnid = f"TXN_{int(time.time())}"
amount = "1000"
productinfo = "Product Description"
firstname = "Customer Name"
email = "customer@example.com"
phone = "9999999999"
surl = "https://yourwebsite.com/success"
furl = "https://yourwebsite.com/failure"

# Split information
split_request = {
    "type": "absolute",
    "splitInfo": {
        "MERCHANT_KEY_1": {
            "aggregatorSubTxnId": "SUB_TXN_ID_1",
            "aggregatorSubAmt": "600",
            "aggregatorCharges": "50"
        },
        "MERCHANT_KEY_2": {
            "aggregatorSubTxnId": "SUB_TXN_ID_2",
            "aggregatorSubAmt": "400"
        }
    }
}

# Convert split request to JSON string
split_request_str = json.dumps(split_request, separators=(',', ':'))

# Generate hash
hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|||||||{salt}|{split_request_str}"
hash_value = hashlib.sha512(hash_string.encode()).hexdigest()

# Create request data
data = {
    'key': key,
    'txnid': txnid,
    'amount': amount,
    'productinfo': productinfo,
    'firstname': firstname,
    'email': email,
    'phone': phone,
    'surl': surl,
    'furl': furl,
    'splitRequest': split_request_str,
    'hash': hash_value
}

# Send request
response = requests.post("https://test.payu.in/_payment", data=data)
print(response.text)
```

### C\#

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Merchant details
        string key = "YOUR_MERCHANT_KEY";
        string salt = "YOUR_MERCHANT_SALT";
        string txnid = "TXN_" + DateTimeOffset.Now.ToUnixTimeSeconds();
        string amount = "1000";
        string productinfo = "Product Description";
        string firstname = "Customer Name";
        string email = "customer@example.com";
        string phone = "9999999999";
        string surl = "https://yourwebsite.com/success";
        string furl = "https://yourwebsite.com/failure";

        // Split information
        string splitRequest = "{\"type\":\"absolute\",\"splitInfo\":{\"MERCHANT_KEY_1\":{\"aggregatorSubTxnId\":\"SUB_TXN_ID_1\",\"aggregatorSubAmt\":\"600\",\"aggregatorCharges\":\"50\"},\"MERCHANT_KEY_2\":{\"aggregatorSubTxnId\":\"SUB_TXN_ID_2\",\"aggregatorSubAmt\":\"400\"}}}";

        // Generate hash
        string hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" +
                          firstname + "|" + email + "|||||||" + salt + "|" + splitRequest;

        string hash;
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] hashBytes = sha512.ComputeHash(Encoding.UTF8.GetBytes(hashString));
            hash = BitConverter.ToString(hashBytes).Replace("-", "").ToLower();
        }

        // Create form data
        var formData = new Dictionary<string, string>
        {
            { "key", key },
            { "txnid", txnid },
            { "amount", amount },
            { "productinfo", productinfo },
            { "firstname", firstname },
            { "email", email },
            { "phone", phone },
            { "surl", surl },
            { "furl", furl },
            { "splitRequest", splitRequest },
            { "hash", hash }
        };

        // Send request
        using (var httpClient = new HttpClient())
        {
            using (var content = new FormUrlEncodedContent(formData))
            {
                HttpResponseMessage response = await httpClient.PostAsync("https://test.payu.in/_payment", content);
                string responseContent = await response.Content.ReadAsStringAsync();
                Console.WriteLine(responseContent);
            }
        }
    }
}
```

### JavaScript (Node.js)

```javascript
const crypto = require('crypto');
const axios = require('axios');

// Merchant details
const key = "YOUR_MERCHANT_KEY";
const salt = "YOUR_MERCHANT_SALT";
const txnid = `TXN_${Date.now()}`;
const amount = "1000";
const productinfo = "Product Description";
const firstname = "Customer Name";
const email = "customer@example.com";
const phone = "9999999999";
const surl = "https://yourwebsite.com/success";
const furl = "https://yourwebsite.com/failure";

// Split information
const splitRequest = JSON.stringify({
    type: "absolute",
    splitInfo: {
        MERCHANT_KEY_1: {
            aggregatorSubTxnId: "SUB_TXN_ID_1",
            aggregatorSubAmt: "600",
            aggregatorCharges: "50"
        },
        MERCHANT_KEY_2: {
            aggregatorSubTxnId: "SUB_TXN_ID_2",
            aggregatorSubAmt: "400"
        }
    }
});

// Generate hash
const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|||||||${salt}|${splitRequest}`;
const hash = crypto.createHash('sha512').update(hashString).digest('hex');

// Create form data
const formData = {
    key,
    txnid,
    amount,
    productinfo,
    firstname,
    email,
    phone,
    surl,
    furl,
    splitRequest,
    hash
};

// Send request
axios.post('https://test.payu.in/_payment', formData, {
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error('Error:', error);
});
```

## Security Considerations

### Hash Validation

Always validate the hash received in the response to ensure data integrity:

```php
<?php
$key = $_POST['key'];
$txnid = $_POST['txnid'];
$amount = $_POST['amount'];
$productinfo = $_POST['productinfo'];
$firstname = $_POST['firstname'];
$email = $_POST['email'];
$salt = "YOUR_MERCHANT_SALT";
$status = $_POST['status'];
$resphash = $_POST['hash'];

// Calculate hash
$hashString = "$salt|$status|||||||||$email|$firstname|$productinfo|$amount|$txnid|$key";
$calculatedHash = hash("sha512", $hashString);

if ($calculatedHash == $resphash) {
    // Hash is valid, proceed with order processing
    if ($status == "success") {
        // Payment successful
        // Update order status and process splits
    } else {
        // Payment failed
        // Handle failure
    }
} else {
    // Hash validation failed
    // Possible tampering detected
}
?>
```

### Split Amount Validation

Always ensure that the sum of all split amounts equals the total transaction amount:

```javascript
function validateSplitAmounts(splitInfo, totalAmount) {
    let sum = 0;
    
    // Calculate total from split amounts
    for (const merchantKey in splitInfo) {
        const merchantInfo = splitInfo[merchantKey];
        sum += parseFloat(merchantInfo.aggregatorSubAmt);
        
        if (merchantInfo.aggregatorCharges) {
            sum += parseFloat(merchantInfo.aggregatorCharges);
        }
    }
    
    // Compare with total amount
    return Math.abs(sum - parseFloat(totalAmount)) < 0.01;
}
```

## Error Handling

### Common Error Codes

| Error Code | Description                 | Resolution                            |
| ---------- | --------------------------- | ------------------------------------- |
| `E000`     | No Error                    | Transaction successful                |
| `E1001`    | Invalid hash                | Check hash calculation                |
| `E1002`    | Invalid parameters          | Verify all required parameters        |
| `E1003`    | Invalid merchant            | Verify merchant key                   |
| `E1004`    | Transaction not found       | Verify transaction ID                 |
| `E1007`    | Invalid split configuration | Check split amounts and merchant keys |

### Handling Split Failures

Even if the main payment succeeds, the split operation might fail. Always check the `splitInfo.splitStatus` field in the response:

```javascript
function handleResponse(response) {
    if (response.status === "success") {
        if (response.splitInfo && response.splitInfo.splitStatus === "success") {
            // Both payment and split successful
            console.log("Payment and split successful");
        } else {
            // Payment successful but split failed
            console.log("Payment successful but split failed");
            // Log split failure details
            console.log("Split status:", response.splitInfo?.splitStatus);
            console.log("Split errors:", response.splitInfo?.errors);
        }
    } else {
        // Payment failed
        console.log("Payment failed:", response.error_Message);
    }
}
```

## Testing

### Test Environment

Use the test environment for development and testing:

* **API URL**: `https://test.payu.in/_payment`
* **Test Cards**:
  * Visa: 4012001037141112
  * MasterCard: 5123456789012346
  * Test CVV: 123
  * Test Expiry: Any future date

### Test Child Merchants

In the test environment, you can use test merchant keys for child merchants:

* **Test Merchant Key 1**: `TEST_MERCHANT_KEY_1`
* **Test Merchant Key 2**: `TEST_MERCHANT_KEY_2`

## Going Live

### Production Environment

Switch to production when testing is complete:

* **API URL**: `https://secure.payu.in/_payment`

### Final Checklist

Before going live, ensure:

1. All child merchants are properly onboarded and verified
2. Split amount calculations are accurate and equal to the total transaction amount
3. Transaction verification is implemented
4. Error handling is in place for both payment and split failures
5. Security measures like hash validation are implemented
6. Production credentials are updated in all code

## Additional Resources

* [PayU Developer Documentation](https://docs.payu.in/)
* [Split Settlements API Reference](https://docs.payu.in/docs/api-integration-for-split-settlements)
* [Absolute Split During Transaction](https://docs.payu.in/reference/absolute-split-during-transaction/)
* [Payment Verification API](https://docs.payu.in/reference/get-transaction-details-api)
* [Error Codes Reference](https://docs.payu.in/docs/error-codes)

## Support

For technical support and integration assistance:

* **Email**: [integration@payu.in](mailto:integration@payu.in)
* **Documentation**: [docs.payu.in](https://docs.payu.in)
* **Developer Community**: [PayU Developer Forum](https://community.payu.in)

***

**Note**: This integration guide provides a comprehensive overview of implementing Absolute Split During Transaction with PayU. Always refer to the latest API documentation for the most up-to-date information and endpoints.