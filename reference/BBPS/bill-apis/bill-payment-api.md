---
title: Bill Payment API
excerpt: ''
api:
  file: bbps-apis-agent-share-7.json
  operationId: BillPaymentAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use the **Bill Payment **API to send the payment information to make the bill payment.

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the Get Token API as **create_transactions** to obtain the access_token for this request. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --location --request POST 'https://<hostName>/payu-nbc/v1/nbc/billpaymentrequest?agentId={agentId}&customerParams={customerParams}&deviceDetails={deviceDetails}&paidAmount={paidAmount}&paymentName={paymentName}&refId={refId}&billerId={billerId}&paymentDetails={paymentDetails}&userDetails={userDetails}&isQuickPay={isQuickPay}&timeStamp={timeStamp}&planId={planId}&additionalParams&COUcustConvFee&planDetails&directBillChannel&payByLink&paymentRefID' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
```

</details>

<details><summary>Response parameters<summary>

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "0-0": "code",
    "0-1": "This field contains the global response code and can be any of the following:  \n  \n- **0**: If web service call failed\n- **1**: if web service call succeeded",
    "1-0": "status",
    "1-1": "The status of the API command and can be any of the following:  \n  \n- SUCCESS\n- FAILURE",
    "2-0": "payload",
    "2-1": "It will contain payload which are explained as subsequent parameters.",
    "3-0": "timeStamp",
    "3-1": "This contains the server time stamp when the request or response in initiated.",
    "4-0": "paidAmount",
    "4-1": "This contains the paid amount by customer.",
    "5-0": "refId",
    "5-1": "This contains the reference ID  passed by agent/consumer in payment request.The length of refID should be between 34 to 35.",
    "6-0": "billerId",
    "6-1": "This contains the biller Identification Number passed by agent/consumer in payment request.",
    "7-0": "additionalParams",
    "7-1": "This contains the additional information provided by biller. Keys and Values can be dynamic inside this block except txnRefId and billerReferenceNumber.    \nFor BBPS response:    \n  \n- **txnRefId**: txn Id returned to agent with every payment response if the biller is on BBPS platform. Also it will contain other required information in case of any specific biller. \n- **billerReferenceNumber**: Reference Number is returned by Biller after payment.For Non-BBPS response, t may contain any additional information if required to share with agents  in future.",
    "8-0": "planResponse",
    "8-1": "This contains the details of plans chooses by customer while payment. This field is conditional and BOU will pass if billerResponseType for respective biller is SELECTIVE type.",
    "9-0": "message",
    "9-1": "This parameter is applicable for failure scenarios. It will contain two messages in case of:  \n  \n- **Failure**: payment\\_request\\_failed\n- **Pending**: payment\\_request\\_pending"
  },
  "cols": 2,
  "rows": 10,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

<details><summary>Sample response</summary>

> 📘 Notes:
> 
> - In case of a failure response, if the message is **payment_request_pending**, this transaction should be considered as in progress by the agent. For terminal status, a payment status call is required.   
>   The agent should consider transaction status as pending in case of any exception received from PayU in payment or status API response. 
> - The agent should not override transaction status against the same reference ID in repeated requests. Ideally, each Payment Request should be raised with a unique Ref Id. 
> - As the Bill Payment API is transactional, so to avoid any issue like duplicate RefId, make sure to post a request with a unique reference ID for a payment call. Each call is mandatorily required to be posted with a unique RefId only. Our fetch flow & payment flow go hand in hand with one reference ID. In case of any issue with the Bill Payment API, Bill Payment Transaction Status API must be used.  For more information, refer to Bill Payment Transaction Status API.
> 
> For the following exceptional cases, PayU recommends using the Bill Payment Transaction Status API, which will provide the correct status for payment.  
> 
> - Connection Failure/ Socket Issue  
> - CU is Down
> - Payment Status as Pending
> - Payment Status as Failure with ErrorCode: “BBPSERR001”

### Success scenario

```
{
   "code":200,
   "payload":{
      "timeStamp":"<server timestamp when response was sent>",
      "paidAmount":"<paid amount in double>",
      "refId":"<reference id>",
      "message":"bill paid to biller",
      "billerId":"<biller-Id>",
      "additionalParams":{
         "txnReferenceId":"TYY567UII",
         "<key1>":<value1>,
         "<key2>":<value2>
      }
   },
   "status":"SUCCESS"
}
```

### Failure scenario

- Payment request failed

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
    "type": "payment_response",
    "message": "payment_request_failed",
    "additionalParams": {
      "Key1": "value1",
      "Key2": "value2",
      "Key3": "value3"
    }
  }
}
```

- Payment request pending

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
    "type": "payment_response",
    "message": "payment_request_pending",
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

> 📘 Reference:
> 
> - For the required fields in the **paymentMode** field of the **paymentDetails** JSON object, refer to [Payment Modes  and Required Parameters](ref:payment-modes-and-required-parameters).
> - For bill payment initiating channel and payment modes allowed mapping, refer to [Initiating Channel  vs Payment Modes](ref:initiating-channel-vs-payment-modes).