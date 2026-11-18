---
title: APIs used for Integration
deprecated: true
hidden: true
icon: far fa-rectangle-api
metadata:
  title: APIs used for Merchant Hosted Integration
  robots: noindex
---
<Callout icon="🔀" theme="warn">
  **This page has moved.** The updated guide is at [Merchant Hosted Checkout APIs](../../../Low-Code%20Products/merchant-hosted-checkout/merchant-hosted-checkout-apis).
</Callout>

| Use case → Reference                                                                                                                                                            | `command` / primary value                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Collect payment (form post from browser, card/UPI/NB/etc. per mode) — [Collect Payment API (Merchant Hosted Checkout)](https://docs.payu.in/reference/_payment_merchant_hosted) | Browser form `POST` to `_payment` with mode-specific fields (`pg`, `bankcode`, card/UPI params as applicable) |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                                                      | `verify_payment`                                                                                              |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)                                                | `check_action_status`                                                                                         |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                                                                  | `get_transaction_info`                                                                                        |
| Refund a transaction — [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api)                                                                          | `cancel_refund_transaction`                                                                                   |

> **Collect Payment endpoint:** `POST https://test.payu.in/_payment` (test) · `POST https://secure.payu.in/_payment` (production)<br />`hash`**&#x20;on&#x20;**`_payment`**:** Base sequence matches hosted checkout; **card and other modes can require extended / different sequences** — follow the Merchant Hosted / mode-specific guides.<br />**Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`

<br />
