---
title: '[OLD]Collect Payment - Merchant Hosted Checkout'
excerpt: ''
api:
  file: tpv-8.json
  operationId: MerchantHostedCheckout
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To process payments with credit/debit card, UPI, wallet, etc. on your website using PayU, collect the payment details on your website and submit them to PayU via API. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction. 

> 📘 Reference:
> 
> For an example of how to submit a payment request on your website, refer to [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website). To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](doc:handling-the-redirect-urls).

### Environment

| Test Environment       | <https://test.payu.in/_payment>   |
| :--------------------- | :-------------------------------- |
| Production Environment | <https://secure.payu.in/_payment> |

## Reference information for request parameters

For the character limit of each parameter, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#character-limit-for-request-parameters).

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
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

## Response parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

> 🚧 Error Handling:
> 
> A list of error_message with corresponding error code and reason for the error is listed in [Error Codes](ref:error-codes). PayU recommends you to handle these errors when you process the transactions.