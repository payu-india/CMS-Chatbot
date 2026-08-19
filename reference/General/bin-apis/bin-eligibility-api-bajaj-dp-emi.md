---
title: BIN Eligibility API — Bajaj DP EMI
deprecated: false
hidden: true
metadata:
  robots: index
---
The BIN Eligibility API allows you to check whether a customer is eligible for Bajaj Down Payment (DP) EMI based on their card's Bank Identification Number (BIN). This API returns eligibility status along with tenure-specific information, including the new `emiTerm` and `downPaymentTerm` fields for DP EMI plans.

<Info>
**New Response Fields for DP EMI**

This API extends the existing BIN Eligibility response schema with two additional fields for Down Payment EMI tenures:
- `emiTerm`: Number of months the customer will pay EMI
- `downPaymentTerm`: Down payment expressed as equivalent number of EMI months
</Info>

---

## Endpoint

### POST /v1/bin/binEligibility

| Environment | URL |
| ----------- | --- |
| Test        | `https://apitest.payu.in/issuing-bank/v1/bin/binEligibility` |
| Production  | `https://info.payu.in/issuing-bank/v1/bin/binEligibility` |

---

## Authentication

All requests to the BIN Eligibility API must be authenticated using **HMAC SHA-512 signature-based authentication**.

### Required Headers

| Header | Description | Example |
|--------|-------------|---------|
| `Content-Type` | Must be `application/json` | `application/json` |
| `accept` | Must be `application/json` | `application/json` |
| `Date` | Current UTC time in RFC 1123 format | `Fri, 24 Jan 2025 10:30:45 GMT` |
| `Authorization` | HMAC authorization header (see below) | `hmac username="...", algorithm="sha512", headers="date", signature="..."` |


### Authorization Header Format

```
Authorization: hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<signature>"
```

### How to Generate the Signature

The signature is computed as follows:

**Step 1:** Prepare your request body as a JSON string (no extra whitespace)

**Step 2:** Get the current UTC time in RFC 1123 format (e.g., `Fri, 24 Jan 2025 10:30:45 GMT`)

**Step 3:** Create the signature string:
```
<request_body>|<Date>|<merchant_salt>
```

**Step 4:** Compute the SHA-512 hash of the signature string
- Convert to lowercase hexadecimal
- Zero-pad to 128 characters if needed

**Step 5:** Build the Authorization header using your merchant key and the computed signature

### Example Signature Computation

```
Request Body: {"binType":"bin","bin":"203040","bankName":["BAJFIN"],"amount":1000,"tenureInfo":true}
Date Header:  Fri, 24 Jan 2025 10:30:45 GMT
Merchant Salt: YOUR_MERCHANT_SALT

Signature String:
{"binType":"bin","bin":"203040","bankName":["BAJFIN"],"amount":1000,"tenureInfo":true}|Fri, 24 Jan 2025 10:30:45 GMT|YOUR_MERCHANT_SALT

SHA-512 Hash:
bb56b9204f195e0ab6638170f8d428fa6e0b6afa2d13713535cf1101290c88b6f45aad32ffa9bba8fbc344ffb7a8e0b48752447a51711aea834020bed7cd30ae

Authorization Header:
hmac username="YOUR_MERCHANT_KEY", algorithm="sha512", headers="date", signature="bb56b9204f195e0ab6638170f8d428fa6e0b6afa2d13713535cf1101290c88b6f45aad32ffa9bba8fbc344ffb7a8e0b48752447a51711aea834020bed7cd30ae"
```

<Warning>
**Important Authentication Notes**

- The Date header value used in the signature string must **exactly match** the Date header sent in the request
- The request body used in signature computation must **exactly match** the POST body (character-for-character, including spacing and order)
- Generate a fresh Date and Authorization header for **every request**
- The signature expires and cannot be reused
</Warning>

---
## Request Parameters
| Parameter | Type & Description | Example |
| :--- | :--- | :--- |
| binType<br /><code>mandatory</code> | <code>String</code><br />Specifies the type of BIN lookup to perform. Use `"bin"` for standard BIN-based eligibility checks. | `"bin"` |
| bin<br /><code>mandatory</code> | <code>String</code><br />The BIN (Bank Identification Number) of the customer's credit card. Typically the first 6 digits of the card number. Must be a valid BIN (6-8 digits). | `"203040"` |
| bankName<br /><code>mandatory</code> | <code>Array[String]</code><br />The name(s) of the bank(s) to check eligibility against. For Bajaj DP EMI, use `["BAJFIN"]`. Must contain valid bank codes. | `["BAJFIN"]` |
| amount<br /><code>mandatory</code> | <code>Number</code><br />The transaction amount (in INR) to evaluate for BIN eligibility. Required for DP EMI tenure calculations. Must be a positive number. | `1000` |
| tenureInfo<br /><code>optional</code> | <code>Boolean</code><br />Set to `true` to receive detailed tenure information including DP EMI terms (`emiTerm` and `downPaymentTerm`) in the response. Highly recommended for DP EMI integrations. | `true` |


## Sample Request

```bash
curl --location 'https://info.payu.in/issuing-bank/v1/bin/binEligibility' \
--header 'Content-Type: application/json' \
--header 'accept: application/json' \
--header 'Date: Fri, 24 Jan 2025 10:30:45 GMT' \
--header 'Authorization: hmac username="YOUR_MERCHANT_KEY", algorithm="sha512", headers="date", signature="bb56b9204f195e0ab6638170f8d428fa6e0b6afa2d13713535cf1101290c88b6f45aad32ffa9bba8fbc344ffb7a8e0b48752447a51711aea834020bed7cd30ae"' \
--data '{
  "binType": "bin",
  "bin": "203040",
  "bankName": ["BAJFIN"],
  "amount": 1000,
  "tenureInfo": true
}'
```
```python
import requests
import hashlib
import json
from email.utils import formatdate

# Your PayU credentials
merchant_key = "YOUR_MERCHANT_KEY"
merchant_salt = "YOUR_MERCHANT_SALT"

# API endpoint
url = "https://info.payu.in/issuing-bank/v1/bin/binEligibility"

# Request payload
payload = {
    "binType": "bin",
    "bin": "203040",
    "bankName": ["BAJFIN"],
    "amount": 1000,
    "tenureInfo": True
}

# Convert payload to JSON string (no extra whitespace)
json_body = json.dumps(payload, separators=(',', ':'))

# Generate Date header (RFC 1123 format, UTC)
date_header = formatdate(timeval=None, localtime=False, usegmt=True)

# Create signature string
signature_string = f"{json_body}|{date_header}|{merchant_salt}"

# Compute SHA-512 hash
signature = hashlib.sha512(signature_string.encode('utf-8')).hexdigest().lower().zfill(128)

# Build Authorization header
auth_header = f'hmac username="{merchant_key}", algorithm="sha512", headers="date", signature="{signature}"'

# Set headers
headers = {
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'Date': date_header,
    'Authorization': auth_header
}

# Make the request
response = requests.post(url, headers=headers, data=json_body)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
```
```php
<?php

// Your PayU credentials
$merchantKey = "YOUR_MERCHANT_KEY";
$merchantSalt = "YOUR_MERCHANT_SALT";

// API endpoint
$url = "https://info.payu.in/issuing-bank/v1/bin/binEligibility";

// Request payload
$payload = array(
    "binType" => "bin",
    "bin" => "203040",
    "bankName" => array("BAJFIN"),
    "amount" => 1000,
    "tenureInfo" => true
);

// Convert payload to JSON string (no extra whitespace)
$jsonBody = json_encode($payload, JSON_UNESCAPED_SLASHES);

// Generate Date header (RFC 1123 format, UTC)
$dateHeader = gmdate('D, d M Y H:i:s') . ' GMT';

// Create signature string
$signatureString = $jsonBody . '|' . $dateHeader . '|' . $merchantSalt;

// Compute SHA-512 hash
$signature = hash('sha512', $signatureString);

// Build Authorization header
$authHeader = 'hmac username="' . $merchantKey . '", algorithm="sha512", headers="date", signature="' . $signature . '"';

// Initialize cURL
$curl = curl_init();

curl_setopt_array($curl, array(
    CURLOPT_URL => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => '',
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => 'POST',
    CURLOPT_POSTFIELDS => $jsonBody,
    CURLOPT_HTTPHEADER => array(
        'Content-Type: application/json',
        'accept: application/json',
        'Date: ' . $dateHeader,
        'Authorization: ' . $authHeader
    ),
));

$response = curl_exec($curl);
$httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
$error = curl_error($curl);

curl_close($curl);

if ($error) {
    echo "cURL Error: " . $error . "\n";
} else {
    echo "HTTP Status: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}
?>
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class BinEligibilityAPI {
    public static void main(String[] args) throws Exception {
        // Your PayU credentials
        String merchantKey = "YOUR_MERCHANT_KEY";
        String merchantSalt = "YOUR_MERCHANT_SALT";
        
        // API endpoint
        String url = "https://info.payu.in/issuing-bank/v1/bin/binEligibility";
        
        // Request payload (JSON string)
        String jsonBody = "{\"binType\":\"bin\",\"bin\":\"203040\",\"bankName\":[\"BAJFIN\"],\"amount\":1000,\"tenureInfo\":true}";
        
        // Generate Date header (RFC 1123 format, UTC)
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH);
        String dateHeader = ZonedDateTime.now(ZoneId.of("UTC")).format(formatter);
        
        // Create signature string
        String signatureString = jsonBody + "|" + dateHeader + "|" + merchantSalt;
        
        // Compute SHA-512 hash
        MessageDigest digest = MessageDigest.getInstance("SHA-512");
        byte[] hashBytes = digest.digest(signatureString.getBytes(StandardCharsets.UTF_8));
        StringBuilder signature = new StringBuilder();
        for (byte b : hashBytes) {
            signature.append(String.format("%02x", b));
        }
        String sig = signature.toString();
        
        // Build Authorization header
        String authHeader = String.format("hmac username=\"%s\", algorithm=\"sha512\", headers=\"date\", signature=\"%s\"", 
                                          merchantKey, sig);
        
        // Create HTTP client and request
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("accept", "application/json")
            .header("Date", dateHeader)
            .header("Authorization", authHeader)
            .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
            .build();
        
        // Send request and get response
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println("Status code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class BinEligibilityAPI
{
    static async Task Main(string[] args)
    {
        // Your PayU credentials
        string merchantKey = "YOUR_MERCHANT_KEY";
        string merchantSalt = "YOUR_MERCHANT_SALT";
        
        // API endpoint
        string url = "https://info.payu.in/issuing-bank/v1/bin/binEligibility";
        
        // Request payload (JSON string)
        string jsonBody = "{\"binType\":\"bin\",\"bin\":\"203040\",\"bankName\":[\"BAJFIN\"],\"amount\":1000,\"tenureInfo\":true}";
        
        // Generate Date header (RFC 1123 format, UTC)
        string dateHeader = DateTime.UtcNow.ToString("r");
        
        // Create signature string
        string signatureString = $"{jsonBody}|{dateHeader}|{merchantSalt}";
        
        // Compute SHA-512 hash
        using (SHA512 sha512 = SHA512.Create())
        {
            byte[] hashBytes = sha512.ComputeHash(Encoding.UTF8.GetBytes(signatureString));
            StringBuilder signature = new StringBuilder();
            foreach (byte b in hashBytes)
            {
                signature.Append(b.ToString("x2"));
            }
            string sig = signature.ToString();
            
            // Build Authorization header
            string authHeader = $"hmac username=\"{merchantKey}\", algorithm=\"sha512\", headers=\"date\", signature=\"{sig}\"";
            
            // Create HTTP client and request
            using (HttpClient client = new HttpClient())
            {
                var request = new HttpRequestMessage(HttpMethod.Post, url);
                request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
                request.Headers.Add("accept", "application/json");
                request.Headers.Add("Date", dateHeader);
                request.Headers.Add("Authorization", authHeader);
                
                // Send request and get response
                HttpResponseMessage response = await client.SendAsync(request);
                string responseBody = await response.Content.ReadAsStringAsync();
                
                Console.WriteLine($"Status code: {(int)response.StatusCode}");
                Console.WriteLine($"Response: {responseBody}");
            }
        }
    }
}
```
```javascript
const crypto = require('crypto');
const https = require('https');

// Your PayU credentials
const merchantKey = "YOUR_MERCHANT_KEY";
const merchantSalt = "YOUR_MERCHANT_SALT";

// Request payload
const payload = {
  binType: "bin",
  bin: "203040",
  bankName: ["BAJFIN"],
  amount: 1000,
  tenureInfo: true
};

// Convert payload to JSON string (no extra whitespace)
const jsonBody = JSON.stringify(payload);

// Generate Date header (RFC 1123 format, UTC)
const dateHeader = new Date().toUTCString();

// Create signature string
const signatureString = `${jsonBody}|${dateHeader}|${merchantSalt}`;

// Compute SHA-512 hash
const signature = crypto.createHash('sha512').update(signatureString).digest('hex');

// Build Authorization header
const authHeader = `hmac username="${merchantKey}", algorithm="sha512", headers="date", signature="${signature}"`;

// Prepare request options
const options = {
  hostname: 'info.payu.in',
  path: '/issuing-bank/v1/bin/binEligibility',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'Date': dateHeader,
    'Authorization': authHeader,
    'Content-Length': Buffer.byteLength(jsonBody)
  }
};

// Make the request
const req = https.request(options, (res) => {
  let data = '';
  
  res.on('data', (chunk) => {
    data += chunk;
  });
  
  res.on('end', () => {
    console.log(`Status Code: ${res.statusCode}`);
    console.log(`Response: ${data}`);
  });
});

req.on('error', (error) => {
  console.error('Error:', error);
});

req.write(jsonBody);
req.end();
```

> **Note:** Replace `YOUR_MERCHANT_KEY` and regenerate the signature using your actual `MERCHANT_SALT`. The signature shown above is for demonstration only and will not work without the correct salt.

---
## Sample Response

### Customer Eligible

```json
{
  "message": "User is eligible",
  "status": 1,
  "result": [
    {
      "bank": "BAJFIN",
      "tenureInfo": {
        "BAJFIN06": {
          "isEligible": 1
        },
        "BJDP0903": {
          "isEligible": 1,
          "emiTerm": 6,
          "downPaymentTerm": 3
        },
        "BAJFIN02": {
          "isEligible": 1
        },
        "BAJFIN03": {
          "isEligible": 0
        },
        "BAJFIN12": {
          "isEligible": 0
        },
        "BAJFIN08": {
          "isEligible": 0
        },
        "BAJFIN09": {
          "isEligible": 0
        }
      }
    }
  ]
}
```

### Customer Not Eligible

```json
{
  "message": "User is not eligible",
  "status": 0,
  "result": [
    {
      "bank": "BAJFIN",
      "tenureInfo": {
        "BAJFIN06": {
          "isEligible": 0
        },
        "BJDP0903": {
          "isEligible": 0,
          "emiTerm": 6,
          "downPaymentTerm": 3
        },
        "BAJFIN02": {
          "isEligible": 0
        },
        "BAJFIN03": {
          "isEligible": 0
        },
        "BAJFIN12": {
          "isEligible": 0
        },
        "BAJFIN08": {
          "isEligible": 0
        },
        "BAJFIN09": {
          "isEligible": 0
        }
      }
    }
  ]
}
```

---

## Request Parameters

| Parameter | Type & Description | Example |
| :--- | :--- | :--- |
| binType<br /><code>mandatory</code> | <code>String</code><br />Specifies the type of BIN lookup to perform. Use `"bin"` for standard BIN-based eligibility checks. | `"bin"` |
| bin<br /><code>mandatory</code> | <code>String</code><br />The BIN (Bank Identification Number) of the customer's credit card. Typically the first 6 digits of the card number. | `"203040"` |
| bankName<br /><code>mandatory</code> | <code>Array[String]</code><br />The name(s) of the bank(s) to check eligibility against. For Bajaj DP EMI, use `["BAJFIN"]`. | `["BAJFIN"]` |
| amount<br /><code>mandatory</code> | <code>Number</code><br />The transaction amount (in INR) to evaluate for BIN eligibility. Required for DP EMI tenure calculations. | `1000` |
| tenureInfo<br /><code>optional</code> | <code>Boolean</code><br />Set to `true` to receive detailed tenure information including DP EMI terms in the response. Recommended for DP EMI integrations. | `true` |

<Note>
**Parameter Validation Rules**

- `bin`: Must be a valid BIN (6-8 digits)
- `bankName`: Must contain valid bank codes (e.g., `BAJFIN` for Bajaj Finserv)
- `amount`: Must be a positive number representing INR amount
- `tenureInfo`: When set to `true`, response will include `emiTerm` and `downPaymentTerm` fields for DP EMI tenures
</Note>

---

## Response Schema

| Field | Type | Description |
| :--- | :--- | :--- |
| `message` | String | Human-readable message indicating eligibility status (e.g., "User is eligible", "User is not eligible") |
| `status` | Integer | Eligibility indicator: `1` = eligible for at least one tenure, `0` = not eligible for any tenure |
| `result[]` | Array | Array of bank-specific eligibility results |
| `result[].bank` | String | Bank code (e.g., `"BAJFIN"` for Bajaj Finserv) |
| `result[].tenureInfo` | Object | Tenure-specific eligibility information keyed by tenure code (e.g., `BJDP0903`, `BAJFIN06`) |
| `result[].tenureInfo[tenureCode].isEligible` | Integer | `1` if customer is eligible for this specific tenure, `0` if not |
| `result[].tenureInfo[tenureCode].emiTerm` | Integer | **[DP EMI only]** Number of months the customer will pay EMI installments |
| `result[].tenureInfo[tenureCode].downPaymentTerm` | Integer | **[DP EMI only]** Down payment expressed as equivalent number of EMI months (Down Payment Amount = Monthly EMI × downPaymentTerm) |

---

## Understanding Bajaj DP EMI Response Fields

The response includes two specialized fields for Down Payment (DP) EMI tenures, which are only present for tenure codes that support DP EMI plans (e.g., `BJDP0903`):

### Field Definitions

- **`emiTerm`**: The number of months over which the customer will pay the EMI installments **after** making the down payment.
- **`downPaymentTerm`**: The down payment amount expressed as an equivalent number of monthly EMI installments.

### Calculation Example

For tenure code `BJDP0903` with the following response:
```json
{
  "isEligible": 1,
  "emiTerm": 6,
  "downPaymentTerm": 3
}
```

**Interpretation:**
- Customer must pay a down payment equivalent to **3 months** of EMI
- Then pay the monthly EMI for **6 months**
- **Total tenure**: 3 (down payment) + 6 (EMI) = 9 months

**If the monthly EMI is ₹500:**
- Down Payment = ₹500 × 3 = **₹1,500** (paid upfront)
- Monthly EMI = **₹500** (paid for 6 months)
- Total amount = ₹1,500 + (₹500 × 6) = **₹4,500**

**Customer payment journey:**
1. Pay ₹1,500 at the time of purchase (down payment)
2. Pay ₹500/month for the next 6 months

### Standard EMI vs DP EMI

| Tenure Type | Response Fields | Payment Structure |
|-------------|----------------|-------------------|
| **Standard EMI** (e.g., `BAJFIN06`) | Only `isEligible` | Equal monthly installments, no down payment |
| **DP EMI** (e.g., `BJDP0903`) | `isEligible`, `emiTerm`, `downPaymentTerm` | Down payment + EMI installments |

<Note>
**Tenure Code Format**

Tenure codes follow these patterns:
- `BAJFIN##`: Standard Bajaj Finserv EMI (## = number of months)
  - Example: `BAJFIN06` = 6-month standard EMI
- `BJDP####`: Bajaj Down Payment EMI (## = tenure details encoded)
  - Example: `BJDP0903` = 9-month total tenure (3 months down payment + 6 months EMI)
</Note>

---

## Error Codes

The BIN Eligibility API returns standard HTTP status codes along with descriptive error messages.

### HTTP Status Codes

| Status Code | Meaning | Common Causes |
|-------------|---------|---------------|
| `200` | Success | Request processed successfully |
| `400` | Bad Request | Invalid or missing request parameters |
| `401` | Unauthorized | Invalid or missing authentication signature |
| `429` | Too Many Requests | Rate limit exceeded |
| `500` | Internal Server Error | Server-side processing error |

### Common Error Messages

#### 400 Bad Request

```json
{
  "status": 0,
  "message": "binType is mandatory"
}
```

**Possible 400 error messages:**
- `"binType is mandatory"`
- `"bin is mandatory"`
- `"bin must be a valid BIN number"`
- `"bankName is mandatory"`
- `"bankName must be an array"`
- `"amount is mandatory"`
- `"amount must be a positive number"`
- `"Invalid request format"`

#### 401 Unauthorized

```json
{
  "status": 0,
  "message": "Invalid or missing signature"
}
```

**Possible 401 error messages:**
- `"Invalid or missing signature"`
- `"Merchant not allowed to use this API"`
- `"Date header is missing or invalid"`
- `"Authorization header is malformed"`

**Common causes:**
- Incorrect merchant key or salt
- Signature computation mismatch
- Date header not matching signature computation
- Request body modified after signature computation

#### 429 Too Many Requests

```json
{
  "status": 0,
  "message": "Requests limit reached"
}
```

**Recommendation:** Implement exponential backoff retry logic.

#### 500 Internal Server Error

```json
{
  "status": 0,
  "message": "Internal server error"
}
```

**Recommendation:** Log the error details and retry after a delay. Contact PayU support if the issue persists.

---

## Troubleshooting Authentication Errors

If you're receiving `401 Unauthorized` errors, verify the following:

### Checklist

✅ **Merchant credentials are correct**
- Verify you're using the correct merchant key for the environment (test/production)
- Confirm your merchant salt is correct

✅ **Date header is properly formatted**
- Must be in RFC 1123 format: `Day, DD Mon YYYY HH:MM:SS GMT`
- Must be in UTC timezone
- Example: `Fri, 24 Jan 2025 10:30:45 GMT`

✅ **Signature computation is correct**
- Signature string format: `<request_body>|<Date>|<merchant_salt>`
- Request body must be the **exact** JSON string sent in the POST request (same spacing, same order)
- Date must be the **exact** value from the Date header
- Use SHA-512 algorithm (not SHA-256)
- Convert hash to lowercase hexadecimal
- Zero-pad to 128 characters if needed

✅ **Headers are sent correctly**
- All four headers are present: `Content-Type`, `accept`, `Date`, `Authorization`
- Authorization header format matches exactly: `hmac username="...", algorithm="sha512", headers="date", signature="..."`

✅ **Request body matches signature**
- The JSON body sent in the POST request must exactly match the body used in signature computation
- Check for extra whitespace, different key ordering, or encoding issues

### Debug Example

**Incorrect signature computation (will fail):**
```
// Request body with extra whitespace
{
  "binType": "bin",
  "bin": "203040",
  "bankName": ["BAJFIN"],
  "amount": 1000,
  "tenureInfo": true
}

// This won't match the compact JSON sent in the actual request!
```

**Correct signature computation:**
```
// Compact JSON (no extra whitespace)
{"binType":"bin","bin":"203040","bankName":["BAJFIN"],"amount":1000,"tenureInfo":true}

// Use this exact string in signature computation
```