---
title: Collect Cross-Border Payments on Shopify
deprecated: false
hidden: true
metadata:
  robots: index
---
You need to ensure that you implement the following steps to collect cross-border payments on Shopify.

## Step 1: Onboard on PayU Payments India as merchant

Merchants outside India using Shopify must onboard as merchant with PayU through PayU Key Account Manager (KAM) assisted flow.

<Callout icon="📘" theme="info">
  **Note:** Do not use PayU Dashboard to register as a merchant as it is only applicable for merchants in India.
</Callout>

## Step 2: Install the PayU Payments India plugin

1. Install the PayU payments plugin. For more information, refer to [Integrate with Shopify](doc:integrate-with-shopify)
2. Sync the oAuth on Shopify. Fore more information, contact your PayU KAM.

## Step 3: Integrate Update UDF API

Implement the **Update UDF** API for cross-border payments to update the invoice ID. For more information, refer to [UDF Update API](ref:udf_update_api).