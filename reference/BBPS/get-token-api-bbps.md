---
title: Get Token API - BBPS
excerpt: ''
api:
  file: payout-for-merchants-41.json
  operationId: GenerateTokenusingMerchant'sCredentialsAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Token API** returns the authentication token generated using the client ID and client secret.

### Environment

| Test           | <https://uat-accounts.payu.in> |
| :------------- | :----------------------------- |
| **Production** | <https://accounts.payu.in>     |

## Additional information for request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameters",
    "h-1": "Description",
    "0-0": "client_id",
    "0-1": "For getting your client ID, refer to [Download Client Credentials](doc:download-client-credentials).",
    "1-0": "client_secret",
    "1-1": "For getting your client secret, refer to [Download Client Credentials](doc:download-client-credentials).",
    "2-0": "scope",
    "2-1": "The scopes used in BBPS are:  \n  \n- read_bills\n- create_transactions\n- read_billers\n- read_biller_categories\n- read_transactions\n- read_plans  \n  The scope varies for each BBPS API and refer the first \"Note\" of the API reference for the scope.",
    "3-0": "grant_type",
    "3-1": "This parameter contains a constant value used to get the access token. The grant_type used across the BBPS will be share by PayU."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

<details><summary>Response parameters</summary>

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

</details>

## Request parameters