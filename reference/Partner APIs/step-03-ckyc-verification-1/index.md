---
title: Step 03 — CKYC Verification
excerpt: >-
  # Step 03 — CKYC (Central KYC) Verification


  Central KYC verification using data from the CKYC registry (CERSAI). The
  method depends on entity type.


  ## Prerequisite Steps

  - Step 02 (PAN + Entity) — PAN must be submitted and entity type set


  ## Entity Applicability

  **All entities** — but the method differs:


  ## Branching Logic


  ```

  IF entity_type IN (Individual, Sole Proprietorship):
      1. Call "Send CKYC OTP" (Sub-request A) — consent: true + mobile required
      2. Merchant receives OTP on mobile
      3. Call "Verify CKYC OTP" (Sub-request B) — with the OTP
  ELSE (Partnership, Pvt Ltd, Public Limited, LLP, Trust, Society, One Person
  Company, etc.):
      1. Call "Fetch CKYC Data" (Sub-request C) — consent: true, fetches directly via PAN
  ```


  ## Skip CKYC


  > **COMING SOON:** A dedicated "Skip CKYC" API is being developed and will be
  available shortly. Until then, CKYC must be attempted for all merchants.

  >

  > **Impact of skipping CKYC:** If CKYC is skipped (once the API is available),
  DigiLocker (Step 09) becomes **mandatory even for Individual/Sole Prop**
  entities. If CKYC succeeds for Individual/Sole Prop, DigiLocker can be
  skipped.


  ## CKYC Response Data (on success)

  - Name

  - Date of Birth / Date of Incorporation

  - Address (city, state, pincode)

  - Masked mobile number


  ## Downstream Impact


  | CKYC Outcome | Entity Type | DigiLocker (Step 09) |

  |-------------|-------------|---------------------|

  | Succeeded | Individual / Sole Prop | **Optional** (can skip) |

  | Succeeded | All others | **Required** |

  | Skipped | Individual / Sole Prop | **Required** |

  | Skipped | All others | **Required** |
hidden: false
---