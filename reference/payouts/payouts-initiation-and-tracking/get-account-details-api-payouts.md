---
title: Get Account Details API - Payouts
excerpt: ''
api:
  file: payout-for-merchants-16.json
  operationId: Getaccountdetail
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **getAccountDetail** API returns complete account details of the merchant’s Payouts account.

**Environment**

|                            |                                                                 |
| -------------------------- | --------------------------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/merchant/getAccountDetail>    |
| **Production Environment** | <https://payout.payumoney.com/payout/merchant/getAccountDetail> |

<details><summary>Sample request</summary>

```curl
curl -X GET \
 https://test.payumoney.com/payout/merchant/getAccountDetail
 -H 'cache-control: no-cache' \
 -H 'content-type: application/x-www-form-urlencoded' \
 -H 'authorization: bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188' \
 -H 'payoutMerchantId: 1111123'
```

</details>

<details><summary>Sample response</summary>

```
{
"status": 0,
"msg": null,
"code": null,
"data": {
"payoutMerchantId": 1111123,
"uuid": "11e8-5a8f-05faaaa4-84a5-020d245326e4",
"virtualAccountNumber": "PAYUIN1111123",
"transferableAmount": 0,
"balance": 94003,
"lowBalance": false,
"ifsc": "YESB0CMSNOC",
"type": "current",
"clientId": "6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e",
"transitAccountNumber": null
}
}
```

</details>

<details><summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "Status",
    "0-1": "Indicates any of the following API status codes as:  \n0: Success  \n1: Failure",
    "1-0": "msg",
    "1-1": "Displays the API response message in this parameter.",
    "2-0": "code",
    "2-1": "Displays the error code in case of any error in this field. For the list of error codes, refer to [Error Codes](ref:error-codes-for-payouts).",
    "3-0": "data.payoutMerchantId",
    "3-1": "Displays the unique Payouts Merchant ID in this field.",
    "4-0": "data.uuid",
    "4-1": "Displays the unique User ID of user in this field.",
    "5-0": "data.virtualAccountNumber",
    "5-1": "Displays the virtual account number of merchant in this field. This is used for prefunding the merchant payout account",
    "6-0": "data.ifsc",
    "6-1": "Displays the IFSC Code of the bank account in this field.",
    "7-0": "data.type",
    "7-1": "Displays the type of the bank account in this field.",
    "8-0": "data.transferableAmount",
    "8-1": "Displays the the amount or limit set for transfer from futuristic payments in this field.",
    "9-0": "data.balance",
    "9-1": "Displays the current balance of merchant’s Payout account in this field.",
    "10-0": "data.lowBalance",
    "10-1": "Displays any of the following flag in this field:  \n  \n- **True**: Payout Account holds low balance to process next transfer request\n- **False**: Payout Account holds enough balance to process next transfer request",
    "11-0": "data.clientId",
    "11-1": "Displays the public client ID for generating access token in this field.",
    "12-0": "data.transitAccountNumber",
    "12-1": "Displays the transit account number in this field."
  },
  "cols": 2,
  "rows": 13,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

## Header & request parameters

> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.