---
title: Share Payment Link API
excerpt: ''
api:
  file: payment-link-4.json
  operationId: SharePaymentLinkAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to share the payment link in the given list of email IDs.

**Environment**

|                        |                                                      |
| :--------------------- | :--------------------------------------------------- |
| Test Environment       | <https://uatoneapi.payu.in/payment-links/{id}/share> |
| Production Environment | <https://oneapi.payu.in/payment-links/{id}/share>    |

> 📘 Note:
> 
> The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

<details> <summary>Sample request</summary>

```curl
		curl --request POST \
     --url https://uatoneapi.payu.in/payment-links/ \
     --header 'authorization: Bearer fjsdkglfd09845084395' \
     --header 'content-type: text/plain' \
     --header 'merchantId: 5016764' \
     --data ashish@gmail.com							
```

</details>

<details> <summary>Sample response </summary>

```
{
  "status": 0,
  "message": "string",
  "result": {},
  "errorCode": 170,
  "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
}
```

</details>

## Request headers

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "mid  \n**mandatory**",
    "0-1": "`String` This contains the merchant identifier.",
    "1-0": "Authorization  \n**mandatory**",
    "1-1": "Bearer `String` This contains the client\\_token. For getting a token, refer to [Get Token API](ref:get_token_api)"
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


## Query parameters

<details> <summary> Reference info for request parameters </summary>

| Parameter   | Reference                                                                                                         |
| :---------- | :---------------------------------------------------------------------------------------------------------------- |
| channelList | `String` This parameter must contain all the emails & phone numbers to which the payment link needs to be shared. |

</details>