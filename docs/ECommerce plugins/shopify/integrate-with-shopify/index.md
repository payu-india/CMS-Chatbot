---
title: Integrate with Shopify
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
After you set up your account in Shopify, you can integrate PayU India as the payment platform for your customers. You can integrate with shopify using any of the following procedure:

* [Install PayU Plugin](doc:install-payu-plugin)
* [Integrate with Shopify using Hyperlink](doc:integrate-with-shopify-using-hyperlink)

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Install PayU Plugin

This part of the document describes how install PayU plugin on your Shopify store to collect payments using PayU.

<RegisterMerchantPrerequiste />

The following video describes how to integrate with Shopify:

<Embed url="https://www.youtube.com/watch?v=0Tqtenk1jGM" href="https://www.youtube.com/watch?v=0Tqtenk1jGM" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F0Tqtenk1jGM%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D0Tqtenk1jGM%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F0Tqtenk1jGM%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

> 📘 Prerequisites
>
> * Credentials to log in to your Shopify account.
> * Ensure that a store is set up on your Shopify account where you want to configure PayU as the payment provider
> * If any PayU India plugin is installed, it must be removed.

To integrate Shopify with PayU as a payment gateway:

1. Log in to your Shopify account if not already logged in.

   Your Shopify account home page is displayed.

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Home_Page-1-1024x464.png" className="border" />

2. Select **Settings** from the menu (at the bottom of the left navigation pane).

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Settings_button_selection-1024x594.png" className="border" />

3. Select **Payments** from the menu on the left navigation pane.

<Image border={false} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Payments_Settings_Shopify-1024x615.png" />

4. Click **Add payment methods** under the **Supported Payment methods** section.

   The _Add payment methods_ page is displayed.

5. Select the **Search by provider** tab and enter **PayU**.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-5.59.01-PM-1024x431.png" className="border" />

6. Select **PayU India** from the result.

A page similar to the following screenshot is displayed.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.02.49-PM-1024x688.png" className="border" />

7. Install the PayU plugin:
   * Click **Activate**.
   * Click **Connect** (scroll down if required).

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_Connect-1024x537.png" className="border" />

The _Install_ page for the PayU India plugin is displayed.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Install_Shopify_Plugin-1024x760.png" className="border" />

* Click **Install app**.

  The _Configure collect payments with PayU_ pop-up page is displayed.

<Image align="center" border={false} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/MicrosoftTeams-image-11-1024x651.png" />

8. Configure the merchant key and salt:
   * Enter your merchant key in the **Merchant Key** field.

> **Reference**: For more information on how to generate the Key and Salt, refer to any of the following:

* **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
* Enter your Salt in the **Merchant Salt** field.
* Click **Submit**.

  The _Pay_U page is displayed.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Activate_Payu_plugin_for_shopify-626x1024.png" className="border" />

* Click **Activate PayU**.

> 📘 Test Mode for PayU Plugin:
>
> You need to test your Shopify integration with your Test key and Salt, so you need  to select the**Enable test mode** check box in this last step before clicking the **Activate PayU** button:
>
> <Image align="center" border={true} width="550px" src="https://files.readme.io/21dbe4109310b44250c121370a106e6abf71d69150c091227cab92de7c6bf856-shopify_payu_activate_test_mode.png" className="border" />

## Integrate Shopify using Hyperlink

After you set up your account in Shopify, you can integrate PayU India as the payment platform for your customers.

> 📘 Prerequisites:
>
>
>
> * Merchant account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
> * Credentials to log in to your Shopify account.
> * Ensure that a store is set up on your Shopify account where you want to configure the PayU as the payment provider
> * If any PayU India plugin is installed, it must be removed.

To integrate Shopify with PayU as a payment gateway:

1. Navigate to the following URL to open the Shopify PayU India app:

[https://apps.shopify.com/payu-india](https://apps.shopify.com/payu-india)

The PayU India app page is displayed.

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/PayU_Shopify_App_page-1024x619.png" className="border" />

2. Click **Add app**.

   The Shopify Login page is displayed.

<Image align="center" border={false} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Login_Page-796x1024.png" />

3. Enter your Shopify credentials and log in.

   The _PayU India_ page is displayed.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_India_Page_Direct_Link-703x1024.png" className="border" />

4. Click **Install app**.

   The _Collect payments with PayU_ page is displayed.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.40.00-PM-1024x688.png" className="border" />

5. Enter your merchant key in the **Merchant Key** field.

**Note**: You need to register or create an account on [PayU Dashboard](https://onboarding.payu.in/app/account) to get the merchant key and salt. For viewing or generating your merchant key and salt, refer to [Generate Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).

6. Enter your Salt in the **Merchant Salt** field.
7. Scroll down and ensure the payment modes or card type you wish to support for your customers are selected. If you do not wish to support a payment mode or card type, clear the corresponding check box selection.

<Image align="center" border={true} width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Shopify_PayU_India_Page_Contd-784x1024.png" className="border" />

8. Select the **Enable Test mode** check box on the **Test mode** section to test the integration with the test key and salt provided by PayU.
9. Click **Activate PayU India**.

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>..
