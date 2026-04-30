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
These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **CheckoutPro SDK Troubleshooting**.

<br />

Use this page with [Payment Failed or Declined](doc:payment-failed-declined)  for debugging guidance and retry handling.

<br />

## Error reference

<br />

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`Some Problem Occurred Issue`', 'Correct the payment request parameters.', 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'],
    ['`Something Went Wrong`', 'Whitelist merchant VPAs for Google Pay onboarding.', 'Apply the SDK-specific solution, verify environment/configuration flags, and retest the integration flow.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
