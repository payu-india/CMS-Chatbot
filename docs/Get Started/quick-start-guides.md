---
title: Quickstart Guides
excerpt: >-
  List of quick start guides of all PayU products to get your first PayU payment
  working in minutes.
deprecated: false
hidden: true
metadata:
  title: PayU Integration Quickstarts
  description: >-
    Step-by-step quickstart guides for every PayU integration path — from
    no-code payment links to fully custom checkout. Each guide gets you to a
    working test payment in under 10 minutes.
  robots: index
---
{/*
=============================================================================
CONTENT PROVENANCE — for SME / editorial review
=============================================================================
NEW CONTENT — this page is new. It is a placeholder index for per-product
              quickstart tutorials that do not yet exist.
              Keep hidden=true until the linked tutorials are published.
              Do not add doc: hyperlinks until each target page is live.
=============================================================================
*/}

{/* NEW CONTENT — page intro. Needs SME review for brand tone. */}

Each quickstart guide below walks you through a single integration path end to end — from your first API call to a completed test payment. Pick the path that matches your use case.

If you haven't chosen an integration yet, go to [Start Here](doc:start-here) and use the wizard to find the right fit.

***

## One-time payments

| Quickstart                                     | What you'll build                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Accept a payment with PayU Hosted Checkout     | Redirect customers to a PayU-hosted payment page and handle the callback. No custom UI required. |
| Accept a payment with Merchant Hosted Checkout | Build your own branded payment page that submits directly to PayU's payment API.                 |
| Accept a payment with Server-to-Server (S2S)   | Collect card details on your server and submit them directly to PayU without a redirect.         |
| Send a Payment Link                            | Create and share a payment link from the Dashboard or via API — no website needed.               |
| Generate a UPI QR code                         | Create a UPI QR code for in-person or digital payments and verify the result via webhook.        |

***

## Plugins and platforms

| Quickstart                  | What you'll build                                                    |
| --------------------------- | -------------------------------------------------------------------- |
| Install PayU on WooCommerce | Add PayU checkout to a WooCommerce store and run a test transaction. |
| Install PayU on Shopify     | Add PayU checkout to a Shopify store and run a test transaction.     |
| Install PayU on Magento     | Add PayU checkout to a Magento store and run a test transaction.     |

***

## Mobile

| Quickstart                                    | What you'll build                                                   |
| --------------------------------------------- | ------------------------------------------------------------------- |
| Accept a payment on Android (CheckoutPro SDK) | Embed the PayU Android SDK into an app and complete a test payment. |
| Accept a payment on iOS                       | Embed the PayU iOS SDK into an app and complete a test payment.     |
| Accept a payment with React Native            | Integrate PayU into a React Native app and complete a test payment. |
| Accept a payment with Flutter                 | Integrate PayU into a Flutter app and complete a test payment.      |

***

## Recurring and advanced

| Quickstart                                    | What you'll build                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------ |
| Create a subscription with Recurring Payments | Set up a recurring mandate and process the first charge.                 |
| Split a payment across sellers                | Route a payment to multiple merchants using Split Settlement.            |
| Issue a refund via API                        | Trigger a full or partial refund programmatically and verify the result. |

***

## Webhooks and developer tools

| Quickstart                   | What you'll build                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------ |
| Receive and verify a webhook | Set up a webhook endpoint, handle the reverse-hash verification, and acknowledge delivery. |
| Test webhooks locally        | Use a tunnelling tool to forward PayU webhook events to your local development server.     |
