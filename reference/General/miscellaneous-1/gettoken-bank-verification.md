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
# Get Token API

This **Get Token API** returns the authentication token generated using the client ID and client secret where, `grant_type` is **client\_credentials** and `scope` is **verify\_bank\_account**.

## Environment

| Environment | URL                                                      |
| ----------- | -------------------------------------------------------- |
| Production  | [https://accounts.payu.in](https://accounts.payu.in)     |
| Test        | [https://onboarding.payu.in](https://onboarding.payu.in) |

## Request parameters

| Parameter                                  | Details                                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id<br /><code>mandatory</code>     | String: This field is the Client ID that was provided by PayU while onboarding.                                                                   |
| client\_secret<br /><code>mandatory</code> | String: This field is the Client secret that was provided by PayU while onboarding.                                                               |
| grant\_type<br /><code>mandatory</code>    | String: This parameter contains a constant value used to get the access token. For Bank Verification API, it is <code>client\_credentials</code>. |
| scope<br /><code>mandatory</code>          | String: This parameter will vary based on the use case. For Bank Verification API, it is <code>verify\_bank\_account</code>.                      |

## Sample request

```bash
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

| Parameter     | Description                                              |
| ------------- | -------------------------------------------------------- |
| access\_token | The access token to be used in Partner Integration APIs. |
| token\_type   | The token type of the access token.                      |
| expires\_in   | The expiry time in seconds of the access token.          |
| scope         | The scope of the access token.                           |
| created\_at   | The UNIX time stamp when the access token was created.   |

> 📘 **Note:**
>
> The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires\_in** parameter of the response. For example, in the following response, the value of the **expires\_in** is 7200 seconds:
>
> ```json
> {
>   "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
>   "token_type": "Bearer",
>   "expires_in": 7200,
>   "scope": "send_sign_in_otp",
>   "created_at": 1595411399
> }
> ```

## Sample response

```json
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "send_sign_in_otp",
  "created_at": 1595411399
}
```