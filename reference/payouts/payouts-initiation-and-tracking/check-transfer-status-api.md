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

|                            |                                                                |
| -------------------------- | -------------------------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/payment/listTransactions>    |
| **Production Environment** | <https://payout.payumoney.com/payout/payment/listTransactions> |

<details><summary>Sample request</summary>

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

<details><summary>Sample response</summary>

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

<details><summary> Response parameters description</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n- **0** - If web service call succeeded.\n- **1** - If web service call failed",
    "1-0": "msg",
    "1-1": "This parameter returns the message to convey success or failure.",
    "2-0": "code",
    "2-1": "This parameter returns the code.",
    "3-0": "data",
    "3-1": "This parameter returns the transfer status in a JSON format. Refer the [Description of data Parameter Fields](https://devguide.vercel.app/payouts-api/payouts-initiation-and-tracking/check-transfer-status-api/#data)"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


### Description of data parameter fields

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "noOfPages",
    "0-1": "The field contains the number of pages with the transfer status details.",
    "1-0": "totalElements",
    "1-1": "The field contains the number of elements with the transfer status details.",
    "2-0": "currentPage",
    "2-1": "The field contains the current page that is returned.",
    "3-0": "totalAmount",
    "3-1": "The field contains the total amount of the transaction.",
    "4-0": "succesTxn",
    "4-1": "The field contains the code whether transaction is successful.",
    "5-0": "pendingTxn",
    "5-1": "This field contains the code whether transaction is pending.",
    "6-0": "transactionDetails",
    "6-1": "This field contains the following transaction details in an JSON format and each object contains the following details:  \n  \n- **txnId**: Contains the transaction ID from PayU\n- **batchId**: Contains the batch ID provided by merchant at the time of initiating transfer\n- **merchantRefId**: merchantRefId provided by merchant at the time of initiating transfer\n- purpose: Contains the purpose provided by merchant at the time of initiating transfer\n- **amount**: The amount transferred for this transaction\n- **txnStatus**: Contains the transaction status for this transaction. For list of transaction status, refer to [Transaction Status](https://devguide.vercel.app/payouts-api/payouts-initiation-and-tracking/check-transfer-status-api/#Transaction_Status)  sub-section\n- **txnSubStatus**: Contains the sub-status of the transaction\n- **txnSource**: Contains the source of transaction from where it is initiated\n- **txnDate**: The date when transaction initiated\n- **scheduledTxnDate**: The date when transactions is scheduled\n- **payuTransactionRefNo**: Contains the PayU transaction reference number.\n- **beneficiaryName**: Contains the name of the beneficiary passed in request\n- **beneficiaryCardNo**: Contains the name of the beneficiary passed in request\n- **msg**: Contains the response message for transaction\n- **responseCode**: Contains the response code from PayU, For the list of response codes, refer to [Payouts Error Codes](https://devguide.payu.in/payouts-api/miscellaneous-2/payouts-error-codes/)\n- **transferType**: Contains the mode of the transfer used while initiating request (IMPS,NEFT,UPI)\n- **bankTransactionRefNo**: Contains the bank transfer reference number\n- **nameWithBank**: Contains the beneficiary name as per bank\n- **lastStatusUpdateDate**: Contains the transfer terminating state time (Transfer success or failure time)\n- succeedOn\n- **fee**: the fee charged for transaction. This is basis the agreement signed by merchant\n- **tax**:applicable on fee as applicable\n- **txnStatusDescription**: show description of transaction failed/queued reason\n- **custom1**: entered by merchant in Initiate transfer API\n- **custom2**: entered by merchant in Initiate transfer API\n- **custom2**: entered by merchant in Initiate transfer API\n- **nameMatch**: Will return name match percentage for penny drop with name match transaction"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    null,
    null
  ]
}
[/block]


This field contains the following transaction details in an JSON format and each object contains the following details:  
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

<details>

## Headers and request parameters

> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

> 📘 Reference:
> 
> For sample request and response, refer to [Sample Request and Response for Initiation & Tracking APIs](ref:sample-request-and-response-for-initiation-tracking-apis#check-transfer-status-api).

<details><summary>Additional Info for request parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "transferStatus  \n`optional`",
    "0-1": "`String` Search by status of transfer. Merchant can get all success or failure transaction of the day to reconcile. The transfer status can be any of the following:  \n  \n- QUEUED/SCHEDULED\n- IN_PROGRESS\n- PENDING\n- FAILED  \n  Refer to the [Transfer Status](#transfer-status) table for the description of each status.",
    "0-2": "success",
    "1-0": "filterBySucceedOn\\]`\noptional`",
    "1-1": "`Boolean` This parameter must be passed **True** along with **dateFrom** and **dateTo** parameters, to filter the transactions that were successful between these dates.  \n **Note**: For this filter, date range can be maximum of seven days.",
    "1-2": " "
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


</details>