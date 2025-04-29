---
title: '[OLD]PayU Hosted - Pre-Authorize Payment'
excerpt: ''
api:
  file: payment-api-3.json
  operationId: PayUHostedCheckoutwithPre-AuthorizePayment
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **pre_authorize** parameter is used to pre-authorize payments using the PayU Hosted Checkout integration.

## Reference info for request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Reference**",
    "0-0": "key",
    "0-1": "The merchant key provided by PayU while onboarding.  \nFor more information on how to generate the Key and Salt, refer to any of the following:  \n  - **Production**: [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n  - **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for \\_payment API is:  \n`sha512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\||\\||\\||SALT) \n`For more information about the hash generation process, refer to \\~~ Generate Hash\\~~."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Request parameters

> 📘 Reference:
> 
> - Use the card details as follows: cccnum=5123456789012346, ccexpmon=11, ccexpyr=2025, ccvv=123 and OTP =123456 (displayed in Simulator page).
> - For the list of error codes, refer to [Error Codes - Pre-Authorize Payment](ref:error-codes-pre-authorize-payment).