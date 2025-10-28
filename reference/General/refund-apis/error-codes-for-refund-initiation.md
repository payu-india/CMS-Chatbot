---
title: Error Codes for Refund Initiation
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following are possible errors and error codes for transaction initiation.


|   Status Code | Status                                                                | Message                                                                                     |
|--------------:|:---------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
|           100 | SUCCESS                                                                    |                                                                                             |
|           101 | PENDING                                                                    |                                                                                             |
|           102 | QUEUED                                                                     |                                                                                             |
|           103 | REJECT                                                                     | Request rejected on reconfirmation                                                          |
|           104 | RECONFIRM                                                                  | Confirmation required                                                                       |
|           105 | Refund FAILURE                                                             | Invalid amount                                                                              |
|           106 | Refund FAILURE                                                             | Token already exists.                                                                       |
|           107 | Refund FAILURE                                                             | Upgraded to refund                                                                          |
|           108 | Refund FAILURE                                                             |                                                                                             |
|           109 | Refund FAILURE                                                             | Request is already logged                                                                   |
|           110 | Refund FAILURE                                                             | More than one partial refund of Maestro transactions are not allowed                        |
|           111 | Refund FAILURE                                                             | Invalid transaction status                                                                  |
|           112 | RISK_QUEUED                                                                |                                                                                             |
|           113 | Refund FAILURE                                                             | Invalid Amount - Chargeback of amount present                                               |
|           115 | Refund FAILURE                                                             | Invalid status to be updated                                                                |
|           116 | Refund FAILURE                                                             | Transaction Not Found                                                                       |
|           117 | Refund FAILURE                                                             | Amount Does not Match                                                                       |
|           119 | Refund FAILURE                                                             | No such Request Found                                                                       |
|           120 | Refund FAILURE                                                             | Transaction lock could not be obtained.                                                     |
|           121 | Refund FAILURE                                                             | Incorrect/Empty value passed in retry                                                       |
|           122 | APPROVAL PENDING                                                           |                                                                                             |
|           123 | Refund FAILURE                                                             | Request set as pending - requires manual follow-up                                          |
|           124 | Refund FAILURE                                                             | Input Data missing                                                                          |
|           125 | Refund FAILURE                                                             | Merchant Failed the pending refund                                                          |
|           126 | IN_PROGRESS                                                                |                                                                                             |
|           127 | REQUESTED                                                                  |                                                                                             |
|           128 | Refund FAILURE                                                             | Partial refunds not allowed                                                                 |
|           129 | Refund FAILURE                                                             | Remark is mandatory for retry 0                                                             |
|           130 | Refund FAILURE                                                             | Refunds not allowed after                                                                   |
|           214 | Refund FAILURE                                                             | Two refunds of same amount for same transaction within 5 minutes are not allowed            |
|           225 | PENDING                                                                    | Overdraft has occurred. Kindly recheck the status tomorrow.                                 |
|           226 | PENDING                                                                    | Capture has been initiated today. Please check for refund status tomorrow.                  |
|           227 | Refund FAILURE                                                             | Transactions with same amount and same token not allowed                                    |
|           230 | Refund FAILURE                                                             | Purged Transaction. Refund request requires manual follow-up                                |
|           231 | Refund could not be initiated due to some internal error                   |                                                                                             |
|           232 | Refund FAILURE                                                             | Refund could not be initiated. Either refunds are not supported or need manual intervention |
|           233 | BLOCKED                                                                    | Refund/Cancel Blocked From Merchant Panel. Contact KM.                                      |
|           234 | BLOCKED                                                                    | Refund/Cancel Blocked From Merchant Panel And API. Contact KM.                              |
|           235 | BLOCKED                                                                    | Refund/Cancel Blocked. Contact KM.                                                          |
|           236 | Refund FAILURE                                                             | Refund not possible on this transaction                                                     |
|           237 | Validation Failure for \{key_name}. Special Characters Not Allowed          |                                                                                             |
|           238 | Validation Failure for \{key_name}. Mandatory Field.                        |                                                                                             |
|           239 | API based alternate instant refunds not activated.                         |                                                                                             |
|           240 | Refund FAILURE                                                             | Store card failed                                                                           |
|           241 | Refund is not supported by the bank because the payment is more than days. |                                                                                             |
|           242 | Refund FAILURE                                                             | Bank Code Not Supported. Raise it to PayU support team                                      |
|           243 | Virtual account setup to process instant refund is incomplete              |                                                                                             |
|           244 | Beneficiary Code for Virtual Account Not Set                               |                                                                                             |
|           245 | BBPS transaction is not successful                                         |                                                                                             |
|           246 | value is Invalid for the Merchant SKU.                                     |                                                                                             |
|           247 | not allowed as no offers found for the SKU.                                |                                                                                             |
|           248 | BAL_CHECK_INIT                                                             |                                                                                             |
|           249 | RETRY                                                                      |                                                                                             |
|           250 | Refund FAILURE                                                             | Refund Failed On Uploading Successful Chargeback                                            |
|           251 | Refund Blocked for this PGMID by Bank                                      |                                                                                             |
|           252 | Refund FAILURE                                                             | Refunds are not allowed from panel for this MID                                             |
|           253 | Refund FAILURE                                                             | Instant refunds invalid mode                                                                |
|           254 | Refund FAILURE                                                             | Remarks cannot contain special characters                                                   |
|           255 | Refund FAILURE                                                             | Token Length Exceeded for Refund                                                            |
|           256 | Refund FAILURE                                                             | Refund not supported on split transactions. Please initiate refund on the order transaction |
|           258 | initiated                                                                  |                                                                                             |
|           259 | REQUESTED_RETRY                                                            |                                                                                             |
|           261 | Refund FAILURE                                                             | Error while processing request                                                              |
|           262 | Refund FAILURE                                                             | Error while processing request                                                              |
|           263 | Refund FAILURE                                                             | Invalid requested amount                                                                    |
|           264 | Refund FAILURE                                                             | Error while processing request                                                              |
|           265 | Refund FAILURE                                                             | Error while processing request                                                              |
|           266 | Refund FAILURE                                                             | Chargeback is pending against this transaction                                              |
|           267 | Refund FAILURE                                                             | Lock acquired on TransactionMetaData                                                        |
|           299 | Refund FAILURE                                                             | Blocking refund initiation for Type A Merchant                                              |
|           301 | Refund FAILURE                                                             | Capture already successful for this transaction                                             |
|           302 | Refund FAILURE                                                             | Please try after some time                                                                  |
|           303 | Refund FAILURE                                                             | Amount greater than maximum capturable amount                                               |
|           304 | Refund FAILURE                                                             | Amount less than allowed                                                                    |
|           305 | Refund FAILURE                                                             | Amount more than allowed                                                                    |
|           306 | Refund FAILURE                                                             | Invalid amount tolerance configuration                                                      |
|           424 | Refund FAILURE                                                             | Transaction upgraded to capture/refund.                                                     |
|           500 | Refund FAILURE                                                             | Some Exception Occurred.                                                                    |
|           501 | Successfully Updated                                                       |                                                                                             |
|           502 | Failed to update                                                           |                                                                                             |
|           270 | FAILURE                                                                    | Transaction not eligible for Instant Refund                                                 |

