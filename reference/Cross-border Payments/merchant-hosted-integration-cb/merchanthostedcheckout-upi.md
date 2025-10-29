---
title: CB -UPI
api:
  file: cb_merchant_hosted_upi.json
  operationId: MerchantHostedCheckout-UPI
hidden: false
link:
  new_tab: false
metadata:
  title: 'Collect Payment API using UPI - Merchant Hosted with Cross-Border Payments '
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles). The **buyer_type_business** parameter is used for Cross Border payment transactions to indicate the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.

## Recommended prerequisite before initiating payment

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle.

Validate the VPA (UPI handle) using the **validateVpa** API. For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

## Environment

| Environment                | URL                                                                |
| :------------------------- | :----------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

<details>
  <summary>Sample request</summary>

  ```bash
  curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```plaintext
  Array
  (
      [mihpayid] => 403993715523409521
      [mode] => UPI
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => 5jJ9xRceXX1ydT
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 1000
      [addedon] => 2021-07-02 15:03:50
      [productinfo] => iPhone
      [firstname] => PayU User
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
      [field1] => vpa-anything@payu
      [field2] => 5jJ9xRceXX1ydT
      [field3] => 
      [field4] => PayU User
      [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
      [field6] => 
      [field7] => Transaction completed successfully
      [field8] => 
      [field9] => Transaction completed successfully
      [payment_source] => payu
      [PG_TYPE] => UPI-PG
      [bank_ref_num] => 5jJ9xRceXX1ydT
      [bankcode] => UPI
      [error] => E000
      [error_Message] => No Error
  )
  ```
</details>

<details>
  <summary>Response parameters</summary>
</details>

## Request parameters

<details>
  <summary>Additional info for request parameters</summary>

  ### Payment Request Parameters

  The payment request parameters include standard fields like key, txnid, amount, firstname, email, phone, and productinfo. For UPI payments, the following specific parameters are important:

  * **pg**: Set to "UPI" to indicate UPI payment method
  * **bankcode**: Set to "UPI" for UPI transactions
  * **vpa**: The Virtual Payment Address (UPI ID) of the customer

  For a comprehensive list of all parameters and their descriptions,  refer to the following:
</details>

<Callout icon="📘" theme="info">
  **Reference:** For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Callout icon="🚧" theme="warn">
  **Testing UPI:** You can test UPI only with the anything@payu or [9999999999@payu.in](mailto:9999999999@payu.in) as VPA.
</Callout>

<Callout icon="❗️" theme="error">
  **Error handling:** If any error message is displayed with an error code, refer to the [Error Codes](ref:error-codes) section to understand the reason for these error codes.
</Callout>