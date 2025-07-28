---
title: Get User Cards API
deprecated: false
hidden: false
metadata:
  robots: index
---
Use the v2 **Get User Cards** API to get the card details of a customer.

> 📘 Note
>
> While PayU token is sent in payment response, the network/issuer token creation may fail. In this case, the subsequent transaction with the said PayU token may fail. Merchant can do a **get\_user\_cards API** to fetch only active/tokenized cards or listen to notification API (to be published) to maintain state at your end.

The **Get User Cards** API is used to fetch all the cards for a customer which were saved earlier. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

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

| Field       | Description                                                                       | Example                    |
| ----------- | --------------------------------------------------------------------------------- | -------------------------- |
| status      | Status indicator: `1` for success, `0` for failure.                               | 1                          |
| msg         | Human-readable response message indicating if card fetching was successful.       | Cards fetched Successfully |
| user\_cards | Contains saved card details for the user, with unique card tokens as object keys. |                            |

### User Cards Object

| Field          | Description                                                                                                                           | Example                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| card\_type     | Type of card: either `CC` (Credit Card) or `DC` (Debit Card).                                                                         | CC                                                                             |
| expiry\_year   | Expiry year of the card.                                                                                                              | 2030                                                                           |
| expiry\_month  | Expiry month of the card.                                                                                                             | 11                                                                             |
| is\_expired    | Shows whether the card has expired or not: `0` for active, `1` for expired.                                                           | 0                                                                              |
| card\_mode     | Either `CC` (Credit Card) or `DC` (Debit Card).                                                                                       | CC                                                                             |
| card\_no       | Masked card number showing only the last four digits.                                                                                 | `XXXXXXXXXXXX6937`                                                             |
| card\_name     | User-defined name for the card.                                                                                                       | raghu\_visa                                                                    |
| name\_on\_card | Cardholder name.                                                                                                                      | DUMMY                                                                          |
| card\_brand    | Network or brand name for the card (e.g., VISA, MASTERCARD).                                                                          | VISA                                                                           |
| card\_bin      | Bank Identification Number of the card (first 6-9 digits).                                                                            | `439040`                                                                       |
| isDomestic     | Indicates if the card is domestic or international: `Y` for domestic, `N` for international.                                          | Y                                                                              |
| card\_cvv      | Indicates if the CVV is required: `0` for Not Required, `1` for Required.                                                             | 0                                                                              |
| PAR            | Payment Account Reference – unique identifier for the card across environments for transaction checks.                                | V0010013022526170404000072387                                                  |
| network\_token | Contains network token details for secure transactions. For more information, refer to[ Network token object](#network-token-object). | For more information, refer to[ Network token object](#network-token-object) . |

### Network token object

| Field           | Description                                                    | Example          |
| --------------- | -------------------------------------------------------------- | ---------------- |
| token\_bin      | Bank Identification Number for the network token.              | 439040           |
| is\_expired     | Indicates the token's status: `0` for active, `1` for expired. | 0                |
| token\_exp\_yr  | Expiry year of the network token.                              | 2030             |
| token\_exp\_mon | Expiry month of the network token.                             | 11               |
| token\_value    | The actual token value used for secure transactions.           | 4390406210204342 |