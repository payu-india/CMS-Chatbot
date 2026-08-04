---
title: 'Step 05 — Update: Bank Details'
excerpt: >-
  # Step 05 — Update Merchant: Bank Details


  Adds bank account details for settlement. PayU attempts **auto-verification**
  of the bank account. If auto-verification fails, proceed to Step 06 to upload
  bank proof manually.


  ## Prerequisite Steps

  - Step 04 (Business Details)


  ## Entity Applicability

  **All entities**


  ## Auto-Verification

  After this call, PayU automatically verifies the bank account via penny drop
  or IFSC validation. Check the result using **GetMerchant** (Utilities) → look
  for `bank_verification_status`.


  - If `bank_verification_status` = `verified` → skip Step 06, proceed to Step
  07

  - If `bank_verification_status` = `failed` or `pending` → proceed to Step 06
  (upload bank proof)
hidden: false
---