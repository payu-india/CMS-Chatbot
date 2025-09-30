---
title: Chargeback Reasons
deprecated: false
hidden: false
metadata:
  robots: index
---
This part of the document explains the various close reasons involved while closing a case in Chargeback lifecycle.

| Close Reason             | Details                                                                                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No Response              | If the merchant does not respond to a chargeback within the TAT, then the Chargeback case gets auto-closed with this reason. Merchants account gets debited.                                         |
| Insufficient doc         | If the merchant does not respond with the requisite documentation for the chargeback basis the TAT, then the Chargeback case will be closed with this reason. Merchants account gets debited.        |
| Bank Denied to represent | If the merchant response does not convince the acquiring bank to represent the case. Merchants account gets debited.                                                                                 |
| Accepted                 | If the merchant accepts the chargeback raised by the customer for the entire amount. Merchants account gets debited and money is returned to the customer.                                           |
| Partially Accepted       | If the merchant accepts the chargeback raised by the customer for a part of the sale amount. Merchants account gets debited for the part sale amount and the part money is returned to the customer. |
| Offline Refund           | If the merchant has already settled with the customer to a different account than that was used for the transaction.                                                                                 |
| Others                   | For any other reasons not listed.                                                                                                                                                                    |
| Accepted By Riskified    | If the chargeback is closed based on the PayU's Fraud liability Program                                                                                                                              |
| Delivered                | The product is accepted to have been delivered to the customer                                                                                                                                       |
| Refunded                 | The entire chargeback amount has already been refunded by the merchant to the customer                                                                                                               |
| Partially Refunded       | Partial chargeback amount has already been refunded by the merchant to the customer                                                                                                                  |

## **Chargeback Types**

| Chargeback Type | Details                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chargeback      | With this chargeback type, the issuer has returned the disputed transaction to the acquirer with the reason                                                                                         |
| Pre-arb         | If the customer rejects the chargeback then the issuer escalates the chargeback into prearbitration case with relevant documentation                                                                |
| Arbitration     | With the pre-arbitration case, If the acquirer rejects the pre-arbitration case then the issuer can escalate the case to an arbitration case                                                        |
| Compliance      | These are compliance case requests which are raised by regulatory authorities for information. Also used if the issuer has no option to raise a chargeback since the chargeback window has expired. |
| Good Faith      | The chargeback is handled outside the official chargeback channel that involves the card network.                                                                                                   |

## **Chargeback Status**

| Chargeback Status        | Details                                                                                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ME Comm Sent             | New chargeback notification has been submitted to the merchant for his response                                                                            |
| ME Comm Received         | The merchant has accepted/disputed the chargeback raised with relevant documentation(if applicable)                                                        |
| Bank Comm Sent           | The chargeback has been submitted to the acquiring bank as a part of the representment package                                                             |
| Doc Rejected             | The chargeback has been rejected for lack of sufficient documentation for representment                                                                    |
| Closed in Customer Favor | The chargeback has been closed in the customer favour. The money has been returned to the customer.                                                        |
| Closed in merchant Favor | The chargeback has been closed in the merchant favour. No money is debited if any money is debited then the same is reversed back to the merchant account. |
