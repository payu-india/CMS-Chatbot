---
title: Change Status or Expiry for a Payment Link API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to update a payment link's status and expiry date.

HTTP Method: **PUT**

**Environment**

|                            |                                           |
| -------------------------- | ----------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payment-links> |
| **Production Environment** | <https://oneapi.payu.in/payment-links>    |

> 📘 Note:
> 
> The access token with the scope as **update_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

## Path parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "ID  \n`mandatory`",
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


## Request headers

| Parameter                 | Description                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| mid`  mandatory`          | `String` This contains the merchant identifier.                                                                                                    |
| Authorization` mandatory` | Bearer `String` This contains the client\_token. For more information, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links) . |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "ID  \n`mandatory`",
    "0-1": "`String` This parameter must contain the payment link invoice number.",
    "0-2": "INV8446471886220",
    "1-0": "subAmount  \n`optional`",
    "1-1": "`String` This parameter must contain the payment sub amount.",
    "1-2": "100.00",
    "2-0": "tax  \n`optional`",
    "2-1": "`String` This parameter must contain the tax amount for the transaction.",
    "2-2": "1.00",
    "3-0": "shippingCharge  \n`optional`",
    "3-1": "`String` This parameter must contain the shipping charge.",
    "3-2": "10.00",
    "4-0": "isPartialPaymentAllowed  \n`optional`",
    "4-1": "`Boolean` This parameter includes whether partial payment is allowed.",
    "4-2": "false",
    "5-0": "active  \n`optional`",
    "5-1": "`Boolean` This parameter includes whether the payment link is active.",
    "5-2": "true",
    "6-0": "expiry  \n`optional`",
    "6-1": "`String` This parameter must contain the expiry date.",
    "6-2": "2024-04-01",
    "7-0": "udf  \n`optional`",
    "7-1": "`JSON`This parameter contains the following UDF parameters in a JSON format as in the example:  \n  \n- udf1\t\n- udf2\t\n- udf3\t\n- udf4\t\n- udf5\t  ",
    "7-2": "{  \n\"udf1\": \"string\",  \n\"udf2\": \"string\",  \n\"udf3\": \"string\",  \n\"udf4\": \"string\",  \n\"udf5\": \"string\"  \n}",
    "8-0": "userToken  \n`optional`",
    "8-1": "`String`This parameter must contain the payment link creation from date.",
    "8-2": "2023-04-01",
    "9-0": "address  \n`optional`",
    "9-1": "`JSON`This parameter must contain the address details in a JSON format as in the example.",
    "9-2": "{  \n\"line1\": \"string\",  \n\"line2\": \"string\",  \n\"city\": \"string\",  \n\"state\": \"string\",  \n\"country\": \"string\",  \n\"zipCode\": \"string\"  \n}",
    "10-0": "reminder  \n`optional`",
    "10-1": "`JSON`This parameter must contain the following reminder details in a JSON format (as in the example):  \n  \n- scheduledAt: The time at the which the reminder was scheduled.\n- channels: The channels used to send the reminder. ",
    "10-2": "{  \n\"id\": 0,  \n\"scheduledAt\": \"string\",  \n\"channels\": [mobile]  \n}",
    "11-0": "customAttributes  \n`optional`",
    "11-1": "`JSON`This parameter must contain the  custom attributes in a JSON format as in the example.",
    "11-2": "{  \n\"customAttributeId\": 0,  \n\"entityType\": \"string\",  \n\"toolId\": 0,  \n\"customAttributeName\": \"string\",  \n\"attributeType\": \"string\",  \n\"options\": \\[],  \n\"checked\": true,  \n\"required\": true  \n}"
  },
  "cols": 3,
  "rows": 12,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```
curl --location --request PUT 'https://uatoneapi.payu.in/payment-links/INV1406204187' \
--header 'merchantId: 5018363' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 010c57cc96af33b84b2de81ee8c30b6f99a1976e74c2bd3fb5f4e5b535f25ae8' \
--header 'Cookie: PHPSESSID=7nv3d144qeh7g102p3uau1o6pm' \
--data '{
"active":false
}'

```

## Sample response

### Success scenario

```
{
  "status": 0,
  "message": "string",
  "result": {},
  "errorCode": 170,
  "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
}
```

### Failure scenario

```
{
  "status": -1,
  "message": "expiry cannot be less than the current date",
  "result": null,
  "errorCode": null,
  "guid": null
}
```