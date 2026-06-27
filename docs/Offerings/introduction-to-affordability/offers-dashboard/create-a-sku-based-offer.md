---
title: Create a SKU-Based Offer
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - PayU India SKU-Based Offer
    - PayU India Stock Keeping Units-Based Offer
    - SKU-Based Offer Setup
    - SKU-Based Offer for PayU India Checkout Integration
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: configure-sku-based-offers-shopify
      title: Configure SKU-Based Offers Shopify
    - type: basic
      slug: >-
        collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration
      title: SKU-Based Offer using Merchant Hosted Checkout
---
PayU allows merchants to create offers for specific Products/SKUs in the cart. These offers will be shown only when the specific product is added by the user and hence can be used by the merchant to promote specific products.

**Example**: A merchant has created offer 1 on mobile and offer 2 on watch. During checkout, the following will be shown for a user on the merchant store page:

- If the cart has Smartphone, offer 1 (SKU ID is smartphone234) would show up for the user.  
- If the cart has an Smartwatch132, offer 2 (SKU ID is smartwatch) would show up for the user.
- If the cart has both mobile and watch, both offer 1 and offer 2 would show up and user will be able to apply both the offers.

The procedure to add SKU-based offer include some extra steps when you provide the basic details about the offer. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer).

After you create a SKU-based offer, you can collect payments from your customers using PayU Hosted (Non-seamless) or Merchant Hosted (Seamless) Checkout integration. For more information, refer to [SKU-Based Offer using Merchant Hosted Checkout](doc:collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration).

To include the SKU-based offer details along with the basic details of the offer:

1. Navigate to the **Offer Usage Guidelines** section of the _Set Offer Rules_ page.
2. Select the **Apply offer on specific SKUs on Product Categories** check box to enable SKUs.

The **SKU** and **Category** tabs are displayed.


<Image src="https://files.readme.io/a40c1a6b79b2be544786339d3728138f8162d7a9220bc8a7f734a54bbcf0c7d6-Screenshot_2025-06-05_at_10.31.31_AM.png" align="center" border={true} />


3. Click **Download** next to **Sample File** if you are not having the XLSX sample file template for SKUs.The XLSX file contains some sample product details, which you need to update according to your requirements.  

   The sample Excel file contains the columns similar to the following screenshot:


   <Image src="https://files.readme.io/a04a4c787297c959fa199842091e5228e9a72160384501b99b8b7251652dc1d1-Screenshot_2025-06-05_at_10.35.33_AM.png" align="center" border={true} />


   The sample Excel file contains the following columns and the values for the **Product ID** column is mandatory:

   <Callout icon="📘" theme="info">
     ### Note:

     The **Product ID** in this Excel file and the **skuId** request parameter used in the PayU Hosted or Merchant Hosted Checkout Integration for SKU-based offer have the same function, Hence, after you create Product IDs on Dashboard, use them as values for the **skuId** parameter. For more information on Merchant Hosted Checkout Integration for SKU-based offer, refer to [Integrate with PayU Hosted Checkout](doc:payu-hosted-checkout-integration-with-offers) or [Instant Discount or Cashback using Merchant Hosted Checkout](doc:instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout).
   </Callout>

   - **Product ID**: The unique product identifier for the product that you wish to apply the SKU-based offer.
   - **Product Name**: The name of the product for which you wish to apply the SKU-based offer.
   - **Min Amount**: For a customer, the minimum amount for which the SKU-based offer is applicable for this product.
   - **Max Amount**: For a customer, the maximum amount for which the SKU-based offer is applicable for this product.
   - **Min Quantity**: The minimum quantity of the product that a customer must order to avail the SKU-based offer.
   - **Max Quantity**: The maximum quantity of the product that a customer can order to avail the SKU-based offer.
4. Update the CSV or text file to include the SKU details. For updating the XLSX file, you can use Microsoft Excel or any other Spreadsheet tool. 
5. Click **Select file from your library** and select the CSV or text file.
6. Select any of the following options in the **In case of multiple quantity of same product** field:

- **Apply offer once**: Select this option to apply the offer only once for multiple quantity of the same product.
- **Apply many times**: Select this option to apply the offer many times for multiple quantity of the same product.

7. Click **Next**.
8. Enter the subvention details in the _Subvention Details_ page. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer#step-4-configure-offer-subvention-details).
9. After you complete the above details in the _Subvention Details_ page and click **Next**.
10. Check the preview page and click **Publish**.

<br />
