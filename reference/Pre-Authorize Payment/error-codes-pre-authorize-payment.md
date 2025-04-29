---
title: Error Codes - Pre-Authorize Payment
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
| Scenario                                                           | Error code | String                                          | Recommendations                                                                                               |
| ------------------------------------------------------------------ | ---------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Success                                                            | 101        |                                                 |                                                                                                               |
| Queue State                                                        | 102        | Capture Request Queued                          |                                                                                                               |
| Failed Transaction                                                 | 109        | Capture failed                                  |                                                                                                               |
| Capture Transaction is Queued & acknowledged at PayU’s end         | 102        | Capture Request Queued                          | Advice is to invoke the check action status API to get final status                                           |
| Capture transaction is in successful state                         | 100        | Capture Request Queued                          | Transaction is in successful state                                                                            |
| If multiple captures request sent corresponding to one transaction | 109        | Capture failed                                  | PayU’s has idempotency check which means PayU will not do multiple captures corresponding to one transaction. |
| If request get time out                                            | -          | Capture Request Queued                          | Recommendation is to retrigger the capture call.                                                              |
| Rate Limit breached                                                | -          | Requests limit reached                          |                                                                                                               |
| Transaction not exist                                              | -          | Transaction not exists                          | To check if auth is successfully done or if correct merchant transaction id is sent                           |
| Failure                                                            | 106        |  Token already exists.                          |                                                                                                               |
| Failure                                                            | 108        |                                                 |                                                                                                               |
| Failure                                                            | 109        | Request is already logged                       |                                                                                                               |
| Failure                                                            | 111        | Invalid transaction status                      |                                                                                                               |
| Failure                                                            | 116        | Transaction Not Found                           |                                                                                                               |
| Failure                                                            | 120        | Transaction lock could not be obtained.         |                                                                                                               |
| Failure                                                            | 301        | Capture already successful for this transaction |                                                                                                               |
| Failure                                                            | 303        | Amount greater than maximum capturable amount   |                                                                                                               |
| Failure                                                            | 304        | Amount less than allowed                        |                                                                                                               |
| Failure                                                            | 305        | Amount more than allowed                        |                                                                                                               |
| Failure                                                            | 306        | Invalid amount tolerance configuration          |                                                                                                               |