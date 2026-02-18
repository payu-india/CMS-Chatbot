---
title: '[Not Supported]Collect Payment API - S2S Link and Pay'
excerpt: ''
api:
  file: payu-api-23.json
  operationId: CollectPaymentAPI-S2SLinkandPay
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collection payments with BNPL using Link and Pay. This section provides the request and response parameters and you can get the sample request and response when use the "Try It" experience. For more information on integration, refer to [Collect Payments with BNPL using Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay)

<PaymentAPIEnvironment />

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
> A list of error\_message with corresponding error code and reason for the error is listed in . PayU recommends you to handle these errors when you process the transactions. For more information, refer to [Error Codes for - S2S Link and Pay](ref:error-codes-for-s2s-link-and-pay).