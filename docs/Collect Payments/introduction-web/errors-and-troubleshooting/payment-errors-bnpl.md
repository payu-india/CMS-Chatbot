---
title: BNPL payment errors
excerpt: Buy Now Pay Later payment failure errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: BNPL payment errors
  description: Buy Now Pay Later payment failure errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **BNPL Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

## Category alignment

Primary category: Payment failures for BNPL eligibility, credit-line, OTP, and lender-state issues.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_BNPL_BEGIN -->

## Error reference

Rows categorized: **4**.

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`The customer does not have an active credit line to book a consumer loan`', '-', 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'],
    ['`The transaction or loan amount is greater than the available credit line with the customer`', '-', 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'],
    ['`The customer’s account is inactive.`', '-', 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'],
    ['`Potential fraud risk. Transaction not permitted`', '-', 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_BNPL_END -->
