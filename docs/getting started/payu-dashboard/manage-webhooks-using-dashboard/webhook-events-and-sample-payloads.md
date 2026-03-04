---
title: Webhook Events and Sample Payloads
excerpt: List of webhook events along with sample payloads.
deprecated: false
hidden: false
metadata:
  robots: index
---
You can accept customer payments using PayU products. By subscribing to payments webhook events you can get notified about payment state changes.

## List of Webhook Events

The table below lists the available webhook events.

| **Event Name** | **Event Type** | **Description**                                   |
| :------------- | :------------- | :------------------------------------------------ |
| `Successful`   | `Payment`      | Triggered when a payment is successful.           |
| `Failed`       | `Payment`      | Triggered when a payment is failed.               |
| `Refund`       | `Payment`      | Triggered when a payment refund is successful.    |
| `Dispute`      | `Payment`      | Triggered when a dispute is raised for a payment. |

## Sample Payloads

Given below are the sample payloads for webhook events.

### Payment Successful

```json
{
  "timestamp":"2026-02-26 11:35:25.000000",
  "request_identifier":"27455843883",
  "event_type":"payment",
  "status":"Success",
  "webhook_delivery_message":null,
  "http_method":"POST",
  "endpoint":"https://partnerapilayer.payu.in/apilayer/partner/paymentCallback",
  "response_code":200,
  "response_body":"",
  "endpoint_latency":1085,
  "event_payload":{
    "country":"",
    "curl":"https://api.payu.in/partner/paymentCancelled",
    "udf10":"",
    "discount":"0.00",
    "offer_key":"",
    "error_Message":"The Bank servers are unreachable over the network",
    "state":"",
    "payment_source":"payuPureS2S",
    "txnid":"25841132755570991",
    "surl":"https://api.payu.in/partner/paymentSuccess",
    "net_amount_debit":"0",
    "lastname":"",
    "zipcode":"",
    "offer_availed":"",
    "phone":"918921784385",
    "pa_name":"Camspay",
    "productinfo":"25841132755570991",
    "hash":"bd4b8272f8a2d3b57a42f4c444642ef9c7c965e41378264f1d94645e386b4c22f4bf810d1020e38586b3e44d3197154be136f467821a166a5119af7d042d426c",
    "status":"pending",
    "firstname":"",
    "city":"",
    "authenticaticationMethod":"",
    "error":"E214",
    "bank_ref_no":"",
    "addedon":"2026-02-26 11:12:25",
    "udf9":"",
    "udf7":"",
    "udf8":"",
    "bank_ref_num":"",
    "key":"rM5M43",
    "email":"",
    "amount":"1.00",
    "unmappedstatus":"in progress",
    "address2":"",
    "address1":"",
    "udf5":"whatsapp",
    "mihpayid":"27455843883",
    "udf6":"",
    "udf3":"",
    "udf4":"",
    "udf1":"",
    "udf2":"",
    "field1":"",
    "field0":"",
    "field7":"VERNEGATIVE",
    "field6":"",
    "furl":"https://api.payu.in/partner/paymentFailed",
    "field9":"HTTP/1.1 500 Internal Server Error",
    "field8":"Verification | failed | Transaction failed at bank end",
    "field3":"",
    "field2":"",
    "field5":"",
    "PG_TYPE":"UPI-PG",
    "field4":""
  }
}
```

### Payment Failed

```json
{
  "timestamp":"2026-02-27 14:24:45.000000",
  "request_identifier":"27472524682",
  "event_type":"payment",
  "status":"Failed",
  "webhook_delivery_message":"HTTP/2 405 ",
  "http_method":"POST",
  "endpoint":"https://payu.in",
  "response_code":405,
  "response_body":"<html>\r\n<head><title>405 Not Allowed</title></head>\r\n<body>\r\n<center><h1>405 Not Allowed</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n",
  "endpoint_latency":7,
  "event_payload":{
    "country":"",
    "curl":"https://admin.payu.in/test_response",
    "udf10":"",
    "discount":"0.00",
    "offer_key":"",
    "error_Message":"Bank failed to authenticate the customer",
    "state":"",
    "payment_source":"payu",
    "txnid":"5e2e5eb03a45f13a8bdb",
    "surl":"https://admin.payu.in/test_response",
    "net_amount_debit":"0",
    "lastname":"",
    "zipcode":"",
    "offer_availed":"",
    "additionalCharges":"0.03",
    "phone":"1234567890",
    "pa_name":"PayU",
    "productinfo":"Product Info",
    "hash":"5aa580a257fc7f7acd8350db00142360d385b105d6b1aa1cb4bb9e14a945fc0bd84afecba321561485046a46d009581c77ec4d184cdf02d134a9c6e41b398817",
    "status":"failure",
    "firstname":"Payu-Admin",
    "city":"",
    "authenticaticationMethod":"",
    "error":"E500",
    "bank_ref_no":"",
    "addedon":"2026-02-27 14:24:42",
    "udf9":"",
    "udf7":"",
    "udf8":"",
    "bank_ref_num":"",
    "key":"rM5M43",
    "email":"test@example.com",
    "amount":"1.00",
    "unmappedstatus":"failed",
    "address2":"",
    "address1":"",
    "udf5":"",
    "mihpayid":"27472524682",
    "udf6":"",
    "udf3":"",
    "udf4":"",
    "udf1":"",
    "udf2":"",
    "field1":"",
    "field0":"",
    "field7":"AUCNEGATIVE",
    "field6":"",
    "furl":"https://admin.payu.in/test_response",
    "field9":"UNKNOWN",
    "field8":"Message Received Invalid",
    "field3":"",
    "field2":"",
    "field5":"",
    "PG_TYPE":"DC-PG",
    "field4":""
  }
}
```

#### Event Payload Parameter Description

<Accordion title="Parameters and Description" icon="fa-table">
  | Parameters               | Description                                                                                                                                                                                                                                                     |
  | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | mihpayid                 | Unique transaction ID assigned by PayU for each transaction. Use for inquiry or refund.                                                                                                                                                                         |
  | key                      | Merchant key identifying the merchant's PayU account; same as in the transaction request.                                                                                                                                                                       |
  | txnid                    | Transaction ID (Order ID) that was sent by the merchant in the transaction request.                                                                                                                                                                             |
  | amount                   | Original payment amount sent in the transaction request by the merchant.                                                                                                                                                                                        |
  | productinfo              | Product description sent in the transaction request.                                                                                                                                                                                                            |
  | firstname                | Customer first name as sent in the transaction request.                                                                                                                                                                                                         |
  | lastname                 | Customer last name as sent in the transaction request.                                                                                                                                                                                                          |
  | email                    | Customer email as sent in the transaction request.                                                                                                                                                                                                              |
  | phone                    | Customer phone number as sent in the transaction request.                                                                                                                                                                                                       |
  | address1                 | Customer address line 1 (from request).                                                                                                                                                                                                                         |
  | address2                 | Customer address line 2 (from request).                                                                                                                                                                                                                         |
  | city                     | Customer city (from request).                                                                                                                                                                                                                                   |
  | state                    | Customer state (from request).                                                                                                                                                                                                                                  |
  | country                  | Customer country (from request).                                                                                                                                                                                                                                |
  | zipcode                  | Customer zip/postal code (from request).                                                                                                                                                                                                                        |
  | udf1 – udf10             | User-defined fields (udf1–udf5 documented; udf6–udf10 in response). Same values as sent in the transaction request. Character limit 255 for udf1–udf5.                                                                                                          |
  | hash                     | Hash calculated by PayU. Merchant must verify it before marking the transaction success/failure to ensure integrity. See [Generate Hash](doc:generate-hash-merchant-hosted).                                                                                    |
  | status                   | Outcome of the transaction: `success`, `failure`, or `pending`. Treat only `success` as successful.                                                                                                                                                             |
  | error                    | Error code indicating the reason for failure (e.g. E500). Failure reasons vary by bank.                                                                                                                                                                         |
  | error\_Message           | Human-readable error message. Refer to [Error Codes](ref:error-codes) for the list.                                                                                                                                                                             |
  | PG\_TYPE                 | Payment gateway type used for the transaction (e.g. `CC-PG` for credit card, `DC-PG` for debit card, `UPI-PG`, `CASH-PG`, `EMI-PG`, `BNPL-PG`, `QR-PG`).                                                                                                        |
  | bank\_ref\_num           | For successful transactions, the bank reference number generated by the bank.                                                                                                                                                                                   |
  | bank\_ref\_no            | Same as bank\_ref\_num; alternate parameter name for bank reference number.                                                                                                                                                                                     |
  | unmappedstatus           | Transaction status in PayU’s internal system; can include intermediate states. Values include: dropped, bounced, captured, auth, failed, usercancelled, pending. See [Payment State Explanations](ref:payment-state-explanations).                              |
  | surl                     | Success URL – URL on which PayU redirects when the transaction is successful.                                                                                                                                                                                   |
  | furl                     | Failure URL – URL on which PayU redirects when the transaction fails.                                                                                                                                                                                           |
  | curl                     | Cancel URL – URL used when the user cancels (character limit 50 in request).                                                                                                                                                                                    |
  | addedon                  | Date and time when the transaction was recorded (e.g. `2026-02-27 14:24:42`).                                                                                                                                                                                   |
  | discount                 | Discount amount applied (e.g. `0.00`).                                                                                                                                                                                                                          |
  | net\_amount\_debit       | Net amount debited from the customer.                                                                                                                                                                                                                           |
  | additionalCharges        | Additional charges applied (e.g. convenience fee).                                                                                                                                                                                                              |
  | payment\_source          | Source of the payment (e.g. `payu`).                                                                                                                                                                                                                            |
  | pa\_name                 | Name of the payment aggregator through which the transaction was routed (e.g. PayU, RazorPay). Shown when using Maximiser / other aggregators.                                                                                                                  |
  | offer\_key               | Key of the offer applied, if any.                                                                                                                                                                                                                               |
  | offer\_availed           | Indicates whether an offer was availed.                                                                                                                                                                                                                         |
  | authenticaticationMethod | Authentication method used (e.g. 3DS). Note: name may appear with typo in payload.                                                                                                                                                                              |
  | field0 – field9          | Gateway- or flow-specific fields. Content varies by payment mode and outcome (e.g. bank reference, RRN, auth result, status message). For cards, field7/field8/field9 often carry auth result or message (e.g. AUCNEGATIVE, UNKNOWN, Message Received Invalid). |
</Accordion>

### Refund Successful

```json
{
  "additionalValue1":null,
  "bank_arn":308239782136,
  "refund_mode":"Instant Credit through UPI",
  "bank_ref_num":"308239782136",
  "key":"lF76TH",
  "amt":"149.00",
  "remark":null,
  "status":"success",
  "token":"DG0036362",
  "mihpayid":"17025521702",
  "request_id":"11865427756",
  "merchantTxnId":"ORDER_33172661_1679394745",
  "additionalValue2":null,
  "action":"refund"
}
```

### Refund Failure

```json
{
  "additionalValue1": null,
  "bank_arn": null,
  "refund_mode": "Instant Credit through UPI",
  "bank_ref_num": "100142082006",
  "key": "IahMJL",
  "amt": "72.00",
  "remark": null,
  "status": "failure",
  "token": "PZT2506150013OR4AN33",
  "mihpayid": " 23907365951 ",
  "request_id": "17265314530",
  "merchantTxnId": "PZT2506150013OR4AN02",
  "additionalValue2": null,
  "action": "refund"
}
```

#### Payload Parameters

<Accordion title="Parameters and Description" icon="fa-table">
  | Parameter        | Description                                                               | Source Data                      |
  | ---------------- | ------------------------------------------------------------------------- | -------------------------------- |
  | merchantTxnId    | `String` Merchant Sale transaction id `Character Limit: 50`               |                                  |
  | mihpayid         | `String` payuid `Character Limit: max 255 chars`                          | Var1 for refund initiate API     |
  | bank\_arn        | `String` Reference number for refund tracking `Character Limit: 45`       |                                  |
  | bank\_ref\_num   | `String` Bank reference number `Character Limit: 255`                     |                                  |
  | request\_id      | `String` Unique refund id generated by payu `Character Limit:  255`       |                                  |
  | token            | `String` Unique refund txn id provided by merchant `Character Limit:  23` | Var2 for refund initiate API     |
  | action           | `String` refund `Character Limit: 32`                                     |                                  |
  | amt              | `String` Refund amount `Character Limit: 65`                              | Var3 for refund initiate API     |
  | status           | `String` Status of the refund `Character Limit: 32`                       | Possible values: success/failure |
  | additionalValue1 | For future scope                                                          |                                  |
  | additionalValue2 |                                                                           |                                  |
  | key              | `String` Merchant key `Character Limit: 20 `                              |                                  |
</Accordion>
