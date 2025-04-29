---
title: UPI Collection - S2S
excerpt: ''
api:
  file: merchant-hosted-36.json
  operationId: S2S-UPICollection
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: upi-collection-s2s
      title: UPI Collection S2S Integration
---
This section provides the request and response parameters used in Step 1 of [UPI Collection S2S Integration](doc:upi-collection-s2s). You can get the sample request and response when use the "Try It" experience. For the complete integration steps, refer to [UPI Collection S2S Integration](doc:upi-collection-s2s).

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

For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

## Request parameters

> ❗️ Error handling
> 
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes. 

> 🚧 Values to be used in Test environment
> 
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.