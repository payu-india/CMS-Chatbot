---
title: APIs used in BNPL Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in BNPL Integration
  robots: index
---
Use these APIs to check BNPL eligibility, initiate supported checkout flows, complete OTP authentication, and verify payment status.

### Eligibility checks

| Use case → Reference                                             | `command` / primary value                  | Description                                                                            |
| ---------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------- |
| [Get EMI Checkout Details API](ref:get-emi-checkout-details-api) | `GET /linkAndPay/get_emi_checkout_details` | Check BNPL Link & Pay eligibility and retrieve checkout details for supported lenders. |
| [Get Checkout Details API](ref:get_checkout_details)             | `get_checkout_details`                     | Check customer BNPL eligibility before initiating payment on merchant-hosted checkout. |

### Collect payment

| Use case → Reference                                                                       | `command` / primary value | Description                                                                                        |
| ------------------------------------------------------------------------------------------ | ------------------------- | -------------------------------------------------------------------------------------------------- |
| [Collect Payment API – BNPL (Merchant Hosted Checkout)](ref:_payment_merchant_hosted_bnpl) | `_payment`                | Submit a BNPL request with `pg=BNPL` and the provider `bankcode` on merchant-hosted checkout.      |
| [Collect Payment API – BNPL Link & Pay](ref:collect-payment-api-bnpl-link-pay)             | `_payment`                | Initiate BNPL Link & Pay transactions, including one-click repeat-user flows after wallet linking. |
| [Collect Payment API – S2S Link and Pay](ref:_payment_s2s_link_pay)                        | `_payment`                | Initiate a server-to-server BNPL Link & Pay transaction with OTP-based authentication.             |

### Submit OTP for Link & Pay

| Use case → Reference                     | `command` / primary value | Description                                                                                 |
| ---------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------- |
| [Submit OTP API](ref:submit-otp-to-payu) | Submit OTP endpoint       | Submit the customer OTP and reference ID returned by `_payment` to complete authentication. |

### Verify the payment

| Use case → Reference                         | `command` / primary value | Description                                                      |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment. |

<br />
