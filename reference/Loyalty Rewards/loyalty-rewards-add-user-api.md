---
title: Add User API
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
The **Create Order** API is used to add a customer to your Loyalty Rewards program.

HTTP Method: **POST**

### Endpoint

|            |                                                         |
| :--------- | :------------------------------------------------------ |
| Production | &lt;https://apitest.payu.in/loyalty-points/points/v1/user&gt; |
|            |                                                         |

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "loyaltyProvider  \n`mandatory`",
    "0-1": "A static identifier for the loyalty provider to facilitate the Close Loop flow.",
    "0-2": "\"LPX\"",
    "1-0": "orderAmount  \n`optional`",
    "1-1": "Represents the total monetary value of the order, affecting loyalty calculations.",
    "1-2": "1000",
    "2-0": "userDetail  \n`mandatory`",
    "2-1": "An object containing details about the user, such as the phone number.",
    "2-2": "{ \"phoneNumber\": \"8901555\\*\\*\\*\\*\" }",
    "3-0": "phoneNumber  \n`mandatory`",
    "3-1": "The customer phone number, used as a unique identifier in the loyalty system.",
    "3-2": "8901555\\*\\*\\*\\*"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

## Sample request body

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
    "result": {
        "userDetail": {
            "userId": "17277864939c4f18a2-cbe5-4f85-bdb8-23b04d5fc1d3",
            "phoneNumber": "8901555****",
            "entityTypeId": 180012,
            "additionalDetail": null,
            "isLoyaltyEnrolled": false
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