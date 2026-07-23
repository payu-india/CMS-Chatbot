---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for CommercePro Checkout Integration
  robots: index
---
| Use case → Reference                                                                                                                                                                                                                       | Integration surface / next step                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Enable CommercePro — [CommercePro Checkout](https://docs.payu.in/docs/checkout-express) **(Integration)**                                                                                                                                  | PayU Dashboard **Help** ticket **or** your **PayU Key Account Manager (KAM)**                |
| Website: handle return data — [Integrate CommercePro Checkout using Response Handler](https://docs.payu.in/docs/integration-checkout-express-response-handler) **(Integration)**                                                           | **Response Handler** integration path                                                        |
| Website: server callback — [Integrate CommercePro Checkout using Callback URL](https://docs.payu.in/docs/integrate-commercepro-checkout-using-callback-url) **(Integration)**                                                              | **Callback URL** integration path                                                            |
| Confirm payment server-side (typical PG follow-up) — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                                                                               | Same post-service flow as other checkouts: `verify_payment` (and related commands as needed) |
| Store platform — [CommercePro Checkout for WooCommerce](https://docs.payu.in/docs/commercepro-platform-for-woocommerce) / [CommercePro Checkout for Magento](https://docs.payu.in/docs/commercepro-platform-for-magento) **(Integration)** | **WooCommerce** or **Magento** plugin/docs (linked from the overview)                        |

> **Note:** CommercePro is an end-to-end checkout product (offers, addresses, COD, etc.). **Collect/verify API details are on the linked implementation guides**, not summarized as one `_payment` / `command` row on the overview alone.

<br />