---
title: Payouts and Smart Send errors
excerpt: Payouts and Smart Send errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: Payouts and Smart Send errors
  description: Payouts and Smart Send errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **Payouts Error Codes, Smart Send Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_PAYOUTS_BEGIN -->

## Error reference

Rows categorized: **17**.

<SearchableTable
    headers={['Error code / type', 'Description', 'Recommended fix']}
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
    placeholder="Search"
  />


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_PAYOUTS_END -->
