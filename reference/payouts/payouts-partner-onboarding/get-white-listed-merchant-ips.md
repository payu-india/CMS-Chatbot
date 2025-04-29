---
title: Get Whitelisted Partner Merchant IPs API
excerpt: ''
api:
  file: payoutspartner-5.json
  operationId: getWhiteListedIp
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to get a list of whitelisted partner merchant IPs.

**Environment**

<PayoutsPartnerEnvionment />

<details><summary>Sample request</summary>

```
curl --location
'https://uatoneapi.payu.in/payout/partner/getWhiteListedIp?payoutMerchantId=2225336' \
--header 'partnerId: 1' \
--header 'Authorization: Bearer 0268711b05d99eee3a068033e3df41f97a532d9a84fcd25d17e0644a835dda2c'
```

</details>

<details><summary>Sample response</summary>

```
{
    "status": 0,
    "msg": "success",
    "code": null,
    "data": "192.168.0.1,192.168.0.2,192.168.0.5"
}
```

</details>