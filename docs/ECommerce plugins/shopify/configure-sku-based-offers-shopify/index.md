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

1. Download SKUs IDs from Shopify. For more information, refer to [Download SKUs IDs from Shopify](doc:download-skus-ids-from-shopify).
2. Create any SKU based offer on PayU dashboard. For more information, refer to [Create a SKU-Based Offer](doc:create-a-sku-based-offer). 

> 📘 Note:
>
> Ensure that the **Product ID** column of the Excel file containing offer details (that you will be uploading in PayU Dashboard) is the same as in Shopify’s SKU (Stock Keeping Unit).

<Image align="center" className="border" border={true} src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/05/Screenshot-2022-05-26-at-11.20.54-AM-875x1024.png" />

3. Configure webhooks to get the status of SKU-based offers. For more information, refer to [Configure Checkout SKU-Based Offers Webhooks](doc:configure-checkout-sku-offers-webhooks-for-shopify).
4. You can do reconciliation :
   * Integrate with **Verify Payment API** for reconciliation. For refer to [Verify Payment API](ref:verify_payment_api).
   * To manually reconcile, refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
