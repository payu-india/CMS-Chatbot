---
title: Fetch Balance API – Sodexo Integration
excerpt: 'API Command: **check\_balance**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Fetch Balance **check\_balance** API command is used to check the balance of a Sodexo card. When using Seamless Integration, integrate this API and display the balance on the Checkout page to your customers.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "key  \n**mandatory**",
    "0-1": "This parameter must contain your merchant key shared by PayU during onboarding.",
    "0-2": "Your Test Key",
    "1-0": "command  \n**mandatory**",
    "1-1": "This parameters must contain the API command as **check\\_balance**.",
    "1-2": "check\\_balance",
    "2-0": "hash  \n**mandatory**",
    "2-1": "This parameter contains the hash. Use the following hash generation format:  \n`sha512(key\\|command\\|var1\\|salt) sha512`",
    "2-2": " ",
    "3-0": "var1  \n**mandatory**",
    "3-1": "This parameter must contain the Sodexo Source ID in JSON format as provided in the example.",
    "3-2": "`{sodexoSourceId\":\"src_81e2c860-631b-4b01-aefa-19cfa9c63415\"}`"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Notes:
> 
> - **var1** is in a JSON format. All the sub fields are to be sent as a json in var1. The whole JSON string should be used for hash generation.
> - **sourceId** is shared by PayU with merchants in the field3 parameter in any of the following API responses for all successful transactions wherever customer has provided permission to save their card.
>   - ws\_callback
>   - [Verify Payment API](ref:verify_payment_api)

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=check_balance&var1={"sodexoSourceId":"src_81e2c860-631b-4b01-aefa-19cfa9c63415"}&hash=fbd44e564f49aaa271250df4fc9fdc5a7eff98d961d6ca8e8049ae0f830d7ee7ff73a4b74c69c9742ccfe0c0478e737c4c685a3fe614ba5ef7edf706097e3346"
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n   - 0 - If web service call failed.  \n   - 1 - If web service call succeeded.",
    "0-2": "1",
    "1-0": "cardNo",
    "1-1": "This parameter contains the Sodexo card number.",
    "1-2": "637513XXXXXX9318",
    "2-0": "cardBalance",
    "2-1": "This parameter returns the card balance (in rupees).",
    "2-2": "3000.00",
    "3-0": "cardName",
    "3-1": "This parameter contains name of the customer as on the Sodexo card.",
    "3-2": "test",
    "4-0": "msg",
    "4-1": "This parameter contains the message, that is successful or failure.",
    "4-2": "success"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample response

### Success scenario

```plaintext
{"status":1,"cardNo":"637513XXXXXX9318","cardBalance":".82","cardName":"test","msg":"success"}
```

### Failure scenarios

- Hash is invalid

```plaintext
{"status":0,"msg":"Invalid Hash."}
```

- Unable to fetch balance

```plaintext
{"status":0,"msg":"Unable to fetch balance"}
```

- Sodexo Source ID is not found

```plaintext
{"status":0,"msg":"Source not found."}
```