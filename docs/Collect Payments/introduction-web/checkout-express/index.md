---
title: CommercePro Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - No Form Filling
    - Pre-fill Address
    - Payment Reminders
    - Quick Checkout
  robots: index
next:
  description: ''
---
PayU CommercePro Checkout provides a comprehensive checkout solution for your business. It helps minimize the COD RTO by analyzing customer shopping history and address quality. It allows your customers to securely save their payment details and addresses and use them across PayU network businesses. PayU CommercePro Checkout optimizes your checkout experience end-to-end by configuring the PayU offer engine and the PayU recommendation engine for your website/app checkout page.

<Callout icon="📘" theme="info">
  ###

  **Enable CommercePro Checkout**: If Checkout Express is not enabled, contact your PayU Key Account Manager (KAM) or click **Help** at the top-right corner of PayU Dashboard to raise a ticket with PayU Support.
</Callout>

## Features:

- **No form filling:** Enable 2-step login with phone number and OTP. PayU will save customers' information and pre-fill it in subsequent transactions.
- **Pre-fill address:** Pre-fill addresses for first-time users from a database of 15.5 million+, making the journey similar to that of repeat customers.
- **Offer COD via PayU PG:** Offer COD as a payment option for customers unwilling to use or without access to digital payment methods.
- **Payment Reminders** — Automate sending payment links via WhatsApp whenever a customer drops off during checkout/if payment fails.
- **Offer engine** — Out of the box offer engine that you can configure and run to drive customer loyalty and conversions
- **Recommendation Engine** — Personalize the checkout experience by recommending payment options and reduce drop-offs.

## Supported platforms

PayU supports CommercePro on the following platforms:

- **WooCommerce**: Refer to [CommercePro Checkout for WooCommerce](doc:commercepro-platform-for-woocommerce) for installation and configuration.
- **Magento**: Refer to [CommercePro Checkout for Magento](doc:commercepro-platform-for-magento)for installation and configuration.
- **Website**: Refer to [CommercePro Checkout](doc:checkout-express) for integration using any of the following:
  - [Response Handler](https://docs.payu.in/docs/integration-checkout-express-response-handler)
  - [Callback URL](https://docs.payu.in/docs/integrate-commercepro-checkout-using-callback-url)

## Customer journey

1. Customer clicks the **Buy Now** button on your website checkout page.


<Image src="https://files.readme.io/7ae8946-1.png" align="center" />


2. The PayU CommercePro Checkout page opens. The order summary, delivery address, and offers are displayed on the checkout page.


<Image src="https://files.readme.io/b6a26b3-2.webp" align="center" />


2. Your customer selects a delivery adresss.


<Image src="https://files.readme.io/01ad51a-3.png" align="center" />


4. Your customer can select offers from the offers and coupon section.


<Image src="https://files.readme.io/0c74435-4.png" align="center" />


5. Your customer selects the payment mode to proceed with the payment.


<Image src="https://files.readme.io/41e1527-5.png" align="center" />


<br />

## APIs Used for Integration

| Use case → Reference                                                                                                                                                                                                                       | Integration surface / next step                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Enable CommercePro — [CommercePro Checkout](https://docs.payu.in/docs/checkout-express) **(Integration)**                                                                                                                                  | PayU Dashboard **Help** ticket **or** your **PayU Key Account Manager (KAM)**                |
| Website: handle return data — [Integrate CommercePro Checkout using Response Handler](https://docs.payu.in/docs/integration-checkout-express-response-handler) **(Integration)**                                                           | **Response Handler** integration path                                                        |
| Website: server callback — [Integrate CommercePro Checkout using Callback URL](https://docs.payu.in/docs/integrate-commercepro-checkout-using-callback-url) **(Integration)**                                                              | **Callback URL** integration path                                                            |
| Confirm payment server-side (typical PG follow-up) — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                                                                               | Same post-service flow as other checkouts: `verify_payment` (and related commands as needed) |
| Store platform — [CommercePro Checkout for WooCommerce](https://docs.payu.in/docs/commercepro-platform-for-woocommerce) / [CommercePro Checkout for Magento](https://docs.payu.in/docs/commercepro-platform-for-magento) **(Integration)** | **WooCommerce** or **Magento** plugin/docs (linked from the overview)                        |

> **Note:** CommercePro is an end-to-end checkout product (offers, addresses, COD, etc.). **Collect/verify API details are on the linked implementation guides**, not summarized as one `_payment` / `command` row on the overview alone.

<br />
