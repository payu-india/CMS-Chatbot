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

<details><summary>Reference information for request parameters</summary>

> 📘 Reference
> 
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)\n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for **\\_payment** API is:  \nsha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)  \nFor more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted)."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
> 
> - email
> - phone
> - address1
> - s2s_client_ip
> - s2s_device_info

</details>

## Response parameters

<details> <summary>Response parameters</summary>

| **Parameter**            | **Description**                                                                                                                                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| metaData                 | `JSON` It is a JSON object containing more information about the response.                                                                                                                                                                                                                  |
| metaData.referenceId     | `String` This is the PayU reference ID which we will be sending to merchant so that they can send us this back in second call.                                                                                                                                                              |
| binData                  | `JSON` This is a JSON object containing information about card number or token number.                                                                                                                                                                                                      |
| binData.pureS2SSupported | `Boolean` The value for this parameter will be returned **false** for REDIRECT.                                                                                                                                                                                                             |
| result                   | `JSON` This is a JSON object containing response of the request and to be used in subsequent steps.                                                                                                                                                                                         |
| result.otpPostUrl        | `String` The parameter will have null value in case of REDIRECT.                                                                                                                                                                                                                            |
| resutl.acsTemplate       | `String` acsTemplate is a **base64 encoded** string. The merchant needs to decode acsTemplate, which is an HTML format with auto submit, which then needs to be shown on the customer’s browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |

</details>

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

> 🚧 Error Handling:
> 
> A list of error_message with corresponding error code and reason for the error is listed in . PayU recommends you to handle these errors when you process the transactions. For more information, refer to [Error Codes for - S2S Link and Pay](ref:error-codes-for-s2s-link-and-pay).