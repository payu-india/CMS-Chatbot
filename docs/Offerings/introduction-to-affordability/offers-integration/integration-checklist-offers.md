---
title: Integration Checklist - Offers
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
Use the following checklist to ensure your Offers integration using Merchant Hosted Checkout is complete:

* [ ] Completed all the required checkout details have been collected correctly on your website and validated.

<Callout icon="📘" theme="info">
  **Reference**: For more information on collecting and submitting the request parameter, refer to:

  * [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website)

  * [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted)
</Callout>

Verified the Response from PayU. For more information on responses, refer to [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)

*   [ ] Completed the callback response (reverse hashing) is not tampered with. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

* [ ] Confirmed the transaction status on the Server-side, if the callback fail. Use Webhooks for hearing callbacks. For more information, refer to [Verify Payment API](ref:verify_payment_api) and [Webhooks](doc:webhooks).

*   [ ] Completed the integration on Production. The endpoint for the  Production environment is:

  ```
  <https://secure.payu.in/>
  ```
