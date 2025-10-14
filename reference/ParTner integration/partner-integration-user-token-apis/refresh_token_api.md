---
title: Refresh Token API
excerpt: refresh_token
api:
  file: partner-apis-16.json
  operationId: refresh_token
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: ''
  description: ''
  robots: index
---
This API is used to generate a refresh token to obtain a renewed access token using client ID.

<Callout icon="📘" theme="info">
  **Note**: You can use this API when the token generated using the** Get Token **API has expired. The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) of the token is displayed in the **expires_in** parameter of the response.
</Callout>

**Environment**

|                |                                                                                       |
| :------------- | :------------------------------------------------------------------------------------ |
| **Test**       | [https://uat-accounts.payu.in/oauth/token](https://uat-accounts.payu.in/oauth/token). |
| **Production** | \<[https://accounts.payu.in>](https://accounts.payu.in>)                              |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --request POST \
       --url https://uat-accounts.payu.in/token \
       --header 'Content-Type: application/x-www-form-urlencoded' \
       --header 'accept: application/json; charset=utf-8' \
       --data 'client_id={{client_id}}' \
       --data 'client_secret={{client_secret}}' \
       --data grant_type=refresh_token \
       --data 'refresh_token={{refresh_token}}'
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Successful transaction**

  ```plaintext
  {
    "access_token": "8703474d8779483d9a298666faafa1ee5c1fc24c71dc1890dc7484e19cf27c9e",
    "token_type": "Bearer",
    "expires_in": 7199,
    "refresh_token": "249fbf69a7841aa28cc494984b45efcb22537c0cedbb672c6fa18ba8eb21d8ce",
    "scope": "hub_session",
    "created_at": 1553511296,
    "user_uuid": "11e7-a7f6-f0494f6c-bbb7-4a020b6b2b14"
  }
  ```

  **Failure scenarios**

  <RefreshTokenSampleResponse />
</details>

<details>
  <summary>Response parameters</summary>

  <PartnerAuthenticationResponseParameters />
</details>

## Request Parameters

<details>
  <summary>Additional Information for Request Parameters</summary>

  | Parameters     | Description                                                                                              |
  | -------------- | -------------------------------------------------------------------------------------------------------- |
  | client\_id     | For getting your client ID, refer to [Download Client Credentials](doc:download-client-credentials).     |
  | client\_secret | For getting your client secret, refer to [Download Client Credentials](doc:download-client-credentials). |
</details>