---
title: Collect Payment using Omni
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
---
title: Initiate Payment API - Omni
excerpt: API reference for initiating POS payments via PayU Omni
category: 65ee4b13ba7bd6003d0c61b4
slug: initiate-payment-api-omni
---

The Initiate Payment API allows partners to initiate in-person payment collection via PayU Omni POS devices. This API pushes a payment request to the specified device, enabling customers to complete payment using their preferred method.

<Warning>
**Critical Prerequisite:** The POS device specified in `posDeviceId` **MUST be activated and mapped** to the merchant account before initiating payments. Unmapped or inactive devices will result in error **E342** or **E343**.

See [Device Activation Guide →](doc:collect-payment-using-payu-omni#step-12-activate-your-pos-device)
</Warning>

---

## Endpoint

**HTTP Method:** `POST`

**URL Path:** `/partner/initiatePayment`

**Content-Type:** `application/json`

---

## Environment URLs

| Environment | URL |
| ----------- | --------- |
| UAT         | `https://apitest.payu.in/partner/initiatePayment` |
| Production  | `https://api.payu.in/partner/initiatePayment` |

---

## Prerequisites

Before calling this API, ensure:

<Info>
✅ **Partner Access Token** obtained from OAuth API (valid for 4 hours)  
✅ **POS Device activated** and mapped to merchant in Partner Dashboard  
✅ **Payment methods enabled** for merchant account AND device  
✅ **Merchant credentials** (`key` and `salt`) available  
✅ **Webhook URL** configured in Partner Dashboard (HTTPS required)
</Info>

---

## Sample Request

### cURL

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

> **Note:** Replace all placeholder values with your actual credentials and transaction data before execution.

### Python

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

### PHP

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

### Java

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

### C#

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

### JavaScript

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

---

## Sample Response

### Success Response (Request Accepted)

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

**Status:** `INITIATED` means the payment push was sent to the device. Wait for webhook notification for final status.

### Failure Response (Invalid Device ID - E342)

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

**Cause:** Device is not registered OR not activated in Partner Dashboard.  
**Resolution:** Activate and map device in Partner Dashboard ([Guide →](doc:collect-payment-using-payu-omni#step-12-activate-your-pos-device))

### Failure Response (Device Not Mapped to Merchant - E343)

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

**Cause:** Device exists but is mapped to a different merchant account.  
**Resolution:** Verify `accountId` and re-map device to correct merchant in Partner Dashboard.

### Failure Response (Configuration Not Enabled - E344)

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

**Cause:** Payment method not enabled at merchant level OR device level.  
**Resolution:** Enable payment methods in merchant settings AND device configuration.

### Webhook Payload (Final Transaction Status)

After the customer completes payment on the device, PayU sends a webhook to your `successAction` or `failureAction` URL:

#### Success Webhook

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

<Warning>
**Always verify the `hash` in webhook payloads** to ensure authenticity. See [Webhook Verification Guide →](doc:collect-payment-using-payu-omni#step-17-response-handling--verification)
</Warning>

---

## Request Headers

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| X-Partner-Token | String | Partner access token from OAuth API (valid for 4 hours) | eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... |
| X-PayU-Reseller-UUID | String | Partner UUID from registration | 550e8400-e29b-41d4-a716-446655440000 |
| date | String | Current date-time in GMT format | Mon, 15 Jan 2024 10:30:00 GMT |
| authorization | String | HMAC-SHA512 signature (format: "HMAC <hash>") | HMAC 9a8b7c6d5e4f3a2b1c0d9e8f... |
| Content-Type | String | Must be application/json | application/json |

<Info>
**Signature Generation:** See [Authentication Guide →](doc:collect-payment-using-payu-omni#step-15-generate-authentication-headers) for HMAC-SHA512 signature generation steps.
</Info>

---

## Request Parameters

**Mandatory parameters**

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
      <td><strong>Must be "omni" for POS transactions</strong></td>
      <td>omni</td>
    </tr>
    <tr>
      <td>paymentMethod</td>
      <td>String</td>
      <td><strong>Must be "pos" for POS device payments</strong></td>
      <td>pos</td>
    </tr>
    <tr>
      <td>posDeviceId</td>
      <td>String</td>
      <td><strong>Device ID from Partner Dashboard. Device MUST be activated and mapped to merchant before use.</strong></td>
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

**Optional parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| additionalInfo | Object | Additional transaction metadata (e.g., custom messages) | See below |
| omniChannelDetails | Object | Channel and location details | See below |
| gstParams | Object | GST parameters for invoicing | See below |

---

### callBackActions Object

**Mandatory parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| successAction | String | Webhook URL called on successful payment (HTTPS required) | https://yourserver.com/webhook/success |
| failureAction | String | Webhook URL called on failed payment (HTTPS required) | https://yourserver.com/webhook/failure |

---

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

---

### gstParams Object

**Optional parameters**

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| gstNumber | String | Merchant's GST number | 27AAPFU0939F1ZV |
| gstAmount | String | Total GST amount | "90.00" |
| cgst | String | Central GST amount | "45.00" |
| sgst | String | State GST amount | "45.00" |
| igst | String | Integrated GST amount | "0.00" |

---

## Response Schema

### metaData Object

| Field | Type | Description |
| :--- | :--- | :--- |
| statusCode | String | "SUCCESS" or "FAILED" |
| message | String | Human-readable status message |
| errorCode | String | Error code (present only on failure) |

### result Object

| Field | Type | Description |
| :--- | :--- | :--- |
| txnId | String | Transaction ID from request |
| accountId | String | Merchant account ID |
| txnStatus | String | "INITIATED", "SUCCESS", "FAILED", "PENDING", "USER_CANCELLED" |
| paymentId | String | PayU-generated payment ID |
| timestamp | String | ISO 8601 timestamp |

---

## Error Codes

| Error Code | Message | Cause | Resolution |
|------------|---------|-------|------------|
| E342 | Device not found or not mapped to merchant | Device not registered OR not activated in Partner Dashboard | Activate and map device ([Guide →](doc:collect-payment-using-payu-omni#step-12-activate-your-pos-device)) |
| E343 | Device not mapped to merchant | Device mapped to different merchant account | Verify `accountId` and re-map device |
| E344 | Required configurations not enabled | Payment method not enabled for merchant or device | Enable methods in merchant settings AND device config |
| E2081 | Invalid PG or Bank Code | Incorrect payment gateway or bank code | Use `posPaymentMethod: "sale"` for auto-detect |
| 401 | Unauthorized | Invalid/expired token or incorrect signature | Refresh token and verify signature logic |
| E_DEVICE_OFFLINE | Device unreachable | Device not connected or powered off | Check device connectivity and retry |
| E_TIMEOUT | Payment timeout | Customer didn't complete payment in time | Use Check Status API to verify state |

For complete troubleshooting guide, see [Troubleshooting →](doc:collect-payment-using-payu-omni#troubleshooting)

---

## Related Resources

- **[Collect Payment Using PayU Omni →](doc:collect-payment-using-payu-omni)** - Complete integration guide
- **[Check Transaction Status API →](doc:check-transaction-status-api-omni)** - Verify payment status
- **[PayU Omni Overview →](doc:payu-omni)** - Product features and benefits

---

## Need Help?

**Integration Support:** integration-support@payu.in  
Include: Partner ID, Merchant ID, Transaction ID, error code, and steps tried
