---
title: Validate VPA - Payouts
excerpt: ''
api:
  file: paritalgeneral-apis-9.json
  operationId: validateVPA
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API lets you validate VPA ID of your customers. It will return whether a particular VPA ID exists or not. We recommend you to validate VPA before initiating UPI transactions to have better success rates on Payouts

|                            |                                                                                                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Production Environment** | [https://payout.payumoney.com/payout/merchant/validateVpa](https://payout.payumoney.com/payout/merchant/validateVpa) |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/merchant/validateVpa](https://uatoneapi.payu.in/payout/merchant/validateVpa)       |

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request POST 'https://uatoneapi.payu.in/payout/merchant/validateVpa?vpa=omi1@yesb' \
  --header 'Authorization: Bearer d7510afefcfd3efb771372205362541ac0d8e1a1921f5020f61c8331dcc2b43e' \
  --header 'payoutMerchantId: 1111126' \
  --header 'Content-Type: application/x-www-form-urlencoded'
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success scenario**

  ```
  {
      "status": 0,
      "msg": "vpa available",
      "code": null,
      "data": {
          "message": null,
          "name": "ANKUSH POKARANA"
      }
  }
  ```

  **Failure scenario**

  ```
  {
      "status": 1,
      "msg": "vpa not available",
      "code": null,
      "data": {
          "message": "UPI address is invalid",
          "name": null
      }
  }
  ```
</details>

## Header and request parameters

> 📘 Note:
>
> The payoutMerchantId is different from PayU merchant ID. Check the Payouts Dashboard or call PayU Customer Support if you don’t know your payoutMerchantID.

> 📘 Sample values for Test environment:
>
> Use only "kk\@okaxis" for the test environment.