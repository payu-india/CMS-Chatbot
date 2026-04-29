---
title: KYC and partner payment errors
excerpt: KYC and partner merchant-status errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: KYC and partner payment errors
  description: KYC and partner merchant-status errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **KYC Errors and Solutions**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_KYC_BEGIN -->

## Error reference

Rows categorized: **6**.

<SearchableTable
  headers={["Error code / type", "Description", "Recommended fix"]}
  rows={[
    ["`Authorisation Letter Document`", "-", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
    ["`Authorised person name mismatch with the provided KYC`", "Re-upload the Authorisation letter with correct authorised person name.", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
    ["`Authorization Letter copy uploaded is not on firm's letterhead`", "Re-upload the authorization letter copy on firm's letterhead", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
    ["`Bank Verification letter is not on Bank letter head`", "Upload the bank verification letter on your Bank's letter head", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
    ["`Uploaded Authorisation letter is not in correct format`", "Re-upload Authorisation letter in correct format.", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
    ["`Uploaded Authorization letter is not clear`", "Re-upload clear authrization letter copy", "Apply the listed KYC or merchant-status correction, update required merchant data, and retry the onboarding/status flow."],
  ]}
  placeholder="Search"
/>


<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_KYC_END -->
