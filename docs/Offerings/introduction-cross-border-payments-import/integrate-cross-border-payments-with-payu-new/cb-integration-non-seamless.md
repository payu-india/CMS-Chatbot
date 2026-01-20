---
title: '[Redirect] PayU Hosted Payment Integration - Cross Border Outward'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes how to integrate Cross-Border Subscriptions with PayU Hosted Checkout integration using **_payment** API.

## Step 1: Post the Payment Request with PayU

For detailed information about the Payment Consent Transaction using PayU Hosted Checkout, refer to [PayU Hosted Checkout - CB](ref:_payment_cross-border_payu_hosted_checkout)

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before.
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount<br /><code>mandatory</code>
      </td>

      <td>
        <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        email<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        firstname<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's first name.<br />Character limit is 60.
      </td>

      <td>
        John
      </td>
    </tr>

    <tr>
      <td>
        lastname<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's middle & last name (wherever applicable).<br />Character limit is 60.
      </td>

      <td>
        Doe
      </td>
    </tr>

    <tr>
      <td>
        phone<br /><code>optional</code>
      </td>

      <td>
        <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        address1<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.
      </td>

      <td>
        123 Main Street
      </td>
    </tr>

    <tr>
      <td>
        city<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.
      </td>

      <td>
        New Delhi
      </td>
    </tr>

    <tr>
      <td>
        state<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.
      </td>

      <td>
        Delhi
      </td>
    </tr>

    <tr>
      <td>
        country<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.
      </td>

      <td>
        India
      </td>
    </tr>

    <tr>
      <td>
        zipcode<br /><code>mandatory</code>
      </td>

      <td>
        <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 6 digit (India Zipcode)
      </td>

      <td>
        110075
      </td>
    </tr>

    <tr>
      <td>
        surl<br /><code>mandatory</code>
      </td>

      <td>
        <code>URL</code> The success URL to which PayU redirects after a successful transaction.
      </td>

      <td>
        [https://example.com/success](https://example.com/success)
      </td>
    </tr>

    <tr>
      <td>
        furl<br /><code>mandatory</code>
      </td>

      <td>
        <code>URL</code> The failure URL to which PayU redirects after a failed transaction.
      </td>

      <td>
        [https://example.com/failure](https://example.com/failure)
      </td>
    </tr>

    <tr>
      <td>
        udf1<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>String</code> The Permanent Account Number (PAN primary taxation ID in India) of the buyer must be collected in this field.

        Character limit: 10 character alphanumeric
      </td>

      <td>
        ABCDE1234K
      </td>
    </tr>

    <tr>
      <td>
        udf2<br /><code>optional</code>
      </td>

      <td>
        <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.
      </td>

      <td>
        Additional transaction data
      </td>
    </tr>

    <tr>
      <td>
        udf3<br /><code>optional but recommended for higher approval rate</code>
      </td>

      <td>
        <code>String</code> Date of Birth (DOB) of buyer in DD-MM-YYYY
      </td>

      <td>
        02-02-1980
      </td>
    </tr>

    <tr>
      <td>
        udf4<br /><code>mandatory<br /> for payment<br /> aggregators</code>
      </td>

      <td>
        <code>String</code> End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.
      </td>

      <td>
        XYZ Pvt. Ltd.
      </td>
    </tr>

    <tr>
      <td>
        udf5<br /><code>mandatory<br /> for cross-border<br /> payments</code>
      </td>

      <td>
        <code>String</code> Contains invoice ID for the merchant. Character limit: 255.
      </td>

      <td>
        INV123456
      </td>
    </tr>

    <tr>
      <td>
        buyer_type_business<br /><code>optional in case of B2B transaction<br /> for cross-border<br /> payments</code>
      </td>

      <td>
        <code>Binary</code> To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br />**Note**: This will be included in hash if posted (covered in next section).
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        udf_params<br /><code>optional</code>
      </td>

      <td>
        <code>String JSON</code>

        UDF7 value to capture "Import or Export Code" of the buyer

        UDF8 value to capture Airway Bill Number / Consignment Number (in case of goods imports)
      </td>

      <td>
        \{"udf7":"0100000029",<br />"udf8":"99953729071"}
      </td>
    </tr>

    <tr>
      <td>
        hash<br /><code>mandatory</code>
      </td>

      <td>
        <code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.
      </td>

      <td>
        \<Generated Hash>
      </td>
    </tr>
  </tbody>
</Table>

### Hashing

<PACB_Hashing />

<br />

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
```

* **Case4 example**: if the merchant wants to pass the api_version = 7 and buyer_type_business, udf_params in the payment request.

```
key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
```

For more information, refer to  <a href="generate-hash-merchant-hosted" target="_blank"> Generate Hash</a>.

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <HashingSample />
</Accordion>

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg&txnid=payuTestTxn12345&amount=100.00&productinfo=iPhone&firstname=Ashish&lastname=Kumar&email=test@gmail.com&phone=9876543210&zipcode=110075&surl=https://example.com/success&furl=https://example.com/failure&udf1=AELPR1234E&udf3=02-02-1980&udf4=XYZ Pvt. Ltd.&udf5=INV123456&buyer_type_business=1&udf_params={\"udf7\":\"<IE_CODE>\",\"udf8\":\"<AWB Num>\"}&hash=<generated_hash>"
```

## Step 2: Check Response from PayU

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

#### Parsed response

```
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

## Step 2: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

<br />
