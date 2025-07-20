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
## Request parameters

## Request headers

| HEADER                    | DESCRIPTION                                                                                                                                                                                                       | EXAMPLE                                                                      |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| date (mandatory)          | string - Current date and time in GMT/UTC format. This header is required for generating the authorization signature.                                                                                             | Wed, 28 Jun 2023 11:25:19 GMT                                                |
| authorization (mandatory) | string - HMAC signature generated using SHA512 algorithm. Format: username="\[accountId]",algorithm="sha512",headers="date",signature="\[calculated\_signature]". This replaces the 'hash' parameter from v1 API. | username="smsplus",algorithm="sha512",headers="date",signature="abcd1234..." |

## Request body

<HTMLBlock>{`
<table>
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Parameter</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
accountId<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> This parameter is the unique Merchant Key provided by PayU for your merchant account. In v2, this replaces the 'key' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
smsplus
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
referenceId<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. In v2, this replaces the 'txnid' parameter from v1. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular reference ID has already been successful at PayU, the usage of the same Reference ID again would fail. Hence, you must post us a unique reference ID for every new transaction.<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">Character limit</code>: 25<br/>
<strong>Note</strong>: Ensure that the reference ID sent in every transaction request is unique.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
order_12345
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
currency<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Currency for the transaction. Default value is INR.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
INR
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentSource<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Source of the payment (e.g., WEB, MOBILE).
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
WEB
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
order<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Contains order-related information including product details, payment charge specification, and user defined fields.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"productInfo": "iPhone",<br/>
&nbsp;&nbsp;"paymentChargeSpecification": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"price": "1000.00"<br/>
&nbsp;&nbsp;},<br/>
&nbsp;&nbsp;"userDefinedFields": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"udf1": "value1"<br/>
&nbsp;&nbsp;}<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
order.productInfo<br/>
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
order.paymentChargeSpecification.price<br/>
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
order.userDefinedFields<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">optional</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> User-defined parameters that can be used for various purposes. These replace the individual udf1-udf5 parameters from v1. Available fields: udf1, udf2, udf3, udf4, udf5<br/>
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
billingDetails<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Customer billing information. This object combines and replaces individual v1 parameters like 'firstname', 'email', 'phone'.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"firstName": "John",<br/>
&nbsp;&nbsp;"lastName": "Doe",<br/>
&nbsp;&nbsp;"email": "john@example.com",<br/>
&nbsp;&nbsp;"phone": "9876543210"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
billingDetails.firstName<br/>
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
billingDetails.lastName<br/>
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
billingDetails.email<br/>
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
billingDetails.phone<br/>
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
billingDetails.address1<br/>
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
billingDetails.address2<br/>
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
billingDetails.city<br/>
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
billingDetails.state<br/>
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
billingDetails.country<br/>
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
billingDetails.zipCode<br/>
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

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
callBackActions<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Callback URLs for different payment outcomes. This object replaces the individual 'surl' and 'furl' parameters from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"successAction": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"redirectUrl": "https://example.com/success"<br/>
&nbsp;&nbsp;},<br/>
&nbsp;&nbsp;"failureAction": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"redirectUrl": "https://example.com/failure"<br/>
&nbsp;&nbsp;}<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
callBackActions.successAction.redirectUrl<br/>
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
callBackActions.failureAction.redirectUrl<br/>
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
callBackActions.cancelAction.redirectUrl<br/>
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

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
additionalInfo<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Additional information required for payment processing.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"txnFlow": "nonseamless"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
additionalInfo.txnFlow<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for non-seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Specifies the transaction flow type. Must be set to "nonseamless" for PayU-hosted integration. Not required for seamless integration.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
nonseamless
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentMethod<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Payment method details required for seamless integration. This object replaces the 'pg' and 'bankcode' parameters from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"name": "CreditCard",<br/>
&nbsp;&nbsp;"bankCode": "CC"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentMethod.name<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Payment method name (e.g., CreditCard, DebitCard, NetBanking, UPI). This replaces the 'pg' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CreditCard
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentMethod.bankCode<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Bank code or payment gateway code. This replaces the 'bankcode' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
CC
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentCard<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">object</code> Card details for seamless card payments. This object combines v1 parameters like 'ccnum', 'ccvv', 'ccexpmon', 'ccexpyr'.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
{<br/>
&nbsp;&nbsp;"cardNumber": "4111111111111111",<br/>
&nbsp;&nbsp;"validThrough": "12/25",<br/>
&nbsp;&nbsp;"ownerName": "John Doe",<br/>
&nbsp;&nbsp;"cvv": "123"<br/>
}
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentCard.cardNumber<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Credit/Debit card number. This replaces the 'ccnum' parameter from v1. Must be between 13-19 digits (15 digits for AMEX, 13-19 digits for Maestro) and must be validated using the LUHN algorithm.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
4111111111111111
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentCard.validThrough<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless card payments</code>
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
paymentCard.ownerName<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Cardholder name as printed on the card. This replaces the 'ccname' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
John Doe
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentCard.cvv<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for seamless card payments</code>
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
paymentCard.cardToken<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for saved card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Saved card token for repeat transactions. This replaces the 'store_card_token' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
token_12345
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
paymentCard.tokenType<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory for saved card payments</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Type of token being used. This replaces the 'storecard_token_type' parameter from v1.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
NETWORK_TOKEN
</td>
</tr>

</tbody>
</table>

<!-- Request Headers Table for v2 _payment API -->
<table style="border-collapse: collapse; width: 100%; max-width: 85%; margin-top: 30px;">
<thead>
<tr style="background-color: #f2f2f2;">
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Header</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
<th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
date<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> Current date and time in GMT/UTC format. This header is required for generating the authorization signature.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
Wed, 28 Jun 2023 11:25:19 GMT
</td>
</tr>

<tr>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
authorization<br/>
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">mandatory</code>
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
<code style="background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px;">string</code> HMAC signature generated using SHA512 algorithm. Format: 
username="[accountId]",algorithm="sha512",headers="date",signature="[calculated_signature]"<br/><br/>
The signature is calculated as: sha512(request_body + '|' + date + '|' + merchant_secret)<br/><br/>
This replaces the 'hash' parameter from v1 API.
</td>
<td style="border: 1px solid #ddd; padding: 12px; vertical-align: top;">
username="smsplus",algorithm="sha512",headers="date",signature="abcd1234..."
</td>
</tr>

</tbody>
</table>
`}</HTMLBlock>

<br />

## Character Limits Summary

Production vs Test Environment Differences:

* firstName: 60 characters (Production), 20 characters (Test)
* All other parameters have the same limits across both environments

Key Parameter Limits:

* referenceId (txnid): 25 characters
* productInfo: 100 characters
* firstName: 60 characters (Production), 20 characters (Test)
* lastName: 20 characters
* email: 50 characters
* phone: 50 characters
* address1: 100 characters
* address2: 100 characters
* city: 50 characters
* state: 50 characters
* country: 50 characters
* zipCode: 20 characters
* successAction/failureAction/cancelAction URLs: 50 characters
* userDefinedFields (udf1-udf5): 255 characters each

Card-Specific Formats:

* cardNumber: 13-19 digits (15 for AMEX, 13-19 for Maestro)
* validThrough: MM/YY format (MM: 01-12, YY: two-digit year)
* cvv: 3-4 digits (3 for most cards, 4 for AMEX)

Key Differences between v1 and v2 \_payment API

Parameter Changes:

1. key → accountId: Merchant key parameter renamed
2. txnid → referenceId: Transaction ID parameter renamed
3. amount → order.paymentChargeSpecification.price: Amount moved to nested object
4. productinfo → order.productInfo: Product info moved to order object
5. firstname, lastname, email, phone → billingDetails object: Customer details grouped into object
6. address1, address2, city, state, country, zipcode → billingDetails object: Address fields grouped
7. surl, furl, curl → callBackActions object: Callback URLs restructured
8. pg, bankcode → paymentMethod object: Payment method details grouped (seamless only)
9. ccnum, ccvv, ccexpmon, ccexpyr → paymentCard object: Card details grouped (seamless only)
10. hash → authorization header: Authentication moved to header
11. udf1-udf5 → order.userDefinedFields object: User defined fields grouped

New Parameters in v2:

* currency: Transaction currency (mandatory)
* paymentSource: Payment source identifier (optional)
* additionalInfo.txnFlow: Flow type for non-seamless integration
* callBackActions.cancelAction: Cancel callback support

Integration Flow Changes:

* Non-seamless: Must include additionalInfo.txnFlow = "nonseamless"
* Seamless: Requires paymentMethod and paymentCard objects
* Headers: Authentication moved to headers with date-based signature
* Structure: More modular with nested objects for better organization

### Additional parameters for Guest Checkout

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        alt\_id
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain Alt ID for the guest checkout.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain the Alt ID expiry month.
        For VISA cards, Plain card's expiry month need to be posted this parameter.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain the Alt ID expiry year.
        For VISA cards, Plain card's expiry year need to be posted this parameter.
      </td>

      <td>
        2021
      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        **mandatory**
      </td>

      <td>
        `JSON`The fields which are included in this JSON are described in the next table.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

The description of the fields in the additional\_info JSON.

| Field            | Description                                                                                                                                                                   |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
| tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
| TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

### Additional parameters for Saved Card

#### Using Network tokens

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccnum
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.
      </td>

      <td>
        512\*\*\*6789012346
      </td>
    </tr>

    <tr>
      <td>
        ccname
        **optional**
      </td>

      <td>
        `varchar` It is the customer's name on card.
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        ccvv
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        **mandatory**
      </td>

      <td>
        `integer` This parameter must contain the Expiry month that is mentioned under card validity.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        **mandatory**
      </td>

      <td>
        `integer` This parameter must contain the Expiry year that is mentioned under card validity.
      </td>

      <td>
        2022
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `varchar` This must include the Network token generated at your end.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        **mandatory**
      </td>

      <td>
        `integer` This parameter is used to specify the store card token type. For this scenario, you must include 1.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        **mandatory**
      </td>

      <td>
        `varchar` This parameter will contain the additional information in the following JSON format:
        \{“last4Digits”: “1234”, “<Glossary>TAVV</Glossary>”: “ABCDEFGH”,”<Glossary>trid</Glossary>”:”1234567890”, “<Glossary>tokenRefNo</Glossary>”:”abcde123456”}
      </td>

      <td>
        \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}
      </td>
    </tr>
  </tbody>
</Table>

#### Using Issuer tokens

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        ccexpmon
        **mandatory**
      </td>

      <td>
        `integer` This parameter must contain the network token expiry month.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr
        **mandatory**
      </td>

      <td>
        `integer` This parameter must contain the network token expiry year.
      </td>

      <td>
        2024
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `varchar` This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        **mandatory**
      </td>

      <td>
        `integer` This parameter is used to specify the store card token type. For this scenario, you must include 0.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        **mandatory**
      </td>

      <td>
        varchar\` This parameter will contain the additional information in the following JSON format:
        \{"<Glossary>trMerchantId</Glossary>":"INBANPAYUWIBPAY011","<Glossary>tokenReferenceId</Glossary>":"02ac786d-0081-4b1a-a2a6-b0755a83964c"," <Glossary>tokenBank</Glossary>":"HDFC","<Glossary>last4Digits</Glossary>":"8179"}
      </td>

      <td>
        \{"trMerchantId":"INBANPAYUWIBPAY011","tokenReferenceId":"02ac786d-0081-4b1a-a2a6-b0755a83964c","tokenBank":"HDFC","last4Digits":"8179"}
      </td>
    </tr>
  </tbody>
</Table>

#### Using card tokenized with PayU

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        **mandatory**
      </td>

      <td>
        `integer` This parameter is used to specify the store card token type. For this scenario, you must include 0.
      </td>

      <td>
        0
      </td>
    </tr>

    <tr>
      <td>
        user\_credentials
        **mandatory**
      </td>

      <td>
        `varchar` This parameter must contain the user credentials.
      </td>

      <td>
        a:b
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `varchar` This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>
  </tbody>
</Table>

## Using card on a decoupled Flow with Network token or other partner tokenization

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        **mandatory**
      </td>

      <td>
        `integer` This parameter is used to specify store card token type, that is, tokenization partner. For this scenario, you must include 1.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `varchar` This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        **mandatory**
      </td>

      <td>
        This parameter will contain the additional information in the following JSON format:
        \{“\{user.glossay:last4Digits}”: “1234”, “<Glossary>TAVV</Glossary>”: “ABCDEFGH”,”<Glossary>trid</Glossary>”:”1234567890”, “<Glossary>tokenRefNo</Glossary>”:”abcde123456”}
      </td>

      <td>
        \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”
      </td>
    </tr>
  </tbody>
</Table>

#### Using Card on a decoupled flow with PayU rtokenization

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ccvv
        **optional**
      </td>

      <td>
        `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type
        **mandatory**
      </td>

      <td>
        `integer` This parameter is used to specify store card token type, that is, tokenization partner. For this scenario, you must include 0.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token
        **mandatory**
      </td>

      <td>
        `varchar` This must include the token generated by PayU for the card.
      </td>

      <td>
        1234 4567 2456 3566
      </td>
    </tr>

    <tr>
      <td>
        additional\_info
        **mandatory**
      </td>

      <td>
        This parameter will contain the additional information in the following JSON format:
        \{“\{user.glossay:last4Digits}”: “1234”, “<Glossary>TAVV</Glossary>”: “ABCDEFGH”,”<Glossary>trid</Glossary>”:”1234567890”, “<Glossary>tokenRefNo</Glossary>”:”abcde123456”}
      </td>

      <td>
        \{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”
      </td>
    </tr>
  </tbody>
</Table>

## Character Limit for Request Parameters

| Parameter   | Production Environment | Test Environment |
| ----------- | ---------------------- | :--------------- |
| productinfo | 100                    | 100              |
| firstname   | 60                     | 20               |
| email       | 50                     | 50               |
| lastname    | 20                     | 20               |
| address1    | 100                    | 100              |
| address2    | 100                    | 100              |
| city        | 50                     | 50               |
| state       | 50                     | 50               |
| country     | 50                     | 50               |
| zipcode     | 20                     | 20               |
| surl        | 50                     | 50               |
| furl        | 50                     | 50               |
| curl        | 50                     | 50               |
| udf1 - udf5 | 255                    | 255              |

## Response parameters

## General response parameters for all Web Checkout integrations

<Table>
  <thead>
    <tr>
      <th>
        **Variable**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        Transaction ID is a unique number assigned by PayU for each transaction. Keep note of it for future reference for inquiry or refund."
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to [Payment Mode Codes](doc:payment-mode-codes).
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter indicates the outcome of the transaction as 'success', 'failed' or 'pending'. A value of 'success' means the transaction was successful, 'failure' or 'pending' means the transaction failed.
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter is used to identify the merchant's PayU account. It is the same key used during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter would contain the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter would contain the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter would contain the same value of email which was sent.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf
      </td>

      <td>
        This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        PayU calculates a hash using other parameters and returns it to the merchant. The merchant must verify it and then mark a transaction as success/failure. This is to ensure the integrity of the transaction. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted)
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        This parameter provides the reason for failure for failed transactions.

        * *Note*\* that failure reasons may vary depending on the error codes from different banks.
      </td>
    </tr>

    <tr>
      <td>
        error\_message
      </td>

      <td>
        This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter holds the code of the payment option used in the transaction, such as Visa Debit Card - VISA, Master Debit Card - MAST.
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter indicates the payment gateway used for the transaction, such as 'CC-PG' for credit card payment gateway.
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter would contain the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information, refer to [Payment State Explanations](ref:payment-state-explanations).
      </td>
    </tr>
  </tbody>
</Table>

## Response for initial Server-to-Server request

| **Parameter**     | **Description**                                                                                                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result            | This parameter contains a JSON Object that includes **post\_uri** and **post\_data** fields.                                                                                                                                                                                 |
| result.post\_uri  | This field contains the redirect URL.                                                                                                                                                                                                                                        |
| result.post\_data | post\_data is a base64 encoded string. The merchant needs to decode post\_data, which is an HTML format with auto submit, which then needs to be shown on the customer’s browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |
| status            | This field contains the status for the transaction.                                                                                                                                                                                                                          |
| error             | For the failed transactions, this parameter provides the reason for  failure.                                                                                                                                                                                                |
| message           | This field contains any additional message about the transaction.                                                                                                                                                                                                            |

> 📘 Note:
>
> The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.

#### metaData JSON Fields Description

| **Field**      | **Description**                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message        | This field contains any additional message about the transaction.                                                                                       |
| referenceId    | This field contains the reference ID of the transaction.                                                                                                |
| statusCode     | This field contains the status code for the transaction.                                                                                                |
| txnId          | This field contains the transaction ID of the transaction that was posted in the request.                                                               |
| unmappedStatus | This field contains the unmapped status of the transaction. For more information, refer to [Payment State Explanations](ref:payment-state-explanations) |

#### result JSON Fields Description

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mihpayid
      </td>

      <td>
        It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.
      </td>
    </tr>

    <tr>
      <td>
        mode
      </td>

      <td>
        This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to [Payment Mode Codes](doc:payment-mode-codes)
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only.
      </td>
    </tr>

    <tr>
      <td>
        key
      </td>

      <td>
        This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        txnid
      </td>

      <td>
        This parameter would contain the transaction ID value posted by the merchant during the transaction request.
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter would contain the original amount which was sent in the transaction request by the merchant.
      </td>
    </tr>

    <tr>
      <td>
        productinfo
      </td>

      <td>
        This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        firstname
      </td>

      <td>
        This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        lastname
      </td>

      <td>
        This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        email
      </td>

      <td>
        This parameter would contain the same value of email which was sent.
      </td>
    </tr>

    <tr>
      <td>
        phone
      </td>

      <td>
        This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.
      </td>
    </tr>

    <tr>
      <td>
        udf
      </td>

      <td>
        This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        PayU calculates the hash using a string of other parameters and returns it to the merchant. The merchant must verify the hash, and only then mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with. The calculation is as follows: 
        sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)

        * *Note*\*: The handling of udf1 – udf5 parameters remains similar to the hash calculation when the merchant sends it in the transaction request to PayU. If any of the udf (udf1-udf5) was posted in the transaction request, it must be taken in hash calculation also. If none of the udf parameters were posted in the transaction request, they should be left empty in the hash calculation too.
      </td>
    </tr>

    <tr>
      <td>
        error
      </td>

      <td>
        For the failed transactions, this parameter provides the reason for  failure. 

        * *Note*\*: The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.
      </td>
    </tr>

    <tr>
      <td>
        bankcode
      </td>

      <td>
        This parameter contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.
      </td>
    </tr>

    <tr>
      <td>
        PG\_TYPE
      </td>

      <td>
        This parameter gives information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.
      </td>
    </tr>

    <tr>
      <td>
        bank\_ref\_num
      </td>

      <td>
        For each successful transaction – this parameter would contain the bank reference number generated by the bank.
      </td>
    </tr>

    <tr>
      <td>
        unmappedstatus
      </td>

      <td>
        This parameter contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate status which are used for tracking various activities internal to the system. For more information, refer to [Payment State Explanations](ref:payment-state-explanations).
      </td>
    </tr>
  </tbody>
</Table>

#### binData fields description (applicable for only for Cards)

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        pureS2SSupported
      </td>

      <td>
        This field contains contains any of the following to indicate whether the card supports S2S:

        * **true**: Card supports S2S
        * **false**: Card does not support S2S
      </td>
    </tr>

    <tr>
      <td>
        issuingBank
      </td>

      <td>
        This field contains the card issuing bank.
      </td>
    </tr>

    <tr>
      <td>
        cardType
      </td>

      <td>
        This field contains the card type such as VISA, MasterCard, etc.
      </td>
    </tr>

    <tr>
      <td>
        isDomestic
      </td>

      <td>
        This field contains contains any of the following to indicate whether the card is domestic or international:

        * **true**: It is a domestic card
        * **false**: It is an international card
      </td>
    </tr>
  </tbody>
</Table>

```
  {
  "mihpayid": "403993715531077182",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "JPM7Fg",
  "txnid": "ypl938459435dfdfdf",
  "amount": "1000.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "addedon": "2024-02-27 15:00:42",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "ashish@gmail.com",
  "phone": "9876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "896193988312194700",
  "field2": "857712",
  "field3": "1000.00",
  "field4": "",
  "field5": "00",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "AUTHORIZED",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "896193988312194700",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params.",
  "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
}
```

## Merchant Hosted Checkout

### Cards

#### Sample request

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
--data-urlencode 'key=JF****g' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'amount=10' \
--data-urlencode 'phone= 9876543210' \
--data-urlencode 'productinfo=Product_info' \
--data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'lastname=Test' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=06' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid=jYhbOYH9o4' \
--data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
--data-urlencode 'ccnum=4012000000002004' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'threeDS2RequestData={
    "browserInfo": {
        "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
        "acceptHeader": "*\/*",
        "language": "en-US",
        "colorDepth": "24",
        "screenHeight": "600",
        "screenWidth": "800",
        "timeZone": "-300",
        "javaEnabled": true,
        "ip": "10.248.2.71"
    }
}'
```

#### Sample response

**Formatted response**

```
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JF***g
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-08 19:37:19
    [productinfo] => iPhone
    [firstname] => Ashish
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
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 0608273386032718000015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 403993715524069222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] =>
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 0608273386032718000015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
)

```

### UPI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```
```
```

#### Sample response

```
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

### Wallets

#### Sample request

```
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => CASH
    [status] => success
    [unmappedstatus] => captured
    [key] => J*****g
    [txnid] => HC13glcAkssIkl
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-10-21 17:45:24
    [productinfo] => iPhone
    [firstname] => Ashish
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
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => CASH-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => CASH
    [error] => E000
    [error_Message] => No Error
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
)
```

### EMI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9123412345&productinfo=iPhone&pg=EMI&bankcode=ICICID03&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=43754118*****12346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523602563
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => v2tWbbdUOuacK9
    [amount] => 20000.00
    [discount] => 0.00
    [net_amount_debit] => 20000.00
    [addedon] => 2021-07-27 11:14:44
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@gmail.com
    [phone] => 1234567890
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
    [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => EMI-PG
    [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
    [bankcode]=> EMIA3
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] =>512345XXXXXX2346
)
```

### BNPL

#### Sample request

```
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => BNPL
    [status] => success
    [unmappedstatus] => captured
    [key] => J****g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
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
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] =>
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] =>
    [field7] => Transaction completed successfully
    [field8] =>
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => BNPL-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => LAZYPAY
    [error] => E000
    [error_Message] => No Error
)
```

### QR

#### Sample response

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=QR&bankcode=UPIQR&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```

#### Sample response

```
(
    [mihpayid] => 403993715524045752
    [mode] => QR
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
    [productinfo] => iPhone
    [firstname] => Ashish
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => QR-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => UPIQR
    [error] => E000
    [error_Message] => No Error
)
```

## From other payment aggregator using Maximiser

The transaction routed to which aggregator will be identified by the parameter **pa\_name** in the transaction response. Also on dashboard merchant can view the aggregator name in transaction list and view details. For example, transaction routed through PayU, UDF will have PayU. Similarly, UDF contains corresponding aggregator name for Razorpay, BillDesk, Pinelabs and Paytm.

```
(
    [mihpayid] => 19855444473
    [mode] => DC
    [status] => success
    [unmappedstatus] => captured
    [key] => mBWD5W
    [txnid] => fb1329207367842ddfa3d
    [amount] => 2.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 2
    [addedon] => 2024-05-10 11:50:19
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] =>
    [address1] =>
    [address2] =>
    [city] =>
    [state] =>
    [country] =>
    [zipcode] =>
    [email] => test@example.com
    [phone] => 1234567890
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
    [hash] => c82ae4a92f52e8cfa7397d1ec787b830e7115ececbe8aab301df3700e96aae8a4d893ff79a92c676c1fd3bc8c41cdf33231c9670a63e5995bb950d6147b33e2c
    [field1] =>
    [field2] => 0
    [field3] =>
    [field4] =>
    [field5] => RazorPay
    [field6] => pay_O8gqNOgWN5jeJa
    [field7] => {"acquirer_payment_id":{},"amount":{},"amount_orig":{},"authorization_staus":{},"bank_code":{},"bank_ref_no":{},"cardmasked":{},"currency":{},"customer_email":{},"customer_name":{},"customer_phone":{},"description":{},"error_desc":{},"order_id":{},"payment_channel":{},"payment_datetime":{},"payment_mode":{},"response_code":{},"response_message":{},"tax_on_tdr_amount":{},"tdr_amount":{},"transaction_id":{},"udf1":{},"udf2":{},"udf3":{},"udf4":{},"udf5":{}}
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [pa_name] => RazorPay
    [PG_TYPE] => DC-PG
    [bank_ref_num] => RPMASDF888D078DF6
    [bankcode] => MAST
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX0231
    [cardhash] => This field is no longer supported in postback params.
    [corporate_card] => 0
    [cobranded_card] =>
```