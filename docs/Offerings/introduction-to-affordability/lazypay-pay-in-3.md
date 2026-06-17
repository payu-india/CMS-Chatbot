---
title: LazyPay Pay-in-3
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

**Merchant hosted checkout** means you collect order and customer details on your website or app, then post a form or server-side request to PayU’s **`/_payment`** endpoint. PayU processes the LazyPay leg of the journey and returns the customer to your **`surl`** / **`furl`** with a signed response. **Lazy Pay in 3** merchants also use **[Get Checkout Details](ref:get_checkout_details)** (same **`hash`** formula as that reference) before **Get EMI / BNPL checkout details**, per your **v1** pack.

This section is **LazyPay-specific** and uses **Get EMI / BNPL checkout details** for eligibility. For the **generic** merchant-hosted BNPL flow that starts from **Get Checkout Details**, see [Merchant Hosted BNPL Workflow](doc:general-flow-bnpl-integration-with-merchant-hosted). For PayU-hosted checkout (customer pays on PayU’s page), see [PayU Hosted Checkout BNPL Workflow](doc:bnpl-workflow-payu-hosted-checkout).


## Benefits for your customers

* Pay later with LazyPay on eligible purchases, subject to lender rules and approval.
* **Lazy Pay in 3:** when offered, customers pay in **three equal** instalments at **0%** interest, with instalment dates/amounts available from checkout APIs for disclosure on your page.
* Checkout stays on your experience (no full redirect to a separate PayU payment page for the whole journey).
* Eligibility can be checked up front so LazyPay is shown only when the customer can use it.

## Benefits for your business

* You control layout, fields, and when to surface LazyPay (based on eligibility API responses).
* Standard PayU **hash**, **redirect**, and **verification** patterns apply, consistent with other merchant-hosted modes.
* You can align LazyPay with your wider BNPL or affordability strategy using the same PayU keys and reconciliation tools.

## Lazy Pay-in-3 integration

Refer to to 