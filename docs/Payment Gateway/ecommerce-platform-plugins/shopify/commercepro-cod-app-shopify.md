---
title: CommercePro COD App - Shopify
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
You can accept Cash on Delivery (COD) payments for your store on Shopify and account them using the CommercePro COD app.  To install the CommercePro COD app, refer to [Install CommercePro COD App](doc:install-commercepro-checkout-app)

## Use cases

* To reduce fraud in COD orders and RTO, the app will check customers' eligibility for the COD payment mode. Only eligible customers are allowed to place orders using the COD payment option.
* If a customer is not eligible for COD, they have the option to place an order using

## Benefits

* Built-in RTO Intelligence supporting blacklisting of COD payment option based on the following parameters:
  * PIN codes
  * Specific addresses
  * Mobile numbers
  * Setting up a maximum cart amount limit for COD orders
* In-house AI model for RTO intelligence to limit COD based on multiple parameters such as cart value, user phone number, pin-code, SKUs added etc.

<Callout icon="📘" theme="info">
  **Reference**: To configure the RTO settings, refer to [Configure RTO Settings](https://docs.payu.in/docs/commercepro-cod-app-shopify/#configure-rto-settings-shopify-cod).
</Callout>

## Install CommercePro COD App

> 📘 Prerequisites
>
> * **Install PayU CommercePro App**: Ensure that PayU CommercePro app installed on the store. For more information, refer to [Install CommercePro Checkout App](doc:install-commercepro-checkout-app).
> * **Enable COD:** Before you follow this procedure, you need to contact your PayU key account manager (KAM) or Support to enable COD on your CommercePro Checkout app. For more information, navigate to the [PayU Support ](https://help.payu.in/)to raise a request.

To install CommercePro COD app:

1. Log on to your shopify store (if required).
2. Navigate to the following URL:

[https://apps.shopify.com/payu-cash-on-delivery](https://apps.shopify.com/payu-cash-on-delivery)

<Image align="center" border={true} src="https://files.readme.io/679c5b505b0b6c8e371a2dc35e7ea74a969fc73a40ccb000e6db34014411bbbc-Screenshot_2024-11-05_at_11.28.11_AM.png" className="border" />

3. Click **Install**.

  You will be redirected to PayU Account sign in page.  

4. Log in into your PayU Account using the **Email** and **Password** OR **Login using OTP** option.

   This process will connect your PayU account with ‘PayU CommercePro Checkout’ Shopify App.  

<Image align="center" border={false} width="650px" src="https://files.readme.io/66f1002-payu_in_dashboard_login.png" />

   After successfully login into your PayU account, a page similar to the following is displayed to indicate that app installation is complete and linked to your PayU account.

<Image align="center" border={true} src="https://files.readme.io/f75a7d07bbeb212fb5862962d95726da3f7485dfcc08ab1255960579f42b808c-CommercePro_COD_install_success.png" className="border" />

## Configure RTO Settings

You can configure RTO settings by configuring the amount limit for COD and blacklist/whitelist users on PayU Dashboard as described in the following sub-sections:

* [Configure amount rule](#configure-amount-rule)
* [Blacklist users](#blacklist-users)
* [Whitelist users](#whitelist-users)

### Navigate to RTO Settings

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard)
2. Select **CommercePro** from the menu on left pane.
3. Select the **Configuration** tab.

<Image align="center" border={true} src="https://files.readme.io/bb0d8d3e1f25aaecc102fd2e51c686467d43875bf5a1df8e8056586087e72035-Dashboard_CommercePro_Config_tab.png" className="border" />

1. Click **Configure Now** on the RTO Settings page.

### Configure amount rule

1. Navigate to the  _RTO Settings_ page.

The **Amount Rule** tab is displayed.

<Image align="center" border={true} src="https://files.readme.io/4381ffa6c7d65fda2f3387354f69658eef5341c5fc54f48281c8f77ec543b3e4-Dashboard_CP_RTO_Amount_Setting.png" className="border" />

2. Click the Edit button in the **Set COD amount rule** field.

The _Set COD amount rule _pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/e436f2cfb9e9a711910d853de4a7e3b0f15503139852ae40a7944245bb352f56-Dashboard_CP_RTO_Set_Amount.png" />

3. Enter the amount limit for COD transactions in the **Amount** field.
4. Click the **Save rule** button.

### Blacklist users

You can manually blacklist user by specifying there details or upload their details in  bulk.

#### Manually blacklist a user

To manually blacklist a user:

1. Navigate to the  _RTO Settings_ page.
2. Select the **Blacklist Users** tab.

<Image align="center" border={true} src="https://files.readme.io/27b004e019ed641ecb366b340af94074482fecba1898d90b5d075e0d4c7a6f36-Dashboard_CP_RTO_Blacklist_tab.png" className="border" />

3. Click the **Manually Black** button.

The _Block Customers_ pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/70244557416e1cab700be41398bc86f897fad96dbc1bfef3943105d120a4fad5-Dashboard_CP_RTO_Blacklist_Manually.png" />

4. Select any of the following options from the **Parameter** drop-down list and specify the value accordingly:
   * Mobile Number
   * PIN Code
   * Email

Based on your customer's any of the above details in Shopify records, they will blocked from using COD  or not shown while payment.

5. Click **Block associate customer**.

### Blacklist users in bulk

To blacklist users in bulk:

1. Navigate to the  _RTO Settings_ page.
2. Select the **Blacklist Users** tab.

<Image align="center" border={true} src="https://files.readme.io/27b004e019ed641ecb366b340af94074482fecba1898d90b5d075e0d4c7a6f36-Dashboard_CP_RTO_Blacklist_tab.png" className="border" />

3. Click the **Upload Blacklisted Customer** button.

   The _Upload Blacklisted Customer List_ pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/94d2e5d2630209f53f6ca7419d801974e8d2a7814732e9400c0c2cbd77786aee-Dashboard_CP_RTO_Blacklist_in_Bulk.png" />

4. Download the sample file using the **Download** button and enter the customer details to be blocked.
5. Click the **Choose file** button to upload the spreadsheet containing the blacklisted customer list.
6. Click **Upload**.

### Whitelist users

You can manually whitelist user by specifying there details or upload their details in  bulk.

#### Manually whitelist a user

To manually whitelist a user:

1. Navigate to the  _RTO Settings_ page.
2. Select the **Whitelist Users** tab.

<Image align="center" border={true} src="https://files.readme.io/8afa69f377e29ddef87b9db6e33ff39086420c49f5b8f8d31afb3673c8db4338-Dashboard_CP_RTO_Whiteist_tab.png" className="border" />

3. Click the **Manually Whitelist** button.

The _Whitelist Customers_ pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/9b6348d8a45397b1f41b88feb6c02c06b2b4fdeb3cc0572f7a84413a6547cc93-Dashboard_CP_RTO_Whiteist_manually.png" />

4. Select any of the following options from the **Parameter** drop-down list and specify the value accordingly:
   * Mobile Number
   * PIN Code
   * Email

Based on your customer's any of the above details in Shopify records, they will be whitelisted so that COD payment mode is shown while payment.

5. Click **Whitelist associate customer**.

### Whitelist users in bulk

To whitelist users in bulk:

1. Navigate to the  _RTO Settings_ page.
2. Select the **Blacklist Users** tab.

<Image align="center" border={true} src="https://files.readme.io/8afa69f377e29ddef87b9db6e33ff39086420c49f5b8f8d31afb3673c8db4338-Dashboard_CP_RTO_Whiteist_tab.png" className="border" />

3. Click the **Upload Whitelisted Customer** button.

   The _Upload Whitelisted Customer List_ pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/661d768ce2697a59ba15683e48e687e031c5742ee3c9a2e2047e519630ee65c0-Dashboard_CP_RTO_Whiteist_Bulk.png" />

4. Download the sample file using the **Download** button and enter the customer details to be whitelisted.
5. Click the **Choose file** button to upload the spreadsheet containing the whitelisted customer list.
6. Click **Upload**.

## View COD Orders

To view the COD orders done using CommercePro Checkout app:

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard)
2. Select **CommercePro** from the menu on left pane.

The **Orders** tab is displayed similar to the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/7b1d1b7c56740db5e8dfb5c01650ae06e3afeef18f3c81dd6d245578d169e7a5-Dashboard_CP_Orders_tab.png" className="border" />

3. Click any of the row on the grid to view the order details.

The order details are displayed for the selected order.

<Image align="center" border={true} src="https://files.readme.io/ac6efc00b0d6cade3d8a92131e7e09b853bfa4ad796741f3d9529a970635d4a3-Dashboard_CP_COD_Order_details.png" className="border" />

## Manage COD Orders

After your customer successfully places an COD order, you can mark it as paid or cancel the order on your Shopify Admin Dashboard. This section describes how to mark an COD order as paid or cancel the order.

### Mark an COD Order as Paid

To mark an COD order as paid:

1. Select **Orders** from the menu on left navigation pane.

   The _Orders_ page is displayed. You can look for the COD order with the "Payment pending" status under the **Payment status** column. For example, the first transaction in the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/d3013fceb1d1acb19289e6e8517a03fc71e66f8c1c70c7555ff73c994f22e88f-shopify_orders_list_COD_payment_pending.png" className="border" />

2. Open the COD order by clicking it.

   The order details are displayed.

<Image align="center" border={true} src="https://files.readme.io/48041cd46043e0b5a989ded53c82e2e19e57c26190023e8d908fb0182e37fd01-shopify_COD_order_details.png" className="border" />

3. Click the **More actions** drop-down menu and select **Open PayU Payment app** from the menu.

<Image align="center" border={true} width="350px" src="https://files.readme.io/50f4d3672bb9b99848bafb3c96389fd24185bb072404c8860f673c71dd0d5740-shopify_COD_open_payu_payment_app.png" className="border" />

The _PayU Transaction_ pop-up page is displayed.

<Image align="center" border={true} width="400px" src="https://files.readme.io/43e4834032b05bbb08f5c0d51c7871bf0baa7716672c35d743d72fe8334ab462-shopify_payu_trans_dialog.png" className="border" />

4. Select the **Mark as paid** option.
5. Click **Process**.

   The order is marked as "Paid" and it will be reflected under the **Payment status** column of the _Orders_ page.

### Cancel an COD Order

To cancel an COD order:

1. Select **Orders** from the menu on left navigation pane.

   The _Orders_ page is displayed. You can look for the COD order with the "Payment pending" status under the **Payment status** column. For example, the first transaction in the following screenshot:

<Image align="center" border={true} src="https://files.readme.io/d3013fceb1d1acb19289e6e8517a03fc71e66f8c1c70c7555ff73c994f22e88f-shopify_orders_list_COD_payment_pending.png" className="border" />

2. Open the COD order by clicking it.

   The order details are displayed.

<Image align="center" border={true} src="https://files.readme.io/48041cd46043e0b5a989ded53c82e2e19e57c26190023e8d908fb0182e37fd01-shopify_COD_order_details.png" className="border" />

3. Click the **More actions** drop-down menu and select **Open PayU Payment app** from the menu.

<Image align="center" border={true} width="350px" src="https://files.readme.io/50f4d3672bb9b99848bafb3c96389fd24185bb072404c8860f673c71dd0d5740-shopify_COD_open_payu_payment_app.png" className="border" />

The _PayU Transaction_ pop-up page is displayed.

<Image align="center" border={true} width="400px" src="https://files.readme.io/43e4834032b05bbb08f5c0d51c7871bf0baa7716672c35d743d72fe8334ab462-shopify_payu_trans_dialog.png" className="border" />

4. Select the **Cancel transaction** option.
5. Click **Process**.

The order is marked as "Cancelled" and it will be reflected under the **Payment status** column of the _Orders_ page.
