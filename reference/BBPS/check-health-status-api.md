---
title: Check Health Status API
excerpt: ''
api:
  file: bbps-apis-agent-share-8.json
  operationId: heartBeatAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Check Health Status** API can be used to check the working status of the PayU server.

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the GET Token API as check_health_status to obtain the access_token for this request. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```curl
curl --location --request POST 'https://<hostName>/payu-nbc/v1/nbc/heartBeat?agentId={agentId}&refId={refId}' \
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
    "2-1": "It will contain a list of biller categories. For more information, refer to the [payload](#payload) table.  \nIf the transaction had failed, it will contain:  \n  \n- additional data related to transactions\n- List of errors which caused failure transactions"
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
    "h-0": "**Paramater**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter can contain any of the following:  \n  \n- UP\n- DOWN",
    "1-0": "type",
    "1-1": "This field contains the the type of request.",
    "2-0": "refId",
    "2-1": "This field contains the reference ID received in request from the agent.",
    "3-0": "payuId",
    "3-1": "It will be payU system ID and it will be unique every time.",
    "4-0": "message",
    "4-1": "For failure scenario, this field contains the message as **heart\\_beat\\_failure**.",
    "5-0": "errors",
    "5-1": "For failure scenario, the errors are displayed in an array format."
  },
  "cols": 2,
  "rows": 6,
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
    "refId": "<refId>",
    "status": "UP",
    "payuId": "<payUSytemId>"
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
        "reason": "<error reason>",
        "errorCode": "<error code>"
      }
    ],
    "refId": "<refId>",
    "type": "heart_beat",
    "message": "heart_beat_failed",
    "additionalParams": null
  }
}
```

</details>

## Request parameters