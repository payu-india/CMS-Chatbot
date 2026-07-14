---
title: PayU Hosted Payment Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes how to integrate Cross-Border Subscriptions with PayU Hosted Checkout integration using **_payment** API. This integration following steps:

<Cards columns={3}>
  <Card title="1. Post the Payment Request with PayU" href="#step-1-post-the-payment-request-with-payu">
    Post the payment parameters to PayU's \_payment API with required UDFs for cross-border.

    <br />
  </Card>

  <Card title="2. Check Response from PayU" href="#step-2-check-response-from-payu">
    Handle the URL-format response from PayU and validate using reverse hashing.

    <br />
  </Card>

  <Card title="3. Verify the Payment" href="#step-3-verify-the-payment">
    Reconcile and validate transaction details using verification methods.
  </Card>

  <Card title="4. Update Invoice ID (Conditional)" href="#step-4-update-invoice-id-conditional">
    Update the invoice ID associated with the transaction

    <br />
  </Card>

  <Card title="5. Upload the Invoices / Shipping Document (Conditional)" href="#step-5-upload-the-invoices-optional">
    Upload invoice documents related to the completed transaction
  </Card>
</Cards>

## Step 1: Post the Payment Request with PayU

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

<Accordion title="Request parameters" icon="fa-table">
  In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

 | Parameter | Description | Example |
|---|---|---|
| key<br/><code>mandatory</code> | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account. | Your Test Key |
| txnid<br/><code>mandatory</code> | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br/>**Note:** Ensure this transaction ID hasn't been processed successfully before. | fd3e847h2 |
| amount<br/><code>mandatory</code> | <code>float</code> This parameter should contain the payment amount for the specific transaction.<br/>**Note:** Typecast the amount to a float type. The amount can vary based on use cases:<br/>• For Net Banking, 0 INR<br/>• For Cards & UPI, a minimum of 1 INR (penny transactions) | 1000 |
| productinfo<br/><code>mandatory</code> | <code>varchar</code> Name or brief description of the goods/services being sold. In case of physical goods, please include name / description of all products. Character limit: 100. | Time Magazine Subscription |
| email<br/><code>mandatory</code> | <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50. | Ashish@test.com |
| firstname<br/><code>mandatory</code> | <code>varchar</code> The customer's first name. Character limit is 60. | John |
| lastname<br/><code>mandatory</code> | <code>varchar</code> The customer's middle & last name (wherever applicable). Character limit is 60. | Doe |
| phone<br/><code>optional</code> | <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50. | 9843176540 |
| address1<br/><code>optional but recommended for higher approval rate</code> | <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255. | 123 Main Street |
| address2<br/><code>optional</code> | <code>varchar</code> The customer's secondary billing address line. Character limit: 255. | Anytown |
| city<br/><code>optional but recommended for higher approval rate</code> | <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50. | New Delhi |
| state<br/><code>optional but recommended for higher approval rate</code> | <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50. | Delhi |
| country<br/><code>optional but recommended for higher approval rate</code> | <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2. | India |
| zipcode<br/><code>mandatory</code> | <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 6 digit (India Zipcode). | 110075 |
| surl<br/><code>mandatory</code> | <code>URL</code> The success URL to which PayU redirects after a successful transaction. | https://example.com/success |
| furl<br/><code>mandatory</code> | <code>URL</code> The failure URL to which PayU redirects after a failed transaction. | https://example.com/failure |
| udf1<br/><code>optional but recommended for higher approval rate</code> | <code>String</code> The Permanent Account Number (PAN primary taxation ID in India) of the buyer must be collected in this field. Character limit: 10 character alphanumeric. | ABCDE1234K |
| udf2<br/><code>optional</code> | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255. | Additional transaction data |
| udf3<br/><code>optional but recommended for higher approval rate</code> | <code>String</code> Date of Birth (DOB) of buyer in DD-MM-YYYY. | 02-02-1980 |
| udf4<br/><code>mandatory for payment aggregators</code> | <code>String</code> End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255. | XYZ Pvt. Ltd. |
| udf5<br/><code>mandatory</code> | <code>String</code> Contains invoice ID for the transaction. Invoice ID / number should be the ID present on the invoice issued to the customer. Character limit: 255. | INV123456 |
| buyer_type_business<br/><code>optional in case of B2B transaction for cross-border payments</code> | <code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br/>**Note:** This will be included in hash if posted (covered in next section). | 1 |
| udf_params<br/><code>optional</code> | <code>String JSON</code> UDF7 value to capture "Import or Export Code" of the buyer. UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports). | {"udf7":"0100000029","udf8":"99953729071"} |
| hash<br/><code>mandatory</code> | <code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt. | \<Generated Hash> |

  #### Hashing

  <PACB_Hashing />

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
  ```

  * **Case4 example**: if the merchant wants to pass the api\_version = 7 and buyer\_type\_business, udf\_params in the payment request.

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
  ```

  <Callout icon="📘" theme="info">
    **Reference:** PayU recommends you to use PayU Hash Verification Tool to verify the hashing. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool)
  </Callout>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JPM7Fg&txnid=payuTestTxn12345&amount=100.00&productinfo=iPhone&firstname=Ashish&lastname=Kumar&email=test@gmail.com&phone=9876543210&zipcode=110075&surl=https://example.com/success&furl=https://example.com/failure&udf1=AELPR1234E&udf3=02-02-1980&udf4=XYZ Pvt. Ltd.&udf5=INV123456&buyer_type_business=1&udf_params={\"udf7\":\"<IE_CODE>\",\"udf8\":\"<AWB Num>\"}&hash=<generated_hash>"
  ```
</Accordion>

***

## Step 2: Check Response from PayU

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded). You must implement the reverse hashing as described in the following:

<ReverseHashing />

<br />

<Accordion title="Sample response" icon="fa-reply">
  **Parsed response**

  ```json
  Array
  (
      [mihpayid] => 403993715525331373
      [mode] => ENACH
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => oRWSUMU4XSQBZn
      [amount] => 100.00
      [discount] => 0.00
      [net_amount_debit] => 0
      [addedon] => 2022-02-03 19:06:55
      [productinfo] => iPhone Subscription
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
      [udf1] => AELPR1234E
      [udf2] => 
      [udf3] => 02-02-1980
      [udf4] => XYZ Pvt. Ltd.
      [udf5] => INV123456
      [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
      [field1] => ENACH285259747472911093
      [field2] => 337026657857179355
      [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
      [payment_source] => sist
      [PG_TYPE] => ENACH-PG
      [bank_ref_num] => 450699821592111537
      [bankcode] => ICICENCC
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

***

## Step 3: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

***

## Step 4: Update Invoice ID [Conditional]

<Update_Invoice_ID />

***

## Step 5: Upload the Invoices [Optional]

<Upload_Invoices />