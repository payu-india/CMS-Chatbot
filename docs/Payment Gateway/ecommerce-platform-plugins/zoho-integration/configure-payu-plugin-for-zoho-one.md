---
title: Configure PayU Plugin for Zoho One
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
Configuring PayU Plugin for Zoho One involves the following steps:

1. [Configure PayU plugin](#configure-payU-plugin)
2. [Verify the Zoho One integration](#verify-the-zoho-one-integration)

## Configure PayU plugin

To configure PayU Plugin for Zoho One:

1. Log in to your Zoho One account.
2. Click the **Settings** button on top right and search for "Online Payments".

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_Settings-1024x652.png" />

The *Customer Payments* page is displayed.

3. Navigate to **PayU** under the **Connected Payment Gateways** section.
4. Click **Setup now** under **PayU**.

   The *Configure Gateway* dialog box is displayed.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Setup_PayU_for_ZohoBooks-1024x630.png" />

5. Enter your merchant key in the **Key** field.

> **Note**: You need to register or create an account on [PayU Dashboard](https://onboarding.payu.in/app/account) to get the merchant key and Salt. For accessing your merchant key and Salt, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

6. Enter your Salt in the **Salt** field.
7. Click **Save**.

## Verify the Zoho One integration

To verify the PayU India integration with Zoho One:

1. Navigate to **Sales** > **Invoice** on Zoho One.

   The *All Invoices* page is displayed.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Zohobooks_New_Invoice_option-1024x485.png" />

2. Click the **New** button on the top-right corner.

   The *New Invoice* page is displayed.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_New_Invoice-1024x457.png" />

3. Enter the details for the invoice. For more information, refer to [Zoho One Help Documentation](https://www.zoho.com/in/books/help/invoice/).
4. Click **Save and Send** after providing the details.\
   The *Email To\<Customer Name>* page is displayed, where \<Customer Name> is substituted with the customer name specified in Step 3.

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_Email_Voucher-1024x505.png" />

5. Click **Send** to verify the invoice.
