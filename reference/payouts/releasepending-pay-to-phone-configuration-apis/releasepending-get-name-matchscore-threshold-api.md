---
title: Get Name Match Score Threshold API
excerpt: ''
api:
  file: payouts-api-3.json
  operationId: SetNameMatchScoreThresholdAPI-Copy
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to fetch name score threshold using the payout merchant ID.

|                        |                                                                                                                                        |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://uatoneapi.in/payout/merchant/nameMatchScoreConfig](https://uatoneapi.in/payout/merchant/nameMatchScoreConfig)                 |
| Production Environment | [https://payout.payumoney.com/payout/merchant/nameMatchScoreConfig](https://payout.payumoney.com/payout/merchant/nameMatchScoreConfig) |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location 'https://uatoneapi.in/payout/merchant/nameMatchScoreConfig' \
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
      "data": 70.0
  }

  ```
</details>

## Request parameters