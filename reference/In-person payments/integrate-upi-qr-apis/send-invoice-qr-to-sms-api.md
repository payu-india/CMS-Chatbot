---
title: Send Invoice QR to SMS API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Send Invoice QR to SMS** API is used to send SMS to provided phoneNumber post transaction. Whenever payment is success/fail via SDK, merchant will call this API to send the payment confirmation SMS to merchant’s executive phone number.

| Environments | URI                                             |
| :----------- | :---------------------------------------------- |
| Production   | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "`string` This parameter must include the merchant key that was provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \n  \nProduction: Generate Production Merchant Key and Sat.  \nTest: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, send_sdk_message must be posted.",
    "1-2": "send_sdk_message",
    "2-0": "hash  \n`mandatory`",
    "2-1": "string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \n  \nsha512(key|command|var1|salt)  \nsha512 is the encryption method used here.",
    "2-2": "ajh84babvav",
    "3-0": "var1  \n`mandatory`",
    "3-1": "`string` This parameter must contain the merchant PayU ID that was provided by PayU.",
    "3-2": "412345678912356095",
    "4-0": "var2  \n`mandatory`",
    "4-1": "string This parameter must contain the merchant phone number to which the invoice is sent as SMS.",
    "4-2": "7727820112"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'command=send_sdk_message' \
--data-urlencode 'key=J****g' \
--data-urlencode 'hash=602a7b58b239e6bdbf762f01cada3652a25b0de0002445dbed69febb652b9c376375b1322b531116cd0a1bee37cdc8ef8a393e066b4c9a836ea4c6c45ff90460' \
--data-urlencode 'var1=13863413996' \
--data-urlencode 'var2=9833208174'
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n0 - If web service call failed.  \n1 - If web service call succeeded",
    "1-0": "msg",
    "1-1": "This parameter returns the following message if the SMS was sent successfully:  \nsms request successful"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample response

#### Success scenario

```Text JSON
a:2:{s:6:"status";i:1;s:3:"msg";s:18:"sms request successful";}
```

#### Failure scenario

- **SMS request failed**

```Text JSON
a:2:{s:6:"status";i:0;s:3:"msg";s:18:"sms request failed";}
```

- **Invalid phone number**

```Text JSON
a:2:{s:6:"status";i:0;s:3:"msg";s:20:"phone is not numeric";}
```

- **Invalid PayU ID**

```
a:2:{s:6:"status";i:0;s:3:"msg";s:59:"There is no success or failed transaction with given payuId";}
```