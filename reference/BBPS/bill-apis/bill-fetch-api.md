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
The **Bill Fetch ** API will fetch data from the biller and provide responses with pending amounts and other useful information.

<BBPSEnvironment />

<br />

> 📘 Note:
> 
> Send the scope of the Get Token API as **read_billers** to obtain the access_token for this request. For more information, refer to [Get Token API - BBPS](ref:get-token-api-bbps).

<details> <summary>Sample request</summary>

```
curl --location --request POST 'https://<hostName>/payu-nbc/v1/nbc/billfetchrequest?agentId={agentId}&billerId={billerId}&customerName={customerName}&customerPhoneNumber={customerPhoneNumber}&timeStamp={timestamp in yyyy-MM-dd HH:mm:ss>}&refId={Reference Id}&customerParams={
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

<details> <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Field Name**",
    "h-1": "**Description**",
    "0-0": "code",
    "0-1": "This field contains the global response code and can be any of the following:  \n  \n- **0**: If web service call failed\n- **1**: if web service call succeeded",
    "1-0": "status",
    "1-1": "The status of the API command and can be any of the following:  \n  \n- **SUCCESS**\n- **FAILURE**",
    "2-0": "payload",
    "2-1": "This parameter contains the bill fetch transaction data.",
    "3-0": "refId",
    "3-1": "This parameter contains the Reference Identification Number. The length of refID will be between 34 to 35.",
    "4-0": "timeStamp",
    "4-1": "This parameter contains the current time stamp of the server.",
    "5-0": "amount",
    "5-1": "This parameter contains the amount to be paid.",
    "6-0": "accountHolderName",
    "6-1": "This parameter contains the account holder name as on the bill.",
    "7-0": "dueDate",
    "7-1": "This parameter contains the due date of the bill.",
    "8-0": "billDate",
    "8-1": "This parameter contains the billing date of bill.",
    "9-0": "billerId",
    "9-1": "This parameter contains the biller Identification ID that is unique number for each customer given by the operator.",
    "10-0": "amountDetails",
    "10-1": "This parameter contains breakup details of total payable amount. (this details may not be available).",
    "11-0": "billNumber",
    "11-1": "Unique identifier of the bill.",
    "12-0": "billPeriod",
    "12-1": "Billing period of the bill. Most possible values are as mentioned below.",
    "13-0": "additionalParams",
    "13-1": "This parameter contains the additional information if any available from the biller side for both BBPS and Non BBPS billers.  \nFor example, if there is any additional information like early payment fee, late payment fee, early payment date ,late payment due date, DTC code etc. has been mentioned in any biller MDM, additional parameters will contain those values as in key value pairs:  \n`\"additionalParams\":{  \n\"Early Pay Date\":\" \\< date1 > \",  \n\"Early Payment Fee\":\" \\< fee1 > \",  \n\"Late Payment Date\":\" \\< date2 > \",  \n\"Late Payment Fee\":\"\",  \n\"DTC code\":\" \\< code > \",  \n\"Base Bill Amount\":\"\"  \n}\n`Similarly, in case of Non BBPS biller wants to share any additional information, it will be sent to agent in additional parameters itself."
  },
  "cols": 2,
  "rows": 14,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

<details> <summary>Sample response</summary>

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