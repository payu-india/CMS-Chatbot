---
title: KYC and Partner Payment Errors
excerpt: >-
  Go through the KYC and partner merchant-status errors and their recommended
  fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are KYC and partner merchant-status errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`Authorisation Letter Document`',
        'description': '-',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      },
      {
        'bank_code': '`Authorised person name mismatch with the provided KYC`',
        'description': 'Re-upload the Authorisation letter with correct authorised person name.',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      },
      {
        'bank_code': '`Authorization Letter copy uploaded is not on firm\'s letterhead`',
        'description': 'Re-upload the authorization letter copy on firm\'s letterhead',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      },
      {
        'bank_code': '`Bank Verification letter is not on Bank letter head`',
        'description': 'Upload the bank verification letter on your Bank\'s letter head',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      },
      {
        'bank_code': '`Uploaded Authorisation letter is not in correct format`',
        'description': 'Re-upload Authorisation letter in correct format.',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      },
      {
        'bank_code': '`Uploaded Authorization letter is not clear`',
        'description': 'Re-upload clear authrization letter copy',
        'recommended_fix': 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'
      }
    ]}
  />
</Accordion>
