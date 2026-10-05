---
title: Get Payment Details API (Crytogram)
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Payment Details API** allows merchants to fetch tokenized card payment details and generate a transaction-specific cryptographic authentication value (**cryptogram / TAVV**) from the card network or token service provider (TSP) to authenticate online card transactions.

## Endpoint & Environments

| Environment    | Method | URL              |
| :------------- | :----- | :--------------- |
| **Test**       | `POST` | `<redacted URL>` |
| **Production** | `POST` | `<redacted URL>` |

***

## Headers

<br />

***

## Request Parameters

The table has 5 rows, so here it is in **Markdown format**:

**Mandatory parameters**

| Parameter        | Description                                                                                                                                                |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userCredential` | `String` Plaintext identifier representing merchant key and customer ID in format `<merchantKey>:<customerId>` (e.g. `sms:user12345`). Max 100 characters. |
| `cardToken`      | `String` The unique card token identifier representing the saved card.                                                                                     |
| `amount`         | `Number` Transaction amount (e.g. `1000.00`). Cryptograms are cryptographically bound to the amount.                                                       |
| `currency_type`  | `String` 3-letter currency code (e.g. `INR`).                                                                                                              |

**Optional parameters**

| Parameter | Description                                                        |
| :-------- | :----------------------------------------------------------------- |
| `source`  | `String` Channel identifier (e.g. `merchant_web`, `merchant_app`). |

## Sample Request
```curl
curl --location --request POST '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'Date: Mon, 05 Oct 2026 08:30:00 GMT' \
--header 'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"' \
--data-raw '{
  "userCredential": "sms:user12345",
  "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
  "amount": 1000.00,
  "currency_type": "INR",
  "source": "merchant_web"
}'
```
```python
import requests

url = "<redacted URL>"
payload = {
    "userCredential": "sms:user12345",
    "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
    "amount": 1000.00,
    "currency_type": "INR",
    "source": "merchant_web"
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
  "cardToken" => "29850879bf39848ca078727b8e1a95165a41cea1",
  "amount" => 1000.00,
  "currency_type" => "INR",
  "source" => "merchant_web"
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

public class GetCryptogram {
    public static void main(String[] args) throws Exception {
        String payload = """
        {
          "userCredential": "sms:user12345",
          "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
          "amount": 1000.00,
          "currency_type": "INR",
          "source": "merchant_web"
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
  cardToken: "29850879bf39848ca078727b8e1a95165a41cea1",
  amount: 1000.00,
  currency_type: "INR",
  source: "merchant_web"
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

| Parameter           | Type    | Description                                                                                                                            |
| :------------------ | :------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| **status**          | Integer | Status indicator: `1` (Success) or `0` (Failure).                                                                                      |
| **msg**             | String  | Outcome description.                                                                                                                   |
| **cardToken**       | String  | The card token identifier queried.                                                                                                     |
| **cardNo**          | String  | Masked card number (e.g. `512345XXXXXX2346`).                                                                                          |
| **cardName**        | String  | Name of the cardholder.                                                                                                                |
| **cardType**        | String  | Network brand (e.g. `MAST`, `VISA`, `RUPAY`).                                                                                          |
| **cardMode**        | String  | Card category: `CC` (Credit Card) or `DC` (Debit Card).                                                                                |
| **cryptogram**      | String  | Base64-encoded Token Authentication Verification Value (TAVV / cryptogram) to pass into `paymentCard.tavv` for transaction processing. |
| **eci**             | String  | Electronic Commerce Indicator returned by the card network (e.g. `05`, `07`).                                                          |
| **oneClickStatus**  | String  | Status of 1-click checkout eligibility for this card instrument (`ELIGIBLE` / `INELIGIBLE`).                                           |
| **oneClickFlow**    | String  | Supported 1-click checkout authorization flow (`DEVICE_BINDING` / `OTP`).                                                              |
| **cardExpiryMonth** | String  | 2-digit expiry month.                                                                                                                  |
| **cardExpiryYear**  | String  | 4-digit expiry year.                                                                                                                   |

### Sample Response (Success)

```json
{
  "status": 1,
  "msg": "Cryptogram generated successfully",
  "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
  "cardNo": "512345XXXXXX2346",
  "cardName": "John Doe",
  "cardType": "MAST",
  "cardMode": "CC",
  "cryptogram": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
  "eci": "05",
  "oneClickStatus": "ELIGIBLE",
  "oneClickFlow": "OTP",
  "cardExpiryMonth": "12",
  "cardExpiryYear": "2029"
}
```

### Sample Response (Failure)

```json
{
  "status": 0,
  "msg": "Failed to fetch cryptogram from card network"
}
```


## Next Steps

1. **Pass Cryptogram to Payment API**:
   - Pass the returned `cryptogram` string into `paymentCard.tavv` and `eci` into `authorization.eci` when calling the [Using Network Tokens API](ref:using-network-tokens) or [Process Transaction with a Saved Card API](ref:process-transaction-with-a-saved-card).
2. **Handle Timeouts & Expirations**:
   - Cryptograms possess short validity windows (typically 15 minutes). Ensure cryptograms are generated just prior to initiating the payment collection request.
