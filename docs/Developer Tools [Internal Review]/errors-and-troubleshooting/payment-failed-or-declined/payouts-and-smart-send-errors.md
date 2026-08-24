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

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`INVALID ACCOUNT NUMBER`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID UPI REQUEST`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID UPI LENGTH`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID UPI ID`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`BENEFICIARY NAME INVALID`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID CARD NUMBER`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID BENEFICIARY ID`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`CARD PROVIDER DETAILS NOT FOUND`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID CARD PROVIDER DETAILS`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID_CARD_TOKEN`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID_CARD_EXPIRY`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID_CARD_CRYPTOGRAM`',
        'description': 'Payouts Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID_ACCOUNT_NUMBER`',
        'description': 'Smart Send Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`OTP_REQUIRED`',
        'description': 'Smart Send Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`OTP_TRIGGERED_FAILED`',
        'description': 'Smart Send Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`OTP_VERIFICATION_FAILED`',
        'description': 'Smart Send Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      },
      {
        'bank_code': '`INVALID_VPA`',
        'description': 'Smart Send Error Codes',
        'recommended_fix': 'Correct payout request fields, beneficiary details, and transfer configuration; retry with a valid unique merchant reference.'
      }
    ]}
  />
</Accordion>
