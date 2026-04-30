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

## Error Codes and Description

The following table lists errors and their recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`Authorisation Letter Document`', '-', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
    ['`Authorised person name mismatch with the provided KYC`', 'Re-upload the Authorisation letter with correct authorised person name.', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
    ['`Authorization Letter copy uploaded is not on firm\'s letterhead`', 'Re-upload the authorization letter copy on firm\'s letterhead', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
    ['`Bank Verification letter is not on Bank letter head`', 'Upload the bank verification letter on your Bank\'s letter head', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
    ['`Uploaded Authorisation letter is not in correct format`', 'Re-upload Authorisation letter in correct format.', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
    ['`Uploaded Authorization letter is not clear`', 'Re-upload clear authrization letter copy', 'Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>
