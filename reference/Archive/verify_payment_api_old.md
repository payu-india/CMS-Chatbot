---
title: '[OLD] Verify Payment API'
excerpt: ''
api:
  file: general-22.json
  operationId: verifypayment
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Verify Payment (**verify_payment**) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU’s database after you receive the response, where var1 is your transaction ID.

## Reference information for request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \nsha512(key|command|var1|salt) sha512"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Environment

| Test Environment       | <https://test.payu.in/merchant/postservice?form=2> |
| :--------------------- | :------------------------------------------------- |
| Production Environment | <https://info.payu.in/merchant/postservice?form=2> |

## Response parameters

For the response parameters, refer to [Additional Info for General APIs](/reference/addl-info-general-apis#response-parameters-for-verify-payment-api).

To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes). 

## Request parameters

**Sample values**

Use the following sample values while trying out the API:

- `var1` (your transaction ID/order ID): 7fa6c4783a363b3da573