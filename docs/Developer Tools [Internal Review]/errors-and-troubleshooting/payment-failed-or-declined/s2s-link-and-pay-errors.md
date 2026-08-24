---
title: S2S Link and Pay Errors
excerpt: Go through these server-to-server link and pay payment errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are server-to-server link and pay payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`The customer does not have an active credit line to book a consumer loan`',
        'description': '-',
        'recommended_fix': 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'
      },
      {
        'bank_code': '`The transaction or loan amount is greater than the available credit line with the customer`',
        'description': '-',
        'recommended_fix': 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'
      },
      {
        'bank_code': '`The customer\'s account is inactive.`',
        'description': '-',
        'recommended_fix': 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'
      },
      {
        'bank_code': '`Potential fraud risk. Transaction not permitted`',
        'description': '-',
        'recommended_fix': 'Validate customer eligibility, credit line, lender configuration, OTP, amount, and required BNPL parameters before retrying.'
      }
    ]}
  />
</Accordion>
