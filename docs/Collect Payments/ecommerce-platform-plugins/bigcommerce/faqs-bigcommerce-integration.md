---
title: Troubleshooting BigCommerce Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---

<Accordion title="1. Which payment methods does PayU support on BigCommerce?" icon="fa-info-circle">
  PayU on BigCommerce supports cards (VISA, MasterCard, Diners, American Express), Net Banking, UPI, EMI, and wallets. Availability may depend on your merchant account configuration.
</Accordion>
<Accordion title="2. How does checkout work with PayU on BigCommerce?" icon="fa-info-circle">
  At checkout, customers are redirected to PayU to complete payment securely. After a successful payment, the order is confirmed and the customer is redirected back to your BigCommerce store.
</Accordion>
<Accordion title="3. What do I need before installing the PayU plugin on BigCommerce?" icon="fa-info-circle">
  You need a BigCommerce store account and your PayU Merchant Key and Salt. Register for a PayU merchant account before starting integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>
<Accordion title="4. Where can I find setup and troubleshooting help for BigCommerce?" icon="fa-info-circle">
  For installation steps, refer to [Install and Configure PayU BigCommerce Plugin](doc:install-payu-plugin-for-bigcommerce). If the plugin is not working, verify your API key and Salt configuration and refer to [Troubleshooting BigCommerce Integration](doc:troubleshooting-bigcommerce-integration).
</Accordion>
<Accordion title="5.My PayU Plugin is not working?" icon="fa-info-circle">
Check whether the merchant API key and Salt are configured accurately and navigate to [Merchant Dashboard](http://onboarding.payu.in/) and verify these values. For more information, refer to Step 8 of [Install PayU Plugin for BigCommerce](doc:install-payu-plugin-for-bigcommerce). For more information on generating API key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>