---
title: Get Payment Status API
excerpt: ''
api:
  file: bbps-apis-agent-share-5.json
  operationId: GetPaymentStatus(V2)
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can use the **Get Payment Status** API to manually request the status of a bill payment transaction. Sometime the response of a **Bill Payment **API can be interrupted due to network failures. To handle such situations you can programmatically use this API to make a manual request.

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the Get Token API as **read_transactions** to obtain the access_token for this request. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details> <summary>Sample request</summary>

```
curl --location -g --request GET 'https://<hostName>/<host name>/v2/nbc/status/billpayment?refId={refId} ' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' 
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
    "2-1": "This parameter contains the bill fetch transaction data. For more information, refer to the [payload](#payload) table."
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

| Field            | Descritpion                                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| refId            | This field contains the reference ID for the queried payment request.                                                                                                                                                                                                                                 |
| txnStatus        | This field contains the status related to requested refId. It will contain status as in the Transaction Status Code table. For more information, refer to [Transaction Status Code](https://devguide.vercel.app/agent-api-integration/bill-apis/bill-payment-transaction-status/#Transaction_Status). |
| requestTimeStamp | This field contains the actual payment requested date time stamp of payment request.                                                                                                                                                                                                                  |
| paidAmount       | This field contains the payment requested amount                                                                                                                                                                                                                                                      |
| billerId         | This field contains the payment requested biller ID.                                                                                                                                                                                                                                                  |
| additionalParams | This field contains the payment related additional params like payment txnRefId.                                                                                                                                                                                                                      |
| planResponse     | This field contains the activated plan information lists returned by Biller. This field is conditional and BOU will pass if billerResponseType for respective biller is SELECTIVE type                                                                                                                |

</details>

<details> <summary>Sample response</summary>

### Success scenario

```
{
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "refId":"<refId>",
      "txnStatus":"PAYMENT_SUCCESS",
      "requestTimeStamp":"<Requested Time stamp>",
      "paidAmount":"<Amount Paid>",
      "billerId":"<billerId>",
      "additionalParams":{
         "txnReferenceId":"<txnRefId>",
         "billerReferenceNumber":"<billerReferenceNumber>",
         "key1":"value2",
         "key2":"value2"
      },
      "planResponse":[
         {
            "planType":"ACTIVATED",
            "key1":"value1",
            "key2":"value2",
            "key3":"value3",
            "key4":"value4",
            "key5":"value5"
         }
      ]
   }
}
```

### Failure scenario

- When the PayU Transaction ID does not exist:

```
{
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "refId":"<refId>",
      "txnStatus":"RECORD_NOT_FOUND",
      "requestTimeStamp":"<Requested Time stamp>",
      "paidAmount":0,
      "billerId":"",
      "additionalParams":{
         "txnReferenceId":""
      }
   }
}
```

- When Payment transaction failed at biller’s end and failure status captured at PayU’s end:

```
{
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "refId":"<refId>",
      "txnStatus":"PAYMENT_FAILURE",
      "requestTimeStamp":"<Requested Time stamp>",
      "paidAmount":"<Amount Paid>",
      "billerId":"<BillerId>",
      "additionalParams":{
         "txnReferenceId":"<txnRefId>"
      }
   }
}
```

- When Payment transaction is not captured at PayU’s end and PayU is also waiting for the actual status of the transaction:

```
{
   "code":200,
   "status":"SUCCESS",
   "payload":{
      "refId":"<refId>",
      "txnStatus":"PAYMENT_PENDING",
      "requestTimeStamp":"<Requested Time stamp>",
      "paidAmount":"<amount paid>",
      "billerId":"<billerId>",
      "additionalParams":{
         "txnReferenceId":"<txnRefId>"
      }
   }
}
```

</details>

## Request parameters