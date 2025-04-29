---
title: Get Biller Categories API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetBillerCategories
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Biller Categories** API will fetch all the categories from PayU.

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the GET Token API as **read\_biller\_categories** to obtain the access_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --location -g --request GET 'https://{{host_name}/payu-nbc//v1/getbillercategory' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

</details>

<details><summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "code",
    "0-1": "The global response code and can be any of the following:  \n  \n- **0**: If web service call failed\n- **1**: if web service call succeeded",
    "1-0": "status",
    "1-1": "The status of the API command and can be any of the following:  \n  \n- SUCCESS\n- FAILURE",
    "2-0": "payload",
    "2-1": "It will contain a list of biller categories. For more information, refer to the [payload](#payload) table."
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
    "9-1": "For failure scenarios, this field contains the following in the response:  \n  \n- **reason**: The error description if the request has failed.\n- **errorCode**: The error code of the error if the request has failed",
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


</details>

<details><summary>Sample response</summary>

### Success scenario

```
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

### Failure scenario

```
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

</details>

## Request Parameters

No request parameters input required for this API.