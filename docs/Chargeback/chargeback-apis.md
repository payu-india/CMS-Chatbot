---
title: Chargeback APIs
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
The following  APIs are used in chargeback:

| API                                                                           | Description                                                                                                                       |
| :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [Read Chargeback API](https://docs.payu.in/reference/read-chargeback-api)     | Responds with the all the chargebacks corresponding to the merchant.                                                              |
| [Read Reasons API](https://docs.payu.in/reference/read-reasons-api)           | Lists all the reasons required for the merchant to provide in order to accept or contest the chargeback.                          |
| [Accept Chargeback API](https://docs.payu.in/reference/accept-chargeback-api) | Accept the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID.            |
| [Contest Chargeback API](ref:contest-chargeback-api)                          | Allows to contest the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID. |