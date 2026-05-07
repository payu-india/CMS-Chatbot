---
title: Payment Failed or Declined
excerpt: Debug issuer declines, bank failures, user cancellations, and payment method failures.
deprecated: false
hidden: false
metadata:
  title: Payment Failed or Declined
  description: Troubleshoot PayU failed or declined transactions using status, error codes, field7, field8, and field9.
  robots: index
next:
  description: ''
---

Payment failures occur after the customer is redirected to PayU, issuer, bank, wallet, or UPI app and the payment cannot be completed.
## Category alignment

Primary categories: Authentication and authorization errors, Payment failures, and Pending/uncertain-status errors.

## When it occurs

Typical indicators:

| Error code / type | Error message or response indicator | Recommended fix |
| --- | --- | --- |
| `status=failure` | Payment attempt failed. | Verify response hash and final status before showing retry options. |
| `unmappedstatus=failed` | Bank/issuer/PayU status maps to failed. | Treat as failed after reconciliation and create a new `txnid` for any retry. |
| `E308`, `E348`, `E500`, `E306`, `E300`, `E1000` | Common failure or decline codes. | Use the code-specific table below to decide customer retry, alternate payment method, or pending reconciliation. |
| `AUCNEGATIVE`, `AUTHNEGATIVE`, `TXNNEGATIVE`, `VERNEGATIVE` | Failed transaction stage in `field7`. | Use the field-stage table below to identify whether authentication, authorization, bank response, or verification failed. |

## Sample response

```json
{
  "mihpayid": "403993715525079998",
  "txnid": "txn_10002",
  "amount": "499.00",
  "status": "failure",
  "unmappedstatus": "failed",
  "error": "E348",
  "error_Message": "Transaction declined by the issuer",
  "PG_TYPE": "CC-PG",
  "field7": "AUTHNEGATIVE",
  "field8": "Refer to card issuer",
  "field9": "ISSUER_DECLINED",
  "bank_ref_num": "",
  "hash": "response_hash"
}
```

## Root cause

Failures are commonly caused by customer action, issuer/bank rules, payment instrument restrictions, or technical timeouts.

Examples:

* Customer entered wrong OTP/CVV.
* Customer cancelled or abandoned payment.
* Issuer declined due to risk, limits, insufficient funds, or card restrictions.
* Bank/PSP was unavailable.
* Payment method is not enabled for the merchant.

## Debugging guide

1. Verify response hash before using the payload.
2. Match `txnid`, `amount`, and `key` with your order record.
3. Read `status`, `unmappedstatus`, `error`, `error_Message`, `field7`, `field8`, and `field9`.
4. Use `field7` to identify the failed stage.
5. If failure is issuer/customer driven, show an actionable message and offer another payment method.
6. If failure is technical or timeout driven, verify final status before creating another attempt.
7. For repeated failures on one method, test another payment mode and check merchant configuration.

| Error code / type | Error message or response indicator | Description | Possible cause | Recommended fix |
| --- | --- | --- | --- | --- |
| `AUCNEGATIVE` | `field7=AUCNEGATIVE` | Authentication failed. | Incorrect OTP/3DS challenge failure, user abandonment, or issuer authentication decline. | Ask the customer to retry authentication or use another payment method after final status verification. |
| `AUTHNEGATIVE` | `field7=AUTHNEGATIVE` | Authorization failed after authentication. | Issuer declined authorization because of limits, risk, card restrictions, or insufficient funds. | Show issuer-decline guidance and offer another payment method. |
| `TXNNEGATIVE` | `field7=TXNNEGATIVE` | Bank/wallet returned failed status. | Bank, wallet, or PSP declined the transaction. | Treat as failed after hash/status verification and allow a new attempt with a new `txnid`. |
| `VERNEGATIVE` | `field7=VERNEGATIVE` | Verification confirmed failed status. | PayU verification with bank/wallet confirmed failure. | Mark the attempt failed and show retry options. |

> **Pro Tip**
>
> Do not show raw bank text directly to customers if it is unclear. Map it to a clear message such as "Your bank declined the payment. Try another card or contact your bank."

## Common failure patterns

| Pattern | Likely cause | Recommended fix |
| --- | --- | --- |
| `E306`, `E300`, `E1000`, `E317` | Authentication failure | Ask customer to retry OTP/3DS or use another card. |
| `E348`, `E307`, `E337` | Issuer declined | Ask customer to contact bank or use another payment method. |
| `E500`, `E308` | Bank authentication/processing failed | Verify final status, then allow retry. |
| `E507`, `E408` | Session/page expired | Create a new payment attempt with a new `txnid`. |
| `E1206`, `E231` | Customer interrupted or transaction dropped | Verify final status before retry. |
| `E4177`, `E4292` | Bank/PSP timeout or unavailable | Keep pending until reconciliation confirms final state. |

## Customer message examples

| PayU error type | Customer-safe message | Recommended fix |
| --- | --- | --- |
| Issuer decline | Your bank declined this payment. Try another payment method or contact your bank. | Offer alternate payment modes and do not retry the same `txnid`. |
| Authentication failure | Authentication failed. Check the OTP/CVV and try again. | Let the customer retry authentication with a new payment attempt after final status verification. |
| Timeout | We could not confirm the payment yet. Please wait while we verify the status. | Keep the order pending and reconcile through webhook or Transaction Detail APIs. |
| Card not permitted | This card is not enabled for this transaction. Try another card or payment method. | Ask the customer to use another card or enable the card with the issuer. |

## Developer checklist

* Confirm the failure is final before creating another attempt.
* Store full diagnostic fields for support and reconciliation.
* Do not retry the same `txnid` as a new payment.
* Offer alternate payment methods for customer/issuer declines.
* Use [Issuer Decline Error Codes](ref:issuer-decline-error-codes) for card decline details.
* Use [Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8) to identify the failed processing stage.

<!-- PAYU_REPO_ERRORS_PAYMENT_FAILED_DECLINED_BEGIN -->

## Repo-backed payment failure and decline errors by product

The mixed repo-backed payment-failure table has been split into product-specific sub-pages. Existing debugging guidance on this page remains unchanged.

| Product page | Rows categorized | Source docs |
| --- | ---: | --- |
| [Collect Payments payment errors](doc:payment-errors-collect-payments) | 1,673 | Collect Payment Error Codes |
| [Issuer decline errors](doc:payment-errors-issuer-declines) | 55 | Issuer Decline Error Codes |
| [Transaction stage errors](doc:payment-errors-transaction-stages) | 4 | Transaction Stages Field7/Field8 |
| [S2S Link and Pay errors](doc:payment-errors-s2s-link-and-pay) | 0 | S2S Link and Pay Error Codes |
| [Refund payment errors](doc:payment-errors-refunds) | 81 | Refund Initiation Error Codes, Refund Status Error Codes |
| [Payouts and Smart Send errors](doc:payment-errors-payouts) | 17 | Payouts Error Codes, Smart Send Error Codes |
| [Alt ID errors](doc:payment-errors-alt-id) | 8 | Alt ID Error Page |
| [BNPL payment errors](doc:payment-errors-bnpl) | 4 | BNPL Error Codes |
| [UPI QR API payment errors](doc:payment-errors-qr-apis) | 3 | QR API Error Codes |
| [CheckoutPro SDK payment errors](doc:payment-errors-checkoutpro-sdk) | 2 | CheckoutPro SDK Troubleshooting |
| [KYC and partner payment errors](doc:payment-errors-kyc) | 6 | KYC Errors and Solutions |
| [Ecommerce plugin payment errors](doc:payment-errors-ecommerce-plugins) | 13 | WooCommerce, Wix, Shopmatic, OpenCart, Magento, BigCommerce, PrestaShop troubleshooting |

Total rows categorized across product sub-pages: **1,866**.

<!-- PAYU_REPO_ERRORS_PAYMENT_FAILED_DECLINED_END -->
