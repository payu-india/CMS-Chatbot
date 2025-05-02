---
title: Get Account Details API - Payouts
excerpt: ''
api:
  file: payout-for-merchants-16.json
  operationId: Getaccountdetail
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **getAccountDetail** API returns complete account details of the merchant’s Payouts account.

**Environment**

|                        |                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://uatoneapi.payu.in/payout/merchant/getAccountDetail](https://uatoneapi.payu.in/payout/merchant/getAccountDetail>)       |
| Production Environment | [https://payout.payumoney.com/payout/merchant/getAccountDetail](https://payout.payumoney.com/payout/merchant/getAccountDetail>) |

<details>
  <summary>Sample request</summary>

  ```curl
  curl -X GET \
   https://test.payumoney.com/payout/merchant/getAccountDetail
   -H 'cache-control: no-cache' \
   -H 'content-type: application/x-www-form-urlencoded' \
   -H 'authorization: bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188' \
   -H 'payoutMerchantId: 1111123'
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```
  {
  "status": 0,
  "msg": null,
  "code": null,
  "data": {
  "payoutMerchantId": 1111123,
  "uuid": "11e8-5a8f-05faaaa4-84a5-020d245326e4",
  "virtualAccountNumber": "PAYUIN1111123",
  "transferableAmount": 0,
  "balance": 94003,
  "lowBalance": false,
  "ifsc": "YESB0CMSNOC",
  "type": "current",
  "clientId": "6f8bb4951e030d4d7349e64a144a534778673585f86039617c167166e9154f7e",
  "transitAccountNumber": null
  }
  }
  ```
</details>

<details>
  <summary>Response parameters</summary>

  <HTMLBlock>{`
    <table style="width: 100%; border-collapse: collapse;">
    <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Status</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Indicates any of the following API status codes as:<br>0: Success<br>1: Failure</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the API response message in this parameter.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the error code in case of any error in this field. For the list of error codes, refer to <a href="ref:error-codes-for-payouts">Error Codes</a>.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.payoutMerchantId</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the unique Payouts Merchant ID in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.uuid</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the unique User ID of user in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.virtualAccountNumber</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the virtual account number of merchant in this field. This is used for prefunding the merchant payout account</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.ifsc</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the IFSC Code of the bank account in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.type</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the type of the bank account in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.transferableAmount</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the the amount or limit set for transfer from futuristic payments in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.balance</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the current balance of merchant’s Payout account in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.lowBalance</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays any of the following flag in this field:  </p>
    <ul>
    <li><strong>True</strong>: Payout Account holds low balance to process next transfer request</li>
    <li><strong>False</strong>: Payout Account holds enough balance to process next transfer request</li>
    </ul>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.clientId</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the public client ID for generating access token in this field.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data.transitAccountNumber</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Displays the transit account number in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>
  `}</HTMLBlock>
</details>

## Header & request parameters

> 📘 Note:
>
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.