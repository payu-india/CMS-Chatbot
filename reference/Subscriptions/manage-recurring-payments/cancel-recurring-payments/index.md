---
title: Cancel Recurring Payments
excerpt: >-
  Cancel recurring payment mandates created using NetBanking, Cards, and UPI
  with PayU APIs. Learn the cancellation flow, supported payment modes, request
  handling, and response behavior.
deprecated: false
hidden: true
metadata:
  title: >-
    Cancel Recurring Payments, recurring payment cancellation API, PayU
    recurring payments, cancel mandate API, UPI mandate cancellation, card
    mandate cancellation, NetBanking mandate cancellation, subscription
    cancellation API, recurring billing API, standing instruction cancellation,
    stop recurring debits, PayU subscription API, recurring mandate management,
    cancel auto debit mandate, PayU recurring API
  description: >-
    Cancel recurring payment mandates created using NetBanking, Cards, and UPI
    with PayU APIs. Learn the cancellation flow, supported payment modes,
    request handling, and response behavior.
  robots: index
---
The Cancel Recurring Payments API allows you to cancel active recurring payment mandates associated with a subscription or standing instruction. This API can be used to stop future debit attempts for mandates created using:

* <Anchor label="Cards of VISA or Mastercard" target="_blank" href="https://docs.payu.in/update/reference/cancel-recurring-payments-of-visa-and-mastercard-cards">Cards of VISA or Mastercard</Anchor>
* <Anchor label="Cards of AMEX or RuPay" target="_blank" href="https://docs.payu.in/update/reference/cancel-recurring-payments-of-amex-and-rupay-cards">Cards of AMEX or RuPay</Anchor>
* <Anchor label="NetBanking (NB) and UPI" target="_blank" href="https://docs.payu.in/update/reference/cancel-recurring-payments-of-netbanking-and-upi">NetBanking (NB) and UPI</Anchor>

## Common Use Cases

* Cancelling active subscriptions
* Stopping future recurring debit attempts
* Handling customer-requested mandate termination
* Deactivating recurring billing during account closure
* Managing subscription lifecycle events
