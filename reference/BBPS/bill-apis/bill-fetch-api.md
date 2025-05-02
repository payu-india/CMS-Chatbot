---
title: Bill Fetch API
excerpt: ''
api:
  file: bbps-apis-agent-share-4.json
  operationId: BillFetchAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Bill Fetch** API will fetch data from the biller and provide responses with pending amounts and other useful information.

|            |                                                                                                          |
| :--------- | :------------------------------------------------------------------------------------------------------- |
| Production | https://bbps-sb.payu.in/payu-nbc/v1/nbc/billfetchrequest|

> 📘 Note:
>
> Send the scope of the Get Token API as **read\_billers** to obtain the access\_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details>
  <summary>Sample request</summary>

```
curl --location --request POST 'https://<hostName>/payu-nbc/v1/nbc/billfetchrequest?agentId=`{agentId}`&billerId=`{billerId}`&customerName=`{customerName}`&customerPhoneNumber=`{customerPhoneNumber}`&timeStamp=`{timestamp in yyyy-MM-dd HH:mm:ss}`&refId=`{Reference Id}`&customerParams={
"<paramName>": "<paramValue>"
}&deviceDetails={
    "INITIATING_CHANNEL": "INT/MOB",
    "IP": "xx.xx.xx.xx",
    "MAC": "xx.xxx.xxx.xx”}
 \
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
        This field contains the global response code and can be any of the following:  

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

        * **SUCCESS**
        * **FAILURE**
      </td>
    </tr>

    <tr>
      <td>
        payload
      </td>

      <td>
        This parameter contains the bill fetch transaction data.
      </td>
    </tr>

    <tr>
      <td>
        refId
      </td>

      <td>
        This parameter contains the Reference Identification Number. The length of refID will be between 34 to 35.
      </td>
    </tr>

    <tr>
      <td>
        timeStamp
      </td>

      <td>
        This parameter contains the current time stamp of the server.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter contains the amount to be paid.
      </td>
    </tr>

    <tr>
      <td>
        accountHolderName
      </td>

      <td>
        This parameter contains the account holder name as on the bill.
      </td>
    </tr>

    <tr>
      <td>
        dueDate
      </td>

      <td>
        This parameter contains the due date of the bill.
      </td>
    </tr>

    <tr>
      <td>
        billDate
      </td>

      <td>
        This parameter contains the billing date of bill.
      </td>
    </tr>

    <tr>
      <td>
        billerId
      </td>

      <td>
        This parameter contains the biller Identification ID that is unique number for each customer given by the operator.
      </td>
    </tr>

    <tr>
      <td>
        amountDetails
      </td>

      <td>
        This parameter contains breakup details of total payable amount. (this details may not be available).
      </td>
    </tr>

    <tr>
      <td>
        billNumber
      </td>

      <td>
        Unique identifier of the bill.
      </td>
    </tr>

    <tr>
      <td>
        billPeriod
      </td>

      <td>
        Billing period of the bill. Most possible values are as mentioned below.
      </td>
    </tr>

    <tr>
      <td>
        additionalParams
      </td>

      <td>
        This parameter contains the additional information if any available from the biller side for both BBPS and Non BBPS billers.\
        For example, if there is any additional information like early payment fee, late payment fee, early payment date ,late payment due date, DTC code etc. has been mentioned in any biller MDM, additional parameters will contain those values as in key value pairs:\
        ```
        "additionalParams":{  
        "Early Pay Date":" \< date1 > ",  
        "Early Payment Fee":" \< fee1 > ",  
        "Late Payment Date":" \< date2 > ",  
        "Late Payment Fee":"",  
        "DTC code":" \< code > ",  
        "Base Bill Amount":""  
        }
        ```
        Similarly, in case of Non BBPS biller wants to share any additional information, it will be sent to agent in additional parameters itself.
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
  "code": 200,
  "status": "SUCCESS",
  "payload": {
    "refId": "<reference ID>",
    "timeStamp": "<yyyy-MM-dd hh:mm:ss>",
    "amount": "<amount to be paid>",
    "accountHolderName": "<account customer name>",
    "dueDate": "<yyyy-MM-dd>",
    "billDate": "<yyyy-MM-dd>",
    "billerId": "<Biller-Id>",
    "amountDetails": [
      {
        "<paramName>": "<paramNameValue>"
      }
    ],
    "additionalParams": {
      "Key1": "value1",
      "Key2": "value2",
      "Key3": "value3"
    },
    "billNumber":"<billNumber>",
    "billPeriod":"<Period of bill>",
    "approvalRefNum":"<bbps biller approval Ref Number>"
  }
}
```

### Failure scenario

```
{
  "code": 600,
  "status": "failure",
  "payload": {
    "errors": [
      {
        "reason": "<Error Message>",
        "errorCode": "<Error Code>"
      }
    ],
    "refId": "<referenceID>",
    "type": "fetch",
    "message": "fetch_request_failed",
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