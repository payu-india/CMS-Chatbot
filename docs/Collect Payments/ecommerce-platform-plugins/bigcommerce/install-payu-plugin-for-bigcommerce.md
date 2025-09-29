---
title: Install PayU Plugin for BigCommerce
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
You can install the PayU plugin on the BigCommerce platform quickly, and no further configuration is required.  If you encounter any issues while integration, refer to [Troubleshooting BigCommerce Integration](doc:troubleshooting-bigcommerce-integration).

## Procedure

To install the PayU plugin on your BigCommerce store:

1. Log on to your BigCommerce store account.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-31-at-11.02.45-AM-1024x686.png)

2. Perform any of the following:
   * Scroll down the page and click **Complete Setup**.
   * Select **App marketplace** under **Apps** from the menu on the left pane.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-31-at-11.02.50-AM-1024x683.png)

The **Apps** tab is displayed on the right pane.

<Image align="center" className="border" border={true} src="https://files.readme.io/8b99a2952f5823c45639df0377b9320ea263ad8a8fc23f78896acf7f28952e67-plugin-bigcommerce-apps.png" />

1. Click the **BigCommerce.com/Apps** button.

   The BigCommerce apps page is displayed in a new browser window/tab.

<Image align="center" className="border" border={true} src="https://files.readme.io/7b77799793861c5cc582b3ea4e9f3e0957b7c1328e982a6812df776b0df18768-plugin-bigcommerce-discover-apps-page.png" />

1. Select **Payment & Security** from the drop-down list and search for **PayU**.

   The **PayU** app is displayed similar to the following screenshot:

<Image align="center" src="https://files.readme.io/5d75bd991024ae4c28ad7145e448cdee19dc9ce64f097f8d2da368205d14161e-plugin-bigcommerce-select-payu-app.png" />

3. Select the **PayU** app .

   The PayU India app page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/27c6e6092ce3f26f0d1b5800a55a0e2deff7ccd1e075f4925203cac71fa77e92-plugin-bigcommerce-payu-app-page.png" />

3. Click **Get This App**.

   You are redirected to the PayU website, and a page similar to the following is displayed:

<Image align="center" className="border" border={true} width="550px" src="https://files.readme.io/41f238ef818257a0ca6d402394c632df23be24cac7911ea83550d7a4e4461d95-Screenshot_2025-04-25_at_4.39.13_PM.png" />

4. Click **Log In**.

> **Note**: If you do not have a BigCommerce store account, use the **Sign up** button and create an account.

The PayU plugin installation page similar to the following is displayed on the BigCommerce store account:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-31-at-11.27.25-AM-1024x671.png)

5. Click **Install**.

   The *PayU is requesting to update its access to your BigCommerce store page* is displayed.

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/03/Screenshot-2022-03-31-at-11.27.45-AM-1024x676.png)

6. Select the check box to acknowledge the PCI-DSS compliance.
7. Click **Confirm**.

   A page similar to the following is displayed.

<Image align="center" src="https://files.readme.io/7a9eeb2396a1e58d6a0377be331cae313ffb123047870a58b013a238a22f04c6-8f20e82eb4631d6848117ec3bb3179b387e9440e80901ca2.png" />

8. Click **Link PayU Account**.

> **Note**: If you do not have a merchant account with PayU, click the **Create New Merchant** button and create an account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

The *PayU Login* page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/fea08bdc2ae55b1ab75d12f8a468acd612b62180a54da3388cfcc2315483cee6-plugin-bigcommerce-payu-ogin.png" />

9. Log in to PayU account with the credentials.

> **Reference**: For more information on how to access the Key and Salt, refer to any of the following:

* **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)

10. Click **Login**.

<Image align="center" className="border" border={true} src="https://files.readme.io/97d0d4dffdb60a90f065a91e6dfe220b28de6edcadc43b9f1cd70738cfe4cc5e-plugin-bigcommerce-payu-acct-linking-success.png" />

The PayU India app is added to the left pane under **Apps** menu on the BigCommerce Dashboard.

<Image align="center" width="330px" src="https://files.readme.io/3e824168329df453c688946f79a8436144d7db824b6373134ac6e332066b5611-plugin-bigcommerce-payu-inida-added.png" />

10. Click **Launch**.

    The PayU *Channel List* page is displayed. The **Channel URL** column will contain your website URL.

<Image align="center" className="border" border={true} src="https://files.readme.io/3d73b6e862386aa2e60e963a06305cc545d5ea4d84d572618cc6de194cb04337-image_5.png" />

11. Click the **Enable** button to enable payments with PayU.

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a>.

The PayU payment is displayed similar to the following store screenshot for example:

<Image align="center" className="border" border={true} src="https://files.readme.io/fb3cf24222d8997fcd5ebe06f140620f9e7169ec0bf0d351cf175161489b9989-plugin-bigcommerce-sample-store.png" />