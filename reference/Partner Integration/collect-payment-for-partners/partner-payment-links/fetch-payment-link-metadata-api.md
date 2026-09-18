---
title: Fetch Payment Link Metadata API
deprecated: false
hidden: true
metadata:
  robots: index
---
Retrieve payment link details including amount, currency, status, and expiry before initiating a payment.

***

## Endpoint

**GET** `/apilayer/partner/payment-link/metadata`

| Environment | URL                                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| UAT         | [https://uat-api.payu.in/apilayer/partner/payment-link/metadata](https://uat-api.payu.in/apilayer/partner/payment-link/metadata) |
| Production  | ⚠️ **Contact PayU team for production API base URL**                                                                             |

***

## Authentication

Requires OAuth2 Bearer token with `partner_payment_links` scope.

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

***

## Sample Request

```bash
curl --location 'https://uat-api.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
```

```python
import requests

url = "https://uat-api.payu.in/apilayer/partner/payment-link/metadata"

headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}

params = {
    "payment_link": "https://v.payu.in/PAYUMN/abc123"
}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"An error occurred: {req_err}")
```

```php
<?php

$base_url = "https://uat-api.payu.in/apilayer/partner/payment-link/metadata";
$payment_link = "https://v.payu.in/PAYUMN/abc123";
$url = $base_url . "?payment_link=" . urlencode($payment_link);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
]);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_errno($ch)) {
    echo "cURL Error: " . curl_error($ch);
    curl_close($ch);
    exit;
}

curl_close($ch);

if ($http_code >= 400) {
    echo "HTTP Error: $http_code\n";
    echo "Response: $response\n";
    exit;
}

echo "Status Code: $http_code\n";
echo "Response: $response\n";

?>
```

```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.ConnectException;
import java.net.http.HttpTimeoutException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;

public class FetchPaymentLinkMetadata {
    public static void main(String[] args) {
        try {
            String baseUrl = "https://uat-api.payu.in/apilayer/partner/payment-link/metadata";
            String paymentLink = URLEncoder.encode("https://v.payu.in/PAYUMN/abc123", StandardCharsets.UTF_8);
            String url = baseUrl + "?payment_link=" + paymentLink;

            HttpClient client = HttpClient.newBuilder()
                    .connectTimeout(Duration.ofSeconds(30))
                    .build();

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Authorization", "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...")
                    .GET()
                    .timeout(Duration.ofSeconds(30))
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            
            int statusCode = response.statusCode();
            System.out.println("Status Code: " + statusCode);
            System.out.println("Response: " + response.body());
            
            if (statusCode >= 400) {
                System.err.println("HTTP Error: " + statusCode);
            }
            
        } catch (ConnectException e) {
            System.err.println("Connection error: " + e.getMessage());
        } catch (HttpTimeoutException e) {
            System.err.println("Request timeout: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

***

## Sample Response

```json
{
  "amount": 10000,
  "currency": "INR",
  "description": "Order #12345 payment",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}
```

***

## Request Parameters

**Mandatory Parameters**

| Parameter     | Type & Description                                                                                                                             | Example                           |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| payment_link  | **string** · _Query Parameter_ · The full PayU payment link URL. The URL host must be one of the configured PayU payment link allowed domains. | `https://v.payu.in/PAYUMN/abc123` |
| Authorization | **string** · _Header_ · OAuth2 Bearer token with `partner_payment_links` scope. Format: `Bearer <access_token>`                                | `Bearer eyJhbGciOiJSUzI1...`      |

<Callout icon="ℹ️" theme="info">
  ### There are no optional parameters for this endpoint.
</Callout>

***

## Response Schema

| Field                 | Type    | Description                                                                                                                    |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `amount`              | number  | Payment link amount (in smallest currency unit, e.g., paise for INR). Example: `10000` = ₹100.00                               |
| `currency`            | string  | Three-letter ISO 4217 currency code (e.g., `INR`)                                                                              |
| `description`         | string  | Payment link description or order details                                                                                      |
| `payment_link_id`     | string  | Full PayU payment link URL (same as request parameter)                                                                         |
| `payment_link_status` | string  | Payment link status. Possible values: `PENDING`, `CANCELLED`, `EXPIRED`, `COMPLETED`                                           |
| `expiry_time`         | integer | Link expiry as Unix epoch timestamp (seconds since Jan 1, 1970 UTC). Validate this is in the future before initiating payment. |

<Info>
**Validation Before Payment Initiation**

Always validate:
- ✅ `payment_link_status` is `PENDING` (not `CANCELLED`, `EXPIRED`, or `COMPLETED`)
- ✅ `expiry_time` is greater than current Unix timestamp
- ✅ `amount` and `currency` match expected values

Do not proceed with payment initiation if validation fails.
</Info>

***

## Error Codes

| HTTP Status | Error Message              | Cause                                                  | Resolution                                                                  |
| ----------- | -------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------- |
| 401         | `Auth token is not valid`  | Invalid or expired OAuth access token                  | Generate a new access token using the OAuth Token Generation API            |
| 404         | `Payment link not found`   | Payment link URL doesn't exist or is invalid           | Verify the payment link URL is correct and belongs to your merchant account |
| 400         | `Payment link expired`     | Payment link has passed its expiry time                | Generate a new payment link for the customer                                |
| 400         | `Invalid payment link URL` | Payment link domain is not in allowed domains list     | Contact PayU team to add the domain to allowed payment-link domains         |
| 403         | `Unauthorized access`      | OAuth token doesn't have `partner_payment_links` scope | Verify your OAuth application configuration includes the required scope     |
| 500         | `Internal server error`    | Server-side error                                      | Retry after a few seconds. Contact PayU support if error persists.          |

> **⚠️ Info Gap:** Complete HTTP status code mapping not documented. The error messages listed above are from the PDF but HTTP status codes may vary. Consult PayU team for comprehensive error code documentation.
