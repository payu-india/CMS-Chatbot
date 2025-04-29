---
title: Merchant Hosted Integration - CB
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can use Merchant Hosted Integration integration to collect Cross Border Payments for the following payment methods:

* [Cards](https://docs.payu.in/reference/_payment_cross-border_merchant_hosted_cards)
* [UPI](https://docs.payu.in/reference/_payment_cross-border_merchant_hosted_upi)

The **buyer\_type\_business** parameter is used in \_payment for Cross Border payment transactions to indicate the type of business of the buyer. After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.
