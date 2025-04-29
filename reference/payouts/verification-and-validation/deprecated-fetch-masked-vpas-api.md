---
title: Fetch Masked VPAs API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **fetchMaskedVpa** API is used to fetch the list of masked UPI IDs against any mobile number.

HTTP Method: **POST**

**Environment**

|                            |                                                              |
| -------------------------- | ------------------------------------------------------------ |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/payment/fetchMaskedVpa>    |
| **Production Environment** | <https://payout.payumoney.com/payout/payment/fetchMaskedVpa> |

## Header parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Authorization`\nmandatory`",
    "0-1": "`String`Specify the access token generated during authentication in this parameter.",
    "0-2": "Bearer {access\\_token}",
    "1-0": "payoutMerchantId  \n`mandatory`",
    "1-1": "`String`Specify the merchant ID provided while onboarding for Payouts in this parameter.",
    "1-2": "1111126",
    "2-0": "Content-Type`\nmandatory`",
    "2-1": "`String`Indicates the format in which the request is sent.",
    "2-2": "application/x-www-form-urlencoded"
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


> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "mobileNumber  \n`mandatory`",
    "0-1": "`String`Indicates the mobile number of the beneficiary",
    "0-2": "9999999999"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```
curl --location --request GET 'https://test.payumoney.com/payout/payment/fetchMaskedVpa?mobileNumber=1234567890' \
--header 'Authorization: Bearer 0f8188bfdf6ff8c630376c63497f3745ff3e21b9dfdc9a4955b4561cec9bb05e' \
--header 'payoutMerchantId: 2222740' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: Path=/; Path=/' \
--data-urlencode 'mobileNumber=1234567890'
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n   -** 0** - If web service call succeeded  \n   -**  1** - If web service call failed",
    "1-0": "msg",
    "1-1": "This parameter returns the success or failure message.",
    "2-0": "code",
    "2-1": "This parameter returns the error code if the API failed to verify or invalid details.",
    "3-0": "data",
    "3-1": "This parameter returns the saved card details in a JSON format. For more information, refer to the next table."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


### Description of data JSON fields

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "result",
    "0-1": "The version of the results displayed for this API.",
    "1-0": "VPA ID",
    "1-1": "This field returns the following details in an array format:  \n   - **Token**: The token for the VPA. For example, \"13e3a8caa1ede3c56a524\"  \n   - **name**: The name of the account holder.  \n    - **App_Name**: The name of the UPI provider through which the UPI is used by beneficiary. For example, Google Pay"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample response

- Success response

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "result": 1.0,
        "9x1x3x5x8x@okaxis": {
            "Token": "13e3a8caa1ede3c56a524",
            "name": "",
            "App_Name": "Google Pay"
        },
        "9x3x5x0x9x@ybl": {
            "Token": "291dc5886ed5a13f50ccd",
            "name": "Sajan Bhadrike ",
            "App_Name": "PhonePe"
        }
    }
}
```

- Failure response
- ```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": null
  }
  ```