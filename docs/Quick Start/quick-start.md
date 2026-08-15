---
title: ' Quick Start — Accept Payments with PayU'
excerpt: >-
  Answer a couple of quick questions and we will show you exactly what to do
  next — no technical background needed.
deprecated: false
hidden: true
metadata:
  robots: index
---
{/* ENGINEERING NOTES (delete before publishing): 1. <PayUIntegrationPathRecommender /> must be rebuilt to the decision tree below exactly. Q4 never changes the recommended product — presentation only. 2. Two product names below are placeholders pending Product/Documentation naming validation: - [Merchant Hosted Checkout / Seamless Checkout — CONFIRM NAME] - [Pay Handle / Payment Links — CONFIRM NAME] Do not pick one unilaterally; both appear bracketed below until resolved. 3. The GoQwik-related flow (and any product outside the standard Merchant Key + Salt model) is NOT represented in this tree. [REQUIRES ENGINEERING VALIDATION] before it can be added — do not assume it fits an existing branch. 4. Testing claim below is deliberately softened to avoid the "zero-KYC across all products" claim flagged as possibly false. Do not strengthen this copy until Product confirms per-product testing/KYC behavior. */}

## Let's Get You Accepting Payments

PayU helps you accept money from customers and get it into your bank account. Answer a couple of quick questions and we will show you exactly what to do next — you do not need any technical background to get started.

Already started? Continue where you left off →

## What are you trying to do?

Let us know what are you trying to do:

I have a website and want customers to pay online
I don't have a website and want to send customers a payment link
I want to accept payments in person — shop, counter, or kiosk
I want to charge customers regularly — subscriptions or memberships
I run a platform or marketplace where multiple sellers get paid
I'm not sure what I need

Just answer honestly — there's no wrong choice here, and you can change your answers anytime.

<PayUIntegrationPathRecommender />

{/* Full decision tree the component must implement: Q1 "What are you trying to do?" - Website → Q2 - Payment link (no website) → Result: [Pay Handle / Payment Links] - In person → Result: UPI QR - Recurring/subscriptions → Result: Recurring Payments → Q4 - Platform/marketplace → Result: Server-to-Server/Split Settlement → Q4 - Not sure → Q1-fallback Q1-fallback "What are you using today — website, social/messaging, in person, or nothing yet?" → maps to same 5 outcomes as Q1 - Still unsure → exits to Ask AI Q2 (only if Q1 = Website) "Is your website on a store platform like Shopify or WooCommerce, or is it custom-built?" - Store platform → Q2a - Custom-built → Q2b - No website yet → Result: [Pay Handle / Payment Links] (bridge framing: "a way to start collecting money now, while your site is being built") Q2a (only if Q2 = store platform) "Which platform?" - Shopify / WooCommerce / Magento / Other → Result: matching plugin, terminal, no Q4 Q2b (only if Q2 = custom-built) "Does the payment page need to match your site exactly?" - Simple PayU page is fine → Result: PayU Hosted Checkout → Q4 - Needs exact match → Result: [Merchant Hosted Checkout / Seamless Checkout] → Q4 - Not sure → Result: PayU Hosted Checkout (default) → Q4, with note: "Most merchants start here — you can add full design control later." Q4 (only after custom-website, recurring, or platform/marketplace results — never after plugin, Pay Handle, or UPI QR) "Who's setting this up? (This changes how we present the next step — not what we recommend.)" - I'll do it myself → guided setup inline - I have a developer → Send This to Your Developer - I'll use an AI assistant → Build with AI - Not sure → guided setup (default) + handoff note */}

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

Recommendation card, shown once a result resolves:

Your recommended setup \[product name in plain language]

Why we're recommending this \[one to two sentences tied to the specific answers given]

What you'll need \[filtered to this path only]

How it will be set up \[one line matching the Q4 answer, or omitted entirely for plugin/Pay Handle/UPI QR results]

\[Start setup →]

Why this recommendation? (expandable) · \[Change my answers]

"Change my answers" reopens at the earliest question that would change the current result — never a full restart.

Prefer to browse instead? See all ways to accept payments with PayU →

Your journey from here

Choose → Prepare → Build → Test → Go live → First payment

Testing before you go live

You can try most PayU setups safely before using them with real customers. \[TO CONFIRM: which products this applies to and whether any require verification first — do not state this applies universally until Product confirms]

See test details →

Ask AI

Not sure any of this applies to you? Describe your business in your own words.

Ask AI →

Get help

Postman Collection · Troubleshooting & error codes · FAQs · Contact support
