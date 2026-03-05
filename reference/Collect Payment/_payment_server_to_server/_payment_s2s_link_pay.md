---
title: Collect Payment API - S2S Link and Pay
excerpt: ''
api:
  file: payu-api-23.json
  operationId: CollectPaymentAPI-S2SLinkandPay
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collection payments with BNPL using Link and Pay. This section provides the request and response parameters and you can get the sample request and response when use the "Try It" experience. For more information on integration, refer to [Collect Payments with BNPL using Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay)

<PaymentAPIEnvironment />

<Accordion title="Sample request" icon="fa-info-circle">
  ```curl
curl --request POST \
     --url https://test.payu.in/_payment \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data key=JPM7Fg \
     --data pg=BNPL \
     --data txn_s2s_flow=4 \
     --data LinkAndPayFlowType=1 \
     --data LinkAndPayFlowDetails=1 \
     --data txnid=951bccfde0ac54f75612 \
     --data amount=2 \
     --data productinfo=Product Info \
     --data firstname=Ashish \
     --data email=test@example.com \
     --data phone=9123412345 \
     --data surl=https://apiplayground-response.herokuapp.com/ \
     --data furl=https://apiplayground-response.herokuapp.com/ \
     --data hash=02647d079d45737aede205a5bf0060ffcf32b5104facebaf901b479b958d80a0e0e88c9edd4f5c9a0576c7bc1688cce15957759029a0e58f5699b8a696c98d10 \
     --data user_credentials=abc:xyz
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-info-circle">
> 📘 Notes:
  >
  > There will be different scenarios and the response according to different scenarios:
  >
  > * **Repeat User Flow**: If the customer’s account is linked and auto-debit is success:
  > * **Repeat User Flow**: If the customer’s account is linked and auto debit fails (eg. Customer not eligible, Failed at Payment Option’s end)
  > * **First Time User Flow**: If customer is eligible, but is not linked: This is the registration flow, where a first-time user is paying on a merchant with the specific payment option
**Sucesss Scenario**
  ```json
{
  "metaData": {
    "message": "No Error",
    "referenceId": "748e033af87f1bb7b6aefd405bec9473",
    "statusCode": "E000",
    "txnId": "951bccfde0ac54f75612",
    "unmappedStatus": "success",
    "submitOtp": {
      "status": "success"
    }
  },
  "result": {
    "link_and_pay": {
      "customerLinked": "true",
      "payuToken": "token12345"
    },
    "mihpayid": "18828133385",
    "mode": "BNPL",
    "status": "success",
    "key": "smsplus",
    "txnid": "951bccfde0ac54f75612",
    "amount": "2.00",
    "addedon": "2023-12-27 18:13:41",
    "productinfo": "Product Info",
    "firstname": "Ashish",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "test@example.com",
    "phone": "9123412345",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "card_token": "",
    "card_no": "",
    "field0": "",
    "field1": "9582567614",
    "field2": "EMI1014338639070843702",
    "field3": "Transaction is successful",
    "field4": "bnpl",
    "field5": "VFhOMzk2MjA3ODY2",
    "field6": "TXN396207866",
    "field7": "PAYMENT_SUCCESSFUL",
    "field8": "SUCCESS",
    "field9": "Transaction is successful",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "BNPL-PG",
    "error": "E000",
    "error_Message": "No Error",
    "net_amount_debit": "2.07",
    "discount": "0.00",
    "offer_key": "",
    "offer_availed": "",
    "additionalCharges": "0.07",
    "unmappedstatus": "captured",
    "hash": "3a7742e5d9284e4f43d349bf1a5ff04353a099920ced98330fab15728841b6c772f00f83163c491d8954ead0c9a1dee7af94d67ddc539ff6cb2d0246baed8148",
    "bank_ref_no": "TXN396207866",
    "bank_ref_num": "TXN396207866",
    "bankcode": "LAZYPAY",
    "surl": "https://admin.payu.in/test_response",
    "curl": "https://admin.payu.in/test_response",
    "furl": "https://admin.payu.in/test_response"
  }
}
  ```
  **Failure scenario**
  * Repeat User Flow: Auto-debit Failed

  ```json
  {
    "metaData": {
      "message": "The customer is not eligible for this transaction",
      "referenceId": "423fe9bfebdb2f92b8ae95a125aff397",
      "statusCode": "E2401",
      "txnId": "4223974b64f88ab4e3a1",
      "txnStatus": "failed",
      "unmappedStatus": "failure"
    },
    "result": {
      "link_and_pay": {
        "customerLinked": "true",
        "payuToken": "token12345"
      }
    }
  }
  ```

  * Failed at Payment option’s end

  ```json
  {
    "metaData": {
      "message": "Transaction Failed at bank end.",
      "referenceId": "ea68a970115a9d87c6ece8d0218e6c2a",
      "statusCode": "E308",
      "txnId": "54d2d883f8e4a3fff6ba",
      "txnStatus": "failed",
      "unmappedStatus": "failure"
    },
    "result": {
      "link_and_pay": {
        "customerLinked": "true",
        "payuToken": "token12345" // can be null or "" <empty string>
      }
    }
  }
  ```




 
</Accordion>

<Additional_paymentRequestParams />

<br />

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter**            | **Description**                                                                                                                                                                                                                                                                             |
  | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | metaData                 | `JSON` It is a JSON object containing more information about the response.                                                                                                                                                                                                                  |
  | metaData.referenceId     | `String` This is the PayU reference ID which we will be sending to merchant so that they can send us this back in second call.                                                                                                                                                              |
  | binData                  | `JSON` This is a JSON object containing information about card number or token number.                                                                                                                                                                                                      |
  | binData.pureS2SSupported | `Boolean` The value for this parameter will be returned **false** for REDIRECT.                                                                                                                                                                                                             |
  | result                   | `JSON` This is a JSON object containing response of the request and to be used in subsequent steps.                                                                                                                                                                                         |
  | result.otpPostUrl        | `String` The parameter will have null value in case of REDIRECT.                                                                                                                                                                                                                            |
  | result.acsTemplate       | `String` acsTemplate is a **base64 encoded** string. The merchant needs to decode acsTemplate, which is an HTML format with auto submit, which then needs to be shown on the customer's browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |

  For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Accordion>

## Request parameters

> 🚧 Error Handling:
>
> A list of error_message with corresponding error code and reason for the error is listed in . PayU recommends you to handle these errors when you process the transactions. For more information, refer to [Error Codes for - S2S Link and Pay](ref:error-codes-for-s2s-link-and-pay).
