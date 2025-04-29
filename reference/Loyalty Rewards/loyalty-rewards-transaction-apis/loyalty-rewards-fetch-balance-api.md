---
title: Fetch Balance API
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
The **Fetch Balalnce** API is used to fetch balance and loyalty points applicable on transaction.

HTTP Method: **POST**

### Endpoint

|            |                                                            |
| :--------- | :--------------------------------------------------------- |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/balance> |
|            |                                                            |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "Identifier for the loyalty service provider.",
    "0-2": "`\"LPX\"`",
    "1-0": "orderAmount  \n`optional`",
    "1-1": "Total monetary value of the order.",
    "1-2": "`1000`",
    "2-0": "",
    "2-1": "",
    "2-2": "",
    "3-0": "userDetail  \n`mandatory`",
    "3-1": "Information related to the user involved in the transaction.",
    "3-2": "`{ \"phoneNumber\": \"8901555****\" }`",
    "4-0": "skusDetail  \n`optional`",
    "4-1": "Details of stock keeping units (SKUs) in the transaction. This parameter must contain the array of SKU details (skus as in example) For the description of the fields in **skus**, refer to[ skus JSON field description](skus-json-field-description).",
    "4-2": " \"skus\": \\[  \n            {  \n                \"skuId\": \"airpod\",  \n                \"quantity\": null,  \n                \"skuAmount\": 900,  \n                \"skuOrderAmount\": 1000  \n            }  \n]"
  },
  "cols": 3,
  "rows": 5,
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

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderAmount": 1000,
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "skusDetail": {
        "skus": [
            {
                "skuId": "airpod",
                "quantity": null,
                "skuAmount": 900,
                "skuOrderAmount": 1000
            }
        ]
    }
}

```

## Sample response

### Success scenario

- Without order amount posted

```plaintext
{
    "status": 1,
    "message": "Loyalty Retrieved Successfully",
    "result": {
        "userDetail": {
            "userId": "newGene775a048-1796-41d7-bb11-d3315dcb0620",
            "phoneNumber": "8901555****",
            "entityTypeId": 180013,
            "isLoyaltyEnrolled": true,  // can be false if not onboarded on loyalty-service
            "additionalDetail": null
        },
        "availablePoints": 10000
    }
}

```

- With order amount

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
        "burnConfig": [
            {
                "loyaltyKey": "test2@qjyAe2YiDwbH",
                "loyaltyId": 1234,
                "title": "test 2",
                "description": "test 2",
                "tnc": "terms and conditions",
                "tncLink": null,
                "minTxnAmount": 100.0,
                "maxTxnAmount": 100000.0,
                "loyaltyPointDetail": {
                    "pointType": "PERCENTAGE",
                    "pointPercentage": 10,
                    "burnPoints": 10,
                    "burnPointsAmount": 10
                }
            }
        ],
        "pointsAmountConversion": {
            "amountToPointUnit": 100,
            "pointCurrency": "ponits/coins/rewards/brownies"
        },
        "availablePoints": 10000,
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

### Failure scenario

```plaintext
{ 

"errorMessage":"Bad Request ", 

"errorType":"APPLICATION_EXCEPTION", 

"issueCode":"LS500_508" 

} 
```