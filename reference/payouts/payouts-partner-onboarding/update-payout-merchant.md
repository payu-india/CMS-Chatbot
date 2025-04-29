---
title: Update Payouts Partner Merchant API
excerpt: ''
api:
  file: payoutspartner-5.json
  operationId: updateMerchant
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to update virtual account belonging to partner ID.

**Environment**

<PayoutsPartnerEnvionment />

<details><summary>Sample request</summary>

```curl
curl --location --request PUT
'https://uatoneapi.payu.in/payout/partner/merchant/update' \
--header 'Authorization: Bearer cfa14f80a6beb1a7cd9093f9b9ef36aa6030767fb3a01f9be03fff16a11c5d97' \
--header 'Cache-Control: no-cache' \
--header 'payoutMerchantId: 1112155' \
--header 'Content-Type: application/json' \
--header 'partnerId: 2' \
--data-raw '{
"commEmail":"makerchecker@yopmail.com",
"commMobile": "9654461774",
"name":"SarAANSH",
"category": "SILVER",
"activationStatus": "FULLY_ACTIVE",
"description":"testing123",
"accountType": "MERCHANT"
}'
```

</details>

<details><summary>Sample response</summary>

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "id": 1112155,
        "uuid": "11ea-bc-svdfbf-sdvbdfbfd",
        "isActive": true,
        "addedOn": "2024-02-07T17:38:00.000+0000",
        "updatedOn": "2024-02-07T17:45:33.087+0000",
        "userId": 730,
        "name": "SarAANSH",
        "commEmail": "makerchecker@yopmail.com",
        "commMobile": "9654461774",
        "purpose": null,
        "parentPid": null,
        "subAccName": null,
        "category": "Silver",
        "lob": null,
        "accountType": "Merchant",
        "onboardingType": null,
        "activationStatus": "FULLY_ACTIVE",
        "businessUseCase": null,
        "description": "testing123",
        "onHoldType": null,
        "riskCategory": null,
        "website": null,
        "lastUpdatedBy": null
    }
}
```

</details>

## Request parameters