---
title: Revoke Token API
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
The Revoke Token API (**revoke\_token**) is used to revoke or delete the token generated earlier using the Get Token API. For more information, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

HTTP Method: **POST**

**Environment**

|                            |                                              |
| -------------------------- | -------------------------------------------- |
| **Test Environment**       | <https://uat-accounts.payu.in/payment-links> |
| **Production Environment** | <https://accounts.payu.in/payment-links>     |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "client\\_id  \n**mandatory**",
    "0-1": "`String` This parameter must contain the public identifier of the client to access the platform.",
    "0-2": "{{client\\_id}}",
    "1-0": "client\\_secret  \n**mandatory**",
    "1-1": "`String` This parameter must contain a unique secret of the client for authorization.",
    "1-2": "{{client\\_secret}}",
    "2-0": "token",
    "2-1": "`String`This parameter must contain the token that must be revoked.",
    "2-2": "{{token}}"
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


## Sample request

```curl
curl --location -g --request POST 'https://uat-accounts.payu.in/revoke' \
--header 'merchantId: {{merchantId}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
}'
```