---
title: Install CommercePro Checkout App
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
To install PayU CommercePro Checkout application in  your Shopify store. 

1. Search for it in Shopify App store.  

OR  

  Navigate to the following URL: 

[https://apps.shopify.com/payu-commercepro-checkout](https://apps.shopify.com/payu-commercepro-checkout) 

2. Click **Install** button to initiate installation process in your store.  

> **Note**: If you have not logged on to Shopify, click the **Log in to install** button and log in with your Shopify Partner Account credentials.  

<Image align="center" className="border" border={true} src="https://files.readme.io/b542e5bbdb5d06e4efa0c580e78a02f48d3da5540ebe9e9905c0103fd30b29ce-Shopify_CommercePro_Click_Login_to_Install.png" />

  You are redirected to request grant / Install App screen into your Shopify store.  

3. Click ‘**Install** to grant permissions and install the PayU CommercePro Checkout app in your store. 

<Image align="center" className="border" width="400px" border={true} src="https://files.readme.io/7768b599fe2f1af24041a6ade678c30e52b3022b73f33abf50de5923e08de16b-shopify-install_app-button.png" />

  You will be redirected to PayU Account sign in page.  

4. Log in into your PayU Account using the **Email** and **Password** OR **Login using OTP** option. 

   This process will connect your PayU account with ‘PayU CommercePro Checkout’ Shopify App.  

<Image align="center" width="650px" src="https://files.readme.io/66f1002-payu_in_dashboard_login.png" />

   After successfully login into your PayU Account, it will redirect you to the successfully login confirmation screen, and then it will redirect automatically to Shopify in 5 seconds. The *Authorize Your Account* page is displayed.

<Image align="center" className="border" width="650px" border={true} src="https://files.readme.io/d2750f6160a36b23c8d57d0591cdf5dc3225c1529f95ee5fddef0e865c15be33-shopify_authorize-acct.png" />

You can go back to Shopify manually by clicking **Back to Shopify** button.  

<Image align="center" className="border" width="650px" border={true} src="https://files.readme.io/86df639e962a2f8a86c76f3cdb39536ed95c269f9717ee10d023e29b41374078-shopify_back_from_payu.png" />

   You will be redirect to the **PayU CommercePro Checkout** Shopify App’s Dashboard.

## Set up Login Widget

You can set up the PayU CommercPro App Login Widget using any of the following procedure described in this section:

* [Set up Login Widget from Dashboard](#set-up-login-widget-from-dashboard)

OR

* [Enable Login Widget from Themes](#enable-login-widget-from-themes)

### Set up Login Widget from Dashboard

To set up PayU commerce pro Login widget into your store: 

> 📘 Note:
>
> Verify the pre-requisite Shopify settings requirements. For more information, refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).

1. Verify that Customer Sync Process is completed on the PayU CommercePro Checkout app:

> **Note**: It may take some time for synching and depends on the total customer count on your store.

*   Navigate to Store admin > **Apps** > **PayU CommercePro Checkout** > **Dashboard**.\
    - Check if the **Complete** status is displayed under **Customer Sync Process** as in the following screenshot:

<Image align="center" className="border" border={true} src="https://files.readme.io/f5ba3965e383100b419c679e1c5b3f12676d86370abbb3c63c0e0e52ffcb898f-Shopify_CommercePro_Sync_Complete.png" />

2. Verify that show login links is enabled:

* Navigate to **Online Store**> **Settings > Customer accounts**.
* Click the **Show login links**toggle button to enable it.
* Ensure that the **Classic** is selected as in the following screenshot:

<Image align="center" src="https://files.readme.io/a96046cb261643e0e25f9ec7cb1f760f1637a8a681208b17bc50b97829f42ca4-Shopify_CommercePro_Settings_Classic.png" />

3. Verify that the following sections are hidden in theme in which you want to enable Login widget:
   * Customer login page > Login. 
   * Customer Register Page > Registration 
4. Verify that guest checkout is disabled:
   * Navigate to **Settings** > **Checkout** 
   * Select **Require customers to log in to their account before checkout** check box. 
   * Click **Save** at the bottom-right.

<Image align="center" className="border" border={true} src="https://files.readme.io/b11ebe1eaeb6d526efc963496da4e7f390bcc74a530505aebf2b10b0e22179bd-Shopify_CommercePro_Settings_Login_Checkbox.png" />

5. Verify that captcha on login, create account and password recovery pages is Disabled. 
   * Navigate to **Online Store** > **Preferences** under **Sales channels**.
   * In the **Spam protection** section, ensure that the **Enable nCaptcha to login, create account and password recovery pages** check box is not selected.
   * Click **Save** at the bottom-right. 

<Image align="center" className="border" border={true} src="https://files.readme.io/b524a6faca6c12b212a067bcb346918cbcd27be88cf31f0c2c013bd4bdfa8417-Shopify_CommercePro_Captcha_Settings.png" />

### Enable Login Widget from Themes

To enable Customer login widget into storefront:

1. Navigate to Online store > **Themes**.
2. Click the **Customize** button in which you want to setup widget. 

<Image align="center" className="border" border={true} src="https://files.readme.io/1d9b7e4cf97e0a6feb29271f4e7e7bd677f71e2b1007b58b48dce120426d8b6c-Shopify_CommercePro_Customize_Theme.png" />

3. Select **App embeds** on left side navigation bar similar to the following screenshot:

<Image align="center" className="border" border={true} src="https://files.readme.io/a31915d7820212d31c697b11aee96f261cbae6c8d318683e6e092b59fa92c2d3-Shopify_CommercePro_App_Embeds.png" />

4. Search for "Customer Login" using the search bar. 
5. Look for "Customer login – PayU ..." enable it using the toggle button.
6. Click **Save** located at the top-right corner.

## Enable Shopify COD (Optional)

To use Shopify’s default payment options or other PGs in addition to PayU – including Shopify’s default Cash on Delivery – follow this procedure to disable payment customization. After you complete the procedure, the CommercePro app can be used with any payment modes on Shopify’s Checkout:.

To disable payment customization on Shopify:

1. Navigate to **Settings** > **Payments**. 

2. Scroll down to “ **Payment method customization** section and click on **Manage**.\
   ![](https://files.readme.io/f779b0e63ea3cea3bcee742441eae12119fdc9cb348b41680c7a121688b91e34-shopify-manage-pymt-method.png)

3. Select the **PayU OTP Login** check box and then click **Deactivate** in the **Manage your customizations** pane.\
   ![](https://files.readme.io/005d0b776fcc173aea14e5f7d1640bc940e16fb52814f027e0fbcf589811ceb9-disable-shopify-payu-pymt-otp-login.png)  

After the **PayU OTP Login** updated to “Inactive” state, any non-PayU payment mode (including Shopify’s Cash on Delivery option) will be available on the checkout page.\
![](https://files.readme.io/be492411b6376c70cea3293c2408113154bdb546afe328aebeee0203578e3c6c-shopify-deactivated-payu-pymt.png)
