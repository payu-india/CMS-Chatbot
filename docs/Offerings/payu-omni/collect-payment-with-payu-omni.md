---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
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

***

## Prerequisites

### 1. Partner Registration

Sign up for a Partner account to obtain API credentials:
- **Registration URL:** [https://partner.payu.in/app/account/signup](https://partner.payu.in/app/account/signup)
- **Credentials received:** `client_id`, `client_secret`, `uuid`
- **Storage:** Keep these credentials secure; they are required for all API calls

### 2. Merchant Account Setup
Each merchant must have:
- Active PayU merchant account
- Unique `key` and `salt` (provided by PayU)
- Payment methods enabled (Card, UPI, Wallet, EMI)
- Merchant account linked to your partner account


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

***

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

***

## Step 1.2: Generate Partner Access Token

**What you need:** `client_id`, `client_secret` from Step 1.1

PayU uses OAuth 2.0 client credentials flow for partner authentication. Access tokens are valid for **4 hours** and must be refreshed before expiry.

### Token API Endpoint

**HTTP Method:** `POST`

**Environment URLs:**

| Environment | URL                                        |
| ----------- | ------------------------------------------ |
| UAT         | `https://uat-accounts.payu.in/oauth/token` |
| Production  | `https://accounts.payu.in/oauth/token`     |

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

<Callout>
**Token Best Practices:**
- Store the `access_token` value securely
- Refresh token **before** expiry (recommend refresh at 3.5 hours)
- Implement automatic token refresh logic in your integration
- Handle 401 errors by refreshing token and retrying request
</Callout>

**Checkpoint:** ✅ Successfully obtained access token | ✅ Token stored and ready for API calls

***

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

| Parameter          | Type   | Description                                             | Example   |
| :----------------- | :----- | :------------------------------------------------------ | :-------- |
| additionalInfo     | Object | Additional transaction metadata (e.g., custom messages) | See below |
| omniChannelDetails | Object | Channel and location details                            | See below |
| gstParams          | Object | GST parameters for invoicing                            | See below |

### callBackActions Object

**Mandatory parameters**

| Parameter     | Type   | Description                                               | Example                                                                          |
| :------------ | :----- | :-------------------------------------------------------- | :------------------------------------------------------------------------------- |
| successAction | String | Webhook URL called on successful payment (HTTPS required) | [https://yourserver.com/webhook/success](https://yourserver.com/webhook/success) |
| failureAction | String | Webhook URL called on failed payment (HTTPS required)     | [https://yourserver.com/webhook/failure](https://yourserver.com/webhook/failure) |

### order Object

**Mandatory parameters**

| Parameter   | Type   | Description                                    | Example        |
| :---------- | :----- | :--------------------------------------------- | :------------- |
| orderId     | String | Order ID from your ERP/billing system          | ORD_2024011501 |
| orderAmount | String | Total order amount (should match amount field) | "500.00"       |

**Optional parameters**

| Parameter    | Type   | Description                                                     | Example             |
| :----------- | :----- | :-------------------------------------------------------------- | :------------------ |
| orderNote    | String | Additional notes about the order                                | "2 items purchased" |
| udf1 to udf5 | String | User-defined fields for custom data (useful for reconciliation) | "Store_Location_A"  |

### gstParams Object (Optional)

| Parameter | Type   | Description           | Example         |
| :-------- | :----- | :-------------------- | :-------------- |
| gstNumber | String | Merchant's GST number | 27AAPFU0939F1ZV |
| gstAmount | String | Total GST amount      | "90.00"         |
| cgst      | String | Central GST amount    | "45.00"         |
| sgst      | String | State GST amount      | "45.00"         |
| igst      | String | Integrated GST amount | "0.00"          |

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

***

## Step 1.5: Generate Authentication Headers

**What you need:** Merchant `key` and `salt`, request body, current GMT timestamp

PayU Omni uses HMAC-SHA512 signature authentication to secure API requests. You must generate a signature hash and include it in the `authorization` header.

### Required Headers

**Mandatory parameters**

| Parameter            | Type   | Description                                  | Example                                 |
| :------------------- | :----- | :------------------------------------------- | :-------------------------------------- |
| X-Partner-Token      | String | Partner access token from Step 1.3           | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... |
| X-PayU-Reseller-UUID | String | Partner UUID from registration               | 550e8400-e29b-41d4-a716-446655440000    |
| date                 | String | Current date-time in GMT format              | Mon, 15 Jan 2024 10:30:00 GMT           |
| authorization        | String | HMAC-SHA512 signature (see generation below) | HMAC 9a8b7c6d5e4f3a2b1c0d9e8f...        |
| Content-Type         | String | Must be application/json                     | application/json                        |

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

***

## Step 1.6: POST the Initiate Payment Request

**What you need:** All parameters from Step 1.4, headers from Step 1.5, access token from Step 1.3

This step sends the payment initiation request to PayU, which pushes the payment notification to the POS device.

### API Endpoint

**HTTP Method:** `POST`

**Environment URLs:**

| Environment | URL                                               |
| ----------- | ------------------------------------------------- |
| UAT         | `https://apitest.payu.in/partner/initiatePayment` |
| Production  | `https://api.payu.in/partner/initiatePayment`     |

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

<Callout>
**What Happens After This Request:**

1. PayU validates the request (credentials, signature, device status)
2. If device is active and mapped → Payment push sent to POS device
3. POS device displays transaction amount and payment options to customer
4. Customer selects payment method and completes payment on device
5. Device shows success/failure message and prints receipt
6. PayU sends webhook notification to your `successAction` or `failureAction` URL
</Callout>
**Checkpoint:** ✅ Request sent successfully | ✅ Received 200 response from PayU

***

## Step 1.7: Response Handling & Verification

**What you need:** Webhook endpoint configured to receive PayU notifications

After initiating the payment, you will receive responses at two points:

1. **Immediate API Response** - Confirms request was received
2. **Webhook Notification** - Contains final transaction status after customer completes payment

### Sample Response

#### Success Scenario (Request Accepted)

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

#### Failure Scenarios
**Invalid Device ID**

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

**Device Not Mapped to Merchant**

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

**Configuration Not Enabled**

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

<Calloiut>
**Critical Webhook Security:**
- Always verify the `hash` before processing any webhook
- Never process payment confirmations without hash verification
- Implement HTTPS for your webhook endpoint
- Return HTTP 200 OK response after processing webhook (PayU expects this)
- Log all webhook failures for investigation
</Callout>

**Checkpoint:** ✅ Webhook endpoint implemented | ✅ Hash verification logic working | ✅ Webhook tested successfully

***

## Step 1.8: Verify the Payment

**What you need:** Transaction ID, merchant credentials

After receiving a webhook, use the Check Transaction Status API to cross-verify payment details.

**Endpoint:** `POST /v1/transaction/?mode=bqr`

**Full Documentation:** See [Check Transaction Status API Reference →](doc:check-transaction-status-api-omni)

### Sample Request

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

***

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

***

## Step 2.2: Simulate a Successful Transaction

Use test credentials to simulate a successful payment flow.

### UAT Environment Details

| Parameter      | Value                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------- |
| Base URL       | [https://apitest.payu.in/partner/initiatePayment](https://apitest.payu.in/partner/initiatePayment)       |
| Token URL      | [https://uat-accounts.payu.in/oauth/token](https://uat-accounts.payu.in/oauth/token)                     |
| Status API URL | [https://test-info.payu.in/v1/transaction/?mode=bqr](https://test-info.payu.in/v1/transaction/?mode=bqr) |

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

***

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

***

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

***

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

| Component             | UAT                                                                                                      | Production                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Token API             | [https://uat-accounts.payu.in/oauth/token](https://uat-accounts.payu.in/oauth/token)                     | [https://accounts.payu.in/oauth/token](https://accounts.payu.in/oauth/token)                   |
| Initiate Payment API  | [https://apitest.payu.in/partner/initiatePayment](https://apitest.payu.in/partner/initiatePayment)       | [https://api.payu.in/partner/initiatePayment](https://api.payu.in/partner/initiatePayment)     |
| Status API            | [https://test-info.payu.in/v1/transaction/?mode=bqr](https://test-info.payu.in/v1/transaction/?mode=bqr) | [https://info.payu.in/v1/transaction/?mode=bqr](https://info.payu.in/v1/transaction/?mode=bqr) |
| Partner Client ID     | UAT client_id                                                                                            | Production client_id                                                                           |
| Partner Client Secret | UAT client_secret                                                                                        | Production client_secret                                                                       |
| Merchant Key/Salt     | Test key/salt                                                                                            | Production key/salt                                                                            |

<Callout>
**Critical:** Store production credentials in secure environment variables, NOT in code or version control.
</Callout>

***

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

