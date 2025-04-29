---
title: CommercePro Checkout for WooCommerce
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
This section describes how to install and configure PayU plugin for WooCommerce on CommercePro Checkout. For overview of CommercePro Checkout and customer journey with PayU Plugin, refer to [CommercePro Checkout](doc:commercepro-checkout).

## Prerequisites

- Merchant must be active on PayU.
- Merchant’s website must be on hosted on WooCommerce v3.4
- The merchant should be on One PayU platform.

## Plugin location

The plugin can be downloaded from the following Github location:

| WooCommerce Version | PayU CommercePro Checkout Download Location                                                      |
| :------------------ | :----------------------------------------------------------------------------------------------- |
| v3.4                | [Github](https://github.com/payu-india/Woocommerce/blob/main/WooCommerce_CommercePro_plugin.zip) |

## Installation

To install the PayU plugin for WooCommerce on CommercePro:

1. After the plugin archive is downloaded in the **ZIP** format, extract to get the integration folder. For the plugin location, refer to in the [Plugin location](plugin-location) sub-section.
2. Log in to WooCommerce Dashboard.
3. Select **Plugin** from the menu on the left pane.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ef2e668-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Click **Add New Plugin** at the top.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c19eca9-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


5. Click **Upload Plugin** at the top.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c139a3b-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


6. Click **Choose File** and select the PayU plugin from your system.

![](https://files.readme.io/cd2012a-image.png)

7. Click **Install Now**.

![](https://files.readme.io/18c8d7e-image.png)

8. Scroll down to **PayU India **plugin and select **Activate** under it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9f30dbc-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


### Configuration

To configure the WooCommerce environment for PayU:

1. Select **WooCommerce** > **Settings** from the menu on the left pane.

![](https://files.readme.io/e9f734a-image.png)

2. Select the **Payment** tab.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b025aba-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


3. Click the **PayU Biz **toggle to enable.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/214ab27-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


4. Click **Manage** next to PayUBiz.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5457ecb-image.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


5. Fill the details as described in the following table and click **Save Changes**:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Enable",
    "0-1": "Select **Yes**from the drop-down list to enable the plugin",
    "1-0": "Checkout Experience",
    "1-1": "Select **Express Checkout** from the drop-down list.",
    "2-0": "Account type",
    "2-1": "Select **PayUBiz** from the drop-down list for the account type.",
    "3-0": "Gateway Mode",
    "3-1": "Select any of the following gateway environments from the drop-down list to which customer payment details will be redirected.  \n   **Sandbox:** This is the Test environment, and no actual fund transfer will take place.  \n  **Production:** This is the Live environment.  \n**Note**: If you select Sandbox in Transaction Mode,  use the following credentials:  \n  \n- Merchant ID: oZ7oo9\n- Salt: UkojH5TS",
    "4-0": "PayUBiz Key for Currency",
    "4-1": "Enter your production account key for the Production environment.",
    "5-0": "PayUBiz Salt Merchant for Currency",
    "5-1": "Enter your Salt for the Production environment. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).",
    "6-0": "Verify Payment",
    "6-1": "Select “Yes”. This will allow plugin to confirm status of transaction and reconcile with PayU APIs",
    "7-0": "Return Page",
    "7-1": "Select the page to which you want to redirect the customers after payment done:  \n_.  Shop  \n_.  Cart  \n_.  Checkout  \n_.  My Account"
  },
  "cols": 2,
  "rows": 8,
  "align": [
    null,
    null
  ]
}
[/block]