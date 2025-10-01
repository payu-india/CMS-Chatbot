---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - checkout integration
    - ' API reference'
    - ' payment gateway API integration'
    - ' payment aggregator API integration'
    - ' payment gateway integration'
    - ' UPI payment integration'
    - ' card payment integration'
    - ' NetBanking integration'
  robots: index
next:
  description: ''
---
PayU offers multiple payment workflows suitable for your online payment collection and disbursement strategy with diverse requirements and operational realities. Your website’s payment workflow is an integral part of your customer’s shopping experience. After the customer adds the products to the shopping cart on your website and checkout, you need to offer various payment modes to make the shopping experience complete.

# What is a payment gateway?

A payment gateway is a technology used by merchants to accept debit or credit card, UPI, wallets, EMI, etc. For purchases made by customers.

# Benefits

* Safer, faster, smoother transactions that give customers peace of mind.
* Secure and protect customers from frauds.
* Improves user experience, saves time, and empowers your customers.
* Enables you to accept multiple payment types and cards securely
* Reduces declined payments with real time transactions.

> 📘 PayU recommends you to:
>
> * Understand the product integration steps on this **Integration Guide** and later refer to [API Reference](ref:introduction-api-reference).
>
> * The [API Reference](ref:introduction-api-reference) pages for various APIs allows you to make mock API calls with most of the PayU APIs (using a static test key).  Also, it provides support in 16 language bindings, so you can get the source code in apart from bash or cURL.
>
> * PayU recommends you to integrate with Test environment initially for all the integration before you go live to Production environment.
>
> * It is recommended to follow the **Integration Checklist** for checkout or SDK integrations to ensure that your integration is complete before making your integration live.

## Collect Payments

* <Anchor label="No Code Solutions" target="_blank" href="https://docs.payu.in/docs/introduction-no-code-payments-integration">No Code Solutions</Anchor>
* <Anchor label="PayU Hosted Checkout" target="_blank" href="doc:prebuilt-checkout-payu-hosted">PayU Hosted Checkout</Anchor>
* <Anchor label="Merchant Hosted Checkout" target="_blank" href="doc:custom-checkout-merchant-hosted">Merchant Hosted Checkout</Anchor>
* <Anchor label="Server-to-Server" target="_blank" href="doc:server-to-server-integration">Server-to-Server</Anchor>
* <Anchor label="CommercePro Checkout" target="_blank" href="doc:checkout-express">CommercePro Checkout</Anchor>
* [Checkout Plus](doc:checkout-plus-integration)
* **Mobile SDK**: For more information, refer to any of the following based on your integration:
  * <Anchor label="Explore Android SDKs" target="_blank" href="doc:explore-android-sdks">Explore Android SDKs</Anchor>
  * <Anchor label="Explore iOS SDKs" target="_blank" href="doc:explore-ios-sdks">Explore iOS SDKs</Anchor>
  * <Anchor label="Explore React Native SDKs" target="_blank" href="doc:explore-reactnative-sdks">Explore React Native SDKs</Anchor>
  * <Anchor label="Explore Flutter SDKs" target="_blank" href="doc:flutter-sdk-introduction">Explore Flutter SDKs</Anchor>
  * <Anchor label="Explore Cordova CheckoutPro SDK" target="_blank" href="doc:cordova-sdk-introduction">Explore Cordova CheckoutPro SDK</Anchor>
* **eCommerce Plugins**: For more information, refer to  <Anchor label="Plugins - Introduction" target="_blank" href="https://docs.payu.in/docs/ecommerce-platform-plugins/">Plugins - Introduction</Anchor>

# Offerings

* [Affordability & Loyalty](https://docs.payu.in/docs/introduction-to-affordability)
  * [EMI](https://docs.payu.in/docs/emi-api-integration)
  * [Offers Dashboard](https://docs.payu.in/docs/offers-dashboard)
  * [Offers Integration APIs](https://docs.payu.in/docs/offers-integration)
  * [BNPL Integration](https://docs.payu.in/docs/payu-bnpl-integration-introduction)
  * [Loyalty Edge](https://docs.payu.in/docs/loyalty-edge-introduction)
  * [Affordability Widget](https://docs.payu.in/docs/affordability-suite)
* [Subscripions or Recurring Payments](https://docs.payu.in/docs/introduction-recurring-payments-integration)
* [International Payments](https://docs.payu.in/docs/introduction-dynamic-currency-conversion)
* [Pre-Authorize Payments](https://docs.payu.in/docs/auth-and-capture-pre-authorize-credit-card-payments)
* [Cross-Border Payments](https://docs.payu.in/docs/introduction-cross-border-payments-import)
* [Split Settlements](https://docs.payu.in/docs/split-settlments)
* [Tokenization or Save Cards](https://docs.payu.in/docs/introduction-save-cards)
* [Third-Party Verification (TPV)](https://docs.payu.in/docs/introduction-to-payu-tpv)
* [Recommendation Engine](https://docs.payu.in/docs/recommendation-engine)
* [Refunds](https://docs.payu.in/docs/introduction-refunds)

# MCP

Communicate with the PayU Payments APIs using Model Context Protocol and collection payments. For more information, refer to [PayU MCP](https://docs.payu.in/docs/payu-mcp-server/).

# Partnership and Payouts

* **Partner Integration**: For more information, refer to [Partner - Introduction](https://docs.payu.in/docs/payu-partner-program-overview#/)
* **Payouts**: For more information, refer to [Payouts - Introduction](https://docs.payu.in/docs/introduction-to-payouts/)

# Wallets

* [Merchant Wallets](https://docs.payu.in/docs/introduction-to-merchant-wallet/)

# Bill Payments

* [Connect Agent API Integration](https://docs.payu.in/docs/connect-agent-api-integration)
* [Recharge API Integration](https://docs.payu.in/docs/recharge-api-integration)

# Developer resources

* **Merchant Key and Salt**:  Before starting your integration, check your key and salt in the Dashboard. For more information, refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy) .
* **Test Card, UPI, Wallet, etc**:  For the card, EMI, UPI, wallet, BNPL details to test the integration, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

<br />

# 💳 Collect Payments on Your Website

PayU provides multiple integration options to help you collect payments on your website.
Each option is designed for different **developer needs, business requirements, and compliance levels**.

* If you want to **start quickly without coding**, choose a **No Code** solution.
* If you want PayU to **handle PCI compliance and payment pages**, choose **Hosted Checkout**.
* If you need **full control over the checkout UI** or already manage PCI compliance, use **Merchant Hosted** or **Server-to-Server** APIs.
* If you want a **high-conversion, optimized checkout** with additional business features, go with **CommercePro / Checkout Plus**.
* For mobile apps, use **PayU SDKs** (Android, iOS, React Native, Flutter, Cordova).
* If you’re running on **Shopify, WooCommerce, Magento, or other eCommerce platforms**, you can use ready-made **plugins**.

***

## Integration Options

### 🌐 Website Integrations

* [No Code Solutions](https://docs.payu.in/docs/introduction-no-code-payments-integration)
* [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted)
* [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)
* [Server-to-Server](doc:server-to-server-integration)
* [CommercePro Checkout](doc:checkout-express)
* [Checkout Plus](doc:checkout-plus-integration)

***

### 📱 Mobile SDKs

For app integrations, explore PayU’s SDKs:

* [Android](doc:explore-android-sdks)
* [iOS](doc:explore-ios-sdks)
* [React Native](doc:explore-reactnative-sdks)
* [Flutter](doc:flutter-sdk-introduction)
* [Cordova](doc:cordova-sdk-introduction)

***

### 🛍 eCommerce Plugins

If you’re on Shopify, WooCommerce, Magento, or similar platforms, use our ready-made plugins:

* [Plugins - Introduction](https://docs.payu.in/docs/ecommerce-platform-plugins/)

***

## 🔍 Integration Comparison Matrix

| Integration Type                               | Dev Effort                                                 | PCI Compliance Needed                        | Customization                                         | Best For                                                        |
| :--------------------------------------------- | :--------------------------------------------------------- | :------------------------------------------- | :---------------------------------------------------- | :-------------------------------------------------------------- |
| **No Code/Low Code** (Payment Link and Button) | Very Low                                                   | No (PayU handles all)                        | Minimal (branding, logo, colors)                      | Small merchants, instant setup                                  |
| **eCommerce Plugins**                          | Very Low                                                   | No                                           | Minimal                                               | Shopify, WooCommerce, Magento or any eCommerce plugin merchants |
| **PayU Hosted Checkout**                       | Low                                                        | No                                           | Minimal (branding, logo, colors)                      | SMBs, merchants looking for go-live                             |
| **Merchant Hosted**                            | Medium                                                     | Yes (cards handled on merchant site)         | High (full UI control)                                | Businesses with PCI DSS compliance                              |
| **Server-to-Server**                           | High                                                       | Yes                                          | Very High (own checkout flow + backend orchestration) | Large merchants, marketplaces                                   |
| **CommercePro / Plus**                         | Medium                                                     | No (PayU handles sensitive data)             | Medium (Optimized UI)                                 | Businesses optimizing for conversions                           |
| **Mobile SDKs**                                | Low to medium depending on type of checkout solution opted | Dependent on type of checkout solution opted | Medium (native customization)                         | Native Android/iOS/Hybrid apps                                  |
| **eCommerce Plugins**                          | Very Low                                                   | No                                           | Minimal                                               | Shopify, WooCommerce, Magento or any eCommerce plugin merchants |

***

✅ This way, merchants can first **read the summary**, then **scan the table** to decide quickly.
