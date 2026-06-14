---
title: 'WooCommerce PayU Plugin Integration Guide '
deprecated: false
hidden: true
metadata:
  robots: index
---
Introduction
Welcome to the comprehensive guide on integrating the PayU plugin with your WooCommerce store. This document is designed to reduce merchant integration time and empower you to set up PayU independently and efficiently.

WooCommerce is an open-source e-commerce plugin for WordPress. It is designed for small to large online merchants using WordPress to set up your e-commerce site easily.

Merchant will not require PCI-DSS certification on Merchant site.

Pre-requisites:-

• Merchant's End:
  oWordPress Access
  oWooCommerce version 3.x or later
  oPayU merchant account & dashboard access required.

• PayU's End:
  oEnsure that the necessary payment modes are enabled according to the merchant's    requirements.

oVerify that the MID is activated.

oEnsure that all MID configurations are correctly set up

Step-by-Step Installation Guide

1.Download the PayU Plugin:
 oVisit the WooCommerce plugin repository.   
 oSearch for "PayU WooCommerce Plugin" and download it.

2.Install the Plugin:
 oGo to your WordPress admin dashboard.

oNavigate to Plugins > Add New.

oClick Upload Plugin and select the downloaded file.

oClick Install Now and then Activate.

o 

3.Configure PayU Settings:

oNavigate to WooCommerce > Settings > Payments.

oFind PayU from the list and click Manage.

o 

oEnter your PayU Key and Salt.

o 

o 

oEnter the parameters for each currency if you had configured as multi-currency. You can configure upto 10 currencies. For example, to configure Indian Rupees as the first currency:

▪ Enter INR in the Currency 1 field.

▪ Enter your merchant key in the PayU Key for Currency 1 field. If you  had selected Sandbox in Step 8, enter your Test environment key as key.

▪ Enter your Salt in the PayU Salt for Currency 1 field. If you had selected  Sandbox in Step 8, enter your Test environment Salt as Salt.

oSave changes.

4.Testing the Integration:
 oPlace a test order through your WooCommerce store.

oCheck redirections.

oVerify the transaction status on WooCommerce and PayU Dashboard

Webhook Configuration Methods

1.Webhook Configuration via PayU Dashboard by Merchant-
 oAvailable Webhook URLs: The necessary webhook URLs are already available   on the WooCommerce admin panel as below.

o 

oInstructions to Copy and Configure:

▪ Merchants should copy the webhook URLs from the WooCommerce  admin panel.

▪ e steps provided in the   to configure these URLs on the PayU dashboard.

2.Webhook Configuration by PayU on MID Level-
 oIf merchants prefer, they can share the webhook URLs directly with us.

oWe will configure the webhooks at the MID level to ensure seamless integration.

Configuration and Setup

• General Settings:
  oEnsure currency settings align with your PayU account.   oConfigure email notifications for payment confirmations.

• Advanced Settings (Optional):
  oCustomize payment page appearance.

oSet transaction rules and limits.

Common Troubleshooting Tips

• Issue: Payment Page Not Loading
  oSolution: Verify that your SSL certificate is active and correctly installed.

• Issue: Transaction Fails with Error Code XYZ
  oSolution: Check if the Key and Salt are correctly entered and match those in your    PayU account.

Conclusion<br />By following these steps, you should have the PayU plugin successfully integrated with your<br />WooCommerce store. For additional help, refer to our support documentation or contact our<br />support team.<br />Appendix<br />• Links to additional resources<br />• FAQs-<br />1)Does SI or Recurring Payments supports with WooCommerce payu plugin?

&#x20; \=> No

2\)How to enable International Payment?<br />  => To enable international payments, contact your PayU key account manager (KAM).

<br />