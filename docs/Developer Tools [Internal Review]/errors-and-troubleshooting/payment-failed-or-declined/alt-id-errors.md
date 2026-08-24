---
title: Alt ID Errors
excerpt: Go through the Alt ID card and token-related payment errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are Alt ID card and token-related payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`Failure`',
        'description': 'Card No is Invalid. Please check and initiate again',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'CVV is Invalid. Please check and initiate again',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Incorrect Card Details. Please recheck CVV or expiry and try again',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Card not eligible. Please try another card',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Issuing bank server down. Please try in some time or try another card',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Card cannot be used. Please try another card',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Invalid details. Please try another card',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      },
      {
        'bank_code': '`Failure`',
        'description': 'Card Association Error',
        'recommended_fix': 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'
      }
    ]}
  />
</Accordion>
