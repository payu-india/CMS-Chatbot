---
title: FAQs
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: FAQs for Zoho
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Zoho FAQs
    - PayU Zoho FAQs
    - Zoho integration FAQs
    - Zoho One PayU
    - Zoho Billing PayU
    - Zoho Inventory PayU
  robots: index
next:
  description: ''
---
This page answers frequently asked questions about integrating PayU with Zoho products, including Zoho One, Commerce, Invoice, Billing, and Inventory.

<Callout icon="📘" theme="info">
  **Reference**: For an overview, refer to [Zoho](doc:zoho-integration) and the linked guides in [Related documentation](#related-documentation).
</Callout>

## General

<Accordion title="1. Which Zoho products support PayU?" icon="fa-info-circle">
  PayU payment gateway can be set up for Zoho One, Zoho Commerce, Zoho Invoice, Zoho Billing, and Zoho Inventory. Setup steps differ by product. For an overview, refer to [Zoho](doc:zoho-integration).
</Accordion>

<Accordion title="2. How does PayU work with Zoho One and Zoho Books?" icon="fa-info-circle">
  With Zoho One, you can collect payments from customers, create invoices, and send them for payment. Invoicing is handled through Zoho Invoice functionality within the Zoho ecosystem. The documented integration path is to install the PayU app from Zoho Marketplace and configure the plugin for Zoho One. For more information, refer to [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one).
</Accordion>

<Accordion title="3. Do I need a PayU merchant account before integrating with Zoho?" icon="fa-info-circle">
  Yes. Register for a merchant account on PayU before starting integration. You need your PayU merchant key and Salt to configure PayU in Zoho. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>

<Accordion title="4. What credentials do I need to connect PayU to Zoho?" icon="fa-info-circle">
  You need your PayU **merchant key** and **Salt**. For production, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard). For test or UAT, refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="5. Which payment methods does PayU support on Zoho?" icon="fa-info-circle">
  PayU supports cards, Net Banking, UPI, EMI, and wallets on supported Zoho integrations. Availability depends on your merchant account configuration and the Zoho product you use. Contact your PayU Key Account Manager (KAM) if a required payment mode is not enabled.
</Accordion>

<Accordion title="6. How does the payment flow work when I send an invoice from Zoho?" icon="fa-info-circle">
  After you create and send an invoice from Zoho, your customer receives the invoice by email and can pay through PayU's secure payment page. Once payment is successful, the transaction is recorded against the invoice in Zoho.
</Accordion>

<Accordion title="7. Who do I contact for Zoho integration enablement or support?" icon="fa-info-circle">
  Contact your PayU Key Account Manager (KAM) for account enablement and payment-mode configuration. For technical issues during integration, use [PayU Support](https://help.payu.in).
</Accordion>

## Install from Zoho Marketplace

<Accordion title="1. How do I install the PayU app from Zoho Marketplace?" icon="fa-info-circle">
  1. Navigate to [Zoho Marketplace](https://marketplace.zoho.in/home) and log in using your Zoho Books credentials.
  2. Search for **PayU for Zoho Books** in the **Search apps** field and select it.
  3. Click **Install** on the top-right corner.

  For more information, refer to [Install PayU app on Zoho Marketplace](doc:install-payu-app-on-zoho-marketplace).
</Accordion>

<Accordion title="2. Why do I search for PayU for Zoho Books on Zoho Marketplace?" icon="fa-info-circle">
  The PayU extension listed on Zoho Marketplace is named **PayU for Zoho Books**. This is the app you install to enable PayU payment gateway integration for supported Zoho products such as Zoho One. For more information, refer to [Install PayU app on Zoho Marketplace](doc:install-payu-app-on-zoho-marketplace).
</Accordion>

<Accordion title="3. Which Zoho integrations require installing from Zoho Marketplace?" icon="fa-info-circle">
  Zoho One and Zoho Inventory integrations documented in the PayU Developer Guide start with installing the PayU app from Zoho Marketplace. Zoho Billing is configured directly from Zoho Billing settings after you have a PayU merchant account.
</Accordion>

## Zoho One

<Accordion title="1. How do I configure PayU for Zoho One?" icon="fa-info-circle">
  1. Log in to your Zoho One account.
  2. Click **Settings** on the top right and search for **Online Payments**.
  3. On the **Customer Payments** page, navigate to **PayU** under **Connected Payment Gateways**.
  4. Click **Setup now** under **PayU**.
  5. Enter your merchant **Key** and **Salt**, then click **Save**.

  For more information, refer to [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one).
</Accordion>

<Accordion title="2. How do I verify the PayU integration on Zoho One?" icon="fa-info-circle">
  1. Navigate to **Sales > Invoice** on Zoho One.
  2. Click **New** and enter the invoice details.
  3. Click **Save and Send**.
  4. On the email page, click **Send** to deliver the invoice to your customer and confirm that PayU payment collection works.

  For more information, refer to [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one).
</Accordion>

<Accordion title="3. Where do I enter my PayU key and Salt in Zoho One?" icon="fa-info-circle">
  In Zoho One, go to **Settings**, search for **Online Payments**, select **PayU** under **Connected Payment Gateways**, click **Setup now**, and enter your key and Salt in the **Configure Gateway** dialog. For more information, refer to [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one).
</Accordion>

## Zoho Commerce

<Accordion title="1. How do I set up PayU on Zoho Commerce?" icon="fa-info-circle">
  Set up PayU as your payment gateway on Zoho Commerce to collect payments when customers place orders on your online store. Configure PayU in your Zoho Commerce payment gateway settings using your PayU merchant key and Salt. Contact your PayU Key Account Manager (KAM) if PayU is not available as a payment option for your account.
</Accordion>

<Accordion title="2. What can I do with PayU on Zoho Commerce?" icon="fa-info-circle">
  Zoho Commerce lets you accept orders, track inventory, process payments, manage shipping, and analyze store data. With PayU configured as the payment gateway, customers can pay securely when they check out on your Zoho Commerce store.
</Accordion>

## Zoho Invoice

<Accordion title="1. Does Zoho Invoice support PayU?" icon="fa-info-circle">
  Zoho Invoice is an online invoicing product for freelancers and small businesses. PayU integration for invoice-based payment collection is documented through Zoho One, where invoicing uses Zoho Invoice functionality. For product details, refer to [Zoho Invoice on Zoho website](https://www.zoho.com/in/invoice/) and [Zoho](doc:zoho-integration).
</Accordion>

<Accordion title="2. Can I collect payments on invoices sent from Zoho Invoice using PayU?" icon="fa-info-circle">
  For Zoho One users, create and send invoices from **Sales > Invoice**, and customers pay through PayU when they receive the invoice. For standalone Zoho Invoice usage, confirm PayU availability in your Zoho Invoice payment gateway settings or contact your PayU Key Account Manager (KAM).
</Accordion>

## Zoho Billing

<Accordion title="1. How do I enable PayU for Zoho Billing?" icon="fa-info-circle">
  1. Log in to Zoho Billing.
  2. Click **Settings** on the toolbar.
  3. Under **Online Payments**, select **Payment Gateway**.
  4. Navigate to **PayU** and click **Set up Now**.
  5. Enter your merchant **Key** and **Salt**, then click **Save**.

  For more information, refer to [Enable PayU for Zoho Billing](doc:enable-payu-for-zoho-billing).
</Accordion>

<Accordion title="2. What types of billing does Zoho Billing support with PayU?" icon="fa-info-circle">
  Zoho Billing supports invoicing, expense management, project billing, recurring billing, automated invoice creation, custom branding, invoice consolidation, and multi-currency support. With PayU enabled as the payment gateway, customers can pay invoices and subscriptions through PayU's secure payment flow. For more information, refer to [Zoho](doc:zoho-integration) and [Enable PayU for Zoho Billing](doc:enable-payu-for-zoho-billing).
</Accordion>

<Accordion title="3. Where do I enter my PayU key and Salt in Zoho Billing?" icon="fa-info-circle">
  In Zoho Billing, go to **Settings > Online Payments > Payment Gateway**, select **PayU**, click **Set up Now**, and enter your key and Salt in the **Configure Gateway** pop-up. For more information, refer to [Enable PayU for Zoho Billing](doc:enable-payu-for-zoho-billing).
</Accordion>

## Zoho Inventory

<Accordion title="1. How do I enable PayU for Zoho Inventory?" icon="fa-info-circle">
  1. Log in to Zoho Inventory.
  2. Click **Settings** on the toolbar.
  3. Under **Online Payments**, select **Customer Payments**.
  4. Navigate to **PayU** and click **Set up Now**.
  5. Enter your merchant **Key** and **Salt**, then click **Save**.

  For more information, refer to [Enable PayU for Zoho Inventory](doc:enable-payu-for-zoho-inventory).
</Accordion>

<Accordion title="2. Why is Customer Payments used for PayU in Zoho Inventory?" icon="fa-info-circle">
  Zoho Inventory uses the **Customer Payments** section under **Online Payments** to configure payment gateways for collecting payments against sales orders and invoices. PayU is enabled from this section. For more information, refer to [Enable PayU for Zoho Inventory](doc:enable-payu-for-zoho-inventory).
</Accordion>

<Accordion title="3. What Zoho Inventory features work with PayU?" icon="fa-info-circle">
  Zoho Inventory supports stock tracking, multichannel selling, warehouse management, and customizable workflows. With PayU configured, you can collect online payments from customers as part of your inventory and order management workflows. For more information, refer to [Zoho](doc:zoho-integration).
</Accordion>

## Testing and verification

<Accordion title="1. How do I test my Zoho integration before going live?" icon="fa-info-circle">
  Use test merchant key and Salt from PayU Dashboard when configuring PayU in Zoho. Create a test invoice or order, send it to a test customer email, and complete a test payment using [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets). Verify the transaction in PayU Dashboard and in Zoho.
</Accordion>

<Accordion title="2. How do I verify transactions after integrating PayU with Zoho?" icon="fa-info-circle">
  PayU recommends verifying transaction details using the [Verify Payment API](ref:verify_payment_api) after you receive a payment response to reconcile with PayU's database.
</Accordion>

## Troubleshooting

<Accordion title="1. PayU is not appearing as a payment gateway in Zoho" icon="fa-info-circle">
  Confirm that you installed **PayU for Zoho Books** from [Zoho Marketplace](https://marketplace.zoho.in/home) and completed gateway setup in the correct Zoho product settings (**Online Payments** for Zoho One, **Payment Gateway** for Zoho Billing, or **Customer Payments** for Zoho Inventory). If PayU still does not appear, contact your PayU Key Account Manager (KAM) to confirm the integration is enabled for your merchant account.
</Accordion>

<Accordion title="2. PayU gateway setup fails after entering key and Salt" icon="fa-info-circle">
  Check the following:

  * Use the merchant key and Salt from the same environment (test or production).
  * Copy the Salt directly from PayU Dashboard; it is case-sensitive.
  * Log in to [PayU Merchant Dashboard](https://onboarding.payu.in/app/account) and confirm the values match what you entered in Zoho.

  For credential access, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) or [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="3. Customer payment link or invoice payment is not working" icon="fa-info-circle">
  Verify that PayU is set up under **Connected Payment Gateways** and that the invoice was saved and sent successfully. Test with a new invoice using test credentials. If the issue persists, verify the transaction using the [Verify Payment API](ref:verify_payment_api) and contact [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="4. I installed the app but cannot find Online Payments in Zoho One settings" icon="fa-info-circle">
  In Zoho One, click **Settings** on the top right and search for **Online Payments** in the settings search field. The **Customer Payments** page lists connected payment gateways including PayU. For more information, refer to [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one).
</Accordion>

## Related documentation

| Topic | Guide |
| --- | --- |
| Overview | [Zoho](doc:zoho-integration) |
| Install from Marketplace | [Install PayU app on Zoho Marketplace](doc:install-payu-app-on-zoho-marketplace) |
| Zoho One | [Configure PayU Plugin for Zoho One](doc:configure-payu-plugin-for-zoho-one) |
| Zoho Billing | [Enable PayU for Zoho Billing](doc:enable-payu-for-zoho-billing) |
| Zoho Inventory | [Enable PayU for Zoho Inventory](doc:enable-payu-for-zoho-inventory) |
