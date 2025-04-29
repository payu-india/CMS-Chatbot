---
title: Resend OTP API
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
If your customer fails to authorize the payment due to incorrect OTP submission or submission of the OTP after it is expired, you can initiate a resend OTP request by using this API

HTTP Method: **POST**

**Environment**

|                            |                                              |
| -------------------------- | -------------------------------------------- |
| **Test Environment**       | <https://test.payu.in/ResponseHandler.php>   |
| **Production Environment** | <https://secure.payu.in/ResponseHandler.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Description**",
    "0-0": "referenceId  \n**mandatory**",
    "0-1": "`String` Pass the ID returned in the response of the transaction request.",
    "0-2": "`bbed416d21dda9941a90cc72819c5b52`",
    "1-0": "resendOtp  \n**mandatory**",
    "1-1": "`String` Pass the value as 1 to resend the OTP.",
    "1-2": "1",
    "2-0": "data  \n**optional**",
    "2-1": "`String` You must pass {\"payuPureS2S\":\"1\"} as the value of this parameter.",
    "2-2": "{\"payuPureS2S\":\"1\"}"
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


## Sample request

```curl
curl --location --request POST 'https://test.payu.in/ResponseHandler.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=ef4510abes5uo7ephv7o20ossc; PHPSESSID=63ff369680638' \
--data-urlencode 'referenceId=e1757a8d4c10e75987d9adb58e2d9a1b' \
--data-urlencode 'resendOtp=1'
```

> 📘 Note:
> 
> After collecting the OTP from your customer, Use the [Submit OTP](ref:submit-otp-to-payu) API to post the OTP to PayU.