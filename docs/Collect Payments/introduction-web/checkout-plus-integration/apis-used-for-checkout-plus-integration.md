---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for Checkout Plus Integration
  robots: index
---
| Use case → Reference                                                                                                                                 | `command` / primary value                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Prerequisite — [PayU Hosted Checkout](https://docs.payu.in/docs/prebuilt-checkout-payu-hosted) **(Integration)**                                     | **PayU Hosted Checkout** must be available/enabled for the merchant (Checkout Plus is an add-on UX)                                |
| Embed Checkout Plus (modal) — [Integrate Checkout Plus](https://docs.payu.in/docs/integrate-checkout-plus) **(Integration)**                         | Same as hosted: browser flow to `_payment`, presented **inside a PayU-served modal** on your site (see full guide for snippet/SDK) |
| Collect payment (underlying PG request) — [Collect Payment API (PayU Hosted Checkout)](https://docs.payu.in/reference/_payment_payu_hosted_checkout) | Form `POST` to `_payment` parameters as for hosted checkout (modal wraps this flow)                                                |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                           | `verify_payment`                                                                                                                   |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)                     | `check_action_status`                                                                                                              |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                                       | `get_transaction_info`                                                                                                             |

> **Collect Payment endpoint:** Same `_payment` URLs as **PayU Hosted Checkout** (modal wraps the hosted experience).<br />`hash`**&#x20;on&#x20;**`_payment`**:** Same family as hosted **unless** the Checkout Plus guide specifies additional fields — follow the Checkout Plus integration doc.<br />**Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`

<br />