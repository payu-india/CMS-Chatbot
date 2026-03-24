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
After you set up your account in Shopify, you can integrate PayU India as the payment platform for your customers. 

Check the following video on Shopify integration:

<Embed typeOfEmbed="youtube" url="https://youtu.be/HL67ij0hp3Y?si=HUN7BrOOhcqvERv_" />

<br />

You can integrate with shopify using any of the following procedure in the tabs:

<Tabs>
  <Tab title="Install PayU Plugin">
    This section explains how to install the PayU plugin in Shopify and facilitate payments through PayU.

    ## Prerequisites

    • Shopify credentials
    • Active Shopify store setup
    • Remove any installed PayU plugin (if applicable)

    ## Integration Steps

    1. Log in to your Shopify account if not already logged in.

       Your Shopify account home page is displayed.

    <Image align="center" border={true} src="https://files.readme.io/a10ec7c5314424471430e1980f93cf194f143ca98e28117e0fdd75e4bed0bb87-install_shopify_step1.png" />

    2. Select **Settings** from the menu (at the bottom of the left navigation pane).

    <Image align="center" border={true} src="https://files.readme.io/d5a043ebd964cb9ec67222a7ad97d721bd80644e364d2d7493014ef31b7623c8-install_shopify_step2.png" />

    3. Select **Payments** from the menu on the left navigation pane.

    <Image align="center" border={true} src=" https://files.readme.io/1938653e03bf33d07122187dac2d4137bb91f0ca84a2a2f81e4af60f5d78f7ce-install_shopify_step3.png" />

    4. Click **Add payment methods** under the **Supported Payment methods** section.

       The *Add payment methods* page is displayed.

    5. Select the **Search by provider** tab and enter **PayU**.

    <Image align="center" border={true} src="https://files.readme.io/f50e8deebf8a9f018a2776d3e3f2b2fe5eb96c3245708016720ce8b14cdd7a11-install_shopify_step5.png" width="550px" />

    6. Select **PayU India** from the result.

    A page similar to the following screenshot is displayed.

    <Image align="center" border={true} src="https://files.readme.io/3a1fbf5c25ccb134cf1462ce08f90daa730f9ce07833a32e1bd6ed780bd7dd4c-install_shopify_step6.png" width="550px" />

    7. Install the PayU plugin:
       * Click **Activate**.
       * Click **Connect** (scroll down if required).

    <Image align="center" border={true} src="https://files.readme.io/afa1fb57c9ad88d7921c94e2f1d91b5f9c20a133e2762069c24f32858ac5c591-install_shopify_step7a.png" width="550px" />

    The *Install* page for the PayU India plugin is displayed.

    <Image align="center" border={true} src="https://files.readme.io/91633eea9c151f8f8ae89233bb13f99260fc71dea7baea0cecddd2948cc9daa5-install_shopify_step7b.png" width="550px" />

    * Click **Install app**.

      The *Configure collect payments with PayU* pop-up page is displayed.

    <Image align="center" src="https://files.readme.io/ad7ccb4b8d11ea564e2f030013133fdb1af40206e0195bf89480e9c8523643e8-install_shopify_step7c.png" width="550px" />

    8. Configure the merchant key and salt:
       * Enter your merchant key in the **Merchant Key** field.

    > **Reference**: For more information on how to generate the Key and Salt, refer to any of the following:

    * **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
    * **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
    * Enter your Salt in the **Merchant Salt** field.
    * Click **Submit**.

      The \_Pay\_U page is displayed.

    <Image align="center" border={true} src="https://files.readme.io/ddbc6dd2bed950f62a88c441f3620906c303ac9a8578a70db0e34c6449f892a0-install_shopify_step8.png" width="550px" />

    * Click **Activate PayU**.

    > 📘 Test Mode for PayU Plugin:
    >
    > You need to test your Shopify integration with your Test key and Salt, so you need  to select the**Enable test mode** check box in this last step before clicking the **Activate PayU** button:
    >
    >     <Image align="center" border={true} src="https://files.readme.io/e7cb91c0ed41d2cf90e518fd8769ac9b6d5363485c1c0ed3fc4ff9fa722a64fd-install_shopify_step8_note.png" width="450px" />
  </Tab>

  <Tab title="Integrate with Shopify using Hyperlink">
    This section involves direct integration using a hyperlink that leads to the Shopify PayU India app.

    ## Prerequisites

    • Merchant account with PayU created beforehand
    • Shopify credentials
    • Remove previously installed PayU plugins
    • Active Shopify store

    ## Integration Steps

    1. Navigate to the following URL to open the Shopify PayU India app:

    [https://apps.shopify.com/payu-india](https://apps.shopify.com/payu-india)

    The PayU India app page is displayed.

    <Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/PayU_Shopify_App_page-1024x619.png" />

    2. Click **Add app**.

       The Shopify Login page is displayed.

    <Image align="center" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Login_Page-796x1024.png" width="550px" />

    3. Enter your Shopify credentials and log in.

       The *PayU India* page is displayed.

    <Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_India_Page_Direct_Link-703x1024.png" width="550px" />

    4. Click **Install app**.

       The *Collect payments with PayU* page is displayed.

    <Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.40.00-PM-1024x688.png" width="550px" />

    5. Enter your merchant key in the **Merchant Key** field.

    **Note**: You need to register or create an account on [PayU Dashboard](https://onboarding.payu.in/app/account) to get the merchant key and salt. For viewing or generating your merchant key and salt, refer to [Generate Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).

    6. Enter your Salt in the **Merchant Salt** field.
    7. Scroll down and ensure the payment modes or card type you wish to support for your customers are selected. If you do not wish to support a payment mode or card type, clear the corresponding check box selection.

    <Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Shopify_PayU_India_Page_Contd-784x1024.png" width="550px" />

    8. Select the **Enable Test mode** check box on the **Test mode** section to test the integration with the test key and salt provided by PayU.
    9. Click **Activate PayU India**.

       ## Additional Notes

       • Verify transactions using the **Verify Payment API** for reconciliation
  </Tab>
</Tabs>

## Summary

Both integration methods provide effective ways to connect PayU India with your Shopify store. Choose the method that best fits your technical requirements and preferences:

• **Plugin Installation**: Direct integration through Shopify's payment settings
• **Hyperlink Integration**: App-based installation through Shopify App Store
