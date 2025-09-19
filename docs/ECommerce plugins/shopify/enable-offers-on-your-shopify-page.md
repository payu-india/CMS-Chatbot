---
title: Enable Offers on your Shopify Page
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
Offers can be displayed on your Shopify Checkout page by implementing the offers widget – which shows the customer all available offers upfront.

<Image align="center" src="https://files.readme.io/13da48c-Screenshot_2023-11-28_at_11.00.13_AM.png" />

> 📘 Note:
>
> * Offers can only be used with PayU’s hosted checkout app – “Cards, UPI, NB by PayU India”. The seamless payments app “Onsite Card Payments by PayU” currently does not support offers due to platform limitations.
> * The widget only displays the available offers, they can only be applied on PayU Hosted Checkout.  For more information on PayU Hosted Checkout, refer to [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted).

To enable the offers widget on the Shopify Dashboard:

1. Create an offer on PayU Dashboard. For more information, refer to any of the following sections: 
   * [Create an Instant Discount or Cashback Offer](doc:create-an-offer)
   * [Create a No-Cost EMI Offer](doc:create-a-no-cost-emi-offer)
   * [Create a SKU-Based Offer](doc:create-a-sku-based-offer)

2. To implement Offers widget, contact the PayU Integration team and schedule a meeting to embed the widget’s JavaScript

   After the widget is embedded, the widget will implement the offers you had configured Offers on your PayU Dashboard.

> 📘 Implementation Notes:
>
> * You need to be on the new PayU Payments app on Shopify.
> * You need to implement the Verification APIs to reconcile the transactions. For more information, refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
> * As Shopify does not consider the discounted value in the response, you should integrate the PayU APIs to fetch payment response into their backend CRM/system. For more information, refer to [Reconcile Shopify Transactions](doc:reconcile-shopify-transactions).
> * Payu recommends your to stop sending automatic emailers to your customers after placing an order. As this can be implemented automatically by PayU from backend. 
> * Refunds against these transactions cannot be triggered from Shopify Dashboard. Hence, you  need to initiate refunds for these transactions from PayU Dashboard.  For more information, refer to [Refunds for Offers](doc:refunds-for-offers).
