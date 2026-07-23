---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for CommercePro Checkout Integration
  robots: index
---
---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for CommercePro Checkout Integration
  robots: index
---
Use these references to enable CommercePro and select the integration journey for your website or ecommerce platform.

### Website integration

| Use case → Reference                                                                                                                                                                             | `command` / primary value                                      | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------- |
| Enable CommercePro — [CommercePro Checkout](https://docs.payu.in/docs/checkout-express) **(Integration)**                                                                                        | PayU Dashboard **Help** ticket or PayU Key Account Manager (KAM) | Enables CommercePro Checkout so you can use its address, offer, recommendation, and payment capabilities. |
| Website: handle return data — [Integrate CommercePro Checkout using Response Handler](https://docs.payu.in/docs/integration-checkout-express-response-handler) **(Integration)**                  | `bolt.launch()` with `responseHandler()`                       | Loads the PayU JavaScript SDK, launches CommercePro, and returns the completed payment response to a handler on your page. |
| Website: server callback — [Integrate CommercePro Checkout using Callback URL](https://docs.payu.in/docs/integrate-commercepro-checkout-using-callback-url) **(Integration)**                     | `bolt.launch()` with a callback URL                            | Loads the PayU JavaScript SDK, launches CommercePro, and sends the payment response to your configured callback URL. |

### Payment verification

| Use case → Reference                                                                                                         | `command` / primary value | Description |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------- |
| Confirm payment server-side (typical PG follow-up) — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api) | `verify_payment`          | Retrieves transaction status and details using the merchant transaction ID for reconciliation with PayU's database. |

### Ecommerce platform integrations

| Use case → Reference                                                                                                                                                                                                                       | `command` / primary value | Description |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- | ----------- |
| Store platform — [CommercePro Checkout for WooCommerce](https://docs.payu.in/docs/commercepro-platform-for-woocommerce) / [CommercePro Checkout for Magento](https://docs.payu.in/docs/commercepro-platform-for-magento) **(Integration)** | WooCommerce or Magento    | Provides the platform-specific installation and configuration steps for adding CommercePro Checkout to a WooCommerce or Magento store. |

> **Note:** CommercePro is an end-to-end checkout product (offers, addresses, COD, etc.). **Collect/verify API details are on the linked implementation guides**, not summarized as one `_payment` / `command` row on the overview alone.

<br />