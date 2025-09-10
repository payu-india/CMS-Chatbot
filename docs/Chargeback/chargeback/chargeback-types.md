---
title: Chargeback Types
deprecated: false
hidden: false
metadata:
  robots: index
---
Any of the following chargeback type can be found in the response of the following Chargeback APIs only:

* [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api)
* [Accept/Contest Chargeback API](https://docs.payu.in/reference/accept-contest-chargeback-api)
* [Contest Chargeback API](https://docs.payu.in/reference/contest-chargeback-api)

| Chargeback Type | Description                                                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chargeback      | With this chargeback type, the issuer has returned the disputed transaction to the acquirer with the reason.                                                                                        |
| Pre-arb         | If the customer rejects the chargeback then the issuer escalates the chargeback into prearbitration case with relevant documentation.                                                               |
| Arbitration     | With the pre-arbitration case, if the acquirer rejects the pre-arbitration case then the issuer can escalate the case to an arbitration case.                                                       |
| Compliance      | These are compliance case requests which are raised by regulatory authorities for information. Also used if the issuer has no option to raise a chargeback since the chargeback window has expired. |
| Good Faith      | The chargeback is handled outside the official chargeback channel that involves the card network.                                                                                                   |
