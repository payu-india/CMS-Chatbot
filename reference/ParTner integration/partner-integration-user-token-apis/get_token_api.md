---
title: Get Token API - Partner Integration
excerpt: ''
api:
  file: partner-apis-16.json
  operationId: get_token
deprecated: false
hidden: false
metadata:
  title: Get Token API - Partner Integration
  description: >-
    The Get Token API generates an authentication token for Payment Link API
    Integration and Partner Integration API Integration, using client ID and
    client secret. The token has configurable expiry time and various scopes for
    different functionalities.
  keywords:
    - Get Token API for Partner Integration
    - ' Get Token API for Payment Links'
    - Get Token API for Partner Integration
    - Get Token API for Partner Onboarding
    - Get Token API for refer_merchant scope
    - ' Get Token API for send_sign_in_otp scope'
    - Get Token API for verify_sign_in_otp
    - Get Token API for client_manage_agreement scope
    - Get Token API for client_manage_kyc_details
    - Get Token API for create_bank_details
    - Get Token API for user_token scope
    - Get Token API for create_payment_links
  robots: index
next:
  description: ''
---
The **Get Token API** returns the authentication token generated using the client ID and client secret for the following products: 

- [Payment Link API Integration](doc:integration-api-for-payment-links)
- [Partner Integration API Integration](doc:refer-merchants)

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
    "2-1": "The scopes to be used for various use cases in Parter Integration are:  \n  \n- Refer Merchant, Verify Link Merchant, Get Merchant, and Update Merchant: **refer_merchant**\n- Send Sign In OTP: **send_sign_in_otp**\n- Verify Sign In OTP: **verify_sign_in_otp**\n- Client Manage Agreement (Used in E-Sign flow): **client_manage_agreement**\n- Client Manage KYC Details (Used in managing KYC documents): **client_manage_kyc_details**\n- Create Bank Details: **create_bank_details**\n- Penny Verify - **user_token**\n- Manage Payment Links: **create_payment_links**",
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