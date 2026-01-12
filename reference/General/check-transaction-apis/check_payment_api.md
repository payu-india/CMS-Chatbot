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

<Accordion title="My Accordion Title" icon="fa-info-circle">
  ```curl
curl --location 'https://secure.payu.in/merchant/postservice' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=6i6633s3gknq1kvph6dtijoabu; USERTXNINFO=68ed4df291d9b7.27710642' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'command=get_TDR' \
--data-urlencode 'var1="25779819010"' \
--data-urlencode 'hash=9ba8c5c14b1d8643053b121ce7beb556b1e81fe7f4685048008bcc9f81a35f2b03f879704c10e0999e84923701219fc507c53a57c5ea8ff033ccd4148fb3366c' \
--data-urlencode 'form=2'
```
</Accordion>

<Accordion title="My Accordion Title" icon="fa-info-circle">
  ```
{
    "status": 1,
    "msg": "Transaction Fetched Successfully",
    "transaction_details": {
        "mihpayid": "Not Found",
        "status": "Not Found"
    }
}
  ```

</Accordion>

## Request parameters

<Accordion title="Reference information for request parameters" icon="fa-book">
  <KeyHashForGeneralParametersDescription />
</Accordion>

**Sample values**

Use the following sample values while trying out the API:

* `var1` (your transaction ID/order ID): 403993715521889530
