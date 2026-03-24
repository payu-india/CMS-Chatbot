---
title: Payment Consent Transaction with Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
---
<Callout icon="👍">
  <NewBadge title="What's New!" asHeading={false} />

  <ul><li><Anchor label="RuPay Debit and Credit Cards" target="_blank" href="https://docs.payu.in/reference/credit-card-recurring-payment-consent-transaction">RuPay Debit and Credit Cards</Anchor> are supported for Subscriptions.</li></ul>
</Callout>

Set up the recurring payment or subscription service with Merchant Hosted Checkout for the following Payment modes:

* [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)
* [Cards Recurring Payment Consent Transaction](ref:credit-card-recurring-payment-consent-transaction)
* [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)

> 📘 Note:
>
> In the case of registration transaction, the formula is used to calculate this hash is similar to the following:  
> `HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`
