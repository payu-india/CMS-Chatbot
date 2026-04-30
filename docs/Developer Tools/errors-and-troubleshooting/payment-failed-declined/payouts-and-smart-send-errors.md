---
title: Payouts and Smart Send Errors
excerpt: Go through these Payouts and Smart Send errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are payouts and smart send errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="fa-wrench">

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`INVALID ACCOUNT NUMBER`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID UPI REQUEST`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID UPI LENGTH`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID UPI ID`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`BENEFICIARY NAME INVALID`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID CARD NUMBER`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID BENEFICIARY ID`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`CARD PROVIDER DETAILS NOT FOUND`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID CARD PROVIDER DETAILS`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID_CARD_TOKEN`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID_CARD_EXPIRY`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID_CARD_CRYPTOGRAM`', 'Payouts Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID_ACCOUNT_NUMBER`', 'Smart Send Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`OTP_REQUIRED`', 'Smart Send Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`OTP_TRIGGERED_FAILED`', 'Smart Send Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`OTP_VERIFICATION_FAILED`', 'Smart Send Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
    ['`INVALID_VPA`', 'Smart Send Error Codes', 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>