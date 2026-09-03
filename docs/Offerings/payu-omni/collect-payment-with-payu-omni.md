---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
This section walks you through integrating the Collect Payment API to push payment requests from your billing system to PayU-enabled devices (Android POS, All-in-One, or DBQR Display).

<Note>
**Prerequisites**

Before you begin, ensure you have:
- ✅ A PayU merchant account with Omni product enabled
- ✅ Partner credentials (`clientId`, `clientSecret`, Partner UUID)
- ✅ At least one registered PayU device (POS terminal or DBQR display)
- ✅ Device ID(s) from your PayU account dashboard
- ✅ OAuth token obtained from PayU Token API (⚠️ Info Gap: Token API endpoint not documented — contact PayU support)
- ✅ A server capable of receiving webhooks (publicly accessible HTTPS endpoint)
</Note>

---

## Step 1: Start Integration

### Step 1.1: Prepare the Request Parameters

The Initiate Payment API requires both request headers and a JSON body with order details.

<Accordion title="Request Headers" icon="fa-list">

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `Content-Type` | String | Must be `application/json` | `application/json` |
| `X-Partner-Token` | String | Bearer OAuth token obtained from PayU token API | `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |
| `X-PayU-Reseller-UUID` | String | Partner UUID provided by PayU during onboarding | `550e8400-e29b-41d4-a716-446655440000` |
| `date` | String | Current request date and time in GMT format (RFC 7231) | `Tue, 15 Nov 2023 08:12:31 GMT` |
| `authorization` | String | HMAC-SHA512 signature header. Format: `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex-signature>"` | `hmac username="your_client_id", algorithm="sha512", headers="date", signature="a1b2c3..."` |

</Accordion>

<Accordion title="Request Body - Mandatory Parameters" icon="fa-list">

<table>
  <thead>
    <tr>
      <th style="text-align:left">Parameter</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
      <th style="text-align:left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>accountId</code></td>
      <td>String</td>
      <td>Merchant account identifier provided by PayU</td>
      <td><code>merchant_12345</code></td>
    </tr>
    <tr>
      <td><code>txnId</code></td>
      <td>String</td>
      <td>Unique transaction ID from your billing system. Must be alphanumeric and unique per transaction.</td>
      <td><code>ORD_20231115_001</code></td>
    </tr>
    <tr>
      <td><code>amount</code></td>
      <td>Double</td>
      <td>Transaction amount with exactly 2 decimal places</td>
      <td><code>1500.00</code></td>
    </tr>
    <tr>
      <td><code>currency</code></td>
      <td>String</td>
      <td>ISO 4217 currency code</td>
      <td><code>INR</code></td>
    </tr>
    <tr>
      <td><code>paymentSource</code></td>
      <td>String</td>
      <td>For POS/Omni integrations, use <code>WEB</code></td>
      <td><code>WEB</code></td>
    </tr>
    <tr>
      <td><code>paymentMethod</code></td>
      <td>Object</td>
      <td>Payment method details. For Omni/POS, use <code>{"name":"POS", "bankCode":"POS"}</code></td>
      <td><code>{"name":"POS", "bankCode":"POS"}</code></td>
    </tr>
    <tr>
      <td><code>paymentMethod.name</code></td>
      <td>String</td>
      <td>Payment method name. Use <code>POS</code> for Omni devices</td>
      <td><code>POS</code></td>
    </tr>
    <tr>
      <td><code>paymentMethod.bankCode</code></td>
      <td>String</td>
      <td>Bank/PG code. Use <code>POS</code> for Omni devices</td>
      <td><code>POS</code></td>
    </tr>
    <tr>
      <td><code>additionalInfo</code></td>
      <td>Object</td>
      <td>Contains transaction flow configuration</td>
      <td><code>{"txnFlow":"seamless", "txnS2sFlow":"4"}</code></td>
    </tr>
    <tr>
      <td><code>additionalInfo.txnFlow</code></td>
      <td>String</td>
      <td>Transaction flow type. Use <code>seamless</code> for integrated flow</td>
      <td><code>seamless</code></td>
    </tr>
    <tr>
      <td><code>additionalInfo.txnS2sFlow</code></td>
      <td>String</td>
      <td>Server-to-server flow identifier. Use <code>4</code> for Omni</td>
      <td><code>4</code></td>
    </tr>
    <tr>
      <td><code>callBackActions</code></td>
      <td>Object</td>
      <td>Webhook URLs for transaction callbacks</td>
      <td><code>{"successAction":"https://yoursite.com/success"}</code></td>
    </tr>
    <tr>
      <td><code>callBackActions.successAction</code></td>
      <td>String (URL)</td>
      <td>URL to receive success webhook notifications</td>
      <td><code>https://yoursite.com/webhook/success</code></td>
    </tr>
    <tr>
      <td><code>order</code></td>
      <td>Object</td>
      <td>Order details including product info and pricing</td>
      <td><code>{"productInfo":"Product Name", "paymentChargeSpecification":{"price":1500.00}}</code></td>
    </tr>
    <tr>
      <td><code>order.productInfo</code></td>
      <td>String</td>
      <td>Product or service description</td>
      <td><code>Coffee and Pastry</code></td>
    </tr>
    <tr>
      <td><code>order.paymentChargeSpecification</code></td>
      <td>Object</td>
      <td>Payment charge details</td>
      <td><code>{"price":1500.00}</code></td>
    </tr>
    <tr>
      <td><code>order.paymentChargeSpecification.price</code></td>
      <td>Double</td>
      <td>Order price (should match top-level amount)</td>
      <td><code>1500.00</code></td>
    </tr>
    <tr>
      <td><code>omniChannelDetails</code></td>
      <td>Object</td>
      <td>Omni device and payment method configuration</td>
      <td><code>{"posDeviceId":"DEVICE_12345", "posPaymentMethod":"sale"}</code></td>
    </tr>
    <tr>
      <td><code>omniChannelDetails.posDeviceId</code></td>
      <td>String</td>
      <td>Unique device ID of the POS terminal or DBQR display where payment should be accepted</td>
      <td><code>DEVICE_POS_12345</code></td>
    </tr>
    <tr>
      <td><code>omniChannelDetails.posPaymentMethod</code></td>
      <td>String</td>
      <td>Payment method to activate on device. Use <code>sale</code> for card payments, <code>qr</code> for DBQR/UPI. If omitted, device may show all options</td>
      <td><code>sale</code></td>
    </tr>
  </tbody>
</table>

</Accordion>

<Accordion title="Request Body - Optional Parameters" icon="fa-list">

<table>
  <thead>
    <tr>
      <th style="text-align:left">Parameter</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
      <th style="text-align:left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>callBackActions.failureAction</code></td>
      <td>String (URL)</td>
      <td>URL to receive failure webhook notifications</td>
      <td><code>https://yoursite.com/webhook/failure</code></td>
    </tr>
    <tr>
      <td><code>callBackActions.cancelAction</code></td>
      <td>String (URL)</td>
      <td>URL to receive cancel webhook notifications</td>
      <td><code>https://yoursite.com/webhook/cancel</code></td>
    </tr>
    <tr>
      <td><code>gstParams</code></td>
      <td>Object</td>
      <td>GST invoice parameters for GST-compliant receipts</td>
      <td><code>{"gstIn":"29ABCDE1234F1Z5", "gst":"18.00"}</code></td>
    </tr>
    <tr>
      <td><code>gstParams.gstIn</code></td>
      <td>String</td>
      <td>Merchant GSTIN number</td>
      <td><code>29ABCDE1234F1Z5</code></td>
    </tr>
    <tr>
      <td><code>gstParams.gst</code></td>
      <td>String</td>
      <td>Total GST amount</td>
      <td><code>18.00</code></td>
    </tr>
    <tr>
      <td><code>gstParams.cgst</code></td>
      <td>String</td>
      <td>Central GST amount</td>
      <td><code>9.00</code></td>
    </tr>
    <tr>
      <td><code>gstParams.sgst</code></td>
      <td>String</td>
      <td>State GST amount</td>
      <td><code>9.00</code></td>
    </tr>
    <tr>
      <td><code>gstParams.igst</code></td>
      <td>String</td>
      <td>Integrated GST amount (for inter-state transactions)</td>
      <td><code>18.00</code></td>
    </tr>
    <tr>
      <td><code>gstParams.cess</code></td>
      <td>String</td>
      <td>GST Cess amount if applicable</td>
      <td><code>1.00</code></td>
    </tr>
    <tr>
      <td><code>printInfo</code></td>
      <td>Object</td>
      <td>Custom fields to print on receipt</td>
      <td><code>{"field1":"Table 5", "field2":"Server: John"}</code></td>
    </tr>
    <tr>
      <td><code>field1</code> through <code>field9</code></td>
      <td>String</td>
      <td>Custom data fields (UDFs) for reporting and receipts. Can store values like table number, customer name, salesperson ID, etc.</td>
      <td><code>Table 5</code></td>
    </tr>
  </tbody>
</table>

</Accordion>

---

### Step 1.2: Generate HMAC Authorization

The `authorization` header requires an HMAC-SHA512 signature computed using your partner credentials.

<Accordion title="How to Generate HMAC Signature" icon="fa-key">

**Signature Components:**
- **Username:** Your partner `clientId`
- **Algorithm:** `sha512`
- **Headers:** `date` (the value from the `date` header)
- **Secret:** Your partner `clientSecret`

**Steps to Generate:**

1. Extract the current GMT date in RFC 7231 format
2. Create the signing string: the exact value of the `date` header
3. Compute HMAC-SHA512 of the signing string using your `clientSecret`
4. Convert the result to lowercase hexadecimal
5. Format the authorization header as: `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex-signature>"`

**Sample Code:**

```python
import hashlib
import hmac
from email.utils import formatdate

# Your credentials
client_id = "payu_client_id"
client_secret = "payu_client_secret"

# Generate GMT date
date_header = formatdate(timeval=None, localtime=False, usegmt=True)

# Create HMAC signature
signing_string = date_header
signature = hmac.new(
    client_secret.encode('utf-8'),
    signing_string.encode('utf-8'),
    hashlib.sha512
).hexdigest()

# Build authorization header
authorization_header = f'hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"'

print(f"date: {date_header}")
print(f"authorization: {authorization_header}")
```

```javascript
const crypto = require('crypto');

// Your credentials
const clientId = "payu_client_id";
const clientSecret = "payu_client_secret";

// Generate GMT date
const dateHeader = new Date().toUTCString();

// Create HMAC signature
const signature = crypto
  .createHmac('sha512', clientSecret)
  .update(dateHeader)
  .digest('hex');

// Build authorization header
const authorizationHeader = `hmac username="${clientId}", algorithm="sha512", headers="date", signature="${signature}"`;

console.log(`date: ${dateHeader}`);
console.log(`authorization: ${authorizationHeader}`);
```

<Warning>
⚠️ **Security Notes:**
- Never hardcode credentials in client-side code
- Compute HMAC signature server-side only
- The `date` header value must exactly match the value used in the HMAC computation (including format and timezone)
- Signatures expire quickly — generate fresh signatures for each request
</Warning>

</Accordion>

---

### Step 1.3: POST the Payment Request

Once you have prepared all parameters and generated the HMAC signature, POST the request to the Initiate Payment endpoint.

<Accordion title="Sample Request - cURL" icon="fa-code">

```bash
curl --location 'https://api.payu.in/partner/initiatePayment' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
--header 'X-PayU-Reseller-UUID: 550e8400-e29b-41d4-a716-446655440000' \
--header 'date: Tue, 15 Nov 2023 08:12:31 GMT' \
--header 'authorization: hmac username="payu_client_id", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."' \
--data '{
  "accountId": "merchant_12345",
  "txnId": "ORD_20231115_001",
  "amount": 1500.00,
  "currency": "INR",
  "paymentSource": "WEB",
  "paymentMethod": {
    "name": "POS",
    "bankCode": "POS"
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "txnS2sFlow": "4"
  },
  "callBackActions": {
    "successAction": "https://yoursite.com/webhook/success",
    "failureAction": "https://yoursite.com/webhook/failure"
  },
  "order": {
    "productInfo": "Coffee and Pastry",
    "paymentChargeSpecification": {
      "price": 1500.00
    }
  },
  "omniChannelDetails": {
    "posDeviceId": "DEVICE_POS_12345",
    "posPaymentMethod": "sale"
  },
  "gstParams": {
    "gstIn": "29ABCDE1234F1Z5",
    "gst": "18.00",
    "cgst": "9.00",
    "sgst": "9.00"
  },
  "printInfo": {
    "field1": "Table 5",
    "field2": "Server: John"
  }
}'
```

> **Note:** Replace all placeholder values (`X-Partner-Token`, `X-PayU-Reseller-UUID`, `date`, `authorization`, `accountId`, `posDeviceId`) with your actual credentials and device details before use.

</Accordion>

<Accordion title="Sample Request - Python" icon="fa-code">

```python
import requests
import json

url = "https://api.payu.in/partner/initiatePayment"

headers = {
    "Content-Type": "application/json",
    "X-Partner-Token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-PayU-Reseller-UUID": "550e8400-e29b-41d4-a716-446655440000",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": "hmac username=\"payu_client_id\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
}

payload = {
    "accountId": "merchant_12345",
    "txnId": "ORD_20231115_001",
    "amount": 1500.00,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "POS",
        "bankCode": "POS"
    },
    "additionalInfo": {
        "txnFlow": "seamless",
        "txnS2sFlow": "4"
    },
    "callBackActions": {
        "successAction": "https://yoursite.com/webhook/success",
        "failureAction": "https://yoursite.com/webhook/failure"
    },
    "order": {
        "productInfo": "Coffee and Pastry",
        "paymentChargeSpecification": {
            "price": 1500.00
        }
    },
    "omniChannelDetails": {
        "posDeviceId": "DEVICE_POS_12345",
        "posPaymentMethod": "sale"
    },
    "gstParams": {
        "gstIn": "29ABCDE1234F1Z5",
        "gst": "18.00",
        "cgst": "9.00",
        "sgst": "9.00"
    },
    "printInfo": {
        "field1": "Table 5",
        "field2": "Server: John"
    }
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {str(e)}")
```

</Accordion>

<Accordion title="Sample Request - PHP" icon="fa-code">

```php
<?php
$url = "https://api.payu.in/partner/initiatePayment";

$headers = [
    "Content-Type: application/json",
    "X-Partner-Token: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-PayU-Reseller-UUID: 550e8400-e29b-41d4-a716-446655440000",
    "date: Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization: hmac username=\"payu_client_id\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
];

$payload = json_encode([
    "accountId" => "merchant_12345",
    "txnId" => "ORD_20231115_001",
    "amount" => 1500.00,
    "currency" => "INR",
    "paymentSource" => "WEB",
    "paymentMethod" => [
        "name" => "POS",
        "bankCode" => "POS"
    ],
    "additionalInfo" => [
        "txnFlow" => "seamless",
        "txnS2sFlow" => "4"
    ],
    "callBackActions" => [
        "successAction" => "https://yoursite.com/webhook/success",
        "failureAction" => "https://yoursite.com/webhook/failure"
    ],
    "order" => [
        "productInfo" => "Coffee and Pastry",
        "paymentChargeSpecification" => [
            "price" => 1500.00
        ]
    ],
    "omniChannelDetails" => [
        "posDeviceId" => "DEVICE_POS_12345",
        "posPaymentMethod" => "sale"
    ],
    "gstParams" => [
        "gstIn" => "29ABCDE1234F1Z5",
        "gst" => "18.00",
        "cgst" => "9.00",
        "sgst" => "9.00"
    ],
    "printInfo" => [
        "field1" => "Table 5",
        "field2" => "Server: John"
    ]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```

</Accordion>

<Accordion title="Sample Request - Java" icon="fa-code">

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class InitiatePayment {
    public static void main(String[] args) throws Exception {
        String url = "https://api.payu.in/partner/initiatePayment";
        
        String payload = """
        {
          "accountId": "merchant_12345",
          "txnId": "ORD_20231115_001",
          "amount": 1500.00,
          "currency": "INR",
          "paymentSource": "WEB",
          "paymentMethod": {
            "name": "POS",
            "bankCode": "POS"
          },
          "additionalInfo": {
            "txnFlow": "seamless",
            "txnS2sFlow": "4"
          },
          "callBackActions": {
            "successAction": "https://yoursite.com/webhook/success",
            "failureAction": "https://yoursite.com/webhook/failure"
          },
          "order": {
            "productInfo": "Coffee and Pastry",
            "paymentChargeSpecification": {
              "price": 1500.00
            }
          },
          "omniChannelDetails": {
            "posDeviceId": "DEVICE_POS_12345",
            "posPaymentMethod": "sale"
          },
          "gstParams": {
            "gstIn": "29ABCDE1234F1Z5",
            "gst": "18.00",
            "cgst": "9.00",
            "sgst": "9.00"
          },
          "printInfo": {
            "field1": "Table 5",
            "field2": "Server: John"
          }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("X-Partner-Token", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
            .header("X-PayU-Reseller-UUID", "550e8400-e29b-41d4-a716-446655440000")
            .header("date", "Tue, 15 Nov 2023 08:12:31 GMT")
            .header("authorization", "hmac username=\"payu_client_id\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```

</Accordion>

---

### Step 1.4: Response Handling & Webhook

The Initiate Payment API typically returns a `pending` status immediately, as the actual payment happens asynchronously on the device. PayU will send a webhook to your `successAction` or `failureAction` URL once the payment completes.

<Accordion title="Success Response (Initiation)" icon="fa-check-circle">

```json
{
  "metaData": {
    "message": "Payment initiated successfully",
    "referenceId": "REF_20231115_12345",
    "statusCode": "E000",
    "txnId": "ORD_20231115_001",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "PAY_abc123xyz789",
    "authAction": null,
    "otpPostUrl": null
  }
}
```

**Key Fields:**
- `statusCode: "E000"` — Payment initiation succeeded
- `txnStatus: "pending"` — Payment is awaiting customer action on device
- `paymentId` — PayU's unique payment identifier (use this for reconciliation)

**What happens next:**
1. The specified device (`posDeviceId`) activates and displays the payment request
2. Customer pays on the device (card swipe/tap or DBQR scan)
3. PayU sends a webhook to your `successAction` or `failureAction` URL
4. You call the Check Transaction Status API to retrieve final details

</Accordion>

<Accordion title="Failure Response (Initiation)" icon="fa-times-circle">

**Example 1: Invalid Device ID**

```json
{
  "metaData": {
    "message": "Invalid Device Id",
    "referenceId": "REF_20231115_12346",
    "statusCode": "E2081",
    "txnId": "ORD_20231115_002",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": null
}
```

**Example 2: Invalid PG & Bank Code**

```json
{
  "metaData": {
    "message": "Invalid PG & Bank Code Combination",
    "referenceId": "REF_20231115_12347",
    "statusCode": "E1101",
    "txnId": "ORD_20231115_003",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": null
}
```

**Example 3: Inactive Payment Option**

```json
{
  "metaData": {
    "message": "Merchant Integration Exception - Inactive payment option",
    "referenceId": "REF_20231115_12348",
    "statusCode": "EX158",
    "txnId": "ORD_20231115_004",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": null
}
```

**Common Failure Error Codes:**

| Code | Meaning | Action Required |
|------|---------|-----------------|
| `E2081` | Invalid Device ID | Verify `posDeviceId` exists in your PayU dashboard |
| `E1101` | Invalid PG & Bank Code | Ensure `paymentMethod.name` and `paymentMethod.bankCode` are both set to "POS" |
| `EX158` | Inactive payment option | Contact PayU support to enable Omni product for your account |
| `E342` | Transaction not initiated | Check all mandatory parameters; review API logs |

</Accordion>

<Accordion title="Webhook Payload (Payment Completion)" icon="fa-bell">

When the customer completes payment on the device, PayU sends a webhook to your `successAction` or `failureAction` URL.

**Sample Webhook Payload:**

```json
{
  "vendorTxnId": "ORD_20231115_001",
  "txnId": "ORD_20231115_001",
  "mihpayId": "403993715534895620",
  "flowType": "ominichannel",
  "message": "Please use the checkBqrStatusAPI to fetch the final status of the transaction",
  "status": "pending"
}
```

**Webhook Fields:**
- `vendorTxnId` / `txnId` — Your original order ID
- `mihpayId` — PayU's internal transaction ID
- `flowType` — Always "ominichannel" for Omni payments
- `status` — May still be "pending" (not final)
- `message` — Instruction to call Check Status API

<Warning>
⚠️ **Important:** The webhook status may not be final. Always call the **Check Transaction Status API** to retrieve authoritative payment details before updating your order status or delivering goods/services.
</Warning>

**How to Handle Webhooks:**

1. Expose a publicly accessible HTTPS endpoint (the URL you passed in `successAction`)
2. Accept POST requests with JSON payload
3. Extract `mihpayId` or `txnId`
4. Call Check Transaction Status API using the `txnId`
5. Verify the response status is `success` (not `pending` or `failed`)
6. Update your order status accordingly
7. Return HTTP 200 to acknowledge receipt

</Accordion>

---

### Step 1.5: Verify the Payment

Always verify the payment using the Check Transaction Status API before marking an order as paid.

<Info>
📘 **See the complete guide:** [Integrate PayU Omni — Check Transaction Status](#)

This ensures you're acting on authoritative, verified transaction data, not just the webhook notification.
</Info>

---

## Step 2: Test Integration

### Step 2.1: Pre-Payment Validation

Before initiating test transactions, verify your setup:

<Accordion title="Pre-Payment Validation Checklist" icon="fa-check-square">

**✅ Credentials**
- [ ] You have a valid `X-Partner-Token` (OAuth Bearer token)
- [ ] You have your `X-PayU-Reseller-UUID`
- [ ] You have partner credentials (`clientId`, `clientSecret`)
- [ ] You have your merchant `accountId`

**✅ Device Setup**
- [ ] Your POS device or DBQR display is registered in your PayU dashboard
- [ ] You have noted the exact `posDeviceId` for your test device
- [ ] The device is powered on and connected to the internet

**✅ Webhook Endpoint**
- [ ] Your `successAction` URL is publicly accessible via HTTPS
- [ ] Your server can receive and log POST requests
- [ ] You've tested the endpoint with a dummy POST request

**✅ HMAC Generation**
- [ ] Your HMAC signature code runs without errors
- [ ] The `date` header format matches RFC 7231 GMT format
- [ ] The signature is lowercase hexadecimal
- [ ] You're generating a fresh signature for each request (not reusing old ones)

</Accordion>

---

### Step 2.2: Simulate a Successful Transaction

<Accordion title="Step-by-Step Success Simulation" icon="fa-play-circle">

**Step 1:** Generate a unique `txnId` for this test (e.g., `TEST_20231115_001`)

**Step 2:** Compute a fresh HMAC signature using your credentials and current GMT date

**Step 3:** POST the request with all mandatory parameters:
- Use a small amount (e.g., `10.00 INR`) for testing
- Set `posPaymentMethod` to `"sale"` to test card payments

**Step 4:** Verify you receive HTTP 200 with `statusCode: "E000"` and `txnStatus: "pending"`

**Step 5:** Check your test device — it should display the payment amount and prompt for card input

**Step 6:** Use a test card (⚠️ Info Gap: Test card numbers not documented — contact PayU support for test cards) or a real card for a small amount

**Step 7:** Complete the payment on the device

**Step 8:** Within 5-10 seconds, you should receive a webhook at your `successAction` URL

**Step 9:** Call the Check Transaction Status API with your `txnId`

**Step 10:** Verify the status API returns `status: "success"` and `unmappedStatus: "captured"`

**Checkpoint:** ✅ You should see a successful transaction in your PayU dashboard and receive a printed receipt (if device has a printer)

</Accordion>

---

### Step 2.3: Simulate a Failed Transaction

<Accordion title="Failure Scenario Testing" icon="fa-exclamation-triangle">

Test the following failure scenarios to ensure robust error handling:

**Scenario 1: Invalid Device ID**
- Set `posDeviceId` to a non-existent value (e.g., `INVALID_DEVICE`)
- Expected response: `statusCode: "E2081"`, `txnStatus: "failed"`

**Scenario 2: Invalid Payment Method**
- Set `paymentMethod.name` to `"NETBANKING"` instead of `"POS"`
- Expected response: `statusCode: "E1101"` or `"EX158"`

**Scenario 3: Customer Cancels Payment**
- Initiate a valid payment request
- Press the "Cancel" button on the POS device before paying
- Expected webhook: `status: "failed"` (webhook sent to `failureAction` URL)

**Scenario 4: Duplicate Transaction ID**
- Send the same `txnId` twice
- Expected response: Duplicate transaction error (exact code may vary — document what you observe)

**Checkpoint:** ✅ Your system should gracefully handle all failure scenarios without crashing, and log meaningful error messages for debugging

</Accordion>

---

### Step 2.4: Post-Transaction Verification

<Accordion title="Post-Transaction Checks" icon="fa-clipboard-check">

After each test transaction, verify:

**✅ Webhook Receipt**
- [ ] Your server received the webhook within 10 seconds of payment completion
- [ ] The webhook payload contains `mihpayId`, `txnId`, and `flowType: "ominichannel"`

**✅ Status API Cross-Check**
- [ ] Calling Check Status API returns the same `mihpayId` as the webhook
- [ ] The `status` field matches the payment outcome (success/failure)
- [ ] All transaction metadata (amount, productInfo, etc.) is accurate

**✅ Dashboard Reconciliation**
- [ ] The transaction appears in your PayU dashboard within 1 minute
- [ ] The dashboard status matches your API response
- [ ] The `txnId` and amount are correct

**✅ Receipt Verification (if applicable)**
- [ ] The printed receipt contains the correct amount and order details
- [ ] Custom fields from `printInfo` appear on the receipt
- [ ] GST details appear correctly (if `gstParams` were included)

</Accordion>

---

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

<Accordion title="Production Credential Migration" icon="fa-rocket">

**Step 1:** Obtain production credentials from PayU
- Production `clientId` and `clientSecret`
- Production OAuth token endpoint and `X-Partner-Token`
- Production `X-PayU-Reseller-UUID`
- Production `accountId`

**Step 2:** Update your code
- Replace all test credentials with production credentials
- Ensure HMAC signature computation uses production `clientSecret`

**Step 3:** Update the API endpoint
- Change `https://apitest.payu.in/...` to `https://api.payu.in/...` (if test endpoint exists)
- Verify the production endpoint URL with PayU support

**Step 4:** Register production devices
- Ensure your live POS devices are registered in your production PayU account
- Note the production `posDeviceId` values

**Step 5:** Update webhook URLs
- Point `successAction` and `failureAction` to production webhook endpoints
- Ensure these URLs are HTTPS and publicly accessible

**Step 6:** Test with production credentials in a controlled environment
- Perform 1-2 small-value transactions with real cards before full launch

</Accordion>

---

### Step 3.2: Final Integration Verification

<Accordion title="Production Readiness Checklist" icon="fa-tasks">

**✅ Conduct a Live Transaction**
- [ ] Initiate a real transaction with a small amount
- [ ] Verify the device activates correctly
- [ ] Complete payment with a real card or UPI
- [ ] Confirm you receive a success webhook
- [ ] Verify transaction appears in production dashboard

**✅ Verify the Webhook Endpoint**
- [ ] Your production webhook endpoint is HTTPS (not HTTP)
- [ ] The endpoint can handle 100+ requests per minute (if you have high transaction volume)
- [ ] Webhook responses are returned within 2 seconds

**✅ Validate HMAC Signatures**
- [ ] Every request uses a freshly computed HMAC signature
- [ ] The `date` header is within ±5 minutes of actual time (some servers validate this)
- [ ] Signatures are lowercase hexadecimal (not uppercase or base64)

**✅ Check Callback URLs**
- [ ] `successAction` URL is correct and tested
- [ ] `failureAction` URL is correct and tested (if used)
- [ ] Both URLs return HTTP 200 to acknowledge PayU webhooks

**✅ Implement Error Handling**
- [ ] Your system retries failed API calls (network timeouts, 5xx errors)
- [ ] You log all API requests and responses for debugging
- [ ] Users see meaningful error messages (not raw API error codes)

**✅ Set Up Monitoring**
- [ ] You have alerts for webhook failures (no webhook received within 30 seconds)
- [ ] You monitor API error rates (> 5% failure rate triggers alert)
- [ ] You track transaction success rates in your analytics dashboard

**✅ Implement a Reconciliation Plan**
- [ ] Daily reconciliation job compares your orders with PayU settlement reports
- [ ] Discrepancies trigger manual review
- [ ] You call Check Status API for any "pending" transactions older than 15 minutes

**✅ Document Your Integration**
- [ ] Internal wiki/docs explain how to add new devices
- [ ] Runbooks exist for common error scenarios
- [ ] On-call engineers know how to debug webhook failures

**✅ Security Checklist**
- [ ] `clientSecret` is stored in environment variables or secrets manager (not hardcoded)
- [ ] API calls are made server-side only (never from client/browser)
- [ ] Webhook endpoint validates the source IP or signature (if PayU provides one)

**✅ Test Edge Cases**
- [ ] What happens if the device loses internet mid-transaction?
- [ ] What if your webhook endpoint is down when PayU sends the notification?
- [ ] What if a customer pays but you never receive a webhook? (Answer: Polling via Check Status API)

**✅ Regulatory Compliance**
- [ ] You store transaction logs for the required duration (e.g., 7 years for tax audits)
- [ ] Customer card details are never logged or stored (PCI-DSS compliance)
- [ ] GST invoices are generated correctly (if applicable)

**✅ Business Continuity**
- [ ] You have a backup plan if the primary device fails (secondary device or manual payment method)
- [ ] Your team knows how to issue refunds (via PayU dashboard or refund API)

</Accordion>

---

**Congratulations!** 🎉 You've successfully integrated the PayU Omni Initiate Payment API. For status checks and reconciliation, proceed to the [Check Transaction Status Integration Guide](#).

