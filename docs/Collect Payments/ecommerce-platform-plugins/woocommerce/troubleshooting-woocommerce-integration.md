---
title: Troubleshooting WooCommerce Integration
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
When you are integrating PayU with WooCommerce, at times you may encounter some issues. This section describes the recommended steps to troubleshoot any issues which you face while integration with WooCommerce.

## Payment Page is showing only card payment mode

Uninstall and delete the current plugin that you had installed earlier and install the PayU WooCommerce v3.8.2 plugin. Also, ensure that you have configured the following fields. For more information, refer to refer to [Configure WooCommerce Settings](#configure-woocommerce-settings).

* **Currency 1** = INR
* **PayU Key for Currency 1 =** Your merchant key
* **PayU Salt for Currency 1** = Your merchant salt
* Ensure the **Verify Payment** checkbox is selected.
* Other currency and key/salt fields remains blank.

## PayU is not appearing as a payment method or not working

* Check whether the merchant API key and Salt are configured accurately and navigate to [Merchant Dashboard](http://onboarding.payu.in/) and verify these values. For more information, refer to [Configure WooCommerce Settings](doc:install-and-configure-payu-woocommerce-plugin#configure-woocommerce-settings). For more information on generating API key and salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard)

> 📘 Note:
>
> The Salt that you get from PayU is case-sensitive. It is recommended to copy the Salt from the Dashboard and paste it in **PayU Salt for Currency 1** field of the _PayUBiz payment_ page. For more information, refer to [Configure WooCommerce Settings](doc:install-and-configure-payu-woocommerce-plugin#configure-woocommerce-settings).

* Check whether the PHP curl extension is installed and activated.

## Unable to process your request

An error message similar to the following screenshot is displayed if the value entered in the **Currency 1** field of the _PayUBiz payment_ page is not in capital letters or blank. For more information, refer to [Configure WooCommerce Settings](doc:install-and-configure-payu-woocommerce-plugin#configure-woocommerce-settings).

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/09/image-6-1024x694.jpg" />

## Incorrect return page is displayed after payment

You may have not configured the **Return Page** field on the **Payments** tab during configuration. For more information, refer to [Configure WooCommerce Settings](doc:install-and-configure-payu-woocommerce-plugin#configure-woocommerce-settings).

> 📘 Note:
>
> For any other issues you face with WooCommerce, refer to the [WooCommerce Troubleshooting](https://docs.woocommerce.com/documentation/plugins/woocommerce/troubleshooting/) documentation.

## SI or Recurring Payments with WooCommerce

PayU does not support recurring payments with WooCommerce. PayU recommends you to use the Web Checkout integration. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).

## International payments with WooCommerce

If you have enabled international payments for your merchant account, international payments will work with WooCommerce platform. Configure the currency settings on the PayU plugin for WooCommerce. For more information, refer to [Install and Configure PayU WooCommerce Plugin](doc:install-and-configure-payu-woocommerce-plugin) >. [International payments with WooCommerce](doc:install-and-configure-payu-woocommerce-plugin#configure-international-payments-or-mcp-on-woocommerce).

## FAQs

* **I need a PayU Money Plugin for WooCommerce to enable EMI options. Where can I find and integrate this plugin?**

PayU offers plugins for various platforms, including WooCommerce. Visit the PayU developer documentation or contact PayU support for information on the PayU Money Plugin for WooCommerce.
