---
title: View Beneficiary Details API
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
The **View Beneficiary Details** API is used to get all the beneficiaries available under the merchant account.

HTTP Method: **GET**

**Environment**

| | |
| -------------------------- | -------------------------------------------------------------------- |
| **Test Environment**       | https://uatoneapi.payu.in/payout/beneficiary?beneficiaryId=`{id}`    |
| **Production Environment** | https://payout.payumoney.com/payout/beneficiary?beneficiaryId=`{id}` |

## Request header

| **Parameter** | **Description** | **Example** |
| ------------- | --------------- | ----------- |
| Authorization<br />`mandatory` | `String` Specify the access token generated earlier in this parameter. | Bearer `{access_token}` |
| payoutMerchantId<br />`mandatory` | `String` Specify the payout merchant id provided while onboarding or creating Payout account. | 1111126 |
| Content-Type<br />`mandatory` | `String` Indicates the format in which the request is sent. | application/json |

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don't know your **payoutsMerchantID**.

## Request parameters

| **Parameters** | **Description** | **Example** |
| -------------- | --------------- | ----------- |
| beneficiaryId<br />`mandatory` | `Long` Indicates beneficiary ID returned while creation | |

## Sample request

```curl
curl --location 'https://uatoneapi.payu.in/payout/beneficiary?beneficiaryId=14' \
--header 'payoutMerchantId: 2225335' \
--header 'Authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7'
```

## Sample response

```json
{
    "status": 0,
    "msg": "Beneficiary Created with Id :12120",
    "code": null,
    "data": {
        "beneficiaryId": 12120,
        "name": "Ankush",
        "email": "ankush@gmail.com",
        "mobile": "1234567890",
        "accountNo": "123456789012",
        "ifsc": "ICIC0000046",
        "vpa": null,
        "merchantId": 2222740,
        "isValid": true,
        "addedOn": "2022-09-06T07:28:40.000+0000",
        "updatedOn": "2022-09-06T07:28:40.000+0000",
        "isVerified": null,
        "isRegistered": null,
        "nameWithBank": null,
        "cardNo": null,
        "beneCode": null
    }
}
```
