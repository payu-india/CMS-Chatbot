# PayU Docs — Tier 2 Product Restructure Template

> **For agents and contributors:** This template defines the process, content rules, component conventions, and git workflow for restructuring any Tier 2 PayU integration product.
>
> **Critical rule: Never create or modify files before the IA proposal is confirmed.** Phases 0 and 1 are read-only. All file operations happen only after explicit approval of both the page structure and the content outlines.
>
> **Reference implementation (completed, read this before proposing any IA):**
> - PayU Hosted Checkout → `docs/Low-Code Products/payu-hosted-checkout-1/`

---

## Phase 0 — Discovery (Read-Only)

Before proposing anything, understand the product. Read every existing file in the product directory and its subdirectories. Do not skim — read fully.

### 0.1 Read the existing structure

```
find {product-directory} -name "*.md" -o -name "*.yaml" -o -name "*.yml" | sort
```

For each file found, read its full contents. Answer these questions before moving on:

- What is the integration model? (form POST, JS SDK, REST API, mobile SDK, etc.)
- How many distinct technical flows exist? (single flow vs. per-method flows)
- What payment methods does it support, and are they documented separately or together?
- What APIs does it call? (one endpoint vs. multiple)
- How complex is the hash setup? (single formula vs. method-specific variants)
- Are there already well-structured pages to retain?
- Are there legacy, duplicate, or deprecated pages that add noise?

### 0.2 Read the two reference implementations

Read this to understand the target structure before forming an opinion:

**PayU Hosted Checkout** (completed reference implementation):
`docs/Low-Code Products/payu-hosted-checkout-1/`

This is the gold standard for structure, frontmatter, component usage, and content conventions. Use it as the benchmark — not as a template to clone. The right IA for the product you are restructuring will be adapted based on that product's complexity and integration model.

### 0.3 Check the reference directory for OAS/JSON files

```
ls reference/
```

Identify OpenAPI spec files for this product's APIs. Note their filenames — needed for the API reference pages.

---

## Phase 1 — Proposal (Read-Only, No File Changes)

After completing Phase 0, produce a written proposal for review. The proposal covers both the **page structure** and the **content outline of every proposed page**. Present it to the user and wait for approval before touching any files.

The proposal must contain all six sections below.

---

### 1.1 Product summary

Write 2–3 sentences answering:

- What does this product do, and what does the developer build?
- What is the integration model?
- How complex is the integration?

---

### 1.2 Proposed page structure with rationale

Propose the page tree and explain *why* each page exists or is omitted based on the product's actual complexity.

**Use this as a starting point and adapt it:**

```
{product-slug}/
├── index.md                   [always include — product overview]
├── how-it-works.md            [always include — architecture + flow]
├── quick-start.md             [always include — first working integration]
├── integration-guide/
│   ├── build-integration/
│   │   ├── index.md           [include only if there are multiple sub-pages]
│   │   └── ...                [one page per distinct integration path; or single page if one flow]
│   ├── test-integration.md    [always include]
│   └── go-live-checklist.md   [always include]
├── errors-and-troubleshooting.md   [always include]
├── faqs.md                    [always include]
└── {product}-apis.md          [include only if the product has its own API endpoints]
```

**Decision rules:**

| Question | If yes | If no |
|---|---|---|
| Does the product have multiple payment methods, each with distinct parameters or flows? | One page per method under `build-integration/` + an `index.md` navigator | Single `build-integration.md`, no subdirectory |
| Does any method require a pre-step (OTP, balance check, two-step initiation)? | Each such method gets its own page | Combine into fewer pages |
| Does the product have its own dedicated API endpoint(s)? | Include `{product}-apis.md` | Omit; reference shared APIs inline |
| Is the SDK/integration initialised separately from the payment call? | Add `initialise-sdk.md` or `setup.md` | No separate setup page |
| Does the product have webhook events distinct from the standard set? | Add `webhooks.md` | Note inline, no separate page |
| Are there substantial compliance requirements (PCI-DSS, MCC restrictions, activation)? | Dedicated `compliance.md` if content is substantial; otherwise Callout inline | Note inline only |

---

### 1.3 Per-page content outline

For every page in the proposed structure, write the full heading outline — every H2 and H3, the ReadMe component for each section, and one line explaining what content goes there. This is what the user reviews and approves before writing begins.

**Format each page outline like this:**

```
── {page-slug}.md ─────────────────────────────────────
  [frontmatter]
  H1: {Page Title}
  
  H2: {Section heading}   [component: Banner / Accordion / Cards / Callout / table / prose / Tabs]
    → {one line: what content goes here}
  
  H2: {Section heading}   [component]
    → {what content goes here}
      H3: {Subsection}   [component]
        → {what content goes here}
────────────────────────────────────────────────────────
```

The outlines for all standard pages are defined in the **Page Content Skeletons** section of this template. Use those as the base and adapt them to the product — remove sections that do not apply, add product-specific sections where the source material warrants it, and note any section where you expect a gap.

> **Mark adapted sections clearly:**
> - `[OMIT — reason]` for sections removed from the standard skeleton
> - `[ADD — reason]` for sections not in the skeleton but needed for this product
> - `[GAP — description]` for sections where source material is missing

---

### 1.4 Pages to deprecate

For each existing page that the new structure supersedes:

| Current path | Migrated to | Action |
|---|---|---|
| `path/old-page.md` | `path/new-page.md` | Deprecate + redirect Callout |

---

### 1.5 Gaps and validations flagged

List every gap or contradiction found during discovery:

- **Gaps** — information the new pages need that is absent from source files
- **Contradictions** — where two source files conflict (different hash formulas, endpoint URLs, field names, etc.)
- **Empty migrations** — pages that exist in the current structure but have no source content to migrate from

---

### 1.6 `_order.yaml` plan

Show the exact `_order.yaml` contents for each directory level.

---

## Confirmation Gate

**Stop here. Present the full Phase 1 proposal to the user.**

Ask explicitly:

> "Here is the proposed structure and content outline for every page in {Product Name}. Please review the page list, the section headings for each page, the deprecation plan, and any gaps I've flagged. Confirm to proceed, or tell me what to adjust."

**Do not start Phase 2 until you receive explicit approval.** Incorporate any adjustments from partial approval before writing a single file.

---

## Phase 2 — Execution (File Operations Begin Here)

Execute only the approved IA and content outlines. Do not add pages, remove pages, rename slugs, or add/remove sections from the approved outlines without asking again.

### Execution order

1. Create `_order.yaml` files (all directory levels)
2. Create pages in this order: `index.md` → `how-it-works.md` → `quick-start.md` → `build-integration/` pages → `test-integration.md` → `go-live-checklist.md` → `errors-and-troubleshooting.md` → `faqs.md` → `{product}-apis.md`
3. Deprecate legacy pages last — only after all new content is written and redirect targets are confirmed to exist

### Source-first writing rule

For every section of every page, read the relevant source files before writing. Extract parameters, code samples, test credentials, flow descriptions, and error codes from the source. Do not write from memory or training data.

If a section has no source material:
```markdown
<!-- DOCUMENTATION GAP: [describe what is missing and where to find it] -->
```

---

## Page Content Skeletons

These are the standard heading outlines for every page type. Use them when building the Phase 1 per-page content outlines. Adapt — do not apply blindly.

**Notation used:**
- `[Banner]`, `[Accordion]`, `[Cards]`, `[Callout]`, `[Tabs]`, `[table]`, `[prose]` — the ReadMe component or element to use
- `*` — conditional: include only if the product warrants it (explained inline)
- `+` — product-specific: add new H2s or H3s here based on source material

---

### Overview — `index.md`

```
[frontmatter]
[Banner] — tier/complexity indicator *top of page, before H1*

H1: {Product Name}
  [prose] — 1-paragraph intro: what it is, what developer builds, what PayU handles

H2: What Can I Build with {Product}?
  [Accordion] × 4–5 — one per major capability
    → Each: title describes the capability; body explains what the developer gets

H2: Is {Product} Right for Me?
  [table] — "I want to…" column + "Works?" column (✅ or ⚠️ + alternative link)
  [Callout info] — "Not sure? See Start Here for comparison"

H2: Supported Payment Methods   *include only if merchant routes per method (e.g. MHC); omit if PayU handles internally (e.g. PayU Hosted)*
  [prose] — 1-sentence intro
  [table] — Method | pg value | bankcode | Guide link
  [Callout info] — note activation-required methods

H2: Common Use Cases
  [Cards columns=3] × 4–5 — real use cases, not generic descriptions

H2: What Do I Need to Get Started?
  [prose list] — prerequisites: account, keys, backend, HTTPS, PCI-DSS if applicable, callback URLs

H2: How Do I Integrate {Product}?
  [Accordion] × 4–6 — high-level steps (no full code here, just the shape of each step)
  [Callout info] — "Full details in Build Integration"

H2: Is My Integration Secure?
  [prose] — hash server-side, salt never in frontend, PCI-DSS if applicable, verify server-side, reverse hash

H2: How Does My Customer Pay?
  [Accordion] × 3–4 — customer journey steps

H2: Post-Payment Actions
  [Cards columns=2] — Refunds, Chargeback, Settlements Dashboard, Webhooks

H2: Use AI to Help You
  [prose] — 1-sentence intro
  [Callout info] — example prompts block
  [Cards columns=2] — Developer MCP, Integration Lab

H2: Next Steps
  [Cards columns=2] — How It Works, Quick Start, Build Integration, APIs
```

---

### How It Works — `how-it-works.md`

```
[frontmatter]

H1: How {Product} Works

H2: Architecture Overview
  [prose or ASCII diagram] — merchant ↔ PayU ↔ bank flow

H2: Endpoints
  [table] — Environment | URL (test + production)

H2: Key Parameters   *include if the product has routing parameters (pg, bankcode, etc.)*
  [table] — Parameter | Value | Purpose

H2: Hash Generation
  H3: Request Hash
    [prose] — formula: sha512(key|txnid|amount|...)
    [Tabs] — code in Node.js, PHP, Python (from source files only)
  H3: Response Hash Verification
    [prose] — reverse formula
    [Tabs] — verification code

H2: Payment Flow — Step by Step
  [Accordion] × 5–8 — each step in sequence, numbered titles

H2: PCI-DSS Scope   *include only if product is in PCI-DSS scope*
  [prose] — what is in scope, SAQ type, what to do

H2: When to Use {Product} vs Alternatives
  [table] — Scenario | Recommended product

H2: Key Concepts
  [prose] — glossary of 5–8 terms the developer will encounter
  *or [Accordion] per term if definitions are long*

+ [add product-specific H2s based on source material]
```

---

### Quick Start — `quick-start.md`

```
[frontmatter]
[Callout warn] — "Use test credentials only. Never use live credentials in test."

H1: Quick Start — {Product Name}

H2: What You'll Build
  [prose] — 1–2 sentences: what this quick start produces

H2: Step 1: Get Your Test Credentials
  [KeySaltReference custom block]

H2: Step 2: Generate the Hash
  [prose] — formula reminder
  [Tabs] — hash code in Node.js and PHP minimum

H2: Step 3: {Submit / Initialise / Call} the Payment
  *heading wording adapts to integration model*
  [table] — endpoint (test)
  [Tabs] — minimal working code (cURL or form POST or SDK call)
  [Callout info] — test card number / test VPA / test bank to use

H2: Step 4: Handle the Callback
  [prose] — what arrives at surl/furl or the callback handler
  [Tabs] — reverse hash verification code

H2: Step 5: Verify the Payment Server-Side
  [Tabs] — Verify Payment API cURL call

H2: Next Steps
  [Cards columns=2] — Build Integration, Test Integration

+ [add steps for products with extra setup (SDK init, OAuth, etc.)]
```

---

### Build Integration — single page (use when product has one integration flow)

```
[frontmatter]

H1: Build the Integration

H2: Endpoints
  [table] — Environment | URL

H2: Request Parameters
  H3: Mandatory Parameters
    [table] — Parameter | Type | Description | Example
  H3: Optional Parameters
    [table] — Parameter | Type | Description | Example

H2: {Submit / Send} the Payment Request
  [Accordion title="cURL" icon="fa-code"] — full cURL example
  [Accordion title="Form POST" icon="fa-code"] — HTML form POST example *if applicable*

H2: Handle the Callback
  [prose] — what PayU POSTs to surl/furl
  [table] — callback fields
  [Accordion title="Verify the response hash" icon="fa-shield-halved"] — reverse hash code

H2: Verify the Payment Server-Side
  [Accordion title="Verify Payment API" icon="fa-circle-check"] — cURL example

H2: Test Credentials
  [table] — test values for this integration

H2: Related Resources
  [Cards columns=2] × 2–3
```

---

### Build Integration — navigator index (use when product has per-method pages)

```
[frontmatter]

H1: Build the Integration

H2: Endpoints
  [table] — Environment | URL
  [Callout warn] — note any methods that use a different endpoint

H2: Choose a Payment Method
  [Cards columns=2] — one Card per supported method, with pg/bankcode and link

H2: Before You Start
  [Accordion title="Credentials" icon="fa-key"] — test key/salt retrieval
  [Accordion title="Hash generation" icon="fa-shield-halved"] — formula + server-side rule
  [Accordion title="Callback URL requirements" icon="fa-link"] — surl/furl rules
  [Accordion title="Post-payment verification" icon="fa-circle-check"] — verify every payment server-side
```

---

### Build Integration — payment method page (one per method, for per-method products)

```
[frontmatter]
[Callout warn]   *include only if method requires activation, restricted MCC, or special prerequisites*

H1: {Method Name}

[prose] — 1 sentence: what this method is + pg and bankcode values

H2: {Pre-step name}   *include only if the method has a mandatory pre-step (OTP, balance check, VPA validation, etc.)*
  [Accordion title="Request" icon="fa-code"] — endpoint + params + cURL
  [Accordion title="Response" icon="fa-table"] — response fields table

H2: Post the Payment Request
  [table] — endpoint (test + production)
  H3: Mandatory Parameters
    [table] — Parameter | Type | Description | Example
  H3: Optional Parameters
    [table] — Parameter | Type | Description | Example
  [Accordion title="cURL" icon="fa-code"]
  [Accordion title="Form POST" icon="fa-code"]   *if applicable*

H2: Handle the Callback
  [prose] — callback field overview
  [Accordion title="Verify the response hash" icon="fa-shield-halved"] — reverse hash code

H2: Verify the Payment Server-Side
  [Accordion title="Verify Payment API" icon="fa-circle-check"] — cURL example

H2: Test Credentials
  [table] — test values specific to this method

H2: Related Resources
  [Cards columns=2] × 2–3

+ [add method-specific H2s — e.g. "Decryption" for Apple Pay, "splitInfo structure" for Rewards SPLITPAY]
```

---

### Test Integration — `test-integration.md`

```
[frontmatter]
[Callout warn] — "Use test credentials only"

H1: Test Your Integration

H2: Test Credentials
  [KeySaltReference custom block]

H2: Test Credentials by Payment Method   *include only for multi-method products*
  H3: {Method Name} × n
    [table] — test values for this method

H2: Test Scenarios
  [Accordion title="Successful payment" icon="fa-circle-check"]
    → trigger + expected callback status
  [Accordion title="Failed / declined payment" icon="fa-xmark"]
    → trigger + expected status
  [Accordion title="Pending / timeout" icon="fa-clock"]
    → when this occurs + how to handle
  [Accordion title="Hash mismatch" icon="fa-shield-halved"]
    → what triggers E501 + how to debug
  [Accordion title="Duplicate txnid" icon="fa-copy"]
    → what happens + how to avoid
  + [method-specific scenarios from source files]
```

---

### Go-Live Checklist — `go-live-checklist.md`

```
[frontmatter]

H1: Go-Live Checklist

[prose] — 1 sentence: complete this before switching to production

[Accordion title="Update credentials" icon="fa-key"]
  → switch from test key/salt to live key/salt; update endpoint to production URL

[Accordion title="Security" icon="fa-shield-halved"]
  → hash always server-side, salt never in frontend, HTTPS everywhere
  → PCI-DSS SAQ A-EP if collecting card data *include only if applicable*

[Accordion title="Callback URLs" icon="fa-link"]
  → surl and furl publicly reachable over HTTPS; configure webhooks as fallback

[Accordion title="Error handling" icon="fa-triangle-exclamation"]
  → all error states handled; never trust callback alone; server-side verify on every transaction

[Accordion title="Payment method coverage" icon="fa-credit-card"]
  → all integrated methods tested end-to-end in production environment

[Accordion title="PayU Dashboard access" icon="fa-gauge"]
  → verify Dashboard login, settlement and reporting config, webhook subscription

+ [product-specific checklist items from source material]
```

---

### Errors & Troubleshooting — `errors-and-troubleshooting.md`

```
[frontmatter]

H1: Errors & Troubleshooting

H2: Quick Reference
  [table] — Error code | Meaning | Fix (1-line each) — 5–8 most common errors from source files

H2: Hash Errors
  [Accordion title="E501 — hash mismatch" icon="fa-shield-halved"]
    → causes + step-by-step fix
  [Accordion title="Hash is empty" icon="fa-shield-halved"]
    → causes + fix

H2: Parameter Errors
  [Accordion title="Missing mandatory parameters" icon="fa-table"]
    → which params are mandatory + what error each missing param produces
  [Accordion title="Duplicate txnid" icon="fa-copy"]
    → cause + fix
  [Accordion title="Wrong pg or bankcode" icon="fa-credit-card"]   *include only for multi-method products*
    → cause + fix

H2: Callback Issues
  [Accordion title="surl not received" icon="fa-link"]
    → common causes + fix
  [Accordion title="Pending status at surl" icon="fa-clock"]
    → what pending means + how to handle (verify server-side, do not fulfil order)
  [Callout warn] — "Pending is not a success. Never fulfil an order on pending status."

H2: Payment Failures
  [Accordion title="E002 — bank declined" icon="fa-xmark"]
    → causes + what to show the user
  [Accordion title="Callback and verify status mismatch" icon="fa-triangle-exclamation"]
    → why this happens + which source to trust (always Verify Payment API)

+ [product-specific error categories from source files]
```

---

### FAQs — `faqs.md`

```
[frontmatter]

H1: FAQs — {Product Name}

[Accordion title="How does {Product} differ from {alternative}? When should I use each?" icon="fa-circle-question"]
[Accordion title="Do I need PCI-DSS compliance?" icon="fa-shield-halved"]   *adapt or omit if product never touches card data*
[Accordion title="Should I generate the hash on the frontend or backend?" icon="fa-code"]
[Accordion title="How do I handle the pending status?" icon="fa-clock"]
[Accordion title="What happens if the customer closes the browser before the redirect?" icon="fa-browser"]
[Accordion title="How is surl/furl different from webhooks? Which is more reliable?" icon="fa-plug"]
[Accordion title="How do I enable specific payment methods?" icon="fa-toggle-on"]   *include only for multi-method products*
[Accordion title="What is the production endpoint?" icon="fa-server"]
[Accordion title="How do I debug a hash mismatch?" icon="fa-bug"]

+ [product-specific FAQs from source files — mark new content]
```

---

### API Reference Index — `{product}-apis.md`

```
[frontmatter]

H1: {Product Name} APIs

[prose] — 1 sentence: APIs used in this integration

H2: Payment APIs
  [Cards columns=2] — one Card per payment/initiation endpoint

H2: Post-Payment APIs
  [Cards columns=2] — Verify Payment, Get Transaction Info, Refund, any product-specific post-payment API

H2: API Quick Reference
  [table] — API name | command value (if applicable) | Hash formula | Link

+ [product-specific API sections from source files]
```

---

## Frontmatter Schema

Every page must include this frontmatter. Do not omit any field.

```yaml
---
title: {Page Title}
excerpt: {One-sentence description of what this page covers}
deprecated: false
hidden: false
updatedAt: "YYYY-MM-DD"
metadata:
  title: {SEO title} | PayU Developer Docs
  description: >-
    {150–160 char SEO description}
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---
```

**Rules:**
- `title` — matches the H1 heading
- `excerpt` — one sentence, no trailing period
- `deprecated: false` and `hidden: false` for all new pages
- `updatedAt` — the date the file is created/updated, `YYYY-MM-DD`
- `metadata.robots: index` for all new pages
- `agentTools.projectIndex` — always `"https://docs.payu.in/llms.txt"` exactly as shown

---

## ReadMe Component Reference

Always use ReadMe's native components. Do not use raw HTML for structure that a component handles.

### Accordion

```mdx
<Accordion title="Step 1: Do something" icon="fa-circle-1">

Content here.

</Accordion>
```

**Icon conventions:** Steps → `fa-circle-1` … `fa-circle-9`. Parameters → `fa-table`. Code → `fa-code`. Security → `fa-shield-halved`. Key/credentials → `fa-key`. Verification → `fa-circle-check`. Warning → `fa-triangle-exclamation`.

### Cards

```mdx
<Cards columns={2}>
  <Card title="Card Title" icon="fa-icon-name" href="./relative-link">
    One or two sentence description.
  </Card>
</Cards>
```

Column guidelines: 2 columns for navigation cards, 3 columns for feature/use case cards.

### Callout

```mdx
<Callout icon="⚠️" theme="warn">Warning message.</Callout>
<Callout icon="📘" theme="info">Info message.</Callout>
<Callout icon="👍" theme="okay">Success/positive message.</Callout>
```

Theme values: `warn` (yellow), `info` (blue), `okay` (green), `default` (grey).

### Banner

Use only on `index.md` (overview page). Never on subpages.

```mdx
<Banner
  isInline={true}
  message="Integration effort: {description}"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>
```

Colour by tier: Tier 1 (No-code) `#0066FF` · Tier 2 (Low-code) `#FF6B00` · Tier 3 (High-code) `#15C614`.

### Tabs / Tab

```mdx
<Tabs>
  <Tab title="Node.js">
    ```javascript
    // code
    ```
  </Tab>
  <Tab title="PHP">
    ```php
    // code
    ```
  </Tab>
</Tabs>
```

### Custom blocks

Reference existing blocks from `custom_blocks/` rather than duplicating content:

| Block | Use |
|---|---|
| `<KeySaltReference />` | Test key/salt retrieval instructions |
| `<HashingSample />` | Hash generation in multiple languages |
| `<HashingRequestParameters />` | Hash parameter description |
| `<Postman_collection />` | Postman collection link |

---

## Content Accuracy Rules

These rules are non-negotiable.

### Do not invent

Never generate content for any of the following unless it exists verbatim in the source files:

- API endpoints (URLs, paths)
- Request parameters (names, types, required/optional, character limits)
- Response fields and their values
- Error codes and their meanings
- `pg` and `bankcode` values
- Test credentials (card numbers, VPAs, OTPs, mobile numbers)
- Dashboard functionality or navigation paths
- PCI-DSS or regulatory requirements
- Hash formulas or field ordering

### Flag gaps

```markdown
<!-- DOCUMENTATION GAP: [what is missing and where to find it] -->
```

A gap comment is always better than invented content.

### Flag contradictions

```markdown
<!-- VALIDATION NEEDED: [describe the contradiction and which files conflict] -->
```

Do not pick one version silently — flag for the docs team.

### Mark new content

```markdown
<!-- NEW CONTENT: [reason — e.g. "standard pattern applied to all payment methods"] -->
```

---

## Deprecating Legacy Pages

After all new content is written and redirect targets confirmed:

**Step 1 — Update frontmatter:**
```yaml
deprecated: true
hidden: true
metadata:
  robots: noindex
```

**Step 2 — Add redirect Callout as the first body element:**
```mdx
<Callout icon="🔀" theme="warn">
  **This page has moved.** The updated guide is at [{New Page Title}](./{new-page-slug}).
</Callout>
```

Keep all original content below the Callout. Never delete legacy content.

---

## Git Workflow

**Branch naming:** `docs/restructure-{product-slug}`

**Commit messages:** `Restructure {Product Name} — {what was done}`

**PR title:** `[Docs] Restructure {Product Name} to Tier 2 IA`

**PR description must include:**
- List of new pages created
- List of deprecated pages and their redirect destinations
- List of `<!-- DOCUMENTATION GAP -->` comments that need resolution
- List of `<!-- VALIDATION NEEDED -->` comments that need resolution

One product per branch.

---

## Pre-Submission Checklist

**Structure**
- [ ] All approved pages exist — no pages added or removed from the approved IA
- [ ] All `_order.yaml` files list the correct slugs in the correct order
- [ ] No pages created outside the approved structure

**Content outlines**
- [ ] Every page contains only the H2/H3 headings from the approved content outline
- [ ] No sections added or removed without re-approval

**Frontmatter**
- [ ] All new pages: `deprecated: false`, `hidden: false`, `metadata.robots: index`
- [ ] All new pages: `updatedAt` set to today's date
- [ ] All new pages: `agentTools.projectIndex: "https://docs.payu.in/llms.txt"`

**Content accuracy**
- [ ] No invented APIs, parameters, endpoints, or test credentials
- [ ] All gaps flagged with `<!-- DOCUMENTATION GAP -->`
- [ ] All contradictions flagged with `<!-- VALIDATION NEEDED -->`
- [ ] New content marked with `<!-- NEW CONTENT -->`

**Legacy pages**
- [ ] Every migrated source page has `deprecated: true`, `hidden: true`, `robots: noindex`
- [ ] Every deprecated page has the redirect Callout as its first body element

**Components**
- [ ] All Accordions have `title` and `icon` attributes
- [ ] All Cards have `title` and `href` attributes
- [ ] Banner used only on `index.md`, not subpages

**Hash formula**
- [ ] SHA-512 request hash verified against source files
- [ ] Reverse hash verified against source files

---

*Template version: v2026-11. Maintained by PayU Developer Docs team.*
