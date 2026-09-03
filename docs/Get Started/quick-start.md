---
title: Start Here
excerpt: Answer a couple of quick questions and we'll show you exactly what to do next.
deprecated: false
hidden: true
metadata:
  title: Start Here — PayU Developer Docs
  description: >-
    New to PayU? Find the right payment integration for your business in
    minutes. From no-code payment links to fully custom checkout — this page
    helps you choose the path that fits your needs and get to your first payment
    faster.
  keywords:
    - payu integration guide
    - payu getting started
    - payu payment gateway setup
    - choose payu integration
    - payu quick start
    - payu payment links
    - payu hosted checkout
    - payu merchant hosted checkout
  robots: index
---
{/*
=============================================================================
CONTENT PROVENANCE — for SME / editorial review
=============================================================================
SOURCE       — drawn from an existing repo file (path shown).
               Lightly rewritten for tone and clarity; facts unchanged.
NEW CONTENT  — written fresh; no equivalent exists in the repo.
               Must be validated by a PayU SME before publishing.
=============================================================================
*/}

{/* NEW CONTENT — the existing introduction/index.md opens with a generic
     "what is a payment gateway" definition and a bullet list of benefits.
     That content is too generic and marketing-heavy for a decision-making
     entry point. The paragraphs below are rewritten to be lean, honest,
     and action-oriented. Needs SME review for accuracy and brand tone. */}

PayU lets you accept payments from customers across India — UPI, cards, net banking, wallets, EMI, and more. Whether you want to share a payment link with no technical setup, add a checkout to your website, or build a fully custom payment flow, PayU has an integration that fits.

Not sure which one is right for you? Answer three quick questions and we'll point you to the right path.

***

{/* SOURCE — wizard component reference.
     The PayUQuickStartWizard component is defined and specced in:
     docs/Quick Start/quick-start.md (currently hidden=true).
     The component handles the full decision tree, product recommendation,
     effort labelling, prerequisites, and "how do you want to proceed" panels.
     It should be rendered inline here (not as a modal launch button). */}

<PayUQuickStartWizard />

***

{/* NEW CONTENT — the static fallback table below does not exist in this
     form in the repo. The product names, effort labels, and doc URLs are
     sourced from the wizard's product catalog (PayUQuickStartWizard component
     data). The table structure and "prefer to browse" framing are new.
     Needs SME review to confirm doc URLs and effort labels are current. */}

## Prefer to browse? All integration paths at a glance

If you already know what you need, go directly to the right guide.

| What you want to do                      | PayU solution            | Effort                  | Guide                                                                 |
| ---------------------------------------- | ------------------------ | ----------------------- | --------------------------------------------------------------------- |
| Share a payment link — no website needed | Payment Links            | 🟢 No coding required   | [Payment Links](doc:payment-links-dashboard)                          |
| Accept payments in person via QR         | UPI QR Code              | 🟢 No coding required   | [UPI QR](doc:integrate-upi-qr)                                        |
| Add checkout to a Shopify store          | Shopify Plugin           | 🟡 Some technical setup | [Shopify Plugin](doc:shopify)                                         |
| Add checkout to a WooCommerce store      | WooCommerce Plugin       | 🟡 Some technical setup | [WooCommerce Plugin](doc:woocommerce)                                 |
| Add checkout to a Magento store          | Magento Plugin           | 🟡 Some technical setup | [Magento Plugin](doc:magento)                                         |
| Add checkout to a custom-built website   | PayU Hosted Checkout     | 🟡 Some technical setup | [Hosted Checkout](doc:prebuilt-checkout-payu-hosted)                  |
| Build a fully custom payment page        | Merchant Hosted Checkout | 🔴 Developer required   | [Merchant Hosted](doc:custom-checkout-merchant-hosted)                |
| Set up subscription or recurring billing | Recurring Payments       | 🔴 Developer required   | [Recurring Payments](doc:introduction-recurring-payments-integration) |
| Split payments across multiple sellers   | Split Settlement         | 🔴 Developer required   | [Split Settlement](doc:split-settlments)                              |
| Accept payments on a mobile app          | Mobile SDKs              | 🔴 Developer required   | [Mobile SDKs](doc:mobile-sdks)                                        |

{/* NEW CONTENT — the "What you'll need before you begin" callout below
     is new. It surfaces the two universal prerequisites (account + credentials)
     that apply regardless of integration type, so users know what to do
     next after choosing a path. Needs SME review. */}

<Callout icon="📘" theme="info">
  ### **Before you start any integration**

  Every PayU integration requires two things:

  1. A registered and activated PayU merchant account
  2. Your Merchant Key and Salt for the environment you are integrating (Test or Production)

  If you don't have these yet, [Set Up Your Account →](doc:set-up-your-account)
</Callout>
