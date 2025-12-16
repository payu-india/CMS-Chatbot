---
title: Cross-Border Payments on Shopify
excerpt: >-
  Merchants located outside India with Shopify web-stores can collect payments
  from Indian buyers
deprecated: false
hidden: false
metadata:
  robots: index
next:
  pages:
    - slug: shopify
      title: Shopify
      type: basic
    - slug: introduction-cross-border-payments-import
      title: Cross-Border Payments
      type: basic
---
Shopify merchants located outside India can utilize PayU to provide Indian payment methods (UPI, Netbanking, Credit & Debit cards) on their checkouts and get the funds settled to an offshore bank account in any desired foreign currency, as part of PayU's [PA-Cross-border](https://docs.payu.in/docs/introduction-cross-border-payments-import#/) stack.

## Steps to accept payments from Indian customers on your Shopify Store

### Step 1: Onboard on PayU Payments India & open a merchant account

Merchants outside India using Shopify must be onboarded on PayU.

<Callout icon="📘" theme="info">
  **Note:** Please reach out to your Key Account Manager or write to us at [crossborder@payu.in](mailto:crossborder@payu.in) to open a merchant account & get onboarded to PayU.
</Callout>

### Step 2: Install the PayU Payments India plugin

Install PayU payments plugin on your Shopify website as per the steps listed here: [Integrate with Shopify](doc:integrate-with-shopify). PayU offers two payment experiences on Shopify:

1. [PayU Hosted payment page ](https://apps.shopify.com/payu-india)(Redirect experience): Supports Cards (DC/CC), UPI, NetBanking & NEFT/RTGS payment methods. You can directly install the app by clicking [here](https://accounts.shopify.com/store-login?no_redirect=true\&redirect=%2Fadmin%2Fsettings%2Fpayments%2Falternative-providers%2F1058567) _(Shopify admin login required)._
2. [Onsite Cards](https://apps.shopify.com/onsite-cards-payments-by-payu) (Seamless experience on Shopify checkout page): Supports all Cards (DC / CC) across VISA & Mastercard schemes. You can directly install the app by clicking [here](https://accounts.shopify.com/store-login?no_redirect=true\&redirect=%2Fadmin%2Fsettings%2Fpayments%2Falternative-providers%2F1058567) _(Shopify admin login required)._

### Step 3: Integrate Update UDF API

Implement the **Update UDF** API for cross-border payments to update the following information. For more information, refer to [UDF Update API](ref:udf_update_api).

1. **Invoice ID** - Mandatory for all transactions - [To be updated in Var6 of the UDF Update API]
2. **Airway-Bill Number** - Mandatory for all physical goods transactions [To be updated in Var9 of the UDF Update API]

### Step 4: Configure checkout for Indian customers on Shopify Store

1. List your catalogue of products / SKUs in Indian National Rupees (INR) currency: Use [Shopify Markets](https://shopify.dev/docs/apps/build/markets) to manage regional pricing and present prices in INR to customers by creating an India-specific catalogue. For more information, refer to [Shopify Markets Documentation](https://shopify.dev/docs/apps/build/markets).
2. [Optional] Limit visibility of PayU payment option only to Indian customers. You can utilize third-party apps on Shopify App store such as - [Localized Payments](https://apps.shopify.com/localized-payments), [HidePay](https://apps.shopify.com/hidepay) etc.

## &#x20;FAQs

### How to manage refunds? Is there support for partial refunds?

Yes. Full and partial refunds process natively through the current plug-in. They can also be managed on PayU's merchant dashboard.

### How to get the settlement related information - status, currency & FX rate applied?

Settlement information is present in the "settlement tab" within the PayU merchant dashboard. APIs can also be provided on request.
