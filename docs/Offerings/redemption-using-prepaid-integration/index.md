---
title: Payment using Prepaid
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Redemption with only Prepaid platform

Merchant has the option to only opt for PayU Prepaid services only. So, in those cases, the following APIs will be used for Redemption from the wallet

* <Anchor label="Retrieve Customer Record API" target="_blank" href="https://docs.payu.in/reference/retrieve-customer-record-api">Retrieve Customer Record API</Anchor>: This API will be required by Merchants to fetch and balance present in the customer wallet.
* <Anchor label="Unload API" target="_blank" href="https://docs.payu.in/reference/unload-api">Unload API</Anchor>: This API will be used to debit the customer wallet.
* <Anchor label="Load API" target="_blank" href="https://docs.payu.in/reference/load-api-closed-loop-wallet/">Load API</Anchor>: This API will be used to load the money in the wallet as part of refunds.
* <Anchor label="Check Status API" target="_blank" href="https://docs.payu.in/reference/check-status-api">Check Status API</Anchor>: This will be required to check status of the load API used in the top-up journey.

## Redemption with Prepaid and PayU as PG

This integration will be done with PayU’s PG, so separate credentials/keys will be required to integrate. For more information, refer to the folliowing:

* <Anchor label="PayU Hosted Check-out Integration" target="_blank" href="https://docs.payu.in/docs/pay-hosted-checkout-merchant-integration-merchant-wallet">PayU Hosted Check-out Integration</Anchor>
* <Anchor label="Merchant Hosted Checkout Integration" target="_blank" href="https://docs.payu.in/docs/merchant-hosted-checkout-integration-merchant-wallet">Merchant Hosted Checkout Integration</Anchor>
* [SDK-Based Integration](https://docs.payu.in/docs/sdk-based-integration-merchant-wallet)

<Callout icon="📘" theme="info">
  **Note**: The following keys required by merchant:

  * Merchant ID
  * Key
  * Salt
</Callout>