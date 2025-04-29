---
title: Additional Info for BBPS APIs
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
## Response Parameters for Get Token API

| **Field Name** | **Description**                                               |
| -------------- | ------------------------------------------------------------- |
| access\_token  | The access token for the validation  for all subsequent apis. |
| token\_type    | The token type and It will always be **Bearer**.              |
| expires\_in    | The expiry time for the token will be in seconds.             |
| scope          | The scope for which the token is applicable for.              |
| created\_at    | The time stamp when the token was created in UNIX format.     |

### Sample Response

- Success scenario

```plaintext
{
  "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
  "token_type": "Bearer",
  "expires_in": 7200,
  "scope": "read_transactions",
  "created_at": 1595411399
}
```

- Failure scenario

```plaintext
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "<error message>", 
        "errorCode": "<error code>" 
      } 
    ], 
    "refId": null, 
    "type": "category_response", 
    "message": "category_response_failed" 
    "additionalParams":{ 
           "Key1": "value1" 
           "Key2": "value2" 
           "Key3": "value3" 
     } 
  } 
} 
```

## Response Parameters for Get Biller Categories API

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "code",
    "0-1": "The global response code and can be any of the following:  \n   - **0**: If web service call failed  \n   - **1**: if web service call succeeded",
    "1-0": "status",
    "1-1": "The status of the API command and can be any of the following:  \n   - SUCCESS  \n   - FAILURE",
    "2-0": "payload",
    "2-1": "It will contain a list of biller categories. For more information, refer to [payload](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/get-biller-categories/#payLoad)."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


### payload

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "**Success Scenarios**",
    "0-1": "",
    "1-0": "billerCategories",
    "1-1": "This field contains the biller categories in an array format.",
    "2-0": "**Failure Scenarios**",
    "2-1": "",
    "3-0": "refId",
    "3-1": "For failure scenarios, This parameter contains the reference ID.  \n**Note**: In case of category fetch refId will be null.",
    "4-0": "type",
    "4-1": "For failure scenarios, this field contains the type of error.",
    "5-0": "code",
    "5-1": "The global response code",
    "6-0": "payload",
    "6-1": "It will contain payload with error messages.",
    "7-0": "status",
    "7-1": "The status of the response. Example, SUCCESS/FAILURE",
    "8-0": "message",
    "8-1": "For failure scenarios, this field contains the description of error type for failure or success.",
    "9-0": "errors",
    "9-1": "For failure scenarios, this field contains the following in the response:  \n   - **reason**: The error description if the request has failed.  \n   - **errorCode**: The error code of the error if the request has failed",
    "10-0": "additionalParams",
    "10-1": "For failure scenarios, this field contains the additional fields (if any) related to billers in an array format."
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


### Sample response

- Success scenario

```plaintext
{ 
  "code": 200, 
  "status": "SUCCESS", 
  "payload": { 
    "billerCategories": [ 
      "INSURANCE", 
      "LOAN", 
      "EDUCATION", 
      "SOCIETY BILLER" 
    ] 
  } 
}
```

- Failure scenario

```plaintext
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "<error message>", 
        "errorCode": "<error code>" 
      } 
    ], 
    "refId": null, 
    "type": "category_response", 
    "message": "category_response_failed" 
    "additionalParams":{ 
           "Key1": "value1" 
           "Key2": "value2" 
           "Key3": "value3" 

     } 
  } 
 
} 
```