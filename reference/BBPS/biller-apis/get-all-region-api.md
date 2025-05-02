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


> 📘 Note:
>
> Send the scope of the Get Token API as **read\_regions** to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```
curl --request GET \
     --url https://bbps-sb.payu.in/payu-nbc/v1/nbc/getRegions \
     --header 'authorization: Bearer stsdafsdfasdfadsfasdfasdfasdfsdafadsf'
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>**Field Name**</th>
      <th>**Description**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>code</td>
      <td>
        The global response code and can be any of the following:
        * **0**: If web service call failed
        * **1**: if web service call succeeded
      </td>
    </tr>
    <tr>
      <td>status</td>
      <td>
        The status of the API command and can be any of the following:
        * SUCCESS
        * FAILURE
      </td>
    </tr>
    <tr>
      <td>payload</td>
      <td>
        It will contain a list of biller categories. For more information, refer to the [payload](#payload) table.
      </td>
    </tr>
  </tbody>
</Table>

### payload

<Table>
  <thead>
    <tr>
      <th>**Field Name**</th>
      <th>**Description**</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>**Success Scenarios**</td>
      <td></td>
    </tr>
    <tr>
      <td>regions</td>
      <td>This field contains the region details in a JSON format.</td>
    </tr>
    <tr>
      <td>regions.regionCode</td>
      <td>This field contain the region code.</td>
    </tr>
    <tr>
      <td>regions.regionName</td>
      <td>This field contain the region name.</td>
    </tr>
    <tr>
      <td>**Failure Scenarios**</td>
      <td></td>
    </tr>
    <tr>
      <td>refId</td>
      <td>
        For failure scenarios, This parameter contains the reference ID.
        * \*Note\*\*: In case of category fetch refId will be null.
      </td>
    </tr>
    <tr>
      <td>type</td>
      <td>For failure scenarios, this field contains the type of error.</td>
    </tr>
    <tr>
      <td>payload</td>
      <td>It will contain payload with error messages.</td>
    </tr>
    <tr>
      <td>payload.errors</td>
      <td>
        For failure scenarios, this field contains the following in the response:
        * **reason**: The error description if the request has failed.
        * **errorCode**: The error code of the error if the request has failed
      </td>
    </tr>
    <tr>
      <td>message</td>
      <td>For failure scenarios, this field contains the description of error type for failure or success.</td>
    </tr>
    <tr>
      <td>additionalParams</td>
      <td>For failure scenarios, this field contains the additional fields (if any) related to billers in an array format.</td>
    </tr>
  </tbody>
</Table>

</details>

<details>
  <summary>Sample response</summary>

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

</details>

## Request parameters