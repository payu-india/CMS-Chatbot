---
title: Install and Configure PrestaShop Plugin
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
This section describes the procedure to install and configure the PayU plugin for the PrestaShop platform.  If you encounter any issues while integration, refer to [Troubleshooting PrestaShop integration](doc:troubleshooting-prestashop-integration).

## Install Plugin for PrestaShop v1.7.x

To install the PayU plugin for PrestaShop v1.7.x:

1. Download the PayU plugin for PrestaShop v1.7.x from the following Dropbox location:

<https://github.com/payu-india/Prestashop/blob/main/Prestashop_ver1.7.zip>

2. Extract the **Prestashop\_ver1.7.zip** archive file.
3. Log in to Prestashop 1.7 Admin and open Modules.
4. Click **Upload a Module.**

   The _Upload a module_ pop-up page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-25.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px"
    }
  ]
}
[/block]


5. Drag the **Prestashop17PayUBiz.zip** archive file in to the _Upload a module_ pop-up page. 
6. Log in to the Prestashop admin panel.
7. Navigate to the **Modules** menu and locate the **PayU** module. You can also search for **PayU** module and locate it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-26.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px"
    }
  ]
}
[/block]


8. Click **Install**. 
9. Configure the plugin installation. For more information, refer to [Configure PrestaShop v1.7.x](#configure-prestashop-v17x).

## Configure PrestaShop v1.7.x

To configure the PrestaShop v1.7x installation after installing the PayU plugin:

1. Navigate to PrestaShop admin panel.
2. Select **Modules** > **Configure**.

   The **Configure** pane is displayed on the right pane.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/image-9-1024x538.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


3. Enter the configuration details as described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "0-0": "Mode",
    "0-1": "Select any of the following gateway environment from the Gateway Mode drop-down list to which customer payment details will be redirected to.  \n  \n- Test: This is the Test environment and no actual fund transfer will take place.\n- Production: This is the Live environment. Use this value only for your website in production. Payments sent in the production environment will get processed.",
    "1-0": "Pay UBiz Key",
    "1-1": "Enter your Key for the Production environment.",
    "2-0": "Pay UBiz Salt",
    "2-1": "Enter your Salt for the Production environment. For more information, refer to \\[Generate Key and Salt."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


**Reference**: For more information on how to access the Key and Salt, refer to any of the following:  

- **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

4. Click **Save** to save configuration details.
5. Logout and navigate to shop page to try the configuration through checkout.

> 📘 **Note**:
> 
> After configuring the Test environment, use the test card details to test the payment. For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)

If everything is installed and configured correctly, you will be able to checkout through the PayUBiz payment page. 

The configuration for the PayU plugin is complete.

> 📘 Note:
> 
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the** Verification Payment **API. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.