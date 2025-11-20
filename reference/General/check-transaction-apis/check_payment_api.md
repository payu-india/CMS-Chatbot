---
title: Check Payment API
api:
  file: check_transaction_api.json
  operationId: CheckPaymentAPI
hidden: false
metadata:
  title: Check Payment API
  description: >-
    The Check Payment API is similar to the Verify Payment API but uses PayUID
    or mihpayuID as input instead of TxnID, and it returns all transaction
    parameters.
  keywords:
    - check_payment API Command
    - Check Payment Status API
    - Payment Checking API
    - Check Payment Status using PayU ID
    - PayU ID payment status
---
The Check Payment (**check_payment**) API functions similar to the [Verify Payment API](ref:verify_payment_api). However, the input parameter in this API is the PayUID or mihpayuID generated at PayU's Server unlike **verify_payment** API where the input parameter is the TxnID (Transaction ID generated at merchant's server). It returns all the parameters for a given transaction.

<GENERALAPIsEnvironment />

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-book">
  <KeyHashForGeneralParametersDescription />
</Accordion>

**Sample values**

Use the following sample values while trying out the API:

* `var1` (your transaction ID/order ID): 403993715521889530