---
title: PayU Hosted CB Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes how to integrate Cross-Border Subscriptions with PayU Hosted Checkout integration using **_payment** API.

## Step 1: Payment Consent Transaction using PayU Hosted Checkout

For detailed information about the Payment Consent Transaction using PayU Hosted Checkout, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).

<Callout icon="📘" theme="info">
  **Note**: For Cross-Border Payments, the UDF parameters (udf1, udf2, udf3, udf4, and udf5) have specific requirements as described in the Request parameters table below.
</Callout>

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

| Parameter                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                    |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| key<br /><code>mandatory</code>                                        | <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Your Test Key                                              |
| txnid<br /><code>mandatory</code>                                      | <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post a unique transaction ID for every new transaction. <code>Character limit</code>: 25<br /><strong>Note:</strong> Ensure this transaction ID hasn't been processed successfully before. | fd3e847h2                                                  |
| amount<br /><code>mandatory</code>                                     | <code>float</code> This parameter should contain the payment amount for the specific transaction.<br /><strong>Note:</strong> Typecast the amount to a float type. The amount can vary based on use cases:<br />• For Net Banking, 0 INR<br />• For Cards & UPI, a minimum of 1 INR (penny transactions)                                                                                                                                                                                                                                                                               | 1000                                                       |
| productinfo<br /><code>mandatory</code>                                | <code>varchar</code> A brief product description. Short information about the product/service. Character limit: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Time Magazine Subscription                                 |
| firstname<br /><code>mandatory</code>                                  | <code>varchar</code> The customer's first name.<br />Character limit is 60.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Ashish                                                     |
| email<br /><code>mandatory</code>                                      | <code>varchar</code> Contains the email of the customer; highly recommended accuracy as fraud detection relies on this. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Ashish@test.com](mailto:Ashish@test.com)                  |
| phone<br /><code>mandatory</code>                                      | <code>varchar</code> Customer phone number for fraud detection and user tracking. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 9843176540                                                 |
| address1<br /><code>mandatory</code>                                   | <code>varchar</code> The customer's primary billing address line. This field is required for billing and fraud prevention purposes. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                            |
| city<br /><code>mandatory</code>                                       | <code>varchar</code> The customer's billing city. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                               | New York                                                   |
| state<br /><code>mandatory</code>                                      | <code>varchar</code> The customer's billing state or province. This field is required for billing and fraud prevention purposes. Character limit: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                  | NY                                                         |
| country<br /><code>mandatory</code>                                    | <code>varchar</code> The customer's billing country code. This field is required for billing and fraud prevention purposes. Use ISO 3166-1 alpha-2 country codes. Character limit: 2.                                                                                                                                                                                                                                                                                                                                                                                                  | US                                                         |
| zipcode<br /><code>mandatory</code>                                    | <code>varchar</code> The customer's billing postal/zip code. This field is required for billing and fraud prevention purposes. Character limit: 20.                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10001                                                      |
| surl<br /><code>mandatory</code>                                       | <code>URL</code> The success URL to which PayU redirects after a successful transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [https://example.com/success](https://example.com/success) |
| furl<br /><code>mandatory</code>                                       | <code>URL</code> The failure URL to which PayU redirects after a failed transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [https://example.com/failure](https://example.com/failure) |
| si<br /><code>mandatory</code>                                         | <code>int</code> Signifies user consent for subscriptions. Must be 1 for a valid subscription setup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                          |
| free_trial<br /><code>optional</code>                                  | <code>int</code> Enables free trials (adjusts transaction amount to INR 0.00 for Net Banking, INR 2.00 for others).                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 1                                                          |
| udf1<br /><code>conditional</code>                                     | <code>String</code> If needed, contains the buyer's PAN. For UPI recurring, format is "Buyer's PAN\|\|Buyer's DOB". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                              | AELPR1234E or AELPR1234E\|\|02-02-1980                     |
| udf2<br /><code>optional</code>                                        | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Additional transaction data                                |
| udf3<br /><code>conditional</code>                                     | <code>String</code> Contains buyer's DOB (DD-MM-YYYY format). For UPI, format is "InvoiceID\|\|MerchantName". Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 02-02-1980 or INV-123_1231\|\|MerchantName                 |
| udf4<br /><code>mandatory<br /> for payment<br /> aggregators</code>   | <code>String</code> End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | XYZ Pvt. Ltd.                                              |
| udf5<br /><code>mandatory<br /> for cross-border<br /> payments</code> | <code>String</code> Contains invoice ID for the merchant. Character limit: 255.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | INV123456                                                  |
| hash<br /><code>mandatory</code>                                       | <code>String</code> Crucial security parameter using SHA512 hash encryption. Formula incorporates key, txnid, amount, productinfo, firstname, email, udf fields, si_details, and merchant salt.                                                                                                                                                                                                                                                                                                                                                                                        | \<Generated Hash>                                          |

<HashingRequestParameters />

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <HashingSample />
</Accordion>

<br />

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone Subscription&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&udf1=AELPR1234E&udf3=02-02-1980&udf4=XYZ Pvt. Ltd.&udf5=INV123456&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

### Sample Response

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
