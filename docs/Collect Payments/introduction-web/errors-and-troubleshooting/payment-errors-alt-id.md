---
title: Alt ID errors
excerpt: Alt ID card and token-related payment errors categorized from the PayU repo.
deprecated: false
hidden: true
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

Rows categorized: **9**.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| Alt ID Error Page | EA021 | Failure | Card No is Invalid. Please check and initiate again | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA023 | Failure | CVV is Invalid. Please check and initiate again | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA081 | Failure | Incorrect Card Details. Please recheck CVV or expiry and try again | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA084 | Failure | Card not eligible. Please try another card | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA085 | Failure | Issuing bank server down. Please try in some time or try another card | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA086 | Failure | Card cannot be used. Please try another card | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA087 | Failure | Invalid details. Please try another card | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA088 | Failure | Card cannot be used. Please try another card | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |
| Alt ID Error Page | EA089 | Failure | Card Association Error | Correct card number, CVV, expiry, or eligibility issues; ask the customer to use another card when issuer/card restrictions apply. |

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_ALT_ID_END -->
