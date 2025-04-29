---
title: Send OTP API
excerpt: ''
api:
  file: send-otp-1.json
  operationId: send_otp
deprecated: false
hidden: false
metadata:
  title: Send OTP API for Partner Integration
  description: >-
    Learn how to use the PayU Send OTP API to securely send OTPs for verifying
    merchant details or updating bank information. This guide provides detailed
    instructions, request parameters, and sample responses for efficient OTP
    management.
  robots: index
next:
  description: ''
---
The **Send OTP** API is used to:

- Used to send the OTP to verify the merchant’s primary details or bank update details
- Used to generate the user token required for authorization

This is authorised through a client token generated using the client ID and secret.

> 📘 Note:
> 
> The access token is required in the **Bearer **field of the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | &lt;https://uat-accounts.payu.in&gt; |
| **Production** | &lt;https://accounts.payu.in&gt;     |

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request POST '{{partner_base_url}}/api/v1/otps/send_otp' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'otp[identity]=9044199921' \
--data-urlencode 'otp[scope]=user_profile' \
--data-urlencode 'otp[channels]=sms' \
--data-urlencode 'otp[type]=SignIn'
```

</details>

<details>
  <summary>Sample request</summary>

```
{
  "data": {
    "id": "11ea-bf84-27aef522-85a0-02f413145cce",
    "type": "notifications",
    "attributes": {
      "status": "sidekiq_queued",
      "send-at": "1594038491",
      "status-details": {},
      "payload": {
        "sms": [
          "90xxxxxx21"
        ]
      }
    }
  }
}
```

</details>

## Request Parameters

<details>
  <summary>Additional info for request parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "otp[scope]",
    "0-1": "Indicates the purpose of the API. The following APIs use different scopes in this field  \n_   Add or Update Bank Detail API uses any of the following according to the use case:  \n    -   create_bank_details  \n    -  update_bank_details  \n_   For Payment Link APIs:  \n   - Create Payment Link API: create_payment_links  \n   - Get Single Payment Link API: read_payment_links  \n   - Change Status and Expiry for a Payment Link API: update_payment_links"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]

</details>