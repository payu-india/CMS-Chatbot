---
title: Get Operators List API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetOperatorsList
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Operator List** API gets all the available operators related to mobile prepaid recharge with basic information. There is no change in this API from v1 other than the endpoint.

<BBPSEnvironment />

> 📘 Note:
>
> This API requires an access token using the Get Token API with the scope as **read\_operators**. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```
curl --location -g --request GET ' https:///payu-nbc/v2/nbc/getOperatorList'  \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

</details>

<details>
  <summary>Response parameters</summary>

<Table>
  <thead>
    <tr>
      <th>
        **Field Name**
      </th>
      <th>
        **Description**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        code
      </td>
      <td>
        The global response code and can be any of the following:  

        * **0**: If web service call failed
        * **1**: if web service call succeeded
      </td>
    </tr>
    <tr>
      <td>
        status
      </td>
      <td>
        The status of the API command and can be any of the following:  

        * SUCCESS
        * FAILURE
      </td>
    </tr>
    <tr>
      <td>
        payload
      </td>
      <td>
        It will contain a list of biller categories. For more information, refer to the [payload](#payload) table.
      </td>
    </tr>
  </tbody>
</Table>

### payload

The **payload** parameter contains the values in a JSON format are described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>
      <th>
        **Description**
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        **Success Scenario**
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        circlesInfo
      </td>
      <td>
        This field contains the following set of values for each circle in an JSON array format:  

        * **operatorCode**: Contains the code of the operator.
        * **operatorName**: Contains the name of the operator
        * **fixedBill**: Contains the flag whether the bill is fixed (**True**) or not fixed (**False**)
      </td>
    </tr>
    <tr>
      <td>
        **Failure Scenario**
      </td>
      <td>
      </td>
    </tr>
    <tr>
      <td>
        refId
      </td>
      <td>
        For failure scenarios, this parameter contains the reference ID.
      </td>
    </tr>
    <tr>
      <td>
        type
      </td>
      <td>
        This field contains the value as **operator\_list** for this API.
      </td>
    </tr>
    <tr>
      <td>
        error
      </td>
      <td>
        For failure scenarios, this field contains the error message in an array format.
      </td>
    </tr>
    <tr>
      <td>
        message
      </td>
      <td>
        This field contains the message type as **operator\_fetch\_request\_failed** for this API.
      </td>
    </tr>
    <tr>
      <td>
        additionalParams
      </td>
      <td>
        For failure scenarios, this field contains the additional fields related to billers in an array format. If there is no any additional info, it will be null. 
      </td>
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
      "operatorsInfo":[
         {
            "operatorCode":"<operator_code_1>",
            "operatorName":"<operator_name_1>",
            "fixedBill":"<True/False>"
         },
         {
            "operatorCode":"<operator_code_2>",
            "operatorName":"<operator_name_2>",
            "fixedBill":"<True/False>"
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
      "type":"operator_list",
      "message":"operator_fetch_request_failed",
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