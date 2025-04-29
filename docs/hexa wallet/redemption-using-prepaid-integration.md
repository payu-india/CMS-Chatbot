---
title: Payment using Prepaid
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
## Redemption with only Prepaid platform

Merchant has the option to only opt for PayU Prepaid services only. So, in those cases, the following APIs will be used for Redemption from the wallet

* [Retrieve Customer Record API](ref:retrieve-customer-record-api): This API will be required by Merchants to fetch and balance present in the customer wallet.
* [Unload API](ref:unload-api): This API will be used to debit the customer wallet.
* [Load API](ref:l): This API will be used to load the money in the wallet as part of refunds.
* [Check Status API](ref:check-status-api): This will be required to check status of the load API used in the top-up journey.

## Redemption with Prepaid and PayU as PG

This integration will be done with PayU’s PG, so separate credentials/keys will be required to integrate. For more information, refer to the folliowing:

* [PayU Hosted Check-out Integration](doc:pay-hosted-checkout-merchant-integration-merchant-wallet)
* [Merchant Hosted Checkout Integration](doc:merchant-hosted-checkout-integration-merchant-wallet)
* [SDK-Based Integration](doc:sdk-based-integration-merchant-wallet)

> 📘 Note:
>
> The following keys required by merchant:
>
> * Merchant ID
> * Key
> * Salt
