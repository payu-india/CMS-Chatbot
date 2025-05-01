---
title: Verify OTP API
excerpt: ''
api:
  file: partner-apis-21.json
  operationId: VerifyOTPAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Learn how to use the PayU Verity OTP API to securely verifying merchant
    details. This API Reference page provides detailed instructions, request
    parameters, and sample responses for efficient OTP management.
  keywords:
    - Verify OTP API
    - ' OTP verification'
    - ' secure OTP'
    - ' tokenization'
    - ' merchant verification'
    - ' bank details update'
    - ' Verify OTP'
  robots: index
next:
  description: ''
---
The **Verify OTP** API involves the following:

- Used to verify the OTP received on the merchant’s (users) phone number/email address through Send OTP API
- On successful OTP verification, the user token is shared in the response along with the Merchant ID (mid).
- This OTP verification will also link the merchant to your partner account with PayU incase the merchant is not referred/created by you on PayU
- This merchant linking process is ideal for platforms using only invoicing products of PayU

> 📘 Note:
> 
> The access token is required in the **Bearer** field of the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | \<https://uat-accounts.payu.in> |
| **Production** | \<https://accounts.payu.in>     |

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request POST '{{partner_base_url}}/api/v1/otps/verify_otp' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'otp[identity]=9044155723' \
--data-urlencode 'otp[email]=tally.onboarding0.akhil.khanna@payutest.in' \
--data-urlencode 'otp[code]=5154' \
--data-urlencode 'otp[type]=SignIn'
```

</details>

<details>
  <summary>Sample response</summary>

**Success scenario**

```
{
  "access_token": "2ed402f549adc354c7f681ca84a0dec7d9a91a8e229d3ee61e2440d1b61d26ec",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "user_profile create_bank_details update_bank_details",
  "created_at": 1594038150,
  "user_uuid": "11ea-bf7f-3063406a-85a0-02f413145cce",
  "reseller_uuid": null,
  "mid": "7060011",
  "merchant_uuid": "11ea-bf7f-2db8ef5e-9363-0acb18027a2a"
}
```

**Failure scenario**

| **Error Code** | **Description**                              | **Sample Code Block**                                                                                                                                                                                                                                                                                         |
| -------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 401            | When token is invalid/expired                | `{ “status”: “Unauthorized” }`                                                                                                                                                                                                                                                                                  |
| 422            | When OTP (type) is invalid                   | `{ “errors”: { “type”: [ “invalid” ] }, “messages”: { “type”: “Type has invalid value” }, “additional_data”: { “type”: { “value”: “SignInas” } } }`                                                                                                                                                          |
| 401            | When token does not have scopes              | `{ “status”: “Unauthorized” }`                                                                                                                                                                                                                                                                                  |
| 422            | When identity/channel is required            | `{ “errors”: { “identity”: [ “invalid_format” ], “channels”: [ “not_permitted” ] }, “messages”: { “identity”: “Identity has invalid value”, “channels”: “Channels has invalid value” }, “additional_data”: { “identity”: { “value”: “88027794841” }, “channels”: { “value”: [ “email”, “smsq” ] } } }` |
| 422            | When user does not exist with given identity | `{ “errors”: { “user”: [ “not_found” ] }, “messages”: { “user”: “User not found” }, “additional_data”: { “user”: { “search_term”: “9044199921” } } }`                                                                                                                                                      |
| 422            | When user account is locked                  | `{ “errors”: { “user”: [ “locked” ] }, “messages”: { “user”: “User account is locked” }, “additional_data”: { “user”: { “lock_duration”: 1744, “search_term”: “8802779484” } } }`                                                                                                                          |

</details>

## Request parameters