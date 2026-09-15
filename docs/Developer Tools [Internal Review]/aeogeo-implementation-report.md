---
title: AEO/GEO Implementation Report
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
**Based on:** _Measuring AI Share of Voice for API Products: Lessons from AEO/GEO Practitioners_ (Pronovix)
**Archive analysed:** `payu_hosted_checkout_v1_2026_09_08t08_40_43_3641a3a.zip` — **1,542 .md files**

***

## Article Core Thesis

AI search systems (ChatGPT, Perplexity, Claude, Gemini) increasingly answer developer questions about payment APIs. Which vendor gets cited depends on four things:

1. Whether documentation is **crawlable and machine-readable** by AI agents
2. Whether content **maps API capabilities to business problems** explicitly
3. Whether **metadata, structure, and FAQ/Q\&A patterns** match how LLMs extract answers
4. Whether you have **measurable baselines and run small, targeted interventions**

The article recommends: _pick capabilities → measure AI share of voice → inspect gaps → intervene → re-measure._

***

## Overall Scorecard — PayU DevGuide Today

| Signal                            | Status | Score | Notes                                         |
| --------------------------------- | ------ | ----- | --------------------------------------------- |
| Crawlability (robots metadata)    | ✅      | 8/10  | 1,337 files carry `robots: index`             |
| Metadata descriptions             | ❌      | 2/10  | 838/1,542 files (54%) missing descriptions    |
| Keywords metadata                 | ❌      | 4/10  | 575 files (37%) missing keywords              |
| FAQ / Q\&A content                | ❌      | 1/10  | Only 19/1,542 files have FAQs (1.2%)          |
| Business framing / "why use this" | ❌      | 3/10  | 567 pages with no benefit language            |
| Structured data (JSON-LD schema)  | ❌      | 0/10  | Zero files with schema markup                 |
| llms.txt / agent discoverability  | ❌      | 0/10  | No llms.txt exists                            |
| Response examples                 | ✅      | 7/10  | 535 files have sample responses               |
| Error code documentation          | ✅      | 6/10  | 453 files cover errors                        |
| Rate limiting docs                | ❌      | 2/10  | Only 18 files cover rate limits               |
| Thin content management           | ⚠️     | 4/10  | 486 thin files; some critical stubs           |
| Content governance / stale docs   | ⚠️     | 5/10  | RECYCLE BIN + Internal Review folders present |
| Changelog / release notes         | ❌      | 1/10  | Only 8 files; no public changelog             |
| Agentic / MCP readiness           | ⚠️     | 4/10  | MCP section started but thin                  |
| Glossary / terminology coverage   | ⚠️     | 5/10  | 75/1,542 files tagged; needs wider rollout    |

**Overall AI Visibility Score: 3.7 / 10** — Significant opportunity to improve.

***

## Pillar 1 — Machine Readability & Crawlability

> _Article: "Ensure your developer portal is accessible to AI crawlers. Use structured data and machine-readable discovery files."_

**What the devguide has:**

- ✅ 1,337 files carry `robots: index` frontmatter
- ✅ Only 4 files marked `robots: noindex` (all in RECYCLE BIN / legacy reference)
- ❌ **ZERO** files contain JSON-LD schema markup (FAQPage, HowTo, Article, SoftwareApp)
- ❌ **No&#x20;**`llms.txt` file exists
- ❌ No `sitemap.xml` or `robots.txt` visible in archive

**What to implement:**

| ID   | Action                                                                                                                       | Files      | Priority    |
| ---- | ---------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------- |
| P1-A | Create `llms.txt` for docs root listing all key integration pages by capability                                              | 1 new      | 🔴 CRITICAL |
| P1-B | Add JSON-LD `FAQPage` schema to all FAQ files; `HowTo` to all step-by-step guides (203 files); `Article` to conceptual pages | 200+       | 🔴 HIGH     |
| P1-C | Add `SoftwareApplication` schema to key Offerings index pages                                                                | 25 pages   | 🔴 HIGH     |
| P1-D | Audit `hidden: true` pages — ensure legitimate offering pages are not blocked (found on `nbbl-overview.md`)                  | Review all | 🟡 MEDIUM   |

**Sample&#x20;**`llms.txt`**&#x20;structure for PayU:**

```
# PayU Developer Documentation
> PayU is India's leading payment gateway. Integrate to accept payments via cards, UPI, net banking, wallets, EMI, BNPL, and more.

## Key Integration Guides
- Dynamic Currency Conversion (DCC): /docs/Offerings/introduction-dynamic-currency-conversion/
- Third Party Verification (TPV): /docs/Offerings/introduction-to-payu-tpv/
- Pre-Authorization (Auth & Capture): /docs/Offerings/auth-and-capture-pre-authorize-card-payments/
- Recurring Payments: /docs/Offerings/introduction-recurring-payments-integration/
- Refunds API: /docs/Offerings/introduction-refunds/
- Tokenization / Save Cards: /docs/Offerings/introduction-save-cards/
- Split Settlements: /docs/Offerings/split-settlments/
```

***

## Pillar 2 — Metadata Completeness _(Highest Impact)_

> _Article: "Meta descriptions are extracted directly into AI-generated summaries. Missing metadata = invisible to LLMs."_

**What the devguide has:**

- ❌ **838 of 1,542 files (54%)** missing meta description
- ❌ **575 files (37%)** missing keywords metadata
- ❌ **163 index/landing pages** missing description
- ❌ **Every single Offerings page** (305 files) is missing description + keywords

**Entire Offerings sections with zero metadata descriptions:**

- `introduction-dynamic-currency-conversion/` (entire section)
- `auth-and-capture-pre-authorize-card-payments/` (entire section)
- `introduction-to-payu-tpv/` (entire section)
- `introduction-to-eftnet/` (entire section)
- `introduction-recurring-payments-integration/` (entire section)
- `introduction-to-affordability/` (entire section)
- `introduction-save-cards/` (entire section)
- `chargeback/` (entire section)
- `split-settlments/` (entire section)
- `virtual-cards-introduction/` (entire section)

**What to implement:**

| ID   | Action                                                               | Files | Priority  |
| ---- | -------------------------------------------------------------------- | ----- | --------- |
| P2-A | Write meta descriptions + keywords for all 305 Offerings pages       | 305   | 🔴 HIGH   |
| P2-B | Apply to Collect Payments (302 files) and getting started (61 files) | 363   | 🟡 MEDIUM |

**Template per page:**

```yaml
metadata:
  description: "Learn how to integrate [Feature] with PayU. [1-sentence business benefit].
                Supports [payment methods]. Step-by-step API guide with code examples."
  keywords:
    - "[feature] integration"
    - "PayU [feature] API"
    - "[use case keyword]"
```

***

## Pillar 3 — Capability → Business Problem Mapping

> _Article: "The biggest gap in competitive benchmarks: API capabilities are documented but NOT connected to business outcomes. LLMs cite sources that answer 'what problem does this solve?' — not just 'here is how the API works'."_

**What the devguide has:**

- ❌ **567 pages (37%)** have NO "why use / benefit / business framing" language
- ❌ **353 integration pages** have no use-case or scenario context
- ❌ **120 step-by-step guides** have no use-case introductions
- ✅ 426 pages do contain some use-case language (good base)

**Specific capability framing gaps:**

| Offering           | Missing Business Context                                                              |
| ------------------ | ------------------------------------------------------------------------------------- |
| DCC                | "Increase revenue from international customers — accept USD, GBP, AED, settle in INR" |
| TPV                | "Mandatory for stockbrokers and mutual funds per SEBI regulations"                    |
| Pre-Authorization  | "Used in hotel bookings, car rentals, and security deposit scenarios"                 |
| EFTNET / NEFTRTGS  | "For large-value B2B transfers and wire payment use cases"                            |
| Tokenization       | "Reduce cart abandonment with one-click checkout; no re-entry of card details"        |
| Recurring Payments | "Enable subscription revenue, auto-collect loan EMIs, reduce churn"                   |

**What to implement:**

| ID   | Action                                                                  | Files | Priority  |
| ---- | ----------------------------------------------------------------------- | ----- | --------- |
| P3-A | Add "## Why Use \[Feature]?" section to all 25+ Offerings index pages   | 25    | 🔴 HIGH   |
| P3-B | Add capability→business framing lead sentence to every integration page | 567   | 🟡 MEDIUM |
| P3-C | Add product-specific framing to DCC, TPV, Pre-Auth, EFTNET pages        | \~40  | 🔴 HIGH   |

**Template:**

```markdown
## Why Use [Feature Name]?

[Feature] helps you [business outcome]. Use this when:
- You need to [scenario 1, e.g., accept payments in multiple currencies]
- Your customers want to [scenario 2]
- You are a [merchant type, e.g., stockbroker, hotel, subscription business]
```

***

## Pillar 4 — FAQ / Q\&A Content _(Highest AI Citation Signal)_

> _Article: "FAQ-structured content is the single most cited format in AI-generated answers. LLMs are optimised to extract discrete Q\&A pairs. Lowest effort, highest impact."_

**What the devguide has:**

- ❌ Only **19 of 1,542 files (1.2%)** have FAQ sections
- ❌ **55 Offerings index pages** have no FAQ link or FAQ content
- ❌ Existing FAQ files use **prose paragraphs**, not H3 Q\&A pairs
- ✅ Some FAQ files exist for DCC, TPV, Shopify, Magento — good starting points

**What to implement:**

| ID   | Action                                                                                                                           | Files    | Priority    |
| ---- | -------------------------------------------------------------------------------------------------------------------------------- | -------- | ----------- |
| P4-A | Reformat existing 19 FAQ files into strict `### Question` / Answer pairs                                                         | 19       | 🔴 CRITICAL |
| P4-B | Add 5+ FAQ Q\&As to every Offerings index page (DCC, TPV, Pre-Auth, EFTNET, Recurring, Tokenization, Refunds, Split Settlements) | 25 pages | 🔴 HIGH     |
| P4-C | Create new FAQ files for Apple Pay, Pre-Auth, EFTNET, Virtual Cards, Chargeback, NBBL                                            | 6 new    | 🟡 MEDIUM   |

**Format every Q as a natural language ChatGPT-style query:**

```markdown
### What currencies does PayU DCC support?
PayU's DCC supports over 20 currencies including USD, GBP, EUR, AED, and SGD.
Merchants receive settlement in INR regardless of the currency the customer pays in.

### Is TPV mandatory for all PayU merchants?
TPV (Third Party Verification) is mandatory for stockbrokers and mutual fund platforms
operating under SEBI regulations in India. It validates that the customer's bank account
matches the one registered with the merchant before debiting funds.
```

***

## Pillar 5 — Thin Content & Stub Pages

> _Article: "Thin pages dilute domain authority signals. AI systems de-prioritise sources with many low-content pages."_

**What the devguide has:**

- ❌ **486 files under 300 words** (31% of all files)
- ❌ **143 non-custom-block pages under 200 words**
- ❌ Critical pages with almost no content:

| File                                            | Words  | Impact                              |
| ----------------------------------------------- | ------ | ----------------------------------- |
| `custom_pages/quick-start.md`                   | 11     | 🔴 Developer onboarding entry point |
| `Collect Payments/introduction-web/webhooks.md` | 16     | 🔴 Heavily searched topic           |
| `getting started/register-with-payu/index.md`   | 17     | 🔴 First-touch page for new devs    |
| `Collect Payments/.../upi-intent.md`            | 18     | 🟡 High-traffic payment method      |
| `Collect Payments/.../net-banking.md`           | 19     | 🟡 High-traffic payment method      |
| 14× Split Settlements dashboard pages           | 50–150 | 🟡 Dilutes section authority        |

**What to implement:**

| ID   | Action                                                                               | Files | Priority  |
| ---- | ------------------------------------------------------------------------------------ | ----- | --------- |
| P5-A | Expand all stub pages (\< 100 words): add intro, prerequisites, sub-page links       | 143   | 🟡 MEDIUM |
| P5-B | Prioritise: `webhooks.md`, `quick-start.md`, `register-with-payu/index.md`           | 5     | 🔴 HIGH   |
| P5-C | Expand 14 Split Settlements dashboard stubs with steps + screenshots + "What's next" | 14    | 🟡 MEDIUM |

***

## Pillar 6 — Content Governance & Consistency

> _Article: "Inconsistent or stale content causes AI systems to generate incorrect answers about your API."_

**What the devguide has:**

- ⚠️ `RECYCLE BIN/` folder (17 files) present and potentially crawlable
- ⚠️ `Docs For Internal Review/` (20 files) + `Developer Tools [Internal Review]/` (31 files) — risk of incomplete docs being indexed
- ⚠️ `AIR India/` specific content (13 files) — may confuse AI answers about PayU
- ❌ Only **8 files** mention changelog or release notes — no public changelog
- ❌ **1,327 files** mention "deprecated" but without structured banners or migration paths

**What to implement:**

| ID   | Action                                                                    | Files | Priority  |
| ---- | ------------------------------------------------------------------------- | ----- | --------- |
| P6-A | Add `robots: noindex` to RECYCLE BIN, Internal Review, AIR India folders  | \~51  | 🔴 HIGH   |
| P6-B | Create a public **Changelog / Release Notes** page with dated API changes | 1 new | 🟡 MEDIUM |
| P6-C | Add `<Callout>` deprecation banners with sunset dates and migration links | 50+   | 🟢 LOW    |
| P6-D | Publish or fully hide 'Docs For Internal Review' sections                 | \~51  | 🔴 HIGH   |

***

## Pillar 7 — Response Examples & Error Docs

> _Article: "AI systems favour complete, evidence-rich answers. Show the full request AND response, plus what can go wrong."_

**What the devguide has:**

- ✅ 535 files have sample responses
- ✅ 453 files cover error codes
- ❌ **210 files** have code blocks but **no sample response**
- ❌ **55 integration guides** have code but **no error handling docs**
- ❌ Only **18 files** cover rate limiting
- ❌ **No canonical Error Codes Reference page** exists

**What to implement:**

| ID   | Action                                                                                               | Files | Priority  |
| ---- | ---------------------------------------------------------------------------------------------------- | ----- | --------- |
| P7-A | Add success + failure response examples to 210 code pages (priority: EFTNET, TPV, Pre-Auth)          | 210   | 🟡 MEDIUM |
| P7-B | Create a canonical **Error Codes Reference** page listing all PayU error codes with resolution steps | 1 new | 🟡 MEDIUM |
| P7-C | Add rate limiting, retry, and idempotency sections to all API integration pages                      | 50+   | 🟢 LOW    |

***

## Pillar 8 — Agentic Readiness _(Forward-Looking)_

> _Article: "Gaps that limit AI representation often also make it harder for AI agents to work with your API. Agentic readiness is the next frontier."_

**What the devguide has:**

- ✅ MCP & CLI section exists (5 files) — forward-thinking
- ✅ Integration ASK AI Docs section (13 files) — pilot in place
- ✅ 26 files reference OpenAPI/Swagger specs
- ❌ No `llms.txt` for agent-based discovery
- ❌ OpenAPI specs not consistently linked from integration pages

**What to implement:**

| ID   | Action                                                    | Priority  |
| ---- | --------------------------------------------------------- | --------- |
| P8-A | Expand MCP & CLI into a full "AI Agent Integration Guide" | 🟡 MEDIUM |
| P8-B | Publish and maintain `llms.txt` at docs root              | 🟡 MEDIUM |
| P8-C | Link OpenAPI specs from every integration landing page    | 🟢 LOW    |

***

## Prioritised Implementation Roadmap

### Phase 1 — Quick Wins (2–4 weeks)

| ID   | Action                                                        | Files | Priority    |
| ---- | ------------------------------------------------------------- | ----- | ----------- |
| P1-A | Create `llms.txt` for docs root                               | 1 new | 🔴 CRITICAL |
| P4-A | Reformat 19 existing FAQ files into H3 Q\&A pairs             | 19    | 🔴 CRITICAL |
| P2-A | Write meta descriptions for all 305 Offerings pages           | 305   | 🔴 HIGH     |
| P3-A | Add "Why Use This?" section to all Offerings index pages      | 25    | 🔴 HIGH     |
| P6-A | Add `robots: noindex` to RECYCLE BIN + Internal Review        | \~51  | 🔴 HIGH     |
| P5-B | Expand 5 critical stub pages (webhooks, quickstart, register) | 5     | 🔴 HIGH     |

### Phase 2 — Medium Term (1–2 months)

| ID   | Action                                                                      | Files | Priority  |
| ---- | --------------------------------------------------------------------------- | ----- | --------- |
| P1-B | Add JSON-LD schema (FAQPage, HowTo, Article)                                | 200+  | 🔴 HIGH   |
| P4-B | Add 5 FAQ Q\&As to every Offerings index page                               | 25    | 🔴 HIGH   |
| P4-C | New FAQ files: Apple Pay, Pre-Auth, EFTNET, Virtual Cards, Chargeback, NBBL | 6 new | 🟡 MEDIUM |
| P3-B | Add capability→business framing to 567 pages                                | 567   | 🟡 MEDIUM |
| P7-B | Create canonical Error Codes Reference page                                 | 1 new | 🟡 MEDIUM |
| P7-A | Add failure response examples to 210 code pages                             | 210   | 🟡 MEDIUM |
| P6-B | Create public Changelog / Release Notes page                                | 1 new | 🟡 MEDIUM |
| P2-B | Meta descriptions for Collect Payments + Get Started                        | 363   | 🟡 MEDIUM |

### Phase 3 — Strategic (2–3 months)

| ID   | Action                                            | Files   | Priority  |
| ---- | ------------------------------------------------- | ------- | --------- |
| P8-A | Full MCP / AI Agent Integration Guide             | 1 new   | 🟡 MEDIUM |
| P8-B | Publish and maintain `llms.txt`                   | ongoing | 🟡 MEDIUM |
| P5-A | Expand all 143 thin core pages                    | 143     | 🟡 MEDIUM |
| P7-C | Rate limiting docs on all API pages               | 50+     | 🟢 LOW    |
| P6-C | Deprecation banners + migration guides            | 50+     | 🟢 LOW    |
| P8-C | Link OpenAPI specs from integration landing pages | 26+     | 🟢 LOW    |

***

## AI Share of Voice Measurement — Baseline Prompts for PayU

Run these across ChatGPT, Perplexity, Claude, and Gemini. Record whether PayU is mentioned, cited as a source, and whether the answer is accurate.

**Branded prompts:**

- "How do I integrate PayU for international payments?"
- "Does PayU support Dynamic Currency Conversion (DCC)?"
- "How does PayU pre-authorization work?"
- "What is PayU TPV and how do I integrate it?"
- "PayU recurring payments integration guide"

**Non-branded (competitive) prompts:**

- "Which Indian payment gateway supports DCC?"
- "How to accept international card payments in India?"
- "Best payment gateway for stockbrokers in India"
- "How to implement UPI autopay for subscriptions in India?"
- "Payment gateway with pre-authorization support India"

> **Process:** Baseline now → implement Phase 1 → re-measure → repeat quarterly.
