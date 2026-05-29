---
title: Integrations Dashboard
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Integrations Dashboard
  description: >-
    Configure PayU Dashboard plugin and platform integrations for e-commerce stores, billing tools, and third-party apps to collect payments and sync merchant data in India. Covers Integrations Dashboard.
  robots: index
  keywords:
    - payu dashboard integrations guide
    - ecommerce plugin integration payu dashboard
    - payu merchant platform integrations
    - payu dashboard zoho woocommerce integration
    - payment gateway plugin setup payu dashboard
    - payu dashboard third party integrations
    - merchant ecommerce integration payu india
    - payu dashboard online payments plugin
    - payment gateway integrations payu vs razorpay cashfree
    - payu dashboard configure gateway plugin
next:
  description: ''
---
Integrate with accounting platforms such as Tally or Zoho One to get the following functions on Dashboard:

* Quick payments by creating payouts for bulk or single bill uploads.
* Easy track of cash flow helps to eliminate the need of reconciliation.
* Approve or get approvals of the bills that are pending on a go.
* Choose hassle-free bulk payments to pay all your vendors on time.​
* Manage all your vendors at one place.​

## **Zoho Integration**

PayU payment gateway can be set up on Zoho One and Zoho Commerce.

### Zoho One

Zoho One provides an integrated system to transform your business’ disparate activities into a more connected and agile organization.

You can integrate PayU with Zoho One to collect payments from your customers, create invoices, and send it to them. The invoicing is done using [Zoho Invoice](https://devguide.payu.in/zoho/zoho-one/#Invoice). The integration with Zoho Books involves the following:

1. [Install the PayU Extension from Zoho Marketplace](http://devguide.payu.in/install-the-payu-extension-from-zoho-marketplace/)
2. [Configure PayU Extension for Zoho One](https://devguide.payu.in/zoho/zoho-one/zoho-one-integration/)

### Zoho Commerce

Zoho Commerce allows you create your online store. You can accept orders, track inventory, process payments, manage shipping, market your brand, and analyze your data using the various tools on Zoho Commerce Dashboard. Zoho Commerce provides templates to choose based on the products you will be selling so that you can quickly build your online store and start selling your products.

You can set up PayU as your payment gateway on Zoho Commerce to collect payments from your customers. To set up PayU payments on Zoho Commerce, refer to [Configure PayU Extension for Zoho Commerce](https://devguide.payu.in/configure-payu-extension-for-zoho-commerce/).

## Zoho Invoice

Zoho Invoice is an online invoicing software designed to help freelancers and small businesses with invoicing and payment collection. For more information, refer to [Zoho website](https://www.zoho.com/in/invoice/).

## **Install the PayU Extension from Zoho Marketplace**

To install the PayU extension from Zoho Marketplace:

1. Navigate to the following Zoho Marketplace website and log on using the Zoho Book credentials:

[https://marketplace.zoho.in/](https://marketplace.zoho.in/home)

The Zoho Marketplace page is displayed.

![PayU Dashboard - The Zoho Marketplace page is displayed.](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Zoho_Marketplace-1024x560.png)

1. Search for **PayU for Zoho Books** using the **Search apps** field and select it.

The *PayU for Zoho Books* page is displayed.

![PayU Dashboard - The PayU for Zoho Books page is displayed.](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Zoho_MP_PayU_for_Zoho_Books_Page-1024x560.png)### **Configure PayU Extension for Zoho One**After you [install the PayU Extension from Zoho Marketplace](http://devguide.payu.in/install-the-payu-extension-from-zoho-marketplace/), you can configure the PayU extension. This section describes the procedure to configure PayU extension and verify the set up.#### **Configure PayU Plugin**To configure PayU Plugin for Zoho One:1. Log in to your Zoho One account.\
2\. Click the **Settings** button on top right and search for “Online Payments”.![PayU Dashboard - ![PayU Dashboard - The PayU for Zoho Books page is displayed.](](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_Settings-1024x652.png)\`\`\`\
The *Customer Payments* page is displayed.

```3. Navigate to **PayU** under the **Connected Payment Gateways** section.
4. Click **Setup now** under **PayU**.

   The _Configure Gateway_ dialog box is displayed.![PayU Dashboard - Click Setup now under PayU](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Setup_PayU_for_ZohoBooks-1024x630.png)5. Enter your merchant key in the **Key** field.**Note**: You need to register or create an account on [PayU Dashboard](https://onboarding.payu.in/app/account) to get the merchant key and Salt. For viewing or generating your merchant key and Salt, refer to [Generate Merchant Key and Salt on PayU Dashboard](https://devguide.payu.in/merchant-integration/getting-started-with-web-checkout/generate-api-key-and-salt/).6. Enter your Salt in the **Salt** field.
7. Click **Save**.#### **Verify the Zoho One Integration**To verify the PayU India integration with Zoho One:1. Navigate to **Sales** > **Invoice** on Zoho One.

   The _All Invoices_ page is displayed.![PayU payment links or invoices - Click Save.#### Verify the Zoho One IntegrationTo verify the PayU India integration with Zoh](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/Zohobooks_New_Invoice_option-1024x485.png)2. Click the **New** button on the top-right corner.The _New Invoice_ page is displayed.![PayU payment links or invoices - Click Save.#### Verify the Zoho One IntegrationTo verify the PayU India integration with Zoh](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_New_Invoice-1024x457.png)1. Enter the details for the invoice. For more information, refer to [Zoho One Help Documentation](https://www.zoho.com/in/books/help/invoice/).
2. Click **Save and Send** after providing the details.

   The _Email To \<Customer Name>_ page is displayed, where \<Customer Name> is substituted with the customer name specified in Step 3. ![PayU Dashboard - Click Save and Send after providing the details](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/ZohoBooks_Email_Voucher-1024x505.png)4. Click **Send** to verify the invoice.

 
```
