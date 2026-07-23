---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs Used for Server-to-Server Integration
  robots: index
---
---
title: APIs used for Integration
deprecated: false
hidden: false
metadata:
  title: APIs Used for Server-to-Server Integration
  robots: index
---
Use these APIs to initiate card or UPI payments from your server and manage the resulting transactions.

### Server-to-server payment flows

| Use case → Reference                                                                                                      | `command` / primary value | Description |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------- |
| S2S collect / orchestration (hub) — [Collect Payment API (S2S)](https://docs.payu.in/reference/_payment_server_to_server) | S2S API reference hub     | Lists the supported server-to-server card and UPI payment initiation references and their Try It experiences. |

### Card payment flows

| Use case → Reference                                                                                                                    | `command` / primary value | Description |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------- |
| Cards — decoupled flow — [Cards Decoupled Flow](https://docs.payu.in/reference/_payment_s2s_decoupled_flow)                             | `POST /_payment`          | Initiates a decoupled card payment so the customer can authenticate without being redirected to a bank page to enter the OTP. |
| Cards — direct authorization — [Cards Direct Authorization Flow](https://docs.payu.in/reference/_payment_s2s_direct_authorization_flow) | `POST /_payment`          | Initiates the payment request for the server-to-server direct authorization card flow. |
| Cards — classic integration — [Classic Integration (S2S)](https://docs.payu.in/reference/_payment_s2s_classic_integration)              | `POST /_payment`          | Initiates the payment request for the classic server-to-server card flow. |

### UPI payment flow

| Use case → Reference                                                                                | `command` / primary value                    | Description |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------- |
| UPI collect (S2S) — [UPI Collect (S2S)](https://docs.payu.in/reference/_payment_s2s_upi_collection) | `POST /_payment` with `txn_s2s_flow=4`       | Initiates the first step of a UPI payment through the server-to-server collection flow. |

### Transaction management

| Use case → Reference                                                                                                             | `command` / primary value      | Description |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------- |
| Verify a payment — [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                     | `verify_payment`               | Retrieves transaction status and details using the merchant transaction ID for reconciliation with PayU's database. |
| Check transaction info — [Check Action Status with PayU ID](https://docs.payu.in/reference/check_action_status_api_with_payu_id) | `check_action_status`          | Retrieves the status of capture, refund, and cancellation requests for a PayU ID. |
| Get transaction by txnid — [Get Transaction Info API](https://docs.payu.in/reference/get_transaction_info_api)                   | `get_transaction_info`         | Retrieves transaction details for an exact transaction time specified in minutes and seconds. |
| Refund a transaction — [Refund Transaction API](https://docs.payu.in/reference/refund_transaction_api)                           | `cancel_refund_transaction`    | Cancels a transaction in the `auth` state or refunds a transaction in the `captured` state. |

> **Post-service (**`command`**&#x20;APIs) endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`<br />**Post-service hash formula:** `sha512(key|command|var1|SALT)`<br />**Note:** **S2S “collect / authorize”** calls use **product-specific JSON/REST (or legacy) endpoints and signing** from the linked S2S guides — not the single `_payment` form hash row above. For **decoupled flow** integration steps (non-reference narrative), see [Decoupled Flow Integration](https://docs.payu.in/docs/integrate-with-decoupled-flow-s2s) **(Integration)**.

<br />
