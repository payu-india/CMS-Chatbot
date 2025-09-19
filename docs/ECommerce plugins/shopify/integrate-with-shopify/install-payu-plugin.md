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

<Embed url="https://www.youtube.com/watch?v=0Tqtenk1jGM" title="Steps to integrate PayU from your Shopify dashboard" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/0Tqtenk1jGM/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=0Tqtenk1jGM" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F0Tqtenk1jGM%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D0Tqtenk1jGM%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F0Tqtenk1jGM%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

## Prerequisites

* Credentials to log in to your Shopify account.
* Ensure that a store is set up on your Shopify account where you want to configure PayU as the payment provider
* If any PayU India plugin is installed, it must be removed.

## Procedure

To integrate Shopify with PayU as a payment gateway:

1. Log in to your Shopify account if not already logged in.

   Your Shopify account home page is displayed.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Home_Page-1-1024x464.png" />

2. Select **Settings** from the menu (at the bottom of the left navigation pane).

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Settings_button_selection-1024x594.png" />

3. Select **Payments** from the menu on the left navigation pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Payments_Settings_Shopify-1024x615.png)

4. Click **Add payment methods** under the **Supported Payment methods** section.

   The *Add payment methods* page is displayed.

5. Select the **Search by provider** tab and enter **PayU**.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-5.59.01-PM-1024x431.png" />

6. Select **PayU India** from the result.

A page similar to the following screenshot is displayed.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.02.49-PM-1024x688.png" />

7. Install the PayU plugin:
   * Click **Activate**.
   * Click **Connect** (scroll down if required).

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_Connect-1024x537.png" />

The *Install* page for the PayU India plugin is displayed.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Install_Shopify_Plugin-1024x760.png" />

* Click **Install app**.

    The *Configure collect payments with PayU* pop-up page is displayed.

<Image align="center" width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/MicrosoftTeams-image-11-1024x651.png" />

8. Configure the merchant key and salt:
   * Enter your merchant key in the **Merchant Key** field.

> **Reference**: For more information on how to generate the Key and Salt, refer to any of the following:

* **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
* Enter your Salt in the **Merchant Salt** field.
* Click **Submit**.

    The \_Pay\_U page is displayed.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Activate_Payu_plugin_for_shopify-626x1024.png" />

* Click **Activate PayU**.

> 📘 Test Mode for PayU Plugin:
>
> You need to test your Shopify integration with your Test key and Salt, so you need  to select the**Enable test mode** check box in this last step before clicking the **Activate PayU** button:
>
> <Image align="center" className="border" width="550px" border={true} src="https://files.readme.io/21dbe4109310b44250c121370a106e6abf71d69150c091227cab92de7c6bf856-shopify_payu_activate_test_mode.png" />
