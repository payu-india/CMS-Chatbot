---
title: '[NEW] Collect Payment for Partners'
deprecated: false
hidden: true
metadata:
  robots: index
---
Initiate payment transactions on behalf of your merchants using this Partner Payments endpoint. Supports multiple payment flows including UPI Intent S2S, UPI TPV, and redirect checkout. The following sections provide the sample request/response with request parameters for partner payment with the various integrations:

* [Partner Payment using Hosted Checkout Integration](https://docs.payu.in/reference/new-partner-payment-using-hosted-checkout-integration)​
* [Partner Payment using UPI Intent \[S2S\]](https://docs.payu.in/reference/new-partner-payment-using-upi-intent-s2s)
* [Partner Payment using UPI TPV](https://docs.payu.in/reference/new-partner-payment-using-upi-tpv)

<Callout icon="📘" theme="info">
  ### Notes:

  - You must generate the token using the **Reseller Client Credentials Token&#x20;**&#x41;PI before to be posted in header in the above APIs. For more information, refer to [Reseller Client Credentials Token API](ref:reseller-client-credentials-token)
  - If you are old partner merchant or reseller, you must a set of APIs to generate the token that must be used in above APIs. For more information, refer to [Token Generation Flow used for Partner Payments.](ref:token-generation-flow-for-old-partner-merchants)
</Callout>
