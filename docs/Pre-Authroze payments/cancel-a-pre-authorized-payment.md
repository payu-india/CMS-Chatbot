---
title: Cancel a Pre-Authorized Payment
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
You can cancel a pre-authorized payment or refund. This command can be used for two different purposes:

* To cancel a transaction which is in **auth** state at the moment
* To refund a transaction which is in **captured** state at the moment.

> 📘 Note:
>
> If transaction is in the **auth** state, you can make full cancellation and not partial cancellation. For partial cancellation, you have to capture the amount and the remaining amount will get auto released.

You need to use the **cancel\_refund\_transaction** API to cancel the pre-authorized payment. For more information on **cancel\_refund\_transaction** API, refer to [Refund Transaction API](ref:refund_transaction_api).
