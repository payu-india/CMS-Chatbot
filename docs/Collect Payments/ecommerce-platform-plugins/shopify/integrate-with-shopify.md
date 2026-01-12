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
After you set up your account in Shopify, you can integrate PayU India as the payment platform for your customers. You can integrate with shopify using any of the following procedure in the tabs:

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
  </Tab>

  <Tab title="Integrate with Shopify using Hyperlink">
    This section involves direct integration using a hyperlink that leads to the Shopify PayU India app.

    ## Prerequisites

    • Merchant account with PayU created beforehand
    • Shopify credentials
    • Remove previously installed PayU plugins
    • Active Shopify store

    ## Integration Steps

    **Step 1:** Navigate to the <a href="https://apps.shopify.com/payu-india">Shopify PayU India App</a>.

    **Step 2:** Click **Add App** to install PayU

    **Step 3:** Log in with your Shopify credentials when prompted

    **Step 4:** Configure Merchant Key and Salt
    • Enter the Merchant Key and Salt (available on the PayU dashboard)
    • Reference guide: \[Generate Production Key and Salt] (doc:generate-merchant-key-and-salt-on-payu-dashboard)

    **Step 5:** Scroll through and select/unselect payment modes

    **Step 6:** **Enable Test Mode** for testing the integration with test key and salt

    **Step 7:** Activate PayU India by clicking **Activate PayU India**

    ## Additional Notes

    • Verify transactions using the **Verify Payment API** for reconciliation
  </Tab>
</Tabs>

## Summary

Both integration methods provide effective ways to connect PayU India with your Shopify store. Choose the method that best fits your technical requirements and preferences:

• **Plugin Installation**: Direct integration through Shopify's payment settings
• **Hyperlink Integration**: App-based installation through Shopify App Store
