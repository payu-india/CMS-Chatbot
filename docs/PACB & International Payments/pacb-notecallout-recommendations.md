---
title: PACB Note/Callout Recommendations
deprecated: false
hidden: true
metadata:
  robots: index
---
This page provides the standardized merchant-facing callout components and integration notices designed for the **Cross-Border Payments — Import (PACB)** documentation suite.

Integrate these standardized callout blocks into your integration guides, parameter tables, and workflow summaries to proactively eliminate common merchant integration pitfalls and post-onboarding compliance issues.

***

## Callout 1: 10-Day Statutory Invoice Upload & Settlement Hold Alert

### Where to Place

Embed this warning in the following pages immediately after the **Payment Response / Webhook** section:

- [workflow-for-cross-border-payments-import.md](doc:workflow-for-cross-border-payments-import)
- [cb-integration-non-seamless.md](doc:cb-integration-non-seamless)
- All Server-to-Server (S2S) payment flow guides

### Markdown Component Code

```markdown
<Callout icon="🚨" theme="warn">
  ### **Critical Regulatory Requirement: 10-Day Commercial Invoice Submission**
  - **Statutory Filing**: Under RBI PACB regulations, you must upload the official commercial invoice PDF matching `udf5` within **10 calendar days** of transaction capture.
  - **Settlement Hold Penalty**: If the invoice (and Airway Bill/AWB for physical goods) is not submitted within 10 days, the AD-1 Category Bank will **place all future merchant settlements on hold**.
  - **Automation Best Practice**: Configure an automated webhook listener on your backend to trigger `POST /merchant/invoice/upload` immediately upon receiving payment capture confirmation.
</Callout>
```

***

## Callout 2: Regulatory Transaction Limits & Flow Routing

### Where to Place

Embed this informational block inside:

- The **Prerequisites** section of all PACB payment guides
- The **Step 1: Build Request** parameter tables across Checkout, UPI, and Cards flows

### Markdown Component Code

```markdown
<Callout icon="⚖️" theme="info">
  ### **Regulatory Value Caps & Smart Routing:**
  - **Online Checkout Limit**: Cards, NetBanking, and UPI payments are capped at a maximum of **₹2,50,000 (₹2.5 Lakh)** per transaction. Transactions exceeding this threshold fail with error code `E308`.
  - **High-Value Purchases**: For transactions between **₹2,50,001 and ₹25,00,000 (₹25 Lakh)**, you must route the customer to [Virtual Account Local Wire Transfers (NEFT/RTGS)](doc:virtual-account-based-local-wire-transfers).
</Callout>
```

***

## Callout 3: Buyer KYC Format Enforcement

### Where to Place

Embed this note directly above or inside the **Request Parameters** table on all PACB payment flow pages:

- One-Time Cards Checkout
- UPI Intent and Collect
- NetBanking Integration
- UPI Autopay Consent Integration

### Markdown Component Code

```markdown
<Callout icon="🛡️" theme="info">
  ### **Mandatory Buyer KYC Validation Rules:**
  - **PAN Format (`udf1`)**: Must be a valid 10-character Indian PAN regex `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`.
  - **Date of Birth (`udf3`)**: Must use hyphens `DD-MM-YYYY` (for example, `15-08-1988`). Slashes (`DD/MM/YYYY`) will cause regulatory parsing rejections.
  - **UPI Autopay Exception**: On UPI Autopay flows, format `udf1` as `PAN||DOB` and `udf3` as `InvoiceID||MerchantName`. Do not pass `udf4`.
</Callout>
```

***

## Callout 4: Webhook Secondary Validation & Hash Check

### Where to Place

Embed this security callout in the **Webhook Handling / Response Verification** section of all integration guides.

### Markdown Component Code

```markdown
<Callout icon="🔒" theme="warn">
  ### **Webhook Idempotency & Reverse Hash Verification:**
  - **Secondary Confirmation**: Never fulfill orders solely based on browser redirects (`surl`). Always treat the asynchronous Server-to-Server (S2S) webhook as the single source of truth.
  - **Reverse Hash Verification**: Always verify the incoming `hash` parameter against your merchant salt. If the payload contains `additional_charges`, prepend it to the hash calculation string before the salt.
  - **Automated Fallback**: If a webhook is not received within 5 minutes, query the [Verify Payment API](<redacted URL>) (`command=verify_payment`) using `txnid`.
</Callout>
```

***

## Callout 5: B2B Software / SaaS Eligibility Restriction

### Where to Place

Embed this regulatory notice on:

- PACB Overview page
- Request parameter tables where `buyer_type_business` is listed

### Markdown Component Code

```markdown
<Callout icon="💼" theme="info">
  ### **B2B Purchase Restriction:**
  - Setting `buyer_type_business=1` to accept payments from corporate Indian entities is legally permitted **strictly for software, SaaS, digital services, and subscriptions**.
  - Physical goods merchants cannot process B2B import payments under the OPGSP framework and must process individual retail consumer (B2C) transactions only.
</Callout>
```

***

## Callout 6: Currency Presentation & Indian Domestic Rails

### Where to Place

Embed this notice in the **Overview**, **Quick Start**, and **Parameters** tables where payment amounts are specified.

### Markdown Component Code

```markdown
<Callout icon="🇮🇳" theme="info">
  ### **Currency Presentation Notice:**
  - Under Cross-Border Payments — Import (PACB), Indian customers are always billed in **Indian Rupees (INR)**.
  - Always set the request `amount` and `currency` to INR. PayU collects funds locally across Indian payment rails and disburses the foreign currency equivalent to your overseas bank account following AD-1 bank settlement conversion.
</Callout>
```

***

## Summary Placement Matrix

| Callout Type                        | Target Pages                                       | Recommended Section                          |
| :---------------------------------- | :------------------------------------------------- | :------------------------------------------- |
| **1. 10-Day Invoice Alert**         | Workflow, Hosted Checkout, S2S Flow Guides         | Immediately after Payment Response / Webhook |
| **2. Transaction Limits & Routing** | Overview, Quick Start, Request Parameters Table    | Prerequisites & Step 1 Request Tables        |
| **3. Buyer KYC Format**             | All Checkout, UPI, and Cards Guides                | Above Request Parameters Table               |
| **4. Webhook Hash Check**           | Webhook Reference, Response Verification Steps     | Step 4 / Callback & Webhook Verification     |
| **5. B2B SaaS Restriction**         | Overview, Parameters Table (`buyer_type_business`) | Parameter description & Eligibility sections |
| **6. Currency Presentation**        | Overview, Quick Start, Payment Initiation          | Step 1 Amount Parameter description          |
