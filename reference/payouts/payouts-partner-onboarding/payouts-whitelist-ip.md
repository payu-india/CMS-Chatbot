---
title: Whitelist Partner Merchant IP API
excerpt: ''
api:
  file: payoutspartner-5.json
  operationId: whitelistIp
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to whitelist IP for partner account at virtual account-level and user-level.

**Environment**

<PayoutsPartnerEnvionment />

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST
'https://uatoneapi.payu.in/payout/partner/whitelistIp?payoutMerchantId=2225336&m
erchantIps=14.143.127.46' \
--header 'Authorization: Bearer
858cafed9e2a8b362b4b4c61f75dee24a6f2f99c2921e51efff0617f695c47cf' \
--header 'partnerId: 1'
```

</details>

<details>
  <summary>Sample request</summary>

```
{
    "status": 0,
    "msg": "IP added successfully at merchant level",
    "code": null,
    "data": null
}
```

</details>

## Request parameters