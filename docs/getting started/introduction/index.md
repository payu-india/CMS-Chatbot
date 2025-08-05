---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - checkout integration
    - ' API reference'
    - ' payment gateway API integration'
    - ' payment aggregator API integration'
    - ' payment gateway integration'
    - ' UPI payment integration'
    - ' card payment integration'
    - ' NetBanking integration'
  robots: index
next:
  description: ''
---
PayU offers multiple payment workflows suitable for your online payment collection and disbursement strategy with diverse requirements and operational realities. Your website’s payment workflow is an integral part of your customer’s shopping experience. After the customer adds the products to the shopping cart on your website and checkout, you need to offer various payment modes to make the shopping experience complete.

# What is a payment gateway?

A payment gateway is a technology used by merchants to accept debit or credit card, UPI, wallets, EMI, etc. For purchases made by customers.

# Benefits

* Safer, faster, smoother transactions that give customers peace of mind.
* Secure and protect customers from frauds.
* Improves user experience, saves time, and empowers your customers.
* Enables you to accept multiple payment types and cards securely
* Reduces declined payments with real time transactions.

# PayU offerings

* Web Checkout: For more information, refer to any of the following based on your integration:
  * [PayU Hosted Checkout](doc:prebuilt-checkout-payu-hosted)
  * [Merchant Hosted Checkout](doc:custom-checkout-merchant-hosted)
  * [Server-to-Server](doc:server-to-server-integration)
  * [CommercePro Checkout](doc:checkout-express)
  * [Checkout Plus](doc:checkout-plus-integration)
* Mobile SDK: For more information, refer to any of the following based on your integration:
  * [Explore Android SDKs](doc:explore-android-sdks)
  * [Explore iOS SDKs](doc:explore-ios-sdks)
  * [Explore React Native SDKs](doc:explore-reactnative-sdks)
  * [Explore Flutter SDKs](doc:flutter-sdk-introduction)
  * [Explore Cordova CheckoutPro SDK](doc:cordova-sdk-introduction)
* eCommerce Plugins: For more information, refer to  [Plugins - Introduction](https://docs.payu.in/docs/ecommerce-platform-plugins/)
* Partner Integration: For more information, refer to [Partner - Introduction](https://docs.payu.in/docs/payu-partner-program-overview#/)
* Payouts: For more information, refer to [Payouts - Introduction](https://docs.payu.in/docs/introduction-to-payouts/)

> 📘 Notes:
>
> PayU recommends you to:
>
> * Understand the product integration steps on this **Integration Guide** and later refer to [API Reference](ref:introduction-api-reference).
> * The [API Reference](ref:introduction-api-reference) pages for various APIs allows you to make mock API calls with most of the PayU APIs (using a static test key for General or Integration APIs).  Also, it provides support in 16 language bindings, so you can get the source code in apart from cURL.
> * PayU recommends you to integrate with Test environment initially for all the integration before you go live to Production enviroment.
> * It is recommended to follow the **Integration Checklist** for checkout or SDK integrations to ensure that your integration is complete before making your integration live.
>
>

## Developer resources

* **Merchant Key and Salt**:  Before starting your integration, check your key and salt in the Dashboard. For more information, refer to:
  * [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
  * [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* **Test Card, UPI, Wallet, etc**:  For the card, EMI, UPI, wallet, BNPL details to test the integration, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

## Get support

Our dedicated support team is here to assist you if you encounter any issues or have questions during your integration process. Visit [https://help.payu.in](https://help.payu.in) and raise a ticket.