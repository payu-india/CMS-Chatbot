---
title: Chargeback Closure Reasons
deprecated: false
hidden: false
metadata:
  robots: index
---
| Close Reason           | Details                                                                                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No Response            | If the merchant does not respond to a chargeback within the TAT, then the Chargeback case gets auto-closed with this reason. Merchant's account gets debited.      |
| Insufficient doc       | If the merchant does not respond with the requisite documentation for the chargeback basis the TAT, then the case will be closed with this reason. Account debited. |
| Bank Denied to represent | If the merchant response does not convince the acquiring bank to represent the case. Merchant's account gets debited.                                              |
| Accepted               | If the merchant accepts the chargeback raised by the customer for the entire amount. Merchant's account gets debited and money is returned to the customer.         |
| Partially Accepted     | If the merchant accepts the chargeback raised by the customer for a part of the sale amount. Account debited for part; part money returned to the customer.        |
| Offline Refund         | If the merchant has already settled with the customer to a different account than that was used for the transaction.                                               |
| Others                 | For any other reasons not listed.                                                                                                                                  |
| Accepted By Riskified  | If the chargeback is closed based on the PayU's Fraud liability Program                                                                                           |
| Delivered              | The product is accepted to have been delivered to the customer                                                                                                     |
| Refunded               | The entire chargeback amount has already been refunded by the merchant to the customer                                                                             |
| Partially Refunded     | Partial chargeback amount has already been refunded by the merchant to the customer                                                                                |
