---
title: Step 15B — UBO KYC via DigiLocker / Offline Aadhaar
excerpt: >-
  # Step 15B — UBO KYC via DigiLocker / Offline Aadhaar


  Runs Aadhaar-based KYC **for an individual UBO** (Ultimate Beneficial Owner)
  added in Step 15, either via DigiLocker (online) or an offline Aadhaar XML
  upload. These are UBO-specific variants of the Step 10 DigiLocker flow — the
  merchant-level DigiLocker/Aadhaar APIs (Step 10) verify the
  merchant/signatory, while these verify an individual UBO.


  ## Prerequisite Steps

  - Step 15 (Add/Update UBO) — the UBO must already exist on the product
  account, and its `ultimate_beneficiary_uuid` must be known (returned in the
  Step 15 response's `ultimate_beneficiaries[]` array)

  - Step 09 (Signatory Details) — required before any DigiLocker-based flow


  ## Entity Applicability

  **Only for:** Private Limited, Public Limited, Partnership, Trust, LLP,
  Society (same entities that require UBO in Step 15)


  ## Choosing Between the Two Sub-Requests


  ```

  IF merchant/UBO can authenticate online with Aadhaar OTP:
      Use "GenerateDigilockerLinkForUBO" — redirect UBO to the returned capture_link
  ELSE (offline flow, UBO already has an Aadhaar XML + share code from UIDAI):
      Use "AadhaarXmlOfflineForUBO" — upload the XML file + share code directly
  ```
hidden: true
link:
  new_tab: false
---