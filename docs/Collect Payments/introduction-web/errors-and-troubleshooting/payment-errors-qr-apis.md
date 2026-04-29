---
title: UPI QR API payment errors
excerpt: In-person UPI QR API payment errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: UPI QR API payment errors
  description: In-person UPI QR API payment errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **QR API Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_QR_APIS_BEGIN -->

## Error reference

Rows categorized: **3**.

<SearchableTable
    headers={['Error code / type', 'Description', 'Recommended fix']}
    rows={[
    ['`No vpa exists against given merchant. Please contact sales support`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
    ['`Incoming VPA Does Not Match with registered vpa. Please provide a valid vpa`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
    ['`qr already exists but vpa does not match with existing qr vpa`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
  ]}
    placeholder="Search"
  />


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_QR_APIS_END -->
