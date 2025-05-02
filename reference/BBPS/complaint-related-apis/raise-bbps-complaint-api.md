---
title: Raise BBPS Complaint API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: RaiseBBPSComplaint
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use this API to raise complaints against a specific BBPS transaction.

The complaints can be either of the following:

* When a customer wants to raise a complaint against the biller.
* When a customer wants to raise a complaint against a particular transaction.

|            |                                                                                                                      |
| :--------- | :------------------------------------------------------------------------------------------------------------------- |
| Production | [https://bbps-sb.payu.in/payu-nbc/v1/nbc/](https://bbps-sb.payu.in/payu-nbc/v1/nbc/) |

> 📘 Note:
>
> Send the scope of the Get Token API as **register\_complaint** to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```curl
curl --location 'https://bbps-sb.payu.in/payu-nbc-int/v1/nbc/raiseComplaint' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 2b42b431dc4ecc4c487675b6c71ee1861adc7283194a7af292e0e1d1f8637895' \
--data '{
    "fetchParameters": {
        "complaintType": "Transaction",
        "description": "Service nhi mili",
        "disposition": "Erroneously paid in wrong account",
        "txnReferenceId": "PA024116O40NVIZZ9870"
    },
    "xchangeId": "501"
}'
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
        It will contain a list of biller categories. For more information, refer to the [payload](#payload) table. If the transaction had failed, it will contain:  

        * additional data related to transactions
        * List of errors which caused failure transactions
      </td>
    </tr>
  </tbody>
</Table>

### payload

The payload parameter contains the following fields in an array format:

| **Field**        | **Description**                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------- |
| refId            | In case number 2 ,this is the reference ID against which the complaint is registered. For case-1, it will be null.     |
| complaintStatus  | It will show whether the complaint is registered with PayU or not.                                                      |
| complaintId      | It is a unique complaint id assigned to customers for reference.                                                        |
| additionalParams | For failed transactions, it will contain additional info.If there is no any additional info available, it will be null. |

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```
{
"code": 200,
"status": "SUCCESS",
"payload": {
"responseReason": "SUCCESS",
"openComplaint": "Y/N",
"complaintStatus": "ASSIGNED_TO_COU",
"complaintId": "<15 digit complaint id>",
"msgId": "<message id for the complaint>",
"assigned": "PayU",
"responseCode": "000"
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
        "reason": "<error Message>", 
        "errorCode": "<Error Code>" 
      } 
    ], 
    "refId": "<RefId>", 
    "type": "non_bbps_complain_register", 
    "message": "invalid_complaint_request", 
    "additionalParams": { 
      "Key1": "value1", 
      "Key2": "value2", 
      "Key3": "value3" 
    } 
  } 
} 
```

</details>

## Request parameters

### Complaint DisposItion

| Code | Transaction                                                                            |
| ---- | -------------------------------------------------------------------------------------- |
| 1    | Transaction Successful, account not updated                                            |
| 2    | Transaction Amount deducted, biller account credited but transaction ID not received   |
| 3    | Transaction Amount deducted, biller account not credited & transaction ID not received |
| 4    | Transaction Amount deducted multiple times                                             |
| 5    | Transaction Double payment updated                                                     |
| 6    | Transaction Erroneously paid in wrong account                                          |
| 7    | Transaction Others, provide details in description                                     |