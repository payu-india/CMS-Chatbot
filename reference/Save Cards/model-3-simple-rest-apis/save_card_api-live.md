---
title: '[OLD]Save a Card API'
excerpt: 'API Command: **save_payment_instrument**'
api:
  file: storecard-1.json
  operationId: save_payment_instrument
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Save Card API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`.

> 📘 Note
> 
> As per RBI guidelines, taking consent from the customer and doing an additional factor of authentication is mandatory to tokenize the card. You must ensure this is done before using this API.

HTTP Method: **POST** 

<GENERALAPIsEnvironment />

## Response parameters

For the response parameter descriptions and sample responses, refer to[ Additional Info for Simple REST APIs](/reference/additional-info-for-model-3-parameters#response-parameters-for-save-a-card-api).

## Reference info for request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "The merchant key provided by PayU while onboarding.  \nFor more information on how to generate the Key and Salt, refer to any of the following:  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for this API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512 \n`",
    "2-0": "var3",
    "2-1": "For more information on card mode codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards).",
    "3-0": "var4",
    "3-1": "For more information on card type codes, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)",
    "4-0": "var6",
    "4-1": "Use only the following **test cards** for doing mock API calls here:  \n- 4895370077346937 (VISA is the card type)  \n- 5506900480000008 (MAST is the card type)",
    "5-0": "var9",
    "5-1": "**Note**: This parameter is mandatory for Rupay cards. Authentication reference number will be sent by the PG in the authorization response. Currently, this check is skipped by Rupay."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Request parameters