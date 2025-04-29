---
title: Activate Payout Partner Merchant API
excerpt: ''
api:
  file: payoutspartner-5.json
  operationId: activatePartnerMerchant
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to create virtual account belonging to partner ID.

**Environment**

<PayoutsPartnerEnvionment />

<details><summary>Sample request</summary>

```curl
curl --location 'https://uatone.payu.in/payout/partner/merchant/create' \
--header 'Authorization: Bearer 9dda80d3eef9e9eec50583e46ff9fb7fd84c10b1ee94c66c5b37f5c017e83e80' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'partnerId: 1' \
--data-urlencode 'merchantName=Lav' \
--data-urlencode 'commEmail=lav.solanki@payu.in' \
--data-urlencode 'commMobile=8447648900' \
--data-urlencode 'bank=axisbank'
```

</details>

<details><summary>Sample response</summary>

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "payoutMerchantId": 111***,
        "uuid": "11ea-bc-****-sdvb",
        "virtualAccountNumber": "PAYF***2152",
        "transferableAmount": 0.0,
        "balance": "0.0",
        "lowBalance": false,
        "ifsc": "UTIB*****",
        "type": "current",
        "clientId": "24***d7*****238cc39b7b5b54c*****41d4acd8*****20393*****f68",
        "transitAccountNumber": null,
        "transitVpa": null,
        "beneficiaryName": null,
        "category": null,
        "accountType": null,
        "onboardingType": null,
        "activationStatus": "FULLY_ACTIVE",
        "description": null,
        "userType": null,
        "limits": null,
        "limitedCapability": false,
        "businessUseCase": null,
        "riskCategory": null,
        "website": null,
        "payoutVolume": null,
        "payoutCount": null,
        "payoutPendingTxn": null,
        "hasTransfer": null,
        "hasDeposit": null,
        "hasUploadedFile": null,
        "lob": null
    }
}
```

</details>

## Request parameters