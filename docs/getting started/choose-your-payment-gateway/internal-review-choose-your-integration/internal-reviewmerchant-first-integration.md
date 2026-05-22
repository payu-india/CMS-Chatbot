---
title: '[Internal Review]Merchant First Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Merchant First Integration Guide
excerpt: >-
  Find the right PayU integration docs, troubleshooting, and go-live steps
  based on common merchant integration topics.
deprecated: false
hidden: false
metadata:
  title: Merchant First Integration Guide
  description: >-
    Route PayU integration questions to the right documentation—Payment APIs,
    web checkout, mobile SDKs, webhooks, plugins, and when to contact your KAM.
  robots: index
next:
  description: ''
---
Use this guide to find documentation quickly. It is organized around topics that appear most often in merchant integration support cases.

> 📘 Start here if you are unsure which integration path to use: [Choose your Integration](doc:choose-your-integration) and [Payment APIs Getting Started](doc:payment-apis-getting-started).

## Payment APIs and web checkout

| Your goal | Start here | Go-live / checklist | Troubleshooting |
| :-------- | :--------- | :------------------ | :-------------- |
| Collect payment with minimal coding (redirect to PayU) | [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) | [Integration Checklist - Plugins](doc:integration-checklist-plugins) (if using a platform) | [FAQs for Web Checkout Integration](doc:faqs-for-web-checkout-integration) |
| Full control of checkout UI on your website | [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted) | [Integration Checklist - Merchant Hosted Checkout](doc:integration-checklist-merchant-hosted-checkout) | [Generate Hash](doc:generate-hash-merchant-hosted), [Hash Verification Tool](doc:using-payu-hash-verification-tool) |
| Backend orchestration (S2S / decoupled) | [Server-to-Server Integration](doc:server-to-server-integration) | [Integration Checklist - S2S](doc:integration-checklist-s2s) | [FAQs for Web Checkout Integration](doc:faqs-for-web-checkout-integration) |
| Payment Links, invoices, no-code | [Introduction - No Code Payments](doc:introduction-no-code-payments-integration) | [FAQs - Payment Links](doc:faqs-payment-links) | [FAQs for Web Checkout Integration](doc:faqs-for-web-checkout-integration) |
| Verify transaction status | [Verify Payment API](ref:verify_payment_api) | [Go-Live Checklist - All Integrations](doc:go-live-checklist-all-integrations) | [General API Testing](doc:general-api-testing) |

**Payment APIs hub:** [Payment APIs Getting Started](doc:payment-apis-getting-started)

## Mobile SDKs

| Platform | Explore SDKs | FAQs | Troubleshooting |
| :------- | :------------- | :--- | :-------------- |
| Android | [Explore Android SDKs](doc:explore-android-sdks) | [FAQs - Android SDK](doc:faqs-android-sdk) | [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors) |
| iOS | [Explore iOS SDKs](doc:explore-ios-sdks) | [FAQs - iOS SDK](doc:ios-sdk-faqs) | [iOS Custom Browser - Test Integration](doc:ios-custombrowser-test-integration) |
| React Native | [Explore React Native SDKs](doc:explore-reactnative-sdks) | [FAQs - React Native SDK](doc:faqs-react-native-sdk) | [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors) (Android layer) |
| Flutter | [Flutter SDK Introduction](doc:flutter-sdk-introduction) | [FAQs - Flutter SDK](doc:faqs-flutter-sdk) | [Generate Dynamic Hash - Flutter](doc:generate-dynamic-hash-flutter) |

**Hash (all mobile SDKs):** Generate hashes on your **server**, not in the app. See [Hash Generation - Android](doc:hash-generation), [Generate Dynamic Hash - CheckoutPro](doc:hash-generation-for-checkoutpro-sdk), and [Handling Redirect URLs (surl/furl) - Android](doc:handling-redirect-urls-surlfurl-with-android-sdk).

## Webhooks

| Task | Documentation |
| :--- | :------------ |
| Create / edit payment webhooks on Dashboard | [Create a New Webhook](doc:create-a-new-webhook), [Payment Webhooks](doc:create-and-manage-webhooks-1) |
| Debug delivery failures | [Using Webhook Logs](doc:using-webhook-logs) |
| Sample payloads | [Webhook Events and Sample Payloads](doc:webhook-events-and-sample-payloads) |

Configure webhooks in **Test Mode** first, then repeat for **Live Mode** with production URLs.

## Ecommerce plugins

| Platform | Integrate | Troubleshoot | Checklist |
| :------- | :-------- | :----------- | :-------- |
| Shopify | [Integrate with Shopify](doc:integrate-with-shopify) | [Troubleshooting Shopify Integration](doc:troubleshooting-shopify-integration) | [Production Checklist - Plugins](doc:integration-checklist-plugins) |
| WooCommerce | [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin) | [Troubleshooting WooCommerce Integration](doc:troubleshooting-woocommerce-integration) | [Production Checklist - Plugins](doc:integration-checklist-plugins) |
| Other platforms | [Plugins - Introduction](doc:ecommerce-platform-plugins) | Platform-specific troubleshooting pages under each plugin folder | [Production Checklist - Plugins](doc:integration-checklist-plugins) |

## Offerings (common add-ons)

| Topic | Documentation |
| :---- | :------------ |
| Subscriptions / SI | [Recurring Payments Integration](doc:introduction-recurring-payments-integration), [FAQs - Recurring Payments](doc:faqs-recurring-payments) |
| Split settlements | [Split Settlements](doc:split-settlments), [FAQs for Split Settlements](doc:faqs-for-split-settlements) |
| TPV | [Introduction to PayU TPV](doc:introduction-to-payu-tpv), [FAQs - TPV Integration](doc:faqs-tpv-integration) |
| Refunds | [Introduction to Refunds](doc:introduction-refunds) |

## Credentials and environments

| Task | Documentation |
| :--- | :------------ |
| Test Key and Salt | [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) |
| Production Key and Salt | [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard) |
| Test vs production endpoints | [PayU India API Environment](doc:payu-india-api-environment) |
| Before go-live (all products) | [Go-Live Checklist - All Integrations](doc:go-live-checklist-all-integrations) |

## When to contact your PayU Key Account Manager (KAM)

Contact your **PayU Key Account Manager (KAM)** for account-level enablement that documentation cannot change from your side:

* Payment mode or feature flags on your MID (for example `txn-s2s_flow`, UPI Intent, PhonePe in-app, fleet card category)
* Production activation of specific payment methods after UAT
* Store card / TRID onboarding for tokenization
* Server-to-Server enablement on your merchant account
* International payments, subscriptions, or specialized offerings not visible on your Dashboard

For integration **how-to** steps, use the documentation links above first. For product defects after you have followed the checklist, use [PayU Support](https://help.payu.in/).

## What is usually not an integration documentation issue

Roughly 9% of integration cases are marked **no action required from the integration team**—for example dormant account reactivation, internal MID configuration, or production-support-only flags. Use Dashboard status and your KAM for those requests rather than changing integration code.
