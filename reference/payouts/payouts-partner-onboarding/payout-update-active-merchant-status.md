---
title: Update Active Merchant Status API
excerpt: ''
api:
  file: payoutspartner-5.json
  operationId: updateActiveMerchantStatus
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to update merchant active status.

**Environment**

<PayoutsPartnerEnvionment />

<details><summary>Sample request</summary>

```curl
'https://uatoneapi.payu.in/payout/partner/merchant/updateActiveMerchantStatus?payoutMerchantId=1111157&isActive=true' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Bearera48006015b338196f8975a63861c1600b0a641e27acc2759e981796906cde7ad' \
--header 'partnerId: 2'
```

</details>

## Request parameters