---
title: Get Auth Token API - BBPS
excerpt: ''
api:
  file: bbps-apis-agent-share.json
  operationId: AuthToken
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API returns the authentication token generated using the client ID and client secret.

> 📘 Note:
>
> The token received using this API has to be passed in the authorization headers to authorize each subsequent request. Example: **Authorization: Bearer `{token_value}`**

<BBPSEnvironment />

<details>
  <summary> Sample request</summary>

```curl
curl -X POST \ 
  'https://<hostName>/oauth/token' \ 
  -H 'content-type: application/x-www-form-urlencoded' \ 
  -d 'client_id=&lt;agent client id shared by payu&gt;&client_secret=&lt;client secret id shared by payu&gt;&grant_type=client_credentials&scope=&lt;scopes&gt;' 
```

</details>

<details>
  <summary> Response parameters</summary>

| **Field Name** | **Description**                                               |
| -------------- | ------------------------------------------------------------- |
| access\_token  | The access token for the validation for all subsequent apis.  |
| token\_type    | The token type and It will always be **Bearer**.              |
| expires\_in    | The expiry time for the token will be in seconds.             |
| scope          | The scope for which the token is applicable for.              |
| created\_at    | The time stamp when the token was created in UNIX format.     |

</details>

<details>
  <summary> Sample response</summary>

* Success scenario

```plaintext
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "read_transactions",
  "created_at": 1595411399
}
```

* Failure scenario

```plaintext
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "&lt;error message&gt;", 
        "errorCode": "&lt;error code&gt;" 
      } 
    ], 
    "refId": null, 
    "type": "category_response", 
    "message": "category_response_failed", 
    "additionalParams":{ 
           "Key1": "value1", 
           "Key2": "value2", 
           "Key3": "value3" 
     } 
  } 
} 
```

</details>

## Request Parameters