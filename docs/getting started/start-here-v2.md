---
title: Start Here V2
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU helps Indian businesses accept payments online and in-person using UPI, cards, net banking, wallets, EMI, and more. Whether you are a business owner looking to get started today or a developer building a custom checkout, this page gets you to your first payment.

***

<Callout icon="📘" theme="info">
  ### **Get Your Credentials First**

  Every PayU integration needs two things: your **Merchant Key** and **Salt**. You will not be able to test or go live without them.

  **Don't have an account yet?** [Set Up Your Account →](https://docs.payu.in/docs/set-up-your-account)

  **Already have an account?** Find your credentials in the PayU Dashboard under **Developer → API Details**.
</Callout>

***

## What Would You Like To Do?

<Cards>
  <Card title="Accept payments on my website" href="https://docs.payu.in/docs/introduction-web" icon="far fa-globe">
    Integrate PayU into your website — hosted checkout, custom checkout, or direct API. Choose based on how much control you need.
  </Card>

  <Card title="Share a payment link or button" href="https://docs.payu.in/docs/introduction-no-code-payments-integration" icon="far fa-link">
    No website or coding needed. Send a payment link via WhatsApp, SMS, or email — or embed a button on any page.
  </Card>

  <Card title="Build for a mobile app" href="https://docs.payu.in/docs/mobile-sdks" icon="far fa-mobile-vibrate">
    Native SDKs for Android and iOS, plus React Native, Flutter, and Cordova wrappers.
  </Card>

  <Card title="Add to my Shopify or WooCommerce store" href="https://docs.payu.in/docs/ecommerce-platform-plugins/" icon="far fa-cart-shopping">
    Ready-made plugins for Shopify, WooCommerce, Magento, and more — no custom code required.
  </Card>

  <Card title="Set up recurring or subscription billing" href="https://docs.payu.in/docs/introduction-recurring-payments-integration" icon="far fa-repeat">
    Charge customers on a schedule — weekly, monthly, or custom — with automated retry handling.
  </Card>

  <Card title="Send money to customers or vendors" href="https://docs.payu.in/docs/introduction-to-payouts/" icon="far fa-paper-plane">
    Disburse bulk payments via UPI, IMPS, NEFT, or RTGS directly from PayU.
  </Card>
</Cards>

***

## Not Sure Where to Start?

Tell us a bit about your business and we'll point you to the right integration. It takes about a minute.

<Callout icon="far fa-lightbulb-on" theme="default">
  ### **No technical setup needed?**

  [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) and [Payment Buttons](https://docs.payu.in/docs/payment-buttons) work straight from your PayU Dashboard — no developer or website required.
</Callout>

<br />

<PayUQuickStartWizard />

***

## Collect Payments

Explore PayU's payment collection options by channel.

<Tabs>
  <Tab title="Online">
    <Cards>
      <Card title="Payment Links" href="https://docs.payu.in/docs/payment-links-dashboard" icon="far fa-link">
        Generate and share a unique payment link via WhatsApp, SMS, or email — no website or coding required.
      </Card>

      <Card title="Payment Buttons" href="https://docs.payu.in/docs/payment-buttons" icon="far fa-hand-pointer">
        Embed a pay button on any webpage with a simple copy-paste. PayU handles the rest.
      </Card>

      <Card title="PayU Hosted Checkout" href="https://docs.payu.in/docs/prebuilt-checkout-payu-hosted" icon="far fa-window-maximize">
        PayU serves the payment page — you send customers there and handle the callback. Fast to go live, zero PCI burden.
      </Card>

      <Card title="Merchant Hosted Checkout" href="https://docs.payu.in/docs/custom-checkout-merchant-hosted" icon="far fa-paintbrush">
        Your design, your flow. Full UI control with PayU's payment engine powering the backend.
      </Card>

      <Card title="Server-to-Server (S2S)" href="https://docs.payu.in/docs/server-to-server-integration" icon="far fa-server">
        Direct API integration for maximum flexibility. Build your own checkout flow end to end.
      </Card>

      <Card title="CommercePro / Checkout Plus" href="https://docs.payu.in/docs/checkout-express" icon="far fa-bolt">
        High-conversion checkout with optimised UX, smart payment mode selection, and minimal integration effort.
      </Card>
    </Cards>
  </Tab>

  <Tab title="In-Person">
    <Cards>
      <Card title="UPI QR Code" href="https://docs.payu.in/docs/integrate-upi-qr" icon="far fa-qrcode">
        Generate a UPI QR code for face-to-face or in-store payments — no hardware needed.
      </Card>

      <Card title="Android POS SDK" href="https://docs.payu.in/docs/android-pos-sdk" icon="far fa-tablet">
        Accept card and UPI payments on Android devices at physical locations.
      </Card>
    </Cards>
  </Tab>

  <Tab title="Recurring">
    <Cards>
      <Card title="Subscriptions & Recurring Payments" href="https://docs.payu.in/docs/introduction-recurring-payments-integration" icon="far fa-repeat">
        Charge customers on a schedule with automated retry, mandate management, and a subscription dashboard.
      </Card>
    </Cards>
  </Tab>
</Tabs>

***

## Integrate by Platform

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

<br />

<details>
<summary>**Compare all integration options in detail →**</summary>

| Integration Type                                 | Dev Effort    | PCI Compliance Needed                | Customization                           | Best For                                  |
| :----------------------------------------------- | :------------ | :----------------------------------- | :-------------------------------------- | :---------------------------------------- |
| **No Code / Low Code** (Payment Links & Buttons) | Very Low      | No                                   | Minimal (branding, logo, colors)        | Small merchants, instant setup            |
| **eCommerce Plugins**                            | Very Low      | No                                   | Minimal                                 | Shopify, WooCommerce, Magento merchants   |
| **PayU Hosted Checkout**                         | Low           | No                                   | Minimal (branding, logo, colors)        | SMBs, merchants looking for quick go-live |
| **Merchant Hosted Checkout**                     | Medium        | Yes (cards handled on merchant site) | High (full UI control)                  | Businesses with PCI DSS compliance        |
| **Server-to-Server**                             | High          | Yes                                  | Very High (own checkout flow + backend) | Large merchants, marketplaces             |
| **CommercePro / Checkout Plus**                  | Medium        | No (PayU handles sensitive data)     | Medium (optimised UI)                   | Businesses optimising for conversion      |
| **Mobile SDKs**                                  | Low to Medium | Dependent on checkout type           | Medium (native customisation)           | Native Android, iOS, and hybrid apps      |

</details>

***

## Developer Resources

<Callout icon="🛠️" theme="default">
  * **Merchant Key & Salt** → [Access Merchant Key and Salt](https://docs.payu.in/docs/generate-merchant-key-and-salt-copy)
  * **Test Credentials** (Card, UPI, Wallet, BNPL) → [Test Cards, UPI IDs and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)
  * **API Reference** → [Explore PayU APIs](https://docs.payu.in/reference/introduction-api-reference)
  * **Postman Collection** → [PayU Integration Workspace](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/overview)
</Callout>

***

## Enhance Your Integration

Once your core integration is live, explore these to improve checkout, expand reach, and streamline operations.

**Enhance Checkout**

* [Affordability & Loyalty](https://docs.payu.in/docs/introduction-to-affordability) — EMI, offers, BNPL, loyalty rewards, affordability widget
* [Tokenization / Save Cards](https://docs.payu.in/docs/introduction-save-cards) — Faster repeat purchases with saved card tokens
* [Recommendation Engine](https://docs.payu.in/docs/recommendation-engine) — Smart payment mode suggestions to improve conversion

**Expand Reach**

* [International Payments](https://docs.payu.in/docs/introduction-dynamic-currency-conversion) — Accept payments in multiple currencies
* [Cross-Border Payments](https://docs.payu.in/docs/introduction-cross-border-payments-import) — Collect import payments from overseas
* [Pre-Authorize Payments](https://docs.payu.in/docs/auth-and-capture-pre-authorize-card-payments) — Authorize now, capture later

**Manage & Operate**

* [Split Settlements](https://docs.payu.in/docs/split-settlments) — Automatically split payments across multiple sellers or accounts
* [Third-Party Verification (TPV)](https://docs.payu.in/docs/introduction-to-payu-tpv) — Verify that payments originate from a registered bank account
* [Refunds](https://docs.payu.in/docs/introduction-refunds) — Full and partial refund APIs with status tracking

***

## Other Products

* **MCP (Model Context Protocol)** → [PayU Remote MCP Server](https://docs.payu.in/docs/payu-remote-mcp-server-integration)
* **Partner Integration** → [Partner Program Overview](https://docs.payu.in/docs/payu-partner-program-overview#/)
* **Payouts** → [Introduction to Payouts](https://docs.payu.in/docs/introduction-to-payouts/)
* **Bill Payments (BBPS)** → [Connect Agent API](https://docs.payu.in/docs/connect-agent-api-integration) · [Recharge API](https://docs.payu.in/docs/recharge-api-integration)

<Callout icon="📞" theme="default">
  ### **Contact PayU**

  Facing issues during integration or want to enable a PayU offering? Reach out to [PayU Support](mailto:integration@payu.in). Include your logs, error messages, and steps to reproduce — it speeds up the resolution.
</Callout>
