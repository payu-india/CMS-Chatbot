---
title: Step 09 — DigiLocker Verification
hidden: false
---
Aadhaar-based identity verification via DigiLocker (MeitY). Generates an authentication URL; merchant authenticates with Aadhaar OTP, and documents flow to PayU.

## Prerequisite Steps
**Step 08 (Signatory Details) — MUST be completed.** 
DigiLocker will fail without signatory details.

## Entity Applicability & Branching

```IF entity_type IN (Individual, Sole Proprietorship):    IF CKYC (Step 03) succeeded:        DigiLocker = OPTIONAL — can be SKIPPED    ELSE (CKYC was skipped or failed):        DigiLocker = REQUIREDELSE (Partnership, Pvt Ltd, Public Limited, LLP, Trust, Society, One Person Company, etc.):    DigiLocker = ALWAYS REQUIRED — even if CKYC succeeded```

## How to Determine if DigiLocker is NeededCall
**GetMerchant** (Utilities) and check:- `entity_type` — Individual/Sole Prop or other- `ckyc_status` — whether CKYC succeeded

## Flow
1. Partner calls this API with `consent: true`
2. PayU returns a DigiLocker authentication URL
3. Partner redirects merchant to that URL
4. Merchant authenticates on DigiLocker with Aadhaar OTP5. Documents flow from DigiLocker directly to PayU6. Merchant is redirected back to partner's pre-configured URL