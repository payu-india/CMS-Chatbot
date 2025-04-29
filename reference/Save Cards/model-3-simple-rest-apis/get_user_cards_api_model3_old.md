---
title: Get User Cards API - Model 3
excerpt: ''
api:
  file: storecard.json
  operationId: get_payment_instrument
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Get User Cards **API is used to fetch all the cards corresponding to the user. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

## Response parameters

For the response parameters and sample responses, refer to [Additional Info for Model 3 Parameters](ref:additional-info-for-model-3-parameters).

## Reference info for request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "The merchant key provided by PayU while onboarding.  \nFor more information on how to generate the Key and Salt, refer to any of the following:  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512 \n`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Request parameters