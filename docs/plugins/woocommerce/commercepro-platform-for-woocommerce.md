---
title: CommercePro Checkout for WooCommerce
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
This section describes how to install and configure PayU plugin for WooCommerce on CommercePro Checkout. For overview of CommercePro Checkout and customer journey with PayU Plugin, refer to [CommercePro Checkout](doc:commercepro-checkout).

## Prerequisites

* Merchant must be active on PayU.
* Merchant’s website must be on hosted on WooCommerce v3.4
* The merchant should be on One PayU platform.

## Plugin location

The plugin can be downloaded from the following Github location:

| WooCommerce Version | PayU CommercePro Checkout Download Location                                                      |
| :------------------ | :----------------------------------------------------------------------------------------------- |
| v3.4                | [Github](https://github.com/payu-india/Woocommerce/blob/main/WooCommerce_CommercePro_plugin.zip) |

## Installation

To install the PayU plugin for WooCommerce on CommercePro:

1. After the plugin archive is downloaded in the **ZIP** format, extract to get the integration folder. For the plugin location, refer to in the [Plugin location](#plugin-location) sub-section.
2. Log in to WooCommerce Dashboard.
3. Select **Plugin** from the menu on the left pane.

<Image align="center" className="border" border={true} src="https://files.readme.io/ef2e668-image.png" />

4. Click **Add New Plugin** at the top.

<Image align="center" className="border" border={true} src="https://files.readme.io/c19eca9-image.png" />

5. Click **Upload Plugin** at the top.

<Image align="center" className="border" border={true} src="https://files.readme.io/c139a3b-image.png" />

6. Click **Choose File** and select the PayU plugin from your system.

![](https://files.readme.io/cd2012a-image.png)

7. Click **Install Now**.

![](https://files.readme.io/18c8d7e-image.png)

8. Scroll down to **PayU India** plugin and select **Activate** under it.

<Image align="center" className="border" border={true} src="https://files.readme.io/9f30dbc-image.png" />

### Configuration

To configure the WooCommerce environment for PayU:

1. Select **WooCommerce** > **Settings** from the menu on the left pane.

![](https://files.readme.io/e9f734a-image.png)

2. Select the **Payment** tab.

<Image align="center" className="border" border={true} src="https://files.readme.io/b025aba-image.png" />

3. Click the **PayU Biz** toggle to enable.

<Image align="center" className="border" border={true} src="https://files.readme.io/214ab27-image.png" />

4. Click **Manage** next to PayUBiz.

<Image align="center" className="border" border={true} src="https://files.readme.io/5457ecb-image.png" />

5. Fill the details as described in the following table and click **Save Changes**:

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Enable
      </td>

      <td>
        Select **Yes**from the drop-down list to enable the plugin
      </td>
    </tr>

    <tr>
      <td>
        Checkout Experience
      </td>

      <td>
        Select **Express Checkout** from the drop-down list.
      </td>
    </tr>

    <tr>
      <td>
        Account type
      </td>

      <td>
        Select **PayUBiz** from the drop-down list for the account type.
      </td>
    </tr>

    <tr>
      <td>
        Gateway Mode
      </td>

      <td>
        Select any of the following gateway environments from the drop-down list to which customer payment details will be redirected.

        * *Sandbox:** This is the Test environment, and no actual fund transfer will take place.
        * *Production:** This is the Live environment.
        * *Note**: If you select Sandbox in Transaction Mode,  use the following credentials:
        * Merchant ID: oZ7oo9
        * Salt: UkojH5TS
      </td>
    </tr>

    <tr>
      <td>
        PayUBiz Key for Currency
      </td>

      <td>
        Enter your production account key for the Production environment.
      </td>
    </tr>

    <tr>
      <td>
        PayUBiz Salt Merchant for Currency
      </td>

      <td>
        Enter your Salt for the Production environment. For more information, refer to 

        [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

        .
      </td>
    </tr>

    <tr>
      <td>
        Verify Payment
      </td>

      <td>
        Select “Yes”. This will allow plugin to confirm status of transaction and reconcile with PayU APIs
      </td>
    </tr>

    <tr>
      <td>
        Return Page
      </td>

      <td>
        Select the page to which you want to redirect the customers after payment done:

        * .  Shop
        * .  Cart
        * .  Checkout
        * .  My Account
      </td>
    </tr>
  </tbody>
</Table>
