---
title: Cancel Transfer API
excerpt: ''
api:
  file: payout-for-merchants-20.json
  operationId: PayoutCancelAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Cancel Transfer** API command is used to cancel the queued transfer.

> 📘 Note:
>
> You can cancel a transfer until it is in the **Queued/Scheduled** status only. After the transaction gets transitioned to the **In Progress** (the next status to Queued), you cannot cancel it.

**Environment**

|            |                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------- |
| Production | [https://payout.payumoney.com/payout/payment/cancel](https://payout.payumoney.com/payout/payment/cancel) |
| Test       | [https://uatoneapi.payu.in/payout/payment/cancel](https://uatoneapi.payu.in/payout/payment/cancel)       |

<details>
  <summary>Sample request</summary>

  ```curl
  curl -X POST \
   https://test.payumoney.com/payout/payment/cancel \
   -H 'authorization: bearer 45f87fed35bdafe9f47698ed03e202e282f873b79a57eb53a9d30247b376f01d' \
   -H 'content-type: application/x-www-form-urlencoded' \
   -H 'payoutmerchantid: 1111122' \
   -d merchantRefId=1584856958885
  ```
</details>

<details>
  <summary>Sample response</summary>

  <br />

  Success response

  ```plaintext
  {
   "status": 0,
   "msg": "Payout transaction cancelled",
   "code": null,
   "data": null
   }
  ```

  Failure response

  ```plaintext
  {
   "status": 1,
   "msg": "Merchant reference Id is incorrect",
   "code": null,
   "data": null
   }
  ```
</details>

## Header and request parameters

> 📘 Note:
>
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

> 📘 Reference:
>
> For sample request and response, refer to [Sample Request and Response for Initiation & Tracking APIs](ref:sample-request-and-response-for-initiation-tracking-apis#cancel-transfer-api).