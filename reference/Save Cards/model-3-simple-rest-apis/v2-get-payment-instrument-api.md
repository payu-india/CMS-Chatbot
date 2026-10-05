---
title: Get Payment Instrument API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Get Payment Instrument API
deprecated: false
hidden: false
metadata:
  robots: index
---

The v2 **Get Payment Instrument** API allows merchants to fetch all saved cards for a specific user. This API returns comprehensive card details including tokenized information, expiry status, and network tokens for secure transactions.

HTTP Method:  **GET**

**Environment**

|            |                                                                                                    |
| :--------- | :------------------------------------------------------------------------------------------------- |
| Test       | [https://apitest.payu.in/storecard/instrument/v1](https://apitest.payu.in/storecard/instrument/v1) |
| Production | [https://info.payu.in/storecard/instrument/v1](https://info.payu.in/storecard/instrument/v1)       |

## Request header

### Authorization header

<HeaderAuthentication />

### Header parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        date
        `mandatory`
      </td>

      <td>
        The current date and time. For example, format of the date is Wed, 28 Jun 2023 11:25:19 GMT.
      </td>
    </tr>
  </tbody>
</Table>

### Query parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        userCredentials
        `mandatory`
      </td>

      <td>
        `String` Encrypted user credentials, typically `<username>:<password>`.
      </td>
    </tr>
  </tbody>
</Table>

## Request body

None

## Sample Request and Response

### Request

```bash
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

### Response

```json
{
    "message": "Success",
    "status": 1,
    "result": {
        "user_cards": {
            "2d1e53f353cd446d3e5d8d": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "2d1e53f353cd446d3e5d8d",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 12,
                "cardExpiryYear": 2034,
                "networkToken": {
                    "tokenValue": "4489682380114436",
                    "isExpired": false,
                    "tokenExpiryMonth": 12,
                    "tokenExpiryYear": 2034,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "476136",
                "cardBrand": "VISA"
            }
        }
    }
}
```

## Response parameters

| Field   | Description                                                                                                                                                         | Example |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| status  | Status indicator: `1` for success, `0` for failure.                                                                                                                 | 1       |
| message | Human-readable response message indicating if card fetching was successful.                                                                                         | Success |
| result  | JSON object that wraps the saved cards. Contains the `user_cards` map keyed by `cardToken`. For more information, refer to [User Cards Object](#user-cards-object). |         |

### User Cards Object

Each entry under `result.user_cards` is keyed by the card's `cardToken` and contains the following fields:

| Field             | Description                                                                                                                           | Example                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| cardToken         | Unique card token assigned by PayU.                                                                                                   | `13b390284be7ef8acf8`         |
| cardNo            | Masked card number showing only the last four digits.                                                                                 | `XXXXXXXXXXXX1258`            |
| cardType          | Type of card: either `CC` (Credit Card) or `DC` (Debit Card).                                                                         | CC                            |
| cardMode          | Card mode: either `CC` (Credit Card) or `DC` (Debit Card).                                                                            | CC                            |
| cardName          | User-defined nickname for the card.                                                                                                   | testAll                       |
| nameOnCard        | Cardholder name.                                                                                                                      | DUMMY                         |
| cardBrand         | Network or brand name for the card (for example, `VISA`, `MASTERCARD`).                                                               | VISA                          |
| cardBin           | Bank Identification Number of the card (first 6 digits).                                                                              | `476136`                      |
| cardExpiryMonth   | Expiry month of the card.                                                                                                             | 12                            |
| cardExpiryYear    | Expiry year of the card.                                                                                                              | 2026                          |
| isExpired         | Boolean flag indicating whether the card has expired.                                                                                 | false                         |
| isDomestic        | Indicates if the card is domestic or international: `Y` for domestic, `N` for international.                                          | Y                             |
| cardCVV           | Indicates if CVV is required: `0` for Not Required, `1` for Required.                                                                 | 0                             |
| par               | Payment Account Reference – unique identifier for the card across environments for transaction checks.                                | 0185NPMT1F8OS22Y4X0UU6AQUL8R1 |
| oneClickFlow      | Indicates whether the card is enrolled for the one-click flow.                                                                        |                               |
| oneClickStatus    | Status of one-click enrollment for the card.                                                                                          |                               |
| oneClickCardAlias | Non-sensitive alias used to represent the card in one-click flows.                                                                    |                               |
| networkToken      | Contains network token details for secure transactions. For more information, refer to [Network token object](#network-token-object). |                               |

### Network token object

| Field            | Description                                           | Example          |
| ---------------- | ----------------------------------------------------- | ---------------- |
| tokenValue       | The actual token value used for secure transactions.  | 4761360000000009 |
| tokenBin         | Bank Identification Number for the network token.     | 476136           |
| tokenExpiryMonth | Expiry month of the network token.                    | 12               |
| tokenExpiryYear  | Expiry year of the network token.                     | 2026             |
| isExpired        | Boolean flag indicating whether the token is expired. | false            |