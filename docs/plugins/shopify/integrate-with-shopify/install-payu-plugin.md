---
title: Install PayU Plugin - Shopify Integration
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
This section describes how install PayU plugin on your Shopify store to collect payments using PayU.

<RegisterMerchantPrerequiste />

The following video describes how to integrate with Shopify:

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F0Tqtenk1jGM%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0Tqtenk1jGM&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F0Tqtenk1jGM%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=0Tqtenk1jGM",
  "title": "Steps to integrate PayU from your Shopify dashboard",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/0Tqtenk1jGM/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=0Tqtenk1jGM",
  "typeOfEmbed": "youtube"
}
[/block]


## Prerequisites

- Credentials to log in to your Shopify account.
- Ensure that a store is set up on your Shopify account where you want to configure PayU as the payment provider
- If any PayU India plugin is installed, it must be removed.

## Procedure

To integrate Shopify with PayU as a payment gateway:

1. Log in to your Shopify account if not already logged in.

   Your Shopify account home page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Home_Page-1-1024x464.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


2. Select **Settings** from the menu (at the bottom of the left navigation pane).

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Settings_button_selection-1024x594.png",
        null,
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]


3. Select **Payments** from the menu on the left navigation pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Payments_Settings_Shopify-1024x615.png)

4. Click **Add payment methods** under the **Supported Payment methods** section.

   The _Add payment methods_ page is displayed.

5. Select the **Search by provider** tab and enter **PayU**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-5.59.01-PM-1024x431.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px",
      "border": true
    }
  ]
}
[/block]


6. Select **PayU India** from the result.

A page similar to the following screenshot is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.02.49-PM-1024x688.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px",
      "border": true
    }
  ]
}
[/block]


7. Install the PayU plugin:
   - Click **Activate**.
   - Click **Connect** (scroll down if required).

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_Connect-1024x537.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px",
      "border": true
    }
  ]
}
[/block]


The _Install_ page for the PayU India plugin is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Install_Shopify_Plugin-1024x760.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px",
      "border": true
    }
  ]
}
[/block]


- Click **Install app**.

    The _Configure collect payments with PayU_ pop-up page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/MicrosoftTeams-image-11-1024x651.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px"
    }
  ]
}
[/block]


8. Configure the merchant key and salt:
   - Enter your merchant key in the **Merchant Key** field.

> **Reference**: For more information on how to generate the Key and Salt, refer to any of the following:

- **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
- Enter your Salt in the **Merchant Salt** field.
- Click **Submit**.

    The \_Pay_U page is displayed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Activate_Payu_plugin_for_shopify-626x1024.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "550px",
      "border": true
    }
  ]
}
[/block]


- Click **Activate PayU**.

> 📘 Test Mode for PayU Plugin:
> 
> You need to test your Shopify integration with your Test key and Salt, so you need  to select the**Enable test mode** check box in this last step before clicking the **Activate PayU** button:
> 
> [block:image]{"images":[{"image":["https://files.readme.io/21dbe4109310b44250c121370a106e6abf71d69150c091227cab92de7c6bf856-shopify_payu_activate_test_mode.png","",""],"align":"center","sizing":"550px","border":true}]}[/block]