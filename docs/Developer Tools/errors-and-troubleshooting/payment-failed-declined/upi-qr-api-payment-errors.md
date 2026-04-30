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
These are in-person UPI QR API payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

## Error Codes and Description

The following table lists errors and their recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
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
</Accordion>

