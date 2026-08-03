---
title: '[Internal] Plugin Integration FAQs'
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Plugin Integration FAQs — Proposed for Review
excerpt: Draft FAQs derived from SFDC cases (Apr–Jun 2026) for plugin integration review
deprecated: false
hidden: true
metadata:
  title: Plugin Integration FAQs — Proposed for Review
  description: Proposed plugin integration FAQs for internal review before publishing to platform FAQ pages
  robots: noindex
next:
  description: ''
---
This section consolidates **proposed FAQs** for PayU ecommerce platform plugin integrations. Content is based on analysis of `Temp/April to June SFDC cases (1).xlsx` (plugin-related themes from April–June 2026) and gaps in existing platform FAQ pages.

> **Status:** Draft for review only. Do not treat as published documentation until approved and moved to the relevant platform FAQ pages.

<Callout icon="📘" theme="info">
  **Source:** SFDC integration cases tagged with platform names (Shopify, WooCommerce, Magento, Wix, BigCommerce, OpenCart, Zoho, Odoo, Fynd, CommercePro). **Target pages after approval:** `faqs-for-<platform>.md` or platform `index.md` as applicable.
</Callout>

---

## Common for all Plugins

<Accordion title="1. Is the Verify Payment API available in UAT or sandbox for plugin testing?" icon="fa-info-circle">
  Yes. Use the PayU test environment and test merchant key and Salt to call the [Verify Payment API](ref:verify_payment_api) after a test transaction. Confirm you are using UAT credentials and the test endpoint documented for your integration type. For test credentials, refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="2. Why does PayU gateway setup fail even when I enter the correct key and Salt?" icon="fa-info-circle">
  Check the following:

  * Use key and Salt from the **same environment** (test or production).
  * Copy the Salt directly from PayU Dashboard; it is **case-sensitive**.
  * Remove leading or trailing spaces from key, Salt, and other configuration values.
  * Confirm your merchant account is active and not dormant.

  For credential access, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) or [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="3. Payment modes are enabled on my PayU account but not visible on my store checkout. What should I check?" icon="fa-info-circle">
  * Confirm the payment mode is enabled on your **merchant account** (MID), not only in the plugin UI.
  * Check plugin-specific settings (for example, payment mode checkboxes in the Shopify app).
  * Ensure you are using the correct PayU app or plugin for the payment modes you need (for example, hosted checkout for UPI and Net Banking vs onsite cards only).
  * Contact your PayU Key Account Manager (KAM) to confirm UPI, wallets, EMI, or Net Banking are enabled for your account.
</Accordion>

<Accordion title="4. Do I need to configure webhooks for standard plugin integrations?" icon="fa-info-circle">
  Webhooks are recommended for reliable transaction status updates alongside browser redirects. Some use cases require webhooks by design (for example, SKU-based offers on Shopify). Configure webhooks in PayU Dashboard and validate payloads using the documented hash formula. For more information, refer to [Webhooks](doc:webhooks) and [Create a New Webhook](doc:create-a-new-webhook).
</Accordion>

<Accordion title="5. How do I map platform order IDs to PayU transactions for reconciliation?" icon="fa-info-circle">
  Store the PayU transaction ID (`mihpayid` or equivalent) and your platform order ID in your order records at payment callback. Use the [Verify Payment API](ref:verify_payment_api) and PayU Dashboard transaction reports to reconcile. Platform-specific bulk reconciliation options vary; refer to guides such as [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions) where available.
</Accordion>

---

## Shopify

<Accordion title="1. Why are UPI, Net Banking, or wallets missing on Shopify when card payments work?" icon="fa-info-circle">
  Check the following:

  1. You are using **Cards, UPI, NB by PayU India** (hosted checkout), not only **Onsite Card Payments by PayU India**.
  2. Required payment modes are selected in the PayU app configuration on Shopify.
  3. UPI, Net Banking, and wallets are **enabled on your merchant account**. Contact your PayU Key Account Manager (KAM) if a mode is missing at the account level.

  For more information, refer to [FAQs for Shopify](doc:faqs-for-shopify) and [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="2. Does PayU support subscription or recurring payments on Shopify?" icon="fa-info-circle">
  Standard PayU Shopify plugin integrations are designed for one-time checkout payments. Recurring or subscription billing typically requires a dedicated recurring payments integration path. For subscription use cases, contact your PayU Key Account Manager (KAM) and refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
</Accordion>

<Accordion title="3. Do I need to configure webhooks for a standard Shopify PayU integration?" icon="fa-info-circle">
  Webhooks are recommended to receive payment status updates reliably. SKU-based offers require specific Shopify webhooks; standard integrations also benefit from payment event webhooks configured in PayU Dashboard. For more information, refer to [Webhooks](doc:webhooks) and [FAQs for Shopify](doc:faqs-for-shopify).
</Accordion>

<Accordion title="4. Do I need to implement UPI Intent or NPCI OC190 separately on Shopify with PayU hosted checkout?" icon="fa-info-circle">
  PayU Hosted Checkout handles applicable NPCI requirements, including UPI Smart Intent, on the PayU-hosted payment page. Merchants using custom or seamless checkout flows must implement applicable requirements in their own checkout. For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) and [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow).
</Accordion>

---

## WooCommerce

<Accordion title="1. Why is the Buy Now with PayU or CommercePro button unclickable on WooCommerce?" icon="fa-info-circle">
  Check the following:

  * **Plugin version compatibility** with your WooCommerce version. Use the PayU plugin version documented for your WooCommerce release. Refer to [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin).
  * **CommercePro-specific settings**, including whether guest checkout is disabled while CommercePro expects a logged-in flow.
  * Browser console and server error logs for JavaScript or PHP conflicts with your theme or other plugins.
  * Clear WordPress and WooCommerce cache after plugin updates.

  If the issue persists, contact [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="2. Does CommercePro on WooCommerce require customers to create an account before checkout?" icon="fa-info-circle">
  Merchant checkout settings affect CommercePro behaviour. If **guest checkout is disabled** in WooCommerce, customers must log in or register before completing CommercePro checkout. Align WooCommerce account settings with your CommercePro customer journey. For more information, refer to [CommercePro Checkout for WooCommerce](doc:commercepro-platform-for-woocommerce).
</Accordion>

<Accordion title="3. Which PayU plugin version should I use for my WooCommerce version?" icon="fa-info-circle">
  PayU supports WooCommerce 3.x or later. Download the plugin version that matches your WooCommerce release from the version table in [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin). Using an incompatible plugin version can cause site errors or a non-functional checkout button.
</Accordion>

<Accordion title="4. Can I use CommercePro Checkout and the standard PayU WooCommerce plugin together?" icon="fa-info-circle">
  CommercePro Checkout is a separate integration path from the standard PayU WooCommerce plugin. Use CommercePro for OTP login, address vault, and Checkout Express features. Use the standard plugin for hosted PayU checkout without CommercePro. Confirm your use case with your PayU Key Account Manager (KAM) before running both on the same store.
</Accordion>

<Accordion title="5. Why did my WooCommerce site crash after installing the PayU plugin?" icon="fa-info-circle">
  This is usually caused by a **plugin version mismatch** with your WooCommerce or PHP version. Uninstall the incompatible plugin, restore from backup if needed, and install the correct PayU plugin version for your WooCommerce release. Refer to the download table in [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin).
</Accordion>

<Accordion title="6. Does PayU support recurring or subscription payments on WooCommerce?" icon="fa-info-circle">
  PayU does not support recurring payments through the standard WooCommerce plugin. Use PayU Web Checkout recurring payments integration for subscription use cases. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration) and [FAQs for WooCommerce](doc:troubleshooting-woocommerce-integration).
</Accordion>

---

## CommercePro Checkout

<Accordion title="1. Which platforms support PayU CommercePro Checkout?" icon="fa-info-circle">
  PayU CommercePro Checkout is supported on **WooCommerce** and **Magento**, with additional Shopify capabilities through CommercePro apps (Checkout, COD). For installation guides, refer to [CommercePro Checkout for WooCommerce](doc:commercepro-platform-for-woocommerce), [CommercePro Checkout for Magento](doc:commercepro-platform-for-magento), and [Install CommercePro Checkout App](doc:install-commercepro-checkout-app) for Shopify.
</Accordion>

<Accordion title="2. Why is Checkout Express or Buy Now with PayU not working on my storefront?" icon="fa-info-circle">
  Check the following:

  * CommercePro plugin is installed and enabled for your platform and WooCommerce/Magento version.
  * Correct production or test key and Salt are configured.
  * Theme or custom frontend (including headless storefronts) does not block CommercePro JavaScript or checkout buttons.
  * Guest checkout, login, and return URL settings are configured correctly.

  For platform-specific steps, refer to [CommercePro Checkout](doc:commercepro-checkout) and the WooCommerce or Magento CommercePro guide.
</Accordion>

<Accordion title="3. Does CommercePro support subscriptions or recurring billing on WooCommerce?" icon="fa-info-circle">
  CommercePro Checkout on WooCommerce is designed for standard checkout flows. Recurring or subscription billing is not supported through the WooCommerce CommercePro plugin path. For subscriptions, use PayU recurring payments integration. Refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
</Accordion>

<Accordion title="4. How do I test CommercePro Checkout before going live?" icon="fa-info-circle">
  Configure test merchant key and Salt from PayU Dashboard, enable test mode in the CommercePro plugin settings, and complete end-to-end test transactions. Verify results using the [Verify Payment API](ref:verify_payment_api). Refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="5. Can CommercePro Checkout work on a custom or headless storefront?" icon="fa-info-circle">
  CommercePro Checkout Express is documented for supported platforms (WooCommerce, Magento, Shopify apps). Custom or headless storefronts (for example, Next.js) require validation with PayU integration teams. Contact your PayU Key Account Manager (KAM) before implementing CommercePro on a non-standard storefront.
</Accordion>

<Accordion title="6. What WooCommerce and PayU plugin versions are required for CommercePro?" icon="fa-info-circle">
  Use the CommercePro plugin build documented for your WooCommerce version. The standard PayU WooCommerce plugin compatibility table in [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin) and the CommercePro guide in [CommercePro Checkout for WooCommerce](doc:commercepro-platform-for-woocommerce) define supported combinations.
</Accordion>

---

## Magento

<Accordion title="7. Why is only card payment showing on Magento after PayU integration?" icon="fa-info-circle">
  Check the following:

  * You installed the correct **PayU Magento plugin version** for your Magento release from PayU GitHub.
  * UPI, Net Banking, and wallets are **enabled on your merchant account**. Contact your PayU Key Account Manager (KAM) if required modes are not enabled.
  * Plugin and Magento cache are cleared after configuration changes.

  For more information, refer to [Install and Configure PayU Magento Plugin](doc:install-and-configure-magento-plugin) and [FAQs for Magento](doc:faqs-for-magento).
</Accordion>

<Accordion title="8. How do I enable UPI, Net Banking, and wallets for Magento?" icon="fa-info-circle">
  Configure the PayU Magento plugin with your merchant key and Salt, then confirm the required payment modes are enabled on your PayU merchant account. Mode availability is account-level as well as plugin-level. Contact your PayU Key Account Manager (KAM) for enablement.
</Accordion>

<Accordion title="9. Which PayU plugin version should I download for my Magento version?" icon="fa-info-circle">
  Download the PayU plugin version that matches your Magento 2.x release from the instructions in [Install and Configure PayU Magento Plugin](doc:install-and-configure-magento-plugin). Installing an incorrect version can prevent the gateway from working.
</Accordion>

<Accordion title="10. How do I configure international payments or MCP on Magento?" icon="fa-info-circle">
  If international payments are enabled for your merchant account, configure currency and international payment settings in the PayU Magento plugin as documented in [Install and Configure PayU Magento Plugin](doc:install-and-configure-magento-plugin). Contact your PayU Key Account Manager (KAM) to confirm international payment enablement.
</Accordion>

<Accordion title="11. How do I verify Magento transactions using the Verify Payment API?" icon="fa-info-circle">
  After receiving the payment response, call the [Verify Payment API](ref:verify_payment_api) with the transaction ID to confirm status before fulfilling the order. PayU recommends this step for all plugin integrations to reconcile with PayU's database.
</Accordion>

<Accordion title="12. Why are payments not reflected in Magento after customers pay successfully?" icon="fa-info-circle">
  If Magento was in **Developer mode** during integration testing, payments may not reflect until you switch to **Production mode**. Clear Magento cache and recompile after mode or plugin changes. For more information, refer to [FAQs for Magento](doc:faqs-for-magento) and [Magento Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/set-mode.html).
</Accordion>

---

## OpenCart

<Accordion title="1. PayU checkout is not showing on my OpenCart store. What should I check?" icon="fa-info-circle">
  * Confirm the PayU plugin is installed and enabled in OpenCart admin.
  * Verify merchant key and Salt are configured correctly for the correct environment.
  * Ensure you are using a supported OpenCart version and the latest PayU OpenCart plugin.
  * Check that PayU appears as an enabled payment method in OpenCart payment settings.

  For more information, refer to [Install and Configure PayU OpenCart Plugin](doc:install-and-configure-opencart-plugin) and [FAQs for OpenCart](doc:faqs-for-opencart).
</Accordion>

<Accordion title="2. How do I verify OpenCart transactions after payment?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api) with the transaction ID from the payment response. Configure return URLs (success and failure) correctly in the OpenCart PayU plugin settings.
</Accordion>

<Accordion title="3. Do I need webhooks for OpenCart PayU integration?" icon="fa-info-circle">
  Webhooks are recommended for reliable asynchronous payment notifications in addition to browser redirects. Configure webhooks in PayU Dashboard and ensure your server can receive PayU callbacks. Refer to [Webhooks](doc:webhooks).
</Accordion>

<Accordion title="4. Which OpenCart versions does PayU support?" icon="fa-info-circle">
  Refer to the compatibility information in [Install and Configure PayU OpenCart Plugin](doc:install-and-configure-opencart-plugin). If the latest plugin is unavailable for your version, contact [PayU Support](https://help.payu.in) or your PayU Key Account Manager (KAM).
</Accordion>

<Accordion title="5. How do I get the latest PayU OpenCart plugin?" icon="fa-info-circle">
  Download the plugin from the source documented in [Install and Configure PayU OpenCart Plugin](doc:install-and-configure-opencart-plugin). If you cannot find a build for your OpenCart version, raise a support request with your OpenCart version details.
</Accordion>

---

## Wix

<Accordion title="1. Do I need to implement UPI Intent or NPCI OC190 on Wix with PayU hosted checkout?" icon="fa-info-circle">
  If you use PayU's standard hosted checkout through Wix, PayU handles applicable NPCI requirements on the hosted payment page. No separate UPI Intent implementation is required on the merchant side for hosted checkout. For more information, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted) and [FAQs for Wix](doc:faqs-for-wix).
</Accordion>

<Accordion title="2. Can I integrate the PayU Affordability Widget on Wix?" icon="fa-info-circle">
  Affordability widget integration on Wix may require custom implementation or PayU enablement. Contact your PayU Key Account Manager (KAM) for feasibility and setup guidance for your Wix store.
</Accordion>

<Accordion title="3. My PayU merchant account is dormant. Can I still integrate PayU on Wix?" icon="fa-info-circle">
  A dormant or inactive merchant account can block payment processing even when PayU is connected in Wix settings. Contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in) to reactivate your account before going live.
</Accordion>

<Accordion title="4. How do I implement UPI on my Wix store with PayU?" icon="fa-info-circle">
  Connect PayU India in **Wix Admin > Settings > Accept Payments** with your merchant key and Salt. UPI is available through PayU hosted checkout when enabled on your merchant account. If UPI does not appear, confirm account-level enablement with your PayU Key Account Manager (KAM). Refer to [Integrate with Wix](doc:integrate-with-wix).
</Accordion>

---

## BigCommerce

<Accordion title="1. Can PayU pass a No-Cost EMI or offer flag back to BigCommerce for order reconciliation?" icon="fa-info-circle">
  Passing offer or EMI metadata to BigCommerce order records depends on the integration capabilities of the PayU BigCommerce plugin and your offer configuration. Contact your PayU Key Account Manager (KAM) to confirm whether offer identifiers or flags can be mapped to BigCommerce order fields for your use case.
</Accordion>

<Accordion title="2. How do I map PayU transactions to BigCommerce order IDs in the PayU Dashboard?" icon="fa-info-circle">
  Store the PayU transaction ID alongside your BigCommerce order ID at payment callback. PayU Dashboard may not display the BigCommerce order ID by default. Use the [Verify Payment API](ref:verify_payment_api) and your platform order records for reconciliation. For bulk transaction fetch requirements, contact your PayU Key Account Manager (KAM).
</Accordion>

<Accordion title="3. Is PayU available in the BigCommerce App Marketplace for India?" icon="fa-info-circle">
  Yes. Install the **PayU** app from BigCommerce App Marketplace under **Payment & Security**, then link your PayU account. For step-by-step instructions, refer to [Install PayU Plugin for BigCommerce](doc:install-payu-plugin-for-bigcommerce).
</Accordion>

---

## Fynd

<Accordion title="1. What value does PayU return for payment_gateway_names on Fynd after order execution?" icon="fa-info-circle">
  Fynd reads payment gateway metadata from the PayU payment response when syncing order data. The exact value passed in `payment_gateway_names` depends on the PayU integration configuration and Fynd mapping. Share a sample PayU response payload with PayU integration support and your Fynd developer for field-level confirmation.
</Accordion>

<Accordion title="2. How do I enable PayU on Fynd WebView or ICP checkout?" icon="fa-info-circle">
  Configure and activate PayU India PG on your Fynd store from the Fynd Dashboard. For WebView or ICP-specific enablement, contact your PayU Key Account Manager (KAM) and refer to [Integrate with Fynd](doc:integrate-with-fynd).
</Accordion>

<Accordion title="3. What webhooks or callbacks does Fynd need from PayU?" icon="fa-info-circle">
  Configure PayU webhooks for payment success and failure events pointing to URLs required by your Fynd integration. Validate webhook payloads and handle duplicate events idempotently. Refer to [Webhooks](doc:webhooks) and [Integrate with Fynd](doc:integrate-with-fynd).
</Accordion>

---

## Odoo

<Accordion title="1. How do I enable EMI, BNPL, and international payments for Odoo sandbox testing?" icon="fa-info-circle">
  EMI, BNPL, and international payment modes must be enabled on your PayU test merchant account. Contact your PayU Key Account Manager (KAM) to activate these modes for your sandbox MID before testing on Odoo.
</Accordion>

<Accordion title="2. Which Odoo versions does the PayU plugin support?" icon="fa-info-circle">
  The PayU Odoo plugin is developed and tested on **Odoo 18**; version 18 or above is recommended. Enable **Developer mode** in Odoo before eCommerce and PayU module setup. Refer to [Install and Configure Odoo Plugin](doc:install-and-configure-odoo-plugin).
</Accordion>

<Accordion title="3. How do I verify Odoo payments and configure return URLs?" icon="fa-info-circle">
  After checkout, Odoo redirects customers to PayU and back to your store on success or failure. Verify transaction status using the [Verify Payment API](ref:verify_payment_api). Ensure success and failure return URLs in your Odoo PayU module match your store routes.
</Accordion>

---

## Zoho

<Accordion title="1. Why does the settlement export Product Info column show Zoho instead of my program name?" icon="fa-info-circle">
  PayU settlement exports may display the integration or product identifier configured for Zoho-originated transactions. If you require a specific program name in settlement reports, contact your PayU Key Account Manager (KAM) with your MID and the expected Product Info value for account-level configuration review.
</Accordion>

<Accordion title="2. PayU is not working on Zoho staging or test. What should I check?" icon="fa-info-circle">
  Confirm you are using **test merchant key and Salt** in the Zoho Configure Gateway dialog for staging, not production credentials. Verify the PayU test account is active. For production, use production key and Salt from [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
</Accordion>

---
