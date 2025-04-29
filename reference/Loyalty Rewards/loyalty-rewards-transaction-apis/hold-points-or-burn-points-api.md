---
title: Hold Points or Burn Points API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Hold Points** API is used to hold points against **orderId** in the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                         |
| :--------- | :------------------------------------------------------ |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/hold> |
|            |                                                         |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example\\*",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "Identifier for the loyalty service provider.",
    "0-2": "\"LPX\"",
    "1-0": "redemptionDetail  \n`mandatory`",
    "1-1": "Details about the points being redeemed in the transaction.",
    "1-2": "`{\"redeemLoyaltyKey\": \"Diamond@RUISebLORdLw\", \"redeemPoints\": 100}`",
    "2-0": "orderId  \n`mandatory`",
    "2-1": "A unique identifier assigned to the order.",
    "2-2": "\"8878787\"",
    "3-0": "orderAmount  \n`mandatory`",
    "3-1": "Total monetary value of the order.",
    "3-2": "1000",
    "4-0": "loyaltyRefId  \n`mandatory`",
    "4-1": "Reference ID given for tracking the loyalty transaction.",
    "4-2": "\"534\"",
    "5-0": "txnAmount  \n`optional`",
    "5-1": "Amount transacted after applying loyalty points reductions.",
    "5-2": "900",
    "6-0": "userDetail  \n`mandatory`",
    "6-1": "Information related to the user participating in the transaction.",
    "6-2": "`{\"phoneNumber\": \"8901555****\"}`"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

<br />

## Sample request body

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderId": "8878787",
    "orderAmount": 1000,
    "loyaltyRefId": "534",
    "txnAmount": 900,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "Diamond@RUISebLORdLw",
        "redeemPoints": 100
    }
}
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Loyalty points used successfully",
    "result": {
        "orderId": "657898761",
        "orderAmount": "1000",
        "loyaltyRefId": "896",
        "burnReason": "Loyalty applied successfully",
        "earnCalculation": "TXN_AMOUNT",
        "burnConfig": [
            {
                "reason": "Loyalty applied successfully",
                "isValid": true,
                "pointsExpiryDate": null,
                "loyaltyKey": "Diamond@RUISebLORdLw",
                "title": "Diamond",
                "description": null,
                "tnc": null,
                "minTxnAmount": 100.0,
                "maxTxnAmount": 100000.0,
                "validFrom": null,
                "validTo": null,
                "isSku": false,
                "paymentMethods": null,
                "isAllPaymentMethodsAvailable": null,
                "skuDetail": null,
                "isAcrossSkuQuantity": null,
                "loyaltyPointDetail": {
                    "pointType": "ABSOLUTE",
                    "burnPoints": 100.0,
                    "burnPointsAmount": 1.0
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "availablePoints": 800.00,
        "isBurnValid": true
    }
}
```

### Failure Scenario

- Customer is not onboarded

```plaintext
{
    "issueCode": "LS500-503",
    "errorMessage": "Customer is not onboarded on Loyalty-service",
    "errorType": "APPLICATION_EXCEPTION"
}
```

- Session expiry

```plaintext
{
    "issueCode": "LS404-401",
    "errorMessage": "Session Expired unable to redeem points",
    "errorType": "APPLICATION_EXCEPTION"
}
```