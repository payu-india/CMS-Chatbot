---
title: Alt ID errors
excerpt: Alt ID card and token-related payment errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: Alt ID errors
  description: Alt ID card and token-related payment errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **Alt ID Error Page**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_ALT_ID_BEGIN -->

## Error reference

Rows categorized: **8**.

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
    ['`Failure`', 'Card Association Error', 'Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_ALT_ID_END -->
