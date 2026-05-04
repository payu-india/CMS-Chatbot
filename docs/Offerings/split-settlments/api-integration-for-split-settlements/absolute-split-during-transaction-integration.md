---
title: Absolute Split During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Absolute Split During Transaction Integration
excerpt: >-
  Integrate split settlements using absolute amounts with the `_payment` API and
  confirm transaction outcome using webhooks.
deprecated: false
hidden: false
metadata:
  title: Absolute Split During Transaction Integration
  description: >-
    Learn how to integrate the `_payment` API for absolute split settlements,
    generate request hash, send splitRequest, and verify successful payment using
    webhook events.
  robots: index
next:
  description: ''
---

Use this integration to split a parent transaction into fixed amounts at payment time using the `_payment` API.

In an absolute split, each child merchant receives an exact amount (`aggregatorSubAmt`) that you define in advance.

## Prerequisites

Before you start, ensure the following:

1. Your parent merchant account is enabled for Split Settlements.
2. Child merchants are onboarded and available for split mapping.
3. You have your merchant `key` and `salt`.
4. You have server-side logic to generate hash and process webhooks.

## Step 1: Build splitRequest for absolute split

Create the `splitRequest` JSON with `type` as `absolute`.

```json
{
  "type": "absolute",
  "splitInfo": {
    "P41sCY": {
      "aggregatorSubTxnId": "subtxn-abs-001",
      "aggregatorSubAmt": "600.00",
      "aggregatorCharges": "50.00"
    },
    "P41sCK": {
      "aggregatorSubTxnId": "subtxn-abs-002",
      "aggregatorSubAmt": "350.00"
    }
  }
}
```

> **Important:** The total of all child split amounts plus parent charges must equal the transaction amount.

## Step 2: Generate request hash

Include `splitRequest` at the end of the hash sequence:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Example hash input string:

```plaintext
Ax4j7J|txn-abs-1001|1000.00|Order #1001|Aman|aman@example.com|||||||||||t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL|{"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-abs-001","aggregatorSubAmt":"600.00","aggregatorCharges":"50.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-abs-002","aggregatorSubAmt":"350.00"}}}
```

## Step 3: Submit payment request to `_payment`

Use the environment endpoint:

* Test: `https://test.payu.in/_payment`
* Production: `https://secure.payu.in/_payment`

Sample request:

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "txnid=txn-abs-1001" \
  -d "amount=1000.00" \
  -d "productinfo=Order #1001" \
  -d "firstname=Aman" \
  -d "email=aman@example.com" \
  -d "phone=9999999999" \
  -d "api_version=7" \
  -d "surl=https://merchant.example.com/payu/success" \
  -d "furl=https://merchant.example.com/payu/failure" \
  -d 'splitRequest={"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-abs-001","aggregatorSubAmt":"600.00","aggregatorCharges":"50.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-abs-002","aggregatorSubAmt":"350.00"}}}' \
  -d "hash=<generated_hash>"
```

## Step 4: Handle checkout response on success/failure URL

PayU posts response parameters to your `surl` or `furl`. Always validate reverse hash before updating order state.

Reverse hash format for split response:

```plaintext
sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

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
  "txnid": "payment-txnid-1",
  "amount": "10.00",
  "mihpayid": "403993715519672950",
  "error_code": "E000",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "P41sCY",
        "amount": 3,
        "txnId": "0e7411799c9f0e96620c11"
      },
      {
        "merchantKey": "P41sCK",
        "amount": 5,
        "txnId": "0e7411799c9f0e96620c22"
      }
    ]
  }
}

```

## Step 5: Verify final payment state using webhooks

Do not rely only on browser redirects. Use webhooks as the source of truth for final payment outcome.

1. Configure a webhook URL on PayU Dashboard.
2. Subscribe to payment status events relevant to your flow.
3. Validate webhook authenticity using your webhook signature validation logic.
4. Mark order as paid only when webhook confirms a successful captured transaction.
5. Persist `txnid`, `mihpayid`, status, and `splitInfo` for reconciliation.

### Sample webhook payload (illustrative)

```json
{
  "event": "payment.success",
  "txnid": "txn-abs-1001",
  "mihpayid": "403993715519672950",
  "status": "success",
  "amount": "1000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "P41sCY",
        "amount": 600,
        "txnId": "subtxn-abs-001"
      },
      {
        "merchantKey": "P41sCK",
        "amount": 350,
        "txnId": "subtxn-abs-002"
      }
    ]
  }
}
```

## [Optional] Check the Transaction Info

Always verify the transaction info using the Get Aggregator/Parent Transaction Info API to ensure data integrity. For more information, refer to [Get Aggregator/Parent Transaction Info API](ref:get_aggregator_parent_transaction_info_api).

**Sample request**

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "command=get_aggregator_transactions" \
  -d "var1=2024-01-15 10:00" \
  -d "var2=2024-01-15 23:59" \
  -d "var3=1" \
  -d "var4=100" \
  -d "var5=1" \
  -d "hash=586e3379b3d9f90682329cf7efd27273aeb290936d9edf98686370bc59fdc67b8c0a15c9b6d5c48a24f66a8834b4b75e7e1a9c8d2e3f4a5b6c7d8e9f0a1b2c3d4e5"

```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.net.URLEncoder;

public class PayUGetAggregatorTransactionInfo {
    public static void main(String[] args) throws Exception {
        // API parameters
        String key = "Ax4j7J";
        String salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        String command = "get_aggregator_transactions";
        String startDate = "2024-01-15 10:00"; // var1
        String endDate = "2024-01-15 23:59";   // var2
        String pageNumber = "1";               // var3
        String pageLimit = "100";              // var4
        String splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

        // Generate hash: sha512(key|command|var1|salt)
        String hashString = key + "|" + command + "|" + startDate + "|" + salt;
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        
        StringBuilder hexString = new StringBuilder();
        for (byte b : digest) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        String hash = hexString.toString();

        // Create form parameters
        Map<String, String> formParams = new HashMap<>();
        formParams.put("key", key);
        formParams.put("command", command);
        formParams.put("var1", startDate);
        formParams.put("var2", endDate);
        formParams.put("var3", pageNumber);
        formParams.put("var4", pageLimit);
        formParams.put("var5", splitFlag);
        formParams.put("hash", hash);

        // Convert to form-urlencoded format
        String formData = formParams.entrySet()
            .stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" + 
                     URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        // Create HTTP client and request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://info.payu.in/merchant/postservice?form=2"))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        // Send request and get response
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Response Status: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}

```
```php
<?php
// API parameters
$key = "Ax4j7J";
$salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
$command = "get_aggregator_transactions";
$startDate = "2024-01-15 10:00"; // var1
$endDate = "2024-01-15 23:59";   // var2
$pageNumber = "1";               // var3
$pageLimit = "100";              // var4
$splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

// Generate hash: sha512(key|command|var1|salt)
$hashString = "{$key}|{$command}|{$startDate}|{$salt}";
$hash = hash("sha512", $hashString);

// Create form data
$postData = [
    'key' => $key,
    'command' => $command,
    'var1' => $startDate,
    'var2' => $endDate,
    'var3' => $pageNumber,
    'var4' => $pageLimit,
    'var5' => $splitFlag,
    'hash' => $hash
];

// Initialize cURL session
$ch = curl_init("https://info.payu.in/merchant/postservice?form=2");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/x-www-form-urlencoded'
]);

// Execute request and get response
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Parse and display response
echo "HTTP Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

// Parse JSON response
$responseData = json_decode($response, true);
if ($responseData && $responseData['status'] == 1) {
    echo "Transaction fetch successful!\n";
    echo "Total transactions: " . count($responseData['Transaction_details']) . "\n";
} else {
    echo "Error: " . ($responseData['msg'] ?? 'Unknown error') . "\n";
}
?>

```
```javascript
const crypto = require('crypto');
const axios = require('axios');
const querystring = require('querystring');

// API parameters
const key = "Ax4j7J";
const salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
const command = "get_aggregator_transactions";
const startDate = "2024-01-15 10:00"; // var1
const endDate = "2024-01-15 23:59";   // var2
const pageNumber = "1";               // var3
const pageLimit = "100";              // var4
const splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

// Generate hash: sha512(key|command|var1|salt)
const hashString = `${key}|${command}|${startDate}|${salt}`;
const hash = crypto.createHash('sha512').update(hashString).digest('hex');

// Create form data
const formData = {
  key,
  command,
  var1: startDate,
  var2: endDate,
  var3: pageNumber,
  var4: pageLimit,
  var5: splitFlag,
  hash
};

// Make the API request
async function getAggregatorTransactionInfo() {
  try {
    const response = await axios.post(
      'https://info.payu.in/merchant/postservice?form=2',
      querystring.stringify(formData),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }
    );
    
    console.log('Status Code:', response.status);
    console.log('Response:', JSON.stringify(response.data, null, 2));
    
    if (response.data.status === 1) {
      console.log('Transaction fetch successful!');
      console.log('Total transactions:', response.data.Transaction_details.length);
      
      // Display transaction details
      response.data.Transaction_details.forEach((transaction, index) => {
        console.log(`\nTransaction ${index + 1}:`);
        console.log(`  ID: ${transaction.id}`);
        console.log(`  Status: ${transaction.status}`);
        console.log(`  Amount: ${transaction.amount}`);
        console.log(`  TxnID: ${transaction.txnid}`);
        console.log(`  Is Parent: ${transaction.is_parent_transaction}`);
        
        if (transaction.splitInfo && transaction.splitInfo.length > 0) {
          console.log(`  Split Info:`);
          transaction.splitInfo.forEach((split, splitIndex) => {
            console.log(`    Split ${splitIndex + 1}: ${split.amount} to ${split.key}`);
          });
        }
      });
    } else {
      console.log('Error:', response.data.msg);
    }
    
    return response.data;
  } catch (error) {
    console.error('Error making request:', error.message);
    if (error.response) {
      console.error('Response status:', error.response.status);
      console.error('Response data:', error.response.data);
    }
    throw error;
  }
}

// Execute the request
getAggregatorTransactionInfo()
  .then(data => console.log('API call successful'))
  .catch(err => console.error('API call failed'));

```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class PayUGetAggregatorTransactionInfo
{
    static async Task Main(string[] args)
    {
        // API parameters
        string key = "Ax4j7J";
        string salt = "t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL";
        string command = "get_aggregator_transactions";
        string startDate = "2024-01-15 10:00"; // var1
        string endDate = "2024-01-15 23:59";   // var2
        string pageNumber = "1";               // var3
        string pageLimit = "100";              // var4
        string splitFlag = "1";                // var5 (1 = split created, 0 = split not created)

        // Generate hash: sha512(key|command|var1|salt)
        string hashString = $"{key}|{command}|{startDate}|{salt}";
        string hash = ComputeSHA512Hash(hashString);

        // Create form data
        var formData = new Dictionary<string, string>
        {
            ["key"] = key,
            ["command"] = command,
            ["var1"] = startDate,
            ["var2"] = endDate,
            ["var3"] = pageNumber,
            ["var4"] = pageLimit,
            ["var5"] = splitFlag,
            ["hash"] = hash
        };

        await SendRequest(formData);
    }

    static string ComputeSHA512Hash(string input)
    {
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            byte[] hashBytes = sha512.ComputeHash(inputBytes);

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hashBytes.Length; i++)
            {
                sb.Append(hashBytes[i].ToString("x2"));
            }
            return sb.ToString();
        }
    }

    static async Task SendRequest(Dictionary<string, string> formData)
    {
        try
        {
            using (HttpClient client = new HttpClient())
            {
                var content = new FormUrlEncodedContent(formData);

                HttpResponseMessage response = await client.PostAsync(
                    "https://info.payu.in/merchant/postservice?form=2", 
                    content
                );
                
                string responseContent = await response.Content.ReadAsStringAsync();
                
                Console.WriteLine($"Status Code: {response.StatusCode}");
                Console.WriteLine($"Response: {responseContent}");

                // Parse JSON response
                try
                {
                    var jsonDoc = JsonDocument.Parse(responseContent);
                    var root = jsonDoc.RootElement;
                    
                    if (root.TryGetProperty("status", out var status) && status.GetInt32() == 1)
                    {
                        Console.WriteLine("Transaction fetch successful!");
                        
                        if (root.TryGetProperty("Transaction_details", out var transactions))
                        {
                            Console.WriteLine($"Total transactions: {transactions.GetArrayLength()}");
                        }
                    }
                    else
                    {
                        if (root.TryGetProperty("msg", out var msg))
                        {
                            Console.WriteLine($"Error: {msg.GetString()}");
                        }
                    }
                }
                catch (JsonException ex)
                {
                    Console.WriteLine($"JSON parsing error: {ex.Message}");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

**Sample response**

```
{
  "status": 1,
  "msg": "Transaction Fetched Successfully",
  "Transaction_details": [
    {
      "id": "412345678912384148",
      "status": "captured",
      "key": "Ax4j7J",
      "merchantname": "Aggregator-Parent",
      "txnid": "payment-txnid-1",
      "base_id": null,
      "firstname": "Payu-Admin",
      "lastname": "",
      "addedon": "2024-01-15 10:11:08",
      "bank_name": "Credit Cards",
      "payment_gateway": "AxisCYBER",
      "phone": "1234567890",
      "email": "test@example.com",
      "transaction_fee": "10.00",
      "amount": "10.00",
      "discount": "0.00",
      "additional_charges": "0.00",
      "productinfo": "Product Info",
      "error_code": "E000",
      "bank_ref_no": "5192296867061049177385",
      "ibibo_code": "CC",
      "mode": "CC",
      "is_parent_transaction": true,
      "splitInfo": [
        {
          "id": "412345678912384152",
          "status": "captured",
          "merchantId": "39032915",
          "key": "P41sCY",
          "txnid": "0e7411799c9f0e96620c11",
          "transaction_fee": "3.00",
          "amount": "3.00",
          "aggregatorCharges": "2.00"
        },
        {
          "id": "412345678912384153",
          "status": "captured",
          "merchantId": "39032916",
          "key": "P41sCK",
          "txnid": "0e7411799c9f0e96620c22",
          "transaction_fee": "5.00",
          "amount": "5.00"
        }
      ]
    }
  ]
}

```

## Go-live checklist

* Use unique `txnid` and unique `aggregatorSubTxnId` values.
* Keep `splitRequest` JSON compact and deterministic before hashing.
* Confirm reverse-hash validation on redirect response.
* Confirm webhook delivery, signature verification, and idempotent processing.
* Switch endpoint from test to production only after successful end-to-end tests.
