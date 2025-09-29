---
title: Install and Configure OpenCart Plugin
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
This section describes how to install configure PayU Plugin on the OpenCart platform.  If you encounter any issues while integration, refer to [Troubleshooting OpenCart Integration](doc:troubleshooting-opencart-integration).

## Install plugin for OpenCart

### Download the PayU plugin

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        OpenCart Version
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
        OpenCart v3.0.2
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/PayUbiz_Opencart/releases/tag/ver3.0.2)
      </td>
    </tr>

    <tr>
      <td>
        OpenCart v3.0
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/PayUbiz_Opencart/releases/tag/ver_3.0)
      </td>
    </tr>

    <tr>
      <td>
        OpenCart v2.3
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/PayUbiz_Opencart/releases/tag/ver_2.3)
      </td>
    </tr>

    <tr>
      <td>
        OpenCart v2.2
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/PayUbiz_Opencart/releases/tag/ver_2.2)
      </td>
    </tr>

    <tr>
      <td>
        OpenCart v2.0
      </td>

      <td>
        [GitHub Location](https://github.com/payu-india/PayUbiz_Opencart/releases/tag/ver_2.0)
      </td>
    </tr>
  </tbody>
</Table>

### Procedure

To download and install the PayU archive for the OpenCart plugin:

1. Ensure that the OpenCart plugin is installed.
2. Download the PayU OpenCard integration archive for the OpenCart version you are using as listed in the [Download the PayU Plugin ](#download-the-payu-plugin)section:
3. Install the downloaded archive using **Extensions** > **Extension Installer**. For more information, refer to the [OpenCart Documentation](http://docs.opencart.com/en-gb/extension/installer/).

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Configure OpenCart

To configure OpenCart after installing the PayU plugin:

1. Enable **PayU** in **Payment setting**s section from OpenCart admin panel.
2. Navigate to the **Payments** page.

   The *Payments* page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-28.png)

3. Click the **Edit** button for the **PayU** entry.

   The PayU configuration page is displayed.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/09/OpenCart_PayU_Config-1-1024x730.jpg)

4. Enter the configuration details as in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Merchant ID INR
      </td>

      <td>
        Enter the test key for the Test environment or the Production key for the Production environment.
      </td>
    </tr>

    <tr>
      <td>
        Salt INR
      </td>

      <td>
        Enter the test salt for the Test environment or Production salt for the Production environment.
      </td>
    </tr>

    <tr>
      <td>
        Mode
      </td>

      <td>
        Select any of the following gateway environments from the Mode drop-down list to which customer payment details will be redirected to.

        * Test: This is the Test environment and no actual fund transfer will take place.
        * Production: This is the Live environment. Use this value only for your website in production. Payments sent in the production environment will get processed. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        Select Enable from the drop-down list to enable the module.
      </td>
    </tr>

    <tr>
      <td>
        Payment Gateway
      </td>

      <td>
        Select PayUBiz from the drop-down list if you want to redirect to the PayUbiz page for payments.
      </td>
    </tr>

    <tr>
      <td>
        Bank Code
      </td>

      <td>
        Select PayUBiz Bank Code from this drop-down list.
      </td>
    </tr>
  </tbody>
</Table>

> **Reference**: For more information on how to access the Key and Salt, refer to any of the following:

* **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

5. Map all the possible states of a transaction from PayU with the corresponding OpenCart status.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-31.png)

6. Select the **PayUBiz Payment Gateway** method on the checkout page.
7. Perform a test transaction.

> **Note**: After configuring the Test environment, use the test card details to test the payment. For more information, refer to  [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

<Image align="center" width="612px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/09/Screenshot-2021-09-01-at-6.44.03-PM-1024x984.jpg" />

The successful payment confirmation message is displayed if the payment is successful.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-34.png)

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>.