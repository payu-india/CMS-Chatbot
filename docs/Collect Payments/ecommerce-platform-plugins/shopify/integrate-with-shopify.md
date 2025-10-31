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

    **Step 1:** Log in to the Shopify dashboard

    **Step 2:** Navigate to **Settings** → **Payments**

    **Step 3:** Select **Add payment methods** under **Supported Payment methods**

    **Step 4:** Search for 'PayU' using the **Search by provider** option and select **PayU India**

    **Step 5:** Install the PayU Plugin
    • **Activate** → **Connect** → Follow prompts and click **Install App**

    **Step 6:** Configure Merchant Key and Salt
    • Enter the Merchant Key and Salt (retrieved from the PayU dashboard)
    • Reference guides:

    * <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Access Production Key and Salt</a>
    * <a href="https://docs.payu.in/docs/generate-test-merchant-key-and-salt">Access Test Merchant Key and Salt</a>

    **Step 7:** Activate PayU India
    • Test the integration by enabling **Test Mode**
    • After testing, click **Activate PayU**

    ## Additional Resources

    📹 **Video Guide:** YouTube Integration Tutorial ([https://www.youtube.com/watch?v=0Tqtenk1jGM](https://www.youtube.com/watch?v=0Tqtenk1jGM))
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
