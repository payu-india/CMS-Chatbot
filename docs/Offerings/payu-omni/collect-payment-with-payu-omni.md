---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
# Integrate PayU Omni — Complete Integration Guide

This comprehensive guide walks you through the complete PayU Omni Integrated Flow: from initiating payment requests to verifying transaction status and reconciliation.

By the end of this guide, you'll be able to:
- Send order-specific payment requests to your PayU devices
- Handle webhooks for payment notifications
- Verify payment status and retrieve transaction details
- Test your complete integration before going live
- Build automated reconciliation systems

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

### Step 1.1: Initiate Payment — Prepare Request Parameters

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

### Step 1.2: Initiate Payment — Generate HMAC Authorization

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

### Step 1.3: Initiate Payment — POST the Request

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

> **Note:** Replace all placeholder values with your actual credentials and device details before use.

</Accordion>

<Accordion title="Sample Request - Other Languages" icon="fa-code">

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
    "authorization": "hmac username=\"payu_client_id\", algorithm=\"sha512\", headers=\"date\", signature=\"a1b2c3d4e5f6...\""
}
payload = {
    "accountId": "merchant_12345",
    "txnId": "ORD_20231115_001",
    "amount": 1500.00,
    # ... (rest of payload)
}

response = requests.post(url, headers=headers, json=payload)
print(response.text)
```

**PHP**

```php
<?php
$url = "https://api.payu.in/partner/initiatePayment";
$headers = [
    "Content-Type: application/json",
    "X-Partner-Token: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    // ... other headers
];
$payload = json_encode([
    "accountId" => "merchant_12345",
    // ... rest of payload
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
$response = curl_exec($ch);
curl_close($ch);
echo $response;
?>
```

> **Full code samples available in the [Initiate Payment API Reference](#initiate-payment-api)**

</Accordion>

---

### Step 1.4: Initiate Payment — Handle Response & Webhook

The Initiate Payment API typically returns a `pending` status immediately. PayU will send a webhook to your `successAction` URL once the payment completes.

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
2. Customer pays on the device (card or DBQR scan)
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
| `E2081` | Invalid Device ID | Verify `posDeviceId` in dashboard |
| `E1101` | Invalid PG & Bank Code | Use `"POS"` for both name and bankCode |
| `EX158` | Inactive payment option | Contact PayU to enable Omni |

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

After receiving the webhook, immediately call the Check Transaction Status API to retrieve final payment details.

<Accordion title="Status API - Request Headers" icon="fa-list">

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `mid` | String | Merchant identifier | `merchant_12345` |
| `Content-Type` | String | Must be `application/json` | `application/json` |
| `Info-Command` | String | Must be `check_bqr_txn_status` | `check_bqr_txn_status` |
| `date` | String | Current GMT date (RFC 7231) | `Tue, 15 Nov 2023 08:12:31 GMT` |
| `authorization` | String | HMAC-SHA512 signature (using **merchant credentials**, not partner credentials) | `hmac username="merchant_key", algorithm="sha512", headers="date", signature="..."` |

<Info>
**Important:** This API uses **merchant credentials** (merchant key + salt), NOT partner credentials.
</Info>

</Accordion>

<Accordion title="Status API - Request Body" icon="fa-list">

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `txnId` | Array of Strings | Transaction IDs to check (up to 10 per request) | `["ORD_20231115_001"]` |

</Accordion>

<Accordion title="Status API - Generate HMAC (Merchant Credentials)" icon="fa-key">

**Important:** Use your **merchant key** and **merchant salt** (different from partner credentials).

```python
import hashlib
import hmac
from email.utils import formatdate

# Your MERCHANT credentials (not partner credentials)
merchant_key = "your_merchant_key"
merchant_salt = "your_merchant_salt"

# Generate GMT date
date_header = formatdate(timeval=None, localtime=False, usegmt=True)

# Create HMAC signature
signature = hmac.new(
    merchant_salt.encode('utf-8'),
    date_header.encode('utf-8'),
    hashlib.sha512
).hexdigest()

# Build authorization header
authorization_header = f'hmac username="{merchant_key}", algorithm="sha512", headers="date", signature="{signature}"'
```

</Accordion>

---

### Step 1.6: Check Transaction Status — POST the Request

<Accordion title="Sample Request - cURL" icon="fa-code">

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

</Accordion>

<Accordion title="Sample Request - Other Languages" icon="fa-code">

**Python**

```python
import requests

url = "https://info.payu.in/v1/transaction/?mode=bqr"
headers = {
    "mid": "merchant_12345",
    "Content-Type": "application/json",
    "Info-Command": "check_bqr_txn_status",
    "date": "Tue, 15 Nov 2023 08:12:31 GMT",
    "authorization": "hmac username=\"merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"...\""
}
payload = {"txnId": ["ORD_20231115_001"]}

response = requests.post(url, headers=headers, json=payload)
print(response.text)
```

> **Full code samples in [Check Transaction Status API Reference](#check-transaction-status-api)**

</Accordion>

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
      "field6": "success@payu",
      "reverseHash": "abcdef123...",
      "omniChannelDetails": {
        "posDeviceId": "DEVICE_POS_12345",
        "posPaymentMethod": "qr"
      }
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

<Accordion title="Success Response - Card Payment" icon="fa-credit-card">

```json
{
  "status": 1,
  "result": [
    {
      "txnId": "ORD_20231115_002",
      "mode": "CARD",
      "status": "success",
      "unmappedStatus": "captured",
      "nameOnCard": "JOHN DOE",
      "cardNo": "XXXXXXXXXXXX1234",
      "bankcode": "VISA",
      "field5": "JOHN DOE",
      "field8": "XXXXXXXXXXXX1234",
      "field9": "VISA"
    }
  ]
}
```

</Accordion>

<Accordion title="Transaction Verification Checklist" icon="fa-clipboard-check">

Before marking an order as paid, verify:

**✅ Payment Status**
- [ ] `status: 1` (top-level API success)
- [ ] `result[].status: "success"` (not "pending" or "failed")
- [ ] `result[].unmappedStatus: "captured"` (not "in progress" or "initiated")
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

<Accordion title="Field Mapping: field0-field9" icon="fa-table">

Fields contain different data based on payment mode:

**DBQR/UPI Mode:**
- `field0`: UPI Transaction ID
- `field1-5`: Custom UDFs (from `printInfo`)
- `field6`: Customer UPI VPA
- `field7`: Flow type
- `field9`: "DBQR"

**Card Mode:**
- `field1-4`: Custom UDFs
- `field5`: Cardholder name
- `field7`: "CARD"
- `field8`: Masked card number
- `field9`: Card network (VISA/MASTERCARD/RUPAY)

> **Full mapping in [Check Transaction Status API Reference](#check-transaction-status-api)**

</Accordion>

---

## Step 2: Test Integration

### Step 2.1: Pre-Integration Validation

<Accordion title="Pre-Integration Checklist" icon="fa-check-square">

**✅ Partner Credentials (for Initiate Payment API)**
- [ ] Valid `X-Partner-Token` (OAuth Bearer token)
- [ ] `X-PayU-Reseller-UUID`
- [ ] Partner `clientId` and `clientSecret`

**✅ Merchant Credentials (for Check Status API)**
- [ ] Merchant ID (`mid`)
- [ ] Merchant key
- [ ] Merchant salt

**✅ Device Setup**
- [ ] Device registered in PayU dashboard
- [ ] `posDeviceId` noted
- [ ] Device powered on and connected

**✅ Webhook Endpoint**
- [ ] HTTPS endpoint publicly accessible
- [ ] Can receive POST requests
- [ ] Returns HTTP 200 to acknowledge

**✅ HMAC Generation**
- [ ] Partner HMAC code works (for Initiate Payment)
- [ ] Merchant HMAC code works (for Check Status)
- [ ] Both generate fresh signatures per request

</Accordion>

---

### Step 2.2: End-to-End Success Flow

<Accordion title="Complete Success Test (8 Steps)" icon="fa-play-circle">

**Step 1:** Generate a unique test `txnId` (e.g., `TEST_20231115_001`)

**Step 2:** Generate partner HMAC signature with current GMT date

**Step 3:** POST Initiate Payment request with test amount (e.g., `10.00 INR`)

**Step 4:** Verify HTTP 200 response with `statusCode: "E000"` and `txnStatus: "pending"`

**Step 5:** Check device — it should display the amount and await payment

**Step 6:** Complete payment on device (card or DBQR scan)

**Step 7:** Receive webhook within 10 seconds at your `successAction` URL

**Step 8:** Extract `txnId` from webhook, generate merchant HMAC, call Check Status API

**Step 9:** Verify Status API returns `status: "success"`, `unmappedStatus: "captured"`

**Step 10:** Verify `amount`, `bankReferenceNumber`, and all custom fields are correct

**Checkpoint:** ✅ Transaction appears in PayU dashboard with "Success" status

</Accordion>

---

### Step 2.3: Failure & Edge Case Testing

<Accordion title="Failure Scenarios to Test" icon="fa-exclamation-triangle">

**Scenario 1: Invalid Device ID**
- Set `posDeviceId` to `INVALID_DEVICE_123`
- Expected: `statusCode: "E2081"`, `txnStatus: "failed"`

**Scenario 2: Customer Cancels Payment**
- Initiate payment → Press cancel on device before paying
- Expected: Webhook to `failureAction` URL
- Status API shows: `status: "failed"`

**Scenario 3: Pending Transaction Polling**
- Initiate payment → Call Status API immediately (before customer pays)
- Expected: `status: "pending"` or `"in progress"`
- Poll every 15 seconds until status changes

**Scenario 4: Batch Status Check**
- Initiate 3 test transactions
- Call Status API with all 3 `txnId` values
- Expected: `result[]` array with 3 transaction objects

**Scenario 5: HMAC Signature Mismatch**
- Use incorrect `clientSecret` / `merchantSalt`
- Expected: HTTP 401 or 403 authentication error

**Checkpoint:** ✅ All failure scenarios handled gracefully without system crashes

</Accordion>

---

### Step 2.4: Reconciliation Testing

<Accordion title="Reconciliation Validation" icon="fa-balance-scale">

**✅ Webhook vs. Status API Cross-Check**
- [ ] Webhook `mihpayId` matches Status API `mihpayId`
- [ ] Both show the same final status

**✅ Dashboard Reconciliation**
- [ ] Transaction appears in PayU dashboard within 1 minute
- [ ] Dashboard amount matches API response
- [ ] Dashboard status matches Status API status

**✅ Field Mapping Verification**
- [ ] For DBQR: `field0` has UPI txn ID, `field6` has VPA
- [ ] For Card: `field5` has cardholder name, `field8` has masked card

**✅ Receipt Verification (if device has printer)**
- [ ] Printed receipt has correct amount
- [ ] Custom fields (`printInfo`) appear on receipt
- [ ] GST details printed correctly (if `gstParams` used)

**✅ Reverse Hash Validation (if implemented)**
- [ ] Computed hash matches `reverseHash` from API
- [ ] No hash mismatches detected

</Accordion>

---

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

<Accordion title="Production Migration Steps" icon="fa-rocket">

**Step 1:** Obtain Production Credentials from PayU
- Production partner credentials (`clientId`, `clientSecret`, UUID, OAuth token)
- Production merchant credentials (`mid`, key, salt)
- Production `accountId`
- Production device IDs

**Step 2:** Update Code
- Replace all test credentials with production credentials
- Update both HMAC generation functions (partner + merchant)

**Step 3:** Update API Endpoints (if different)
- Confirm production endpoints with PayU support
- Update Initiate Payment URL (currently: `https://api.payu.in/partner/initiatePayment`)
- Update Check Status URL (currently: `https://info.payu.in/v1/transaction/?mode=bqr`)

**Step 4:** Update Webhook URLs
- Point `successAction` to production webhook endpoint
- Ensure production webhook URL is HTTPS and publicly accessible

**Step 5:** Test with Production Credentials in Staging
- Perform 1-2 small-value real transactions in a controlled environment

**Step 6:** Monitor First Live Transactions Closely
- Watch for any authentication errors
- Verify webhooks arrive correctly
- Confirm dashboard updates

</Accordion>

---

### Step 3.2: Production Readiness Checklist

<Accordion title="Final Go-Live Checklist (15 Points)" icon="fa-tasks">

**✅ Credentials & Authentication**
- [ ] Production partner credentials configured (Initiate Payment)
- [ ] Production merchant credentials configured (Check Status)
- [ ] HMAC signatures use correct production secrets
- [ ] OAuth token refresh logic implemented (if token expires)

**✅ Integration Testing**
- [ ] End-to-end flow tested with production credentials
- [ ] Payment initiated successfully on production device
- [ ] Webhook received at production endpoint
- [ ] Status API verified payment successfully

**✅ Webhook Reliability**
- [ ] Webhook endpoint returns HTTP 200 within 2 seconds
- [ ] Can handle 100+ webhooks per minute (if high volume)
- [ ] Webhook failures trigger retry logic

**✅ Status API Polling**
- [ ] Pending transactions polled every 10-15 seconds
- [ ] Polling stops after status becomes "success" or "failed"
- [ ] Transactions stuck in "pending" > 15 minutes trigger alerts

**✅ Error Handling**
- [ ] Network timeouts trigger automatic retry (max 3 attempts)
- [ ] All API errors logged with full request/response
- [ ] User-friendly error messages displayed (not raw API codes)

**✅ Security**
- [ ] Credentials stored in environment variables or secrets manager
- [ ] API calls made server-side only (never client-side)
- [ ] Reverse hash validation implemented (recommended)
- [ ] Customer card data never logged or stored

**✅ Reconciliation**
- [ ] Daily reconciliation compares orders with PayU settlement reports
- [ ] Uses `merchantUTR` / `bankReferenceNumber` for bank matching
- [ ] Uses `mihpayId` for PayU settlement matching
- [ ] Discrepancies flagged for manual review

**✅ Monitoring & Alerts**
- [ ] API error rate alerts (trigger if > 5%)
- [ ] Webhook failure alerts (no webhook received within 30 seconds)
- [ ] Transaction success rate monitoring
- [ ] Device connectivity monitoring

**✅ Business Continuity**
- [ ] Backup plan if primary device fails (secondary device or manual payment)
- [ ] Process documented for refunds (via dashboard or refund API)
- [ ] On-call support knows how to debug common issues

**✅ Documentation**
- [ ] Internal wiki explains how to add new devices
- [ ] Runbooks for common error scenarios
- [ ] Contact information for PayU support

**✅ Compliance**
- [ ] Transaction logs stored for required duration (e.g., 7 years)
- [ ] PCI-DSS compliance verified (no card data storage)
- [ ] GST invoices generated correctly (if applicable)

**✅ Performance**
- [ ] API response time acceptable (< 3 seconds for initiate, < 2 seconds for status)
- [ ] Database queries optimized for reconciliation
- [ ] No bottlenecks during peak transaction hours

**✅ Testing Edge Cases**
- [ ] Device offline during transaction — what happens?
- [ ] Webhook endpoint down — does Status API polling work?
- [ ] Duplicate `txnId` rejection tested

**✅ User Experience**
- [ ] Clear on-screen messages for all states (success, pending, failed)
- [ ] Receipt printing works reliably (if applicable)
- [ ] Customer receives confirmation (SMS/email) for successful payments

**✅ Rollback Plan**
- [ ] Can switch back to test environment if critical issues arise
- [ ] Database backup available before go-live
- [ ] Rollback runbook documented

</Accordion>

---

You've successfully integrated the complete PayU Omni Integrated Flow. Your system can now:
- ✅ Initiate payments on devices
- ✅ Receive real-time webhooks
- ✅ Verify payment status
- ✅ Reconcile transactions automatically

For detailed API specifications, refer to:
- [Initiate Payment API Reference](#initiate-payment-api)
- [Check Transaction Status API Reference](#check-transaction-status-api)
