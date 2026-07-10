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

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`The customer does not have an active credit line to book a consumer loan`', '-', 'Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status.'],
    ['`The transaction or loan amount is greater than the available credit line with the customer`', '-', 'Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status.'],
    ['`The customer’s account is inactive.`', '-', 'Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status.'],
    ['`Potential fraud risk. Transaction not permitted`', '-', 'Correct the S2S Link-and-Pay request, eligibility, or enablement issue, then retry only after confirming the current status.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>
