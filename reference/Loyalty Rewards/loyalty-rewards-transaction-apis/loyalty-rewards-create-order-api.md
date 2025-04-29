---
title: Create Order API
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
The **Create Order** API is used to create order against **orderId** in the Loyalty Rewards integration.

HTTP Method: **POST**

### Endpoint

|            |                                                          |
| :--------- | :------------------------------------------------------- |
| Production | <https://apitest.payu.in/loyalty-points/points/v1/order> |
|            |                                                          |

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "A static value which need to passed for LoyaltyPointClose Loop flow",
    "0-2": "\"LPX\"",
    "1-0": "orderId  \n`mandatory`",
    "1-1": "Identifier for the order",
    "1-2": "\"223234\"",
    "2-0": "orderAmount  \n`mandatory`",
    "2-1": "The total amount of the order",
    "2-2": "1000",
    "3-0": "txnAmount  \n`optional`",
    "3-1": "The order amount that can be any of the following purposes:  \n  \n- discount\n- burn points amount",
    "3-2": "900",
    "4-0": "userDetail  \n`mandatory`",
    "4-1": "The user details such as phone number",
    "4-2": "{  \n        \"phoneNumber\": \"8901555\\*\\*\\*\\*\"  \n    }"
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

## Sample request Body

```plaintext
{
    "loyaltyProvider": "LPX",
    "orderId": "223234",
    "orderAmount": 1000,
    "txnAmount": 950,
    "userDetail": {
        "phoneNumber": "8901555****"
    }
}
```

## Sample response

### Success scenario

```plaintext
{
    "status": 1,
    "message": "Order created successfully!",
    "result": {
        "userDetail": {
            "userId": "1726853623d5babd27-98d2-4e5f-83f9-2deb1fe44efe",
            "phoneNumber": "8800108523",
            "entityTypeId": 2,
            "additionalDetail": null,
            "isLoyaltyEnrolled": false
        },
        "orderId": "657898761",
        "orderAmount": "1000",
        "loyaltyRefId": "896",
        "availablePoints": 800.00
    }
}
```

### Failure scenario

```plaintext
{ 
"errorMessage":"Bad Request ", 
"errorType":"VALIDATION_EXCEPTION", 
"issueCode":"LS400_408" 
} 
```