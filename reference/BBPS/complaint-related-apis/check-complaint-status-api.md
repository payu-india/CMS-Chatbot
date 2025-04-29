---
title: Check Complaint Status API
excerpt: ''
api:
  file: bbps-apis-agent-share-3.json
  operationId: CheckComplaintStatus
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Check Complaint Status** API is to check the status of a non-BBPS complaint by passing the ID of the complaint in the request.

<BBPSEnvironment />

<br />

> 📘 Note:
>
> Send the scope of the Get Token API as **check\_complain\_status** to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```curl
curl --location -g --request GET 'https://<hostName>/payu-nbc/v1/nbc/checkComplaintStatus/?&complaintId={{Complaint ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
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
        If the transaction had failed, it will contain:  
        * additional data related to transactions
        * List of errors which caused failure transactions
      </td>
    </tr>
  </tbody>
</Table>

### payload

| **Parameter**    | **Description**                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| refId            | The reference ID against which the complaint was registered.                                                             |
| billerReply      | It will contain the latest updated response provided by the biller.                                                      |
| complaintId      | It is the queried complaint ID.                                                                                          |
| billerId         | Biller ID against which the complaint was registered by the customer.                                                    |
| complaintStatus  | It is updated Status which is provided by PayU. It’s value can be CAPTURED/RESOLVED/ASSIGNED                             |
| additionalParams | For failed transactions, it will contain additional info. If there is no any additional info available, it will be null. |

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```
{  
  "code": 200,  
  "status": "SUCCESS",  
  "payload": {  
    "refId": null,  
    "billerReply": "Not Received any response from biller yet!",  
    "complaintId": "239uu42942",  
    "billerID": "PMCBPAYU014831",  
    "complaintStatus": "CAPTURED"  
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
    "type": "non_bbps_complain_status",
    "message": "complaint_request_failed",
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