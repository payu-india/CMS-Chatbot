---
title: Fetch Earn Config API
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
The **Fetch Earn Config** API is used to fetch loyalty earn point config on transaction.

HTTP Method: **POST**

### Endpoint

|            |                                                               |
| :--------- | :------------------------------------------------------------ |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/earnConfig> |
|            |                                                               |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "Identifier for the loyalty service provider.",
    "0-2": "\"LPX\"",
    "1-0": "orderAmount  \n`mandatory`",
    "1-1": "Total monetary value of the order.",
    "1-2": "1000",
    "2-0": "userDetail  \n`mandatory`",
    "2-1": "Information related to the user involved in the transaction.",
    "2-2": "{ \"phoneNumber\": \"8901555\\*\\*\\*\\*\" }",
    "3-0": "txnAmount  \n`optional`",
    "3-1": "The order amount that can be any of the following purposes:  \n  \n- discount\n- burn points amount",
    "3-2": "900",
    "4-0": "isCampaignTncRequired  \n`optional`",
    "4-1": "To indicate if the campaign Terms & Conditions required.",
    "4-2": "true",
    "5-0": "skusDetail  \n`optional`",
    "5-1": "Details of stock keeping units (SKUs) in the transaction. This parameter must contain the array of SKU details (skus as in example) For the description of the fields in **skus**, refer to[ skus JSON field description](skus-json-field-description).",
    "5-2": " \"skus\": \\[  \n            {  \n                \"skuId\": \"airpod\",  \n                \"quantity\": null,  \n                \"skuAmount\": 900,  \n                \"skuOrderAmount\": 1000  \n            }  \n]"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### skus JSON field description

| **Parameter**  | **Description**                                           | **Example** |
| -------------- | --------------------------------------------------------- | ----------- |
| skuId          | Unique identifier for each SKU in the transaction.        | "airpod"    |
| quantity       | Number of units for the SKU, can be null if unquantified. | null        |
| skuAmount      | Total amount for each SKU unit.                           | 900         |
| skuOrderAmount | Order amount associated with each SKU.                    | 1000        |

## Sample request body

### Regular request

```
{ 
    "loyaltyProvider": "LPX", 
    "orderAmount": 1000,//Mandatory 
    "txnAmount":900 , 
    "isCampaignTncRequired":true , 
    "userDetail": { 
        "phoneNumber":"8901555****" 
    } 
} 
```

### Request with SKU details

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderAmount": 1000, // Mandatory
    "txnAmount": 900,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "skusDetail": {
        "skus": [
            {
                "skuId": "airpod",
                "quantity": null,
                "skuAmount": 1000,
                "skuOrderAmount": 1000
            }
        ]
    }
}

```

## Sample response

### Success scenario

- Without SKU

```
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true, // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "mid": "8235901",
        "amount": "900",
        "orderAmount": "1000",
        "earnConfig": [
            {
                "isValid": true,
                "pointsExpiryDate": null,
                "loyaltyKey": "TestSeamlessCampaign@vtpuYAh4rIy6",
                "title": "TestSeamlessCampaign",
                "description": "Heading2",
                "tnc": "Body2",
                "minTxnAmount": 250.0,
                "maxTxnAmount": 50000.0,
                "validFrom": "2024-09-12 12:09:24",
                "validTo": "2034-09-12 12:09:24",
                "paymentMethods": {
                    "creditCard": null,
                    "debitCard": null,
                    "netBanking": null,
                    "wallet": null,
                    "clw": null,
                    "upi": null,
                    "emi": null,
                    "bnpl": null
                },
                "isAllPaymentMethodsAvailable": true,
                "loyaltyPointDetail": {
                    "pointType": "ABSOLUTE",
                    "earnPoints": 200.0,
                    "earnPointsAmount": 2.0
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "pointExpiryDetails": {
            "loyaltyPoints": 1000,
            "days": 5
        },
        "pointsSummary": {
            "lifeTimeEarnPoints": 100.00,
            "lifeTimeEarnAmount": 2000.00,
            "lifeTimeBurnPoints": 10.00,
            "lifeTimeBurnAmount": 200.00
        }
    }
}

```

- With SKU

```plaintext
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true, // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "mid": "8235901",
        "amount": "900",
        "orderAmount": "1000",
        "skusDetail": {
            "skus": [
                {
                    "skuId": "iphone",
                    "quantity": 1,
                    "skuAmount": 2500,
                    "suppressSkuQuantity": false,
                    "earnConfig": [
                        {
                            "reason": null,
                            "isValid": true,
                            "pointsExpiryDate": "2024-09-18",
                            "loyaltyKey": "SkuDuplicateTest@u78FEHQK6ZKF",
                            "title": "SkuDuplicateTest",
                            "description": "SkuDuplicateTest",
                            "tnc": "{\"text\":\"SkuDuplicateTest\\n\",\"html\":\"<p>SkuDuplicateTest</p>\",\"ops\":[{\"insert\":\"SkuDuplicateTest\\n\"}]}",
                            "minTxnAmount": 1000.0,
                            "maxTxnAmount": 1000000.0,
                            "validFrom": "2024-09-11 15:35:34",
                            "validTo": "2034-09-11 15:35:34",
                            "isSku": true,
                            "paymentMethods": {
                                "creditCard": [
                                    {
                                        "networks": [],
                                        "banks": [
                                            {
                                                "code": "ICICI",
                                                "title": "ICICI"
                                            }
                                        ],
                                        "title": null,
                                        "paymentCode": null,
                                        "handle": null
                                    }
                                ],
                                "debitCard": null,
                                "netBanking": null,
                                "wallet": null,
                                "clw": null,
                                "upi": null,
                                "emi": null,
                                "bnpl": null
                            },
                            "isAllPaymentMethodsAvailable": null,
                            "skuDetail": null,
                            "isAcrossSkuQuantity": null,
                            "loyaltyPointDetail": {
                                "pointType": "ABSOLUTE",
                                "earnPoints": 551.0,
                                "earnPointsAmount": 5.51
                            }
                        }
                    ],
                    "skuOrderAmount": 2500,
                    "earnFailureReason": null,
                    "earnIsValid": true
                },
                {
                    "skuId": "airpod",
                    "quantity": 1,
                    "skuAmount": 2500,
                    "suppressSkuQuantity": false,
                    "earnConfig": [
                        {
                            "reason": null,
                            "isValid": true,
                            "pointsExpiryDate": "2024-09-18",
                            "loyaltyKey": "SkuDuplicateTest@u78FEHQK6ZKF",
                            "title": "SkuDuplicateTest",
                            "description": "SkuDuplicateTest",
                            "tnc": "{\"text\":\"SkuDuplicateTest\\n\",\"html\":\"<p>SkuDuplicateTest</p>\",\"ops\":[{\"insert\":\"SkuDuplicateTest\\n\"}]}",
                            "minTxnAmount": 1000.0,
                            "maxTxnAmount": 1000000.0,
                            "validFrom": "2024-09-11 15:35:34",
                            "validTo": "2034-09-11 15:35:34",
                            "isSku": true,
                            "paymentMethods": {
                                "creditCard": [
                                    {
                                        "networks": [],
                                        "banks": [
                                            {
                                                "code": "ICICI",
                                                "title": "ICICI"
                                            }
                                        ],
                                        "title": null,
                                        "paymentCode": null,
                                        "handle": null
                                    }
                                ],
                                "debitCard": null,
                                "netBanking": null,
                                "wallet": null,
                                "clw": null,
                                "upi": null,
                                "emi": null,
                                "bnpl": null
                            },
                            "isAllPaymentMethodsAvailable": null,
                            "skuDetail": null,
                            "isAcrossSkuQuantity": null,
                            "loyaltyPointDetail": {
                                "pointType": "ABSOLUTE",
                                "earnPoints": 551.0,
                                "earnPointsAmount": 5.51
                            }
                        }
                    ],
                    "skuOrderAmount": 2500,
                    "earnFailureReason": null,
                    "earnIsValid": true
                }
            ]
        },
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "Diamond",
            "pointIconUrl": "https://d24r6yy703ziu6.cloudfront.net/web/images/assets/loyalty/icons/coin.svg"
        },
        "pointExpiryDetails": null,
        "pointsSummary": null
    }
}

```

<br />

### Failure scenario

```plaintext
  { 
"errorMessage":"Bad Request ", 
"errorType":"APPLICATION_EXCEPTION", 
"issueCode":"LS500_508" 
} 
```