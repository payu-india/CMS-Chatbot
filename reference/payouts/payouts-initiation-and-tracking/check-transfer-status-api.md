---
title: Check Transfer Status API
excerpt: ''
api:
  file: payouts-api-7.json
  operationId: CheckTransferStatusAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Check Transfer Status** API will return the status of the transfers initiated by the merchant.

HTTP Method: **POST**

**Environment**

|                            |                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | [https://uatoneapi.payu.in/payout/payment/listTransactions](https://uatoneapi.payu.in/payout/payment/listTransactions)       |
| **Production Environment** | [https://payout.payumoney.com/payout/payment/listTransactions](https://payout.payumoney.com/payout/payment/listTransactions) |

<details>
  <summary>Sample request</summary>

  ```curl
  curl -X POST \
   https://test.payumoney.com/payout/payment/listTransactions \
   -H 'authorization: Bearer 2678f236346281e6029e3430da1a721af29bb3546d6acbc27e6aadd7fca72605' \
   -H 'cache-control: no-cache' \
   -H 'content-type: application/x-www-form-urlencoded' \
   -H 'payoutmerchantid: 1111122' \
   -d 'transferStatus=QUEUED&from=01%2F01%2F2019&to=01%2F01%2F2019&page=1&pageSize=100&merchantRefId=&batchId=1'
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
</details>

<details>
  <summary> Response parameters description</summary>

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
      <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the status of web service call. The status can be any of the following:  </p>
    <ul>
    <li><strong>0</strong> - If web service call succeeded.</li>
    <li><strong>1</strong> - If web service call failed</li>
    </ul>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>msg</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the message to convey success or failure.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the code.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>data</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter returns the transfer status in a JSON format. Refer the <a href="https://devguide.vercel.app/payouts-api/payouts-initiation-and-tracking/check-transfer-status-api/#data">Description of data Parameter Fields</a></p>
    </td>
    </tr>
    </tbody>
    </table>
  `}</HTMLBlock>

  ### Description of data parameter fields

  <HTMLBlock>{`
    <table style="width: 100%; border-collapse: collapse;">
    <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>noOfPages</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The field contains the number of pages with the transfer status details.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>totalElements</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The field contains the number of elements with the transfer status details.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>currentPage</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The field contains the current page that is returned.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>totalAmount</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The field contains the total amount of the transaction.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>succesTxn</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The field contains the code whether transaction is successful.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pendingTxn</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the code whether transaction is pending.</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDetails</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the following transaction details in an JSON format and each object contains the following details:  </p>
    <ul>
    <li><strong>txnId</strong>: Contains the transaction ID from PayU</li>
    <li><strong>batchId</strong>: Contains the batch ID provided by merchant at the time of initiating transfer</li>
    <li><strong>merchantRefId</strong>: merchantRefId provided by merchant at the time of initiating transfer</li>
    <li>purpose: Contains the purpose provided by merchant at the time of initiating transfer</li>
    <li><strong>amount</strong>: The amount transferred for this transaction</li>
    <li><strong>txnStatus</strong>: Contains the transaction status for this transaction. For list of transaction status, refer to <a href="https://devguide.vercel.app/payouts-api/payouts-initiation-and-tracking/check-transfer-status-api/#Transaction_Status">Transaction Status</a>  sub-section</li>
    <li><strong>txnSubStatus</strong>: Contains the sub-status of the transaction</li>
    <li><strong>txnSource</strong>: Contains the source of transaction from where it is initiated</li>
    <li><strong>txnDate</strong>: The date when transaction initiated</li>
    <li><strong>scheduledTxnDate</strong>: The date when transactions is scheduled</li>
    <li><strong>payuTransactionRefNo</strong>: Contains the PayU transaction reference number.</li>
    <li><strong>beneficiaryName</strong>: Contains the name of the beneficiary passed in request</li>
    <li><strong>beneficiaryCardNo</strong>: Contains the name of the beneficiary passed in request</li>
    <li><strong>msg</strong>: Contains the response message for transaction</li>
    <li><strong>responseCode</strong>: Contains the response code from PayU, For the list of response codes, refer to <a href="https://devguide.payu.in/payouts-api/miscellaneous-2/payouts-error-codes/">Payouts Error Codes</a></li>
    <li><strong>transferType</strong>: Contains the mode of the transfer used while initiating request (IMPS,NEFT,UPI)</li>
    <li><strong>bankTransactionRefNo</strong>: Contains the bank transfer reference number</li>
    <li><strong>nameWithBank</strong>: Contains the beneficiary name as per bank</li>
    <li><strong>lastStatusUpdateDate</strong>: Contains the transfer terminating state time (Transfer success or failure time)</li>
    <li>succeedOn</li>
    <li><strong>fee</strong>: the fee charged for transaction. This is basis the agreement signed by merchant</li>
    <li><strong>tax</strong>:applicable on fee as applicable</li>
    <li><strong>txnStatusDescription</strong>: show description of transaction failed/queued reason</li>
    <li><strong>custom1</strong>: entered by merchant in Initiate transfer API</li>
    <li><strong>custom2</strong>: entered by merchant in Initiate transfer API</li>
    <li><strong>custom2</strong>: entered by merchant in Initiate transfer API</li>
    <li><strong>nameMatch</strong>: Will return name match percentage for penny drop with name match transaction</li>
    </ul>
    </td>
    </tr>
    </tbody>
    </table>
  `}</HTMLBlock>

  This field contains the following transaction details in an JSON format and each object contains the following details:\
  e for penny drop with name match transaction|

  #### Transaction status Description

  | **Status**          | **Description**                                                                                                                                                                                                                       |
  | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | QUEUED              | It will be first state once we get transaction request from merchant. If merchant is not having enough balance in his account txn will be in queued state only till he/she do deposit in virtual account. Check disable queued payout |
  | IN\_PROGRESS        | Transaction picked for processing with bank                                                                                                                                                                                           |
  | PENDING             | PayU has received pending status from bank. Final status will be updated once PayU get success or failure from bank. Reconciliation for these type of transaction happen after every 5 min.                                           |
  | FAILED              | Transaction got failed at bank end. Check error message and fix if anything wrong in request or else retry.                                                                                                                           |
  | SUCCESS             | Transaction got success. Amount is transferred to customer account                                                                                                                                                                    |
  | WAITING\_FOR\_RETRY | Transaction is waiting to be picked again. You will get this status only in case bank / beneficiary bank server is down and you have passed retry as true or empty while calling transfer API.                                        |
</details>

## Headers and request parameters

> 📘 Note:
>
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

> 📘 Reference:
>
> For sample request and response, refer to [Sample Request and Response for Initiation & Tracking APIs](ref:sample-request-and-response-for-initiation-tracking-apis#check-transfer-status-api).

<details>
  <summary>Additional Info for request parameters</summary>

  <HTMLBlock>{`
    <table style="width: 100%; border-collapse: collapse;">
    <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>transferStatus<br><code>optional</code></p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Search by status of transfer. Merchant can get all success or failure transaction of the day to reconcile. The transfer status can be any of the following:  </p>
    <ul>
    <li>QUEUED/SCHEDULED</li>
    <li>IN_PROGRESS</li>
    <li>PENDING</li>
    <li>FAILED<br>Refer to the <a href="#transfer-status">Transfer Status</a> table for the description of each status.</li>
    </ul>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>success</p>
    </td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>filterBySucceedOn]<code> optional</code></p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This parameter must be passed <strong>True</strong> along with <strong>dateFrom</strong> and <strong>dateTo</strong> parameters, to filter the transactions that were successful between these dates.<br> <strong>Note</strong>: For this filter, date range can be maximum of seven days.</p>
    </td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
    </td>
    </tr>
    </tbody>
    </table>
  `}</HTMLBlock>
</details>