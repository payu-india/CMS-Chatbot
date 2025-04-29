---
title: Get Circle List API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetCircleList
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Get Circle List** API gets a list of all the available circles. There is no change in this API from v1 other than the endpoint.  

<BBPSEnvironment />

<br />

> 📘 Note:
> 
> This API requires an access token using the Get Token API with the scope as **read_circles**. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --location -g --request GET ' https:///payu-nbc/v2/nbc/getCircleList'  \
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

The **payload** parameter contains the values in a JSON format are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "**Success Scenario**",
    "0-1": "",
    "1-0": "circlesInfo",
    "1-1": "This field contains the following set of values for each circle in an JSON array format:  \n  \n- **circleRefID**: Contains the circle reference ID.\n- **circleName**: Contains the circle name",
    "2-0": "**Failure Scenario**",
    "2-1": "",
    "3-0": "refId",
    "3-1": "For failure scenarios, this parameter contains the reference ID.",
    "4-0": "type",
    "4-1": "This field contains the value as **circle\\_list\\_info** for this API.",
    "5-0": "error",
    "5-1": "For failure scenarios, this field contains the error message in an array format.",
    "6-0": "message",
    "6-1": "This field contains the message type as **circle\\_fetch\\_request\\_failed** for this API.",
    "7-0": "additionalParams",
    "7-1": "For failure scenarios, this field contains the additional fields related to billers in an array format. If there is no any additional info, it will be null. "
  },
  "cols": 2,
  "rows": 8,
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
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "circlesInfo":[
         {
            "circleRefID":"<id_1>",
            "circleName":"<circle_name_1>"
         }{
            "circleRefID":"<id_2>",
            "circleName":"<circleName_2>"
         }
      ]
   }
}
```

### Failure scenario

```
{
   "code":600,
   "status":"FAILURE",
   "payload":{
      "errors":[
         {
            "reason":"<error Message>",
            "errorCode":"<Error Code>"
         }
      ],
      "refId":null,
      "type":"circle_list_info",
      "message":"circle_fetch_request_failed",
      "additionalParams":{
         "Key1":"value1",
         "Key2":"value2",
         "Key3":"value3"
      }
   }
}
```

</details>

## Request parameters