---
title: Chargeback Types
deprecated: false
hidden: false
metadata:
  robots: index
---
The chargeback types are used while processing a chargeback. You can find the chargeback type in the Chargeback home as in the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/fc20984bfb1fb7e4d72948c8747e513a90034ea10e1015e2b6e7bb2d154e0d07-chargeback_type_highlighted.png" className="border" />

| Chargeback Type | Details                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chargeback      | With this chargeback type, the issuer has returned the disputed transaction to the acquirer with the reason                                                                                         |
| Pre-arb         | If the customer rejects the chargeback then the issuer escalates the chargeback into prearbitration case with relevant documentation                                                                |
| Arbitration     | With the pre-arbitration case, If the acquirer rejects the pre-arbitration case then the issuer can escalate the case to an arbitration case                                                        |
| Compliance      | These are compliance case requests which are raised by regulatory authorities for information. Also used if the issuer has no option to raise a chargeback since the chargeback window has expired. |
| Good Faith      | The chargeback is handled outside the official chargeback channel that involves the card network.                                                                                                   |
