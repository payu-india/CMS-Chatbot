---
title: Settlement APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Settlement APIs for Split Settlements
  description: ''
  robots: index
next:
  description: ''
---
The following APIs are used for releasing the settlement or get settlement details for a given date range:

* [Settlement Detail Range API](https://docs.payu.in/reference/settlement-detail-range-api): Returns transaction-level settlement details for a specified date or date range. Provides paginated results containing UTR/settlement-level summaries and individual transaction breakdowns for reconciliation purposes.
* [Transaction Details API](https://docs.payu.in/reference/settlement_transaction_details_api): Retrieves detailed information about a specific transaction using the merchant transaction ID. Returns transaction status, amounts, settlement details (UTR, date, settlement ID, settled amount), transaction type, and related metadata for inquiries, refunds, or reconciliation.
* [Merchant Upcoming and Pending Settlement API](https://docs.payu.in/reference/merchant_upcoming_settlement_api):Retrieves a merchant's upcoming and pending settlement information, providing visibility into scheduled settlement amounts and times, total pending amounts, hold status, currency, and a component-wise breakdown (sales, refunds, fees, adjustments, etc.) to help with cash-flow planning and financial forecasting.
