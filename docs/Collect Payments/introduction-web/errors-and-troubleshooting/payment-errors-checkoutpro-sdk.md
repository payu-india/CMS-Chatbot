---
title: CheckoutPro SDK payment errors
excerpt: CheckoutPro SDK payment and integration errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: CheckoutPro SDK payment errors
  description: CheckoutPro SDK payment and integration errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **CheckoutPro SDK Troubleshooting**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_CHECKOUTPRO_SDK_BEGIN -->

## Error reference

Rows categorized: **2**.

<SearchableTable
    headers={['Error code / type', 'Description', 'Recommended fix']}
    rows={[
    ['`Some Problem Occurred Issue`', 'Correct the payment request parameters.', 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'],
    ['`Something Went Wrong`', 'Whitelist merchant VPAs for Google Pay onboarding.', 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'],
  ]}
    placeholder="Search"
  />


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_CHECKOUTPRO_SDK_END -->
