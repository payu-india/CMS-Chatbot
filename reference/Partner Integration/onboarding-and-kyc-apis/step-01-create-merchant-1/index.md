---
title: Step 01 — Create Merchant
hidden: false
---
Creates a new merchant account on PayU. Returns `mid` and `uuid` identifiers used in all subsequent steps.  You can create a merchant with regualar onbarding or offline onboarding using **Create Merchant&#x20;**&#x41;PI as described in the following sections:

- [Create Merchant API](ref:partner-create-merchant-api)
- [Offline Merchant Onboarding API](ref:partner-offline-merchant-onboarding-api)

## Prerequisite Steps

Step 00 (Authentication) — valid bearer token required

## Entity Applicability

**All entities** — this is always the first onboarding step.

<Callout icon="📘" theme="info">
  ### Important

  Only `display_name`, `email`, and `mobile` are sent here- **Do NOT send&#x20;**`business_entity_type`**&#x20;in this step** — it is set in Step 02- `email` must be unique across PayU — duplicate emails are rejected- Store both `mid` and `uuid` from the response — different APIs require different identifiers
</Callout>