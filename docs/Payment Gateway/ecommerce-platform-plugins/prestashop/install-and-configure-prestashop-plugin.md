---
title: Install and Configure PrestaShop Plugin
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
This section describes the procedure to install and configure the PayU plugin for the PrestaShop platform.  If you encounter any issues while integration, refer to [Troubleshooting PrestaShop integration](doc:troubleshooting-prestashop-integration).

## Install Plugin for PrestaShop v1.7.x

To install the PayU plugin for PrestaShop v1.7.x:

1. Download the PayU plugin for PrestaShop v1.7.x from the following Dropbox location:

[https://github.com/payu-india/Prestashop/blob/main/Prestashop\_ver1.7.zip](https://github.com/payu-india/Prestashop/blob/main/Prestashop_ver1.7.zip)

2. Extract the **Prestashop\_ver1.7.zip** archive file.
3. Log in to Prestashop 1.7 Admin and open Modules.
4. Click **Upload a Module.**

   The *Upload a module* pop-up page is displayed.

<Image align="center" width="550px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-25.png" />

5. Drag the **Prestashop17PayUBiz.zip** archive file in to the *Upload a module* pop-up page. 
6. Log in to the Prestashop admin panel.
7. Navigate to the **Modules** menu and locate the **PayU** module. You can also search for **PayU** module and locate it.

<Image align="center" width="550px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-26.png" />

8. Click **Install**. 
9. Configure the plugin installation. For more information, refer to [Configure PrestaShop v1.7.x](#configure-prestashop-v17x).

## Configure PrestaShop v1.7.x

To configure the PrestaShop v1.7x installation after installing the PayU plugin:

1. Navigate to PrestaShop admin panel.
2. Select **Modules** > **Configure**.

   The **Configure** pane is displayed on the right pane.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/image-9-1024x538.png" />

3. Enter the configuration details as described in the following table:

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
        Mode
      </td>

      <td>
        Select any of the following gateway environment from the Gateway Mode drop-down list to which customer payment details will be redirected to.

        * Test: This is the Test environment and no actual fund transfer will take place.
        * Production: This is the Live environment. Use this value only for your website in production. Payments sent in the production environment will get processed.
      </td>
    </tr>

    <tr>
      <td>
        Pay UBiz Key
      </td>

      <td>
        Enter your Key for the Production environment.
      </td>
    </tr>

    <tr>
      <td>
        Pay UBiz Salt
      </td>

      <td>
        Enter your Salt for the Production environment. For more information, refer to \[Generate Key and Salt.
      </td>
    </tr>
  </tbody>
</Table>

**Reference**: For more information on how to access the Key and Salt, refer to any of the following:

* **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

4. Click **Save** to save configuration details.
5. Logout and navigate to shop page to try the configuration through checkout.

> 📘 **Note**:
>
> After configuring the Test environment, use the test card details to test the payment. For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets)

If everything is installed and configured correctly, you will be able to checkout through the PayUBiz payment page. 

The configuration for the PayU plugin is complete.

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>.