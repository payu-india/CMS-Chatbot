---
title: Ecommerce Plugin Payment Errors
excerpt: >-
  Go through the Ecommerce platform plugin troubleshooting issues and their
  recommended fixes.
deprecated: false
hidden: true
metadata:
  robots: index
---
These rows are categorized from existing PayU ecommerce plugin troubleshooting documentation.

<br />

Use this page with [Payment Failed or Declined](doc:payment-failed-declined)  for debugging guidance and retry handling.

<br />

## Error reference

<br />

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  rows={[
    ['`WooCommerce`', 'Payment Page is showing only card payment mode', 'Install the PayU WooCommerce v3.8.2 plugin and configure Currency 1, merchant key, salt, and Verify Payment as documented.'],
    ['`WooCommerce`', 'PayU is not appearing as a payment method or not working', 'Verify the merchant API key and salt in Merchant Dashboard, configure them in WooCommerce, and ensure PHP curl is installed and active.'],
    ['`WooCommerce`', 'Unable to process your request', 'Enter the Currency 1 value in capital letters, for example INR, and ensure it is not blank.'],
    ['`WooCommerce`', 'Incorrect return page is displayed after payment', 'Configure the Return Page field on the Payments tab in WooCommerce settings.'],
    ['`WooCommerce`', 'SI or Recurring Payments with WooCommerce', 'Use Web Checkout recurring payments because PayU does not support recurring payments with WooCommerce.'],
    ['`Wix`', 'PayU Plugin is not working', 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in Wix.'],
    ['`Shopmatic`', 'PayU Plugin is not working', 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in Shopmatic.'],
    ['`OpenCart`', 'PayU plugin is not working', 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in OpenCart.'],
    ['`Magento`', 'PayU Plugin is not working', 'Install the correct PayU plugin version, then verify merchant API key and salt in Merchant Dashboard and Magento configuration.'],
    ['`Magento`', 'Payments are not reflected', 'Switch Magento to Production mode before processing live payments.'],
    ['`Magento`', 'Magento upgrade issues', 'Clear and refresh Magento cache, run setup upgrade, deploy static content, and recompile Magento.'],
    ['`BigCommerce`', 'PayU Plugin is not working', 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in BigCommerce.'],
    ['`PrestaShop`', 'PayU is not appearing as a payment method or not working', 'Install the correct PayU plugin version, verify merchant ID and salt in Merchant Dashboard, and ensure PHP curl is installed and active.'],
  ]}
  placeholder="Search errors..."
/>
