---
title: Troubleshooting Magento integration
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
When integrating PayU with Magento v2.4, you may sometimes encounter some issues. This section describes the recommended steps to troubleshoot any issues you face while integrating with Magento.

## PayU Plugin is not working

* Check whether you have downloaded the correct PayU plugin version from PayU GitHub and installed. For more information, refer to [Install Plugin for Magento v2.4](#install-plugin) based on the Magento version you are using.
* Check whether the merchant API key and Salt are configured accurately and navigate to [Merchant Dashboard](http://onboarding.payu.in/) and verify these values. For more information, refer to [Configure Magento v2.4](#configure-magento-v24). For more information on generating API key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

## Payments are not reflected

If you had switched to Magento **Developer** mode before starting the integration with the PayU plugin, you might not see the payments made by customers reflected if you did not switch to the Magento **Production** mode. For more information, refer to [Magento Configuration Guide](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/cli/set-mode.html).

## Magento upgrade issues

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
