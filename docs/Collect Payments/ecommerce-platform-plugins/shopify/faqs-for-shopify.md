---
title: FAQs
deprecated: false
hidden: false
metadata:
  title: FAQs for Shopify
  robots: index
---
This section provides answers for frequently asked questions about integrating PayU with Shopify, including hosted checkout, onsite card payments, offers, CommercePro, and cross-border payments.

## General

<Accordion title="What PayU capabilities are available on Shopify?" icon="fa-info-circle">
  PayU supports hosted checkout (Cards, UPI, Net Banking via **Cards, UPI, NB by PayU India**), onsite card payments (**Onsite Card Payments by PayU India**), offers and affordability widgets, transaction reconciliation, SKU-based offers, CommercePro Checkout (OTP login and checkout), CommercePro COD with RTO intelligence, and cross-border payments for merchants outside India. For an overview, refer to [Shopify](doc:shopify).
</Accordion>

<Accordion title="Can I use multiple PayU apps on the same Shopify store?" icon="fa-info-circle">
  Yes, depending on your use case. For example, you can use hosted checkout for UPI and Net Banking alongside onsite card payments for a seamless card experience. Some features have specific app requirements—for example, offers work with hosted checkout, not the onsite card app. Review prerequisites on each guide before installing multiple apps.
</Accordion>

<Accordion title="Where do I get my merchant key and salt for Shopify?" icon="fa-info-circle">
  Generate production key and salt from PayU Dashboard. For testing, use test credentials. Refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) and [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="How do I test my Shopify integration before going live?" icon="fa-info-circle">
  Enable **Test mode** in the PayU app settings on Shopify and enter your test merchant key and salt. Complete a test transaction and verify it using the [Verify Payment API](ref:verify_payment_api). Refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="Who do I contact for Shopify enablement or configuration issues?" icon="fa-info-circle">
  Contact your PayU Key Account Manager (KAM) for enablement, offers widget embedding, SKU-based offer webhook setup, CommercePro COD enablement, and cross-border onboarding. For technical support, use [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="1. On Shopify, why are only card payment options showing while UPI, Net Banking, or wallets are missing?" icon="fa-info-circle">
  Check the following:

  1. Confirm that UPI, Net Banking, and wallets are enabled for your merchant account.
  2. Review the payment methods selected in **Shopify Admin > Settings > Payments > PayU**.
  3. Check whether the integration request restricts the checkout to cards.
  4. Save the configuration and test again in a new browser session.
     New merchant accounts can initially have a limited set of payment modes. Contact your PayU Key Account Manager (KAM) if a required mode is not enabled.
     For more information, refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

## Integrate with Shopify

<Accordion title="What are the two ways to integrate PayU on Shopify?" icon="fa-info-circle">
  You can install the PayU plugin from **Settings > Payments** in Shopify admin, or install the app from the Shopify App Store at [https://apps.shopify.com/payu-india](https://apps.shopify.com/payu-india). Both methods connect your store to PayU using your merchant key and salt. Refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="Should I remove an existing PayU plugin before reinstalling?" icon="fa-info-circle">
  Yes. If you previously installed a PayU plugin, remove it before installing again to avoid configuration conflicts. Refer to the prerequisites in [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="Which payment modes can I enable or disable in the PayU Shopify app?" icon="fa-info-circle">
  During configuration, you can select or clear check boxes for the payment modes and card types you want to support. Uncheck modes you do not wish to offer to customers.
</Accordion>

<Accordion title="How do I verify transactions after integrating PayU on Shopify?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api) or reconcile using Shopify and PayU transaction exports. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

## Enable Offers on your Shopify Page

<Accordion title="Which PayU Shopify app supports offers?" icon="fa-info-circle">
  Offers work with the hosted checkout app **Cards, UPI, NB by PayU India**. The onsite card app **Onsite Card Payments by PayU** does not support offers due to platform limitations.
</Accordion>

<Accordion title="How do I display the offers widget on my Shopify store?" icon="fa-info-circle">
  Create offers on PayU Dashboard, then contact the PayU Integration team to schedule embedding of the offers widget JavaScript on your checkout. The widget displays available offers; customers apply them on PayU Hosted Checkout. Refer to [Enable Offers on your Shopify Page](doc:enable-offers-on-your-shopify-page).
</Accordion>

<Accordion title="Why does Shopify not show the discounted order value after an offer is applied?" icon="fa-info-circle">
  Shopify does not include the discounted value in its order response. Integrate PayU APIs to fetch the payment response into your backend or CRM for accurate order values. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="Can I initiate refunds for offer transactions from Shopify?" icon="fa-info-circle">
  No. Refunds for transactions with offers must be initiated from PayU Dashboard. Refer to [Refunds for Offers](doc:refunds-for-offers).
</Accordion>

<Accordion title="Should I disable automatic order emailers when using offers?" icon="fa-info-circle">
  PayU recommends stopping automatic customer emailers after order placement because PayU can send them from the backend when offers are applied.
</Accordion>

## Reconcile Shopify Transactions

<Accordion title="How do I find the PayU transaction ID for a Shopify order?" icon="fa-info-circle">
  Export orders from Shopify admin and check the **Payment Reference** column in the CSV, or open individual order details in Shopify. You can also retrieve transaction details from PayU Dashboard or using PayU APIs. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="How do I reconcile Shopify orders with PayU transactions in bulk?" icon="fa-info-circle">
  Export orders from Shopify and transaction reports from PayU Dashboard, then map Shopify transaction IDs to the Merchant Ref ID in PayU using vLookup or similar tools in Excel. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="Which PayU APIs can I use for Shopify reconciliation?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api), [Get Transaction Info API](ref:get_transaction_info_api), or [Get Transaction Details API](ref:get_transaction_details_api).
</Accordion>

## Affordability Widget Integration for Shopify

<Accordion title="What is the PayU Affordability Widget on Shopify?" icon="fa-info-circle">
  The Affordability Widget shows customers eligible payment offers (for example EMI or discounts) on product or cart pages before checkout. It is added through Shopify theme Liquid templates, snippets, and sections.
</Accordion>

<Accordion title="Do I need to duplicate my Shopify theme before adding the widget?" icon="fa-info-circle">
  Duplicate your theme if you use a theme created in 2020 or later with `product.json`. Older themes without `product.json` can skip duplication and proceed to add the PayU snippet. Refer to [Affordability Widget Integration for Shopify](doc:affordability-widget-integration-for-shopify).
</Accordion>

<Accordion title="What is the difference between non-SKU-based and SKU-based affordability widget setup?" icon="fa-info-circle">
  Non-SKU-based setup uses merchant key and cart or product amount. SKU-based setup additionally passes `skusDetail` with SKU IDs, amounts, and quantities so offers tied to specific products display correctly. Create the corresponding offer type on PayU Dashboard before configuring the widget.
</Accordion>

<Accordion title="Where can I display the Affordability Widget on my store?" icon="fa-info-circle">
  You can show the widget on product pages and the cart page by updating `product.json`, `cart.json`, and the corresponding Liquid section files. Refer to [Affordability Widget Integration for Shopify](doc:affordability-widget-integration-for-shopify).
</Accordion>

## Install CommercePro Checkout App

<Accordion title="What is PayU CommercePro Checkout for Shopify?" icon="fa-info-circle">
  CommercePro Checkout is a Shopify app that connects your PayU account to your store for OTP-based customer login, checkout customisation, and related CommercePro features. Install it from [https://apps.shopify.com/payu-commercepro-checkout](https://apps.shopify.com/payu-commercepro-checkout). Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="How long does the CommercePro customer sync take?" icon="fa-info-circle">
  Customer sync duration depends on the total number of customers in your store. Check **Apps > PayU CommercePro Checkout > Dashboard** and confirm **Customer Sync Process** shows **Complete** before enabling the login widget.
</Accordion>

<Accordion title="What Shopify settings are required for the CommercePro login widget?" icon="fa-info-circle">
  Enable **Show login links** under **Online Store > Settings > Customer accounts** (Classic accounts), disable guest checkout (**Require customers to log in before checkout**), disable captcha on login and registration pages, and hide default Shopify login and registration sections in your theme. Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="How do I enable the CommercePro login widget from the theme editor?" icon="fa-info-circle">
  In **Online Store > Themes > Customize**, open **App embeds**, search for **Customer Login**, enable **Customer login – PayU**, and save. Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="Can I use Shopify's default COD or other payment gateways with CommercePro?" icon="fa-info-circle">
  Yes. Deactivate **PayU OTP Login** under **Settings > Payments > Payment method customization** to allow non-PayU payment modes, including Shopify Cash on Delivery, on checkout.
</Accordion>

## Enable Onsite Payments on Shopify

<Accordion title="What is onsite card payment on Shopify?" icon="fa-info-circle">
  Onsite card payments let customers pay with cards directly on the Shopify checkout page without redirecting to PayU Hosted Checkout, improving conversion and payment experience for card transactions.
</Accordion>

<Accordion title="Which payment methods does the onsite card app support?" icon="fa-info-circle">
  **Onsite Card Payments by PayU India** supports debit and credit cards. UPI, Net Banking, and other modes require the hosted checkout app **Cards, UPI, NB by PayU India**.
</Accordion>

<Accordion title="How do I enable test mode for onsite card payments?" icon="fa-info-circle">
  Deactivate the plugin if active, enable the **Test mode** toggle, select **Manage** from **More Actions**, and enter test merchant key and salt. Refer to [Enable Onsite Payments on Shopify](doc:enable-onsite-payments-on-shopify).
</Accordion>

<Accordion title="Do onsite card payments support offers?" icon="fa-info-circle">
  No. Offers are not supported on the onsite card app due to platform limitations. Use hosted checkout for offers. Refer to [Enable Offers on your Shopify Page](doc:enable-offers-on-your-shopify-page).
</Accordion>

<Accordion title="What should I do if I cannot activate the onsite card plugin?" icon="fa-info-circle">
  Ensure the plugin is installed from **Settings > Payments**, credentials are correct, and the plugin is activated. If issues persist, contact [PayU Support](https://help.payu.in).
</Accordion>

## Configure SKU-Based Offers

<Accordion title="What are SKU-based offers on Shopify?" icon="fa-info-circle">
  SKU-based offers apply only when specific products (identified by Shopify SKU IDs) are in the cart. Multiple SKU-based offers can apply when multiple qualifying products are present. Refer to [Configure SKU-Based Offers](doc:configure-sku-based-offers-shopify).
</Accordion>

<Accordion title="Which PayU app is required for SKU-based offers on Shopify?" icon="fa-info-circle">
  You must install the hosted checkout app **Cards, UPI, NB by PayU India**. Your PayU MID must be active.
</Accordion>

<Accordion title="How do I get SKU IDs from Shopify for offer configuration?" icon="fa-info-circle">
  Export products from **Products** in Shopify admin, download the export file, and use the SKU column values as **Product ID** when uploading offer details on PayU Dashboard. The Product ID in PayU must match the Shopify SKU.
</Accordion>

<Accordion title="Which Shopify webhooks are required for SKU-based offers?" icon="fa-info-circle">
  Create webhooks for **Checkout creation** and **Checkout update** events with JSON format, pointing to `https://partnerapilayer.payu.in/apilayer/shopify_app/shopifyWebhook`. Share your MID and the webhook signature hash from Shopify with PayU to enable SKU-based offers.
</Accordion>

<Accordion title="How do I reconcile SKU-based offer transactions?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api) or follow manual reconciliation steps in [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

## CommercePro COD App - Shopify

<Accordion title="What are the prerequisites for CommercePro COD on Shopify?" icon="fa-info-circle">
  Install PayU CommercePro Checkout app first. Contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in) to enable COD on CommercePro before installing the COD app from [https://apps.shopify.com/payu-cash-on-delivery](https://apps.shopify.com/payu-cash-on-delivery).
</Accordion>

<Accordion title="How does CommercePro COD reduce fraud and RTO?" icon="fa-info-circle">
  The app checks customer eligibility for COD before allowing the payment mode. RTO intelligence can blacklist or whitelist customers by PIN code, address, mobile number, email, cart amount limits, and AI-based risk signals.
</Accordion>

<Accordion title="Where do I configure COD amount limits and blacklists?" icon="fa-info-circle">
  On PayU Dashboard, go to **CommercePro > Configuration > RTO Settings** to set amount rules, blacklist users, and whitelist users manually or in bulk. Refer to [CommercePro COD App - Shopify](doc:commercepro-cod-app-shopify).
</Accordion>

<Accordion title="How do I mark a CommercePro COD order as paid in Shopify?" icon="fa-info-circle">
  In Shopify admin, open the COD order with **Payment pending** status, select **More actions > Open PayU Payment app**, choose **Mark as paid**, and click **Process**.
</Accordion>

<Accordion title="How do I cancel a CommercePro COD order?" icon="fa-info-circle">
  Open the order in Shopify admin, select **More actions > Open PayU Payment app**, choose **Cancel transaction**, and click **Process**.
</Accordion>

<Accordion title="Where can I view CommercePro COD orders?" icon="fa-info-circle">
  View orders on PayU Dashboard under **CommercePro > Orders**, or manage payment status from Shopify admin order details.
</Accordion>

## Cross-Border Payments on Shopify

<Accordion title="Can merchants outside India accept Indian payment methods on Shopify with PayU?" icon="fa-info-circle">
  Yes. Shopify merchants located outside India can offer UPI, Net Banking, and cards to Indian buyers and receive settlements in offshore accounts in foreign currency through PayU's cross-border stack. Contact your PayU Key Account Manager (KAM) or [crossborder@payu.in](mailto:crossborder@payu.in) to onboard.
</Accordion>

<Accordion title="Which PayU Shopify apps support cross-border payments?" icon="fa-info-circle">
  Use **Cards, UPI, NB by PayU India** (hosted) for Cards, UPI, Net Banking, and NEFT/RTGS, or **Onsite Card Payments by PayU India** for seamless card payments. Refer to [Cross-Border Payments on Shopify](doc:collect-cross-border-payments-on-shopify).
</Accordion>

<Accordion title="What APIs must I integrate for cross-border Shopify transactions?" icon="fa-info-circle">
  Implement the [UDF Update API](ref:udf_update_api) to pass **Invoice ID** (Var6, mandatory) and **Airway-Bill Number** (Var9, mandatory for physical goods). Refer to [Cross-Border Payments on Shopify](doc:collect-cross-border-payments-on-shopify).
</Accordion>

<Accordion title="How should I price products for Indian customers on Shopify?" icon="fa-info-circle">
  List catalogue SKUs in INR using [Shopify Markets](https://shopify.dev/docs/apps/build/markets) for India-specific pricing. Optionally limit PayU visibility to Indian customers using apps such as Localized Payments or HidePay.
</Accordion>

<Accordion title="How do I manage refunds for cross-border Shopify transactions?" icon="fa-info-circle">
  Full and partial refunds process through the PayU plugin and can also be managed from PayU merchant dashboard.
</Accordion>

<Accordion title="Where do I find settlement status, currency, and FX rate for cross-border transactions?" icon="fa-info-circle">
  Settlement information is available in the settlement tab on PayU merchant dashboard. APIs can be provided on request through your PayU Key Account Manager (KAM).
</Accordion>

<br />
