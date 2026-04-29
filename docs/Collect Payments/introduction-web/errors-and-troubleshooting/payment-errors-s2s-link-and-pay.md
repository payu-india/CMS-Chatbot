---
title: S2S Link and Pay errors
excerpt: Server-to-server Link and Pay payment errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: S2S Link and Pay errors
  description: Server-to-server Link and Pay payment errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **S2S Link and Pay Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_S2S_LINK_AND_PAY_BEGIN -->

## Error reference

Rows categorized: **4**.

<SearchableTable
  headers={["Error code / type", "Description", "Recommended fix"]}
  rows={[
    ["`The customer does not have an active credit line to book a consumer loan`", "-", "Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status."],
    ["`The transaction or loan amount is greater than the available credit line with the customer`", "-", "Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status."],
    ["`The customer’s account is inactive.`", "-", "Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status."],
    ["`Potential fraud risk. Transaction not permitted`", "-", "Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status."],
  ]}
  placeholder="Search"
/>


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_S2S_LINK_AND_PAY_END -->
