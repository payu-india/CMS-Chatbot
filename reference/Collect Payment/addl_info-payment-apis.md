---
title: Additional Info for Payment APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: Additional Info for Payment APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes the additional information on **v2/payment** API such as character limit and data type of each parameter or fields of various JSON objects.

## Request headers
<HTMLBlock>{`
<Table>
<thead>
<tr>
<th>
Header
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
date
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> Current date and time in GMT/UTC format (RFC 7231 / IMF-fixdate). This header is required for generating the authorization signature.
</td>

<td>
Wed, 28 Jun 2023 11:25:19 GMT
</td>
</tr>

<tr>
<td>
authorization
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> HMAC signature generated using SHA512 algorithm. Format: 
hmac username="[accountId]", algorithm="sha512", headers="date", signature="[calculated_signature]"

The signature is calculated as: sha512(request_body + '|' + date + '|' + merchant_secret)

This replaces the 'hash' parameter from v1 API.
</td>

<td>
hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="abcd1234..."
</td>
</tr>

<tr>
<td>
content-type
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> Must be set to <code>application/json</code>.
</td>

<td>
application/json
</td>
</tr>

</tbody>
</Table>
`}</HTMLBlock>

## Request body
<HTMLBlock>{`
<Table>
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
accountId
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> The unique Merchant Key provided by PayU for your merchant account. In v2, this replaces the 'key' parameter from v1.
<br/>
<code>Character limit</code>: 50
</td>

<td>
<YOUR_TEST_KEY>
</td>
</tr>

<tr>
<td>
txnId
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> Unique Transaction ID generated at your (Merchant's) end to track a particular order. In v2, this replaces the 'txnid' parameter from v1. If a transaction using a particular txnId has already been processed at PayU, reusing the same txnId will fail.
<br/>
<code>Character limit</code>: 50

* **Note**: Ensure that the txnId sent in every transaction request is unique.
</td>

<td>
txn_12345
</td>
</tr>

<tr>
<td>
currency
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> Three-letter ISO currency code for the transaction.
<br/>
<code>Character limit</code>: 3
</td>

<td>
INR
</td>
</tr>

<tr>
<td>
order
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Contains order-related information including product details, payment charge specification, and user defined fields. See detailed fields in the <a href="#order-json-object-fields">order JSON object fields</a> section below.
</td>

<td>
  Refer to <a href="#order-json-object-fields">order JSON object fields</a>.
</td>
</tr>

<tr>
<td>
billingDetails
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Customer billing information. Combines customer contact and address details. See detailed fields in <a href="#billingdetails-json-object-fields">billingDetails JSON object fields</a>.
</td>

<td>
  Refer to <a href="#billingdetails-json-object-fields">billingDetails JSON object fields</a>.
</td>
</tr>

<tr>
<td>
callBackActions
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Callback URLs for different payment outcomes. Replaces individual 'surl', 'furl', and 'curl' parameters from v1. See detailed fields in <a href="#callbackactions-json-object-fields">callBackActions JSON object fields</a>.
</td>
<td>
  Refer to <a href="#callbackactions-json-object-fields">callBackActions JSON object fields</a>.
</td>
</tr>

<tr>
<td>
additionalInfo
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Additional configuration parameters for routing and transaction flow. See flow-specific documentation for details.
</td>

<td>
{
  "txnFlow": "nonseamless"
}
</td>
</tr>

<tr>
<td>
paymentMethod
<br/>
<code>mandatory for seamless</code>
</td>

<td>
<code>object</code> Payment method details required for seamless integration. Replaces 'pg' and 'bankcode' parameters from v1. For more information, refer to <a href="#paymentmethod-json-object-fields-only-for-seamless-integration">paymentMethod JSON object fields</a>.
</td>

<td>
Refer to <a href="#paymentmethod-json-object-fields-only-for-seamless-integration">paymentMethod JSON object fields</a>.
</td>
</tr>

</tbody>
</Table>
`}</HTMLBlock>

<br />

### order JSON object fields
<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Field</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
productInfo<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Brief description of the product(s) or service being purchased. Replaces the 'productinfo' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 100
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
iPhone 13
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentChargeSpecification<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Contains payment charge information including the transaction price and convenience fees.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"price": 1000.00<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentChargeSpecification.price<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">number</code> The transaction amount. In v2, this is passed as a numeric value inside the order object.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
1000.00
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentChargeSpecification.convenienceFee<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Convenience fee specification if dynamic convenience fee is configured on your merchant account.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CC:12,AMEX:19
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> User-defined parameters for passing merchant metadata. These replace individual udf1–udf5 parameters from v1. Only udf1 through udf5 are supported and returned in payment responses.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255 for each field
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"udf1": "value1",<br/>
&nbsp;&nbsp;"udf2": "value2"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf1 – udf5<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Merchant-defined metadata strings.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
order_ref_meta
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

### billingDetails JSON object fields
<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Field</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
firstName<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's first name. Replaces the 'firstname' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 60
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
John
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
lastName<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's last name. Replaces the 'lastname' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 20
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
Doe
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
email<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's valid email address. Replaces the 'email' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
john@example.com
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
phone<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's contact phone number (10-digit mobile number for Indian transactions). Replaces the 'phone' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
9876543210
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
address1<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing address line 1. Replaces 'address1' from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 100
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
123 Main Street
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
address2<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing address line 2. Replaces 'address2' from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 100
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
Apartment 4B
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
city<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing city.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
Mumbai
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
state<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing state.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
Maharashtra
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
country<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing country.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
India
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
zipCode<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing postal/zip code.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 20
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
400001
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

### callBackActions JSON object fields
<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Field</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
successAction<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Full HTTPS URL where PayU redirects the customer upon successful payment completion. Replaces 'surl' from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<redacted URL>
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
failureAction<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Full HTTPS URL where PayU redirects the customer upon payment failure. Replaces 'furl' from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<redacted URL>
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cancelAction<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Full HTTPS URL where PayU redirects the customer if the transaction is cancelled on the payment page. Replaces 'curl' from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<redacted URL>
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

### paymentMethod JSON object fields (only for Seamless Integration)
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Payment mode identifier. Valid values: <code>CreditCard</code>, <code>DebitCard</code>, <code>NetBanking</code>, <code>UPI</code>, <code>Wallet</code>, <code>EMI</code>, <code>BNPL</code>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>NetBanking</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Bank, provider, or network identifier for the chosen payment method.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SBIN</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCard<br> <code>mandatory for Cards &amp; EMI</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>object</code> Contains card or token details when paying with cards or card-based EMI. See <a href="#paymentcard-json-object-fields-only-for-seamless-card-payments">paymentCard JSON object fields</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Refer to paymentCard section</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard JSON object fields (only for Seamless Card Payments)
<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Field</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cardNumber<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for new card</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Credit/Debit card number. Must be between 13-19 digits and pass Luhn algorithm validation.<br/>
<strong>Note:</strong> Omit when processing saved card tokens.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
4111111111111111
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
validThrough<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Card expiry date in <code>MM/YYYY</code> format.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 7 characters (MM/YYYY)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
12/2026
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
ownerName<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for new card</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Cardholder name printed on the card.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
John Doe
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cvv<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Card verification value (CVV/CVC).<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 3-4 digits (3 for Visa/Mastercard, 4 for AMEX)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
123
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cardToken<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for tokenized cards</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Saved card token for repeat / tokenized card transactions. Replaces 'store_card_token' from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
token_12345
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cardTokenType<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for tokenized cards</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Classification of the token.<br/>
<strong>Allowed values:</strong> <code>PAYU</code>, <code>NETWORK</code>, <code>ISSUER</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
NETWORK
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
tavv<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">conditional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Token Authentication Verification Value (TAVV), required for network token transactions when performing device authentication.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
kH8e...
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
last4Digits<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">conditional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Last 4 digits of the actual card number for tokenized transactions.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
1111
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## Key Differences between v1 and v2 Payment API
### Parameter Changes:
1. **key** → **accountId**: Merchant key parameter renamed (max 50 chars).
2. **txnid** → **txnId**: Transaction ID parameter renamed (max 50 chars).
3. **amount** → **order.paymentChargeSpecification.price**: Amount passed as a number inside the order object.
4. **productinfo** → **order.productInfo**: Product info organized inside the order object.
5. **firstname, lastname, email, phone** → **billingDetails object**: Customer details grouped into a structured object.
6. **address1, address2, city, state, country, zipcode** → **billingDetails object**: Address parameters structured under billingDetails.
7. **surl, furl, curl** → **callBackActions object**: Direct string URLs for `successAction`, `failureAction`, and `cancelAction`.
8. **pg, bankcode** → **paymentMethod object**: Grouped into `paymentMethod.name` and `paymentMethod.bankCode` (seamless only).
9. **ccnum, ccvv, ccexpmon, ccexpyr** → **paymentMethod.paymentCard object**: Card parameters consolidated with `validThrough` in `MM/YYYY`.
10. **hash** → **authorization header**: Cryptographic authentication generated per request and passed via HTTP headers.
11. **udf1-udf5** → **order.userDefinedFields object**: User-defined metadata passed as key-value pairs (udf1 to udf5 supported).

## API Endpoints
* **Test Environment**: `https://apitest.payu.in/v2/payments`
* **Production Environment**: `https://api.payu.in/v2/payments`
* **HTTP Method**: `POST`

### Sample Request Format (Hosted Checkout):
```json
{
  "accountId": "<YOUR_MERCHANT_KEY>",
  "txnId": "ORDER_TXN_1001",
  "currency": "INR",
  "order": {
    "productInfo": "iPhone 13",
    "paymentChargeSpecification": {
      "price": 25000.00
    },
    "userDefinedFields": {
      "udf1": "meta1",
      "udf2": "meta2"
    }
  },
  "billingDetails": {
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "9876543210",
    "address1": "123 Main Street",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "zipCode": "400001"
  },
  "callBackActions": {
    "successAction": "<redacted URL>",
    "failureAction": "<redacted URL>",
    "cancelAction": "<redacted URL>"
  },
  "additionalInfo": {
    "txnFlow": "nonseamless"
  }
}
```

## Sample Responses

### Success Response (Seamless Final Status)
```json
{
  "status": "success",
  "result": {
    "paymentId": "PAY_abc123xyz789",
    "txnId": "ORDER_TXN_1001",
    "amount": 25000.00,
    "currency": "INR"
  },
  "message": "Transaction successful"
}
```

### Pending Response (Hosted / 3DS Redirect)
```json
{
  "status": "PENDING",
  "result": {
    "checkoutUrl": "https://checkout.payu.in/pay/PAY_pending456"
  },
  "message": "Awaiting customer authentication"
}
```

### Failure Response
```json
{
  "status": "failed",
  "error": {
    "code": "PAYMENT_DECLINED",
    "message": "Declined by bank"
  },
  "result": {
    "paymentId": "PAY_failed789",
    "txnId": "ORDER_TXN_1001"
  }
}
```

## Error Codes

| Code | HTTP Status | Description | Resolution |
| ---- | ----------- | ----------- | ---------- |
| `INVALID_AMOUNT` | 400 | Invalid amount value | Ensure price is positive number |
| `INVALID_CURRENCY` | 400 | Unsupported currency | Use supported currency code (e.g. INR) |
| `AUTHENTICATION_FAILED` | 401 | Invalid HMAC signature or key | Verify authorization signature format and merchant secret |
| `DUPLICATE_REFERENCE` | 409 | txnId already processed | Provide a new unique txnId |
| `PAYMENT_DECLINED` | 422 | Payment declined by downstream issuer | Retry with another payment mode |

## Next Steps
1. **Verify Transaction**: Always call the [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api/) to retrieve the final transaction state.
2. **Handle Webhooks**: Configure webhooks on the PayU merchant dashboard for server-to-server notifications.
