---
title: Transaction Notify API
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
The **Transactoin Notify** API is used to  notify transaction status , and redeem/earn loyalty points.

HTTP Method: **POST**

### Endpoint

|            |                                                             |
| :--------- | :---------------------------------------------------------- |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/transact> |
|            |                                                             |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "Identifier for the loyalty service provider.",
    "0-2": "\\`LPX",
    "1-0": "txnAmount  \n`optional`",
    "1-1": "The transaction amount after discounts and loyalty point reductions.",
    "1-2": "`900`",
    "2-0": "orderAmount  \n`mandatory`",
    "2-1": "The total order amount before applying any discounts or loyalty points.",
    "2-2": "`1000`",
    "3-0": "status  \n`mandatory`",
    "3-1": "Transaction status indicating success or failure.",
    "3-2": "\"SUCCESS\" or \"FAILED\"",
    "4-0": "pgPaymentId  \n`optional`",
    "4-1": "Payment gateway ID. For example, IDs for Razorpay or PayU.",
    "4-2": "\"31234124234234\"",
    "5-0": "orderId  \n`mandatory`",
    "5-1": "Unique identifier for the order assigned by the merchant.",
    "5-2": "\"merchantTxnId\"",
    "6-0": "loyaltyRefId  \n`optional`",
    "6-1": "Reference ID for the loyalty transaction.",
    "6-2": "\"504\"",
    "7-0": "userDetail  \n`mandatory`",
    "7-1": "Information related to the user involved in the transaction.",
    "7-2": "{ \"phoneNumber\": \"8901555\\*\\*\\*\\*\" }",
    "8-0": "redemptionDetails  \n`optional`",
    "8-1": "Details of redemption, including key and points redeemed.",
    "8-2": "{ \"redeemLoyaltyKey\": \"test@lzbevLxNILTS\", \"redeemPoints\": 100 }",
    "9-0": "earnDetails  \n`optional`",
    "9-1": "Details regarding points earned in the transaction.",
    "9-2": "`{ \"earnLoyaltyKey\": \"test@lzbevLxNILTS\", \"earnPoints\": 100, \"autoApply\": true }`",
    "10-0": "paymentDetails  \n`mandatory for seamless`",
    "10-1": "Includes payment method info such as card number.",
    "10-2": "`{ \"category\": \"CREDITCARD\", \"paymentCode\": \"CC\", \"cardNumber\": \"4808550000000000\" }`"
  },
  "cols": 3,
  "rows": 11,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### paymentDetails JSON field description

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "`category`",
    "0-1": "Indicates the type or category of payment method being used. It can be any of the following:  \n  \n- CREDITCARD\n- DEBITCARD\n- NETBANKING",
    "0-2": "",
    "1-0": "`paymentCode`",
    "1-1": "A specific code representing the payment method; often used to facilitate backend processing.",
    "1-2": "`\"CC\"`",
    "2-0": "`cardNumber`",
    "2-1": "The masked or partially visible card number used for the transaction, usually following PCI DSS standards.",
    "2-2": "`\"4808550000000000\"`"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request body

### Regular request body

````plaintext
Here's the formatted JSON:

```json
{
    "loyaltyProvider": "LPX",
    "txnAmount": 900,
    "orderAmount": 1000,
    "status": "SUCCESS/FAILED",
    "pgPaymentId": "31234124234234", // Example: razorpayid, payuid.
    "orderId": "merchantTxnId",
    "loyaltyRefId": "504",
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "test@lzbevLxNILTS",
        "redeemPoints": 100
    },
    "earnDetails": {
        "earnLoyaltyKey": "test@lzbevLxNILTS",
        "earnPoints": 100,
        "autoApply": true // Default: false
    },
    "paymentDetails": {
        "cardBin": null,
        "cardHash": null,
        "cardMask": null,
        "category": "CREDITCARD",
        "isCollect": null,
        "paymentCode": "CC",
        "vpa": null,
        "cardNumber": "4808550000000000",
        "cardToken": null,
        "cardTokenType": null
    }
}
```
This formatted JSON aligns the elements clearly and maintains comments for context-specific details like examples and defaults. If there's anything else you need, feel free to ask! 😊
````

### Request with SKU

```
{
    "loyaltyProvider": "LPX",
    "txnAmount": 900,
    "orderAmount": 1000,
    "status": "SUCCESS/FAILED",
    "pgPaymentId": "31234124234234", // example: razorpyid, payuid.
    "orderId": "merchantTxnId",
    "loyaltyRefId": "504",
    "userDetail": {
        "phoneNumber": "8901555****"
    },
    "redemptionDetails": {
        "redeemLoyaltyKey": "test@lzbevLxNILTS",
        "redeemPoints": 100
    },
    "skusDetail": {
        "skus": [
            {
                "skuAmount": "1000.00",
                "skuOrderAmount": 1000,
                "quantity": "1",
                "skuId": "iphone",
                "earnConfig": {
                    "key": [],
                    "autoApply": "true", // Boolean
                    "earnPoints": null
                }
            }
        ]
    },
    // Payment details is mandatory in SEAMLESS mode,
    // Construct will be same as offer. because offer requires that.
    "paymentDetails": {
        "cardBin": null,
        "cardHash": null,
        "cardMask": null,
        "category": "CREDITCARD",
        "isCollect": null,
        "paymentCode": "CC",
        "vpa": null,
        "cardNumber": "4808550000000000",
        "cardToken": null,
        "cardTokenType": null
    }
}

```

<br />

## Sample response

### Success scenario

- Without order amount posted

```plaintext
{
    "orderId": "8878787",
    "loyaltyRefId": "534",
    "pgPaymentId": "31234124234234",
    "redemptionInfo": {
        "redeemLoyaltyKey": "Diamond@RUISebLORdLw",
        "redeemPoints": 100.0,
        "referenceId": "120"
    },
    // Earn on SKU
    "earnInfo": {
        "autoApply": true,
        "earnPoints": 200,
        "referenceId": "115"
    }
}

```

### Failure scenario

- Validation exception

```plaintext
{ 
"errorMessage":"Bad Request ", 
"errorType":"VALIDATION_EXCEPTION", 
"issueCode":"LS400_408" 
} 

```

- Session expired

```
{ 
    "issueCode": "LS404-401", 
    "errorMessage": "Session Expired unable to redeem points", 
    "errorType": "APPLICATION_EXCEPTION" 
}
```