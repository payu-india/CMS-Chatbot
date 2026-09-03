---
title: Collect Payment using Omni
deprecated: false
hidden: false
metadata:
  robots: index
---
# Initiate Payment API

The Initiate Payment API allows merchants to push payment requests from their billing system to PayU-enabled devices (POS terminals or DBQR displays). This API is the core of the PayU Omni Integrated Flow.

---

## Endpoint

**HTTP Method:** `POST`

**URL:** `/partner/initiatePayment`

**Content-Type:** `application/json`

---

## Environment URLs

| Environment | URL |
| ----------- | ------------------------------------------------------------------------ |
| Production  | `https://api.payu.in/partner/initiatePayment` |

<Warning>
⚠️ **Info Gap:** Test/sandbox environment URL not documented. Contact PayU support for test endpoint details and test credentials.
</Warning>

---

## Sample Request

### cURL

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

> **Note:** Replace all placeholder values with your actual credentials before use.

### Python

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

### PHP

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

### Java

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

---

## Sample Response

### Success Response

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

### Failure Response (Invalid Device ID)

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

### Failure Response (Invalid PG & Bank Code)

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

### Webhook Payload (Sent to successAction/failureAction)

After the payment completes on the device, PayU sends a webhook:

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

<Warning>
⚠️ **Important:** The webhook status may still be "pending". Always call the **Check Transaction Status API** to retrieve final, authoritative payment details.
</Warning>

---

## Request Headers

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `Content-Type` | String | Must be `application/json` | `application/json` |
| `X-Partner-Token` | String | Bearer OAuth token obtained from PayU token API | `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |
| `X-PayU-Reseller-UUID` | String | Partner UUID provided by PayU during onboarding | `550e8400-e29b-41d4-a716-446655440000` |
| `date` | String | Current request date and time in GMT format (RFC 7231) | `Tue, 15 Nov 2023 08:12:31 GMT` |
| `authorization` | String | HMAC-SHA512 signature header. Format: `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex-signature>"` | `hmac username="your_client_id", algorithm="sha512", headers="date", signature="a1b2c3..."` |

<Info>
**HMAC Signature Generation:**
1. Use partner `clientId` as username
2. Use partner `clientSecret` to compute HMAC-SHA512 hash
3. Hash the exact value of the `date` header
4. Output as lowercase hexadecimal
5. Format: `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex>"`
</Info>

---

## Request Parameters

### Mandatory Parameters

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

### Optional Parameters

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

---

## Response Schema

### metaData Object

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `message` | String | Human-readable message describing the result | `Payment initiated successfully` |
| `referenceId` | String | PayU's internal reference ID for this request | `REF_20231115_12345` |
| `statusCode` | String | Result status code (see Error Codes section) | `E000` |
| `txnId` | String | Your transaction ID (echoed back) | `ORD_20231115_001` |
| `txnStatus` | String | Transaction status: `pending` or `failed` | `pending` |
| `unmappedStatus` | String | Internal PayU status: `pending` or `failure` | `pending` |

### result Object

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `paymentId` | String | PayU's unique payment identifier | `PAY_abc123xyz789` |
| `authAction` | String | Authentication action URL (null for Omni) | `null` |
| `otpPostUrl` | String | OTP post URL (null for Omni) | `null` |

---

## Error Codes

| Code | Status | Message | Meaning | Action Required |
| :--- | :--- | :--- | :--- | :--- |
| `E000` | Success | Payment initiated successfully | Payment request accepted. Device activated. Customer can now pay. | Wait for webhook. Then call Check Status API to verify final status. |
| `E2081` | Failed | Invalid Device Id | The `posDeviceId` does not exist or is not linked to your account. | Verify the device ID in your PayU dashboard. Ensure the device is registered and active. |
| `E1101` | Failed | Invalid PG & Bank Code Combination | The `paymentMethod` values are incorrect. | Ensure `paymentMethod.name` and `paymentMethod.bankCode` are both set to `"POS"`. |
| `EX158` | Failed | Merchant Integration Exception - Inactive payment option | Omni product is not enabled for your merchant account. | Contact PayU support to enable the Omni product for your account. |
| `E342` | Failed | Transaction not initiated | Generic failure. Payment request could not be processed. | Check all mandatory parameters. Review API logs for validation errors. Retry with corrected parameters. |

---

## Webhook Schema

After the customer completes payment on the device, PayU sends a webhook to your `successAction` or `failureAction` URL.

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `vendorTxnId` | String | Your transaction ID | `ORD_20231115_001` |
| `txnId` | String | Your transaction ID (duplicate of vendorTxnId) | `ORD_20231115_001` |
| `mihpayId` | String | PayU's internal transaction ID | `403993715534895620` |
| `flowType` | String | Always "ominichannel" for Omni payments | `ominichannel` |
| `message` | String | Instruction to call Status API | `Please use the checkBqrStatusAPI to fetch the final status` |
| `status` | String | May be "pending" (not final) | `pending` |

<Warning>
⚠️ **Critical:** Do NOT rely solely on the webhook status. Always call the **Check Transaction Status API** to retrieve authoritative payment details before marking an order as paid.
</Warning>

---

## Related Resources

- [Check Transaction Status API Reference](#check-transaction-status-api)
- [Integration Guide — Initiate Payment](#integrate-payu-omni-initiate-payment)
- [PayU Omni Overview](#payu-omni-integrated-flow)
