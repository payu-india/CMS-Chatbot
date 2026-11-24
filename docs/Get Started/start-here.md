---
title: Start Here
excerpt: >-
  Find the right PayU integration for your business, from no-code payment links
  and Payment Buttons to hosted checkout, mobile SDKs, and recurring payments.
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
next:
  description: Explore related topics and resources.
---
Whether you are a business owner who wants to start accepting payments today with no coding, or a developer building a fully custom checkout, this is where you start. PayU supports UPI, cards, net banking, wallets, EMI, and more across India. The sections below will help you find the right product and get to your first payment as quickly as possible.

***

## Find the Right Product for You

{/* NEW CONTENT — wizard heading and description are new. No equivalent label exists
     on the wizard component or the Quick Start page it is sourced from.
     Needs SME review for tone. */}

<Callout icon="far fa-lightbulb-on" theme="default">
  ### **No Technical Setup? No problem!**

  If you just want to start accepting payments today without any coding, <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links-dashboard">Payment Links</Anchor> and <Anchor target="_blank" href="https://docs.payu.in/docs/payment-buttons-dashboard">Payment Buttons</Anchor> work straight from the PayU Dashboard without the need of a developer.
</Callout>

If you want to find the right fit, tell us about your business and technical capability for this wizard to recommend you the PayU product that fits. Not sure where to start? Answer a few questions and we will point you to the right path. It takes about a minute.

<PayUQuickStartWizard />

***

{/* NEW CONTENT — the static fallback table below does not exist in this
     form in the repo. The product names, effort labels, and doc URLs are
     sourced from the wizard's product catalog (PayUQuickStartWizard component
     data). The table structure and "prefer to browse" framing are new.
     Needs SME review to confirm doc URLs and effort labels are current. */}

## Prefer to Browse? All Integration Paths at a Glance

If you already know what you need, go directly to the right guide.

| What you want to do                                | PayU solution            | Effort                  |
| -------------------------------------------------- | ------------------------ | ----------------------- |
| Share a payment link without the need of a website | Payment Links            | 🟢 No coding required   |
| Add checkout to a Shopify store                    | Shopify Plugin           | 🟡 Some technical setup |
| Add checkout to a WooCommerce store                | WooCommerce Plugin       | 🟡 Some technical setup |
| Add checkout to a Magento store                    | Magento Plugin           | 🟡 Some technical setup |
| Add checkout to a custom-built website             | PayU Hosted Checkout     | 🟡 Some technical setup |
| Build a fully custom payment page                  | Merchant Hosted Checkout | 🔴 Developer required   |
| Set up subscription or recurring billing           | Recurring Payments       | 🔴 Developer required   |
| Split payments across multiple sellers             | Split Settlement         | 🔴 Developer required   |
| Accept payments on a mobile app                    | Mobile SDKs              | 🔴 Developer required   |

{/* NEW CONTENT — the "What you'll need before you begin" callout below
     is new. It surfaces the two universal prerequisites (account + credentials)
     that apply regardless of integration type, so users know what to do
     next after choosing a path. Needs SME review. */}

{/* NEW CONTENT — cards block showing what you can do with PayU.
     Use case labels and capabilities are drawn from product docs across the repo.
     Card descriptions are new editorial copy. Needs SME review for accuracy and completeness. */}

***

## What You Can Do With PayU?

<Cards>
  <Card title="Collect one-time payments" icon="far fa-credit-card">
    Accept UPI, cards, net banking, wallets, and EMI on your website or app — via a PayU-hosted page or your own custom checkout.
  </Card>

  <Card title="Share a payment link" icon="far fa-link">
    Send a payment link over WhatsApp, email, or SMS. No website or technical setup required.
  </Card>

  <Card title="Set up recurring billing" icon="far fa-repeat">
    Charge customers on a schedule — subscriptions, mandates, and EMI plans with automated retry handling.
  </Card>

  <Card title="Accept in-person payments" icon="far fa-barcode-scan">
    Generate a UPI QR code for face-to-face or digital in-store payments.
  </Card>

  <Card title="Add checkout to your store" icon="far fa-cart-shopping">
    Ready-made plugins for Shopify, WooCommerce, and Magento — no custom code needed.
  </Card>

  <Card title="Build for mobile" icon="far fa-mobile-vibrate">
    Native SDKs for Android and iOS, plus React Native, Flutter, and Cordova wrappers.
  </Card>
</Cards>

***

<Callout icon="📘" theme="info">
  ### **Before You Start Integrating**

  Every PayU integration requires two things:<br />

  1. A registered and activated PayU merchant account
  2. Your Merchant Key and Salt for the environment you are integrating (Test or Production)

  **Do not have an account yet?** <Anchor target="_blank" href="https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard">Set Up Your Account →</Anchor>

  <br />

  **Already have an account?** Your credentials are in the PayU Dashboard under **Developer → API Details**.
</Callout>