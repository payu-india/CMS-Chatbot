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

|            |                                                                                              |
| :--------- | :------------------------------------------------------------------------------------------- |
| Test       | [https://test.payu.in/storecard/instrument/v1](https://test.payu.in/storecard/instrument/v1) |
| Production | [https://info.payu.in/storecard/instrument/v1](https://info.payu.in/storecard/instrument/v1) |

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
curl --location 'https://apitest.payu.in/storecard/instrument/v1?userCredentials=sms%3A123' \
--header 'Content-Type: application/json' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="30d8f518edda5b0962c35c0057024cabb6e7f19727488cb1874e75652bcea7499811dbf3ddac419c50c2fe56a8e032129bb0d6eaeaa3f971b3c2b5ccbfd12aa3"' \
--header 'date: Fri, 24 Apr 2026 07:05:59 GMT' \
--header 'Cookie: PHPSESSID=krida5voc39gqosfud8tt6n8as'
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
