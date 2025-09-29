---
title: Understanding Refunds for Supercoins Pay
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
A refund can either be full or partial:

* **Full refund**: 100% of the amount paid is returned to your customer.
* **Partial refund** – The amount you received will be returned to the customer. Multiple partial refunds can be made until the full amount has been refunded.

| Scenario                                                       | Transaction Amount (T) | Supercoin Amount (S) | Other Instrument (I) | Refund Amount (R) | Supercoin Refund (R’) | Other instrument Refund (I’) |
| -------------------------------------------------------------- | ---------------------- | -------------------- | -------------------- | ----------------- | --------------------- | ---------------------------- |
| Part refund, less than equal to Supercoin Amount               | 1000                   | 200                  | 800                  | 150               | 150                   | 0                            |
| Part refund, more than Supercoin Amount, less than Transaction | 1000                   | 200                  | 800                  | 300               | 200                   | 100                          |

> 📘 Notes:
>
> * Flipkart Supercoins used for the transaction will be refunded before the amount used by another instrument for the transaction.
> * Instant refund is not enabled for Supercoins Pay.
>
> For more details on Refunds, refer to [Refunds](doc:introduction-refunds).
