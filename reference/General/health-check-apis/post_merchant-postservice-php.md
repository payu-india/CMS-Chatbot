---
api:
  file: getpaymentgatewayupstatus_api_postman_collection_updated.json
  operationId: post_merchant-postservice-php
hidden: true
---
The **Get Payment Gateway Up Status** API allows you to check the real-time availability of payment options (Net Banking, Wallets, UPI) before displaying them to customers. This helps improve checkout experience by hiding unavailable payment methods.

> **Note:** This API replaces the [Get Net Banking Status API](https://docs.payu.in/reference/get_net_banking_status_api). PayU strongly recommends you to migrate to this endpoint for continued support.

## Key Features

* **Check specific payment options individually:** You can check the status of a wallet, a specific Net Banking provider, or UPI by passing the relevant code in the `var1` parameter. For example:
  - For a specific bank like Axis, pass `var1=AXIB`
  - For UPI, pass `var1=UPI`
  - For a wallet like PhonePe, pass `var1=PHONEPE`
  - For all payment options at once, pass `var1=default`
  
  The hash calculation changes accordingly since `var1` is part of the hash sequence. There's no separate parameter to filter by mode.

* **Gateway-level health monitoring:** PayU routes payments through multiple backend payment gateways. For any given payment option (for example, Axis Net Banking), there might be 2-3 gateways handling it. The API checks if **at least one gateway is working**:
  - `up_status = 1`: At least one gateway is operational
  - `up_status = 0`: All gateways are down
  - `up_status = 3`: The option is available but performing poorly (low success rate). This status only appears if you explicitly pass `var2=1` in the request; otherwise, you'll only see `0` or `1`.

---

**POST /merchant/postservice.php**
### Environment
<Info>
**Test Environment:**
```
https://test.payu.in/merchant/postservice.php?form=2
```

**Production Environment:**
```
https://info.payu.in/merchant/postservice.php?form=2
```

Remember to use your production merchant key and salt when making requests to the production endpoint.
</Info>


<Accordion title="Request Parameters" icon="fa-table">
<div>
  <table>
    <thead>
      <tr>
        <th style="width: 10%;">Parameter</th>
        <th style="width: 75%; white-space: normal; word-break: break-word;">Type & Description</th>
        <th style="width: 15%;">Example</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          key<br>
          <code>mandatory</code>
        </td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> Your merchant key provided by PayU. This identifies your merchant account.
        </td>
        <td>vqpS7W</td>
      </tr>
      <tr>
        <td>
          command<br>
          <code>mandatory</code>
        </td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> The API command identifier. Must be set to <code>getNetbankingStatus</code> for this endpoint.
        </td>
        <td>getNetbankingStatus</td>
      </tr>
      <tr>
        <td>
          var1<br>
          <code>mandatory</code>
        </td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> The payment option code to check. Use <code>default</code> to retrieve all payment options, or specify a bank code (e.g., <code>AXIB</code>, <code>SBIB</code>), wallet code (e.g., <code>PHONEPE</code>, <code>OLAM</code>), or <code>UPI</code> for UPI payments.
        </td>
        <td>default</td>
      </tr>
      <tr>
        <td>
          hash<br>
          <code>mandatory</code>
        </td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> SHA-512 hash for request authentication. Formula: <code>sha512(key|command|var1|salt)</code>. The hash must be computed server-side and passed as lowercase hexadecimal. See <a href="#hash-generation">Hash Generation</a> section below.
        </td>
        <td>5d96e2c5a7...</td>
      </tr>
      <tr>
        <td>
          var2<br>
          <code>optional</code>
        </td>
        <td style="white-space: normal; word-break: break-word;">
          <code>Integer</code> Set to <code>1</code> to include performance status in the response. When enabled, the API will return <code>up_status=3</code> for payment options with low success rates. Default is <code>0</code>.
        </td>
        <td>1</td>
      </tr>
    </tbody>
  </table>
</div>
</Accordion>
### Hash Generation

The hash parameter is required to authenticate your request. It must be generated server-side using the SHA-512 algorithm.

**Hash Sequence:**
```
sha512(key|command|var1|salt)
```

**Important Notes:**
- Use the pipe character (`|`) as a separator between values
- The hash must be in lowercase hexadecimal format
- Never expose your salt in client-side code

**Sample Hash Generation Code:**

```javascript
// Node.js example
const crypto = require('crypto');

const key = 'vqpS7W';
const command = 'getNetbankingStatus';
const var1 = 'default';
const salt = 'rF1d43OgVcGCVctqAFTG6QiTCB9UXiyg';

const hashString = `${key}|${command}|${var1}|${salt}`;
const hash = crypto.createHash('sha512').update(hashString).digest('hex');

console.log(hash);
```

---

### Request Examples

<Accordion title="Check All Payment Options (default)" icon="fa-list">

**Request**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vqpS7W' \
--data-urlencode 'command=getNetbankingStatus' \
--data-urlencode 'var1=default' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```

**Sample Response**

```json
{
  "status": 1,
  "msg": "Success",
  "result": {
    "AXIB": {
      "up_status": "1",
      "title": "Axis Bank"
    },
    "SBIB": {
      "up_status": "1",
      "title": "State Bank of India"
    },
    "UPI": {
      "up_status": "1",
      "title": "UPI"
    },
    "PHONEPE": {
      "up_status": "1",
      "title": "PhonePe Wallet"
    }
  }
}
```

</Accordion>

<Accordion title="Check Specific Net Banking Option" icon="fa-building-columns">

**Request**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vqpS7W' \
--data-urlencode 'command=getNetbankingStatus' \
--data-urlencode 'var1=SBIB' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```

> **Note:** When checking a specific option, ensure you recalculate the hash using the specific `var1` value (e.g., `SBIB`), not `default`.

**Sample Response**

```json
{
  "status": 1,
  "msg": "Success",
  "result": {
    "SBIB": {
      "up_status": "1",
      "title": "State Bank of India"
    }
  }
}
```

</Accordion>

<Accordion title="Check UPI Status" icon="fa-mobile">

**Request**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vqpS7W' \
--data-urlencode 'command=getNetbankingStatus' \
--data-urlencode 'var1=UPI' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```

**Sample Response**

```json
{
  "status": 1,
  "msg": "Success",
  "result": {
    "UPI": {
      "up_status": "1",
      "title": "UPI"
    }
  }
}
```

</Accordion>

<Accordion title="Check Wallet Status" icon="fa-wallet">

**Request**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vqpS7W' \
--data-urlencode 'command=getNetbankingStatus' \
--data-urlencode 'var1=OLAM' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```

**Sample Response**

```json
{
  "status": 1,
  "msg": "Success",
  "result": {
    "OLAM": {
      "up_status": "1",
      "title": "Ola Money Wallet"
    }
  }
}
```

</Accordion>

<Accordion title="Check with Performance Status (var2=1)" icon="fa-chart-line">

**Request**

```bash
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=vqpS7W' \
--data-urlencode 'command=getNetbankingStatus' \
--data-urlencode 'var1=default' \
--data-urlencode 'var2=1' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```

> **Note:** When using `var2=1`, recalculate the hash using the sequence: `sha512(key|command|var1|var2|salt)`

**Sample Response**

```json
{
  "status": 1,
  "msg": "Success",
  "result": {
    "AXIB": {
      "up_status": "1",
      "title": "Axis Bank"
    },
    "SBIB": {
      "up_status": "3",
      "title": "State Bank of India"
    },
    "UPI": {
      "up_status": "1",
      "title": "UPI"
    },
    "PHONEPE": {
      "up_status": "0",
      "title": "PhonePe Wallet"
    }
  }
}
```

In this example:
- `AXIB` and `UPI` are fully operational (`up_status=1`)
- `SBIB` is available but has low success rate (`up_status=3`)
- `PHONEPE` is currently unavailable (`up_status=0`)

</Accordion>

---

### Response Schema

<div>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Field</th>
        <th style="width: 70%; white-space: normal; word-break: break-word;">Type & Description</th>
        <th style="width: 15%;">Example</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>status</td>
        <td style="white-space: normal; word-break: break-word;">
          <code>Integer</code> API call status. <code>1</code> = Success, <code>0</code> = Failure
        </td>
        <td>1</td>
      </tr>
      <tr>
        <td>msg</td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> Status message describing the API response
        </td>
        <td>Success</td>
      </tr>
      <tr>
        <td>result</td>
        <td style="white-space: normal; word-break: break-word;">
          <code>Object</code> Contains payment option codes as keys, each with nested <code>up_status</code> and <code>title</code> fields
        </td>
        <td>{ "AXIB": {...} }</td>
      </tr>
      <tr>
        <td>result.[code].up_status</td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> Availability status of the payment option. <code>"1"</code> = Available, <code>"0"</code> = Down, <code>"3"</code> = Available but low performance (only when <code>var2=1</code>)
        </td>
        <td>"1"</td>
      </tr>
      <tr>
        <td>result.[code].title</td>
        <td style="white-space: normal; word-break: break-word;">
          <code>String</code> Display name of the payment option
        </td>
        <td>Axis Bank</td>
      </tr>
    </tbody>
  </table>
</div>

---

### Common Payment Option Codes

<Accordion title="Net Banking Bank Codes" icon="fa-building-columns">

| Code | Bank Name |
|------|-----------|
| AXIB | Axis Bank |
| SBIB | State Bank of India |
| HDFB | HDFC Bank |
| ICIB | ICICI Bank |
| PUNB | Punjab National Bank |
| BBCB | Bank of Baroda Corporate |
| INDB | IndusInd Bank |
| KKBK | Kotak Mahindra Bank |
| YESB | Yes Bank |

> **Note:** For a complete list of bank codes, refer to your PayU merchant dashboard or contact PayU support.

</Accordion>

<Accordion title="Wallet Codes" icon="fa-wallet">

| Code | Wallet Name |
|------|-------------|
| PHONEPE | PhonePe |
| PAYTM | Paytm |
| OLAM | Ola Money |
| FREECHARGE | FreeCharge |
| MOBIKWIK | MobiKwik |
| AMAZON_PAY | Amazon Pay |

</Accordion>

<Accordion title="UPI Codes" icon="fa-mobile">

| Code | Description |
|------|-------------|
| UPI | UPI Collect (VPA-based) |
| INTENT | UPI Intent (App-based) |

</Accordion>

---

### Error Codes

<div>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Error Code</th>
        <th style="width: 70%; white-space: normal; word-break: break-word;">Description & Action</th>
        <th style="width: 15%;">HTTP Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>INVALID_HASH</td>
        <td style="white-space: normal; word-break: break-word;">
          Hash validation failed. Verify that you are using the correct salt and hash sequence. Ensure hash is lowercase hexadecimal.
        </td>
        <td>200</td>
      </tr>
      <tr>
        <td>INVALID_KEY</td>
        <td style="white-space: normal; word-break: break-word;">
          Merchant key is invalid or inactive. Verify your merchant key from the PayU dashboard.
        </td>
        <td>200</td>
      </tr>
      <tr>
        <td>MISSING_PARAMETER</td>
        <td style="white-space: normal; word-break: break-word;">
          One or more required parameters are missing. Ensure <code>key</code>, <code>command</code>, <code>var1</code>, and <code>hash</code> are all provided.
        </td>
        <td>200</td>
      </tr>
      <tr>
        <td>INVALID_COMMAND</td>
        <td style="white-space: normal; word-break: break-word;">
          The <code>command</code> parameter must be <code>getNetbankingStatus</code>.
        </td>
        <td>200</td>
      </tr>
    </tbody>
  </table>
</div>

---

### Code Examples in Multiple Languages

<Accordion title="Python" icon="fa-code">

```python
import hashlib
import requests

# Merchant credentials
key = 'vqpS7W'
salt = 'rF1d43OgVcGCVctqAFTG6QiTCB9UXiyg'
command = 'getNetbankingStatus'
var1 = 'default'  # or specific code like 'AXIB', 'UPI', 'PHONEPE'

# Generate hash
hash_string = f"{key}|{command}|{var1}|{salt}"
hash_value = hashlib.sha512(hash_string.encode()).hexdigest()

# API request
url = 'https://test.payu.in/merchant/postservice.php?form=2'
payload = {
    'key': key,
    'command': command,
    'var1': var1,
    'hash': hash_value
}

response = requests.post(url, data=payload)
print(response.json())
```

</Accordion>

<Accordion title="PHP" icon="fa-code">

```php
<?php
// Merchant credentials
$key = 'vqpS7W';
$salt = 'rF1d43OgVcGCVctqAFTG6QiTCB9UXiyg';
$command = 'getNetbankingStatus';
$var1 = 'default'; // or specific code like 'AXIB', 'UPI', 'PHONEPE'

// Generate hash
$hashString = $key . '|' . $command . '|' . $var1 . '|' . $salt;
$hash = hash('sha512', $hashString);

// API request
$url = 'https://test.payu.in/merchant/postservice.php?form=2';
$postData = array(
    'key' => $key,
    'command' => $command,
    'var1' => $var1,
    'hash' => $hash
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

</Accordion>

<Accordion title="Java" icon="fa-code">

```java
import java.io.*;
import java.net.*;
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;

public class PayUGatewayStatus {
    public static void main(String[] args) throws Exception {
        // Merchant credentials
        String key = "vqpS7W";
        String salt = "rF1d43OgVcGCVctqAFTG6QiTCB9UXiyg";
        String command = "getNetbankingStatus";
        String var1 = "default"; // or specific code like "AXIB", "UPI", "PHONEPE"
        
        // Generate hash
        String hashString = key + "|" + command + "|" + var1 + "|" + salt;
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        StringBuilder hash = new StringBuilder();
        for (byte b : hashBytes) {
            hash.append(String.format("%02x", b));
        }
        
        // API request
        String url = "https://test.payu.in/merchant/postservice.php?form=2";
        String postData = "key=" + URLEncoder.encode(key, "UTF-8") +
                         "&command=" + URLEncoder.encode(command, "UTF-8") +
                         "&var1=" + URLEncoder.encode(var1, "UTF-8") +
                         "&hash=" + URLEncoder.encode(hash.toString(), "UTF-8");
        
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.getOutputStream().write(postData.getBytes(StandardCharsets.UTF_8));
        
        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String response = in.readLine();
        in.close();
        
        System.out.println(response);
    }
}
```

</Accordion>

---

### Best Practices

<Warning>
**Security Best Practices:**
- Never expose your salt in client-side code or version control
- Always generate the hash server-side
- Use HTTPS for all API requests
- Rotate your salt periodically and update your hash generation accordingly
</Warning>

<Success>
**Integration Tips:**
- Call this API before displaying payment options on your checkout page to hide unavailable methods
- Cache the response for 2-5 minutes to reduce API calls while maintaining freshness
- Implement fallback logic: if the API call fails, display all payment options rather than none
- Use `var1=default` during checkout initialization, then filter client-side based on customer preference
- For mission-critical transactions, check specific payment methods using their codes (e.g., `var1=UPI`) before final submission
</Success>

---

## Postman Collection

Download the complete Postman collection for this API:

📮 **[Download Postman Collection](attachment:getpaymentgatewayupstatus_api_postman_collection_updated.json)**

The collection includes pre-configured requests for:
- Checking all payment options (default)
- Checking specific Net Banking providers
- Checking wallet status
- Checking UPI status
- Checking UPI Intent status