---
title: Biller Plans API
excerpt: ''
api:
  file: bbps-apis-agent-share-5.json
  operationId: BillerPlansAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Biller Plans** API to fetch the plans for a biller.

`<BBPSEnvironment />`

> 📘 Note:
> 
> Send the scope of the Get Token API as **read_plans** to obtain the access_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<br />

<details>
  <summary>Sample request</summary>

```
curl --location -g --request POST 'https://<hostName>/payu-nbc/v1/nbc/billerPlans?agentId=`{AGENT_ID}`&billerId=`{BILLER_ID}`&refId=`{UNIQUE_REF_ID}`&searchByTime=`{searchByTime}`&offset=`{offset}`&flowType=`{NON-BBPS/BBPS}`&limi={100}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

</details>

<details>
  <summary>Response parameters</summary>

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field Name</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the global response code and can be any of the following:  </p>
<ul>
<li><strong>0</strong>: If web service call failed</li>
<li><strong>1</strong>: if web service call succeeded</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The status of the API command and can be any of the following:  </p>
<ul>
<li><strong>SUCCESS</strong></li>
<li><strong>FAILURE</strong></li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payload</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the bill fetch transaction data. Ror more information, refer to the <a href="#payload">payload</a> table.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### payload

| Parameter           | Description                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **BBPS Flow**       |                                                                                                                                          |
| planId              | This field contains a unique plan iD received from Biller.                                                                               |
| billerId            | This field contains the biller identification number.                                                                                    |
| category            | This field contains the category of plan.                                                                                                |
| subCategory         | This field contains the sub category of plan.                                                                                            |
| planDescription     | This field contains the description of plan.                                                                                             |
| effctvFrom          | This field contains the plan effective from (usable as identification that plan is active to inactive).                                  |
| effctvTo            | This field contains the plan effective to (usable as identification that plan is active to inactive).                                    |
| status              | This field contains the indicator of plan status.                                                                                        |
| **Non-BBPS Flow**   |                                                                                                                                          |
| planName            | For Non-BBBPS flow, this field contains the plan name received from biller.                                                              |
| price               | For Non-BBBPS flow, this field contains the price of plan.                                                                               |
| validity            | For Non-BBBPS flow, this field contains the validity of plan.                                                                            |
| talkTime            | For Non-BBBPS flow, this field contains the talk time of plan.                                                                           |
| validityDescription | For Non-BBBPS flow, this field contains the validity description of plan.                                                                |
| packageDescription  | For Non-BBBPS flow, this field contains the package description of plan.                                                                 |
| additionalParams    | For failure scenarios, this parameter will contain additional info.If there is not any additional info available than it will be null.   |

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

- BBPS flow:

```
{
  "code": 200,
  "status": "SUCCESS",
  "payload": [
    {
      "planId": "UNIQUE_ID_FOR_PLAN",
      "billerId": "<BILLER_ID>",
      "category": "<PLAN_CATEGORY>",
      "subCategory": "<PLAN_SUB_CAT>",
      "amountInRupees": "<PLAN_Amount_In_Rupees>",
      "planDescription": "<PLAN_DESC>",
      "effctvFrom": "yyyy-MM-dd",
      "effctvTo": "yyyy-MM-dd",
      "status": "ACTIVE/DEACTIVATED",
      "additionalInfo": {
        "<KEY1>": "<VALUE1>",
        "<KEY2>": "<VALUE2>",
        "<KEY3>": "<VALUE3>",
        "<KEY4>": "<VALUE4>",
        "<KEY5>": "<VALUE5>"
      }
    }
  ]
}
```

- For non-BBPS flow:

```
{
  "code": 200,
  "status": "SUCCESS",
  "payload": [
    {
      "planName": "ALPHANUMERIC",
      "price": "254.9",
      "validity": "20 days",
      "talkTime": "ALPHANUMERIC",
      "validityDescription": "ALPHANUMERIC",
      "packageDescription": "ALPHANUMERIC"
    }
  ]
}
```

### Failure scenario

```
{
  "code": 600,
  "status": "Failure",
  "payload": null,
  "errors": [
    {
      "reason": "<error Message>",
      "errorCode": "<Error Code>"
    }
  ],
  "refId": "<refId>",
  "type": "biller_plans",
  "message": "biller_plans_fetch_failed",
  "additionalParams": {
    "Key1": "value1",
    "Key2": "value2",
    "Key3": "value3"
  }
}
```

</details>