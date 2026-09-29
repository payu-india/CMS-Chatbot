---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
---
title: Collect Payment Using PayU Omni
excerpt: Complete integration guide for accepting in-person payments via PayU POS devices
category: 65ee4b13ba7bd6003d0c61b4
slug: collect-payment-using-payu-omni
---

PayU Omni enables you to accept in-person payments through secure POS devices integrated with your ERP, billing, or ordering system. This guide walks you through the complete integration process from device activation to going live.

<Warning>
**Critical Prerequisites**

Before you begin integration:
- Your POS device **MUST be activated and mapped** to your merchant account in the Partner Dashboard
- Partner credentials (`client_id`, `client_secret`, `uuid`) must be obtained
- Merchant `key` and `salt` must be available
- Webhook URL must be configured and publicly accessible (HTTPS)

If any prerequisite is missing, you will encounter authentication or device errors during integration.
</Warning>

---

## Prerequisites

<Info>
### 1. Partner Registration

Sign up for a Partner account to obtain API credentials:

- **Registration URL:** [https://partner.payu.in/app/account/signup](https://partner.payu.in/app/account/signup)
- **Credentials received:** `client_id`, `client_secret`, `uuid`
- **Storage:** Keep these credentials secure; they are required for all API calls
</Info>

<Info>
### 2. Merchant Account Setup

Each merchant must have:
- Active PayU merchant account
- Unique `key` and `salt` (provided by PayU)
- Payment methods enabled (Card, UPI, Wallet, EMI)
- Merchant account linked to your partner account
</Info>

<Warning>
### 3. Device Activation (MANDATORY)

**Every POS device MUST be activated and mapped before it can process payments.**

Skip this step and your integration will fail with error **E342** or **E343**.

See [Step 1.2: Activate Your POS Device](#step-12-activate-your-pos-device) below for detailed activation instructions.
</Warning>

<Info>
### 4. Technical Requirements

- **Programming Language:** Any language supporting HTTP/REST APIs
- **Security:** TLS 1.2 or higher for API calls
- **Webhook Endpoint:** HTTPS endpoint to receive transaction notifications
- **Hash Algorithm:** HMAC-SHA512 for request signatures
- **Token Management:** OAuth 2.0 client credentials flow
</Info>

---

# Step 1: Start Integration

## Step 1.1: Obtain Partner Credentials

**What you need:** Email address and business details

1. Navigate to [partner.payu.in/app/account/signup](https://partner.payu.in/app/account/signup)
2. Complete the partner registration form with your business details
3. Submit the form and await approval (typically 1-2 business days)
4. Once approved, log in to the Partner Dashboard
5. Navigate to **Settings** > **API Credentials**
6. Copy and securely store the following values:
   - `client_id` (e.g., `partner_abc123xyz`)
   - `client_secret` (e.g., `secret_xyz789abc`)
   - `uuid` (e.g., `550e8400-e29b-41d4-a716-446655440000`)

<Warning>
**Never expose `client_secret` in client-side code, version control, or logs.** Store it in environment variables or secure credential management systems.
</Warning>

**Checkpoint:** ✅ You have `client_id`, `client_secret`, and `uuid` stored securely

---

## Step 1.2: Activate Your POS Device

**What you need:**
- Access to PayU Partner Dashboard
- Physical POS device from PayU (with serial number)
- Merchant account credentials

<Warning>
**This step is MANDATORY.** Attempting to initiate payments with an inactive or unmapped device will result in error **E342** (device not found) or **E343** (device not mapped to merchant).
</Warning>


<Cards columns={2}>
  <Card title="1. Access Partner Dashboard" href="https://partner.payu.in">
    Log in to the **PayU Partner Dashboard** and navigate to Device Management

    - Visit [partner.payu.in](https://partner.payu.in) and sign in
    - Go to **Devices** → **Device Management**

    <br />
  </Card>

  <Card title="2. Add & Map Device" href="https://partner.payu.in">
    Register your POS device and link it to the merchant

    - Click **"Add New Device"**
    - Enter **device serial number** (on back of device)
    - Select **merchant account** to map the device

    > ⚠️ Each device can only be mapped to **ONE merchant** at a time

    <br />
  </Card>

  <Card title="3. Configure Payment Methods" href="https://partner.payu.in">
    Enable payment methods for this device

    - Toggle on: 💳 Card | 📱 UPI DBQR | 🔲 QR | 👛 Wallet | 🏦 EMI
    - **Save** and copy the `posDeviceId` value

    > ⚠️ Methods must be enabled at **merchant** AND **device** level

    <br />
  </Card>

  <Card title="4. Verify Activation" href="https://partner.payu.in">
    Confirm device is active and ready

    - ✅ Status shows **"Active"**
    - ✅ `posDeviceId` copied and saved
    - ✅ Payment methods enabled

    <br />
  </Card>
</Cards>

**Checkpoint:** ✅ Device status is "Active" in dashboard | ✅ `posDeviceId` value stored securely

---

## Step 1.3: Generate Partner Access Token

**What you need:** `client_id`, `client_secret` from Step 1.1

PayU uses OAuth 2.0 client credentials flow for partner authentication. Access tokens are valid for **4 hours** and must be refreshed before expiry.

### Token API Endpoint

**HTTP Method:** `POST`

**Environment URLs:**

| Environment | URL |
|-------------|-----|
| UAT | `https://uat-accounts.payu.in/oauth/token` |
| Production | `https://accounts.payu.in/oauth/token` |

### Sample Request

```bash
curl --location 'https://accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=YOUR_CLIENT_ID' \
--data-urlencode 'client_secret=YOUR_CLIENT_SECRET' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=partner_payments'
```

### Sample Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "token_type": "Bearer",
  "expires_in": 14400,
  "scope": "partner_payments"
}
```

<Info>
**Token Best Practices:**
- Store the `access_token` value securely
- Refresh token **before** expiry (recommend refresh at 3.5 hours)
- Implement automatic token refresh logic in your integration
- Handle 401 errors by refreshing token and retrying request
</Info>

**Checkpoint:** ✅ Successfully obtained access token | ✅ Token stored and ready for API calls

---

## Step 1.4: Prepare the Request Parameters

**What you need:** Merchant `key`, `salt`, transaction details, `posDeviceId` from Step 1.2

PayU Omni Initiate Payment API requires specific parameters to process in-person payments through POS devices.

### Mandatory Parameters

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Type</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>accountId</td>
      <td>String</td>
      <td>Merchant's unique account identifier provided by PayU</td>
      <td>ACC_12345</td>
    </tr>
    <tr>
      <td>txnId</td>
      <td>String</td>
      <td>Unique transaction ID from your ERP/billing system. Can be reused for retry only if previous attempt failed.</td>
      <td>TXN_2024011501</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>String</td>
      <td>Transaction amount in decimal format (INR)</td>
      <td>"500.00"</td>
    </tr>
    <tr>
      <td>currency</td>
      <td>String</td>
      <td>Currency code. Always use "INR" for India</td>
      <td>INR</td>
    </tr>
    <tr>
      <td>paymentSource</td>
      <td>String</td>
      <td>Must be "omni" for POS transactions</td>
      <td>omni</td>
    </tr>
    <tr>
      <td>paymentMethod</td>
      <td>String</td>
      <td>Must be "pos" for POS device payments</td>
      <td>pos</td>
    </tr>
    <tr>
      <td>posDeviceId</td>
      <td>String</td>
      <td><strong>Device ID from Partner Dashboard (Step 1.2). Device MUST be activated and mapped to merchant before use.</strong></td>
      <td>DEVICE_ABC123</td>
    </tr>
    <tr>
      <td>posPaymentMethod</td>
      <td>String</td>
      <td>Payment method on device: "sale" (auto-detect - recommended), "qr" (UPI QR), "wallet", "emi", "preauth"</td>
      <td>sale</td>
    </tr>
    <tr>
      <td>callBackActions</td>
      <td>Object</td>
      <td>Webhook URLs for success and failure notifications (HTTPS required)</td>
      <td>See below</td>
    </tr>
    <tr>
      <td>order</td>
      <td>Object</td>
      <td>Order details including line items and UDF fields</td>
      <td>See below</td>
    </tr>
  </tbody>
</table>

### Optional Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| additionalInfo | Object | Additional transaction metadata (e.g., custom messages) | See below |
| omniChannelDetails | Object | Channel and location details | See below |
| gstParams | Object | GST parameters for invoicing | See below |

### callBackActions Object

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| successAction | String | Webhook URL called on successful payment (HTTPS required) | https://yourserver.com/webhook/success |
| failureAction | String | Webhook URL called on failed payment (HTTPS required) | https://yourserver.com/webhook/failure |

### order Object

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| orderId | String | Order ID from your ERP/billing system | ORD_2024011501 |
| orderAmount | String | Total order amount (should match amount field) | "500.00" |

**Optional parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| orderNote | String | Additional notes about the order | "2 items purchased" |
| udf1 to udf5 | String | User-defined fields for custom data (useful for reconciliation) | "Store_Location_A" |

### gstParams Object (Optional)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| gstNumber | String | Merchant's GST number | 27AAPFU0939F1ZV |
| gstAmount | String | Total GST amount | "90.00" |
| cgst | String | Central GST amount | "45.00" |
| sgst | String | State GST amount | "45.00" |
| igst | String | Integrated GST amount | "0.00" |

<Warning>
**Critical POS-Specific Values:**

For PayU Omni POS integration, these fields MUST have exact values:
- `paymentSource` = `"omni"`
- `paymentMethod` = `"pos"`
- `posPaymentMethod` = `"sale"` (recommended for auto-detect) or specific method
- `posDeviceId` = Device ID from Partner Dashboard (Step 1.2)

Using incorrect values will result in validation errors.
</Warning>

**Checkpoint:** ✅ All mandatory parameters prepared | ✅ `posDeviceId` matches active device in dashboard

---


## Step 1.5: Generate Authentication Headers

**What you need:** Merchant `key` and `salt`, request body, current GMT timestamp

PayU Omni uses HMAC-SHA512 signature authentication to secure API requests. You must generate a signature hash and include it in the `authorization` header.

### Required Headers

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| X-Partner-Token | String | Partner access token from Step 1.3 | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... |
| X-PayU-Reseller-UUID | String | Partner UUID from registration | 550e8400-e29b-41d4-a716-446655440000 |
| date | String | Current date-time in GMT format | Mon, 15 Jan 2024 10:30:00 GMT |
| authorization | String | HMAC-SHA512 signature (see generation below) | HMAC 9a8b7c6d5e4f3a2b1c0d9e8f... |
| Content-Type | String | Must be application/json | application/json |

### Signature Generation

The signature ensures request integrity and authenticity.

**Hashing Sequence:**

```
signature_string = "POST" + "|" + request_body_json + "|" + merchant_salt

signature_hash = HMAC_SHA512(signature_string, merchant_salt)

authorization_header = "HMAC " + signature_hash (lowercase hexadecimal)
```

**Important Notes:**
- Compute signature **server-side only** (never in browser/mobile app)
- Use the complete request body JSON as a string (no formatting/whitespace changes)
- The hash must be **lowercase hexadecimal**
- Include "HMAC " prefix in the authorization header

### Sample Code for Signature Generation

```python
import hmac
import hashlib
import json

def generate_signature(request_body, merchant_salt):
    # Convert request body to JSON string
    body_string = json.dumps(request_body, separators=(',', ':'))
    
    # Create signature string
    signature_string = f"POST|{body_string}|{merchant_salt}"
    
    # Generate HMAC-SHA512 hash
    signature = hmac.new(
        merchant_salt.encode('utf-8'),
        signature_string.encode('utf-8'),
        hashlib.sha512
    ).hexdigest()
    
    return f"HMAC {signature}"

# Example usage
request_body = {
    "accountId": "ACC_12345",
    "txnId": "TXN_2024011501",
    "amount": "500.00",
    # ... other parameters
}

merchant_salt = "your_merchant_salt_here"
auth_header = generate_signature(request_body, merchant_salt)
print(auth_header)
```

<Warning>
**Security Best Practices:**
- Never expose `merchant_salt` in client-side code
- Always generate signatures on your backend server
- Rotate merchant salt periodically (contact PayU support)
- Log signature generation for debugging but never log the salt value
</Warning>

**Checkpoint:** ✅ Signature generation logic implemented | ✅ All headers prepared correctly

---

## Step 1.6: POST the Initiate Payment Request

**What you need:** All parameters from Step 1.4, headers from Step 1.5, access token from Step 1.3

This step sends the payment initiation request to PayU, which pushes the payment notification to the POS device.

### API Endpoint

**HTTP Method:** `POST`

**Environment URLs:**

| Environment | URL |
|-------------|-----|
| UAT | `https://apitest.payu.in/partner/initiatePayment` |
| Production | `https://api.payu.in/partner/initiatePayment` |

### Sample Request (cURL)

```bash
curl --location 'https://api.payu.in/partner/initiatePayment' \
--header 'X-Partner-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token' \
--header 'X-PayU-Reseller-UUID: 550e8400-e29b-41d4-a716-446655440000' \
--header 'date: Mon, 15 Jan 2024 10:30:00 GMT' \
--header 'authorization: HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b' \
--header 'Content-Type: application/json' \
--data '{
  "accountId": "ACC_12345",
  "txnId": "TXN_2024011501",
  "amount": "500.00",
  "currency": "INR",
  "paymentSource": "omni",
  "paymentMethod": "pos",
  "posDeviceId": "DEVICE_ABC123",
  "posPaymentMethod": "sale",
  "callBackActions": {
    "successAction": "https://yourserver.com/webhook/success",
    "failureAction": "https://yourserver.com/webhook/failure"
  },
  "order": {
    "orderId": "ORD_2024011501",
    "orderAmount": "500.00",
    "orderNote": "Payment for 2 items",
    "udf1": "Store_Location_A"
  }
}'
```

> **Note:** Replace all placeholder values (`YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, device IDs, merchant credentials) before executing.

<Info>
**What Happens After This Request:**

1. PayU validates the request (credentials, signature, device status)
2. If device is active and mapped → Payment push sent to POS device
3. POS device displays transaction amount and payment options to customer
4. Customer selects payment method and completes payment on device
5. Device shows success/failure message and prints receipt
6. PayU sends webhook notification to your `successAction` or `failureAction` URL
</Info>

### Sample Request in Other Languages

```python
import requests
import json

url = "https://api.payu.in/partner/initiatePayment"

headers = {
    "X-Partner-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token",
    "X-PayU-Reseller-UUID": "550e8400-e29b-41d4-a716-446655440000",
    "date": "Mon, 15 Jan 2024 10:30:00 GMT",
    "authorization": "HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b",
    "Content-Type": "application/json"
}

payload = {
    "accountId": "ACC_12345",
    "txnId": "TXN_2024011501",
    "amount": "500.00",
    "currency": "INR",
    "paymentSource": "omni",
    "paymentMethod": "pos",
    "posDeviceId": "DEVICE_ABC123",
    "posPaymentMethod": "sale",
    "callBackActions": {
        "successAction": "https://yourserver.com/webhook/success",
        "failureAction": "https://yourserver.com/webhook/failure"
    },
    "order": {
        "orderId": "ORD_2024011501",
        "orderAmount": "500.00",
        "orderNote": "Payment for 2 items",
        "udf1": "Store_Location_A"
    }
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

```php
<?php

$url = "https://api.payu.in/partner/initiatePayment";

$headers = [
    "X-Partner-Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token",
    "X-PayU-Reseller-UUID: 550e8400-e29b-41d4-a716-446655440000",
    "date: Mon, 15 Jan 2024 10:30:00 GMT",
    "authorization: HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b",
    "Content-Type: application/json"
];

$payload = json_encode([
    "accountId"        => "ACC_12345",
    "txnId"            => "TXN_2024011501",
    "amount"           => "500.00",
    "currency"         => "INR",
    "paymentSource"    => "omni",
    "paymentMethod"    => "pos",
    "posDeviceId"      => "DEVICE_ABC123",
    "posPaymentMethod" => "sale",
    "callBackActions"  => [
        "successAction" => "https://yourserver.com/webhook/success",
        "failureAction" => "https://yourserver.com/webhook/failure"
    ],
    "order" => [
        "orderId"     => "ORD_2024011501",
        "orderAmount" => "500.00",
        "orderNote"   => "Payment for 2 items",
        "udf1"        => "Store_Location_A"
    ]
]);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    echo "Status Code: " . curl_getinfo($ch, CURLINFO_HTTP_CODE) . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}

curl_close($ch);
?>
```

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class InitiatePayment {
    public static void main(String[] args) {
        String url = "https://api.payu.in/partner/initiatePayment";

        String payload = "{"
            + ""accountId": "ACC_12345","
            + ""txnId": "TXN_2024011501","
            + ""amount": "500.00","
            + ""currency": "INR","
            + ""paymentSource": "omni","
            + ""paymentMethod": "pos","
            + ""posDeviceId": "DEVICE_ABC123","
            + ""posPaymentMethod": "sale","
            + ""callBackActions": {"
            +     ""successAction": "https://yourserver.com/webhook/success","
            +     ""failureAction": "https://yourserver.com/webhook/failure""
            + "},"
            + ""order": {"
            +     ""orderId": "ORD_2024011501","
            +     ""orderAmount": "500.00","
            +     ""orderNote": "Payment for 2 items","
            +     ""udf1": "Store_Location_A""
            + "}"
            + "}";

        try {
            HttpClient client = HttpClient.newHttpClient();

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("X-Partner-Token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token")
                .header("X-PayU-Reseller-UUID", "550e8400-e29b-41d4-a716-446655440000")
                .header("date", "Mon, 15 Jan 2024 10:30:00 GMT")
                .header("authorization", "HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(payload))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class InitiatePayment
{
    static async Task Main(string[] args)
    {
        string url = "https://api.payu.in/partner/initiatePayment";

        string payload = @"{
            ""accountId"": ""ACC_12345"",
            ""txnId"": ""TXN_2024011501"",
            ""amount"": ""500.00"",
            ""currency"": ""INR"",
            ""paymentSource"": ""omni"",
            ""paymentMethod"": ""pos"",
            ""posDeviceId"": ""DEVICE_ABC123"",
            ""posPaymentMethod"": ""sale"",
            ""callBackActions"": {
                ""successAction"": ""https://yourserver.com/webhook/success"",
                ""failureAction"": ""https://yourserver.com/webhook/failure""
            },
            ""order"": {
                ""orderId"": ""ORD_2024011501"",
                ""orderAmount"": ""500.00"",
                ""orderNote"": ""Payment for 2 items"",
                ""udf1"": ""Store_Location_A""
            }
        }";

        try
        {
            using HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.Add("X-Partner-Token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token");
            client.DefaultRequestHeaders.Add("X-PayU-Reseller-UUID", "550e8400-e29b-41d4-a716-446655440000");
            client.DefaultRequestHeaders.Add("date", "Mon, 15 Jan 2024 10:30:00 GMT");
            client.DefaultRequestHeaders.Add("authorization", "HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b");

            StringContent content = new StringContent(payload, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.PostAsync(url, content);
            string responseBody = await response.Content.ReadAsStringAsync();

            Console.WriteLine("Status Code: " + (int)response.StatusCode);
            Console.WriteLine("Response: " + responseBody);
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}
```

```javascript
const url = "https://api.payu.in/partner/initiatePayment";

const headers = {
    "X-Partner-Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example_token",
    "X-PayU-Reseller-UUID": "550e8400-e29b-41d4-a716-446655440000",
    "date": "Mon, 15 Jan 2024 10:30:00 GMT",
    "authorization": "HMAC 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b",
    "Content-Type": "application/json"
};

const payload = {
    accountId: "ACC_12345",
    txnId: "TXN_2024011501",
    amount: "500.00",
    currency: "INR",
    paymentSource: "omni",
    paymentMethod: "pos",
    posDeviceId: "DEVICE_ABC123",
    posPaymentMethod: "sale",
    callBackActions: {
        successAction: "https://yourserver.com/webhook/success",
        failureAction: "https://yourserver.com/webhook/failure"
    },
    order: {
        orderId: "ORD_2024011501",
        orderAmount: "500.00",
        orderNote: "Payment for 2 items",
        udf1: "Store_Location_A"
    }
};

const initiatePayment = async () => {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(payload)
        });

        const responseText = await response.text();
        console.log("Status Code:", response.status);
        console.log("Response:", responseText);
    } catch (error) {
        console.error("Error:", error.message);
    }
};

initiatePayment();
```

**Checkpoint:** ✅ Request sent successfully | ✅ Received 200 response from PayU

---


## Step 1.7: Response Handling & Verification

**What you need:** Webhook endpoint configured to receive PayU notifications

After initiating the payment, you will receive responses at two points:
1. **Immediate API Response** - Confirms request was received
2. **Webhook Notification** - Contains final transaction status after customer completes payment

### Immediate API Response

#### Success Response (Request Accepted)

```json
{
  "metaData": {
    "statusCode": "SUCCESS",
    "message": "Payment request initiated successfully"
  },
  "result": {
    "txnId": "TXN_2024011501",
    "accountId": "ACC_12345",
    "txnStatus": "INITIATED",
    "paymentId": "PAYU_TXN_12345ABC",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

**Status Value:** `INITIATED` means the payment push was sent to the device successfully. This does NOT mean the payment is complete—wait for the webhook.

#### Failure Response (Invalid Device ID)

```json
{
  "metaData": {
    "statusCode": "FAILED",
    "message": "Device not found or not mapped to merchant",
    "errorCode": "E342"
  },
  "result": null
}
```

**Error Code E342:** Device either does not exist or is not activated/mapped in the Partner Dashboard. See [Troubleshooting: Error - Device Not Mapped](#troubleshooting) for resolution steps.

#### Failure Response (Device Not Mapped to Merchant)

```json
{
  "metaData": {
    "statusCode": "FAILED",
    "message": "Device not mapped to this merchant account",
    "errorCode": "E343"
  },
  "result": null
}
```

**Error Code E343:** The device exists but is mapped to a different merchant account. Verify the `accountId` and re-map the device in Partner Dashboard.

#### Failure Response (Configuration Not Enabled)

```json
{
  "metaData": {
    "statusCode": "FAILED",
    "message": "Required payment method not enabled",
    "errorCode": "E344"
  },
  "result": null
}
```

**Error Code E344:** The payment method (Card, UPI, etc.) is not enabled for this merchant or device. Enable it in merchant settings AND device configuration.

### Webhook Payload (Final Transaction Status)

After the customer completes (or cancels) payment on the device, PayU sends a POST request to your `successAction` or `failureAction` webhook URL.

#### Webhook Success Payload

```json
{
  "txnId": "TXN_2024011501",
  "paymentId": "PAYU_TXN_12345ABC",
  "orderId": "ORD_2024011501",
  "amount": "500.00",
  "txnStatus": "SUCCESS",
  "message": "Transaction successful",
  "paymentMethod": "CARD",
  "cardDetails": {
    "cardType": "CREDIT",
    "cardNetwork": "VISA",
    "last4Digits": "1234"
  },
  "timestamp": "2024-01-15T10:32:45Z",
  "hash": "a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0"
}
```

#### Webhook Failure Payload

```json
{
  "txnId": "TXN_2024011501",
  "paymentId": "PAYU_TXN_12345ABC",
  "orderId": "ORD_2024011501",
  "amount": "500.00",
  "txnStatus": "FAILED",
  "message": "Transaction declined by bank",
  "errorCode": "E_PAYMENT_DECLINED",
  "timestamp": "2024-01-15T10:32:45Z",
  "hash": "a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0"
}
```

#### Webhook User Cancelled Payload

```json
{
  "txnId": "TXN_2024011501",
  "paymentId": "PAYU_TXN_12345ABC",
  "txnStatus": "USER_CANCELLED",
  "message": "Payment cancelled by customer",
  "timestamp": "2024-01-15T10:32:45Z"
}
```

### Response Verification Using Reverse Hashing

Always verify the `hash` value in webhook payloads to prevent fraud.

**Reverse Hash Sequence:**

```
hash_string = merchant_salt + "|" + txnStatus + "|" + udf5 + "|" + udf4 + "|" + udf3 + "|" + udf2 + "|" + udf1 + "|" + email + "|" + firstname + "|" + txnId + "|" + amount + "|" + paymentId + "|" + merchant_key

expected_hash = SHA512(hash_string) (lowercase hexadecimal)

if (expected_hash === received_hash) {
    // Webhook is authentic - process the transaction
} else {
    // Potential fraud - reject the webhook
}
```

**Important:** Use empty strings for fields not present in your request (e.g., if you didn't send `email`, use `""` in the hash sequence).

#### Sample Webhook Verification Code (Python)

```python
import hashlib

def verify_webhook_hash(webhook_payload, merchant_key, merchant_salt):
    # Extract values from webhook
    txnId = webhook_payload.get('txnId', '')
    amount = webhook_payload.get('amount', '')
    paymentId = webhook_payload.get('paymentId', '')
    txnStatus = webhook_payload.get('txnStatus', '')
    received_hash = webhook_payload.get('hash', '')
    
    # Build hash string (use empty strings for missing fields)
    hash_string = f"{merchant_salt}|{txnStatus}|||||{txnId}|{amount}|{paymentId}|{merchant_key}"
    
    # Calculate expected hash
    expected_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
    
    # Verify (case-sensitive comparison)
    if expected_hash == received_hash:
        return True  # Authentic webhook
    else:
        return False  # Potential fraud - reject

# Example usage
webhook_data = {
    "txnId": "TXN_2024011501",
    "amount": "500.00",
    "paymentId": "PAYU_TXN_12345ABC",
    "txnStatus": "SUCCESS",
    "hash": "a3b2c1d0e9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0"
}

is_authentic = verify_webhook_hash(webhook_data, "YOUR_MERCHANT_KEY", "YOUR_MERCHANT_SALT")
if is_authentic:
    print("Webhook verified - Update order status to PAID")
else:
    print("Webhook verification failed - Reject this request")
```

<Warning>
**Critical Webhook Security:**
- Always verify the `hash` before processing any webhook
- Never process payment confirmations without hash verification
- Implement HTTPS for your webhook endpoint
- Return HTTP 200 OK response after processing webhook (PayU expects this)
- Log all webhook failures for investigation
</Warning>

**Checkpoint:** ✅ Webhook endpoint implemented | ✅ Hash verification logic working | ✅ Webhook tested successfully

---

## Step 1.8: Verify the Payment

**What you need:** Transaction ID, merchant credentials

After receiving a webhook, use the Check Transaction Status API to cross-verify payment details.

### Why Verify?

- Webhooks can be delayed or missed due to network issues
- Verification ensures you have the latest transaction state
- Required for reconciliation and refund processing

### Check Status API

**Endpoint:** `POST /v1/transaction/?mode=bqr`

**Full Documentation:** See [Check Transaction Status API Reference →](doc:check-transaction-status-api-omni)

### Sample Status Check Request

```bash
curl --location 'https://info.payu.in/v1/transaction/?mode=bqr' \
--header 'mid: YOUR_MERCHANT_ID' \
--header 'Info-Command: check_bqr_txn_status' \
--header 'Content-Type: application/json' \
--data '{
  "merchantKey": "YOUR_MERCHANT_KEY",
  "merchantTransactionIds": ["TXN_2024011501"],
  "hash": "calculated_hash_value"
}'
```

**Best Practices:**
- Call Status API if webhook is not received within 5 minutes
- Implement automatic status polling for pending transactions
- Store status API response for audit trail
- Use status verification during daily reconciliation

**Checkpoint:** ✅ Status API integration implemented | ✅ Cross-verification logic working

---

# Step 2: Test Integration

## Step 2.1: Pre-Payment Validation

Before testing actual payments, validate your integration setup:

1. **Verify Partner Token Generation**
   - Call the OAuth token API
   - Confirm you receive a valid `access_token`
   - Verify token refresh logic works before 4-hour expiry

2. **Verify Device Activation**
   - Log in to Partner Dashboard
   - Navigate to Devices > Device Management
   - Confirm device status shows **"Active"**
   - Verify device is mapped to the correct merchant account
   - Confirm payment methods are enabled

3. **Test Signature Generation**
   - Generate a signature using sample data
   - Verify the hash format is lowercase hexadecimal
   - Test with different request bodies to ensure consistency

4. **Validate Webhook Endpoint**
   - Test your webhook URL is publicly accessible (use tools like webhook.site initially)
   - Confirm HTTPS is enabled
   - Test webhook signature verification logic

**Checkpoint:** ✅ All validation checks passed | ✅ Ready for test transactions

---

## Step 2.2: Simulate a Successful Transaction

Use test credentials to simulate a successful payment flow.

### UAT Environment Details

| Parameter | Value |
|-----------|-------|
| Base URL | https://apitest.payu.in/partner/initiatePayment |
| Token URL | https://uat-accounts.payu.in/oauth/token |
| Status API URL | https://test-info.payu.in/v1/transaction/?mode=bqr |

<Info>
**UAT Device Testing**

> **⚠️ Info Gap:** Contact PayU Integration Support (integration-support@payu.in) to inquire about UAT device provisioning or virtual device testing for your partner account.
</Info>

### Test Transaction Flow

1. **Create Test Order in Your ERP/Billing System**
   - Amount: ₹10.00 (small amount for testing)
   - Generate unique `txnId` and `orderId`

2. **Call Initiate Payment API**
   - Use UAT endpoint
   - Use test merchant credentials
   - Use active UAT device ID

3. **Complete Payment on Device**
   - Device should display ₹10.00 payment request
   - Select payment method (Card/UPI)
   - Complete the payment

4. **Verify Webhook Receipt**
   - Confirm webhook is received at your endpoint
   - Verify `txnStatus: "SUCCESS"`
   - Verify hash is authentic

5. **Call Check Status API**
   - Cross-verify transaction status
   - Confirm details match webhook data

**Test Card Details (UAT):**

> **⚠️ Info Gap:** Test card numbers and UPI IDs for UAT environment not documented. Contact PayU Integration Support for test payment credentials.

**Checkpoint:** ✅ Successful test transaction completed | ✅ Webhook and Status API verified

---

## Step 2.3: Simulate a Failed Transaction

Test error handling for common failure scenarios.

### Failure Scenarios to Test

1. **Invalid Device ID**
   - Use a non-existent `posDeviceId`
   - Expected: Error E342

2. **Device Not Mapped to Merchant**
   - Use a device mapped to a different merchant
   - Expected: Error E343

3. **Payment Method Not Enabled**
   - Disable a payment method in device config
   - Attempt payment with that method
   - Expected: Error E344

4. **Customer Cancels Payment**
   - Initiate payment on device
   - Press "Cancel" on the device
   - Expected: Webhook with `txnStatus: "USER_CANCELLED"`

5. **Expired Token**
   - Use a token older than 4 hours
   - Expected: 401 Unauthorized error

**Checkpoint:** ✅ All failure scenarios tested | ✅ Error handling implemented

---

## Step 2.4: Post-Transaction Verification

Verify the complete end-to-end flow including reconciliation.

1. **Check Webhook Logs**
   - Verify all webhooks are logged in your system
   - Confirm no webhook failures or timeouts
   - Verify hash validation passed for all webhooks

2. **Verify Status API Responses**
   - Call Status API for all test transactions
   - Confirm statuses match webhook notifications
   - Verify all transaction details are accurate

3. **Cross-Verify in Partner Dashboard**
   - Log in to Partner Dashboard
   - Navigate to Transactions
   - Verify all test transactions appear with correct statuses
   - Check transaction details match your records

4. **Test Reconciliation Logic**
   - Generate transaction report from your system
   - Compare with Partner Dashboard transactions
   - Verify all amounts, statuses, and timestamps match

**Checkpoint:** ✅ Reconciliation logic working | ✅ All transactions verified | ✅ Ready for production

---

# Step 3: Going Live — Your Final Checklist

## Step 3.1: Update to Production Credentials

### Generate Live Keys

1. Contact PayU Partner Success team to activate production access
2. Log in to Partner Dashboard (Production)
3. Navigate to Settings > API Credentials
4. Copy production `client_id`, `client_secret`, and `uuid`
5. Obtain production merchant `key` and `salt` for each merchant

### Update Your Code

Replace all UAT credentials and endpoints with production values:

| Component | UAT | Production |
|-----------|-----|------------|
| Token API | https://uat-accounts.payu.in/oauth/token | https://accounts.payu.in/oauth/token |
| Initiate Payment API | https://apitest.payu.in/partner/initiatePayment | https://api.payu.in/partner/initiatePayment |
| Status API | https://test-info.payu.in/v1/transaction/?mode=bqr | https://info.payu.in/v1/transaction/?mode=bqr |
| Partner Client ID | UAT client_id | Production client_id |
| Partner Client Secret | UAT client_secret | Production client_secret |
| Merchant Key/Salt | Test key/salt | Production key/salt |

<Warning>
**Critical:** Store production credentials in secure environment variables, NOT in code or version control.
</Warning>

### Update Production Device IDs

- **Important:** UAT device IDs are different from production device IDs
- Log in to Production Partner Dashboard
- Map production POS devices to merchant accounts
- Copy production `posDeviceId` values
- Update your configuration with production device IDs

**Checkpoint:** ✅ All production credentials updated | ✅ Production device IDs configured | ✅ Code deployed to production environment

---

## Step 3.2: Final Integration Verification

### ✅ Conduct a Live Transaction

1. Create a real order in your production ERP/billing system
2. Use a small amount (₹1 or ₹10) for initial test
3. Call Initiate Payment API with production credentials
4. Complete payment on production POS device
5. Verify customer receives printed receipt

### ✅ Verify the Webhook

1. Confirm webhook is received at your production endpoint
2. Verify `txnStatus: "SUCCESS"`
3. Verify hash authentication passed
4. Confirm transaction status updated in your system

### ✅ Validate the Response Hash

1. Log the received webhook hash
2. Calculate expected hash using reverse hash logic
3. Compare received vs calculated hash (must match exactly)
4. Verify your hash validation function returns TRUE

### ✅ Check successAction / failureAction URLs

1. Verify webhook was sent to correct URL (`successAction` for success)
2. Check webhook logs for any errors
3. Confirm your endpoint returned HTTP 200 OK to PayU

### ✅ Implement a Reconciliation Plan

1. Schedule daily reconciliation jobs
2. Compare your transaction records with Partner Dashboard
3. Use Check Status API for any discrepancies
4. Set up alerts for missing webhooks or status mismatches

**Checkpoint:** ✅ Live transaction successful | ✅ All verifications passed | ✅ Reconciliation process active

---

# Troubleshooting

# PayU Omni Troubleshooting Guide

<Accordion title="Device Activation Issues" icon="fa-list-check">

Use this section to diagnose why a device is not appearing as active or cannot be mapped in the Partner Dashboard.

- **Device not showing as "Active" in dashboard** — Allow up to 5 minutes after registration for the status to refresh. Hard-reload the dashboard and check again.
- **Cannot map device to merchant** — Ensure the merchant account is fully onboarded and in an active state before attempting device mapping.
- **Device serial number not recognized** — Confirm the serial number is entered exactly as printed on the device (case-sensitive, no spaces). Cross-check against the device's settings screen.
- **When to contact Integration Support** — If the device remains inactive after 15 minutes and all checks above pass, escalate to Integration Support with the serial number and merchant ID.

</Accordion>


<Accordion title="Device Not Receiving Payment Push" icon="fa-magnifying-glass">

Follow these steps in order when a device shows as Active in the dashboard but no payment notification arrives on the device.

- **Device appears active but no payment notification** — Confirm that the payment request was submitted successfully (HTTP 200 returned by the API).
- **Check device internet connectivity** — Open a browser on the device and load any public URL to confirm the network is reachable.
- **Verify posDeviceId matches dashboard** — Compare the `posDeviceId` value sent in the API request against the ID listed under Device Management in the Partner Dashboard (exact match required).
- **Restart device and retry** — Power-cycle the device, wait 60 seconds, and resubmit the payment request.
- **Contact support if issue persists** — If the push still does not arrive after a restart, contact Integration Support with the `txnId`, `posDeviceId`, and timestamp of the failed attempt.

</Accordion>


<Accordion title="Error: Device Not Mapped" icon="fa-times-circle">

  <Accordion title="Error Details" icon="fa-times-circle">

  | Field  | Value |
  |--------|-------|
  | **Error Code** | E342 |
  | **Cause** | The device exists in the system but has not been mapped to the merchant account. API calls referencing this device will be rejected until mapping is complete. |

  </Accordion>

  <Accordion title="Resolution Steps" icon="fa-list-check">

  1. Log in to the **Partner Dashboard**.
  2. Navigate to **Device Management → Map Device**.
  3. Select the merchant account and the target device, then confirm the mapping.
  4. **Verify merchant key** — Ensure the `merchantKey` used in the API call matches the key displayed in the merchant's account settings. A mismatch causes mapping lookups to fail even when the device is correctly mapped.

  </Accordion>

</Accordion>


<Accordion title="Error: Required Configurations Not Enabled" icon="fa-times-circle">

  <Accordion title="Cause" icon="fa-times-circle">

  The requested payment method (e.g., UPI, card, wallet) has not been enabled for the merchant account, the specific device, or both. The API rejects the transaction before it reaches the device.

  </Accordion>

  <Accordion title="Resolution Steps" icon="fa-list-check">

  Enable the required payment methods in **both** of the following locations:

  - **Merchant account settings** — Partner Dashboard → Merchant → Payment Methods → toggle on the required method.
  - **Device configuration settings** — Partner Dashboard → Device Management → select device → Allowed Payment Methods → toggle on the required method.

  > **Note:** If both settings appear correct and the error persists, contact Integration Support — the method may require back-end activation on PayU's side.

  </Accordion>

</Accordion>


<Accordion title="Authentication Failures (401 Unauthorized)" icon="fa-key">

  <Accordion title="Common Causes" icon="fa-times-circle">

  - **Invalid or expired partner token** — Partner tokens are valid for **4 hours**. A 401 after that window means the token must be refreshed before retrying.
  - **Malformed token** — Copy-paste errors (extra spaces, truncated strings) result in a token that cannot be validated.
  - **Incorrect signature generation** — The HMAC-SHA256 signature must be computed over the exact concatenated string specified in the API docs; any field order or encoding difference causes a mismatch.

  </Accordion>

  <Accordion title="Resolution Checklist" icon="fa-list-check">

  1. **Refresh the token** — Call the token endpoint with your `client_id` and `client_secret` to obtain a new bearer token.
  2. **Verify `client_id` and `client_secret`** — Retrieve fresh credentials from the Partner Dashboard under **API Credentials**; do not use values cached from earlier sessions.
  3. **Re-validate signature logic** — Log the raw string before hashing and compare it character-by-character against the documented format.
  4. **Check system clock** — Token validation is time-sensitive; ensure the server clock is synced via NTP (drift > 5 minutes can cause failures).

  </Accordion>

</Accordion>


<Accordion title="Payment Timeout or No Response" icon="fa-times-circle">

  <Accordion title="Possible Causes" icon="fa-times-circle">

  - **Customer inaction** — The customer did not complete the payment on the device within the session timeout window.
  - **Device offline** — The device lost network connectivity after the payment push was delivered, preventing the result from being returned.
  - **Network latency** — Intermittent connectivity caused the response to be dropped after a successful transaction.

  </Accordion>

  <Accordion title="Resolution Steps" icon="fa-list-check">

  1. **Check transaction status** — Call the **Check Transaction Status API** using the original `txnId`. This is the authoritative source of truth and works even when the push notification or webhook was not received.
  2. **Interpret the status**:
     - `SUCCESS` — Payment completed; do not retry.
     - `PENDING` — Payment is in-flight; poll again after 30 seconds.
     - `FAILED` / `CANCELLED` — Safe to retry using the **same `txnId`**.
  3. **Never retry with a new `txnId`** before confirming the original is failed/cancelled — doing so risks double-charging.

  </Accordion>

</Accordion>


<Accordion title="Webhook Not Received" icon="fa-shield-check">

  <Accordion title="Configuration Checks" icon="fa-list-check">

  - **Webhook URL configured** — Confirm the URL is saved under **Partner Dashboard → Webhook Settings**. Unsaved changes do not take effect.
  - **Publicly accessible HTTPS endpoint** — The URL must be reachable from PayU's servers over the public internet; `localhost` or private-network URLs will not work. TLS (HTTPS) is mandatory.
  - **Firewall / network settings** — Whitelist PayU's outbound IP ranges on your firewall. Contact Integration Support for the current IP list if needed.

  </Accordion>

  <Accordion title="Validation & Debugging Steps" icon="fa-magnifying-glass">

  1. **Verify signature validation logic** — Re-derive the expected signature on your server using the documented algorithm and compare it with the `X-PayU-Signature` header value in the incoming request.
  2. **Review webhook logs** — Navigate to **Partner Dashboard → Webhook Logs** to see delivery attempts, HTTP response codes your endpoint returned, and PayU's retry history.
  3. **Test with a webhook inspection tool** — Temporarily point the webhook URL to a service such as webhook.site to confirm PayU is dispatching the event correctly before debugging your own endpoint.

  </Accordion>

</Accordion>


<Accordion title="When to Contact Integration Support" icon="fa-clipboard-check">

  <Accordion title="Escalation Scenarios" icon="fa-list-check">

  Contact Integration Support only after completing all relevant self-service steps above. Escalate immediately for:

  - **Device hardware issues** — Physical damage, boot failures, or device not powering on.
  - **Merchant account configuration issues** — Settings that cannot be changed from the Partner Dashboard UI.
  - **Production incident escalation** — Live transactions failing at scale or a systematic API outage.
  - **Persistent errors after self-service** — Any error that reproduces consistently after following all resolution steps in this guide.

  </Accordion>

  <Accordion title="Support Contact Details" icon="fa-clipboard-check">

  **Email:** integration-support@payu.in

  When raising a ticket, include **all** of the following in your first message to avoid back-and-forth:

  | Field | Description |
  |-------|-------------|
  | Merchant ID | Your PayU merchant key/ID |
  | `txnId` | Transaction ID of the affected request |
  | Timestamp | Date and time of the failed event (with timezone) |
  | Error Code | E.g., E342, HTTP 401 |
  | Steps Already Tried | Summary of every resolution step already attempted |

  </Accordion>

</Accordion>


---

# Frequently Asked Questions (FAQ)

<Accordion title="Can one device be used for multiple merchants?" icon="fa-question-circle">

No. Each PayU Omni POS device can only be mapped to **one merchant account** at a time. If you need to process payments for multiple merchants, you must register and activate a separate device for each merchant.

**Why this limitation exists:**
- Device-merchant mapping ensures transaction security and proper fund settlement
- Each merchant has unique credentials and settlement accounts
- Prevents cross-merchant transaction errors

</Accordion>

<Accordion title="How long does device activation take?" icon="fa-question-circle">

Device activation is **instant** once you complete the mapping in the Partner Dashboard. The device should show "Active" status immediately.

**If status doesn't update:**
- Wait 2 minutes and refresh the dashboard
- Verify all required fields were filled during device registration
- Check that payment methods are enabled
- Contact Integration Support if status remains inactive after 5 minutes

</Accordion>

<Accordion title="What happens if I use an incorrect posDeviceId?" icon="fa-question-circle">

You will receive error code **E342** with the message "Device not found or not mapped to merchant."

**Resolution steps:**
1. Log in to Partner Dashboard
2. Navigate to Devices > Device Management
3. Find the device and copy the exact `posDeviceId` value
4. Verify the device is mapped to the merchant account used in the API call
5. Verify device status is "Active"
6. Update your code with the correct `posDeviceId` and retry

</Accordion>

<Accordion title="Can I reuse the same txnId for retry attempts?" icon="fa-question-circle">

**Yes**, but only if the previous transaction failed or timed out.

**Safe to reuse when:**
- Transaction status is "FAILED"
- Transaction status is "USER_CANCELLED"
- Transaction timed out (no status after 10 minutes)

**Do NOT reuse when:**
- Transaction status is "SUCCESS" (will return original transaction details)
- Transaction status is "PENDING" (use Check Status API to verify first)

**Best Practice:** Always call Check Status API before retry to verify the current transaction state.

</Accordion>

<Accordion title="Do payment methods need to be enabled separately for each device?" icon="fa-question-circle">

**Yes.** Payment methods (Card, UPI DBQR, QR, Wallet, EMI) must be enabled at **two levels:**

1. **Merchant account level** (global merchant settings)
2. **Device level** (individual device configuration)

If a payment method is disabled at either level, customers will not see that option on the device.

**How to enable:**
- **Merchant Level:** Contact PayU support or enable in merchant dashboard
- **Device Level:** Partner Dashboard > Devices > Select Device > Configure Payment Methods

</Accordion>

<Accordion title="What should I do if the customer cancels payment on the device?" icon="fa-question-circle">

The transaction will be marked as "USER_CANCELLED" and you will receive a webhook notification.

**Handling customer cancellations:**

1. **Webhook received:** `txnStatus: "USER_CANCELLED"`
2. **Update order status** in your ERP/billing system to "Cancelled" or "Payment Pending"
3. **Display cancellation message** to cashier
4. **Allow customer to retry** with same or different payment method
5. **Do NOT process the order** as payment was not completed

**Retry logic:**
- You can reuse the same `txnId` for retry (transaction failed)
- Or generate a new `txnId` for a fresh transaction

</Accordion>

<Accordion title="How often do I need to refresh the partner access token?" icon="fa-question-circle">

Partner access tokens expire after **4 hours (14,400 seconds).**

**Token refresh best practices:**

✅ **Recommended approach:**
- Refresh token **proactively before expiry** (e.g., at 3 hours 30 minutes)
- Implement automatic token refresh background job
- Store token expiry timestamp when token is generated
- Refresh if `(current_time + 30 minutes) >= expiry_time`

✅ **Handle 401 errors gracefully:**
- If you receive 401 Unauthorized error
- Refresh token immediately
- Retry the original request with new token
- Log token refresh events for monitoring

❌ **Don't:**
- Wait for 401 error to refresh (causes transaction delays)
- Request new token for every API call (inefficient)
- Hard-code token values (tokens expire)

</Accordion>

<Accordion title="What is the maximum transaction amount supported?" icon="fa-question-circle">

> **⚠️ Info Gap:** Maximum transaction limits vary by payment method and merchant configuration.

**To find your limits:**
- Log in to Partner Dashboard > Merchant Settings > Transaction Limits
- Or contact PayU Integration Support: integration-support@payu.in
- Or check your merchant agreement for specific limits

**Common limits (verify with PayU):**
- **Card payments:** Often ₹1,00,000 to ₹2,00,000 per transaction
- **UPI payments:** ₹1,00,000 per transaction (RBI limit)
- **EMI:** Minimum ₹3,000 to ₹5,000 depending on bank

**Note:** Limits may differ for your merchant account based on business category and verification level.

</Accordion>

<Accordion title="Can I test the integration without a physical POS device?" icon="fa-question-circle">

> **⚠️ Info Gap:** Contact PayU Integration Support to inquire about virtual device testing or UAT device provisioning for your partner account.

**Contact Integration Support:**
- **Email:** integration-support@payu.in
- **Include in your request:**
  - Partner account ID
  - Merchant account ID (if available)
  - Testing requirements
  - Expected go-live date

PayU may provide:
- Virtual device simulator for UAT environment
- Temporary UAT device for testing
- Device provisioning for your test merchant accounts

</Accordion>

<Accordion title="Who do I contact if my device has a hardware issue?" icon="fa-question-circle">

For hardware issues (device not powering on, printer malfunction, network connectivity problems, physical damage):

**Contact Integration Support:**
- **Email:** integration-support@payu.in
- **Subject:** "Device Hardware Issue - [Device Serial Number]"

**Include in your email:**
- Device serial number (on back of device)
- Merchant ID the device is mapped to
- Partner account ID
- Description of the issue
- Photos of the issue (if applicable)
- Error messages displayed on device

**Response time:**
- Typically 1-2 business days for hardware issues
- Critical issues: mention "URGENT" in subject line

</Accordion>

---

# Error Code Reference

Complete error code table for PayU Omni integration:

| Error Code | Message | Cause | Resolution |
|------------|---------|-------|------------|
| E000 | Success | Transaction completed successfully | No action needed — transaction successful |
| E342 | Device not found or not mapped to merchant | Device not registered OR not mapped to the merchant account used in API call | 1. Log in to Partner Dashboard<br>2. Go to Devices > Device Management<br>3. Map device to merchant<br>4. Verify device status is "Active" |
| E343 | Device not mapped to merchant | Device exists but not associated with this merchant account | 1. Verify merchant `key` matches account that owns device<br>2. Re-map device to correct merchant in dashboard<br>3. Ensure `accountId` parameter matches device mapping |
| E344 | Required configurations not enabled | Payment method not enabled for merchant or device | 1. Enable payment methods in merchant account settings<br>2. Enable payment methods in device configuration<br>3. Contact PayU support if settings appear correct |
| E2081 | Invalid PG or Bank Code | Incorrect payment gateway or bank code in request | 1. Verify `pg` and `bankcode` parameters<br>2. Use values from PayU documentation<br>3. For POS, use `posPaymentMethod: "sale"` for auto-detect |
| 401 | Unauthorized | Invalid or expired partner token, or incorrect signature | 1. Refresh access token (tokens expire after 4 hours)<br>2. Verify signature generation logic<br>3. Check `client_id` and `client_secret` are correct<br>4. Verify date header is in correct GMT format |
| E_DEVICE_OFFLINE | Device unreachable | Device is not connected to network or powered off | 1. Check device power and network connectivity<br>2. Restart the device<br>3. Retry payment after device comes online<br>4. Contact support if device repeatedly goes offline |
| E_TIMEOUT | Payment timeout | Customer did not complete payment within allowed time (usually 10 minutes) | 1. Use Check Status API to verify final transaction state<br>2. If status is PENDING or FAILED, safe to retry<br>3. If status is SUCCESS, payment completed (don't retry) |
| E_PAYMENT_DECLINED | Payment declined by bank | Insufficient funds, card declined, UPI PIN incorrect, etc. | 1. Display decline message to customer<br>2. Allow customer to retry with same or different payment method<br>3. Safe to reuse same `txnId` for retry<br>4. Customer should contact their bank for card/UPI issues |

<Info>
**Additional Error Codes**

This table covers the most common errors. For a comprehensive error code reference, contact PayU Integration Support at **integration-support@payu.in**.
</Info>

---

# Best Practices

Follow these best practices for a robust PayU Omni integration:

### Device Management
- ✅ Always verify device activation status before initiating payments
- ✅ Store `posDeviceId` values securely in your system configuration
- ✅ Map devices to correct merchant accounts
- ✅ Enable all required payment methods at both merchant and device level
- ✅ Monitor device connectivity and status regularly

### API Integration
- ✅ Implement automatic token refresh (tokens expire every 4 hours)
- ✅ Generate HMAC signatures server-side only (never client-side)
- ✅ Use `posPaymentMethod: "sale"` for auto-detection (recommended)
- ✅ Include unique `txnId` and `orderId` for each transaction
- ✅ Set appropriate timeout values (recommend 30 seconds for API calls)

### Security
- ✅ Validate webhook signatures to prevent fraud
- ✅ Use HTTPS for all webhook endpoints
- ✅ Store credentials in environment variables, not code
- ✅ Never expose `client_secret` or `merchant_salt` in logs
- ✅ Implement rate limiting to prevent API abuse
- ✅ Rotate credentials periodically (contact PayU support)

### Error Handling
- ✅ Implement proper error handling for all error codes
- ✅ Log all API requests and responses (but redact sensitive data)
- ✅ Handle device offline scenarios gracefully
- ✅ Implement retry logic with exponential backoff for transient errors
- ✅ Display user-friendly error messages to cashiers

### Payment Verification
- ✅ Use Check Transaction Status API for payment verification
- ✅ Never rely solely on webhooks (webhooks can be delayed)
- ✅ Implement webhook retry handling
- ✅ Cross-verify webhook data with Status API for high-value transactions
- ✅ Return HTTP 200 OK after processing webhooks (PayU expects this)

### Reconciliation
- ✅ Implement daily reconciliation jobs
- ✅ Compare your transaction records with Partner Dashboard
- ✅ Use Check Status API to resolve discrepancies
- ✅ Set up alerts for missing webhooks or status mismatches
- ✅ Maintain audit logs for all transactions

### Testing
- ✅ Test all payment methods before going live
- ✅ Test error scenarios (invalid device, expired token, etc.)
- ✅ Test customer cancellation flow
- ✅ Verify webhook signature validation
- ✅ Conduct end-to-end testing in UAT environment

### Going Live
- ✅ Complete at least 10 successful test transactions in UAT
- ✅ Verify all failure scenarios are handled
- ✅ Update all credentials to production values
- ✅ Conduct small-value live transaction before full rollout
- ✅ Monitor first 24 hours closely for any issues

---

## Related Resources

- **[PayU Omni Overview →](doc:payu-omni)** - Product features and benefits
- **[Initiate Payment API Reference →](doc:initiate-payment-api-omni)** - Complete API specification
- **[Check Transaction Status API Reference →](doc:check-transaction-status-api-omni)** - Status verification API

---

## Need Help?

<Info>
**Integration Support**

For technical integration assistance, device issues, or account configuration:

📧 **Email:** integration-support@payu.in

**Include in your support request:**
- Partner account ID
- Merchant account ID
- Transaction ID (if applicable)
- Error code and error message
- Steps you've already tried
- Timestamp of the issue

**Response Time:** Typically 1-2 business days for non-critical issues. For urgent production issues, mention "URGENT" in the subject line.
</Info>

---

> 📮 **Postman Collection**  
> Download the PayU Omni Postman Collection: [Coming Soon]
