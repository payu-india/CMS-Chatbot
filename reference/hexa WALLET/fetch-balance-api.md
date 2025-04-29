---
title: Fetch Balance API
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
The **check\_balance** API command is used to check the balance using the customer’s mobile number. When using Seamless Integration, integrate this API and display the balance on the Checkout page to your customers.

**Environment**

|                        |                                                 |
| :--------------------- | :---------------------------------------------- |
| Test Environment       | <https://test.payu.in/merchant/postservice.php> |
| Production Environment | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "command  \n**mandatory**",
    "0-1": "This parameters must contain the API command as **check\\_balance**.",
    "0-2": "check\\_balance",
    "1-0": "key  \n**mandatory**",
    "1-1": "This parameter must contain your merchant key shared by PayU during onboarding.",
    "1-2": "Your Test Key",
    "2-0": "hash  \n**mandatory**",
    "2-1": "This parameter contains the hash. Use the following hash generation format:`\nsha512(key\\|command\\|var1\\|salt) sha512`",
    "2-2": " ",
    "3-0": "var1  \n**mandatory**",
    "3-1": "This parameter must be in a JSON format as described in [var1 fields description](#var1-fields-description) table.",
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
> - var1 is in a JSON format. 
> - All the sub fields are to be sent as a json in var1. 
> - The whole JSON string should be used for hash generation.

### var1 fields description

The var1 is posted in the following format:

```
{"walletIdentifier":"AMUL","mobile":"9886575652","ibibo_code":"PAY"}
```

| Field            | Desscription                 |
| :--------------- | :--------------------------- |
| walletidentifier | Name of the wallet.          |
| ibibo_code       | The bank code of the wallet. |
| mobile           | Customer's mobile number.    |

## Sample request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=check_balance&  var1={"walletIdentifier":"AMUL","mobile":"9886575652","ibibo_code":"PAY"}&hash=fbd44e564f49aaa271250df4fc9fdc5a7eff98d961d6ca8e8049ae0f830d7ee7ff73a4b74c69c9742ccfe0c0478e737c4c685a3fe614ba5ef7edf706097e3346"
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n- 0 - If web service call failed.\n- 1 - If web service call succeeded.",
    "0-2": "1",
    "1-0": "cardBalance",
    "1-1": "This parameter returns the card balance (in rupees).",
    "1-2": "3000.00",
    "2-0": "cardName",
    "2-1": "This parameter contains name of the customer as on the Sodexo card.",
    "2-2": "test"
  },
  "cols": 3,
  "rows": 3,
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
{"status":1,"cardBalance":"117.83","cardName":"Madhu Sudhan"}
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