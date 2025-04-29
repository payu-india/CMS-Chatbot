---
title: Error codes for QR APIs
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
| Status | Message                                                                                   | Error Code | Description                                                                    |
| :----- | :---------------------------------------------------------------------------------------- | :--------- | :----------------------------------------------------------------------------- |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"  | -          | Command name is empty                                                          |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"  | -          | Merchant key is empty                                                          |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"  | -          | Hash is empty                                                                  |
| failed | transactionId is                                                                          | E2003      | -                                                                              |
| failed | transactionId is longer than 40                                                           | E2017      | -                                                                              |
| failed | transactionId is not alphanumeric                                                         | E2018      | -                                                                              |
| failed | Amount is empty or less than 1                                                            | E2004      | -                                                                              |
| failed | Amount is less than 1                                                                     | E2006      | -                                                                              |
| failed | No vpa exists against given merchant. Please contact sales support                        | E2007      | -                                                                              |
| failed | Incoming VPA Does Not Match with registered vpa. Please provide a valid vpa               | E2008      | -                                                                              |
| failed | Expiry Time cannot be less than 1                                                         | E2009      | -                                                                              |
| failed | PG Params are missing. Please contact sales support                                       | E2015      | Mastercard, Rupay & Visa IDs are missing for the merchant                      |
| failed | QR Generation Failed                                                                      | E2013      | Couldn't generate QR due to internal issues                                    |
| failed | qr already exists but amount does not match with existing qr amount                       | E2010      | Couldn't match the incoming amount with existing QR's amount                   |
| failed | qr already exists but vpa does not match with existing qr vpa                             | E2011      |                                                                                |
| failed | QR with the given transactionId has been already used. Please provide a new TransactionId | E2012      | when status of transaction with the sent transactionId is success              |
| failed | Duplicate Request                                                                         | E2025      | when multiple qr generation requests are sent with same txnid at the same time |