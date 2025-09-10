---
title: Chargeback Status List
deprecated: false
hidden: false
metadata:
  robots: index
---
Any of the status listed in the following table can be found in response of the following Chargeback APIs only:

* [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api)
* [Accept/Contest Chargeback API](https://docs.payu.in/reference/accept-contest-chargeback-api)
* [Contest Chargeback API](https://docs.payu.in/reference/contest-chargeback-api)

| Chargeback Status         | Description                                                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ME Comm Sent              | New chargeback notification has been submitted to the merchant for his response.                                                                              |
| ME Comm Received          | The merchant has accepted/disputed the chargeback raised with relevant documentation (if applicable).                                                         |
| Bank Comm Sent            | The chargeback has been submitted to the acquiring bank as a part of the representment package.                                                               |
| Doc Rejected              | The chargeback has been rejected for lack of sufficient documentation for representment.                                                                      |
| Closed in Customer favour | The chargeback has been closed in the customer favour. The money has been returned to the customer.                                                           |
| Closed in Merchant favour | The chargeback has been closed in the merchant favour. No money is debited; if any money was debited, then the same is reversed back to the merchant account. |

<br />
