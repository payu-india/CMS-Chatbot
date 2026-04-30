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

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`Failure`', 'Card No is Invalid. Please check and initiate again', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'CVV is Invalid. Please check and initiate again', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Incorrect Card Details. Please recheck CVV or expiry and try again', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Card not eligible. Please try another card', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Issuing bank server down. Please try in some time or try another card', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Card cannot be used. Please try another card', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Invalid details. Please try another card', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Card cannot be used. Please try another card', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
    ['`Failure`', 'Card Association Error', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>

<br />

