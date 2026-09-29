---
title: Get Payment Link Metadata API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Get Payment Link Metadata API** allows authorized partners and resellers to query the current state and details of a customer's PayU payment link before attempting payment initiation.

HTTP Method: **GET**

### Endpoints

| Environment    | URL                                                                           |
| :------------- | :---------------------------------------------------------------------------- |
| **Test**       | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata` |
| **Production** | `https://partnerapilayer.payu.in/apilayer/partner/payment-link/metadata`      |

***

## Request Headers

| Header          | Description                                                                                                                    |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | `String `Bearer token obtained from OAuth Token API (`Bearer <access_token>`). Must include the `partner_payment_links` scope. |

***

## Query Parameters

**The&#x20;**`payment_link `**parameter is mandatory.**

| Parameter      | Description                                                                                                               | Example                           |
| :------------- | :------------------------------------------------------------------------------------------------------------------------ | :-------------------------------- |
| `payment_link` | `String` Full URL of the PayU payment link. The domain host must be registered under PayU's allowed payment link domains. | `https://v.payu.in/PAYUMN/abc123` |

<Warning>
**Eligibility Constraints:**
A payment link is **not eligible** for partner fulfillment if:
- It contains custom attributes.
- It allows partial payments.
- It has a zero (`0`) or negative payable amount.
- Its status is not `PENDING`.
</Warning>

***

## Sample Request

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer your_access_token_here'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata"
params = {
    "payment_link": "https://v.payu.in/PAYUMN/abc123"
}
headers = {
    "Authorization": "Bearer your_access_token_here"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```
```javascript
const paymentLink = 'https://v.payu.in/PAYUMN/abc123';
const token = 'your_access_token_here';

const response = await fetch(`https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=${encodeURIComponent(paymentLink)}`, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`
  }
});

const data = await response.json();
console.log(data);
```
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class GetPaymentLinkMetadata {
    public static void main(String[] args) {
        try {
            String paymentLink = URLEncoder.encode("https://v.payu.in/PAYUMN/abc123", StandardCharsets.UTF_8.toString());
            String endpoint = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=" + paymentLink;
            
            URL url = new URL(endpoint);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Authorization", "Bearer your_access_token_here");

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            System.out.println(response.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string paymentLink = Uri.EscapeDataString("https://v.payu.in/PAYUMN/abc123");
        string url = $"https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link={paymentLink}";

        client.DefaultRequestHeaders.Clear();
        client.DefaultRequestHeaders.Add("Authorization", "Bearer your_access_token_here");

        HttpResponseMessage response = await client.GetAsync(url);
        string result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```
```php
<?php
$paymentLink = urlencode("https://v.payu.in/PAYUMN/abc123");
$url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=" . $paymentLink;

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer your_access_token_here"
]);

$response = curl_exec($ch);
curl_close($ch);
echo $response;
?>
```

***

## Response Parameters

| Parameter             | Description                                                    |
| :-------------------- | :------------------------------------------------------------- |
| `amount`              | Total transaction amount payable on the payment link.          |
| `currency`            | Currency code for the transaction (e.g., `INR`).               |
| `description`         | Merchant-defined description or purpose of the payment link.   |
| `payment_link_id`     | The canonical PayU payment link URL submitted in the query.    |
| `payment_link_status` | Current lifecycle state: `PENDING`, `CANCELLED`, or `EXPIRED`. |
| `expiry_time`         | Expiration timestamp in Unix epoch format (in seconds).        |

***

## Sample Response

### Success Scenario&#x20;

`200 OK`

```json
{
  "amount": 100.0,
  "currency": "INR",
  "description": "Test payment link",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "payment_link_status": "PENDING",
  "expiry_time": 1735689600
}
```

### Failure Scenarios

#### 1. Authentication Failure / Invalid Scope (`401 Unauthorized`)

Occurs if the bearer token is missing, expired, or was generated without the `partner_payment_links` scope.

```json
{
  "status": "failed",
  "error": "UNAUTHORIZED",
  "message": "Auth token is not valid"
}
```

#### 2. Payment Link Not Found (`404 Not Found`)

Occurs when the payment link URL does not exist or the link belongs to an unlinked merchant.

```json
{
  "status": "failed",
  "error": "LINK_NOT_FOUND",
  "message": "Payment link not found"
}
```

#### 3. Payment Link Expired (`400 Bad Request`)

Occurs when the link's validity window has elapsed.

```json
{
  "status": "failed",
  "error": "LINK_EXPIRED",
  "message": "Payment link expired"
}
```

#### 4. Payment Link Already Paid (`400 Bad Request`)

Occurs when the payment link was already fulfilled by another transaction.

```json
{
  "status": "failed",
  "error": "LINK_ALREADY_USED",
  "message": "Payment link already used"
}
```