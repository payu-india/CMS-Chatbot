---
title: October 2026
author: Raghuram Pandurangan
hidden: false
published_at: '2026-11-05T05:40:55.837Z'
---
Discover PayU payment capabilities, API enhancements, and integration changes for October 2026. This changelog is for merchants and developers integrating PayU APIs. Availability can depend on merchant activation, payment-method support, or eligibility described in the relevant entry.

## Developer Tools & AI

<Accordion title="Integrate PayU Hosted Checkout with AI (MCP Skill)" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>
        **Product:** Developer Tools & SDKs  
        **Feature/API:** PayU Hosted Checkout AI Skill (MCP-Powered)  
        **Impact:** Low  
        **Breaking Change:** No  
        **Action Required:** Optional, developer productivity tool
      </div>
    </Column>
  </Columns>

  **Summary**

  PayU has released the **PayU Hosted Checkout AI Skill**, a prompt-driven developer tool that enables merchants to scaffold and implement an end-to-end PayU Hosted Checkout (web redirect) integration into Java, Node.js, PHP, or Python backends in a single prompt using Claude Code, Cursor, or any MCP-enabled AI coding assistant. The skill connects directly to the live `payu-docs` Model Context Protocol (MCP) server to retrieve verified hash formulas, endpoints, and code samples while enforcing strict security guardrails to protect merchant credentials.

  **Why this matters**

  Integrating payment gateways often involves repetitive boilerplate code, risk of hash calculation mismatches, and potential credential leakage into LLM chat windows. This AI skill automates the entire implementation lifecycle adapted to the merchant's existing codebase while guaranteeing that merchant secrets (`PAYU_MERCHANT_KEY` and `PAYU_MERCHANT_SALT`) are never exposed, logged, or read by AI assistants.

  **Who is affected**

  - Developers and engineering teams implementing or upgrading PayU Hosted Checkout.
  - Merchants using AI-assisted development environments (Cursor, Claude Code, VS Code Copilot).

  **What's new**

  - **Single-Prompt Scaffolding:** Detects the backend stack and automatically implements the 7 core integration steps: request hash generation, response reverse-hash verification, initiate route (`POST /api/payu/initiate`), frontend auto-submit form, `surl`/`furl` callback handlers, route registration, and Verify Payment API (`verify_payment`) fallback logic.
  - **Live PayU Docs MCP Integration:** Connects to the authoritative `payu-docs` MCP server (`https://ask-ai-mcp-710575177112.asia-south1.run.app/mcp`) to fetch up-to-date SHA-512 formulas, endpoints, and code snippets rather than relying on stale model training data.
  - **Multi-Stack Support:** Supports Java (Java 11+), Node.js, PHP, and Python (Flask, Django, FastAPI) backends.
  - **Reverse Hash Robustness:** Generates constant-time reverse-hash verification covering standard UDFs, no-UDF variants, `additional_charges`, `splitInfo`, and Web Checkout Pro edge cases, falling back to the Verify Payment API when verification fails.
  - **Security Guardrails:** Hardcoded never to read `.env` files, never to log or echo keys or salts, never to expose the salt to frontend templates, never to run git commits/pushes, and never to make unauthorized live API calls.
  - **Embedded Troubleshooting Guide:** Automatically appends an error-handling debugging matrix to the project's README covering invalid hashes, duplicate `txnid`, and callback resolution.

  **Action required**

  To use the skill, add the `payu-docs` MCP server to your assistant's MCP configuration, save the prompt as `.claude/commands/payu-hosted-checkout.md` (or add it to your assistant's system instructions), ensure `PAYU_MERCHANT_KEY` and `PAYU_MERCHANT_SALT` are defined in your local environment variables, and invoke the prompt.

  **Need to migrate**

  No. This is an optional developer enablement tool. Existing manual PayU Hosted Checkout integrations continue to function as documented.

  **Related documentation**

  - [Integrate PayU Hosted Checkout with AI](https://docs.payu.in/docs/integrate-payu-hosted-checkout-with-ai)
</Accordion>

## Partner Integration Enhancements

<Accordion title="Generate DigiLocker Link for UBO" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>
        **Product:** Partner Platform / KYC  
        **Feature/API:** Generate DigiLocker Link for UBO  
        **Impact:** Medium  
        **Breaking Change:** No  
        **Action Required:** Optional, for partners onboarding non-individual merchants
      </div>
    </Column>
  </Columns>

  **Summary**

  Partners can now generate a DigiLocker authentication link to verify the Aadhaar identity of Ultimate Beneficial Owners (UBOs) programmatically via API. This enables end-to-end digital, paperless KYC for key owners and stakeholders of non-individual business entities directly within partner-managed onboarding flows.

  **Why this matters**

  Regulatory guidelines require verifying individual beneficial owners who hold significant ownership in corporate or partnership entities (such as Private Limited, Public Limited, or LLP companies). Generating a direct DigiLocker verification link allows UBOs to authenticate instantly via Aadhaar OTP, eliminating manual document scanning, physical document collection, and verification delays.

  **Who is affected**

  - Partners onboarding non-individual merchants through PayU Partner Onboarding APIs.
  - Developers integrating partner KYC and document-collection flows.
  - Operations and compliance teams managing merchant onboarding verification.

  **What's new**

  - **Dedicated API Endpoint:** Call `POST /api/v3/merchants/{mid}/kyc_document/generate_digilocker_link_for_ubo` using Bearer authentication scoped to KYC permissions.
  - **Prerequisite Binding:** The UBO must first be registered using the Add/Update UBO step, which issues the required `ultimate_beneficiary_uuid`.
  - **Explicit Consent Check:** The API enforces explicit user consent by requiring `consent: true` in the request body alongside the `ultimate_beneficiary_uuid`. Missing either field returns an HTTP 422 validation response.
  - **Authentication Capture Link:** A successful request returns `status: "link_generated"` and a secure DigiLocker OAuth2 redirect URL in `capture_link`.
  - **Smooth Onboarding Progression:** Directing the UBO to the generated `capture_link` allows them to complete Aadhaar OTP verification on DigiLocker, enabling partners to automatically proceed with subsequent verification and activation stages.

  **Action required**

  Partners onboarding non-individual merchants should integrate this endpoint following UBO creation. Ensure your application captures explicit consent, retrieves the `ultimate_beneficiary_uuid`, and redirects the UBO to the returned `capture_link` for OTP authentication.

  **Need to migrate**

  No. This is an optional API capability that augments existing partner KYC flows for non-individual entities.

  **Related documentation**

  - [Generate DigiLocker Link for UBO](https://docs.payu.in/reference/generate-digilocker-link-for-ubo)
</Accordion>

<Accordion title="Set Merchant Rates API" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>

        **Date:** October 8, 2026  
        **Product:** Partner Platform / Pricing  
        **Feature/API:** Set Merchant Rates API  
        **Impact:** Medium  
        **Breaking Change:** No  
        **Action Required:** Optional, for partners configuring custom merchant rates
      </div>
    </Column>
  </Columns>

  **Summary**

  PayU has introduced the **Set Merchant Rates API**, allowing partners to configure and update custom Transaction Discount Rates (TDR) and Transaction Service Fees (TSF) for their referred merchants programmatically. The endpoint supports batch upserts of up to 300 pricing entries per request with independent entry processing.

  **Why this matters**

  Partners often maintain differentiated commercial terms or negotiated payment-method pricing for their referred sub-merchants. Instead of relying on manual operations intervention or uniform partner-level pricing, partners can now automate merchant-specific rate provisioning directly via API during or post-onboarding.

  **Who is affected**

  - Partners offering custom rate plans to referred merchants.
  - Developers integrating partner pricing and rate-card configuration workflows.
  - Finance and operations teams managing sub-merchant pricing agreements.

  **What's new**

  - **Batch Upsert Endpoint:** Submit rate configuration requests to `POST /api/v1/partners/merchant_rates` supporting up to 300 pricing entries in a single batch.
  - **Independent Entry Processing:** Each entry in the payload is evaluated independently. A validation error or failure on one payment mode or instrument does not roll back or reject other valid entries in the batch.
  - **Structured Outcome Handling:**
    - `HTTP 200` + `status: success`: All pricing entries in the batch were processed and applied successfully.
    - `HTTP 200` + `status: partial_success`: Partial batch completion. Inspect the `results[]` array to identify which entries succeeded and which failed.
    - `HTTP 422` + `status: error` (with `results[]`): Entry-level validation failures where all submitted entries failed.
    - `HTTP 422` + `status: error` (with `message`, no `results[]`): Service-level rejection (e.g., invalid MID, merchant not mapped to partner account, or batch size exceeding 300 entries).
    - `HTTP 400 / 401 / 403 / 404`: Request rejected before entry processing due to bad syntax, authentication failures, or route issues.
  - **Mechanism-to-Instrument Support:** Configure customized rates mapped across supported payment mechanisms and instruments in accordance with PayU's pricing specifications.

  **Action required**

  To automate merchant pricing, incorporate the Set Merchant Rates API into your partner management application. Ensure requests reference linked MIDs, observe the 300-entry batch limit, and inspect `status` and `results[]` to handle partial successes.

  **Need to migrate**

  No. Partners not configuring custom rates programmatically may continue using standard partner-level pricing agreements.

  **Related documentation**

  - [Set Merchant Rates API](https://docs.payu.in/reference/setmerchantrates)
</Accordion>