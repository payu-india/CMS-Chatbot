---
title: '[OLD]Edit a Saved Card API'
excerpt: 'API Command: **edit_payment_instrument**'
api:
  file: storecard-4.json
  operationId: edit_payment_instrument
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Edit a Card **API is used to edit the details of an existing stored card on the vault. In this case, along with all the parameters required to save to the card, the **cardToken** has to be posted. After successfully editing the card, it returns the **cardToken** of the card.

**Environment**

| Test Environment       | <https://test.payu.in/merchant>  |
| :--------------------- | :------------------------------- |
| Production Environment | <https://info.payu.in/merchant/> |

## Reference Info for Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "The merchant key provided by PayU while onboarding.  \nFor more information on how to generate the Key and Salt, refer to any of the following:  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for \\_payment API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512 \n`"
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

For the response parameter description, refer to [Additional Info for Simple REST APIs](/reference/additional-info-for-model-3-parameters#response-parameters-for-edit-card-api).

## Request Parameters