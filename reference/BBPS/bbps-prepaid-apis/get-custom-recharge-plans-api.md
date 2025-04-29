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
> This API requires an access token using the Get Token API with the scope as **read\_plans**. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```curl
curl --location --request GET 'https://payu-nbc/v2/nbc/getCustomizedRechargePlans?agentId={agentId}&circleId={circleId}&mobileNo={mobileNumber}&operatorId={operatorId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
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
        This field contains the following set of values for each circle in a JSON array format:

        * **planName**: This field contains the plan name.
        * **price**: This field contains the plan price.
        * **validity**: This field contains the validity period of the plan.
        * **talkTime**: This field contains the talk time for the plan.
        * **validityDescription**: This field contains the validity description.
        * **packageDescription**: This field contains the package description.
        * **planType**: This field contains the plan type.
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
        This field contains the value as **mobile\_plans** for this API.
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
        This field contains the message type as **mobile\_plans\_fetch\_failed.** for this API.
      </td>
    </tr>
    <tr>
      <td>
        additionalParams
      </td>
      <td>
        For failure scenarios, this field contains the additional fields related to billers in an array format. If there is no additional info, it will be null.
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
      "Key3": "value3"
   }
}
```

</details>

## Request parameters