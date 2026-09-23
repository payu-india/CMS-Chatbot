---
title: Collect Payment with PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
# Integrate V2 Payments API for POS

This guide walks you through integrating PayU's V2 Payments API for POS merchants, enabling you to accept in-person payments with advanced device tracking and omnichannel capabilities.

<Warning>
**Prerequisites**

Before starting integration, ensure you have:
- PayU merchant account with **POS enabled** (contact support@payu.in to enable)
- **Registered POS devices** with valid `posDeviceId` values
- **Client ID and Client Secret** from PayU (used for authentication)
- **OAuth Partner Token** and **Reseller UUID** from PayU
- Server-side implementation capability (API requires server-to-server calls)

⚠️ **Critical**: If your POS devices are not registered, you will receive error code `E342` or `E2081`. Complete device registration before proceeding.
</Warning>

***

## Step 1: Start Integration

### Step 1.1: Prepare the Request Parameters

**Mandatory Parameters**

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type &amp; Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><strong>Top-Level Fields</strong></td>
    </tr>
    <tr>
      <td>accountId</td>
      <td><strong>String</strong><br>Merchant account identifier in PayU.</td>
      <td>12345678</td>
    </tr>
    <tr>
      <td>txnId</td>
      <td><strong>String</strong><br>Merchant's unique transaction ID.</td>
      <td>TXN123456789</td>
    </tr>
    <tr>
      <td>amount</td>
      <td><strong>Double / String</strong><br>Transaction amount in Rs. Both String and Double formats are accepted.</td>
      <td>10, 10.55, "10.55"</td>
    </tr>
    <tr>
      <td>currency</td>
      <td><strong>String</strong><br>ISO currency code.</td>
      <td>INR</td>
    </tr>
    <tr>
      <td>paymentSource</td>
      <td><strong>String</strong><br>Source channel of the transaction. For POS-initiated flows, use <code>POS</code> or <code>WEB</code> as per integration.</td>
      <td>POS</td>
    </tr>
    <tr>
      <td colspan="3"><strong>paymentMethod Object</strong></td>
    </tr>
    <tr>
      <td>paymentMethod.name</td>
      <td><strong>String</strong><br>Hardcoded value. Must always be <code>"POS"</code> for POS transactions.</td>
      <td>POS</td>
    </tr>
    <tr>
      <td>paymentMethod.bankCode</td>
      <td><strong>String</strong><br>Hardcoded value. Must always be <code>"POS"</code> for POS transactions.</td>
      <td>POS</td>
    </tr>
    <tr>
      <td colspan="3"><strong>additionalInfo Object</strong></td>
    </tr>
    <tr>
      <td>additionalInfo.txnFlow</td>
      <td><strong>String</strong><br>Hardcoded value. Must always be <code>"seamless"</code> for POS transactions.</td>
      <td>seamless</td>
    </tr>
    <tr>
      <td>additionalInfo.txnS2sFlow</td>
      <td><strong>String</strong><br>Hardcoded value. Must always be <code>"4"</code> for POS transactions.</td>
      <td>4</td>
    </tr>
    <tr>
      <td colspan="3"><strong>callBackActions Object</strong></td>
    </tr>
    <tr>
      <td>callBackActions.successAction</td>
      <td><strong>String</strong><br>Success callback URL. Use a dummy URL for offline POS flows.</td>
      <td>https://example.com/success</td>
    </tr>
    <tr>
      <td colspan="3"><strong>order Object</strong></td>
    </tr>
    <tr>
      <td>order.paymentChargeSpecification.price</td>
      <td><strong>Double / String</strong><br>Transaction amount in Rs. Both String and Double formats are accepted.</td>
      <td>10.55</td>
    </tr>
    <tr>
      <td colspan="3"><strong>omniChannelDetails Object</strong></td>
    </tr>
    <tr>
      <td>omniChannelDetails.posDeviceId</td>
      <td><strong>String</strong><br>Unique POS device identifier registered with PayU.</td>
      <td>POS_DEVICE_001</td>
    </tr>
  </tbody>
</table>

***

**Optional Parameters**

<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Type &amp; Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><strong>callBackActions Object</strong></td>
    </tr>
    <tr>
      <td>callBackActions.failureAction</td>
      <td><strong>String</strong><br>Failure callback URL.</td>
      <td>https://example.com/failure</td>
    </tr>
    <tr>
      <td>callBackActions.cancelAction</td>
      <td><strong>String</strong><br>Cancel callback URL.</td>
      <td>https://example.com/cancel</td>
    </tr>
    <tr>
      <td colspan="3"><strong>order Object</strong></td>
    </tr>
    <tr>
      <td>order.productInfo</td>
      <td><strong>String</strong><br>Product information for the transaction.</td>
      <td>POS Payment</td>
    </tr>
    <tr>
      <td>order.userDefinedFields.udf1</td>
      <td><strong>String</strong><br>User-defined field 1. Can be used for store identifier.</td>
      <td>STORE_001</td>
    </tr>
    <tr>
      <td>order.userDefinedFields.udf2</td>
      <td><strong>String</strong><br>User-defined field 2. Can be used for cashier identifier.</td>
      <td>CASHIER_001</td>
    </tr>
    <tr>
      <td>order.userDefinedFields.udf3–5</td>
      <td><strong>String</strong><br>Additional user-defined custom fields.</td>
      <td>custom_value</td>
    </tr>
    <tr>
      <td colspan="3"><strong>omniChannelDetails Object</strong></td>
    </tr>
    <tr>
      <td>omniChannelDetails.printInfo.printInfo1</td>
      <td><strong>String</strong><br>Custom text to print on receipt line 1.</td>
      <td>Thank you for shopping!</td>
    </tr>
    <tr>
      <td>omniChannelDetails.printInfo.printInfo2</td>
      <td><strong>String</strong><br>Custom text to print on receipt line 2.</td>
      <td>Visit us again.</td>
    </tr>
    <tr>
      <td>omniChannelDetails.additionalInfo.addInfo1</td>
      <td><strong>String</strong><br>Additional information field 1.</td>
      <td>Store: Main Branch</td>
    </tr>
    <tr>
      <td>omniChannelDetails.additionalInfo.addInfo2</td>
      <td><strong>String</strong><br>Additional information field 2.</td>
      <td>Terminal: T001</td>
    </tr>
    <tr>
      <td>omniChannelDetails.userId</td>
      <td><strong>String</strong><br>User identifier for the transaction.</td>
      <td>USER_001</td>
    </tr>
    <tr>
      <td>omniChannelDetails.posPaymentMethod</td>
      <td><strong>String</strong><br>Payment method type at POS. Allowed values: <code>sale</code>, <code>qr</code>, <code>wallet</code>, <code>emi</code>, <code>preauth</code>. If not specified, or an unrecognised value is sent, the POS terminal displays all available payment methods.</td>
      <td>sale</td>
    </tr>
    <tr>
      <td colspan="3"><strong>gstParams Object</strong></td>
    </tr>
    <tr>
      <td>gstParams.invoiceNo</td>
      <td><strong>String</strong><br>Invoice number.</td>
      <td>INV-2024-001</td>
    </tr>
    <tr>
      <td>gstParams.invoiceDate</td>
      <td><strong>String</strong><br>Invoice date in ISO 8601 format with timezone offset.</td>
      <td>2024-01-15T10:30:00+05:30</td>
    </tr>
    <tr>
      <td>gstParams.invoiceName</td>
      <td><strong>String</strong><br>Invoice name or description.</td>
      <td>POS Sale Invoice</td>
    </tr>
    <tr>
      <td>gstParams.gstIn</td>
      <td><strong>String</strong><br>GSTIN number of the merchant.</td>
      <td>22AAAAA0000A1Z5</td>
    </tr>
    <tr>
      <td>gstParams.gst</td>
      <td><strong>String</strong><br>Total GST amount.</td>
      <td>18.00</td>
    </tr>
    <tr>
      <td>gstParams.cgst</td>
      <td><strong>String</strong><br>CGST component of the GST amount.</td>
      <td>9.00</td>
    </tr>
    <tr>
      <td>gstParams.sgst</td>
      <td><strong>String</strong><br>SGST component of the GST amount.</td>
      <td>9.00</td>
    </tr>
    <tr>
      <td>gstParams.igst</td>
      <td><strong>String</strong><br>IGST component of the GST amount.</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>gstParams.cess</td>
      <td><strong>String</strong><br>Cess component of the tax amount.</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>gstParams.gstIncentive</td>
      <td><strong>String</strong><br>GST incentive amount.</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>gstParams.gstPercentage</td>
      <td><strong>String</strong><br>GST percentage applicable to the transaction.</td>
      <td>18</td>
    </tr>
  </tbody>
</table>

<Note>
**POS-Specific Hardcoded Values**

The following fields MUST use exact hardcoded values for POS transactions:
- `paymentMethod.name`: `"POS"`
- `paymentMethod.bankCode`: `"POS"`
- `additionalInfo.txnFlow`: `"seamless"`
- `additionalInfo.txnS2sFlow`: `"4"`

Using any other values will result in transaction failure.
</Note>

***

### Step 1.2: Authentication & Request Headers

The V2 Payments API uses **HMAC-SHA512 signature-based authentication** to secure all requests.

#### Required Headers

| Header                 | Type   | Required | Description                                                                                                                 |
| ---------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------- |
| `Content-Type`         | String | Yes      | Must be `application/json`                                                                                                  |
| `X-Partner-Token`      | String | Yes      | Bearer token provided by PayU during onboarding (format: `Bearer <token>`)                                                  |
| `X-PayU-Reseller-UUID` | String | Yes      | Your unique partner/reseller UUID provided by PayU                                                                          |
| `date`                 | String | Yes      | Current timestamp in RFC 7231 format (GMT). Example: `Tue, 15 Nov 2023 08:12:31 GMT`                                        |
| `authorization`        | String | Yes      | HMAC signature in the format: `hmac username="<clientId>", algorithm="sha512", headers="date", signature="<hex_signature>"` |

***

#### HMAC Signature Generation

The `authorization` header must contain an HMAC-SHA512 signature computed over the `date` header value.

**Algorithm:**

1. **Generate RFC 7231 formatted date string in GMT**
   ```
   Example: "Tue, 15 Nov 2023 08:12:31 GMT"
   ```

2. **Compute HMAC-SHA512 signature**
   ```
   signature = HMAC-SHA512(date_header_value, client_secret)
   ```
   - **Input**: The exact value of the `date` header (not the entire header line)
   - **Secret Key**: Your client secret provided by PayU
   - **Output**: Hex-encoded string (128 characters)

3. **Build the authorization header**
   ```
   authorization: hmac username="<your_client_id>", algorithm="sha512", headers="date", signature="<computed_signature>"
   ```

***

#### Code Samples for Authentication

```python
import hmac
import hashlib
from datetime import datetime
from email.utils import formatdate

def generate_auth_headers(client_id, client_secret):
    # Generate RFC 7231 date
    date_string = formatdate(timeval=None, localtime=False, usegmt=True)
    
    # Compute HMAC-SHA512 signature
    signature = hmac.new(
        client_secret.encode('utf-8'),
        date_string.encode('utf-8'),
        hashlib.sha512
    ).hexdigest()
    
    # Build authorization header
    auth_header = f'hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"'
    
    return {
        'Content-Type': 'application/json',
        'X-Partner-Token': 'Bearer YOUR_PARTNER_TOKEN',
        'X-PayU-Reseller-UUID': 'YOUR_RESELLER_UUID',
        'date': date_string,
        'authorization': auth_header
    }

# Usage:
headers = generate_auth_headers("your_client_id", "your_client_secret")
```
```php
<?php

function generateAuthHeaders($clientId, $clientSecret, $partnerToken, $resellerUuid) {
    // Generate RFC 7231 date
    $dateString = gmdate('D, d M Y H:i:s') . ' GMT';
    
    // Compute HMAC-SHA512 signature
    $signature = hash_hmac('sha512', $dateString, $clientSecret);
    
    // Build authorization header
    $authHeader = 'hmac username="' . $clientId . '", algorithm="sha512", headers="date", signature="' . $signature . '"';
    
    return [
        'Content-Type' => 'application/json',
        'X-Partner-Token' => 'Bearer ' . $partnerToken,
        'X-PayU-Reseller-UUID' => $resellerUuid,
        'date' => $dateString,
        'authorization' => $authHeader
    ];
}

// Usage:
$headers = generateAuthHeaders(
    "your_client_id", 
    "your_client_secret",
    "YOUR_PARTNER_TOKEN",
    "YOUR_RESELLER_UUID"
);
?>
```
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class PayUAuthGenerator {
    
    public static Map<String, String> generateAuthHeaders(
        String clientId, 
        String clientSecret,
        String partnerToken,
        String resellerUuid
    ) throws Exception {
        // Generate RFC 7231 date
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(
            "EEE, dd MMM yyyy HH:mm:ss 'GMT'", 
            Locale.US
        );
        String dateString = ZonedDateTime.now(java.time.ZoneOffset.UTC).format(formatter);
        
        // Compute HMAC-SHA512
        Mac sha512Hmac = Mac.getInstance("HmacSHA512");
        SecretKeySpec secretKey = new SecretKeySpec(
            clientSecret.getBytes("UTF-8"), 
            "HmacSHA512"
        );
        sha512Hmac.init(secretKey);
        byte[] hash = sha512Hmac.doFinal(dateString.getBytes("UTF-8"));
        
        // Hex encode
        StringBuilder hexString = new StringBuilder();
        for (byte b : hash) {
            hexString.append(String.format("%02x", b));
        }
        String signature = hexString.toString();
        
        // Build authorization header
        String authHeader = String.format(
            "hmac username=\"%s\", algorithm=\"sha512\", headers=\"date\", signature=\"%s\"",
            clientId,
            signature
        );
        
        // Return headers map
        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Partner-Token", "Bearer " + partnerToken);
        headers.put("X-PayU-Reseller-UUID", resellerUuid);
        headers.put("date", dateString);
        headers.put("authorization", authHeader);
        
        return headers;
    }
}
```
```javascript
const crypto = require('crypto');

function generateAuthHeaders(clientId, clientSecret, partnerToken, resellerUuid) {
    // Generate RFC 7231 date
    const dateString = new Date().toUTCString();
    
    // Compute HMAC-SHA512 signature
    const signature = crypto
        .createHmac('sha512', clientSecret)
        .update(dateString)
        .digest('hex');
    
    // Build authorization header
    const authHeader = `hmac username="${clientId}", algorithm="sha512", headers="date", signature="${signature}"`;
    
    return {
        'Content-Type': 'application/json',
        'X-Partner-Token': `Bearer ${partnerToken}`,
        'X-PayU-Reseller-UUID': resellerUuid,
        'date': dateString,
        'authorization': authHeader
    };
}

// Usage:
const headers = generateAuthHeaders(
    "your_client_id",
    "your_client_secret",
    "YOUR_PARTNER_TOKEN",
    "YOUR_RESELLER_UUID"
);
```
```csharp
using System;
using System.Security.Cryptography;
using System.Text;
using System.Collections.Generic;

public class PayUAuthGenerator
{
    public static Dictionary<string, string> GenerateAuthHeaders(
        string clientId, 
        string clientSecret,
        string partnerToken,
        string resellerUuid)
    {
        // Generate RFC 7231 date
        string dateString = DateTime.UtcNow.ToString("r");
        
        // Compute HMAC-SHA512 signature
        using (var hmac = new HMACSHA512(Encoding.UTF8.GetBytes(clientSecret)))
        {
            byte[] hashBytes = hmac.ComputeHash(Encoding.UTF8.GetBytes(dateString));
            string signature = BitConverter.ToString(hashBytes).Replace("-", "").ToLower();
            
            // Build authorization header
            string authHeader = $"hmac username=\"{clientId}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"";
            
            // Return headers dictionary
            return new Dictionary<string, string>
            {
                { "Content-Type", "application/json" },
                { "X-Partner-Token", $"Bearer {partnerToken}" },
                { "X-PayU-Reseller-UUID", resellerUuid },
                { "date", dateString },
                { "authorization", authHeader }
            };
        }
    }
}
```

<Note>
**Important Security Notes**

- **Never expose your Client Secret** in client-side code or version control
- Store credentials securely using environment variables or a secrets manager
- Generate the signature server-side only
- The `date` header must be current (within ±5 minutes of server time)
- Use the exact `date` header value for signature computation (no modifications)
</Note>

***

### Step 1.3: POST the Request

**Sample Request (cURL)**

```bash
curl --location 'https://api.payu.in/v2/payments' \
--header 'Content-Type: application/json' \
--header 'X-Partner-Token: Bearer YOUR_PARTNER_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'date: Tue, 15 Nov 2023 08:12:31 GMT' \
--header 'authorization: hmac username="your_client_id", algorithm="sha512", headers="date", signature="COMPUTED_SIGNATURE"' \
--data '{
  "accountId": "12345678",
  "txnId": "TXN20240115001",
  "amount": 1500.00,
  "currency": "INR",
  "paymentSource": "POS",
  "paymentMethod": {
    "name": "POS",
    "bankCode": "POS"
  },
  "additionalInfo": {
    "txnFlow": "seamless",
    "txnS2sFlow": "4"
  },
  "callBackActions": {
    "successAction": "https://yoursite.com/success",
    "failureAction": "https://yoursite.com/failure",
    "cancelAction": "https://yoursite.com/cancel"
  },
  "order": {
    "productInfo": "POS Payment",
    "userDefinedFields": {
      "udf1": "STORE_001",
      "udf2": "CASHIER_001",
      "udf3": "",
      "udf4": "",
      "udf5": ""
    },
    "paymentChargeSpecification": {
      "price": 1500.00
    }
  },
  "omniChannelDetails": {
    "printInfo": {
      "printInfo1": "Thank you for shopping!",
      "printInfo2": "Visit us again"
    },
    "additionalInfo": {
      "addInfo1": "Store: Main Branch",
      "addInfo2": "Terminal: T001"
    },
    "userId": "USER_001",
    "posDeviceId": "POS_DEVICE_001",
    "posPaymentMethod": "sale"
  },
  "gstParams": {
    "invoiceNo": "INV-2024-001",
    "invoiceDate": "2024-01-15T10:30:00+05:30",
    "invoiceName": "POS Sale Invoice",
    "gstIn": "22AAAAA0000A1Z5",
    "gst": "270.00",
    "cgst": "135.00",
    "sgst": "135.00",
    "igst": "0.00",
    "cess": "0.00",
    "gstPercentage": "18"
  }
}'
```

> **Note:** Replace `COMPUTED_SIGNATURE` with the actual HMAC-SHA512 signature generated using the code samples above. The `date` header and signature must be freshly generated for each request.



**Sample Request in Other Languages**

<Accordion title="Python - Complete Request" icon="python">

```python
import requests
import json
import hmac
import hashlib
from email.utils import formatdate

def generate_auth_headers(client_id, client_secret, partner_token, reseller_uuid):
    date_string = formatdate(timeval=None, localtime=False, usegmt=True)
    signature = hmac.new(
        client_secret.encode('utf-8'),
        date_string.encode('utf-8'),
        hashlib.sha512
    ).hexdigest()
    
    auth_header = f'hmac username="{client_id}", algorithm="sha512", headers="date", signature="{signature}"'
    
    return {
        'Content-Type': 'application/json',
        'X-Partner-Token': f'Bearer {partner_token}',
        'X-PayU-Reseller-UUID': reseller_uuid,
        'date': date_string,
        'authorization': auth_header
    }

url = "https://api.payu.in/v2/payments"
headers = generate_auth_headers("client_id", "client_secret", "token", "uuid")

payload = {
    "accountId": "12345678",
    "txnId": "TXN20240115001",
    "amount": 1500.00,
    "currency": "INR",
    "paymentSource": "POS",
    "paymentMethod": {"name": "POS", "bankCode": "POS"},
    "additionalInfo": {"txnFlow": "seamless", "txnS2sFlow": "4"},
    "callBackActions": {
        "successAction": "https://yoursite.com/success",
        "failureAction": "https://yoursite.com/failure",
        "cancelAction": "https://yoursite.com/cancel"
    },
    "order": {
        "productInfo": "POS Payment",
        "userDefinedFields": {"udf1": "STORE_001", "udf2": "CASHIER_001", "udf3": "", "udf4": "", "udf5": ""},
        "paymentChargeSpecification": {"price": 1500.00}
    },
    "omniChannelDetails": {
        "printInfo": {"printInfo1": "Thank you!", "printInfo2": "Visit again"},
        "additionalInfo": {"addInfo1": "Store: Main", "addInfo2": "Terminal: T001"},
        "userId": "USER_001",
        "posDeviceId": "POS_DEVICE_001",
        "posPaymentMethod": "sale"
    },
    "gstParams": {
        "invoiceNo": "INV-2024-001", "invoiceDate": "2024-01-15T10:30:00+05:30",
        "invoiceName": "POS Sale", "gstIn": "22AAAAA0000A1Z5",
        "gst": "270.00", "cgst": "135.00", "sgst": "135.00", 
        "igst": "0.00", "cess": "0.00", "gstPercentage": "18"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Status:", response.status_code)
print("Response:", response.json())
```

</Accordion>

<Accordion title="PHP - Complete Request" icon="php">

```php
<?php
function generateAuthHeaders($clientId, $clientSecret, $partnerToken, $resellerUuid) {
    $dateString = gmdate('D, d M Y H:i:s') . ' GMT';
    $signature = hash_hmac('sha512', $dateString, $clientSecret);
    $authHeader = 'hmac username="' . $clientId . '", algorithm="sha512", headers="date", signature="' . $signature . '"';
    
    return [
        'Content-Type: application/json',
        'X-Partner-Token: Bearer ' . $partnerToken,
        'X-PayU-Reseller-UUID: ' . $resellerUuid,
        'date: ' . $dateString,
        'authorization: ' . $authHeader
    ];
}

$url = "https://api.payu.in/v2/payments";
$headers = generateAuthHeaders("client_id", "client_secret", "token", "uuid");

$payload = [
    "accountId" => "12345678",
    "txnId" => "TXN20240115001",
    "amount" => 1500.00,
    "currency" => "INR",
    "paymentSource" => "POS",
    "paymentMethod" => ["name" => "POS", "bankCode" => "POS"],
    "additionalInfo" => ["txnFlow" => "seamless", "txnS2sFlow" => "4"],
    "callBackActions" => [
        "successAction" => "https://yoursite.com/success",
        "failureAction" => "https://yoursite.com/failure"
    ],
    "order" => [
        "productInfo" => "POS Payment",
        "userDefinedFields" => ["udf1" => "STORE_001", "udf2" => "CASHIER_001"],
        "paymentChargeSpecification" => ["price" => 1500.00]
    ],
    "omniChannelDetails" => [
        "printInfo" => ["printInfo1" => "Thank you!", "printInfo2" => "Visit again"],
        "userId" => "USER_001",
        "posDeviceId" => "POS_DEVICE_001",
        "posPaymentMethod" => "sale"
    ],
    "gstParams" => [
        "invoiceNo" => "INV-2024-001",
        "gst" => "270.00", "cgst" => "135.00", "sgst" => "135.00"
    ]
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));

$response = curl_exec($ch);
echo "Response: " . $response;
curl_close($ch);
?>
```

</Accordion>

---

### Step 1.4: Response Handling

#### Success Response

```json
{
  "metaData": {
    "message": "Transaction initiated successfully",
    "referenceId": "REF123456",
    "statusCode": "E000",
    "txnId": "TXN20240115001",
    "txnStatus": "pending",
    "unmappedStatus": "INITIATED"
  },
  "result": {
    "paymentId": "403993715529994433"
  }
}
```

**Response Fields:**

| Field | Description |
|-------|-------------|
| metaData.statusCode | `E000` = success |
| metaData.txnStatus | `pending`, `success`, `failed` |
| result.paymentId | PayU's payment ID for tracking |

#### Error Responses

<Accordion title="E342: Device Not Registered">

```json
{
  "metaData": {
    "message": "POS device not registered",
    "statusCode": "E342",
    "txnStatus": "failed"
  }
}
```

**Resolution:** Register device in PayU Dashboard → POS Devices

</Accordion>

<Accordion title="E2081: Invalid Device ID">

```json
{
  "metaData": {
    "message": "Invalid device ID",
    "statusCode": "E2081",
    "txnStatus": "failed"
  }
}
```

**Resolution:** Verify exact posDeviceId from dashboard

</Accordion>

<Accordion title="401: Authentication Failed">

**Resolution:** Check Client ID/Secret, regenerate signature with current timestamp

</Accordion>

---

### Step 1.5: Verify Payment via Webhook

#### Webhook Payload

```json
{
  "vendorTxnId": "TXN20240115001",
  "txnId": "403993715529994433",
  "status": "captured",
  "message": "Payment successful"
}
```

#### Webhook Verification

<Accordion title="Python - Webhook Verification">

```python
import hmac
import hashlib

def verify_webhook(headers, client_secret):
    date_header = headers.get('date')
    auth_header = headers.get('authorization')
    
    import re
    match = re.search(r'signature="([^"]+)"', auth_header)
    received_sig = match.group(1)
    
    computed_sig = hmac.new(
        client_secret.encode(), 
        date_header.encode(), 
        hashlib.sha512
    ).hexdigest()
    
    return hmac.compare_digest(computed_sig, received_sig)
```

</Accordion>

---

## Step 2: Test Integration

### Step 2.1: Register Your POS Device

1. Log into PayU Dashboard
2. Go to **POS Devices** → **Register Device**
3. Enter device details, submit
4. Copy the assigned `posDeviceId`
5. Verify status shows "Active"

---

### Step 2.2-2.5: Testing Steps

**2.2 Pre-Payment Validation:** Verify credentials, device registration, hardcoded values

**2.3 Successful Transaction:** Test with ₹10, complete on POS, verify webhook

**2.4 Failed Scenarios:** Test invalid device ID, wrong payment method

**2.5 Verification:** Check webhook delivery, dashboard, reconciliation

---

## Step 3: Going Live

### Step 3.1: Production Credentials

1. Generate live keys from dashboard
2. Store securely (environment variables)
3. Update endpoint to `https://api.payu.in/v2/payments`
4. Update all device IDs to production values

### Step 3.2: Final Checklist

✅ Test ₹1 transaction in production  
✅ Verify webhook endpoint (HTTPS, valid SSL)  
✅ All devices registered and active  
✅ Error handling implemented  
✅ Reconciliation process ready  

<Success>
**Integration Complete!**

Monitor first 24 hours closely. Contact support@payu.in for any issues.
</Success>
