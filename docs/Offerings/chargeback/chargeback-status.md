---
title: Chargeback Status
deprecated: false
hidden: false
metadata:
  robots: index
---
The chargeback status are used while processing a chargeback. You can find the **Chargeback Status** field in the Chargeback home page while filtering cases as in the following screenshot:

<Image align="center" src="https://files.readme.io/46155e43504169f74683d610eece923b634a3c19bfaac7b5be0f04a90d7b85b7-chargeback_status_highlighted.png" />

| Chargeback Status         | Details                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pending Response          | New chargeback notification has been submitted to the merchant for his response                                                                            |
| Pending Doc Review        | The merchant has accepted/disputed the chargeback raised with relevant documentation(if applicable)                                                        |
| Submitted to bank         | The chargeback has been submitted to the acquiring bank as a part of the representment package                                                             |
| Insufficient Document     | The chargeback has been rejected for lack of sufficient documentation for representment                                                                    |
| Closed Customer Favour    | The chargeback has been closed in the customer favour. The money has been returned to the customer.                                                        |
| Closed in merchant favour | The chargeback has been closed in the merchant favour. No money is debited if any money is debited then the same is reversed back to the merchant account. |
| Closed under fraud        | Closed under fraud liability                                                                                                                               |
