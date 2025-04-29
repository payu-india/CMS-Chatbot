---
title: Get Operator and Circle By Mobile Number API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: GetOperatorandCircleByMobileNumber(MNP)
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get Prepaid Recharge Plans** API for getting prepaid plans. It will provide all the available prepaid recharge plans available for a given agent ID, circle ID and operator ID.

<BBPSEnvironment />

> 📘 Note:
>
> This API requires an access token using the Get Token API with the scope as **read\_operator\_circle**. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```curl
curl --location --request GET 'https://payu-nbc/v2/nbc/getOperatorAndCircleInfo?agentId=`{agentId}`&mobileNumber=`{mobileNumber}`' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer &lt;token&gt;'
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

The **payload** parameter contains the values in a JSON format are described in the following table:

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

        * **operatorAndCircleInfo** : contains information regarding operator & circle details like operator code, operator name, and circle reference ID of the customer’s mobile number entered as an input.
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
        This field contains the value as **operator\_circle\_fetch** for this API.
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
      "operatorName":"OPERATOR_1",
      "operatorId":"OPERATOR_ID_1",
      "plansInfo":[
         {
            "planName":"&lt;plan_name_1&gt;",
            "price":"&lt;plan_price_1&gt;",
            "validity":"&lt;validity_1&gt;",
            "talkTime":"&lt;talk_time_1&gt;",
            "packageDescription":"&lt;description_1&gt;",
            "planType":"&lt;plan_type&gt;"
         },
         {
            "planName":"&lt;plan_name_1&gt;",
            "price":"&lt;plan_price_1&gt;",
            "validity":"&lt;validity_1&gt;",
            "talkTime":"&lt;talk_time_1&gt;",
            "packageDescription":"&lt;description_1&gt;",
            "planType":"&lt;plan_type&gt;"
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
            "reason":"&lt;error Message&gt;",
            "errorCode":"&lt;Error Code&gt;"
         }
      ],
      "refId":null,
      "type":"mobile_plans",
      "message":"mobile_plans_fetch_failed",
      "additionalParams":{
         "Key": "value1", 
         "Key2": "value2", 
         "Key3": "value3"
       }
    }
}
```

</details>

## Request parameters