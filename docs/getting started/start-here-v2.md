---
title: Start Here V2
deprecated: false
hidden: true
metadata:
  robots: index
---
You've set up your PayU account. This page gets you from zero to your first payment. Find the right integration, get your credentials, and start building.

***

<Callout icon="📘" theme="info">
  ### **Before You Start Integrating**

  Every PayU integration requires two things:

  1. A registered and activated PayU merchant account
  2. Your Merchant Key and Salt for the environment you are integrating (Test or Production)

  **Do not have an account yet?** [Set Up Your Account →](https://docs.payu.in/docs/set-up-your-account)

  **Already have an account?** Your credentials are in the PayU Dashboard under **Developer → API Details**.
</Callout>

***

## Find Your Integration Path

Not sure where to start? Answer a few questions and we'll recommend the right PayU product for you. Already know what you need? Browse the table or compare options in detail below.

<Callout icon="far fa-lightbulb-on" theme="default">
  ### **No Technical Setup? No Problem!**

  If you just want to start accepting payments today without any coding, [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) and [Payment Buttons](https://docs.payu.in/docs/payment-buttons) work straight from the PayU Dashboard — no developer needed.
</Callout>

<br />

<PayUQuickStartWizard />

***

### Common Integration Paths

If you already know what you need, go directly to the right guide.

| What you want to do                      | PayU solution                                                                               | Effort                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------- |
| Share a payment link — no website needed | [Payment Links](https://docs.payu.in/docs/payment-links-dashboard)                          | 🟢 No coding required   |
| Embed a buy button on any webpage        | [Payment Buttons](https://docs.payu.in/docs/payment-buttons)                                | 🟢 No coding required   |
| Add checkout to a Shopify store          | [Shopify Plugin](https://docs.payu.in/docs/shopify)                                         | 🟡 Some technical setup |
| Add checkout to a WooCommerce store      | [WooCommerce Plugin](https://docs.payu.in/docs/woocommerce)                                 | 🟡 Some technical setup |
| Add checkout to a Magento store          | [Magento Plugin](https://docs.payu.in/docs/magento)                                         | 🟡 Some technical setup |
| Add checkout to a custom-built website   | [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted)             | 🟡 Some technical setup |
| Build a fully custom payment page        | [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted)       | 🔵 Developer required   |
| Set up subscription or recurring billing | [Recurring Payments](https://docs.payu.in/docs/introduction-recurring-payments-integration) | 🔵 Developer required   |
| Split payments across multiple sellers   | [Split Settlement](https://docs.payu.in/docs/split-settlments)                              | 🔵 Developer required   |
| Accept payments on a mobile app          | [Mobile SDKs](https://docs.payu.in/docs/mobile-sdks)                                        | 🔵 Developer required   |

***

### Compare All Options in Detail

| Integration Type                                 | Dev Effort    | PCI Compliance Needed                | Customization                           | Best For                                  |
| :----------------------------------------------- | :------------ | :----------------------------------- | :-------------------------------------- | :---------------------------------------- |
| **No Code / Low Code** (Payment Links & Buttons) | Very Low      | No                                   | Minimal (branding, logo, colors)        | Small merchants, instant setup            |
| **eCommerce Plugins**                            | Very Low      | No                                   | Minimal                                 | Shopify, WooCommerce, Magento merchants   |
| **PayU Hosted Checkout**                         | Low           | No                                   | Minimal (branding, logo, colors)        | SMBs, merchants looking for quick go-live |
| **Merchant Hosted Checkout**                     | Medium        | Yes (cards handled on merchant site) | High (full UI control)                  | Businesses with PCI DSS compliance        |
| **Server-to-Server**                             | High          | Yes                                  | Very High (own checkout flow + backend) | Large merchants, marketplaces             |
| **CommercePro / Checkout Plus**                  | Medium        | No (PayU handles sensitive data)     | Medium (optimised UI)                   | Businesses optimising for conversion      |
| **Mobile SDKs**                                  | Low to Medium | Dependent on checkout type           | Medium (native customisation)           | Native Android, iOS, and hybrid apps      |

***

## What You Can Do With PayU

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

## All Integration Options

### Website Integrations

* [No Code Solutions](https://docs.payu.in/docs/introduction-no-code-payments-integration)
* [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted)
* [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted)
* [Server-to-Server](https://docs.payu.in/docs/server-to-server-integration)
* [CommercePro Checkout](https://docs.payu.in/docs/checkout-express)
* [Checkout Plus](https://docs.payu.in/docs/checkout-plus-integration)

### Mobile SDKs

* [Android](https://docs.payu.in/docs/explore-android-sdks)
* [iOS](https://docs.payu.in/docs/explore-ios-sdks)
* [React Native](https://docs.payu.in/docs/explore-reactnative-sdks)
* [Flutter](https://docs.payu.in/docs/flutter-sdk-introduction)
* [Cordova](https://docs.payu.in/docs/cordova-sdk-introduction)

### eCommerce Plugins

* [Shopify](https://docs.payu.in/docs/shopify)
* [WooCommerce](https://docs.payu.in/docs/woocommerce)
* [Magento](https://docs.payu.in/docs/magento)
* [All Plugins →](https://docs.payu.in/docs/ecommerce-platform-plugins/)

***

## Developer Resources

* **Merchant Key & Salt** → [Access Merchant Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-copy)
* **Test Credentials** (Card, UPI, Wallet, BNPL) → [Test Cards, UPI IDs and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)
* **Postman Collection** → [PayU Integration Workspace](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/overview)

***

## Offerings & Advanced Features

Once your core integration is live, explore these to enhance your checkout and customer experience.

* [**Affordability & Loyalty**](https://docs.payu.in/docs/introduction-to-affordability) — EMI, offers, BNPL, loyalty rewards, affordability widget
* [**Subscriptions / Recurring Payments**](https://docs.payu.in/docs/introduction-recurring-payments-integration)
* [**International Payments**](https://docs.payu.in/docs/introduction-dynamic-currency-conversion)
* [**Pre-Authorize Payments**](https://docs.payu.in/docs/auth-and-capture-pre-authorize-card-payments)
* [**Cross-Border Payments**](https://docs.payu.in/docs/introduction-cross-border-payments-import)
* [**Split Settlements**](https://docs.payu.in/docs/split-settlments)
* [**Tokenization / Save Cards**](https://docs.payu.in/docs/introduction-save-cards)
* [**Third-Party Verification (TPV)**](https://docs.payu.in/docs/introduction-to-payu-tpv)
* [**Recommendation Engine**](https://docs.payu.in/docs/recommendation-engine)
* [**Refunds**](https://docs.payu.in/docs/introduction-refunds)

***

## Other Products

* **MCP (Model Context Protocol)** → [PayU Remote MCP Server](https://docs.payu.in/docs/payu-remote-mcp-server-integration)
* **Partner Integration** → [Partner Program Overview](https://docs.payu.in/docs/payu-partner-program-overview#/)
* **Payouts** → [Introduction to Payouts](https://docs.payu.in/docs/introduction-to-payouts/)
* **Bill Payments (BBPS)** → [Connect Agent API](https://docs.payu.in/docs/connect-agent-api-integration) · [Recharge API](https://docs.payu.in/docs/recharge-api-integration)

***

## Contact PayU

If you are facing issues during integration or want to enable a PayU offering, contact [PayU Support](mailto:integration@payu.in). Include logs, error messages, and steps to reproduce the issue.