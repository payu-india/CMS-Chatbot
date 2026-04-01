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
| Test       | https://test.payu.in/storecard/instrument/v1                                                 |
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
        userCredential
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
curl --location 'https://pp30info.payu.in/storecard/instrument/v1?userCredentials=testuser%3Atestuser123' \
  --header 'authorization: {{authorization}}' \
  --header 'date: {{date}}'
```

### Response

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "user_cards": {
      "13b390284be7ef8acf8": {
        "cardNo": "XXXXXXXXXXXX1258",
        "cardMode": "CC",
        "par": "0185NPMT1F8OS22Y4X0UU6AQUL8R1",
        "oneClickStatus": "",
        "oneClickCardAlias": "",
        "cardToken": "13b390284be7ef8acf8",
        "oneClickFlow": "",
        "cardName": "testAll",
        "nameOnCard": "DUMMY",
        "cardType": "CC",
        "isExpired": false,
        "cardExpiryMonth": 12,
        "cardExpiryYear": 2026,
        "networkToken": {
          "tokenValue": "4761360000000009",
          "isExpired": false,
          "tokenExpiryMonth": 12,
          "tokenExpiryYear": 2026,
          "tokenBin": "476136"
        },
        "cardCVV": "0",
        "isDomestic": "Y",
        "cardBin": "476136",
        "cardBrand": "VISA"
      }
      // ... more tokens
    }
  }
}
```

## Response parameters

| Field      | Description                                                                       | Example                    |
| ---------- | --------------------------------------------------------------------------------- | -------------------------- |
| status     | Status indicator: `1` for success, `0` for failure.                               | 1                          |
| msg        | Human-readable response message indicating if card fetching was successful.       | Cards fetched Successfully |
| user_cards | Contains saved card details for the user, with unique card tokens as object keys. |                            |

### User Cards Object

| Field         | Description                                                                                                                           | Example                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| card_type     | Type of card: either `CC` (Credit Card) or `DC` (Debit Card).                                                                         | CC                                                                             |
| expiry_year   | Expiry year of the card.                                                                                                              | 2030                                                                           |
| expiry_month  | Expiry month of the card.                                                                                                             | 11                                                                             |
| is_expired    | Shows whether the card has expired or not: `0` for active, `1` for expired.                                                           | 0                                                                              |
| card_mode     | Either `CC` (Credit Card) or `DC` (Debit Card).                                                                                       | CC                                                                             |
| card_no       | Masked card number showing only the last four digits.                                                                                 | `XXXXXXXXXXXX6937`                                                             |
| card_name     | User-defined name for the card.                                                                                                       | raghu_visa                                                                     |
| name_on_card  | Cardholder name.                                                                                                                      | DUMMY                                                                          |
| card_brand    | Network or brand name for the card (e.g., VISA, MASTERCARD).                                                                          | VISA                                                                           |
| card_bin      | Bank Identification Number of the card (first 6-9 digits).                                                                            | `439040`                                                                       |
| isDomestic    | Indicates if the card is domestic or international: `Y` for domestic, `N` for international.                                          | Y                                                                              |
| card_cvv      | Indicates if the CVV is required: `0` for Not Required, `1` for Required.                                                             | 0                                                                              |
| PAR           | Payment Account Reference – unique identifier for the card across environments for transaction checks.                                | V0010013022526170404000072387                                                  |
| network_token | Contains network token details for secure transactions. For more information, refer to[ Network token object](#network-token-object). | For more information, refer to[ Network token object](#network-token-object) . |

### Network token object

| Field         | Description                                                    | Example          |
| ------------- | -------------------------------------------------------------- | ---------------- |
| token_bin     | Bank Identification Number for the network token.              | 439040           |
| is_expired    | Indicates the token's status: `0` for active, `1` for expired. | 0                |
| token_exp_yr  | Expiry year of the network token.                              | 2030             |
| token_exp_mon | Expiry month of the network token.                             | 11               |
| token_value   | The actual token value used for secure transactions.           | 4390406210204342 |
