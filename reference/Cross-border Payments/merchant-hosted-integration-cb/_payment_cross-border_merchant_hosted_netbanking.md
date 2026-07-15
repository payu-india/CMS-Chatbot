---
api:
  file: cb_merchant_hosted_net_banking.json
  operationId: merchantHostedCheckoutNetBanking
hidden: true
---
---
title: CB - NB
api:
  file: cb_merchant_hosted_net_banking.json
  operationId: merchantHostedCheckoutNetBanking
hidden: false
link:
  new_tab: false
metadata:
  title: >-
    Collect Payment API using Net Banking - Merchant Hosted with Cross-Border
    Payments
---
PayU allows you to collect Cross-Border payments using Net Banking. Set **`pg`** to **NB** and **`bankcode`** to the PayU code for the selected bank (sandbox sample: **TESTPGNB**). The **buyer_type_business** parameter indicates the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload invoices for bank processing. AWB details are mandatory for Goods transactions.

<Callout icon="📘" theme="info">
  **Reference**: For steps to integrate Net Banking for Cross-Border Payments, refer to [NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb).
</Callout>

<PaymentAPIEnvironment />

<Accordion title="Sample Request" icon="fa-info-code">
  ```curl
  curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'txnid=xdB9G7qYpfqszo' \
  --data-urlencode 'amount=10' \
  --data-urlencode 'firstname=PayU' \
  --data-urlencode 'lastname=User' \
  --data-urlencode 'email=test@gmail.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'productinfo=iPhone' \
  --data-urlencode 'address1=123 Main Street' \
  --data-urlencode 'city=New York' \
  --data-urlencode 'state=NY' \
  --data-urlencode 'country=US' \
  --data-urlencode 'zipcode=10001' \
  --data-urlencode 'surl=https://test-payment-middleware.payu.in/simulatorResponse' \
  --data-urlencode 'furl=https://test-payment-middleware.payu.in/simulatorResponse' \
  --data-urlencode 'pg=NB' \
  --data-urlencode 'bankcode=TESTPGNB' \
  --data-urlencode 'udf1=AELPR1234E' \
  --data-urlencode 'udf3=02-02-1980' \
  --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
  --data-urlencode 'udf5=INV123456' \
  --data-urlencode 'buyer_type_business=1' \
  --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-info-reply">
  **Redirect postback** (posted to **surl** or **furl**)

  ```text
  mihpayid=403993715523409521&mode=NB&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=5jJ9xRceXX1ydT&amount=10.00&discount=0.00&net_amount_debit=10.00&addedon=2021-07-02+15%3A03%3A50&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&PG_TYPE=NB-PG&bank_ref_num=5jJ9xRceXX1ydT&bankcode=TESTPGNB&error=E000&error_Message=No+Error&hash=716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
  ```

  Verify the response **`hash`** before updating the order status. See [Generate Hash](doc:generate-hash-merchant-hosted).
</Accordion>

<Accordion title="Redirect response parameters" icon="fa-list">
  Parameters posted to **surl** or **furl** after the customer completes or abandons payment.

  | **Parameter** | **Description** |
  | --- | --- |
  | mihpayid | Unique reference number created for each transaction at PayU's end; used to identify a transaction for refunds. |
  | mode | Payment category. For net banking, the value is **NB**. |
  | bankcode | Code for the net-banking option used (for example, **TESTPGNB** in sandbox). |
  | status | Transaction status: `success`, `failure`, or `pending`. Treat `failure` and `pending` as failed for order mapping unless your integration guide specifies otherwise. |
  | unmappedstatus | Internal PayU status (for example, dropped, bounced, captured, auth, failed, usercancelled, pending). See [Payment State Explanations](ref:payment-state-explanations). |
  | key | Merchant key. |
  | error | Failure reason for failed transactions. |
  | error\_message | Error message. See [Error Codes](ref:error-codes). |
  | bank\_ref\_num | Bank reference number for successful transactions. |
  | txnid | Transaction ID posted by the merchant in the request. |
  | amount | Amount sent in the transaction request. |
  | discount | Discount amount applied by the merchant. |
  | net\_amount\_debit | Net amount debited. |
  | addedon | Transaction date and time. |
  | productinfo | Product information echoed from the request. |
  | firstname | First name echoed from the request. |
  | lastname | Last name echoed from the request. |
  | address1 | Billing address line 1 echoed from the request. |
  | address2 | Billing address line 2 echoed from the request. |
  | city | Billing city echoed from the request. |
  | state | Billing state echoed from the request. |
  | country | Billing country echoed from the request. |
  | zipcode | Billing postal code echoed from the request. |
  | email | Email echoed from the request. |
  | phone | Phone echoed from the request. |
  | hash | Response hash. Verify using PayU post-response hash rules. See [Generate Hash](doc:generate-hash-merchant-hosted). |
  | PG\_TYPE | Payment gateway used for the transaction (for example, **NB-PG**). |
  | udf1 | Echo of **udf1** from the request (buyer PAN for Cross-Border). |
  | udf2 | Echo of **udf2** from the request. |
  | udf3 | Echo of **udf3** from the request (buyer DOB for Cross-Border). |
  | udf4 | Echo of **udf4** from the request (merchant name for PA2PA). |
  | udf5 | Echo of **udf5** from the request (invoice ID). |
  | udf6 | Echo of **udf6** from the request. |
  | udf7 | Import or export code when passed via **udf_params**. |
  | udf8 | Airway bill / consignment number when passed via **udf_params**. |
  | udf9 | Echo of **udf9** from the request. |
  | field1 – field9 | Gateway-specific fields returned by the bank or PayU for the selected net-banking flow. |
  | payment\_source | Source of the payment (for example, `payu`). |
  | success\_at | Date and timestamp when the transaction succeeded. |
</Accordion>

> 🚧 Values to be used in Test environment
>
> For sandbox net-banking codes and test credentials, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets#web-checkout) and [Net Banking Codes](doc:net-banking-codes).

<TransactionStages />

<Callout icon="📘" theme="info">
  **Reference**:

  * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
  * Net-banking bank codes: [Net Banking Codes](doc:net-banking-codes).
</Callout>

<Callout icon="❗️" theme="error">
  **Error handling:** If any error message is displayed with an error code, refer to the [Error Codes](ref:error-codes) section.
</Callout>