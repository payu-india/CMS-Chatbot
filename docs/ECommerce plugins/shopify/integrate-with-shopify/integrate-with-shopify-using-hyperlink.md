---
title: Integrate with Shopify using Hyperlink
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
After you set up your account in Shopify, you can integrate PayU India as the payment platform for your customers.

## Prerequisites

* Merchant account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
* Credentials to log in to your Shopify account.
* Ensure that a store is set up on your Shopify account where you want to configure the PayU as the payment provider
* If any PayU India plugin is installed, it must be removed.

## Procedure

To integrate Shopify with PayU as a payment gateway:

1. Navigate to the following URL to open the Shopify PayU India app:

[https://apps.shopify.com/payu-india](https://apps.shopify.com/payu-india)

The PayU India app page is displayed.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/PayU_Shopify_App_page-1024x619.png" />

2. Click **Add app**.

   The Shopify Login page is displayed.

<Image align="center" width="550px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Shopify_Login_Page-796x1024.png" />

3. Enter your Shopify credentials and log in.

   The *PayU India* page is displayed.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Shopify_PayU_India_Page_Direct_Link-703x1024.png" />

4. Click **Install app**.

   The *Collect payments with PayU* page is displayed.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/08/Screenshot-2022-08-01-at-6.40.00-PM-1024x688.png" />

5. Enter your merchant key in the **Merchant Key** field.

**Note**: You need to register or create an account on [PayU Dashboard](https://onboarding.payu.in/app/account) to get the merchant key and salt. For viewing or generating your merchant key and salt, refer to [Generate Production Key and Salt on PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard).

6. Enter your Salt in the **Merchant Salt** field.
7. Scroll down and ensure the payment modes or card type you wish to support for your customers are selected. If you do not wish to support a payment mode or card type, clear the corresponding check box selection.

<Image align="center" className="border" width="550px" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Shopify_PayU_India_Page_Contd-784x1024.png" />

8. Select the **Enable Test mode** check box on the **Test mode** section to test the integration with the test key and salt provided by PayU.
9. Click **Activate PayU India**.

> 📘 Note:
>
> PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the **Verification Payment**API. For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>..
