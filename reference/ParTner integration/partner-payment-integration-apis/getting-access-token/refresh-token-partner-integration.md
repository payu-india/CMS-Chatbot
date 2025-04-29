---
title: Refresh Token API - Partner Integration
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
This API is used to generate a refresh token to obtain a renewed access token using client ID.

> 📘 Note:
> 
> You can use this API when the token generated using the** Get Token **API has expired. The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires_in** parameter of the response.

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | <https://uat-accounts.payu.in> |
| **Production** | <https://accounts.payu.in>     |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "client\\_ID  \n**mandatory**",
    "0-1": "`String`This parameter will contain the public Client ID.",
    "0-2": "`6f8bb4951e030d4d7349e64a144a53477\n8673585f86039617c167166e9154f7e`",
    "1-0": "client\\_secret  \n**optional**",
    "1-1": "`String`This parameter will contain the client secret.",
    "1-2": "",
    "2-0": "grant\\_type  \n**mandatory**",
    "2-1": "`String`This parameter will contain the value as **refresh\\_token**.",
    "2-2": "refresh\\_token",
    "3-0": "refresh\\_token  \n**mandatory**",
    "3-1": "`String` Indicates the refresh token. This is the token that was generated using the  [Get Access Token - WhatsApp](ref:getting-access-token).",
    "3-2": " "
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


## Sample request

```curl
curl --location -g --request POST 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token={{refresh_token}}'
```

## Response parameters

<PartnerAuthenticationResponseParameters />

## Sample response

### Successful transaction

Success

```plaintext
{
  "access_token": "8703474d8779483d9a298666faafa1ee5c1fc24c71dc1890dc7484e19cf27c9e",
  "token_type": "Bearer",
  "expires_in": 7199,
  "refresh_token": "249fbf69a7841aa28cc494984b45efcb22537c0cedbb672c6fa18ba8eb21d8ce",
  "scope": "hub_session",
  "created_at": 1553511296,
  "user_uuid": "11e7-a7f6-f0494f6c-bbb7-4a020b6b2b14"
}
```

### Failure scenarios

<RefreshTokenSampleResponse />