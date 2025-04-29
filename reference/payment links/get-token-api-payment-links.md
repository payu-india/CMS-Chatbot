---
title: Get Token API - Payment Links
excerpt: ''
api:
  file: payout-for-merchants-40.json
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
    "0-1": "For getting your client ID, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)",
    "1-0": "client_secret",
    "1-1": "For getting your client secret, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard)",
    "2-0": "scope",
    "2-1": "The scope that must be used for payment links are:  \n  \n- **Create Link**: create_payment_links\n- **Change status and expiry**: update_payment_links\n- **Get a single payment link**:read_payment_links\n- **Get all payment links**: read_payment_links\n- **Share payment links**: read_payment_links**Note**: Merchant can pass up to three scopes simultaneously for an access token value. This is done by passing scopes separated by a space between them. For example:  \n  create_payment_links update_payment_links read_payment_links",
    "3-0": "grant_type",
    "3-1": "This parameter contains a constant value used to get the access token. The grant_type used across the partner integration is **client_credentials**."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


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