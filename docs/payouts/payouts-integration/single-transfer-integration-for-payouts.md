---
title: Single Transfer Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Single Transfer Integration
  description: >-
    Integrate PayU's Single Transfer Payouts seamlessly with our comprehensive
    API guide. Learn how to automate and manage your business payouts securely
    and efficiently. Explore the step-by-step process for integrating PayU's
    payout solutions to enhance your financial operations.
  keywords:
    - PayU Payouts integration
    - Single transfer payouts
    - Automate payouts with PayU
    - Secure payouts Integration with PayU
    - Real-time payouts API
    - Business payouts with PayU
    - Integrate PayU payouts
    - ' Salary Payouts integration with PayU Payouts API'
    - Amount Disbursements with Payouts API
  robots: index
next:
  description: ''
---
Single Transfer Integration with Payouts allows you to make instant payments to a beneficiary through the APIs using different payment modes as illustrated in the following figure:

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Frame-5-1024x304.png" />


## Step 1. Generate authentication token

Payouts Integration begins with access token generation. You should have an Access Token for authentication while accessing Payouts Endpoints. Without authentication, payouts core APIs can’t be accessed.

For this purpose, PayU provides two methods to generate the authentication token as follows:

1. [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
2. [Generate Token using Private Client ID](ref:generate-token-using-private-client-id)

> 📘 Note:
>
> The authentication tokens have a TTL (Time To Live) and are required to be refreshed after a fixed interval of time. A Refresh Token API can be requested to obtain a renewed access token. For more information on this, refer to [Refresh Token API - Payouts](ref:refresh-token-api-payouts)

***

## Step 2. Get account details

The **getAccountDetail** API returns complete account details of the merchant’s Payouts account.

**Environment**

|                        |                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://uatoneapi.payu.in/payout/merchant/getAccountDetail](https://uatoneapi.payu.in/payout/merchant/getAccountDetail>)       |
| Production Environment | [https://payout.payumoney.com/payout/merchant/getAccountDetail](https://payout.payumoney.com/payout/merchant/getAccountDetail>) |

<Accordion title="Sample request" icon="fa-code">
```curl
  curl -X GET \
   https://test.payumoney.com/payout/merchant/getAccountDetail
   -H 'cache-control: no-cache' \
   -H 'content-type: application/x-www-form-urlencoded' \
   -H 'authorization: bearer aab9dc927c4a68af7eb95ef694f0b48bb731c5a1a7111786d6658d774db14188' \
   -H 'payoutMerchantId: 1111123'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
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
</Accordion>

## Step 3. Initiate single transfer

Request for initiation of a single transfer to the beneficiary using Initiate Single Transfer API. For Try IT experience, refer to [Initiate Transfer API](ref:initiate-transfer-api).

You can transfer through various payment modes described in [Initiate Transfer API](ref:initiate-transfer-api):

* IMPS, NEFT or RTGS Payment Request
* UPI Payment Request
* Phone Payment Request
* MasterCard Payment Request
* VISA Card Payment Request
* Credit Card Payment Request
**Environment**

|                            |                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/v2/payment](https://uatoneapi.payu.in/payout/v2/payment) |
| **Production Environment** | [https://payout.payumoney.com/payout/payment](https://payout.payumoney.com/payout/payment) |

<Accordion title="Sample request" icon="fa-code">
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
</Accordion>

<Accordion title="Sample response" icon="fa-code">
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
</Accordion>


## Step 4. Check transfer status

Fetch the status of the transfer by posting the merchant’s reference ID as a parameter using the Check Transfer Status API. For more information on Payouts statuses, refer to [Payouts Lifecycle](doc:payouts-lifecycle). For Try-It experience for Check Transfer Status API, refer to [Check Transfer Status API](https://docs.payu.in/reference/check-transfer-status-api/).
**Environment**

|                            |                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/payment/listTransactions](https://uatoneapi.payu.in/payout/payment/listTransactions)       |
| **Production Environment** | [https://payout.payumoney.com/payout/payment/listTransactions](https://payout.payumoney.com/payout/payment/listTransactions) |

<Accordion title="Sample request" icon="fa-code">
```curl
  curl -X POST \
   https://test.payumoney.com/payout/payment/listTransactions \
   -H 'authorization: Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605' \
   -H 'cache-control: no-cache' \
   -H 'content-type: application/x-www-form-urlencoded' \
   -H 'payoutmerchantid: 1111122' \
   -d 'transferStatus=QUEUED&from=01%2F01%2F2019&to=01%2F01%2F2019&page=1&pageSize=100&merchantRefId=&batchId=1'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": {
          "payoutMerchantId": null,
          "noOfPages": 1,
          "totalElements": 1,
          "currentPage": 0,
          "totalAmount": 0.0,
          "succesTxn": 0,
          "pendingTxn": 0,
          "transactionDetails": [
              {
                  "txnId": 71870,
                  "batchId": "smartSendBatch",
                  "merchantRefId": "0101010031",
                  "purpose": "Payout",
                  "amount": 1.0,
                  "txnStatus": "FAILED",
                  "txnSubStatus": null,
                  "txnSource": "SMART_SEND",
                  "txnDate": "2022-08-22T05:56:13.000+0000",
                  "scheduledTxnDate": "2022-08-22T05:56:13.000+0000",
                  "payuTransactionRefNo": "PAYOUT1661147773462lrSLcvHSc1K",
                  "beneficiaryName": "Customer",
                  "beneficiaryCardNo": null,
                  "msg": "Internal Error while validating vpa account",
                  "responseCode": null,
                  "transferType": "UPI",
                  "bankTransactionRefNo": null,
                  "nameWithBank": null,
                  "lastStatusUpdateDate": "2022-08-22T05:56:15.000+0000",
                  "succeedOn": null,
                  "fee": null,
                  "tax": null,
                  "txnStatusDescription": "Internal Error while validating vpa account",
                  "custom1": null,
                  "custom2": null,
                  "custom3": null,
                  "nameMatch": null
              }
          ]
      }
  }
  ```

  The status of a particular transaction has to be determined only from the field **txnStatus** in the**transactionDetails** JSON against the **merchantRefId**.

  On receiving the following JSON Response in the **Check Transfer Status** API, the transaction status is not determined and has to considered as **unidentified** or **Pending** by merchant.

  ```
  {
      "status": 0,
      "msg": null,
      "code": null,
      "data": {
          "payoutMerchantId": null,
          "noOfPages": 0,
          "totalElements": 0,
          "currentPage": 0,
          "totalAmount": 0.0,
          "succesTxn": 0,
          "pendingTxn": 0,
          "transactionDetails": []
      }
  }
  ```
</Accordion>


## Step 5. Integrate with webhooks

You can integrate with webhooks to track the status of your payment. For more information, refer to the [Payouts Webhooks](doc:payouts-webhooks).
