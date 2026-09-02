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

<Accordion title="1. What PayU capabilities are available on Shopify?" icon="fa-info-circle">
  PayU supports hosted checkout (Cards, UPI, Net Banking via **Cards, UPI, NB by PayU India**), onsite card payments (**Onsite Card Payments by PayU India**), offers and affordability widgets, transaction reconciliation, SKU-based offers, CommercePro Checkout (OTP login and checkout), CommercePro COD with RTO intelligence, and cross-border payments for merchants outside India. For an overview, refer to [Shopify](doc:shopify).
</Accordion>

<Accordion title="2. Can I use multiple PayU apps on the same Shopify store?" icon="fa-info-circle">
  Yes, depending on your use case. For example, you can use hosted checkout for UPI and Net Banking alongside onsite card payments for a seamless card experience. Some features have specific app requirements—for example, offers work with hosted checkout, not the onsite card app. Review prerequisites on each guide before installing multiple apps.
</Accordion>

<Accordion title="3. Where do I get my merchant key and salt for Shopify?" icon="fa-info-circle">
  Generate production key and salt from PayU Dashboard. For testing, use test credentials. Refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) and [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="4. How do I test my Shopify integration before going live?" icon="fa-info-circle">
  Enable **Test mode** in the PayU app settings on Shopify and enter your test merchant key and salt. Complete a test transaction and verify it using the [Verify Payment API](ref:verify_payment_api). Refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="5. Who do I contact for Shopify enablement or configuration issues?" icon="fa-info-circle">
  Contact your PayU Key Account Manager (KAM) for enablement, offers widget embedding, SKU-based offer webhook setup, CommercePro COD enablement, and cross-border onboarding. For technical support, use [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="6. On Shopify, why are only card payment options showing while UPI, Net Banking, or wallets are missing?" icon="fa-info-circle">
  Check the following:

  1. Confirm that UPI, Net Banking, and wallets are enabled for your merchant account.
  2. Review the payment methods selected in **Shopify Admin > Settings > Payments > PayU**.
  3. Check whether the integration request restricts the checkout to cards.
  4. Save the configuration and test again in a new browser session.
     New merchant accounts can initially have a limited set of payment modes. Contact your PayU Key Account Manager (KAM) if a required mode is not enabled.
     For more information, refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

## Integrate with Shopify

<Accordion title="1. What are the two ways to integrate PayU on Shopify?" icon="fa-info-circle">
  You can install the PayU plugin from **Settings > Payments** in Shopify admin, or install the app from the Shopify App Store at [https://apps.shopify.com/payu-india](https://apps.shopify.com/payu-india). Both methods connect your store to PayU using your merchant key and salt. Refer to [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="2. Should I remove an existing PayU plugin before reinstalling?" icon="fa-info-circle">
  Yes. If you previously installed a PayU plugin, remove it before installing again to avoid configuration conflicts. Refer to the prerequisites in [Integrate with Shopify](doc:integrate-with-shopify).
</Accordion>

<Accordion title="3. Which payment modes can I enable or disable in the PayU Shopify app?" icon="fa-info-circle">
  During configuration, you can select or clear check boxes for the payment modes and card types you want to support. Uncheck modes you do not wish to offer to customers.
</Accordion>

<Accordion title="4. How do configure webhooks on Shopify?" icon="fa-info-circle">
  1. Log in to your **Shopify Admin Panel**
  2. Navigate to **Settings > Notifications**
  3. Scroll down to the **Webhooks** section.
  4. Click **Create webhook.**

     ![](https://files.readme.io/8439756b511c546d96fc469847ecb9c69cead366b0185221769fecc3b48d5070-image_20260902053926_u2l.png)



  5. Configure the webhook with the following details:
     * **Event**: Select `Order updated`
     * **Format**: JSON
     * **URL**: `https://info.payu.in/merchant/shopify/webhook/refund`
     * **API Version**: Use the latest available version

  6. Click **Save webhook**
</Accordion>

<Accordion title="5. How do I verify transactions after integrating PayU on Shopify?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api) or reconcile using Shopify and PayU transaction exports. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

## Refunds for Transactions on Shopify

<Accordion title="1. How to initiate refund for transactions made on Shopify?" icon="fa-info-circle">
  ### Method 1: Refund from Shopify Dashboard

  Shopify can automatically notify PayU when you process a refund directly from the Shopify admin panel.

  1. Log in to your **Shopify Admin Panel**
  2. Navigate to **Orders**
  3. Right-click the order you want to refund and select **Cancel orders**.

     <Image src="https://files.readme.io/5b19f52eb28f350798e573f5803395ced9d81375d3469921258d6f2039bfddd6-shopify_cancel_order.png" framed={true} />

     The Cancel order \\<order number> pop-up page is displayed.

     ![](https://files.readme.io/3bc0b033ef59916d9efae4a39bdbe04de39f3d92d49003d5cec6921a496facfb-shopify_cancel_order_dialog_order.png)



  4. Select the required option in the **Refund payments** field based on refund.
  5. Select the reason for cancelling the transaction from the **Reason for cancellation&#x20;**&#x66;ield.
  6. Enter the reason for cancelling the order in the **Staff note** field.
  7. Enter the refund amount and select the items (for partial refunds).
  8. Click **Cancel order** to process.

  If webhooks are configured correctly, PayU will receive the refund notification and process it automatically. For more information, refer to [Webhooks for Refunds.](doc:webhooks-for-refunds)

  ### Method 2: Refund from PayU Dashboard

  You can also initiate refunds directly from the PayU Dashboard for Shopify transactions.

  1. Log in to the **PayU Merchant Dashboard**
  2. Navigate to **Track > Transactions**
  3. Use the search function to find the transaction using:
     - PayU Transaction ID
     - Shopify Order ID (if mapped correctly)
     - Customer email or phone number

  4. Click the transaction ID to view transaction details

  The transaction details page is displayed.


  <Image src="https://files.readme.io/87507999bbaea97706db60af650cc61e1e072ec46c2dbd47d0efcc0fc9b0bd60-Dashboard_Transaction_Details_Page_Issue_Refund.png" framed={true} />




  5. Click **Issue Refund** at the top-right corner

  The _Refund Payment_ pop-up is displayed.


  <Image src="https://files.readme.io/e7d438d8ff968456d49419f4f6a5e3f7c4d418d2cabba56f04d81f2702f91b12-Dashboard_Transaction_Refund_Dialog.png" align="center" width="350px" framed={true} />




  6. Enter the amount to be refunded in the **Refund Amount** field
  7. Add an optional note describing the reason for refund in th&#x65;**&#x20;Enter remark f**ield.
  8. Click **Send Full Refund** for full amount or **Send Partial Refund** for partial amount
</Accordion>

<Accordion title="2. How long does it take for automated refunds to process?" icon="fa-info-circle">
  Once the automated refund is triggered, it typically takes 5-7 working days for the refund amount to reflect in the customer's bank account. The timeline may vary based on the payment method:

  * **Credit Cards**: 5-7 working days
  * **Debit Cards**: 7-10 working days
  * **Net Banking**: 5-7 working days
  * **UPI**: 3-5 working days
  * **Wallets**: Instant to 24 hours
</Accordion>

<Accordion title="3. Can I configure different refund rules for different order tags?" icon="fa-info-circle">
  Yes, you can create multiple automated refund rules, each triggered by different Shopify order tags. For example:

  * Tag "Defective-Product" → Full refund
  * Tag "Partial-Return" → Partial refund based on items returned
  * Tag "Customer-Cancelled" → Full refund minus processing fee
</Accordion>

<Accordion title="4. What happens if a customer disputes after an automated refund?" icon="fa-info-circle">
  If a chargeback or dispute is raised after an automated refund has been processed:

  1. Contact PayU support immediately.
  2. Provide evidence of the refund, including the transaction ID and refund ARN.
  3. PayU will coordinate with the bank to resolve the dispute.
  4. Duplicate refunds will be recovered from the customer's bank account.
</Accordion>

<Accordion title="5. Can I set refund limits for automated rules?" icon="fa-info-circle">
  Yes, you can configure maximum refund amounts per rule to prevent accidental large refunds:

  1. Edit your automated refund rule.
  2. Set the **Maximum Refund Amount** field.
  3. Refunds exceeding this amount will require manual approval.
</Accordion>

<Accordion title="6. How do I handle partial refunds for specific line items?" icon="fa-info-circle">
  For partial refunds based on specific items returned:

  1. Configure your Shopify refund to specify which items are being refunded.
  2. The webhook will include line item details.
  3. PayU will calculate the refund amount based on the refunded items.
  4. Ensure your automated rule is set to **Partial Refund** mode.
</Accordion>

<Accordion title="7. Can I use automated refunds with Shopify subscriptions?" icon="fa-info-circle">
  Yes, automated refunds work with Shopify subscription orders. However:

  * Ensure each subscription charge has a unique transaction ID.
  * Configure rules to handle recurring and one-time charges differently.
  * Consider setting up separate rules for subscription cancellations.
</Accordion>

<Accordion title="8. What are the transaction mapping options?" icon="fa-info-circle">
  You can map Shopify orders to PayU transactions using:

  * `txnid` parameter (recommended): Pass the Shopify order ID as the transaction ID.
  * `udf1` to `udf5` fields: Store the Shopify order ID in user-defined fields.
  * Order reference number: Use the Shopify order name, such as `#1001`.
</Accordion>

<Accordion title="9. Do automated refunds work for cross-border payments?" icon="fa-info-circle">
  Yes, automated refunds are supported for cross-border payments made through PayU. However:

  * Currency conversion rates at the time of the refund apply.
  * Processing times may be longer, typically 7-14 working days.
  * Additional documentation may be required for certain countries.
</Accordion>

## Enable Offers on your Shopify Page

<Accordion title="1. Which PayU Shopify app supports offers?" icon="fa-info-circle">
  Offers work with the hosted checkout app **Cards, UPI, NB by PayU India**. The onsite card app **Onsite Card Payments by PayU** does not support offers due to platform limitations.
</Accordion>

<Accordion title="2. How do I display the offers widget on my Shopify store?" icon="fa-info-circle">
  Create offers on PayU Dashboard, then contact the PayU Integration team to schedule embedding of the offers widget JavaScript on your checkout. The widget displays available offers; customers apply them on PayU Hosted Checkout. Refer to [Enable Offers on your Shopify Page](doc:enable-offers-on-your-shopify-page).
</Accordion>

<Accordion title="3. Why does Shopify not show the discounted order value after an offer is applied?" icon="fa-info-circle">
  Shopify does not include the discounted value in its order response. Integrate PayU APIs to fetch the payment response into your backend or CRM for accurate order values. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="4. Can I initiate refunds for offer transactions from Shopify?" icon="fa-info-circle">
  No. Refunds for transactions with offers must be initiated from PayU Dashboard. Refer to [Refunds for Offers](doc:refunds-for-offers).
</Accordion>

<Accordion title="5. Should I disable automatic order emailers when using offers?" icon="fa-info-circle">
  PayU recommends stopping automatic customer emailers after order placement because PayU can send them from the backend when offers are applied.
</Accordion>

## Reconcile Shopify Transactions

<Accordion title="1. How do I find the PayU transaction ID for a Shopify order?" icon="fa-info-circle">
  Export orders from Shopify admin and check the **Payment Reference** column in the CSV, or open individual order details in Shopify. You can also retrieve transaction details from PayU Dashboard or using PayU APIs. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="2. How do I reconcile Shopify orders with PayU transactions in bulk?" icon="fa-info-circle">
  Export orders from Shopify and transaction reports from PayU Dashboard, then map Shopify transaction IDs to the Merchant Ref ID in PayU using vLookup or similar tools in Excel. Refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

<Accordion title="3. Which PayU APIs can I use for Shopify reconciliation?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api), [Get Transaction Info API](ref:get_transaction_info_api), or [Get Transaction Details API](ref:get_transaction_details_api).
</Accordion>

## Affordability Widget Integration for Shopify

<Accordion title="1. What is the PayU Affordability Widget on Shopify?" icon="fa-info-circle">
  The Affordability Widget shows customers eligible payment offers (for example EMI or discounts) on product or cart pages before checkout. It is added through Shopify theme Liquid templates, snippets, and sections.
</Accordion>

<Accordion title="2. Do I need to duplicate my Shopify theme before adding the widget?" icon="fa-info-circle">
  Duplicate your theme if you use a theme created in 2020 or later with `product.json`. Older themes without `product.json` can skip duplication and proceed to add the PayU snippet. Refer to [Affordability Widget Integration for Shopify](doc:affordability-widget-integration-for-shopify).
</Accordion>

<Accordion title="3. What is the difference between non-SKU-based and SKU-based affordability widget setup?" icon="fa-info-circle">
  Non-SKU-based setup uses merchant key and cart or product amount. SKU-based setup additionally passes `skusDetail` with SKU IDs, amounts, and quantities so offers tied to specific products display correctly. Create the corresponding offer type on PayU Dashboard before configuring the widget.
</Accordion>

<Accordion title="4. Where can I display the Affordability Widget on my store?" icon="fa-info-circle">
  You can show the widget on product pages and the cart page by updating `product.json`, `cart.json`, and the corresponding Liquid section files. Refer to [Affordability Widget Integration for Shopify](doc:affordability-widget-integration-for-shopify).
</Accordion>

## Install CommercePro Checkout App

<Accordion title="1. What is PayU CommercePro Checkout for Shopify?" icon="fa-info-circle">
  CommercePro Checkout is a Shopify app that connects your PayU account to your store for OTP-based customer login, checkout customisation, and related CommercePro features. Install it from [https://apps.shopify.com/payu-commercepro-checkout](https://apps.shopify.com/payu-commercepro-checkout). Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="2. How long does the CommercePro customer sync take?" icon="fa-info-circle">
  Customer sync duration depends on the total number of customers in your store. Check **Apps > PayU CommercePro Checkout > Dashboard** and confirm **Customer Sync Process** shows **Complete** before enabling the login widget.
</Accordion>

<Accordion title="3. What Shopify settings are required for the CommercePro login widget?" icon="fa-info-circle">
  Enable **Show login links** under **Online Store > Settings > Customer accounts** (Classic accounts), disable guest checkout (**Require customers to log in before checkout**), disable captcha on login and registration pages, and hide default Shopify login and registration sections in your theme. Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="4. How do I enable the CommercePro login widget from the theme editor?" icon="fa-info-circle">
  In **Online Store > Themes > Customize**, open **App embeds**, search for **Customer Login**, enable **Customer login – PayU**, and save. Refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
</Accordion>

<Accordion title="5. Can I use Shopify's default COD or other payment gateways with CommercePro?" icon="fa-info-circle">
  Yes. Deactivate **PayU OTP Login** under **Settings > Payments > Payment method customization** to allow non-PayU payment modes, including Shopify Cash on Delivery, on checkout.
</Accordion>

## Enable Onsite Payments on Shopify

<Accordion title="1. What is onsite card payment on Shopify?" icon="fa-info-circle">
  Onsite card payments let customers pay with cards directly on the Shopify checkout page without redirecting to PayU Hosted Checkout, improving conversion and payment experience for card transactions.
</Accordion>

<Accordion title="2. Which payment methods does the onsite card app support?" icon="fa-info-circle">
  **Onsite Card Payments by PayU India** supports debit and credit cards. UPI, Net Banking, and other modes require the hosted checkout app **Cards, UPI, NB by PayU India**.
</Accordion>

<Accordion title="3. How do I enable test mode for onsite card payments?" icon="fa-info-circle">
  Deactivate the plugin if active, enable the **Test mode** toggle, select **Manage** from **More Actions**, and enter test merchant key and salt. Refer to [Enable Onsite Payments on Shopify](doc:enable-onsite-payments-on-shopify).
</Accordion>

<Accordion title="4. Do onsite card payments support offers?" icon="fa-info-circle">
  No. Offers are not supported on the onsite card app due to platform limitations. Use hosted checkout for offers. Refer to [Enable Offers on your Shopify Page](doc:enable-offers-on-your-shopify-page).
</Accordion>

<Accordion title="5. What should I do if I cannot activate the onsite card plugin?" icon="fa-info-circle">
  Ensure the plugin is installed from **Settings > Payments**, credentials are correct, and the plugin is activated. If issues persist, contact [PayU Support](https://help.payu.in).
</Accordion>

## Configure SKU-Based Offers

<Accordion title="1. What are SKU-based offers on Shopify?" icon="fa-info-circle">
  SKU-based offers apply only when specific products (identified by Shopify SKU IDs) are in the cart. Multiple SKU-based offers can apply when multiple qualifying products are present. Refer to [Configure SKU-Based Offers](doc:configure-sku-based-offers-shopify).
</Accordion>

<Accordion title="2. Which PayU app is required for SKU-based offers on Shopify?" icon="fa-info-circle">
  You must install the hosted checkout app **Cards, UPI, NB by PayU India**. Your PayU MID must be active.
</Accordion>

<Accordion title="3. How do I get SKU IDs from Shopify for offer configuration?" icon="fa-info-circle">
  Export products from **Products** in Shopify admin, download the export file, and use the SKU column values as **Product ID** when uploading offer details on PayU Dashboard. The Product ID in PayU must match the Shopify SKU.
</Accordion>

<Accordion title="4. Which Shopify webhooks are required for SKU-based offers?" icon="fa-info-circle">
  Create webhooks for **Checkout creation** and **Checkout update** events with JSON format, pointing to `https://partnerapilayer.payu.in/apilayer/shopify_app/shopifyWebhook`. Share your MID and the webhook signature hash from Shopify with PayU to enable SKU-based offers.
</Accordion>

<Accordion title="5. How do I reconcile SKU-based offer transactions?" icon="fa-info-circle">
  Use the [Verify Payment API](ref:verify_payment_api) or follow manual reconciliation steps in [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
</Accordion>

## CommercePro COD App - Shopify

<Accordion title="1. What are the prerequisites for CommercePro COD on Shopify?" icon="fa-info-circle">
  Install PayU CommercePro Checkout app first. Contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in) to enable COD on CommercePro before installing the COD app from [https://apps.shopify.com/payu-cash-on-delivery](https://apps.shopify.com/payu-cash-on-delivery).
</Accordion>

<Accordion title="2. How does CommercePro COD reduce fraud and RTO?" icon="fa-info-circle">
  The app checks customer eligibility for COD before allowing the payment mode. RTO intelligence can blacklist or whitelist customers by PIN code, address, mobile number, email, cart amount limits, and AI-based risk signals.
</Accordion>

<Accordion title="3. Where do I configure COD amount limits and blacklists?" icon="fa-info-circle">
  On PayU Dashboard, go to **CommercePro > Configuration > RTO Settings** to set amount rules, blacklist users, and whitelist users manually or in bulk. Refer to [CommercePro COD App - Shopify](doc:commercepro-cod-app-shopify).
</Accordion>

<Accordion title="4. How do I mark a CommercePro COD order as paid in Shopify?" icon="fa-info-circle">
  In Shopify admin, open the COD order with **Payment pending** status, select **More actions > Open PayU Payment app**, choose **Mark as paid**, and click **Process**.
</Accordion>

<Accordion title="5. How do I cancel a CommercePro COD order?" icon="fa-info-circle">
  Open the order in Shopify admin, select **More actions > Open PayU Payment app**, choose **Cancel transaction**, and click **Process**.
</Accordion>

<Accordion title="6. Where can I view CommercePro COD orders?" icon="fa-info-circle">
  View orders on PayU Dashboard under **CommercePro > Orders**, or manage payment status from Shopify admin order details.
</Accordion>

## Cross-Border Payments on Shopify

<Accordion title="1. Can merchants outside India accept Indian payment methods on Shopify with PayU?" icon="fa-info-circle">
  Yes. Shopify merchants located outside India can offer UPI, Net Banking, and cards to Indian buyers and receive settlements in offshore accounts in foreign currency through PayU's cross-border stack. Contact your PayU Key Account Manager (KAM) or [crossborder@payu.in](mailto:crossborder@payu.in) to onboard.
</Accordion>

<Accordion title="2. Which PayU Shopify apps support cross-border payments?" icon="fa-info-circle">
  Use **Cards, UPI, NB by PayU India** (hosted) for Cards, UPI, Net Banking, and NEFT/RTGS, or **Onsite Card Payments by PayU India** for seamless card payments. Refer to [Cross-Border Payments on Shopify](doc:collect-cross-border-payments-on-shopify).
</Accordion>

<Accordion title="3. What APIs must I integrate for cross-border Shopify transactions?" icon="fa-info-circle">
  Implement the [UDF Update API](ref:udf_update_api) to pass **Invoice ID** (Var6, mandatory) and **Airway-Bill Number** (Var9, mandatory for physical goods). Refer to [Cross-Border Payments on Shopify](doc:collect-cross-border-payments-on-shopify).
</Accordion>

<Accordion title="4. How should I price products for Indian customers on Shopify?" icon="fa-info-circle">
  List catalogue SKUs in INR using [Shopify Markets](https://shopify.dev/docs/apps/build/markets) for India-specific pricing. Optionally limit PayU visibility to Indian customers using apps such as Localized Payments or HidePay.
</Accordion>

<Accordion title="5. How do I manage refunds for cross-border Shopify transactions?" icon="fa-info-circle">
  Full and partial refunds process through the PayU plugin and can also be managed from PayU merchant dashboard.
</Accordion>

<Accordion title="6. Where do I find settlement status, currency, and FX rate for cross-border transactions?" icon="fa-info-circle">
  Settlement information is available in the settlement tab on PayU merchant dashboard. APIs can be provided on request through your PayU Key Account Manager (KAM).
</Accordion>
