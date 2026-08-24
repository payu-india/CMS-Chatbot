---
title: UPI QR API Payment Errors
excerpt: >-
  Go through the In-person UPI QR API payment errors and their recommended
  fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are in-person UPI QR API payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`No vpa exists against given merchant. Please contact sales support`',
        'description': '-',
        'recommended_fix': 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'
      },
      {
        'bank_code': '`Incoming VPA Does Not Match with registered vpa. Please provide a valid vpa`',
        'description': '-',
        'recommended_fix': 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'
      },
      {
        'bank_code': '`qr already exists but vpa does not match with existing qr vpa`',
        'description': '-',
        'recommended_fix': 'Correct QR request parameters, merchant VPA setup, amount, and transactionId; retry with a valid unique transactionId.'
      }
    ]}
  />
</Accordion>
