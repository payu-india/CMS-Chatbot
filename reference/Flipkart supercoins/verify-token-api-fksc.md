---
title: Verify Token API - FKSC
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
The **Verify Token** API is used to verify the OTP entered by the customer to get the token as a response.

> 📘 Note: 
> 
> The token received in the response can be used only for getting the reward balance.

#### Endpoints

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Test Environment</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Production Environment</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">&lt;TBD&gt;</td></tr></tbody></table>

## **Request Header**

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Content-Type  \n**mandatory**",
    "0-1": "Indicates the format in which the request is sent.",
    "0-2": "application/json",
    "1-0": "clientType",
    "1-1": "Pass the type of client making the request and in this case, it is **loyalty**.",
    "1-2": "loyalty",
    "2-0": "Origin",
    "2-1": "Pass the origin URL (the domain) from which the request is being made.",
    "2-2": "<https://staging-rewards-api.payu.in'>",
    "3-0": "Referer",
    "3-1": "Pass the URL that the client was on when the request was done.",
    "3-2": "<https://staging-rewards-api.payu.in/>"
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


## **Request Parameters**

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "mobileNumber  \n**mandatory**",
    "0-1": "The customer's mobile number for whom the reward balance must be fetched.",
    "0-2": "8076499393",
    "1-0": "otp  \n**mandatory**",
    "1-1": "The OTP received by the customer on their mobile.",
    "1-2": "518730",
    "2-0": "merchantTxnId  \n**mandatory**",
    "2-1": "The merchant must pass the transaction ID.",
    "2-2": "CL001",
    "3-0": "transactionFlow  \n**mandatory**",
    "3-1": "This parameter must be set with the value as \"SEAMLESS.\"",
    "3-2": "SEAMLESS",
    "4-0": "parentPayuTxnId  \n**optional**",
    "4-1": "The PayU transaction ID of the transaction.",
    "4-2": "999000000017497",
    "5-0": "uuid  \n**mandatory**",
    "5-1": "The UUID (Universally unique identifier) of the customer.",
    "5-2": "1894095170321102220",
    "6-0": "loyaltyProvider  \n**mandatory**",
    "6-1": "The loyalty provider name is specified in this parameter. For FKSC, it is SUPERCOIN.",
    "6-2": "SUPERCOIN"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]




## Sample Request

```curl
curl -X 'POST' \  'https://ltest.payu.in/otp/v1?action=verify' \  -H 'accept: application/json' \  -H 'Content-Type: application/json' \  -d '{  "otp": "123123",  "uuid": 123456789,  "merchantTxnId": "123merchantTxnId",  "mobileNumber": "9999999999",  "loyaltyProvider": "SUPERCOIN",  "transactionFlow": "SEAMLESS"}'
```



## Sample Response

```plaintext
{    "token": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MDc2NDk5MzkzIiwibW9iaWxlTnVtYmVyIjoiODA3NjQ5OTM5MyIsImV4cCI6MTY4NjQ2NDkyNywiaWF0IjoxNjc4Njg4OTI3fQ.xIpRniWLFa0suN8Cb2ndzX4JVFfXHELCi2bdVSMTdlE"}
```