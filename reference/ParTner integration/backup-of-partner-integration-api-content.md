---
title: Backup of Partner Integration API Content
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Get Token API

The **Get Token** API returns the authentication token generated using the client ID and client secret.

### Environment

| Test           | <https://uat-accounts.payu.in> |
| :------------- | :----------------------------- |
| **Production** | <https://accounts.payu.in>     |

## Additional Information for Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameters",
    "h-1": "Description",
    "0-0": "client_id",
    "0-1": "For getting your client ID, refer to [Download Client Credentials](https://devguide.payu.in/docs/download-client-credentials).",
    "1-0": "client_secret",
    "1-1": "For getting your client secret, refer to [Download Client Credentials](https://devguide.payu.in/docs/download-client-credentials).",
    "2-0": "scope",
    "2-1": "The scope varies based on the any of the use case:  \n  \n- **Refer Merchant**: refer\\_merchant.  \n- **Send Sign In OTP**: send\\_sign\\_in\\_otp  \n- **Verify Sign In OTP**: verify\\_sign\\_in\\_otp  \n- **Client Manage Agreement (Used in E-Sign flow)**: client\\_manage\\_agreement  \n- **Client Manage KYC Details (Used in managing KYC documents)**: client\\_manage\\_kyc\\_details"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]

## Response Parameters Description

| Parameter    | Description                                              |
| :----------- | :------------------------------------------------------- |
| access_token | The access token to be used in Partner Integration APIs. |
| token_type   | The token type of the access token.                      |
| expires_in   | The expiry time in seconds of the access token.          |
| scope        | The scope of the access token.                           |
| created_at   | The UNIX time stamp when the access token was created.   |

# Send OTP API

The **Send OTP** API is used to:

- Used to send the OTP to verify the merchant’s primary details or bank update details
- Used to generate the user token required for authorization

This is authorised through a client token generated using the client ID and secret.

### Environment

| Test           | <https://uat-accounts.payu.in> |
| :------------- | :----------------------------- |
| **Production** | <https://accounts.payu.in>     |

# Verify OTP API

The **Verify OTP** API involves the following:

- Used to verify the OTP received on the merchant’s (users) phone number/email address through Send OTP API
- On successful OTP verification, the user token is shared in the response along with the Merchant ID (mid).
- This OTP verification will also link the merchant to your partner account with PayU incase the merchant is not referred/created by you on PayU
- This merchant linking process is ideal for platforms using only invoicing products of PayU

### Environment

| Test           | <https://uat-accounts.payu.in> |
| :------------- | :----------------------------- |
| **Production** | <https://accounts.payu.in>     |

# Add or Update Bank Details

This API is used to perform the following:

- Used to add or update the bank account details, only after a successful verification of merchant’s PAN card details.
- Authorized using the user token received from verify OTP API

### Environment

| Test           | <https://uat-partner.payu.in/> |
| :------------- | :----------------------------- |
| **Production** | <https://partner.payu.in/>     |

The access token with the **scope** as create_bank_details (to create bank details) or update_bank_details (to update bank details) using the User Token APIs is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:user-token-apis).