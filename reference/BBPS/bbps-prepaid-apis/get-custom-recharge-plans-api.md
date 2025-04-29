---
title: Get Custom Recharge Plans API
excerpt: ''
api:
  file: bbps-apis-agent-share-6.json
  operationId: GetCustomRechargePlans
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Custom Recharge Plans**API for getting available prepaid plans for a mobile number. 

<BBPSEnvironment />

> 📘 Note:
> 
> This API requires an access token using the Get Token API with the scope as **read_plans**. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```curl
curl --location --request GET 'https://payu-nbc/v2/nbc/getCustomizedRechargePlans?agentId={agentId}&circleId={circleId}&mobileNo={mobileNumber}&operatorId={operatorId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
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
    "1-1": "This field contains the following set of values for each circle in an JSON array format:  \n  \n- **planName**: This field contains the plan name.\n- **price**: This field contains the plan price.\n- **validity**: This field contains the validity period of the plan.\n- **talkTime**: This field contains the talk time for the plan.\n- **validityDescription**: This field contains the validity description.\n- **packageDescription**: This field contains the package description.\n- **planType**: This field contains the plan type.",
    "2-0": "**Failure Scenario**",
    "2-1": "",
    "3-0": "refId",
    "3-1": "For failure scenarios, this parameter contains the reference ID.",
    "4-0": "type",
    "4-1": "This field contains the value as **mobile_plans** for this API.",
    "5-0": "error",
    "5-1": "For failure scenarios, this field contains the error message in an array format.",
    "6-0": "message",
    "6-1": "This field contains the message type as **mobile_plans_fetch_failed.** for this API.",
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
      "operatorName":"OPERATOR_1",
      "operatorId":"OPERATOR_ID_1",
      "plansInfo":[
         {
            "planName":"<plan_name_1>",
            "price":"<plan_price>",
            "validity":"<validity>",
            "validityDescription":"<description>",
            "talkTime":"<talk_time>",
            "packageDescription":"<description>",
            "planType":"<plan_type_1>"
         },
         {
            "planName":"<plan_name_2>",
            "price":"<plan_price>",
            "validity":"<validity>",
            "validityDescription":"<description>",
            "talkTime":"<talk_time>",
            "packageDescription":"<description>",
            "planType":"<plan_type_2>"
         }
      ]
   }
}
```

### Failure scenario

```
"code":600,
"status":"FAILURE",
"payload":{
   "errors":[
      {
         "reason":"<error Message>",
         "errorCode":"<Error Code>"
      }
   ],
   "refId":"<refId>",
   "type":"mobile_plans",
   "message":"mobile_plans_fetch_failed",
   "additionalParams":{
      "Key: "value1",
"Key2": "value2",
"Key3": "value3"\"\"
}
}
}"
```

</details>

## Request parameters