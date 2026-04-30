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

## Error Codes and Description

The following table lists errors and their recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
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
</Accordion>

