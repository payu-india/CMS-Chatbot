---
title: APIs used Integration
deprecated: false
hidden: false
icon: far fa-cash-register
metadata:
  title: APIs used in Chargeback Integration
  robots: index
---
The following  APIs are used in chargeback:

| API                                                                           | Purpose                                                                                                                           |
| :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [Read Chargeback API](https://docs.payu.in/reference/read-chargeback-api)     | Responds with the all the chargebacks corresponding to the merchant.                                                              |
| [Read Reasons API](https://docs.payu.in/reference/read-reasons-api)           | Lists all the reasons required for the merchant to provide in order to accept or contest the chargeback.                          |
| [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api) | Accept the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID.            |
| [Accept/Contest Chargeback API](ref:accept-contest-chargeback-api)            | Accept or context a chargeback by providing appropriate reasons in the request body against the chargeback and merchant ID.       |
| [Contest Chargeback API](ref:contest-chargeback-api)                          | Allows to contest the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID. |

<br />