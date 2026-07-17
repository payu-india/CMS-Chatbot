---
title: Install and Configure PayU WooCommerce Plugin
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
This section describes the procedure to install and configure the PayU WooCommerce plugin by either using the WordPress Plugin or manually. Also, how to configure international payments.  If you encounter any issues while integration, refer to [Troubleshooting WooCommerce Integration](doc:troubleshooting-woocommerce-integration).

## Install plugin

You can install the PayU WooCommerce plugin by either using the WordPress Plugin Installer wizard or manually.

<Callout icon="📘" theme="info">
  ### Notes:

  - PayU supports WooCommerce version 3.x or later and you need to use the PayU plugin based on the WooCommerce version you are using. Use the PayU plugin according to the WooCommerce version as listed in the [Download the PayU Plugin for WooCommerce](#download-the-payu-plugin) subsection.
  - WooCommerce does not have built-in multi-currency feature. Hence it is important to use separate multi-currency plugin for WooCommerce. This plugin uses currency present in Order.
</Callout>

### Download the PayU plugin

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        PayU Plugin Version
      </th>

      <th>
        Supported WooCommerce Versions
      </th>

      <th>
        PayUI Plugin

        Download Link
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Woocommerce v4.1
      </td>

      <td>
        v8.0 or Higher
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/Woocommerce/blob/main/WooCommerce_CommercePro_plugin.zip)
      </td>
    </tr>
  </tbody>
</Table>

### Procedure

#### Install the PayU Plugin using Installer

To install the PayU plugin using the WordPress installer:

1. Login to the **WordPress Admin** panel.
2. Navigate to **Plugin**s **>Add New**.
3. Click **Upload Plugin**.

   The _Add Plugins_ page is displayed in WordPress.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image.png)

4. Choose the PayU plugin zip that you downloaded earlier (as required in [Download the PayU plugin](#download-the-payu-plugin) section) from the file chooser.
5. Click **Install Now**.

#### **Install Manually**

1. Unzip the PayU plugin zip that you downloaded (as required in the [Download PayU Plugin ](#download-the-payu-plugin)section) earlier.

   The contents of the PayU plugin zip are extracted to the  folder and folder name is based on the plugin version:

- Version 5.5.2: _WooCommerce_v552_MultiCurrency_PayUBiz_ folder.
- Version 3.8.1: _WooCommerce_v381_MultiCurrency_PayUBiz_ folder.

2. Copy the folder created in Step 1 to the clipboard and paste or upload it to _\<wordpress root>\wp-content\plugins_ folder, where _\<wordpress root>_ is the location where WordPress is installed.
3. Log in to the WordPress Admin panel.
4. Navigate to Plugins.
5. Search for the PayU plugin and activate the plugin.

## Configure WooCommerce Settings

To configure WooCommerce Settings after installing the PayU plugin:

1. Log in to WordPress as admin.
2. Open **WooCommerce Settings**.
3. Select the **Payments** tab.
4. Click the **PayUBiz** toggle button to enable PayU as payment gateway.

   The PayUBiz is enabled as in the following screenshot:

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/woocommerce_payubix1-1024x791.png)

5. Click **Manage.**

   The _PayUBiz payment_ page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/woocommerce_payubiz2-1024x793.png)

6. Select the **Enable PayU** check box to enable the module.
7. Enter a description in the **Description** text area that must be displayed on your checkout page.
8. Select any of the following gateway environment from the **Gateway Mode** drop-down list to which customer payment details will be redirected to.
   - **Sandbox**: This is the Test environment and no actual fund transfer will take place.
   - **Production**: This is the Live environment. Use this value only for your website in production. Payments sent in the production environment will get processed.

> **Note**: PayU suggests you use Sandbox for testing to validate the payment.

9. Enter the parameters for each currency if you had configured as multi-currency. You can configure upto 10 currencies. For example, to configure Indian Rupees as the first currency:
   - Enter **INR** in the **Currency 1** field.
   - Enter your merchant key in the **PayU Key for Currency 1** field. If you had selected **Sandbox** in Step 8, enter your Test environment key as key.
   - Enter your Salt in the **PayU Salt for Currency 1** field. If you had selected **Sandbox** in Step 8, enter your Test environment Salt as Salt.

> **Note**: Step 9 is mandatory, so you need to provide input for **Currency 1**, **PayU Key for Currency 1** and **PayU Key for Currency 2** fields. For more information on how to access the Key and Salt, refer to any of the following:

- **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

> **Note**: You must enter INR (all in capitals) in the **Currency 1** field to avoid any error messages when the customer checks out on your website.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/woocommerce_payubiz2a-1024x513.png)

10. Select the **Verify Payment** check box (after the currency fields) to verify the payment.
11. Select the page from the **Return Page** drop-down list. The _My Account_ option is selected by default and the selected return page is displayed after payment response.

> **Note**: You may create a custom page and select from this drop-down list. However, the custom page must contain appropriate WordPress / WooCommerce codes to show custom messages. Refer to the [WooCommerce Development Guide for custom pages.](https://docs.woocommerce.com/document/woocommerce-theme-developer-handbook/)

12. Click **Save Changes**.

    Your customer will get **PayUBiz** as a payment option during the checkout process. 


<Image src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-8.png" align="center" border={true} />


A page similar to the following screenshot is displayed after the customer clicks **Place Orde**r on your shopping page.

> **Note**: After configuring with the PayU Test environment, use the test card details to test the payment. For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-10.png)

<Callout icon="📘" theme="info">
  ### Note:

  PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>..
</Callout>

## Configure international payments or MCP on WooCommerce

If you are accepting multiple currencies, ensure you configure the following:

<Callout icon="📘" theme="info">
  ### Enable international payments:

  To enable international payments, contact your PayU key account manager (KAM).
</Callout>

- Configure the base currency and foreign currencies on your WooCommerce Store Settings. For more information refer the [WooCommerce > Shop Currency Documentation ](https://woocommerce.com/document/shop-currency/).
- Configure the following parameters in Step 9 of [Configure WooCommerce Settings](##configure-woocommerce-settings)  for accepting payments in another currency:
  1. Enter the currency code in the **Currency 2** field.
  2. Enter your merchant key in the **PayU Key for Currency 2** field. If you had selected **Sandbox** in Step 8 of of [Configure WooCommerce Settings](##configure-woocommerce-settings), enter your Test environment key as key.
  3. Enter your Salt in the **PayU Salt for Currency 2** field. If you had selected **Sandbox** in Step 8 of [Configure WooCommerce Settings](##configure-woocommerce-settings), enter your Test environment Salt as Salt.
  4. If you want add more currencies, repeat the above Steps i to iii.

<br />
