---
title: Initiate Transfer API
excerpt: ''
api:
  file: payouts-api-16.json
  operationId: InitiateTransferAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **payment** API is used to initiate/schedule a single transfer to the beneficiary account, UPI address, or credit card.

**Environment**

|                            |                                               |
| -------------------------- | --------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/v2/payment> |
| **Production Environment** | <https://payout.payumoney.com/payout/payment> |

<details>
  <summary>Sample request</summary>

**IMPS, NEFT or RTGS Payment Request**

```curl
[
 {
 "beneficiaryAccountNumber": "51234567890",
 "beneficiaryIfscCode": "HDFC0001234",
 "beneficiaryName": "Payu",
 "beneficiaryEmail": "payu@payu.in",
 "beneficiaryMobile": "9876473627",
 "purpose": "Payment from Company",
 "amount": 1234.12,
 "batchId": "1",
 "merchantRefId": "123asdfad3",
 "paymentType": "IMPS",
 "retry" : false
 }
]
```

**UPI Payment Request**

```curl
[
 {
 "beneficiaryName": "Payu",
 "beneficiaryEmail": "payu@payu.in",
 "beneficiaryMobile": "9876473627",
 "purpose": "Payment from Company",
 "amount": 1234.12,
 "batchId": "1",
 "merchantRefId": "123",
 "paymentType": "UPI",
 "vpa" : "ankush.pokarana@ybl",
 "retry" : false
 }
]
```

</details>

<details>
  <summary>Sample response</summary>

**Success response**

```plaintext
{
 "status": 0,
 "msg": "Requests are in process. Will send response of individual request on webhooks set by you",
 "code": null,
 "data": []
 }
```

**Failure response**

```plaintext
{
 "status": 1,
 "msg": null,
 "code": null,
 "data": [
           {
            "batchId": "1",
            "merchantRefId": "111",
            "error": "beneficiary account number can not be empty. ",
            "code": [1004]
           }
         ]
 }
```

</details>

## Header and request parameters

> 📘 Version 2.0 API:
>
> This page includes Try IT experience for version 2.0. of** Initiate Transfer **API, so you need to pass the **pid** in the header unlike payoutMerchantId with version 1.0 APIs.

<details>
  <summary>Additional information for Request parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "merchantRefId`\noptional`",
    "0-1": "`String`Indicates a unique reference ID at the merchant side to distinguish between multiple transfers.  \n**Max char length**: 40.  \n**Notes** :  \n  \n- Same value will be used by the merchant in the status check of transfer.\n- In case if the merchant reference ID is not passed, an auto generated ID will be used.",
    "0-2": " ",
    "1-0": "paymentType  \n`mandatory`",
    "1-1": "`String` Specify the any of the following mode of payment in this field:  \n  \n- IMPS\n- UPI\n- NEFT\n- RTGS",
    "1-2": "UPI"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]

</details>