---
title: Steps to Integrate - Import
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
You can integrate Cross-Border Payments for the following:

* [Integrate Cross-Border Payments for Payments OS](doc:integrate-cross-border-payments-for-payments-os)
* [Integrate Cross-Border Payments for PayUBiz](doc:integrate-cross-border-payments-for-payubiz)

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

The integration for Payments OS or PayUBiz requires the following:

* **Invoice ID**: The Invoice ID needs to be shared with the AD-1 category bank on the same day of the transaction to initiate settlements with the merchant. Hence, if the Invoice ID is not available at the time of the transaction, it is mandatory to be passed through the UDF Update API or Invoice Upload API on the same day (IST). If the merchant fails to furnish the invoice ID on the same day (IST) of the transaction through any of the three options, PayU or the Partner Bank will not be able to process the settlement. For more information on **UDF Update** API and **Invoice Upload** API, refer to [UDF Update API](ref:udf_update_api) and [Invoice Upload API](ref:invoice_upload_api).
* **Invoice file**: The invoice file must be shared with PayU within 10 days of transaction since the bank requires the same as per the Govt and RBI guidelines. To follow the guidelines – PayU’s system will create an auto-refund entry to the buyer if the Invoice file is not received within 10 days. Merchant can configure the 10 days window on a merchant *MID* level. 

> 📘 Note:
>
> The recommended solution is to pass both the Invoice ID and Invoice file simultaneously when hitting the Invoice Upload API on the same day of the transaction.