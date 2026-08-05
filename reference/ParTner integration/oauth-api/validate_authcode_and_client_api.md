---
title: Validate Auth Code and Client
excerpt: ''
api:
  file: validate-auth-code-4.json
  operationId: ValidateAuthCodeandClient
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Validate Auth Code and Client** API is used for validating auth code and client.

**Environment**

|                |                                |
| :------------- | :----------------------------- |
| **Test**       | \<https://uat-accounts.payu.in> |
| **Production** | \<https://accounts.payu.in>     |

> 📘 Notes:
> 
> - The grant type for the **grant_type** parameter for this API is** authorization_code**. 
> - For the client credentials, refer to [Download Client Credentials](doc:download-client-credentials).

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST 'https://test-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=68a276132f82c056a6ed9b5e00e45523c260544b87dd3cc91840d591bd93' \
--data-urlencode 'client_secret=93f29bd09aca64f304ee8380232310f7caa0bc2dcd838f15903dc85b0110b' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=23e563c95e3c433e38072fef0c8d18b21d8598c51eb498814e7c9cadd60edc09' \
--data-urlencode 'redirect_uri=http://www.abcdefghi/success'
```

</details>

<details>
  <summary>Sample response</summary>

**Success response**

- Status - 200

```
{
    "access_token": "e6ff7e34b704be2b14c8ae3c0e776597df4ae7de9e12d3e4c79781fcbbf2c4bb",
    "token_type": "Bearer",
    "expires_in": 7199,
    "refresh_token": "356fe080daa69438e0c2d3b0a80b3fe4aa3f78b264e6092e95e4429ae59486a7",
    "scope": "credentials_using_oauth create_payment_links read_payment_links update_payment_links delete_payment_links",
    "created_at": 1709198191,
    "user_uuid": "11ed-933c-d307ba06-b71a-0a64ecf8a4cc"
}
```

**Failure response**

<FailureResponseForValidateAuthCode />

</details>

<details>
  <summary>Response parameters</summary>

<PartnerAuthenticationResponseParameters />

</details>

## Request parameters