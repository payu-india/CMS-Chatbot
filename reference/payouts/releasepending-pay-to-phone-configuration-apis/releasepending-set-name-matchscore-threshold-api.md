---
title: Set Name Match Score Threshold API
excerpt: ''
api:
  file: payouts-api-2.json
  operationId: SetNameMatchScoreThresholdAPI
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to set name score threshold at payout virtual account level using payoutMerchantId and threshold.

|                        |                                                                                                                                        |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://uatoneapi.in/payout/merchant/nameMatchScoreConfig](https://uatoneapi.in/payout/merchant/nameMatchScoreConfig)                 |
| Production Environment | [https://payout.payumoney.com/payout/merchant/nameMatchScoreConfig](https://payout.payumoney.com/payout/merchant/nameMatchScoreConfig) |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request PUT 'https://uatoneapi.in/payout/merchant/nameMatchScoreConfig?threshold=70' \
  --header 'Authorization: Bearer 2a708a367c5169d1643bf471f3c72c15be3334c67742d023dafc079a7ba67c2e' \
  --header 'payoutMerchantId: 1111157'
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```
  {
      "status": 0,
      "msg": "success",
      "code": null,
      "data": {
          "id": 63,
          "merchantId": null,
          "entityId": 1111157,
          "entityType": "merchant_id",
          "configKey": "merchant_name_match_threshold",
          "configValue": "70.0",
          "groupName": null,
          "isActive": true,
          "addedOn": "2024-04-24T14:43:42.643+0000",
          "updatedOn": "2024-04-24T14:43:42.643+0000",
          "isDeleted": false,
          "updatedBy": null
      }
  }

  ```
</details>

## Request parameters