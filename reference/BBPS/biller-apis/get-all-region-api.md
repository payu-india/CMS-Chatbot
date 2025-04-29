---
title: Get All Region API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetAllRegion
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API will fetch all the regions, So that billers can be fetched according to the specific region.

<BBPSEnvironment />

<br />

> 📘 Note:
> 
> Send the scope of the Get Token API as **read_regions** to obtain the access_token for this request. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --request GET \
     --url https://bbps-sb.payu.in/payu-nbc/v1/nbc/getRegions \
     --header 'authorization: Bearer stsdafsdfasdfadsfasdfasdfasdfsdafadsf'
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
    "1-0": "regions",
    "1-1": "This field contains the region details in a JSON format.",
    "2-0": "regions.regionCode",
    "2-1": "This field contain the region code.",
    "3-0": "regions.regionName",
    "3-1": "This field contain the region name.",
    "4-0": "**Failure Scenarios**",
    "4-1": "",
    "5-0": "refId",
    "5-1": "For failure scenarios, This parameter contains the reference ID.  \n**Note**: In case of category fetch refId will be null.",
    "6-0": "type",
    "6-1": "For failure scenarios, this field contains the type of error.",
    "7-0": "payload",
    "7-1": "It will contain payload with error messages.",
    "8-0": "payload.errors",
    "8-1": "For failure scenarios, this field contains the following in the response:  \n  \n- **reason**: The error description if the request has failed.\n- **errorCode**: The error code of the error if the request has failed",
    "9-0": "message",
    "9-1": "For failure scenarios, this field contains the description of error type for failure or success.",
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
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "regions":[
         {
            "regionCode":"STRING",
            "regionName":"STRING"
         },
         {
            "regionCode":"STRING",
            "regionName":"STRING"
         },
         {
            "regionCode":"STRING",
            "regionName":"STRING"
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
            "reason":"<error reason>",
            "errorCode":"<error code>"
         }
      ],
      "refId":null,
      "type":"<type of message>",
      "message":"<message>",
      "additionalParams":{
         "Key1":"value1",
         "Key2":"value2",
         "Key3":"value3"
      }
   }
}
```

</summary>

## Request parameters