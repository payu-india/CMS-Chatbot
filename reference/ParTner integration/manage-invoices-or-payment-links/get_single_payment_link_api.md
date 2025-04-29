---
title: Get Single Payment Link API
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: ReadInvoiceAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to get a single payment link using the payment link invoice number.

The invoice number in the request header must be included as a query parameter in the **invoice_number** field.

> 📘 Note:
> 
> The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:user-token-apis).

### Environment

|                            |                             |
| :------------------------- | :-------------------------- |
| **Test Environment**       | &lt;https://uatoneapi.payu.in&gt; |
| **Production Environment** | &lt;https://oneapi.payu.in&gt;    |