---
title: '[Backup]Collect Payment API - Server-to-Server'
excerpt: ''
api:
  file: payu-api-16.json
  operationId: CollectPaymentAPI-S2S
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The S2S Integration used for the following:

- Classic Integration
- Direct authorization for pre-authenticated transactions (external MPI/3DSS)
- Decoupled flow for cards involves the following steps for the redirect experience

For more information, refer to [Server-to-Server Integration](doc:server-to-server-integration)

### Environment

| Test Environment       | <https://test.payu.in/_payment>   |
| :--------------------- | :-------------------------------- |
| Production Environment | <https://secure.payu.in/_payment> |

## Reference Information for Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for **\\_payment** API is:  \nsha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)  \nFor more information about the hash generation process, refer to [Encryption of Request.](/docs/hashing-request-and-response)"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Response Parameters

For the response parameters, refer to [Additional Info for Payment APIs](ref:backup-of-payment-apis)

## Request Parameters