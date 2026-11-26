---
title: Start Here V2
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU helps Indian businesses accept payments online and in-person — UPI, cards, net banking, wallets, EMI, and more. Use this page to find the right integration for your business and get to your first payment.

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

## Prefer to Browse? Common Integration Paths

This is a quick gist of the most common paths, not an exhaustive list. If you already know what you need, go directly to the right guide.

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
| Accept in-person payments via QR code    | [UPI QR Code](https://docs.payu.in/docs/integrate-upi-qr)                                   | 🔵 Developer required   |
| Accept card payments at a physical store | [Android POS SDK](https://docs.payu.in/docs/android-pos-sdk)                                | 🔵 Developer required   |

<Accordion title="Compare all integration options in detail">
  | Integration Type                                 | Dev Effort    | PCI Compliance Needed                | Customization                           | Best For                                  |
  | :----------------------------------------------- | :------------ | :----------------------------------- | :-------------------------------------- | :---------------------------------------- |
  | **No Code / Low Code** (Payment Links & Buttons) | Very Low      | No                                   | Minimal (branding, logo, colors)        | Small merchants, instant setup            |
  | **eCommerce Plugins**                            | Very Low      | No                                   | Minimal                                 | Shopify, WooCommerce, Magento merchants   |
  | **PayU Hosted Checkout**                         | Low           | No                                   | Minimal (branding, logo, colors)        | SMBs, merchants looking for quick go-live |
  | **Merchant Hosted Checkout**                     | Medium        | Yes (cards handled on merchant site) | High (full UI control)                  | Businesses with PCI DSS compliance        |
  | **Server-to-Server**                             | High          | Yes                                  | Very High (own checkout flow + backend) | Large merchants, marketplaces             |
  | **CommercePro / Checkout Plus**                  | Medium        | No (PayU handles sensitive data)     | Medium (optimised UI)                   | Businesses optimising for conversion      |
  | **Mobile SDKs**                                  | Low to Medium | Dependent on checkout type           | Medium (native customisation)           | Native Android, iOS, and hybrid apps      |
</Accordion>

***

## Getting Started

Once you have chosen your integration, here is what you need to begin building.

1. **Get your credentials**: <Anchor target="_blank" href="https://docs.payu.in/docs/generate-merchant-key-and-salt-copy">Retrieve your Merchant Key and Salt</Anchor> from the PayU Dashboard
2. **Build on the test environment**: All integrations support a test mode. Always build and validate there first
3. **Simulate transactions**: Use <Anchor target="_blank" href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets">test cards, UPI IDs, and wallets</Anchor> to cover different payment scenarios
4. **Review the production checklist**: Make sure your integration handles all edge cases before going live
5. **Go live**: Switch to your production credentials and you're done

**Don't have an account yet?** [Set Up Your Account →](https://docs.payu.in/docs/set-up-your-account)

<Callout icon="🛠️" theme="default">
  ### **Developer Resources**

  * [Explore PayU APIs](https://docs.payu.in/reference/introduction-api-reference)
  * [Callbacks & Webhook](https://docs.payu.in/docs/callbacks-webhook-reference)
</Callout>

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="What payment modes does PayU support?">
    PayU supports 100+ payment modes including UPI, credit and debit cards (Visa, Mastercard, RuPay, Amex), net banking (50+ banks), wallets (Paytm, PhonePe, Amazon Pay, and others), EMI (bank EMI, no-cost EMI, cardless EMI), BNPL (Buy Now Pay Later), and international cards. The available modes depend on your merchant account configuration.
  </Accordion>

  <Accordion title="Do I need PCI compliance to integrate PayU?">
    It depends on your integration type. If you use **PayU Hosted Checkout**, **Payment Links**, or **Payment Buttons**, PayU handles all sensitive card data and you do not need PCI compliance. If you use **Merchant Hosted Checkout** or **Server-to-Server**, card data may pass through your servers and PCI DSS compliance is required. When in doubt, choose Hosted Checkout — it is the fastest and safest path.
  </Accordion>

  <Accordion title="What is the difference between PayU Hosted and Merchant Hosted Checkout?">
    With **PayU Hosted Checkout**, customers are redirected to PayU's payment page — you do not handle any card data, and there is no PCI compliance burden on your side. With **Merchant Hosted Checkout**, the payment UI stays on your website (you control the design and experience), but PayU processes the transaction on the backend. Merchant Hosted gives you more control but requires you to handle PCI compliance.
  </Accordion>

  <Accordion title="How do I test my integration before going live?">
    PayU provides a full test environment. Use the test Merchant Key and Salt (available in your PayU Dashboard under test mode), and use the [test cards, UPI IDs, and wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets) to simulate different payment scenarios including success, failure, and pending states. Never test with real payment details.
  </Accordion>

  <Accordion title="How long does it take to integrate PayU?">
    It depends on the integration type. **Payment Links and Buttons** take minutes — no coding at all. **PayU Hosted Checkout** can typically be live within a few hours. **Merchant Hosted Checkout** or **Server-to-Server** integrations typically take a few days to a few weeks, depending on your team's capacity and the complexity of your checkout flow.
  </Accordion>

  <Accordion title="What do I need before I can start?">
    You need three things: a **registered and activated PayU merchant account**, your **Merchant Key and Salt** (from the PayU Dashboard under Developer → API Details), and a **server to receive payment callbacks** (required for most integrations except Payment Links and Buttons). If you don't have an account yet, [set one up here](https://docs.payu.in/docs/set-up-your-account).
  </Accordion>
</AccordionGroup>

***

### Explore by Platform

<Tabs>
  <Tab title="Website">
    * [No Code Solutions](https://docs.payu.in/docs/introduction-no-code-payments-integration)
    * [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted)
    * [Merchant Hosted Checkout](https://docs.payu.in/docs/custom-checkout-merchant-hosted)
    * [Server-to-Server](https://docs.payu.in/docs/server-to-server-integration)
    * [CommercePro Checkout](https://docs.payu.in/docs/checkout-express)
    * [Checkout Plus](https://docs.payu.in/docs/checkout-plus-integration)
  </Tab>

  <Tab title="Mobile SDKs">
    * [Android](https://docs.payu.in/docs/explore-android-sdks)
    * [iOS](https://docs.payu.in/docs/explore-ios-sdks)
    * [React Native](https://docs.payu.in/docs/explore-reactnative-sdks)
    * [Flutter](https://docs.payu.in/docs/flutter-sdk-introduction)
    * [Cordova](https://docs.payu.in/docs/cordova-sdk-introduction)
  </Tab>

  <Tab title="eCommerce Plugins">
    * [Shopify](https://docs.payu.in/docs/shopify)
    * [WooCommerce](https://docs.payu.in/docs/woocommerce)
    * [Magento](https://docs.payu.in/docs/magento)
    * [All Plugins →](https://docs.payu.in/docs/ecommerce-platform-plugins/)
  </Tab>
</Tabs>

***

## Offerings For Your Products

Once your core integration is live, explore these to enhance your checkout, expand your reach, and streamline operations.

**Enhance Checkout**

* [Affordability & Loyalty:](https://docs.payu.in/docs/introduction-to-affordability) EMI, offers, BNPL, loyalty rewards, affordability widget
* [Tokenization / Save Cards:](https://docs.payu.in/docs/introduction-save-cards) Faster repeat purchases with saved card tokens
* [Recommendation Engine:](https://docs.payu.in/docs/recommendation-engine) Smart payment mode suggestions to improve conversion

**Expand Reach**

* [International Payments:](https://docs.payu.in/docs/introduction-dynamic-currency-conversion) Accept payments in multiple currencies
* [Cross-Border Payments:](https://docs.payu.in/docs/introduction-cross-border-payments-import) Collect import payments from overseas
* [Pre-Authorize Payments:](https://docs.payu.in/docs/auth-and-capture-pre-authorize-card-payments) Authorize now, capture later

**Manage and Operate**

* [Split Settlements:](https://docs.payu.in/docs/split-settlments) Automatically split payments across multiple sellers or accounts
* [Third-Party Verification (TPV):](https://docs.payu.in/docs/introduction-to-payu-tpv) Verify that payments originate from a registered bank account
* [Refunds:](https://docs.payu.in/docs/introduction-refunds) Full and partial refund APIs with status tracking

**Other Products**

* [Partner Integration:](https://docs.payu.in/docs/payu-partner-program-overview#/) Onboard and manage sub-merchants under your platform
* [Payouts:](https://docs.payu.in/docs/introduction-to-payouts/) Disburse payments to customers, vendors, or employees
* [Bill Payments (BBPS):](https://docs.payu.in/docs/connect-agent-api-integration) Collect utility and recharge bill payments

***

## MCP (Model Context Protocol)

Use <Anchor target="_blank" href="https://docs.payu.in/docs/payu-remote-mcp-server-integration">PayU's MCP</Anchor> to communicate with PayU APIs using.

***

<Callout icon="📞" theme="default">
  ### **Contact PayU**

  Facing issues during integration or want to enable a PayU offering? Reach out to [PayU Support](mailto:integration@payu.in). Include your logs, error messages, and steps to reproduce — it speeds up the resolution.
</Callout>