---
title: Generate Token using Private Client ID
excerpt: ''
api:
  file: payout-for-merchants-13.json
  operationId: GenerateTokenusingPrivateClientID
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to generate authentication tokens using client\_secret and private client ID. You must pass the generated token as the value of the **Authorization** header for all Payout APIs.

HTTP Method: **POST**

<PAYOUTSEnvironment />

<details><summary>Sample request</summary>

```
curl -X POST \
 https://uat-accounts.payu.in/oauth/token \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/x-www-form-urlencoded' \
 -d 'grant_type=client_credentials&client_id=cf608fd***4fd52f94fb**02e4bb431641c40339991787568773411df368&client_secret=26ec3cc4bc7caaasdf90b006b655582b92ed0116554597942a884c6cb626e3f&scope=create_payout_transactions'
```

</details>

<details><summary>Sample response</summary>

```
{
  "access_token": "994as40fd3bee9a0e830b5a5743a93d4f5c32c84f637510b128a7c69586ab8d",
  "token_type": "Bearer",
  "expires_in": 6351,
  "scope": "create_payout_transactions",
  "created_at": 1585215909
}
```

</details>

<details><summary>Response parameters</summary>

| **Parameters** | **Description**                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| access\_token  | Indicates the Security Token used to get access in Payouts API calls.                                                              |
| expire\_in     | Indicates the TTL i.e., the time limit (in seconds) after which the Security Token will expire                                     |
| scope          | Represents the allowed scopes in generated security token. For e.g., the generated token can be used only for Payouts API requests |
| created\_at    | Indicates the Time of creation in milliseconds                                                                                     |

</details>

## Request parameters

> 📘 Note:
> 
> Use your test client ID and secret that was provided by PayU. For getting your client_id and client_secret, refer to [Get Client ID and Secret from Dashboard](doc:get-client-id-and-secret-from-dashboard).