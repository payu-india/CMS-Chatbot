---
title: On-Hold and Settlement APIs - Cross-Border Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
The following APIs are used for On-hold Settlement and Settlements:

## On-Hold Settlement APIs

* [Get On-Hold Transactions API](https://docs.payu.in/reference/get-on-hold-transactions-api): To retrieve a list of on-hold transactions that require additional information or action.
* [Update On-Hold Transactions API](https://docs.payu.in/reference/update-on-hold-transactions-api): To submit additional customer information required to release on-hold settlements. After successful submission, the API updates the transaction fields and triggers a settlement fallback process.

<Callout icon="📘" theme="info">
  **Reference**: For how to integrate the above APIs, refer to [On-Hold Settlement Integration for CB](doc:on-hold-settlement-integration-for-cb).
</Callout>

## Settlement APIs

* [Settlement Detail Range API](ref:settlement-detail-range-api-for-cross-border): Provides transaction level data for a given date or date range or UTR. These APIs returns paginated response for the given input page and page size.
* [Get Settlement Detail API](ref:get-settlement-detail-api-cross-border-payments): Provides the settlement details.

<br />
