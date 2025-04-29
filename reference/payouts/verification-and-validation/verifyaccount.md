---
title: Verify Account or Penny Test API
excerpt: ''
api:
  file: paritalgeneral-apis-18.json
  operationId: VerifyAccount
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Penny Test is performed to verify the account. A certain amount is deposited into the beneficiary account details and verified if it is deposited successfully or not. On successful deposit, the account verification is completed successfully.

The **Verify Account** API will return the account holder’s name against the bank details provided.

|                            |                                                               |
| -------------------------- | ------------------------------------------------------------- |
| **Production Environment** | \<<https://payout.payumoney.com/payout/payment/verifyAccount> |
| **Test Environment**       | \<<https://uatoneapi.payu.in/payout/payment/verifyAccount>    |

<details><summary>Sample request</summary>

```curl
curl --location --request POST 'https://test.payumoney.com/payout/payment/verifyAccount' \
--header 'Authorization: Bearer c9d6fbde1b730e4d3d6c4e68002974097bb7fbc173e83aa68dd43064e502ed16' \
--header 'payoutMerchantId: 1111594' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'accountNumber=51234567890' \
--data-urlencode 'ifscCode=HDFC0001098' \
--data-urlencode 'merchantRefId=987668124234235' \
--data-urlencode 'validateIfsc=true' \
--data-urlencode 'beneName=Ankush Pokarana' \
--data-urlencode 'nameMatching=true' \
--data-urlencode 'purpose=Test'
```

</details>

<details><summary>Sample response</summary>

**Success scenario**

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "accountExists": "YES",
        "beneficiaryName": "Ankush Pokarana",
        "nameMatch": 59.45121951219513,
        "status": "Success",
        "error": ""
    }
}
```

**Pending**

```
{
   "status": 0,
   "msg": null,
   "code": null,
   "data": {
      "accountExists": "VERIFICATION_PENDING",
      "beneficiaryName": "Ankush Pokarana",
      "nameMatch": null,
      "status": "Success",
      "error": ""
   }
}
```

**Failure scenario**

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "accountExists": "No",
        "beneficiaryName": "",
        "status": "Success", 
        "error": "Invalid Benificiary MMID/Mobile Number"
    }
}
```

</details>

## Header and request parameters

> 📘 Note:
> 
> The **payoutMerchantId** is different from PayU merchant ID. Check the Payouts Dashboard or call PayU Customer Support if you don’t know your **payoutMerchantID**.