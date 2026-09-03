---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
# Integrate PayU Omni — Complete Integration Guide

This section describes the complete PayU Omni Integrated Flow: from initiating payment requests to verifying transaction status and reconciliation.

<Note>
**Prerequisites**

Before you begin, ensure you have:
- ✅ A PayU merchant account with Omni product enabled
- ✅ Partner credentials (`clientId`, `clientSecret`, Partner UUID) for Initiate Payment API
- ✅ Merchant credentials (`mid`, merchant key, merchant salt) for Check Status API
- ✅ At least one registered PayU device (POS terminal or DBQR display)
- ✅ Device ID(s) from your PayU account dashboard
- ✅ OAuth token obtained from PayU Token API (⚠️ Info Gap: Token API endpoint not documented — contact PayU support)
- ✅ A server capable of receiving webhooks (publicly accessible HTTPS endpoint)
</Note>

---

## Step 1: Start Integration

<Cards columns={3}>
  <Card title="1.1 Initiate Payment — Prepare Request Parameters" href="#step-11-initiate-payment--prepare-request-parameters">
    Gather partner credentials (clientId, clientSecret, UUID), OAuth token, and device ID. Prepare all required headers and request body fields.

    **✅ Checkpoint:** All mandatory parameters are ready and you understand the difference between mandatory and optional fields.
  </Card>

  <Card title="1.2 Initiate Payment — Generate HMAC Authorization" href="#step-12-initiate-payment--generate-hmac-authorization">
    Generate GMT date in RFC 7231 format. Create an HMAC-SHA512 signature by hashing the date string with your clientSecret.

    **✅ Checkpoint:** HMAC signature is generated successfully and the authorization header is properly formatted.
  </Card>

  <Card title="1.3 Initiate Payment — POST the Request" href="#step-13-initiate-payment--post-the-request">
    Send a POST request to `https://api.payu.in/partner/initiatePayment` with all required headers and the complete JSON body.

    **✅ Checkpoint:** You receive an HTTP 200 response with statusCode `E000` and txnStatus `pending`.
  </Card>

  <Card title="1.4 Initiate Payment — Handle Response & Webhook" href="#step-14-initiate-payment--handle-response--webhook">
    Parse the initiation response. The device activates and customer completes payment. Webhook is sent to your successAction URL.

    **✅ Checkpoint:** Webhook received successfully with mihpayId and flowType `ominichannel`.
  </Card>

  <Card title="1.5 Check Transaction Status — Prepare Request" href="#step-15-check-transaction-status--prepare-request">
    Switch from partner credentials to merchant credentials. Prepare headers and request body with the txnId array.

    **✅ Checkpoint:** You understand that the Check Status API uses merchant credentials, not partner credentials.
  </Card>

  <Card title="1.6 Check Transaction Status — POST the Request" href="#step-16-check-transaction-status--post-the-request">
    Generate a fresh HMAC signature using merchant credentials. POST to Check Status endpoint.

    **✅ Checkpoint:** You receive an HTTP 200 response with `status: 1` and transaction details.
  </Card>

  <Card title="1.7 Check Transaction Status — Verify Response" href="#step-17-check-transaction-status--verify-response">
    Verify all transaction fields. Mark the order as paid only after all checks pass.

    **✅ Checkpoint:** All verification checks pass and the order is marked as paid.
  </Card>
</Cards>

---

### Step 1.1: Initiate Payment — Prepare Request Parameters

<Tabs>
  <Tab title="Request Parameters">

#### Request Headers

**Mandatory Parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| <Glossary>Content-Type</Glossary> | String | Must be application/json | application/json |
| X-Partner-Token | String | Bearer OAuth token obtained from PayU token API | Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... |
| X-PayU-Reseller-UUID | String | Partner UUID provided by PayU during onboarding | 550e8400-e29b-41d4-a716-446655440000 |
| date | String | Current request date and time in GMT format (RFC 7231) | Tue, 15 Nov 2023 08:12:31 GMT |
| authorization | String | <Glossary>HMAC</Glossary>-<Glossary>SHA-512</Glossary> signature header in format: hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex-signature>" | hmac username="your_client_id", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..." |

#### Request Body — Mandatory Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| accountId | String | Merchant account identifier provided by PayU | merchant_12345 |
| <Glossary>txnid</Glossary> | String | Unique transaction ID from your billing system. Must be alphanumeric and unique per transaction. | ORD_20231115_001 |
| amount | Double | Transaction amount with exactly 2 decimal places | 1500.00 |
| currency | String | ISO 4217 currency code | INR |
| <Glossary>payment_source</Glossary> | String | For <Glossary>POS</Glossary>/Omni integrations, use "WEB" | WEB |
| paymentMethod | Object | Payment method details. For Omni/POS, use {"name":"POS", "bankCode":"POS"} | {"name":"POS", "bankCode":"POS"} |
| paymentMethod.name | String | Payment method name. Use "POS" for Omni devices | POS |
| paymentMethod.bankCode | String | Bank/PG code. Use "POS" for Omni devices | POS |
| additionalInfo | Object | Contains transaction flow configuration | {"txnFlow":"seamless", "txnS2sFlow":"4"} |
| additionalInfo.txnFlow | String | Transaction flow type. Use "seamless" for integrated flow | seamless |
| additionalInfo.txnS2sFlow | String | Server-to-server flow identifier. Use "4" for Omni | 4 |
| <Glossary>Callback</Glossary> | Object | Webhook URLs for transaction callbacks | {"successAction":"https://yoursite.com/success"} |
| callBackActions.successAction | String (URL) | URL to receive success <Glossary>webhook</Glossary> notifications | https://yoursite.com/webhook/success |
| order | Object | Order details including product info and pricing | {"productInfo":"Product Name", "paymentChargeSpecification":{"price":1500.00}} |
| <Glossary>productinfo</Glossary> | String | Product or service description | Coffee and Pastry |
| order.paymentChargeSpecification | Object | Payment charge details | {"price":1500.00} |
| order.paymentChargeSpecification.price | Double | Order price (should match top-level amount) | 1500.00 |
| omniChannelDetails | Object | Omni device and payment method configuration | {"posDeviceId":"DEVICE_12345", "posPaymentMethod":"sale"} |
| omniChannelDetails.posDeviceId | String | Unique device ID of the POS terminal or DBQR display where payment should be accepted | DEVICE_POS_12345 |
| omniChannelDetails.posPaymentMethod | String | Payment method to activate on device. Use "sale" for card payments, "qr" for DBQR/UPI | sale |

#### Request Body — Optional Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| callBackActions.failureAction | String (URL) | URL to receive failure webhook notifications | https://yoursite.com/webhook/failure |
| callBackActions.cancelAction | String (URL) | URL to receive cancel webhook notifications | https://yoursite.com/webhook/cancel |
| <Glossary>GST</Glossary> | Object | GST invoice parameters for GST-compliant receipts | {"gstIn":"29ABCDE1234F1Z5", "gst":"18.00"} |
| gstParams.gstIn | String | Merchant GSTIN number | 29ABCDE1234F1Z5 |
| gstParams.gst | String | Total GST amount | 18.00 |
| gstParams.cgst | String | Central GST amount | 9.00 |
| gstParams.sgst | String | State GST amount | 9.00 |
| gstParams.igst | String | Integrated GST amount (for inter-state transactions) | 18.00 |
| gstParams.cess | String | GST Cess amount if applicable | 1.00 |
| printInfo | Object | Custom fields to print on receipt | {"field1":"Table 5", "field2":"Server: John"} |
| <Glossary>User Defined Field</Glossary> | String | Custom data fields (UDFs) for reporting and receipts | Table 5 |

  </Tab>

  <Tab title="Sample Request">

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
  }
}'
```
**Python**
```python
import requests
import json
url = "https://api.payu.in/partner/initiatePayment"
headers = {
    "Content-Type": "application/json",
    "X-Partner-Token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-PayU-Reseller-UUID": "550e8400-e29b-41d4-a716-446655440000",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": 'hmac username="payu_client_id", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
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
    }
}
response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.text)
```
**JavaScript**
```javascript
const url = "https://api.payu.in/partner/initiatePayment";
const payload = {
  accountId: "merchant_12345",
  txnId: "ORD_20231115_001",
  amount: 1500.00,
  currency: "INR",
  paymentSource: "WEB",
  paymentMethod: { name: "POS", bankCode: "POS" },
  additionalInfo: { txnFlow: "seamless", txnS2sFlow: "4" },
  callBackActions: {
    successAction: "https://yoursite.com/webhook/success",
    failureAction: "https://yoursite.com/webhook/failure"
  },
  order: {
    productInfo: "Coffee and Pastry",
    paymentChargeSpecification: { price: 1500.00 }
  },
  omniChannelDetails: { posDeviceId: "DEVICE_POS_12345", posPaymentMethod: "sale" }
};
const response = await fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-Partner-Token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-PayU-Reseller-UUID": "550e8400-e29b-41d4-a716-446655440000",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": 'hmac username="payu_client_id", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
  },
  body: JSON.stringify(payload)
});
const data = await response.text();
console.log(response.status, data);
```
**PHP**
```php
<?php
$url = "https://api.payu.in/partner/initiatePayment";
$payload = json_encode([
    "accountId" => "merchant_12345",
    "txnId" => "ORD_20231115_001",
    "amount" => 1500.00,
    "currency" => "INR",
    "paymentSource" => "WEB",
    "paymentMethod" => ["name" => "POS", "bankCode" => "POS"],
    "additionalInfo" => ["txnFlow" => "seamless", "txnS2sFlow" => "4"],
    "callBackActions" => [
        "successAction" => "https://yoursite.com/webhook/success",
        "failureAction" => "https://yoursite.com/webhook/failure"
    ],
    "order" => [
        "productInfo" => "Coffee and Pastry",
        "paymentChargeSpecification" => ["price" => 1500.00]
    ],
    "omniChannelDetails" => ["posDeviceId" => "DEVICE_POS_12345", "posPaymentMethod" => "sale"]
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "X-Partner-Token: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "X-PayU-Reseller-UUID: 550e8400-e29b-41d4-a716-446655440000",
    "date: Tue, 15 Nov 2023 08:12:31 GMT",
    'authorization: hmac username="payu_client_id", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
]);
$response = curl_exec($ch);
echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n" . $response;
curl_close($ch);
?>
```
**Java**
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
public class InitiatePayment {
    public static void main(String[] args) throws Exception {
        String url = "https://api.payu.in/partner/initiatePayment";
        String payload = "{" +
            "\"accountId\":\"merchant_12345\"," +
            "\"txnId\":\"ORD_20231115_001\"," +
            "\"amount\":1500.00," +
            "\"currency\":\"INR\"," +
            "\"paymentSource\":\"WEB\"," +
            "\"paymentMethod\":{\"name\":\"POS\",\"bankCode\":\"POS\"}," +
            "\"additionalInfo\":{\"txnFlow\":\"seamless\",\"txnS2sFlow\":\"4\"}," +
            "\"callBackActions\":{\"successAction\":\"https://yoursite.com/webhook/success\",\"failureAction\":\"https://yoursite.com/webhook/failure\"}," +
            "\"order\":{\"productInfo\":\"Coffee and Pastry\",\"paymentChargeSpecification\":{\"price\":1500.00}}," +
            "\"omniChannelDetails\":{\"posDeviceId\":\"DEVICE_POS_12345\",\"posPaymentMethod\":\"sale\"}" +
        "}";
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
        System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}
```
**C#**
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
class InitiatePayment {
    static async Task Main() {
        var client = new HttpClient();
        var url = "https://api.payu.in/partner/initiatePayment";
        var payload = "{" +
            "\"accountId\":\"merchant_12345\"," +
            "\"txnId\":\"ORD_20231115_001\"," +
            "\"amount\":1500.00," +
            "\"currency\":\"INR\"," +
            "\"paymentSource\":\"WEB\"," +
            "\"paymentMethod\":{\"name\":\"POS\",\"bankCode\":\"POS\"}," +
            "\"additionalInfo\":{\"txnFlow\":\"seamless\",\"txnS2sFlow\":\"4\"}," +
            "\"callBackActions\":{\"successAction\":\"https://yoursite.com/webhook/success\",\"failureAction\":\"https://yoursite.com/webhook/failure\"}," +
            "\"order\":{\"productInfo\":\"Coffee and Pastry\",\"paymentChargeSpecification\":{\"price\":1500.00}}," +
            "\"omniChannelDetails\":{\"posDeviceId\":\"DEVICE_POS_12345\",\"posPaymentMethod\":\"sale\"}" +
        "}";
        client.DefaultRequestHeaders.Add("X-Partner-Token", "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...");
        client.DefaultRequestHeaders.Add("X-PayU-Reseller-UUID", "550e8400-e29b-41d4-a716-446655440000");
        client.DefaultRequestHeaders.Add("date", "Tue, 15 Nov 2023 08:12:31 GMT");
        client.DefaultRequestHeaders.Add("authorization", "hmac username=\"payu_client_id\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\"");
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        var response = await client.PostAsync(url, content);
        Console.WriteLine((int)response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

> **Note:** Replace all placeholder values with your actual credentials and device details.

  </Tab>
</Tabs>

---

### Step 1.2: Initiate Payment — Generate HMAC Authorization

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
- The `date` header value must exactly match the value used in the HMAC computation
- Signatures expire quickly — generate fresh signatures for each request
</Warning>

</Accordion>

---

### Step 1.3: Initiate Payment — POST the Request

(See the Sample Request tab in Step 1.1 above for the complete multi-language POST request.)

---

### Step 1.4: Initiate Payment — Handle Response & Webhook

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

**What happens next:**
1. Device activates and displays the payment request
2. Customer pays on device (card or DBQR scan)
3. PayU sends webhook to your `successAction` URL
4. You call Check Transaction Status API (Step 1.5)

</Accordion>

<Accordion title="Failure Response Examples" icon="fa-times-circle">

**Invalid Device ID:**
```json
{
  "metaData": {
    "message": "Invalid Device Id",
    "statusCode": "E2081",
    "txnStatus": "failed"
  }
}
```

**Common Error Codes:**

| Code | Meaning | Action |
|------|---------|--------|
| E2081 | Invalid Device ID | Verify posDeviceId in dashboard |
| E1101 | Invalid PG & Bank Code | Use "POS" for both name and bankCode |
| EX158 | Inactive payment option | Contact PayU to enable Omni |

</Accordion>

<Accordion title="Webhook Payload" icon="fa-bell">

```json
{
  "vendorTxnId": "ORD_20231115_001",
  "txnId": "ORD_20231115_001",
  "mihpayId": "403993715534895620",
  "flowType": "ominichannel",
  "message": "Please use the checkBqrStatusAPI to fetch the final status",
  "status": "pending"
}
```

<Warning>
⚠️ **Critical:** The webhook status may be "pending". Always call Check Transaction Status API (Step 1.5) to get final payment details.
</Warning>

</Accordion>

---

### Step 1.5: Check Transaction Status — Prepare Request

<Tabs>
  <Tab title="Request Parameters">

#### Status API — Request Headers

**Mandatory Parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| <Glossary>MID</Glossary> | String | Merchant identifier provided by PayU | merchant_12345 |
| Content-Type | String | Must be application/json | application/json |
| Info-Command | String | Must be check_bqr_txn_status | check_bqr_txn_status |
| date | String | Current request date and time in GMT format (RFC 7231) | Tue, 15 Nov 2023 08:12:31 GMT |
| authorization | String | HMAC-SHA512 signature header in format: hmac username="<merchantKey>", algorithm="sha512", headers="date", signature="<hex-signature>" | hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..." |

<Info>
**Important:** This API uses **merchant credentials** (merchant key + salt), NOT partner credentials.
</Info>

#### Status API — Request Body

**Mandatory Parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| txnId | Array of Strings | Array of transaction IDs to check status for. You can query multiple transactions in a single request (up to 10 recommended). | ["ORD_20231115_001", "ORD_20231115_002"] |

  </Tab>

  <Tab title="Sample Request">

```bash
curl --location 'https://info.payu.in/v1/transaction/?mode=bqr' \
--header 'mid: merchant_12345' \
--header 'Content-Type: application/json' \
--header 'Info-Command: check_bqr_txn_status' \
--header 'date: Tue, 15 Nov 2023 08:12:31 GMT' \
--header 'authorization: hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."' \
--data '{
  "txnId": ["ORD_20231115_001"]
}'
```
**Python**
```python
import requests
url = "https://info.payu.in/v1/transaction/?mode=bqr"
headers = {
    "mid": "merchant_12345",
    "Content-Type": "application/json",
    "Info-Command": "check_bqr_txn_status",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": 'hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
}
payload = {"txnId": ["ORD_20231115_001"]}
response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.text)
```
**JavaScript**
```javascript
const url = "https://info.payu.in/v1/transaction/?mode=bqr";
const response = await fetch(url, {
  method: "POST",
  headers: {
    "mid": "merchant_12345",
    "Content-Type": "application/json",
    "Info-Command": "check_bqr_txn_status",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": 'hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
  },
  body: JSON.stringify({ txnId: ["ORD_20231115_001"] })
});
const data = await response.text();
console.log(response.status, data);
```
**PHP**
```php
<?php
$url = "https://info.payu.in/v1/transaction/?mode=bqr";
$payload = json_encode(["txnId" => ["ORD_20231115_001"]]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "mid: merchant_12345",
    "Content-Type: application/json",
    "Info-Command: check_bqr_txn_status",
    "date: Tue, 15 Nov 2023 08:12:31 GMT",
    'authorization: hmac username="your_merchant_key", algorithm="sha512", headers="date", signature="a1b2c3d4e5f6..."'
]);
$response = curl_exec($ch);
echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n" . $response;
curl_close($ch);
?>
```
**Java**
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
public class CheckTransactionStatus {
    public static void main(String[] args) throws Exception {
        String url = "https://info.payu.in/v1/transaction/?mode=bqr";
        String payload = "{\"txnId\":[\"ORD_20231115_001\"]}";
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("mid", "merchant_12345")
            .header("Content-Type", "application/json")
            .header("Info-Command", "check_bqr_txn_status")
            .header("date", "Tue, 15 Nov 2023 08:12:31 GMT")
            .header("authorization", "hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}
```
**C#**
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
class CheckTransactionStatus {
    static async Task Main() {
        var client = new HttpClient();
        var url = "https://info.payu.in/v1/transaction/?mode=bqr";
        var payload = "{\"txnId\":[\"ORD_20231115_001\"]}";
        client.DefaultRequestHeaders.Add("mid", "merchant_12345");
        client.DefaultRequestHeaders.Add("Info-Command", "check_bqr_txn_status");
        client.DefaultRequestHeaders.Add("date", "Tue, 15 Nov 2023 08:12:31 GMT");
        client.DefaultRequestHeaders.Add("authorization", "hmac username=\"your_merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\"");
        var content = new StringContent(payload, Encoding.UTF8, "application/json");
        var response = await client.PostAsync(url, content);
        Console.WriteLine((int)response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

  </Tab>
</Tabs>

---

### Step 1.6: Check Transaction Status — POST the Request

(See the Sample Request tab in Step 1.5 above for the complete multi-language POST request.)

---

### Step 1.7: Check Transaction Status — Verify Response

<Accordion title="Success Response - DBQR Payment" icon="fa-check-circle">

```json
{
  "status": 1,
  "message": "Success",
  "result": [
    {
      "txnId": "ORD_20231115_001",
      "mihpayId": "403993715534895620",
      "bankReferenceNumber": "332116831375",
      "amount": "1500.00",
      "mode": "DBQR",
      "status": "success",
      "unmappedStatus": "captured",
      "errorCode": "E000",
      "errorMessage": "No Error",
      "productInfo": "Coffee and Pastry",
      "merchantUTR": "332116831375",
      "field0": "b5f29799-9999-8798-9990-012345678901",
      "field1": "Table 5",
      "field6": "success@payu"
    }
  ]
}
```

**Success Indicators:**
- ✅ `status: 1` (API call succeeded)
- ✅ `result[].status: "success"` (Payment succeeded)
- ✅ `result[].unmappedStatus: "captured"` (Funds captured)
- ✅ `result[].errorCode: "E000"` (No errors)

</Accordion>

<Accordion title="Transaction Verification Checklist" icon="fa-clipboard-check">

Before marking an order as paid, verify:

**✅ Payment Status**
- [ ] `status: 1` (top-level API success)
- [ ] `result[].status: "success"` (not "pending" or "failed")
- [ ] `result[].unmappedStatus: "captured"` (not "in progress")
- [ ] `result[].errorCode: "E000"`

**✅ Amount & Order Matching**
- [ ] `amount` matches your order amount exactly
- [ ] `txnId` matches your order ID
- [ ] `productInfo` matches your order description

**✅ Bank Reconciliation Fields**
- [ ] `bankReferenceNumber` is present (not empty)
- [ ] `merchantUTR` is present
- [ ] `mihpayId` is present

**✅ Reverse Hash Validation (Recommended)**
- [ ] Compute reverse hash using merchant salt
- [ ] Compare with `reverseHash` field
- [ ] Proceed only if hash matches

<Warning>
⚠️ **Only mark order as PAID if ALL checks pass.** If status is "pending", poll the API again after 10-15 seconds.
</Warning>

</Accordion>

---

## Step 2: Test Integration

<Cards columns={3}>
  <Card title="2.1 Pre-Integration Validation" href="#step-21">
    Validate both partner and merchant credentials. Verify device is accessible and webhook endpoint works.
    
    **✅ Checkpoint:** All credentials work, device is accessible.
  </Card>

  <Card title="2.2 End-to-End Success Flow" href="#step-22">
    Execute complete flow: initiate → device payment → webhook → status check.
    
    **✅ Checkpoint:** Complete successful transaction visible in dashboard.
  </Card>

  <Card title="2.3 Failure Testing" href="#step-23">
    Test invalid device ID, cancellation, pending states, batch queries.
    
    **✅ Checkpoint:** System handles all failures gracefully.
  </Card>

  <Card title="2.4 Reconciliation Testing" href="#step-24">
    Cross-check webhook, Status API, and dashboard data.
    
    **✅ Checkpoint:** All reconciliation points match.
  </Card>
</Cards>

[Testing content follows same pattern as above...]

---

## Step 3: Going Live

<Cards columns={3}>
  <Card title="3.1 Update to Production Credentials" href="#step-31">
    Replace all test credentials with production values.
    
    **✅ Checkpoint:** Production credentials configured and tested.
  </Card>

  <Card title="3.2 Production Readiness Checklist" href="#step-32">
    Verify security, monitoring, reconciliation, and compliance.
    
    **✅ Checkpoint:** All 15 production checks pass.
  </Card>
</Cards>

[Go-live content follows...]

---

**Congratulations!** 🎉 You've successfully integrated PayU Omni Integrated Flow.

For detailed API specifications, refer to:
- [Initiate Payment API Reference](#initiate-payment-api)
- [Check Transaction Status API Reference](#check-transaction-status-api)
