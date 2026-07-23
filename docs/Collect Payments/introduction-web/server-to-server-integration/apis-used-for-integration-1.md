---
title: APIs used for Integration
deprecated: false
hidden: false
metadata:
  title: APIs Used for Server-to-Server Integration
  robots: index
---
| Use case → Reference                                                                                                                    | `command` / primary value                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| S2S collect / orchestration (hub) — [Collect Payment API (S2S)](https://docs.payu.in/reference/_payment_server_to_server)               | Entry reference for **Server-to-Server** collect patterns; pair with mode-specific references below |
| Cards — decoupled flow — [Cards Decoupled Flow](https://docs.payu.in/reference/_payment_s2s_decoupled_flow)                             | Backend collect path for decoupled cards (see page for request/response and signing)                |
| Cards — direct authorization — [Cards Direct Authorization Flow](https://docs.payu.in/reference/_payment_s2s_direct_authorization_flow) | Backend collect path for direct authorization                                                       |
| Cards — classic integration — [Classic Integration (S2S)](https://docs.payu.in/reference/_payment_s2s_classic_integration)              | Legacy/classic cards S2S pattern                                                                    |
| UPI collect (S2S) — [UPI Collect (S2S)](https://docs.payu.in/reference/_payment_s2s_upi_collection)                                     | UPI collect server-to-server                                                                        |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                              | `verify_payment`                                                                                    |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id)        | `check_action_status`                                                                               |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                          | `get_transaction_info`                                                                              |
| Refund a transaction — [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api)                                  | `cancel_refund_transaction`                                                                         |

> **Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`<br />**Note:** **S2S “collect / authorize”** calls use **product-specific JSON/REST (or legacy) endpoints and signing** from the linked S2S guides — not the single `_payment` form hash row above. For **decoupled flow** integration steps (non-reference narrative), see [Decoupled Flow Integration](https://docs.payu.in/docs/integrate-with-decoupled-flow-s2s) **(Integration)**.

<br />
