---
title: Refund API
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
The **Refund **API is used to refund loyalty points for the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                           |
| :--------- | :-------------------------------------------------------- |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/refund> |
|            |                                                           |

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "orderId`\nmandatory`",
    "0-1": "The unique identifier of the merchant's transaction.",
    "0-2": "\"merchantTxnId\"",
    "1-0": "refundType  \n`mandatory`",
    "1-1": "Specifies whether the refund is partial or full.",
    "1-2": "\"PARTIAL\"",
    "2-0": "refundAmount  \n`mandatory`",
    "2-1": "Amount to be refunded to the customer.",
    "2-2": "1000",
    "3-0": "skuInfo`\nmandatory for SKUs`",
    "3-1": "Details of stock keeping units (SKUs) in the transaction. This parameter must contain the array of SKU details (skus as in example) For the description of the fields in **skus**, refer to[ skus JSON field description](skus-json-field-description) .",
    "3-2": "\"skus\": \\[  \n            {  \n                \"skuId\": \"airpod\",  \n                \"quantity\": null,  \n                \"skuAmount\": 900,  \n                \"skuOrderAmount\": 1000  \n            }  \n]",
    "4-0": "refundId  \n`mandatory`",
    "4-1": "Unique identifier for the refund transaction. Optional identifier for tracking.",
    "4-2": "\"refundId\""
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

## Request body

```plaintext
{ 
  "refundType":"PARTIAL/FULL", 
  "refundAmount":1000, 
  "skuInfo":null, 
  "orderId": "merchantTxnId", 
  "refundId":"refundId" 
} 
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Refund processed successfully",
    "refundInfo": {
        "referenceId": "1234", // loyalty-pg reference-id
        "adjustmentId": "adj1", // can be null
        "refundAmount": 110,
        "split": {
            "pgAmount": 100,
            "loyaltyPoint": 10,
            "loyaltyPointAmount": 10
        },
        "adjustment": {
            "loyaltyPoint": 10,
            "loyaltyPointAmount": 10
        }
    }
}

```

### Failure scenario

```
{ 
"errorMessage":"Bad Request ", 
"errorType":"APPLICATION_EXCEPTION", 
"issueCode":"LS500_508" 
} 
```