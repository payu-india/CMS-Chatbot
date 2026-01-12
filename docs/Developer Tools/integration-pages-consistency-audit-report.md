---
title: ' Integration Pages Consistency Audit Report'
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

**Generated:** January 12, 2026  
**Scope:** All documentation pages under `/docs` and subfolders

***

## Executive Summary

| Check                             | Total Files | Compliant | Non-Compliant | Compliance Rate |
| --------------------------------- | ----------- | --------- | ------------- | --------------- |
| H3/H4 with Accordion              | 240         | 43        | 197           | 18%             |
| cURL with Multi-Language Bindings | 100         | 46        | 54            | 46%             |
| Step Headings with Cards          | 138         | 62        | 76            | 45%             |

***

## 1. Pages with H3/H4 Headings but No Accordion

**Issue:** Content under Heading 3 (###) or Heading 4 (####) should be wrapped in `<Accordion>` components for better UX and content organization.

**Statistics:**

* Total files with H3/H4 headings: 240
* Files with Accordion implemented: 141
* Files missing Accordion: 197

### Files Requiring Accordion Implementation

#### API Basics

* `docs/API basics/api-authentication-and-security.md`
* `docs/API basics/handling-web-checkout/handling-the-redirect-urls.md`
* `docs/API basics/rest-api-format.md`

#### Collect Payments - Cordova SDK

* `docs/Collect Payments/cordova-sdk-introduction/dynamic-configuration-using-dashboard-2.md`
* `docs/Collect Payments/cordova-sdk-introduction/index.md`
* `docs/Collect Payments/cordova-sdk-introduction/internal-review-chargebacks.md`
* `docs/Collect Payments/cordova-sdk-introduction/one-click-checkout-with-net-banking-2.md`

#### Collect Payments - E-commerce Plugins

* `docs/Collect Payments/ecommerce-platform-plugins/interakt-for-whatsapp-business/integrate-payu-with-interakt.md`
* `docs/Collect Payments/ecommerce-platform-plugins/magento/install-and-configure-magento-plugin.md`
* `docs/Collect Payments/ecommerce-platform-plugins/odoo/install-and-configure-odoo-plugin.md`
* `docs/Collect Payments/ecommerce-platform-plugins/opencart/install-and-configure-opencart-plugin.md`
* `docs/Collect Payments/ecommerce-platform-plugins/opencart/troubleshooting-opencart-integration.md`
* `docs/Collect Payments/ecommerce-platform-plugins/prestashop/troubleshooting-prestashop-integration.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/affordability-widget-integration-for-shopify.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/collect-cross-border-payments-on-shopify.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/commercepro-cod-app-shopify.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/configure-sku-based-offers-shopify.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/install-commercepro-checkout-app.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/reconcile-shopify-transactions.md`
* `docs/Collect Payments/ecommerce-platform-plugins/woocommerce/commercepro-platform-for-woocommerce.md`
* `docs/Collect Payments/ecommerce-platform-plugins/woocommerce/install-and-configure-payu-woocommerce-plugin.md`

#### Collect Payments - Android SDKs

* `docs/Collect Payments/explore-android-sdks/android-checkoutpro-sdk/android-checkoutpro-oneclickcheckout-with-net-banking.md`
* `docs/Collect Payments/explore-android-sdks/android-checkoutpro-sdk/android-checkoutpro-tpv-integration.md`
* `docs/Collect Payments/explore-android-sdks/android-checkoutpro-sdk/dynamic-configuration-using-dashboard-copy.md`
* `docs/Collect Payments/explore-android-sdks/android-google-pay-sdk/index.md`
* `docs/Collect Payments/explore-android-sdks/android-google-pay-sdk/integration-steps-android-google-pay-sdk.md`
* `docs/Collect Payments/explore-android-sdks/android-phonepe-sdk/integration-steps-android-phonepe-sdk.md`
* `docs/Collect Payments/explore-android-sdks/android-upi-sdk/android-upisdk-tpv-integration.md`
* `docs/Collect Payments/explore-android-sdks/android-upi-sdk/integration-steps-android-upi-sdk.md`
* `docs/Collect Payments/explore-android-sdks/custom-browser-sdk/android-custombrowser-third-party-payment-support.md`
* `docs/Collect Payments/explore-android-sdks/custom-browser-sdk/integration-steps-android-customer-browser.md`
* `docs/Collect Payments/explore-android-sdks/faqs-android-sdk.md`
* `docs/Collect Payments/explore-android-sdks/flashpay-android-sdk/flashpay-coupled-flow-android-integration.md`
* `docs/Collect Payments/explore-android-sdks/flashpay-android-sdk/flashpay-decoupled-flow-android-integration-mfa.md`
* `docs/Collect Payments/explore-android-sdks/flashpay-android-sdk/index.md`
* `docs/Collect Payments/explore-android-sdks/generate-static-hash-android-sdk-pro.md`
* `docs/Collect Payments/explore-android-sdks/internal-reviewandriod-mobile-sdks.md`
* `docs/Collect Payments/explore-android-sdks/native-otp-assist-sdk/index.md`
* `docs/Collect Payments/explore-android-sdks/native-otp-assist-sdk/integration-steps-android-native-otp-assist.md`
* `docs/Collect Payments/explore-android-sdks/ola-money-sdk.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/payubolt-sdk-integration-native.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/upi-bolt-native-integration-procedure.md`

#### Collect Payments - iOS SDKs

* `docs/Collect Payments/explore-ios-sdks/flashpay-ios-sdk/3ds-20-flashpay-coupled-flow-ios-integration.md`
* `docs/Collect Payments/explore-ios-sdks/flashpay-ios-sdk/index.md`
* `docs/Collect Payments/explore-ios-sdks/generate-static-hash-ios.md`
* `docs/Collect Payments/explore-ios-sdks/internal-reviewios-mobile-sdks.md`
* `docs/Collect Payments/explore-ios-sdks/ios-checkoutpro-sdk/ios-checkoutprosdk-dynamic-configuration-using-dashboard.md`
* `docs/Collect Payments/explore-ios-sdks/ios-checkoutpro-sdk/ios-tpv-integration.md`
* `docs/Collect Payments/explore-ios-sdks/ios-core-sdk/index.md`
* `docs/Collect Payments/explore-ios-sdks/ios-custombrowser-sdk/ios-custombrowser-golive-checklist.md`

#### Collect Payments - ReactNative SDKs

* `docs/Collect Payments/explore-reactnative-sdks/react-native-checkoutpro-sdk/reactnative-checkoutpro-change-logs.md`
* `docs/Collect Payments/explore-reactnative-sdks/react-native-core-sdk/index.md`
* `docs/Collect Payments/explore-reactnative-sdks/react-native-core-sdk/reactnative-coresdk-integrate-with-android-copy.md`
* `docs/Collect Payments/explore-reactnative-sdks/react-native-core-sdk/reactnative-coresdk-supported-payment-types.md`
* `docs/Collect Payments/explore-reactnative-sdks/react-native-core-sdk/reactnative-coresdk-web-services.md`
* `docs/Collect Payments/explore-reactnative-sdks/upi-bolt-sdk-integration-react-native.md`

#### Collect Payments - Flutter SDK

* `docs/Collect Payments/flutter-sdk-introduction/flutter-checkoutpro-sdk/dynamic-configuration-using-dashboard-1.md`
* `docs/Collect Payments/flutter-sdk-introduction/flutter-checkoutpro-sdk/index.md`
* `docs/Collect Payments/flutter-sdk-introduction/flutter-checkoutpro-sdk/one-click-checkout-with-net-banking-1.md`
* `docs/Collect Payments/flutter-sdk-introduction/flutter-custombrowser-sdk.md`
* `docs/Collect Payments/flutter-sdk-introduction/payubolt-flutter-integration/index.md`

#### Collect Payments - Web Integration

* `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/generate-hash-merchant-hosted.md`
* `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/index.md`
* `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/paypal-integration.md`
* `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/test-integration.md`
* `docs/Collect Payments/introduction-web/checkout-plus-integration/integrate-webview-for-mobile-apps-checkout-plus.md`
* `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/generate-hash-payu-hosted.md`
* `docs/Collect Payments/introduction-web/test-cards-upi-id-and-wallets.md`
* `docs/Collect Payments/introduction-web/webhooks.md`

#### Developer Tools

* `docs/Developer Tools/webhooks-consolidated/create-and-manage-webhooks.md`
* `docs/Developer Tools/webhooks-consolidated/index.md`

#### Getting Started

* `docs/getting started/check-api-key-and-salt.md`
* `docs/getting started/choose-your-integration.md`
* `docs/getting started/introduction/index.md`
* `docs/getting started/payu-dashboard/add-features-to-your-account.md`
* `docs/getting started/payu-dashboard/bank-account.md`
* `docs/getting started/payu-dashboard/business-detail.md`
* `docs/getting started/payu-dashboard/configure-email-notification.md`
* `docs/getting started/payu-dashboard/configure-invoices.md`
* `docs/getting started/payu-dashboard/generate-api-keys-and-salt.md`
* `docs/getting started/payu-dashboard/my-stores.md`
* `docs/getting started/payu-dashboard/payu-dashboard-main.md`
* `docs/getting started/payu-dashboard/settlements.md`
* `docs/getting started/payu-dashboard/transactions.md`

#### Offerings

* `docs/Offerings/affordability-introduction.md`
* `docs/Offerings/chargeback/faqs-for-chargeback.md`
* `docs/Offerings/introduction-refunds/internal-reviewrefunds-overview.md`
* `docs/Offerings/introduction-refunds/refunds-dashboard/index.md`
* `docs/Offerings/introduction-refunds/refunds-dashboard/refund-wallet-dashboard.md`
* `docs/Offerings/introduction-refunds/refunds-in-payu-products/refunds-for-bnpl.md`
* `docs/Offerings/introduction-refunds/refunds-in-payu-products/refunds-for-emi.md`
* `docs/Offerings/introduction-refunds/refunds-in-payu-products/refunds-for-offers.md`
* `docs/Offerings/introduction-to-eftnet/payu-hosted-checkout-eftnet.md`
* `docs/Offerings/introduction-to-eftnet/collect-payments-with-eftnet-neftrtgs-seamless/reusable-van-integration-neft.md`
* `docs/Offerings/recommendation-engine/index.md`
* `docs/Offerings/recommendation-engine/re-customer-journey.md`
* `docs/Offerings/wealth-tech-payments/index.md`

#### Partners

* `docs/partners/faqs-partner-integration.md`
* `docs/partners/refer-merchants-using-api.md`

#### Payouts

* `docs/payouts/introduction-to-payouts.md`
* `docs/payouts/payouts-integration/payouts-webhooks.md`
* `docs/payouts/releasepending-pay-to-phone-integration/index.md`
* `docs/payouts/releasepending-pay-to-phone-integration/releasepending-pay-to-phone-initiation.md`

#### Monitoring & Alerts

* `docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/index.md`

_... and 97 more files (see full list in script output)_

***

## 2. Pages with cURL Examples but Missing Language Bindings

**Issue:** Sample Request sections containing cURL examples should include equivalent code in Python, Java, JavaScript, and PHP for better developer experience.

**Statistics:**

* Total files with cURL examples: 100
* Files with all language bindings: 46
* Files missing some language bindings: 54

### Files Missing Language Bindings

| File                                                                                                                                                                  | Missing Languages             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `docs/BBPS/connect-agent-api-integration-1.md`                                                                                                                        | Python, Java, PHP             |
| `docs/Collect Payments/explore-ios-sdks/ios-native-otp-assist-sdk.md`                                                                                                 | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/faqs-payment-links.md`                                                       | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/collect-payments-with-upi-seamless.md`                                                        | PHP                           |
| `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/payu-payment-page-customization.md`                                                             | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/webview-for-mobile-apps.md`                                                                     | Python, JavaScript, PHP       |
| `docs/Collect Payments/introduction-web/server-to-server-integration/decoupled-flow-authentication-only-integration.md`                                               | Python, Java, PHP             |
| `docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-decoupled-flow-s2s.md`                                                            | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-direct-authorization-s2s.md`                                                      | Python, Java, PHP             |
| `docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-s2s-for-cards-classic-integration.md`                                             | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-web/server-to-server-integration/integrate-with-s2s.md`                                                                           | Python, Java, JavaScript, PHP |
| `docs/Collect Payments/introduction-web/server-to-server-integration/legacy-flow-for-server-to-server.md`                                                             | Python, Java, JavaScript, PHP |
| `docs/MCP/install-and-configure-payu-mcp-server.md`                                                                                                                   | Python, Java, PHP             |
| `docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md`                                                                                         | Java, PHP                     |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/pre-authorize-card-transactions/credit-card-merchant-hosted-integration-pre-authorize-payment.md` | Python, Java, JavaScript, PHP |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/pre-authorize-card-transactions/debit-card-merchant-hosted-integration-preauthorize-payments.md`  | Python, Java, JavaScript, PHP |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/pre-authorize-card-transactions/payu-hosted-integration-pre-authorize-payments.md`                | Python, Java, PHP             |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/s2s-pre-authorize-payment.md`                                                                     | Python, Java, JavaScript, PHP |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/upi-one-time-mandate-integration/upi-collect-one-time-mandate-integration.md`                     | Python, Java, JavaScript, PHP |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/upi-one-time-mandate-integration/upi-intent-one-time-mandate-integration-payu-hosted.md`          | Python, Java, JavaScript, PHP |
| `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/upi-one-time-mandate-integration/upi-intent-one-time-mandate-integration.md`                      | Python, Java, JavaScript, PHP |
| `docs/Offerings/internal-subscripions-or-recurring-payments/subscriptions-integration/payu-hosted-integration-subscriptions.md`                                       | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-cross-border-payments-import/cb-lrs-integration/cb-lrs-merchant-hosted-api-integration.md`                                               | Python, Java, PHP             |
| `docs/Offerings/introduction-cross-border-payments-import/cb-lrs-integration/integrate-payu-hosted-checkout-cb-lrs.md`                                                | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-cross-border-payments-import/cb-subscription-integration-seamless/upi-consent-transaction-cb.md`                                         | Java                          |
| `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-for-payubiz.md`                                                             | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/index.md`                                                     | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-cross-border-payments-import/integrate-import-with-upi-autopay-for-payubiz/post-an-upi-consent-transaction-cb.md`                        | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-recurring-payments-integration/payment-consent-transaction-using-payu-hosted-checkout-copy.md`                                           | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/emi-api-integration/cardless-emi-s2s-integration.md`                                                                    | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/steps-to-integrate-mobikwik-link-pay.md`                                                  | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/offers-integration/instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout.md`                   | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/offers-integration/payu-hosted-checkout-integration-with-offers.md`                                                     | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/collect-payments-with-bnpl-using-link-and-pay.md`                                    | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/general-flow-bnpl-integration-with-merchant-hosted.md`                               | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-affordability/payu-bnpl-integration-introduction/native-otp-flow-bnpl-integration-with-merchant-hosted.md`                            | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-merchant-wallet/wallet-management-issuance-journey/merchant-hosted-checkout-integration-merchant-wallet.md`                           | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-merchant-hosted-checkout/upi-intent-and-collect-autopay-tpv-integration.md`                        | Python, Java, JavaScript, PHP |
| `docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-merchant-hosted-checkout/upi-integration-for-tpv.md`                                               | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/api-integration-for-split-settlements/onboarding-child-merchants-integration.md`                                                     | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/api-integration-for-split-settlements/split-during-transaction-integration.md`                                                       | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/introduction-split-settlements/convenience-fee-handling.md`                                                                          | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/introduction-split-settlements/create-the-split.md`                                                                                  | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/introduction-split-settlements/fetch-child-merchants-details-1.md`                                                                   | Python, Java, JavaScript, PHP |
| `docs/Offerings/split-settlments/introduction-split-settlements/index.md`                                                                                             | Python, Java, JavaScript, PHP |
| `docs/Offerings/twid-zillion-coins-integration/twid-seamless-transaction-integration/index.md`                                                                        | Python, Java, JavaScript, PHP |
| `docs/Offerings/twid-zillion-coins-integration/twid-seamless-transaction-integration/twid-seamless-card-transaction-integration.md`                                   | Python, Java, JavaScript, PHP |
| `docs/Offerings/twid-zillion-coins-integration/twid-seamless-transaction-integration/twid-seamless-upi-transaction-integration.md`                                    | Python, Java, JavaScript, PHP |
| `docs/Offerings/wealth-tech-payments/upi-autopay-integration-wealth-tech-payment.md`                                                                                  | Python, Java, JavaScript, PHP |
| `docs/partners/refer-merchants-using-api.md`                                                                                                                          | Python, Java, JavaScript, PHP |
| `docs/payouts/payouts-integration/single-transfer-integration-for-payouts.md`                                                                                         | Python, Java, JavaScript, PHP |
| `docs/payu rewardsx/introduction-flipkart-supercoins-pay/merchant-hosted-checkout-integration-supercoins-pay.md`                                                      | Python, Java, JavaScript, PHP |
| `docs/payu rewardsx/introduction-to-flipkart-supercoins/merchant-hosted-integration-fksc.md`                                                                          | Python, Java, JavaScript, PHP |

_... and 24 more files_

***

## 3. Pages with Step Headings but No Cards Navigation

**Issue:** Pages containing `## Step 1`, `## Step 2`, etc. headings should include `<Card>` or `<Cards>` MDX components at the top to provide quick navigation to each step.

**Statistics:**

* Total files with Step headings: 138
* Files with Cards navigation: 62
* Files missing Cards navigation: 76

### Files Missing Cards Navigation

#### API Basics

* `docs/API basics/using-payu-hash-verification-tool.md`

#### Collect Payments - SDKs

* `docs/Collect Payments/cordova-sdk-introduction/cordova-checkoutprosdk-integration-steps.md`
* `docs/Collect Payments/explore-android-sdks/android-checkoutpro-sdk/android-checkoutpro-tpv-integration.md`
* `docs/Collect Payments/explore-android-sdks/android-core-sdk/android-coresdk-tpv-integration.md`
* `docs/Collect Payments/explore-android-sdks/android-core-sdk/integration-steps-android-core-sdk.md`
* `docs/Collect Payments/explore-android-sdks/android-google-pay-sdk/integration-steps-android-google-pay-sdk.md`
* `docs/Collect Payments/explore-android-sdks/flashpay-android-sdk/flashpay-decoupled-flow-android-integration-mfa.md`
* `docs/Collect Payments/explore-android-sdks/native-otp-assist-sdk/integration-steps-android-native-otp-assist.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/android-standing-instruction-parameters.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/payu-otp-parser.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/payubolt-sdk-integration-native.md`
* `docs/Collect Payments/explore-android-sdks/payu-bolt-sdk/upi-bolt-native-integration-procedure.md`
* `docs/Collect Payments/explore-ios-sdks/ios-checkoutpro-sdk/ios-tpv-integration.md`
* `docs/Collect Payments/explore-ios-sdks/ios-core-sdk/ios-coresdk-integrate-tpv.md`
* `docs/Collect Payments/explore-ios-sdks/ios-core-sdk/ios-coresdk-setup-recurring-payments.md`
* `docs/Collect Payments/explore-ios-sdks/ios-custombrowser-sdk/ios-custombrowser-make-payment-using-custom-browser.md`
* `docs/Collect Payments/explore-ios-sdks/ios-standing-instructions-parameters.md`
* `docs/Collect Payments/explore-reactnative-sdks/react-native-core-sdk/reactnative-coresdk-integrate-with-android-copy.md`
* `docs/Collect Payments/flutter-sdk-introduction/flutter-checkoutpro-sdk/flutter-checkoutprosdk-integration-steps.md`

#### Collect Payments - E-commerce

* `docs/Collect Payments/ecommerce-platform-plugins/shopify/affordability-widget-integration-for-shopify.md`
* `docs/Collect Payments/ecommerce-platform-plugins/shopify/reconcile-shopify-transactions.md`
* `docs/Collect Payments/ecommerce-platform-plugins/woocommerce/affordability-widget-integration-for-woocommerce.md`

#### Collect Payments - Web Integration

* `docs/Collect Payments/introduction-no-code-payments-integration/payment-buttons-dashboard.md`
* `docs/Collect Payments/introduction-web/server-to-server-integration/classic-integration-for-cards-otp-integration.md`
* `docs/Collect Payments/introduction-web/server-to-server-integration/legacy-flow-for-server-to-server.md`

#### Collect Payments - Ionic

* `docs/Collect Payments/upi-bolt-sdk-ionic/upi-bolt-capacitor-ionic-angular-sdk-integration.md`

#### Monitoring & Alerts

* `docs/Monitoring & Alerts/flashpay-ios-integration-wibmo-mfa.md`

#### Offerings - Auth & Capture

* `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/s2s-pre-authorize-payment.md`
* `docs/Offerings/auth-and-capture-pre-authorize-credit-card-payments/upi-one-time-mandate-integration/upi-intent-one-time-mandate-integration-payu-hosted.md`

#### Offerings - Chargeback

* `docs/Offerings/chargeback/chargeback-process.md`

#### Offerings - Cross-Border Payments

* `docs/Offerings/introduction-cross-border-payments-import/cb-lrs-integration/cb-lrs-merchant-hosted-api-integration.md`
* `docs/Offerings/introduction-cross-border-payments-import/cb-lrs-integration/integrate-payu-hosted-checkout-cb-lrs.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/cards-with-payu-tokenization-one-time-pacb.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/cb-integration-non-seamless.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/network-tokens-one-time-payment-pacb.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/plain-cards-integration-one-time-pacb.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-with-payu-new/plain-cards-with-tokenization-integration-one-time-pacb.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-import-with-upi-autopay-for-payubiz/post-a-upi-recurring-transaction-cb.md`
* `docs/Offerings/introduction-cross-border-payments-import/integrate-import-with-upi-autopay-for-payubiz/post-an-upi-consent-transaction-cb.md`

#### Offerings - Recurring Payments

* `docs/Offerings/introduction-recurring-payments-integration/payment-consent-transaction-using-payu-hosted-checkout-copy.md`
* `docs/Offerings/introduction-recurring-payments-integration/subscription-dashboard/create-a-subscription-payment-link-using-dashboard.md`

#### Offerings - Affordability

* `docs/Offerings/introduction-to-affordability/emi-api-integration/cardless-emi-s2s-integration.md`
* `docs/Offerings/introduction-to-affordability/loyalty-edge-introduction/launch-loyalty-program-using-dashboard.md`
* `docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/steps-to-integrate-mobikwik-link-pay.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-a-milestone-offer.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-a-no-cost-emi-offer.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-a-pre-discounted-offer.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-an-offer.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-downpaymentemi-offer.md`
* `docs/Offerings/introduction-to-affordability/offers-dashboard/create-personalized-coupon.md`

#### Offerings - Merchant Wallet

* `docs/Offerings/introduction-to-merchant-wallet/wallet-management-issuance-journey/load-and-pay-integration-clw.md`
* `docs/Offerings/introduction-to-merchant-wallet/wallet-management-issuance-journey/register-you-customer-intregration-clw.md`

#### Offerings - TPV

* `docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-merchant-hosted-checkout/net-banking-integration-for-tpv.md`
* `docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-merchant-hosted-checkout/upi-integration-for-tpv.md`

#### Offerings - Split Settlements

* `docs/Offerings/split-settlments/api-integration-for-split-settlements/onboarding-child-merchants-integration.md`
* `docs/Offerings/split-settlments/api-integration-for-split-settlements/split-during-transaction-integration.md`
* `docs/Offerings/split-settlments/introduction-split-settlements/create-the-split.md`
* `docs/Offerings/split-settlments/introduction-split-settlements/fetch-child-merchants-details-1.md`

#### Offerings - Virtual Cards

* `docs/Offerings/virtual-cards-introduction/web-integration-virtual-cards/iframe-virtual-cards-api-integration.md`
* `docs/Offerings/virtual-cards-introduction/web-integration-virtual-cards/payu-hosted-virtual-cards-api-integration.md`

#### Offerings - Wealth Tech

* `docs/Offerings/wealth-tech-payments/merchant-hosted-integration-wealth-tech-payment.md`

#### Payouts

* `docs/payouts/payouts-integration/single-transfer-integration-for-payouts.md`

_... and 26 more files_

***

## Recommendations

### Priority 1: High Impact Pages

Focus on pages that are frequently accessed or critical for integration:

1. Server-to-server integration pages (S2S)
2. Pre-authorize payment pages
3. Cross-border payment integration pages
4. UPI integration pages

### Priority 2: Quick Wins

Pages that need minimal changes:

1. Files missing only 1-2 language bindings
2. Files with existing Accordion patterns that can be replicated

### Priority 3: Template Standardization

Create templates for:

1. Standard Accordion structure for H3/H4 content
2. Multi-language code block format
3. Cards navigation component for Step-based pages

***

## Action Items

* [ ] Add Accordion components to 197 files with H3/H4 headings
* [ ] Add missing language bindings to 54 files with cURL examples
* [ ] Add Cards navigation to 76 files with Step headings
* [ ] Create documentation style guide for consistency
* [ ] Implement automated linting for documentation patterns
