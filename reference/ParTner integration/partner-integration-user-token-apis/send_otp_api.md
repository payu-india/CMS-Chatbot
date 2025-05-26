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

* Used to send the OTP to verify the merchant’s primary details or bank update details
* Used to generate the user token required for authorization

This is authorised through a client token generated using the client ID and secret.

> 📘 Note:
>
> The access token is required in the \*\*Bearer \*\*field of the header. To obtain the bearer token,
>
> * Use the scope - **send\_sign\_in\_otp** in the Get Token API.
>
> For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

**Environment**

|                |                                                                 |
| :------------- | :-------------------------------------------------------------- |
| **Test**       | \<[https://uat-accounts.payu.in](https://uat-accounts.payu.in)> |
| **Production** | \<[https://accounts.payu.in](https://accounts.payu.in)>         |

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

  <HTMLBlock>{`
    <table style="width: 100%; border-collapse: collapse;">
    <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
      <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>otp[scope]</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Indicates the purpose of the API. The following APIs use different scopes in this field<br>_   Add or Update Bank Detail API uses any of the following according to the use case:<br>    -   create_bank_details<br>    -  update_bank_details<br>_   For Payment Link APIs:  </p>
    <ul>
    <li>Create Payment Link API: create_payment_links  </li>
    <li>Get Single Payment Link API: read_payment_links  </li>
    <li>Change Status and Expiry for a Payment Link API: update_payment_links</li>
    </ul>
    </td>
    </tr>
    </tbody>
    </table>
  `}</HTMLBlock>
</details>