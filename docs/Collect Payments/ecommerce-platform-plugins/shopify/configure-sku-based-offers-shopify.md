---
title: Configure SKU-Based Offers
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Configure SKU-Based Offers for Shopify
  description: ''
  keywords:
    - Configure SKU-Based Offers for Shopify
    - SKU-Based Offers for Shopify
    - Shopify SKU-Based Offers Configuration
  robots: index
next:
  description: ''
---
The following guide contains steps to configure and support **SKU based offers** on Shopify stores.  

## What is SKU-based offers

PayU allows merchants to create offers for specific Products/SKUs in the cart. These offers will be shown only when the specific product is added by the user and hence can be used by the merchant to promote specific products.

**Example**: A merchant has created offer 1 on mobile and offer 2 on watch. During checkout, the following will be shown for a user on the merchant store page:

* If the cart has Smartphone, offer 1 (SKU ID is smartphone234) would show up for the user.
* If the cart has an Smartwatch132, offer 2 (SKU ID is smartwatch) would show up for the user.
* If the cart has both mobile and watch, both offer 1 and offer 2 would show up and user will be able to apply both the offers.

For more information on how to create a SKU-based offer, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer). 

## Prerequisites

* MID status of the merchant should be **active** on PayU. 
* Merchant’s website should be on Shopify 
* Merchant should’ve installed PayU’s redirect checkout app “**Cards, UPI, NB by PayU India**” on their Shopify store 

## Steps to configure

To configure SKU-based offers on Shopify:

1. Download SKUs IDs from Shopify. For more information, refer to [Download SKUs IDs from Shopify](doc:configure-sku-based-offers-shopify#download-skus-ids-from-shopify).
2. Create any SKU based offer on PayU dashboard. For more information, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer). 

> 📘 Note:
>
> Ensure that the **Product ID** column of the Excel file containing offer details (that you will be uploading in PayU Dashboard) is the same as in Shopify’s SKU (Stock Keeping Unit).

<Image align="center" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.20.54-AM-875x1024.png" className="border" />

3. You can do reconciliation :
   * Integrate with **Verify Payment API** for reconciliation. For refer to [Verify Payment API](ref:verify_payment_api).
   * To manually reconcile, refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).

### Download SKU IDs from Shopify

To download the SKU ID’s in bulk:

1. Log in to your Shopify’s admin dashboard. 
2. Navigate to **Products**.
3. Click the **Export** button.

<Image align="center" border={false} src="https://files.readme.io/078f4b25cda29898010c779bd23702c1147a9bac797104d9358835001a3e0810-shopify_dashboard_products_export_button.png" />

4. Select **All products**.
5. Download the file using the **Export products** button.

<Image align="center" border={false} src="https://files.readme.io/5085d4262b362299f407d0940193eb12521ad7f89c6f6b30da096597b41a8d17-Screenshot_2024-10-03_at_10.12.12_AM.png" />

6. Segregate all the SKU ID’s from Shopify’s export eligible for SKU based offers and include them in the file uploaded on PayU dashboard at the time of offer configuration.

## Configure Checkout SKU-Based Offers Webhooks

This part of the document describes the procedure to configure webhooks for SKU-based offers on Shopify.

To configure webhooks for Shopify and share it with PayU support:

1. Log in to Shopify admin panel.
2. Navigate to **Settings** > **Notifications**.
3. Select **Webhooks**. 

<Image border={false} src="https://files.readme.io/e2d75bfd02c8d8e8a33f8ae23817f5ea778e4cb5b0195da27ca2f46689a5e554-shopify_webhook_select_webhooks_from_menu.png" />

4. Select **Create webhook** from the **Webhooks** page. You need to subscribe to following events:
   1. Checkout creation
   2. Checkout update

<Image align="center" border={true} src="https://files.readme.io/0b17ea589a9b6a77fc1d34510463754d4d99115743cbd5c480874156c54b699d-shopify_dashboard_click_create_webhook.png" className="border" />


5. Enter the following details in the _Add webhook_ pop-up page and then click **Save**.
   * Select **Checkout creation** from the **Event** drop-down list.
   * Select **JSON** from the **Format** drop-down list.
   * Enter the following URL in the **URL** field:  
     [https://partnerapilayer.payu.in/apilayer/shopify_app/shopifyWebhook](https://partnerapilayer.payu.in/apilayer/shopify_app/shopifyWebhook)    

<Image align="center" border={true} width="450px" src="https://files.readme.io/be6160585a76882f7018aed6b8ccdb0bb1d3023f8b808d3d58eda414f374b047-shopify_dashboard_add_webhook_page.png" className="border" />

6. Repeat Step 5 with “Checkout update” event type from the **Event** drop-down list.

<Image align="center" border={false} width="450px" src="https://files.readme.io/b5a04aaef13c494ae191bb9d83631f831c957c1a912229e570e94b2d8676673e-shopify_dashboard_webhooks_event_types.png" />

7. Copy the hash key given as under the “Your webhooks will be signed with” section at the bottom.  

<Image align="center" border={true} src="https://files.readme.io/b369535a0b7730977ace369a823ac48f0d4f28fa726c6d244ada5ccd5a1d7112-shopify_dashboard_webhooks_api_key.png" className="border" />

8. Share the following details with PayU to enable of SKU-based offers. 
   * **MID**: Your MID provided by PayU
   * **The webhook signature** : The hash key you copied in Step 7 from Shopify dashboard after creation of checkout webhooks
