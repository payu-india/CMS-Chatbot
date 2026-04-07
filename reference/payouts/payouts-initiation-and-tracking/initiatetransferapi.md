---
title: InitiateTransferAPI
api:
  file: initiate_transfer.json
  operationId: InitiateTransferAPI
hidden: false
---
The **payment** API is used to initiate/schedule a single transfer to the beneficiary account, UPI address, or credit card.

**Environment**

|                            |                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/v2/payment](https://uatoneapi.payu.in/payout/v2/payment) |
| **Production Environment** | [https://payout.payumoney.com/payout/payment](https://payout.payumoney.com/payout/payment) |

<details>
  <summary>Sample request</summary>

  **IMPS, NEFT or RTGS Payment Request**

  ```curl
  [
   {
   "beneficiaryAccountNumber": "51234567890",
   "beneficiaryIfscCode": "HDFC0001234",
   "beneficiaryName": "Payu",
   "beneficiaryEmail": "payu@payu.in",
   "beneficiaryMobile": "9876473627",
   "purpose": "Payment from Company",
   "amount": 1234.12,
   "batchId": "1",
   "merchantRefId": "123asdfad3",
   "paymentType": "IMPS",
   "retry" : false
   }
  ]
  ```

  **UPI Payment Request**

  ```curl
  [
   {
   "beneficiaryName": "Payu",
   "beneficiaryEmail": "payu@payu.in",
   "beneficiaryMobile": "9876473627",
   "purpose": "Payment from Company",
   "amount": 1234.12,
   "batchId": "1",
   "merchantRefId": "123",
   "paymentType": "UPI",
   "vpa" : "ankush.pokarana@ybl",
   "retry" : false
   }
  ]
  ```
</details>

<details>
  <summary>Sample response</summary>

  **Success response**

  ```plaintext
  {
   "status": 0,
   "msg": "Requests are in process. Will send response of individual request on webhooks set by you",
   "code": null,
   "data": []
   }
  ```

  **Failure response**

  ```plaintext
  {
   "status": 1,
   "msg": null,
   "code": null,
   "data": [
             {
              "batchId": "1",
              "merchantRefId": "111",
              "error": "beneficiary account number can not be empty. ",
              "code": [1004]
             }
           ]
   }
  ```
</details>

## Header and request parameters

> 📘 Version 2.0 API:
>
> This page includes Try IT experience for version 2.0. of** Initiate Transfer **API, so you need to pass the **pid** in the header unlike payoutMerchantId with version 1.0 APIs.

<details>
  <summary>Additional information for Request parameters</summary>

  <HTMLBlock>{`
      <table style="width: 100%; border-collapse: collapse;">
      <thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
        <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantRefId<code> optional</code></p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Indicates a unique reference ID at the merchant side to distinguish between multiple transfers.<br><strong>Max char length</strong>: 40.<br><strong>Notes</strong> :  </p>
      <ul>
      <li>Same value will be used by the merchant in the status check of transfer.</li>
      <li>In case if the merchant reference ID is not passed, an auto generated ID will be used.</li>
      </ul>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"></td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentType<br><code>mandatory</code></p>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Specify the any of the following mode of payment in this field:  </p>
      <ul>
      <li>IMPS</li>
      <li>UPI</li>
      <li>NEFT</li>
      <li>RTGS</li>
      </ul>
      </td>
        <td style="border: 1px solid #ddd; padding: 8px;"><p>UPI</p>
      </td>
      </tr>
      </tbody>
      </table>
  `}</HTMLBlock>
</details>
