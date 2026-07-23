---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: List of APIs used for PayU Hosted Checkout Integration
  robots: index
---
| Use case → Reference                                                                                                                            | `command` / primary value                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Collect payment (redirect to PayU) — [Collect Payment API (PayU Hosted Checkout)](https://docs.payu.in/reference/_payment_payu_hosted_checkout) | Browser form `POST` to `_payment API` (see below table) |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                                      | `verify_payment`                                        |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)                | `check_action_status`                                   |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                                  | `get_transaction_info`                                  |
| Refund a transaction — [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api)                                          | `cancel_refund_transaction`                             |

> **Collect Payment endpoint:** `POST https://test.payu.in/_payment` (test) · `POST https://secure.payu.in/_payment` (production)<br />`hash`**&#x20;on&#x20;**`_payment`**&#x20;(standard sequence):** `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`<br />**Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`