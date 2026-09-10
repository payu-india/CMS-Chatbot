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

## Dashboard & No-Code Tools \[No coding required]

Start accepting payments directly from the PayU Dashboard — no developer or website needed.

| Quickstart               | What you'll build                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Send a Payment Link      | Create and share a payment link over WhatsApp, email, or SMS. Customers pay without visiting your website. |
| Create a Payment Invoice | Generate and send a branded invoice with a built-in payment link for your customer.                        |
| Add a Payment Button     | Embed a PayU payment button on any existing webpage with a single line of code.                            |
| Generate a UPI QR code   | Create a UPI QR code for in-person or digital in-store payments and verify the result in real time.        |

***

## Plugins and Platforms \[Some technical setup]

Requires plugin installation or basic configuration. Minimal or no custom code.

### eCommerce plugins

| Quickstart                  | What you'll build                                                     |
| --------------------------- | --------------------------------------------------------------------- |
| Install PayU on Shopify     | Add PayU checkout to a Shopify store and run a test transaction.      |
| Install PayU on WooCommerce | Add PayU checkout to a WooCommerce store and run a test transaction.  |
| Install PayU on Magento     | Add PayU checkout to a Magento store and run a test transaction.      |
| Install PayU on OpenCart    | Add PayU checkout to an OpenCart store and run a test transaction.    |
| Install PayU on PrestaShop  | Add PayU checkout to a PrestaShop store and run a test transaction.   |
| Install PayU on BigCommerce | Add PayU checkout to a BigCommerce store and run a test transaction.  |
| Install PayU on Wix         | Add PayU checkout to a Wix site and run a test transaction.           |
| Install PayU on Bagisto     | Add PayU checkout to a Bagisto store and run a test transaction.      |
| Install PayU on Odoo        | Add PayU checkout to an Odoo store and run a test transaction.        |
| Install PayU on Shopmatic   | Add PayU checkout to a Shopmatic store and run a test transaction.    |
| Install PayU on Fynd Store  | Add PayU checkout to a Fynd Store and run a test transaction.         |
| Install PayU on Zoho        | Add PayU as a payment method across Zoho One, Billing, and Inventory. |

### Website checkout

| Quickstart                                 | What you'll build                                                                                |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Accept a payment with PayU Hosted Checkout | Redirect customers to a PayU-hosted payment page and handle the callback. No custom UI required. |
| Accept a payment with Checkout Plus        | Embed a PayU checkout widget directly into your webpage without a full redirect.                 |

***

## Custom Integrations \[Developer required]

Requires coding, API integration, or SDK implementation.

### Web integrations

| Quickstart                                     | What you'll build                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Accept a payment with Merchant Hosted Checkout | Build your own branded payment page that submits directly to PayU's payment API.            |
| Accept a payment with CommercePro Checkout     | Integrate PayU's enhanced checkout with advanced UX controls and callback handling.         |
| Accept a payment with Server-to-Server (S2S)   | Collect payment details on your server and submit them directly to PayU without a redirect. |
| Pre-authorise and capture a card payment       | Place an authorisation hold on a card and capture the amount after fulfilment.              |

### Server-side SDKs

| Quickstart                  | What you'll build                                                                |
| --------------------------- | -------------------------------------------------------------------------------- |
| Integrate PayU with PHP     | Use the PayU PHP SDK to initiate and verify payments from a PHP backend.         |
| Integrate PayU with Node.js | Use the PayU Node.js SDK to initiate and verify payments from a Node.js backend. |
| Integrate PayU with Python  | Use the PayU Python SDK to initiate and verify payments from a Python backend.   |
| Integrate PayU with Java    | Use the PayU Java SDK to initiate and verify payments from a Java backend.       |
| Integrate PayU with Go      | Use the PayU Go SDK to initiate and verify payments from a Go backend.           |

### Android SDKs

| Quickstart                                    | What you'll build                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------- |
| Accept a payment with Android CheckoutPro SDK | Embed the full-featured PayU checkout UI in an Android app and complete a test payment. |
| Accept a payment with Android Core SDK        | Integrate PayU at a lower level in an Android app for maximum UI control.               |
| Accept a UPI payment with Android UPI SDK     | Add a dedicated UPI payment flow to an Android app.                                     |
| Accept a payment with Android UPI Bolt SDK    | Embed the PayU UPI Bolt UI in an Android app for a streamlined UPI experience.          |
| Accept a payment with Android Google Pay SDK  | Integrate Google Pay as a payment method in an Android app via PayU.                    |
| Accept a payment with Android PhonePe SDK     | Integrate PhonePe as a payment method in an Android app via PayU.                       |

### iOS SDKs

| Quickstart                                | What you'll build                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| Accept a payment with iOS CheckoutPro SDK | Embed the full-featured PayU checkout UI in an iOS app and complete a test payment. |
| Accept a payment with iOS Core SDK        | Integrate PayU at a lower level in an iOS app for maximum UI control.               |
| Accept a UPI payment with iOS UPI SDK     | Add a dedicated UPI payment flow to an iOS app.                                     |
| Accept a payment with iOS UPI Bolt SDK    | Embed the PayU UPI Bolt UI in an iOS app for a streamlined UPI experience.          |

### Cross-platform SDKs

| Quickstart                                         | What you'll build                                                              |
| -------------------------------------------------- | ------------------------------------------------------------------------------ |
| Accept a payment with React Native CheckoutPro SDK | Integrate the PayU checkout UI in a React Native app for both Android and iOS. |
| Accept a payment with React Native Core SDK        | Integrate PayU at a lower level in a React Native app.                         |
| Accept a payment with Flutter CheckoutPro SDK      | Integrate the PayU checkout UI in a Flutter app for both Android and iOS.      |
| Accept a payment with Flutter UPI Bolt SDK         | Embed the PayU UPI Bolt UI in a Flutter app.                                   |
| Accept a payment with Cordova CheckoutPro SDK      | Integrate PayU checkout in a Cordova or Ionic hybrid app.                      |
| Accept a payment with Capacitor UPI Bolt SDK       | Embed the PayU UPI Bolt UI in a Capacitor or Ionic Angular app.                |

### Recurring & advanced

| Quickstart                                    | What you'll build                                                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------------- |
| Create a subscription with Recurring Payments | Set up a recurring mandate and process the first charge automatically.             |
| Automate subscriptions with Zion Platform     | Use the Zion subscription automation platform to manage complex billing schedules. |
| Split a payment across sellers                | Route a payment to multiple merchants using Split Settlement.                      |
| Issue a refund via API                        | Trigger a full or partial refund programmatically and verify the result.           |
| Set up UPI Autopay (cross-border)             | Configure UPI Autopay for import/cross-border recurring payments.                  |

### Channels & commerce

| Quickstart                        | What you'll build                                                               |
| --------------------------------- | ------------------------------------------------------------------------------- |
| Send payment links on WhatsApp    | Deliver PayU payment links directly to customers over WhatsApp.                 |
| Accept WhatsApp Native Payments   | Enable in-chat UPI payments via WhatsApp Business API.                          |
| Accept payments at a POS terminal | Integrate PayU with a physical POS terminal via the POS API or Android POS SDK. |
| Accept payments via BBPS (Agent)  | Integrate the BBPS Connect Agent API for bill collection.                       |
| Accept recharge payments via BBPS | Integrate the BBPS Recharge API for prepaid recharge collection.                |

***

## Developer Tools

| Quickstart                   | What you'll build                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Receive and verify a webhook | Set up a webhook endpoint, handle reverse-hash verification, and acknowledge delivery correctly. |
| Test webhooks locally        | Use a tunnelling tool to forward PayU webhook events to your local development server.           |
