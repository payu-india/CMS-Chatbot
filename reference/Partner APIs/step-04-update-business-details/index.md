---
title: 'Step 04 — Update: Business Details'
excerpt: .
hidden: false
---
Central KYC verification using data from the CKYC registry (CERSAI). The method depends on entity type.

## Prerequisite Steps
Step 02 (PAN + Entity) — PAN must be submitted and entity type set

## Entity Applicability
**All entities** — but the method differs:

## Branching Logic
IF entity_type IN (Individual, Sole Proprietorship):    
1. Call "Send CKYC OTP" (Sub-request A) — consent: true + mobile required    
2. Merchant receives OTP on mobile    
3. Call "Verify CKYC OTP" (Sub-request B) — with the OTPELSE (Partnership, Pvt Ltd, Public Limited, LLP, Trust, Society, One Person Company, etc.):    
   a. Call "Fetch CKYC Data" (Sub-request C) — consent: true, fetches directly via PAN

## CKYC Response Data (on success)- Name- Date of Birth / Date of Incorporation- Address (city, state, pincode)- Masked mobile number

## Downstream Impact
| CKYC Outcome | Entity Type | DigiLocker (Step 09) |
|-------------|-------------|---------------------|
| Succeeded | Individual / Sole Prop | **Optional** (can skip) || Succeeded | All others | **Required** || Skipped | Individual / Sole Prop | **Required** |
| Skipped | All others | **Required** |