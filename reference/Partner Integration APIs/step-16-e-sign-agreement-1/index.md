---
title: Step 16 — E-Sign Agreement
hidden: false
---
This is the Final step. Generates the merchant agreement for digital signing.

## Prerequisite Steps
**All prior steps** must be complete

## Entity Applicability
**All entities**

## Correct Endpoint & Auth
| | Value |
|---|---|
| **URL** | `GET /api/v1/merchants/{uuid}/generate_merged_document_for_esign` |
| **Base** | `test-partner.payu.in` (Test) / `partner.payu.in` (Prod) |
| **Scope** | Must include BOTH `refer_merchant` AND `client_manage_agreement` |
## After Success
Merchant activated. Day-0 flags: S2S, tokenisation, callbacks, refunds.