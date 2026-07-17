---
title: Install and Configure Magento Plugin
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
This section describes the procedure to install and configure the PayU Magento plugin.  If you encounter any issues while integration, refer to [Troubleshooting Magento integration](doc:troubleshooting-magento-integration).

## Install plugin

### Download the PayU plugin

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        PayU Plugin Version
      </th>

      <th>
        Supported PHP Versions or Feature
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
        Magento
      </td>

      <td>
        General
      </td>

      <td>
        <Anchor target="_blank" href="https://github.com/payu-india/PayUbiz_Magento/blob/master/Magento_CommercePro_plugin.zip">GitHub Location</Anchor>
      </td>
    </tr>

    <tr>
      <td>
        Magento Affordability
      </td>

      <td>
        Affordability
      </td>

      <td>
        <Anchor target="_blank" href="https://github.com/payu-india/PayUbiz_Magento/blob/master/PayUIndia_Affordability_Widget.zip">GitHub Location</Anchor>
      </td>
    </tr>

    <tr>
      <td>
        Magento v2.4.x
      </td>

      <td>
        PHP 7.4, 8.0, 8.1, 8.2
      </td>

      <td>
        <Anchor target="_blank" href="https://github.com/payu-india/PayUbiz_Magento/blob/master/PayUIndia_version_2.4.4.zip">GitHub Location</Anchor>
      </td>
    </tr>
  </tbody>
</Table>

### Procedure

To install the PayU plugin for Magento:

1. Download the PayU Plugin for Magento to the Magento version you use from the [Download the PayU plugin](#download-the-payu-plugin) table:
2. Extract the archive that you have downloaded.
3. Upload the _PayUIndia_ folder that you find after extracting the archive to the _app/code_ folder under Magento.

> **Note**: If the _code_ folder does not exist under the /_app_ folder, create a code folder.

4. Disable the cache:
   - Navigate to the **Magento Admin** panel > **System** > **Cache Management**.
   - Select all the cache types from left pane.
   - Select **Action** and then select **Disable** from the drop-down list.
   - Click **Submit.**
5. Execute the following Magento commands:

```plaintext
php bin/magento setup:upgrade
php bin/magento setup:static-content:deploy
```

6. Configure the module in the **Magento Admin** panel. For more information, refer to  [Configure Magento 2.4](#configure-magento-v24).

### Configure Magento v2.4

After installing PayU plugin for Magento v2.4, you need to configure Magento installation as described in this section.

To configure the Magento v2.4 environment for PayU:

1. Log in to the Magento admin panel.
2. Navigate to **Store** > **Configuration** > **Sales** > **Payment Methods**.
3. Expand the **Payu** menu.

   The _Configuration_ page with the **Payu** tab selected is displayed, similar to the following screenshot:

> **Note**: If the **Payu** tab is not displayed, clear the cache as described in the [Install Plugin for Magento v2.x](#install-plugin).

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/word-image-17.png)

4. Enter the configuration details as described in the following table:

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
        Enabled
      </td>

      <td>
        Select **Yes** from the drop-down list to enable the module.
      </td>
    </tr>

    <tr>
      <td>
        Account Type
      </td>

      <td>
        Select **PayUBiz** for the account type.
      </td>
    </tr>

    <tr>
      <td>
        Environment
      </td>

      <td>
        Select any of the following gateway environments from the drop-down list to which customer payment details will be redirected.

        - - **Sandbox**: This is the Test environment and no actual fund transfer will take place.

        - - **Production**: This is the Live environment. Use this value only
            If you select Sandbox in Transaction Mode, then use the following credentials:\\

        - Merchant id: oZ7oo9

        - Salt: UkojH5TS |
      </td>
    </tr>

    <tr>
      <td>
        Merchant Key
      </td>

      <td>
        Enter your production account key for the Production environment.
      </td>
    </tr>

    <tr>
      <td>
        Salt Key
      </td>

      <td>
        Enter your Salt for the Production environment. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
      </td>
    </tr>
  </tbody>
</Table>

> **Reference**: For more information on how to acess the Key and Salt, refer to any of the following:

- **Production**:  [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
- **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

5. Click **Save Config** at the top-right corner.

<Callout icon="📘" theme="info">
  ### Note:

  After configuring the PayU Test environment, use the test card details to test the payment. For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
</Callout>

The configuration for the PayU plugin is complete and your customers can make payments through PayU.

<Callout icon="📘" theme="info">
  ### Note:

  PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>..
</Callout>

<br />
