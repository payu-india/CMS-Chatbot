---
title: Get User Cards API
deprecated: false
hidden: false
metadata:
  robots: index
---
Use the v2 **Get User Cards** API to get the card details of a customer.

<Callout icon="📘" theme="info">
  **Note**: While PayU token is sent in payment response, the network/issuer token creation may fail. In this case, the subsequent transaction with the said PayU token may fail. Merchant can do a **get_user_cards API** to fetch only active/tokenized cards or listen to notification API (to be published) to maintain state at your end.
</Callout>

The **Get User Cards** API is used to fetch all the cards for a customer which were saved earlier. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

## Request Header

### Header authentication

<HeaderAuthentication />

<br />

### Query parameter

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>userCredential<br/><code>mandatory</code></td>
      <td><code>String</code> User authentication credential in the format <code>username:userid</code>.</td>
      <td>testuser:testuser123</td>
    </tr>
    <tr>
      <td>getSoftDeleted<br/><code>optional</code></td>
      <td><code>Integer</code> Flag to include soft-deleted records in the response. Set to <code>1</code> to include, <code>0</code> to exclude.</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Request header

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
        mid
        `mandatory`
      </td>

      <td>
        Merchant ID provided by PayU. Use the value provided in your PayU dashboard.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --location '<info.storecard.service.url>/storecard/instrument/v1?testuser%3Atestuser123&getSoftDeleted=1' \
--header 'mid: 2'
```

## Sample response

```
{
    "message": "Success",
    "status": 1,
    "result": {
        "user_cards": {
            "a4270b1fc031d38079e": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "a4270b1fc031d38079e",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 5,
                "cardExpiryYear": 2037,
                "networkToken": {
                    "tokenValue": "4489682380100740",
                    "isExpired": false,
                    "tokenExpiryMonth": 5,
                    "tokenExpiryYear": 2037,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "448968",
                "cardBrand": "VISA"
            },
            "7ffe8ef0e2667aac3b8": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "7ffe8ef0e2667aac3b8",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 5,
                "cardExpiryYear": 2037,
                "networkToken": {
                    "tokenValue": "4489682380100740",
                    "isExpired": false,
                    "tokenExpiryMonth": 5,
                    "tokenExpiryYear": 2037,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "448968",
                "cardBrand": "VISA"
            },
            "cde4561f038e60f488": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "cde4561f038e60f488",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 5,
                "cardExpiryYear": 2037,
                "networkToken": {
                    "tokenValue": "4489682380100740",
                    "isExpired": false,
                    "tokenExpiryMonth": 5,
                    "tokenExpiryYear": 2037,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "448968",
                "cardBrand": "VISA"
            },
            "2f4537bbb66c15b1ca88": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "2f4537bbb66c15b1ca88",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 5,
                "cardExpiryYear": 2037,
                "networkToken": {
                    "tokenValue": "4489682380100740",
                    "isExpired": false,
                    "tokenExpiryMonth": 5,
                    "tokenExpiryYear": 2037,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "448968",
                "cardBrand": "VISA"
            },
            "2f5543d4fc7f23063df1": {
                "cardNo": "XXXXXXXXXXXX1258",
                "cardMode": "CC",
                "par": "V0010013021320427651459792018",
                "oneClickStatus": "",
                "oneClickCardAlias": "",
                "cardToken": "2f5543d4fc7f23063df1",
                "oneClickFlow": "",
                "cardName": "testAll",
                "nameOnCard": "DUMMY",
                "cardType": "CC",
                "isExpired": false,
                "cardExpiryMonth": 5,
                "cardExpiryYear": 2037,
                "networkToken": {
                    "tokenValue": "4489682380100740",
                    "isExpired": false,
                    "tokenExpiryMonth": 5,
                    "tokenExpiryYear": 2037,
                    "tokenBin": "448968"
                },
                "cardCVV": "0",
                "isDomestic": "Y",
                "cardBin": "448968",
                "cardBrand": "VISA"
            }
        },
        "user_instruments": {
            "testuser_instrument_token_999": {
                "friendlyName": "Test User Wallet",
                "nickName": "TestWalletUser"
            }
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
