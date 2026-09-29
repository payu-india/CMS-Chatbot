---
title: Partner Payment Link API with UPI Intent
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Payment Link UPI Intent API (**`UPI_PL`**)** allows external partners and resellers to fulfill standard PayU payment links directly via UPI Intent on mobile devices.

By omitting `redirect_url` in the initiation request, PayU returns a standardized `upi_intent_url`. The partner invokes native UPI apps installed on the customer's device without requiring a browser redirect.

<Callout icon="📘" theme="info">
  ### Reference
  For details on how to integrate, refer to [Partner Payment Links with UPI Intent](https://docs.payu.in/docs/partner-payment-links-via-upi-intent)
  
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

### Body Parameters

| Parameter         | Description                                                                                                                                 | Example                           |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------- |
| `payment_link_id` | The full PayU payment link URL. Must belong to an allowlisted PayU domain (e.g., `v.payu.in`).                                              | `https://v.payu.in/PAYUMN/abc123` |
| `phone_number`    | Customer mobile phone number (5–16 numeric digits). Country code prefix is recommended.                                                     | `919820988398`                    |
| `redirect_url`    | **Do not pass** or leave empty. When omitted, PayU evaluates the link configuration and returns the UPI Intent response (`upi_intent_url`). | `""` or omitted                   |

<Warning>
**UPI Configuration Requirement:**
For the `UPI_PL` flow to succeed, the underlying payment link configuration must enforce UPI as the permitted payment mode. If the link does not allow UPI, the API returns an error indicating that UPI Intent cannot be generated.
</Warning>

***

## Sample Request

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer a1b2c3d4e5f67890abcdef1234567890' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "phone_number": "919820988398"
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
    "phone_number": "919820988398"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```
```javascript
const payload = {
  payment_link_id: "https://v.payu.in/PAYUMN/abc123",
  phone_number: "919820988398"
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

public class PaymentLinkUPIInitiate {
    public static void main(String[] args) throws Exception {
        String url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment";
        String jsonPayload = "{"
            + "\"payment_link_id\":\"https://v.payu.in/PAYUMN/abc123\","
            + "\"phone_number\":\"919820988398\""
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
    "phone_number"    => "919820988398"
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
            phone_number = "919820988398"
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
  "upi_intent_url": "upi://pay?pa=payu@axisbank&pn=PayU&am=150.00&tr=28408067218883788&cu=INR&mc=5411",
  "expiry_time": 1735689900
}
```

## Response Parameters

| Field            | Type      | Description                                                                                                                          |
| :--------------- | :-------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| `order_ref_id`   | `string`  | Unique order reference generated by PayU for tracking and verification.                                                              |
| `upi_intent_url` | `string`  | Deep-link URI formatted as per NPCI UPI specs (`upi://pay?...`) used to trigger installed UPI applications on the customer's device. |
| `expiry_time`    | `integer` | Expiration time of the generated payment session in Unix epoch format (seconds).                                                     |

***

## Error Codes and Handling

| HTTP Code          | Error Message                              | Reason                                                              | Resolution                                                               |
| :----------------- | :----------------------------------------- | :------------------------------------------------------------------ | :----------------------------------------------------------------------- |
| `400 Bad Request`  | `Payment link is not valid or expired`     | The link URL does not exist or has expired.                         | Validate link status with the Metadata API before initiating payment.    |
| `400 Bad Request`  | `UPI is not enabled for this payment link` | Payment link config does not allow UPI payments.                    | Enable UPI as a payment option on the link or use the `NON_UPI_PL` flow. |
| `400 Bad Request`  | `Invalid phone number`                     | Phone number length is not between 5 and 16 digits.                 | Ensure the phone number contains numeric characters only.                |
| `401 Unauthorized` | `Auth token is not valid`                  | Missing or expired Bearer token.                                    | Refresh the access token with the `partner_payment_links` scope.         |
| `403 Forbidden`    | `Merchant not linked to reseller`          | The merchant ID on the link is not linked to your reseller account. | Link the merchant to your reseller account in the Reseller Portal.       |
