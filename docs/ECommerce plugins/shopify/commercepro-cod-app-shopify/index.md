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
You can accept Cash on Delivery (COD) payments for your store on Shopify and account them using the CommercePro COD app.  To install the CommercePro COD app, refer to [Install CommercePro COD App](doc:install-commercepro-cod-app-shopify)

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
  **Reference**: To configure the RTO settings, refer to [Configure RTO Settings](doc:configure-rto-settings-shopify-cod).
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
