---
title: Get Single Payment Link API
excerpt: 'Resource: **payment-links**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Get Single Payment Link API is used to get a single payment link using the payment link invoice number.

HTTP Method: **GET**

**Environment**

|                        |                                           |
| :--------------------- | :---------------------------------------- |
| Test Environment       | <https://uatoneapi.payu.in/payment-links> |
| Production Environment | <https://oneapi.payu.in/payment-links>    |

> 📘 Note:
> 
> The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

## Request headers

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "mid  \n**mandatory**",
    "0-1": "`String` This contains the merchant identifier.",
    "1-0": "Authorization  \n**mandatory**",
    "1-1": "Bearer `String` This contains the client\\_token. For getting a token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links) ."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Path parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Id  \n**mandatory**",
    "0-1": "`String` This parameter must contain the payment link invoice number.",
    "0-2": "INV8446471886220"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location --request GET 'https://uatoneapi.payu.in/payment-links/INV0063002462' \
--header 'merchantId: 8237550' \
--header 'Authorization: Bearer e53f7d25071e6c2e631a920f38b9dbceeb571d6aadaed7e100f55fc7dab110ff
```

## Sample response

### Success scenario

```
{
  "status": 0,
  "message": null,
  "result": {
    "summary": {
      "amountRequested": 2,
      "totalRevenue": 0,
      "totalViews": 0
    },
    "subAmount": 2,
    "tax": 0,
    "shippingCharge": 0,
    "totalAmount": 2,
    "totalAmountCollected": 0,
    "invoiceNumber": "INV8446471886220",
    "paymentLink": "http://pp72.pmny.in/4IwlctBtwp2V",
    "description": "paymentLink for testing",
    "active": true,
    "isPartialPaymentAllowed": false,
    "status": "active",
    "expiryDate": "2023-03-21T14:53:52.000+0530",
    "udf": {
      "udf1": null,
      "udf2": null,
      "udf3": null,
      "udf4": null,
      "udf5": null
    },
    "address": {
      "line1": null,
      "line2": null,
      "city": null,
      "state": null,
      "country": null,
      "zipCode": null
    },
    "addedOn": "2022-03-21T14:53:53.000+0530",
    "isAmountFilledByCustomer": false,
    "isScheduled": 0,
    "reminderCount": 0,
    "customAttributes": []
  },
  "errorCode": null,
  "guid": null
}
```

### Failure scenario

```
{
  "status": -1,
  "message": "paymentLink not found",
  "result": null,
  "errorCode": null,
  "guid": null
}
```