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