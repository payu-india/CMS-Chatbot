---
title: BNPL payment errors
excerpt: Buy Now Pay Later payment failure errors categorized from the PayU repo.
deprecated: false
hidden: true
metadata:
  title: BNPL payment errors
  description: Buy Now Pay Later payment failure errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **BNPL Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_BNPL_BEGIN -->

## Error reference

Rows categorized: **4**.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| BNPL Error Codes | E2402 | The customer does not have an active credit line to book a consumer loan | - | Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying. |
| BNPL Error Codes | E2408 | The transaction or loan amount is greater than the available credit line with the customer | - | Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying. |
| BNPL Error Codes | E2414 | The customer’s account is inactive. | - | Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying. |
| BNPL Error Codes | E2421 | Potential fraud risk. Transaction not permitted | - | Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying. |

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_BNPL_END -->
