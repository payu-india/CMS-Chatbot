---
title: UPI QR API Payment Errors
excerpt: >-
  Go through the In-person UPI QR API payment errors and their recommended
  fixes.
deprecated: false
hidden: false
metadata:
  robots: index
---
These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **QR API Error Codes**.

<br />

Use this page with [Payment Failed or Declined](doc:payment-failed-declined)  for debugging guidance and retry handling.

<br />

## Error reference

<br />

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`No vpa exists against given merchant. Please contact sales support`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
    ['`Incoming VPA Does Not Match with registered vpa. Please provide a valid vpa`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
    ['`qr already exists but vpa does not match with existing qr vpa`', '-', 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
