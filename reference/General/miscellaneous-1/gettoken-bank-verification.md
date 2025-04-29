---
title: Get Token API - Bank Verification
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
This **Get Token API** returns the authentication token generated using the client ID and client secret where,  `grant_type` is **client_credentials** and `scope` is **verify_bank_account**.

## Environment

|            |                            |
| :--------- | :------------------------- |
| Production | <https://accounts.payu.in> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Details",
    "0-0": "client_id  \n`mandatory`",
    "0-1": "String: This field is the Client ID that was provided by PayU while onboarding.",
    "1-0": "client_secret  \n`mandatory`",
    "1-1": "String: This field is the Client secret that was provided by PayU while onboarding.",
    "2-0": "grant_type  \n`mandatory`",
    "2-1": "String: This parameter contains a constant value used to get the access token. For Bank Verification API, it is `client_credentials`.",
    "3-0": "scope  \n`mandatory`",
    "3-1": "String: This parameter will vary based on the use case. For Bank Verification API, it is `verify_bank_account`."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```
curl --request POST \
     --url https://uat-accounts.payu.in/oauth/token \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data grant_type=client_credentials \
     --data scope=verify_bank_account \
     --data 'client_id=<client_id>' \
     --data 'client_secret=<client_secret>'
```

## Response parameters

| Parameter    | Description                                              |
| :----------- | :------------------------------------------------------- |
| access_token | The access token to be used in Partner Integration APIs. |
| token_type   | The token type of the access token.                      |
| expires_in   | The expiry time in seconds of the access token.          |
| scope        | The scope of the access token.                           |
| created_at   | The UNIX time stamp when the access token was created.   |

> 📘 Note:
> 
> The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires_in** parameter of the response. For example, in the following response, the value of the **expires_in** is 7200 seconds:
> 
> ```
> {
>   "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
>   "token_type": "Bearer",
>   "expires_in": 7200,
>   "scope": "send_sign_in_otp",
>   "created_at": 1595411399
> }
> ```

## Sample response

```
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "send_sign_in_otp",
  "created_at": 1595411399
}
```