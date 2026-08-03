---
title: FAQs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: FAQs for Magento integration
  description: ''
  robots: index
next:
  description: ''
---
---
title: FAQs for Magento
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Magento FAQs
    - PayU Magento FAQs
    - Magento integration FAQs
  robots: index
next:
  description: ''
---
This page includes the answers for frequently asked questions about integrating PayU with Magento, including setup, CommercePro, and troubleshooting.

<Callout icon="📘" theme="info">
  **Reference**: For integration steps, refer to [Magento](doc:magento) and [Install and Configure PayU Magento Plugin](doc:install-and-configure-magento-plugin).
</Callout>


<Accordion title="1. What PayU integrations are available for Magento?" icon="fa-info-circle">
  PayU offers the **PayU Magento Plugin** for standard payment collection and **CommercePro Checkout for Magento** for CommercePro features. For more information, refer to [Install and Configure PayU Magento Plugin](doc:install-and-configure-magento-plugin) and [CommercePro Checkout for Magento](doc:commercepro-platform-for-magento).
</Accordion>

<Accordion title="2. Which payment methods does PayU support on Magento?" icon="fa-info-circle">
  The PayU Magento plugin enables payments through credit cards, debit cards, Net Banking, and saved cards on Magento v2.x. Availability may depend on your merchant account configuration.
</Accordion>

<Accordion title="3. Do I need a PayU merchant account before integrating with Magento?" icon="fa-info-circle">
  Yes. Register for a merchant account on PayU before starting integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>

## Troubleshooting

<Accordion title="4. PayU Plugin is not working" icon="fa-info-circle">
  * Check whether you have downloaded the correct PayU plugin version from PayU GitHub and installed. For more information, refer to [Install Plugin for Magento v2.4](#install-plugin) based on the Magento version you are using.
  * Check whether the merchant API key and Salt are configured accurately and navigate to [Merchant Dashboard](http://onboarding.payu.in/) and verify these values. For more information, refer to [Configure Magento v2.4](#configure-magento-v24). For more information on generating API key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="5. Payments are not reflected" icon="fa-info-circle">
  If you had switched to Magento **Developer** mode before starting the integration with the PayU plugin, you might not see the payments made by customers reflected if you did not switch to the Magento **Production** mode. For more information, refer to [Magento Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/set-mode.html).
</Accordion>

<Accordion title="6. I am facing Magento upgrade issues" icon="fa-info-circle">
  After you upgrade from a previous version of Magento, you cannot see the new features of Magento.

  You need to clear the cache and refresh your Magento cache:

  1. Clear the Magento cache. For more information, refer to [Magento Documentation](https://devdocs.magento.com/guides/v2.2/howdoi/php/php_clear-dirs.html)
  2. Refresh the Magento cache by executing the following commands:

  ```plaintext
  php bin/magento setup:upgrade
  php bin/magento cache:flush
  php bin/magento setup:static-content:deploy
  ```

  3. Recompile the Magento installation using the following command:

  ```plaintext
  php bin/magento setup:di:compile
  ```

  > 📘 Note:
  >
  > For any other issues you face with Magento v2.4, refer to [Magento Troubleshooting](https://support.magento.com/hc/en-us/categories/115000200533-Troubleshooting).
</Accordion>
