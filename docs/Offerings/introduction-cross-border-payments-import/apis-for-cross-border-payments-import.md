---
title: APIs for Import Integration
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
The following APIs are used for Cross-Border Payments - Import which can be found under API Reference:

* [UDF Update API](ref:udf_update_api) is used to update the UDF1-UDF5 values of a transaction using **_payment** API.
* [Invoice Upload API](ref:invoice_upload_api) is used to collect Invoices or AWB from Cross-Border Payments merchants through upload from the Merchant Dashboard. Invoice ID and Invoice file will be passed by merchants selling software, whereas, for merchants selling goods, there will be separate requests for passing Invoice ID, Invoice file, and AWB number, AWB file.
* [Settlement Detail Range APII](ref:settlement-detail-range-api-for-cross-border): Provides transaction level data for a given date or date range or UTR. These APIs returns paginated response for the given input page and page size.
* [Get Settlement Detail API](ref:get-settlement-detail-api-cross-border-payments): Provides the settlement details.