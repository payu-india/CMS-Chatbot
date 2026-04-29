---
title: Transaction Stage Errors
excerpt: Go through Field7 and Field8 transaction-stage payment errors.
deprecated: false
hidden: false
metadata:
  robots: index
---
These are Field7 and Field8 transaction-stage payment errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`When received authentication response Negative from ACS on our TermURL`', 'Indicates that the ACS returned a negative authentication response to PayU\'s termination URL. This typically happens when the cardholder fails to correctly complete the challenge (e.g., enters wrong OTP multiple times...', 'Use field7/field8 to identify the failed stage, then verify final status before retrying or changing order state.'],
    ['`When Authentication is failed and 3DS Status=N,U`', 'Occurs when authentication fails with status "N" (No - authentication failed) or "U" (Unable to authenticate). This may happen when the cardholder enters incorrect authentication details or the issuer rejects the auth...', 'Use field7/field8 to identify the failed stage, then verify final status before retrying or changing order state.'],
    ['`OnUs OTP at PayU\'s end and PayU requested for an OTP Generation`', 'Occurs when PayU\'s own authentication system (rather than the bank\'s) generates and sends a One-Time Password to the customer for transaction verification. This is used in certain payment flows where PayU manages the...', 'Use field7/field8 to identify the failed stage, then verify final status before retrying or changing order state.'],
    ['`Callback received from the bank - Negative identification`', 'Occurs when the bank or wallet provider sends a negative callback to PayU, indicating that the payment was declined or rejected. This could be due to insufficient funds, incorrect payment details, expired cards, or th...', 'Use field7/field8 to identify the failed stage, then verify final status before retrying or changing order state.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>
