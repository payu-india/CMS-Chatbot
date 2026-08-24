---
title: CheckoutPro SDK Payment Errors
excerpt: >-
  Go through the CheckoutPro SDK payment and integration errors and their
  recommended fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are checkoutPro SDK payment and integration errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`Some Problem Occurred Issue`',
        'description': 'Correct the payment request parameters.',
        'recommended_fix': 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'
      },
      {
        'bank_code': '`Something Went Wrong`',
        'description': 'Whitelist merchant VPAs for Google Pay onboarding.',
        'recommended_fix': 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'
      }
    ]}
  />
</Accordion>
