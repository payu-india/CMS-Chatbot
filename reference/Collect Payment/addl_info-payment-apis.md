---
title: Additional Info for Payment APIs
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
This section describes the additional information on v2 **\_payment** API such as character limit and data type of each parameter or fields of various JSON objects.

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
<code>string</code> Current date and time in GMT/UTC format. This header is required for generating the authorization signature.
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
username="[accountId]",<br/>algorithm="sha512",<br/>headers="date",signature="[calculated_signature]"

The signature is calculated as: sha512(request_body + '|' + date + '|' + merchant_secret)

This replaces the 'hash' parameter from v1 API.
</td>

<td>
username="smsplus",<br/>algorithm="sha512",headers="date",<br/>signature="abcd1234..."
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
<code>string</code> This parameter is the unique Merchant Key provided by PayU for your merchant account. In v2, this replaces the 'key' parameter from v1.
</td>

<td>
smsplus
</td>
</tr>

<tr>
<td>
referenceId
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. In v2, this replaces the 'txnid' parameter from v1. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular reference ID has already been successful at PayU, the usage of the same Reference ID again would fail. Hence, you must post us a unique reference ID for every new transaction.
<br/>
<code>Character limit</code>: 25

* **Note**: Ensure that the reference ID sent in every transaction request is unique.
</td>

<td>
order_12345
</td>
</tr>

<tr>
<td>
currency
<br/>
<code>mandatory</code>
</td>

<td>
<code>string</code> Currency for the transaction. Default value is INR.
</td>

<td>
INR
</td>
</tr>

<tr>
<td>
paymentSource
<br/>
<code>optional</code>
</td>

<td>
<code>string</code> Source of the payment (e.g., WEB, MOBILE).
</td>

<td>
WEB
</td>
</tr>

<tr>
<td>
order
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Contains order-related information including product details, payment charge specification, and user defined fields. See detailed fields in the order Object Fields section below.
</td>

<td>
  Refer to <a href="#order-object-fields">order JSON object field description</a>.
</td>
</tr>

<tr>
<td>
billingDetails
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Customer billing information. This object combines and replaces individual v1 parameters like 'firstname', 'email', 'phone'. See detailed fields. For more information, refer to <a href="#billingDetails-json-object-fields"> billingDetails JSON object field description</a>.
</td>

<td>
  Refer to <a href="#billingDetails-json-object-fields"> billingDetails JSON object field description</a>.
</td>
</tr>

<tr>
<td>
callBackActions
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Callback URLs for different payment outcomes. This object replaces the individual 'surl' and 'furl' parameters from v1. For more information, refer to <a href="#callBackActions-json-object-fields"> callBackActions JSON object field description</a>.
</td>
  Refer to <a href="#callBackActions-json-object-fields"> callBackActions JSON object field description</a>.
<td>
  
</td>
</tr>

<tr>
<td>
additionalInfo
<br/>
<code>mandatory</code>
</td>

<td>
<code>object</code> Additional information required for payment processing.
</td>

<td>
{
  "txnFlow": "nonseamless"
}
</td>
</tr>

<tr>
<td>
additionalInfo.txnFlow
<br/>
<code>mandatory for non-seamless</code>
</td>

<td>
<code>string</code> Specifies the transaction flow type. Must be set to "nonseamless" for PayU-hosted integration. Not required for seamless integration.
</td>

<td>
nonseamless
</td>
</tr>

<tr>
<td>
paymentMethod
<br/>
<code>mandatory for seamless</code>
</td>

<td>
<code>object</code> Payment method details required for seamless integration. This object replaces the 'pg' and 'bankcode' parameters from v1. For more information, refer to <a href="#paymentmethod-json-object-fields-only-for-seamless-integration">paymentMethod JSON object fields</a>.
</td>

<td>
Refer to <a href="#paymentmethod-json-object-fields-only-for-seamless-integration">paymentMethod JSON object fields</a>.
</td>
</tr>

<tr>
<td>
paymentCard
<br/>
<code>mandatory for seamless card payments</code>
</td>

<td>
<code>object</code> Card details for seamless card payments. This object combines v1 parameters like 'ccnum', 'ccvv', 'ccexpmon', 'ccexpyr'. For more information, refer to <a href="#paymentcard-json-object-fields-only-for-seamless-card-payments"paymentCard JSON object fields</a>.
</td>
<td>
Refer to <a href="#paymentcard-json-object-fields-only-for-seamless-card-payments">paymentCard JSON object fields</a>.  
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Brief description of the product(s). This parameter replaces the 'productinfo' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 100
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
iPhone
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentChargeSpecification<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Contains payment charge information including the transaction amount.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"price": "1000.00"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentChargeSpecification.price<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">float</code> The payment amount for the transaction. In v2, this is nested within the order object instead of being a top-level parameter like 'amount' in v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
1000.00
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> User-defined parameters that can be used for various purposes. These replace the individual udf1-udf5 parameters from v1. Available fields: udf1, udf2, udf3, udf4, udf5<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255 for each field
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"udf1": "value1",<br/>
&nbsp;&nbsp;"udf2": "value2",<br/>
&nbsp;&nbsp;"udf3": "value3",<br/>
&nbsp;&nbsp;"udf4": "value4",<br/>
&nbsp;&nbsp;"udf5": "value5"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf1<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> User defined field 1. This replaces the 'udf1' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
value1
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf2<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> User defined field 2. This replaces the 'udf2' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
value2
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf3<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> User defined field 3. This replaces the 'udf3' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
value3
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf4<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> User defined field 4. This replaces the 'udf4' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
value4
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
userDefinedFields.udf5<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> User defined field 5. This replaces the 'udf5' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 255
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
value5
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's first name. This replaces the 'firstname' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 60 (Production), 20 (Test)
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's last name. This replaces the 'lastname' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's email address. This replaces the 'email' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's phone number. This replaces the 'phone' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing address line 1. This replaces the 'address1' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing address line 2. This replaces the 'address2' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing city. This replaces the 'city' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing state. This replaces the 'state' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing country. This replaces the 'country' parameter from v1.<br/>
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Customer's billing postal code. This replaces the 'zipcode' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 20
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
400001
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## callBackActions JSON object fields

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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Action to be taken upon successful payment completion.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"redirectUrl": "https://example.com/success"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
successAction.redirectUrl<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> URL to redirect after successful payment. This replaces the 'surl' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
https://example.com/success
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
failureAction<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Action to be taken upon payment failure.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"redirectUrl": "https://example.com/failure"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
failureAction.redirectUrl<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> URL to redirect after failed payment. This replaces the 'furl' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
https://example.com/failure
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cancelAction<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Action to be taken when payment is cancelled by the user.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"redirectUrl": "https://example.com/cancel"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cancelAction.redirectUrl<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> URL to redirect when payment is cancelled. This replaces the 'curl' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 50
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
https://example.com/cancel
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## paymentMethod JSON object Fields (only for Seamless Integration)

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
name<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Payment method name (e.g., CreditCard, DebitCard, NetBanking, UPI). This replaces the 'pg' parameter from v1.<br/><br/>
<strong>Possible values:</strong><br/>
• CreditCard<br/>
• DebitCard<br/>
• NetBanking<br/>
• UPI<br/>
• Wallet<br/>
• EMI<br/>
• BNPL
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CreditCard
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
bankCode<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Bank code or payment gateway code. This replaces the 'bankcode' parameter from v1.<br/><br/>
<strong>Common values:</strong><br/>
• CC (Credit Card)<br/>
• DC (Debit Card)<br/>
• NB (Net Banking)<br/>
• UPI (UPI payments)<br/>
• WALLET (Wallet payments)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CC
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## paymentCard JSON object fields (only for Seamless Card Payments)

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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for new card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Credit/Debit card number. This replaces the 'ccnum' parameter from v1. Must be between 13-19 digits (15 digits for AMEX, 13-19 digits for Maestro) and must be validated using the LUHN algorithm.<br/><br/>
<strong>Note:</strong> Not required when using saved card tokens.
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Card expiry date in MM/YY format. This replaces the separate 'ccexpmon' and 'ccexpyr' parameters from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Format</code>: MM/YY where MM is two-digit month (01-12) and YY is two-digit year
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
12/25
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
ownerName<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for new card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Cardholder name as printed on the card. This replaces the 'ccname' parameter from v1.<br/><br/>
<strong>Note:</strong> Not required when using saved card tokens.
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
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Card verification value. This replaces the 'ccvv' parameter from v1.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Format</code>: 3-4 digit number (3 digits for most cards, 4 digits for AMEX)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
123
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
cardToken<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for saved card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Saved card token for repeat transactions. This replaces the 'store_card_token' parameter from v1.<br/><br/>
<strong>Usage:</strong> When using saved cards, provide this token instead of cardNumber and ownerName.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
token_12345
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
tokenType<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for saved card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Type of token being used. This replaces the 'storecard_token_type' parameter from v1.<br/><br/>
<strong>Possible values:</strong><br/>
• NETWORK_TOKEN (Network tokenization)<br/>
• ISSUER_TOKEN (Bank issued tokens)<br/>
• PAYU_TOKEN (PayU generated tokens)
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
NETWORK_TOKEN
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

## Character Limits Summary

### Production vs Test Environment Differences:

* **firstName**: 60 characters (Production), 20 characters (Test)
* All other parameters have the same limits across both environments

### Key Parameter Limits:

* **referenceId** (txnid): 25 characters
* **productInfo**: 100 characters
* **firstName**: 60 characters (Production), 20 characters (Test)
* **lastName**: 20 characters
* **email**: 50 characters
* **phone**: 50 characters
* **address1**: 100 characters
* **address2**: 100 characters
* **city**: 50 characters
* **state**: 50 characters
* **country**: 50 characters
* **zipCode**: 20 characters
* **successAction/failureAction/cancelAction URLs**: 50 characters
* **userDefinedFields (udf1-udf5)**: 255 characters each

### Card-Specific Formats:

* **cardNumber**: 13-19 digits (15 for AMEX, 13-19 for Maestro)
* **validThrough**: MM/YY format (MM: 01-12, YY: two-digit year)
* **cvv**: 3-4 digits (3 for most cards, 4 for AMEX)

## Key Differences between v1 and v2 \_payment API

### Parameter Changes:

1. **key** → **accountId**: Merchant key parameter renamed
2. **txnid** → **referenceId**: Transaction ID parameter renamed
3. **amount** → **order.paymentChargeSpecification.price**: Amount moved to nested object
4. **productinfo** → **order.productInfo**: Product info moved to order object
5. **firstname, lastname, email, phone** → **billingDetails object**: Customer details grouped into object
6. **address1, address2, city, state, country, zipcode** → **billingDetails object**: Address fields grouped
7. **surl, furl, curl** → **callBackActions object**: Callback URLs restructured
8. **pg, bankcode** → **paymentMethod object**: Payment method details grouped (seamless only)
9. **ccnum, ccvv, ccexpmon, ccexpyr** → **paymentCard object**: Card details grouped (seamless only)
10. **hash** → **authorization header**: Authentication moved to header
11. **udf1-udf5** → **order.userDefinedFields object**: User defined fields grouped

### New Parameters in v2:

* **currency**: Transaction currency (mandatory)
* **paymentSource**: Payment source identifier (optional)
* **additionalInfo.txnFlow**: Flow type for non-seamless integration
* **callBackActions.cancelAction**: Cancel callback support

### Integration Flow Changes:

* **Non-seamless**: Must include `additionalInfo.txnFlow = "nonseamless"`
* **Seamless**: Requires `paymentMethod` and `paymentCard` objects
* **Headers**: Authentication moved to headers with date-based signature
* **Structure**: More modular with nested objects for better organization

## API Endpoints

### v2 Endpoints:

* **Test Environment**: `https://apitest.payu.in/v2/payments`
* **Production Environment**: `https://api.payu.in/v2/payments`
* **HTTP Method**: `POST`

### Request Format:

```json
{
  "accountId": "merchant_key",
  "referenceId": "unique_transaction_id",
  "currency": "INR",
  "order": {
    "productInfo": "Product description",
    "paymentChargeSpecification": {
      "price": "1000.00"
    }
  },
  "billingDetails": {
    "firstName": "John",
    "email": "john@example.com",
    "phone": "9876543210"
  },
  "callBackActions": {
    "successAction": {
      "redirectUrl": "https://example.com/success"
    },
    "failureAction": {
      "redirectUrl": "https://example.com/failure"
    }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless"
  }
}
```