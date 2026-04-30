---
title: BNPL Payment Errors
excerpt: Go through the Buy Now Pay Later payment failure errors and find their fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are Alt ID card and token-related payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

## Error Codes and Description

The following table lists Alt ID card and token-related payment errors and their recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
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
</Accordion>

<br />