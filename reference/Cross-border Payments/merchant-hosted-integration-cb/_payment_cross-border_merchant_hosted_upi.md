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

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload invoices / AWBs (Air-way bill number). AWB details are mandatory for Goods transactions.

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

  ```curl
curl --location --request POST 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JPM7Fg' \
--data-urlencode 'txnid=payuTestTransaction12345' \
--data-urlencode 'amount=100.00' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@payu.in' \
--data-urlencode 'phone=9988776655' \
--data-urlencode 'productinfo=Product Info' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=INTENT' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 's2s_client_ip=10.200.12.12' \
--data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
--data-urlencode 'udf1=AELPR1234E' \
--data-urlencode 'udf3=02-02-1980' \
--data-urlencode 'udf4=XYZ Pvt. Ltd.' \
--data-urlencode 'udf5=INV123456' \
--data-urlencode 'buyer_type_business=1' \
--data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
--data-urlencode 'hash=YOUR_CALCULATED_HASH'
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
