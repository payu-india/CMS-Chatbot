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

| **Codes** | **Status**   | **Message**                                                                                           |
| --------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| 100       | SUCCESS      | Refund Successful                                                                                     |
| 101       | PENDING      | Refund Successful                                                                                     |
| 102       | QUEUED       | Refund Queued                                                                                         |
| 103       | REJECT       | Request rejected on reconfirmation                                                                    |
| 104       | RECONFIRM    | Confirmation Required                                                                                 |
| 105       | FAILURE      | Invalid Amount                                                                                        |
| 106       | FAILURE      | Token already exists                                                                                  |
| 107       | FAILURE      | Upgraded to refund, //only in case of Citi cancel failure                                             |
| 108       | FAILURE      |                                                                                                       |
| 109       | FAILURE      | The request is already logged                                                                         |
| 110       | FAILURE      | More than one partial refund of Maestro transactions are not allowed                                  |
| 111       | FAILURE      | Invalid transaction status                                                                            |
| 113       | FAILURE      | Invalid Amount – Chargeback of amount 20.00 present, the remaining refundable amount is 50.00         |
| 115       | FAILURE      | Invalid status to be uploaded                                                                         |
| 116       | FAILURE      | Transaction not found                                                                                 |
| 117       | FAILURE      | The amount does not match                                                                             |
| 119       | FAILURE      | No such Request Found                                                                                 |
| 120       | FAILURE      | Transaction lock could not be obtained                                                                |
| 123       | FAILURE      | The request set as pending – requires manual follow-up                                                |
| 126       | IN\_PROGRESS | IN\_PROGRESS                                                                                          |
| 127       | REQUESTED    | REQUESTED                                                                                             |
| 214       | FAILURE      | Same amount same transaction within 5 minutes                                                         |
| 225       | PENDING      | Overdraft has occurred. Kindly recheck the status tomorrow                                            |
| 226       | PENDING      | Capture has been initiated today. Please check for refund status tomorrow                             |
| 227       | FAILURE      | Transactions with the same amount and same token are not allowed                                      |
| 230       | FAILURE      | FAILURE – Purged Transaction. Refund request requires manual follow-up                                |
| 231       | FAILURE      | Hold settlement                                                                                       |
| 232       | FAILURE      | FAILURE – Refund could not be initiated. Either refunds are not supported or need manual intervention |
| 233       | FAILURE      | BLOCKED – Refund/Cancel Blocked From Merchant Panel. Contact KM.                                      |
| 234       | FAILURE      | BLOCKED – Refund/Cancel Blocked From Merchant Panel And API. Contact KM.                              |
| 235       | FAILURE      | BLOCKED – Refund/Cancel Blocked. Contact KM.                                                          |
| 236       | FAILURE      | STATUS\_REFUND\_NOT\_POSSIBLE                                                                         |
| 237       | FAILURE      | Validation Failure for {key\_name}. Special Characters Not Allowed                                    |
| 238       | FAILURE      | Validation Failure for {key\_name}. Mandatory Field.                                                  |
| 239       | FAILURE      | API-based alternate instant refunds not activated.                                                    |
| 250       | FAILURE      | FAILURE – Refund Failed On Uploading Successful Chargeback                                            |
| 251       | FAILURE      | Refund Blocked for this PGMID by Bank                                                                 |
| 301       | FAILURE      | FAILURE – Capture already successful for this transaction                                             |
| 302       | FAILURE      | FAILURE – Please try after some time                                                                  |
| 303       | FAILURE      | FAILURE – Amount greater than the maximum capturable amount                                           |
| 304       | FAILURE      | FAILURE – Amount less than allowed                                                                    |
| 305       | FAILURE      | FAILURE – Amount more than allowed                                                                    |
| 306       | FAILURE      | FAILURE – Invalid amount tolerance configuration                                                      |
| 424       | FAILURE      | FAILURE – Transaction upgraded to capture/refund.                                                     |
| 500       | FAILURE      | Some Exception Occurred                                                                               |
| 501       | FAILURE      | Successfully Updated,//used in case of updating refunds thru file                                     |
| 502       | FAILURE      | Failed to update                                                                                      |