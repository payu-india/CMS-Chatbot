---
title: Partner Payment Link API - Hosted Checkout Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Payment Link Hosted Checkout API (**`NON_UPI_PL`**)** allows external partners and resellers to fulfill PayU payment links using PayU's multi-method Hosted Payment Page (HPP).

When the partner provides an allowlisted `redirect_url` in the initiation request, PayU returns an `hpp_url`. The partner directs the customer's browser to this URL where they can pay using any merchant-supported payment method (Credit/Debit Cards, Net Banking, EMI, Wallets, and UPI). Upon completion, PayU redirects the customer back to the partner's `redirect_url`.

<Callout icon="📘" theme="info">
  ### Reference

  For details on how to integrate, refer to [Partner Payment Links Integration using Hosted Checkout](https://docs.payu.in/docs/partner-payment-links-integration-using-hosted-checkout)
</Callout>

HTTP Method: **POST**

### Endpoints

| Environment       | URL                                                                          |
| :---------------- | :--------------------------------------------------------------------------- |
| **Sandbox (UAT)** | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment` |
| **Production**    | `https://partnerapilayer.payu.in/apilayer/partner/payment-link/payment`      |

***

## Request Parameters

<Callout icon="📘" theme="info">
  ### All the parameters are mandatory in header and body.
</Callout>

### Request Headers

| Header          | Description                                                                                                         |
| :-------------- | :------------------------------------------------------------------------------------------------------------------ |
| `Authorization` | Bearer token obtained from the OAuth Token API with `scope=partner_payment_links`. Format: `Bearer <access_token>`. |
| `Content-Type`  | Must be `application/json`.                                                                                         |

***

### Body Parameters

| Parameter         | Description                                                                                                                                | Example                                              |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| `payment_link_id` | `String `The full PayU payment link URL. Must belong to an allowlisted PayU domain (e.g., `v.payu.in`).                                    | `https://v.payu.in/`<br />`PAYUMN/abc123`            |
| `phone_number`    | `String `Customer mobile phone number (5–16 numeric digits). Country code prefix is recommended.                                           | `919820988398`                                       |
| `redirect_url`    | `String `The partner callback URL where the customer is redirected after completing or cancelling the transaction on PayU Hosted Checkout. | `https://partner.example.com/`<br />`payment/return` |

<Warning>
**Domain Allowlist Prerequisite:**
The domain and path of `redirect_url` **must be allowlisted** in PayU's payment link configuration. If an unapproved domain is passed, the API responds with an HTTP 400 error (`redirect_url domain not allowed`).
</Warning>

***

## Sample Request

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer a1b2c3d4e5f67890abcdef1234567890' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "phone_number": "919820988398",
  "redirect_url": "https://partner.example.com/payment/return"
}'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment"
headers = {
    "Authorization": "Bearer a1b2c3d4e5f67890abcdef1234567890",
    "Content-Type": "application/json"
}
payload = {
    "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
    "phone_number": "919820988398",
    "redirect_url": "https://partner.example.com/payment/return"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```
```javascript
const payload = {
  payment_link_id: "https://v.payu.in/PAYUMN/abc123",
  phone_number: "919820988398",
  redirect_url: "https://partner.example.com/payment/return"
};

const response = await fetch('https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer a1b2c3d4e5f67890abcdef1234567890',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(payload)
});

const data = await response.json();
console.log(data);
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class PaymentLinkHPPInitiate {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";
        String jsonPayload = "{"
            + "\"payment_link_id\":\"https://v.payu.in/PAYUMN/abc123\","
            + "\"phone_number\":\"919820988398\","
            + "\"redirect_url\":\"https://partner.example.com/payment/return\""
            + "}";

        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Authorization", "Bearer a1b2c3d4e5f67890abcdef1234567890");
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            os.write(jsonPayload.getBytes(StandardCharsets.UTF_8));
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        StringBuilder sb = new StringBuilder();
        while ((line = br.readLine()) != null) sb.append(line);
        System.out.println(sb.toString());
    }
}
```
```php
<?php
$url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";

$payload = [
    "payment_link_id" => "https://v.payu.in/PAYUMN/abc123",
    "phone_number"    => "919820988398",
    "redirect_url"    => "https://partner.example.com/payment/return"
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer a1b2c3d4e5f67890abcdef1234567890",
    "Content-Type: application/json"
]);

$response = curl_exec($ch);
curl_close($ch);
echo $response;
?>
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";
        var payload = new
        {
            payment_link_id = "https://v.payu.in/PAYUMN/abc123",
            phone_number = "919820988398",
            redirect_url = "https://partner.example.com/payment/return"
        };

        var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
        client.DefaultRequestHeaders.Clear();
        client.DefaultRequestHeaders.Add("Authorization", "Bearer a1b2c3d4e5f67890abcdef1234567890");

        HttpResponseMessage response = await client.PostAsync(url, content);
        string result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```

***

## Sample Response

### Success Scenario

```json
{
  "order_ref_id": "28408067218883788",
  "hpp_url": "https://secure.payu.in/_payment?mihpayid=28408067218883788&token=e82f716298a0021c...",
  "expiry_time": 1735689900
}
```

## Response Parameters

| Field          | Type      | Description                                                                                         |
| :------------- | :-------- | :-------------------------------------------------------------------------------------------------- |
| `order_ref_id` | `string`  | Unique order reference generated by PayU for tracking and verification.                             |
| `hpp_url`      | `string`  | Secure URL of the PayU Hosted Payment Page. Redirect the customer's browser or webview to this URL. |
| `expiry_time`  | `integer` | Expiration time of the checkout session in Unix epoch format (seconds).                             |

***

## Error Codes and Handling

| HTTP Code          | Error Message                          | Reason                                                                  | Resolution                                                                        |
| :----------------- | :------------------------------------- | :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| `400 Bad Request`  | `redirect_url domain not allowed`      | The domain of `redirect_url` has not been allowlisted for this partner. | Register your return URL domain with the PayU Partner Integration team.           |
| `400 Bad Request`  | `Payment link is not valid or expired` | The link URL is invalid, cancelled, or passed its expiry time.          | Check the link state via `/payment-link/metadata` before invoking payment.        |
| `400 Bad Request`  | `Invalid phone number`                 | Phone number formatting error (not 5–16 numeric digits).                | Pass valid numeric phone digits without special characters (+, -, spaces).        |
| `401 Unauthorized` | `Auth token is not valid`              | Missing, expired, or invalid OAuth token.                               | Refresh the token using the OAuth Token API with `scope=partner_payment_links`.   |
| `403 Forbidden`    | `Merchant not linked to reseller`      | The link’s merchant MID is not linked to your `reseller_id`.            | Ensure the merchant is mapped under your reseller profile in the Reseller Portal. |