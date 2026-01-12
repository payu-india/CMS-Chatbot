---
title: Enable Onsite Payments on Shopify
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
PayU has enabled a seamless payment experience for all card payments on Shopify checkout thereby eliminating redirection on cards.

## Benefits

* Improved Success Rate
* High Conversion rate
* Better Payment Experience for the users

## Install Procedure

To enable onsite payments on Shopify:

1. Login to your Shopify Dashboard.
2. Navigate to **Settings** > **Payments** and click the **Choose a provider** button.

<Image align="center" border={false} src="https://files.readme.io/ef4e2199f225e62ebe8243ad992571e5364f0e412dc8b98a758194d6c1712192-shopify_dashboard-onsite-choose-provider.png" />

3. Search for PayU onsite card payments.  

<Image border={false} src="https://files.readme.io/14acfc7d9dd856758a0c532393e109b289590768df8f8d55f33d1daed24f4b38-Screenshot_2024-10-07_at_11.18.46_AM.png" />

4. Select **Onsite Card Payments by PayU India** and click the **Install** button

![](https://files.readme.io/cba8a7bf3976981cd6116495d7c30b59313ba8411a0444c01b72a7d0cef2c893-Screenshot_2024-10-07_at_11.21.54_AM.png)The _Collect payments with PayU_ page is displayed.

> 📘 Note:
>
> Follow the Step 1 to 4 and click the **Manage** button if the following _Collect payments with PayU_ page is not displayed to configure the PayU key and Salt.

<Image border={false} src="https://files.readme.io/bba590c0388174a035fecd8f888dccd536398d3cae6cb2a96db39d00e62d0354-enable_onsite_payment4.jpg" />

5. Enter the following details and click **Submit**:
   * Merchant Key: Enter the production key provided by PayU.
   * Merchant Salt: Enter the production key provided by PayU.
     > **Reference**: For getting merchant key and salt, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard). 

The Onsite Payment experience is enabled for the store.

## Using Test mode

To use the test mode for PayU Onsite plugin:

1. Login to your Shopify Dashboard.

2. Navigate to **Settings** > **Payments** and click the **Choose a provider** button.

   <Image align="center" border={false} src="https://files.readme.io/ef4e2199f225e62ebe8243ad992571e5364f0e412dc8b98a758194d6c1712192-shopify_dashboard-onsite-choose-provider.png" />

3. Search for PayU onsite card payments.  

   ![](https://files.readme.io/14acfc7d9dd856758a0c532393e109b289590768df8f8d55f33d1daed24f4b38-Screenshot_2024-10-07_at_11.18.46_AM.png) 

4. Select **Onsite Card Payments by PayU India**.

5. Click the **Deactivate** button if the plugin is active.

6. Click the **Test mode**toggle button to enable the test mode.

<Image align="center" border={false} src="https://files.readme.io/e06be7b42c1d74e0268e265c78841fad552cd401b1e0503edec5d21ff31d9118-768219ec3e08e5f0f08cfc800df08447d51a844a19d3298617db3508f75b341f-shopify-onsite-payments-manage-plugin.png" />

7. Select **Manage** from the  **More Actions** drop-down menu at the top-right corner.
8. Enter the test credentials for following details and click **Submit**:

   * Merchant Key: Enter the production key provided by PayU.
   * Merchant Salt: Enter the production key provided by PayU.
     > **Reference**: For getting merchant key and salt, refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).

   The following page is displayed for granting access permissions to Shopify.

<Image align="center" border={true} src="https://files.readme.io/493089ac31f92991225d703866e7a85590d8f14ab82554465302d9cbb80052e2-shopify_grant_access_to_payu.png" className="border" />

9. Click the **Allow access to this account** button.

The integration is complete.

<Image align="center" border={true} src="https://files.readme.io/1dd86e84fda955561292cff0d3df9d70bcd4d0454792e15ecbfe3519dc86878a-shopify_connected_to_payu_confirmation.png" className="border" />

> 📘 Notes:
>
> * If the **Onsite Card Payments by PayU India** plugin is not active, you will not be able to accept payments. Repeat Steps 3 and 4 and the click the **Activate** button.
> * If you are not able to activate or encounter any issues, contact [PayU Support](https://help.payu.in).
