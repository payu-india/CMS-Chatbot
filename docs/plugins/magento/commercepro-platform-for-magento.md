---
title: CommercePro Checkout for Magento
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
This section describes how to install and configure PayU plugin for Magento on CommercePro Checkout. For overview of CommercePro Checkout and customer journey with PayU Plugin, refer to [CommercePro Checkout](doc:commercepro-checkout).

## Prerequisites

- Merchant must be active on PayU.
- Merchant’s website must be on hosted on Magento v2.4.x
- The merchant should be on One PayU platform.

## Installation

To install the PayU plugin for Magento on CommercePro:

1. After the plugin archive is downloaded in the **ZIP** format, extract it to get the integration folder.
2. Copy the integration folder to the desired location on your system. 

> **Note**: Ensure that you have sufficient permission to access and modify files within this folder. 

3. Paste the folder under `<root_directory>/app/code`. 
4. Execute the following commands:

```
php bin/magento s:up  
php bin/magento s:di:c  
php bin/magento setup:static-content:deploy -f 
php bin/magento c:f 
chmod -R 777 generated/ pub/static/* var/cache/* 
```

## Configuration

After installing PayU plugin for Magento v2.4, you need to configure the Magento installation as described in this section. 

To configure the Magento v2.4 environment for PayU:

1. Log in to the Magento admin panel.
2. Navigate to **Store** > **Configuration** > **Sales** > **Payment Methods**.
3. Expand the **PayU** menu.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ebb0180-commercepro_magento_payu_config.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Enter the configuration details as described in the table:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Enable",
    "0-1": "Select **Yes** from the drop-down list to enable the plugin.",
    "1-0": "Payment Type",
    "1-1": "Select **Express Checkout** from the drop-down list.",
    "2-0": "Enable Webhook",
    "2-1": " Select **Yes** from the drop-down to notify when specific events occurred such as Payment Success, Payment Failed to merchant by PayU.",
    "3-0": "Payment Action",
    "3-1": "Select any of the following:  \n  \n- **Authorize Only** : PayU will authorize payment only.\n- **Authorize and capture**: PayU will authorize and capture the status of transaction.",
    "4-0": "Account Type",
    "4-1": "Select **PayUBiz** from the drop-down list for the account type.",
    "5-0": "Environment",
    "5-1": "Select any of the following gateway environments from the drop-down list:  \n  \n- **Sandbox:**: This is the Test environment, and no actual fund transfer will take place.\n\n- **Production:**: This is the Live environment.  \n    **Note**: If you select **Sandbox**, use the following credentials:  \n  **Merchant ID**: oZ7oo9  \n  **Salt**: UkojH5TS.",
    "6-0": "Merchant Key",
    "6-1": "Enter your PayU account key for the Production environment.",
    "7-0": "Salt Key Password",
    "7-1": "Enter your Salt for the Production environment. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).",
    "8-0": "Enable Payment Verification ",
    "8-1": "Select **Yes** from the drop-down list. This will allow plugin to confirm status of transaction and reconcile with PayU APIs"
  },
  "cols": 2,
  "rows": 9,
  "align": [
    null,
    null
  ]
}
[/block]


5. Click** Save Config** at the top-right corner to save the changes.
6. Run this command: 

```
php bin/magento c:f
```