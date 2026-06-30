---
title: Bank Verification APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Bank Verification APIs
excerpt: >-
  Verify bank accounts using penny drop or penniless transactions—authenticate
  with Get Token, call Bank Verification, and complete OTP when required.
deprecated: false
hidden: false
metadata:
  title: Bank Verification APIs
  description: >-
    API reference hub for PayU bank account verification: Get Token
    (verify_bank_account), Bank Verification (penny drop / penniless), and
    Submit OTP when the flow requires customer authentication.
  robots: index
next:
  description: ''
---
Bank Verification API let you confirm that a bank account is valid and that the account holder name matches your records. Verification uses a **penny drop** or **penniless** transaction against the account number and IFSC you provide.

Use this hub when you integrate bank verification during merchant onboarding, KYC, or payout beneficiary validation. Each API below has its own reference page with request parameters, samples, and response fields.

1. **[Get Token API – Bank Verification](ref:gettoken-bank-verification)** — Obtain a Bearer `access_token` with scope `verify_bank_account`.
2. **[Bank Verification API](ref:bank-verification-api)** — Post account number, IFSC, and holder name; optionally enable name matching.
3. **[Submit OTP API](ref:submit-otp-to-payu)** — When the verification or linked authentication flow returns a `referenceId` and requires customer OTP, collect the OTP on your page and submit it to complete the step.

If OTP submission fails or expires, use [Resend OTP API](ref:resend-otp-api) before retrying Submit OTP.