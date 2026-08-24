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
These are Ecommerce platform plugin troubleshooting issues, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`WooCommerce`',
        'description': 'Payment Page is showing only card payment mode',
        'recommended_fix': 'Install the PayU WooCommerce v3.8.2 plugin and configure Currency 1, merchant key, salt, and Verify Payment as documented.'
      },
      {
        'bank_code': '`WooCommerce`',
        'description': 'PayU is not appearing as a payment method or not working',
        'recommended_fix': 'Verify the merchant API key and salt in Merchant Dashboard, configure them in WooCommerce, and ensure PHP curl is installed and active.'
      },
      {
        'bank_code': '`WooCommerce`',
        'description': 'Unable to process your request',
        'recommended_fix': 'Enter the Currency 1 value in capital letters, for example INR, and ensure it is not blank.'
      },
      {
        'bank_code': '`WooCommerce`',
        'description': 'Incorrect return page is displayed after payment',
        'recommended_fix': 'Configure the Return Page field on the Payments tab in WooCommerce settings.'
      },
      {
        'bank_code': '`WooCommerce`',
        'description': 'SI or Recurring Payments with WooCommerce',
        'recommended_fix': 'Use Web Checkout recurring payments because PayU does not support recurring payments with WooCommerce.'
      },
      {
        'bank_code': '`Wix`',
        'description': 'PayU Plugin is not working',
        'recommended_fix': 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in Wix.'
      },
      {
        'bank_code': '`Shopmatic`',
        'description': 'PayU Plugin is not working',
        'recommended_fix': 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in Shopmatic.'
      },
      {
        'bank_code': '`OpenCart`',
        'description': 'PayU plugin is not working',
        'recommended_fix': 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in OpenCart.'
      },
      {
        'bank_code': '`Magento`',
        'description': 'PayU Plugin is not working',
        'recommended_fix': 'Install the correct PayU plugin version, then verify merchant API key and salt in Merchant Dashboard and Magento configuration.'
      },
      {
        'bank_code': '`Magento`',
        'description': 'Payments are not reflected',
        'recommended_fix': 'Switch Magento to Production mode before processing live payments.'
      },
      {
        'bank_code': '`Magento`',
        'description': 'Magento upgrade issues',
        'recommended_fix': 'Clear and refresh Magento cache, run setup upgrade, deploy static content, and recompile Magento.'
      },
      {
        'bank_code': '`BigCommerce`',
        'description': 'PayU Plugin is not working',
        'recommended_fix': 'Verify the merchant API key and salt in Merchant Dashboard and configure them correctly in BigCommerce.'
      },
      {
        'bank_code': '`PrestaShop`',
        'description': 'PayU is not appearing as a payment method or not working',
        'recommended_fix': 'Install the correct PayU plugin version, verify merchant ID and salt in Merchant Dashboard, and ensure PHP curl is installed and active.'
      }
    ]}
  />
</Accordion>