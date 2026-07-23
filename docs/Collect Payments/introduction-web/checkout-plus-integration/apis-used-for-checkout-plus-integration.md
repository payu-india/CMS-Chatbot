---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for Checkout Plus Integration
  robots: index
---
Use these references to embed Checkout Plus and manage the payments completed through its PayU-hosted modal.

### Checkout Plus setup

| Use case → Reference                                                                                                         | `command` / primary value     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Prerequisite — [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted) **(Integration)**             | PayU Hosted Checkout          | Provides the underlying hosted payment experience that must be available before you add the Checkout Plus modal.             |
| Embed Checkout Plus (modal) — [Integrate Checkout Plus](https://docs.payu.in/docs/integrate-checkout-plus) **(Integration)** | `bolt.launch(data, handlers)` | Loads the PayU inline JavaScript SDK, launches the payment modal with transaction data, and returns the result to your page. |

### Payment APIs

| Use case → Reference                                                                                                                                 | `command` / primary value         | Description                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Collect payment (underlying PG request) — [Collect Payment API (PayU Hosted Checkout)](https://docs.payu.in/reference/_payment_payu_hosted_checkout) | Browser form `POST` to `_payment` | Collects the payment through PayU Hosted Checkout, which Checkout Plus presents in a modal on your website.         |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                           | `verify_payment`                  | Retrieves transaction status and details using the merchant transaction ID for reconciliation with PayU's database. |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)                     | `check_action_status`             | Retrieves the status of capture, refund, and cancellation requests for a PayU ID.                                   |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                                       | `get_transaction_info`            | Retrieves transaction details for an exact transaction time specified in minutes and seconds.                       |

> **Collect Payment endpoint:** Same `_payment` URLs as **PayU Hosted Checkout** (modal wraps the hosted experience).<br />`hash`**&#x20;on&#x20;**`_payment`**:** Same family as hosted **unless** the Checkout Plus guide specifies additional fields — follow the Checkout Plus integration doc.<br />**Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`

<br />
