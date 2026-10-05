---
title: Save Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
# Save Card API

The **Save Card API** enables merchants to store customer card details securely in PayU Vault and obtain a unique token (`cardToken`) for future recurring or one-click checkouts, ensuring compliance with RBI tokenization directives and PCI-DSS standards.

## Endpoint & Environments

| Environment    | Method | URL              |
| :------------- | :----- | :--------------- |
| **Test**       | `POST` | `<redacted URL>` |
| **Production** | `POST` | `<redacted URL>` |

***

## Headers

<HeaderAuthentication />

***

## Request Parameters

The table has 7 rows, so here it is in **HTML format**:

**Mandatory parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>userCredential</code></td>
      <td><code>String</code> Plaintext identifier representing the merchant key and customer ID in the format <code>&lt;merchantKey&gt;:&lt;customerId&gt;</code> (e.g. <code>sms:user12345</code>). Max 100 characters.</td>
    </tr>
    <tr>
      <td><code>cardNumber</code></td>
      <td><code>String</code> 15- or 16-digit Primary Account Number (PAN).</td>
    </tr>
    <tr>
      <td><code>cardName</code></td>
      <td><code>String</code> Name of the cardholder as embossed on the card.</td>
    </tr>
    <tr>
      <td><code>cardExpiryMonth</code></td>
      <td><code>String</code> 2-digit expiry month (<code>01</code>–<code>12</code>).</td>
    </tr>
    <tr>
      <td><code>cardExpiryYear</code></td>
      <td><code>String</code> 4-digit expiry year (e.g. <code>2029</code>).</td>
    </tr>
    <tr>
      <td><code>cardMode</code></td>
      <td><code>String</code> Card type: <code>CC</code> (Credit Card) or <code>DC</code> (Debit Card).</td>
    </tr>
  </tbody>
</table>

**Conditional parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>authRefNumber</code></td>
      <td><code>String</code> Authorization Reference Number provided by issuing bank / card network during customer authentication. Mandatory for <strong>RuPay</strong> and <strong>AMEX</strong> (AEVV) tokenization; optional for Visa and Mastercard.</td>
    </tr>
  </tbody>
</table>

### Sample Request

```bash
curl --location --request POST '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'Date: Mon, 05 Oct 2026 08:30:00 GMT' \
--header 'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"' \
--data-raw '{
  "userCredential": "sms:user12345",
  "cardNumber": "5123456789012346",
  "cardName": "John Doe",
  "cardExpiryMonth": "12",
  "cardExpiryYear": "2029",
  "cardMode": "CC",
  "authRefNumber": "AUTH12345678"
}'
```
```python
import requests
import json

url = "<redacted URL>"

payload = {
    "userCredential": "sms:user12345",
    "cardNumber": "5123456789012346",
    "cardName": "John Doe",
    "cardExpiryMonth": "12",
    "cardExpiryYear": "2029",
    "cardMode": "CC",
    "authRefNumber": "AUTH12345678"
}

headers = {
    "Content-Type": "application/json",
    "Date": "Mon, 05 Oct 2026 08:30:00 GMT",
    "Authorization": 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$curl = curl_init();

$payload = json_encode([
  "userCredential" => "sms:user12345",
  "cardNumber" => "5123456789012346",
  "cardName" => "John Doe",
  "cardExpiryMonth" => "12",
  "cardExpiryYear" => "2029",
  "cardMode" => "CC",
  "authRefNumber" => "AUTH12345678"
]);

curl_setopt_array($curl, [
  CURLOPT_URL => '<redacted URL>',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => $payload,
  CURLOPT_HTTPHEADER => [
    'Content-Type: application/json',
    'Date: Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  ],
]);

$response = curl_exec($curl);
curl_close($curl);
echo $response;
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class SaveCard {
    public static void main(String[] args) throws Exception {
        String payload = """
        {
          "userCredential": "sms:user12345",
          "cardNumber": "5123456789012346",
          "cardName": "John Doe",
          "cardExpiryMonth": "12",
          "cardExpiryYear": "2029",
          "cardMode": "CC",
          "authRefNumber": "AUTH12345678"
        }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Content-Type", "application/json")
            .header("Date", "Mon, 05 Oct 2026 08:30:00 GMT")
            .header("Authorization", "hmac username=\"merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const axios = require('axios');

const data = {
  userCredential: "sms:user12345",
  cardNumber: "5123456789012346",
  cardName: "John Doe",
  cardExpiryMonth: "12",
  cardExpiryYear: "2029",
  cardMode: "CC",
  authRefNumber: "AUTH12345678"
};

const config = {
  method: 'post',
  url: '<redacted URL>',
  headers: { 
    'Content-Type': 'application/json',
    'Date': 'Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization': 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  },
  data: data
};

axios(config)
  .then(response => console.log(JSON.stringify(response.data)))
  .catch(error => console.error(error));
```

***

## Response Parameters

| Parameter           | Type    | Description                                                                                                                       |
| :------------------ | :------ | :-------------------------------------------------------------------------------------------------------------------------------- |
| **status**          | Integer | Status flag: `1` (Success) or `0` (Failure).                                                                                      |
| **message**         | String  | Descriptive message detailing the operation outcome.                                                                              |
| **cardToken**       | String  | Unique token identifier generated by PayU Vault for the stored card. Use this token in subsequent payment requests.               |
| **cardNo**          | String  | Masked card number (e.g. `512345XXXXXX2346`).                                                                                     |
| **cardType**        | String  | Card network brand (e.g. `MAST`, `VISA`, `RUPAY`, `AMEX`).                                                                        |
| **cardCategory**    | String  | Category of card: `CC` or `DC`.                                                                                                   |
| **cardExpiryYear**  | String  | 4-digit card expiry year.                                                                                                         |
| **cardExpiryMonth** | String  | 2-digit card expiry month.                                                                                                        |
| **isExpired**       | Boolean | Indicates whether the card is expired (`true` / `false`).                                                                         |
| **networkToken**    | String  | Network-generated token (returned if tokenization was processed via card network and merchant has requisite PCI-DSS permissions). |
| **issuerToken**     | String  | Issuer-generated token (returned for supported issuing banks).                                                                    |

### Sample Response (Success)

```json
{
  "status": 1,
  "message": "Card saved successfully",
  "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
  "cardNo": "512345XXXXXX2346",
  "cardType": "MAST",
  "cardCategory": "CC",
  "cardExpiryYear": "2029",
  "cardExpiryMonth": "12",
  "isExpired": false
}
```

### Sample Response (Failure)

```json
{
  "status": 0,
  "message": "CardNumber is invalid"
}
```

***

## Next Steps

1. **Store Card Token**:
   - Save the returned `cardToken` in your database linked to the customer's profile for 1-click checkout.
2. **Retrieve Customer Cards at Checkout**:
   - Use the [Get User Cards API](ref:v2_get_user_cards_api) or [Get Payment Instrument API](ref:v2-get-payment-instrument-api) to show saved cards on your payment screen.
3. **Execute Payment with Saved Card**:
   - Pass the `cardToken` and `cvv` in the [Process Transaction with a Saved Card API](ref:process-transaction-with-a-saved-card).
