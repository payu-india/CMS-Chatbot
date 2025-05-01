---
title: v2 Net Banking Integration
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
Collect payments using Net Banking with Merchant Hosted Checkout integration using **v2/payments** API as described in this section. After collecting the details from the customer, make the transaction request with the payment details to PayU.

**Steps to Integrate**

1. [Initiate the payment to PayU](#step-1-initiate-the-payment-to-payu)
2. [Verify Payment](#step-3-verify-the-payment)

> 👍 Before you begin:
> 
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Initiate the payment to PayU

The following parameters vary for the NetBanking payment mode in the **Collect Payment** API (**v2/payments** API). For the API reference. refer to [Collect Payment - Net Banking](https://docs.payu.in/v2/reference/_payment_v2_merchant_hosted_netbanking).

|                            |                                       |
| :------------------------- | :------------------------------------ |
| **Test Environment**       | \<https://apitest.payu.in/v2/payments> |
| **Production Environment** | \<https://api.payu.in/v2/payments>     |

## Request parameters

### Request Header

| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Parameter | Description                                                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username  | Represents the username or identifier for the client or merchant, in this case, it's "smsplus".                                                                                  |
| algorithm | Indicates the hashing algorithm used for the HMAC signature. Here, it is set to "sha512".                                                                                        |
| headers   | Specifies which headers have been used in generating the hash. In this case, only the "date" header is used.                                                                     |
| signature | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

You must hash the request parameters using the following hash logic:

```
sha512(<Body data> + '|' + date + '|' + merchant_secret}
```

Where, \<Body data\> contains the request Body posted with the request.

<details>
<summary>Sample header code</summary>

```
var merchant_key = 'smsplus';
var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';

// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = date.toUTCString();

// authorization
var authorization = getAuthHeader(date);
console.log(authorization);

function getAuthHeader(date) {
var AUTH_TYPE = 'sha512';
var data = isEmpty(request['data'])?"":request['data'];
var hash_string = data + '|' + date + '|' + merchant_secret;
console.log("Hash String is ", hash_string);
var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
return authHeader;
}

pm.environment.set('date', date);
pm.environment.set('authorization', authorization);
pm.environment.set('merchant_key',merchant_key);
pm.environment.set('merchant_secret',merchant_secret);

function isEmpty(obj) {
for(var key in obj) {
if(obj.hasOwnProperty(key))
return false;
}
return true;
}
```

</details>

<br />

### Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The merchant key provided by PayU during onboarding.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT123</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Reference ID for transaction tracking and this must be unique for every transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>REF123456</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Amount of the transaction.<br><strong>Note</strong>: This value will not be considered as the transaction. Only the details in the<code> order.paymentChargeSpecification.price</code> field will be considered.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Currency of the transaction. By default, <strong>INR</strong> is posted.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentSource<code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Contains the payment source. </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>WeB</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentMethod<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the payment method used. For more information, refer to <a href="#paymentmethod-object-fields-description">paymentMethod object fields description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>        &quot;name&quot;: &quot;NetBanking&quot;,	<br>        &quot;bankCode&quot;: &quot;TESTNB&quot;<br>    }</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to <a href="#callbackactions-object-fields-description">callbackActions object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-field-descriptions">billingDetails object field descriptions</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>siDetails<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code>Subscription or SI details for the consent transaction. For more information, refer to<a href="#sidetails-object-fields-description"> siDetails object fields description</a> .</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryDetaIl <code>mandatory for NetBanking</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the beneficiary for NetBanking. For more information, refer to <a href="#beneficiarydetaIl-object-fields-description">beneficiaryDetaIl object fields description.</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{&quot;beneficiaryName&quot;: &quot;Ram&quot;, &quot;beneficiaryAccountNumber&quot;: &quot;115501029190&quot;}</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>. For NetBanking, this must contain <strong>NetBanking</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the bank code. For more information, refer to <a href="https://docs.payu.in/v1/docs/net-banking-codes">Net Banking Codes</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### order object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>productInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Details about the product being purchased. For more information, refer to<a href="#userdefinedfields-object-fields-description"> userDefinedFields object fields description</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userDefinedFields<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code>Custom fields defined by the user for additional information.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentChargeSpecification<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to <a href="#paymentchargespecification-object-fields-description">paymentChargeSpecification object fields description</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


#### userDefinedFields object fields description

| Field | Description         |
| ----- | ------------------- |
| udf1  | User defined field. |
| udf2  | User defined field. |
| udf3  | User defined field. |
| udf4  | User defined field. |
| udf5  | User defined field. |
| udf6  | User defined field. |
| udf7  | User defined field. |
| udf8  | User defined field. |
| udf9  | User defined field. |
| udf10 | User defined field. |

#### paymentChargeSpecification object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>price<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field must contain the price or transaction amount to be posted.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>10.00</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### callbackActions object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>successAction<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL to redirect to upon successful payment.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>failureAction<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL to redirect to if the payment is failed.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cancelAction<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL to redirect to if the transaction is cancelled.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>codAction<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL to handle Cash on Delivery actions.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>termAction<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL for completing terms and conditions actions.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>returnAction<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>URL to return to after successful payment action is completed.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## beneficiaryDetaIl object fields description

| Field                               | Description                                                        | Example      |
| ----------------------------------- | ------------------------------------------------------------------ | ------------ |
| beneficiaryName (required)          | The name of the beneficiary to whom the funds will be transferred. | Ram          |
| beneficiaryAccountNumber (required) | The account number of the beneficiary's bank account.              | 115501029190 |
| beneficiaryAccountType (required)   | The type of the beneficiary's bank account.                        | SAVINGS      |

> ❗️ Error Handling
> 
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.

### siDetails object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingCycle<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The frequency of the billing, indicating how often the payment occurs.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MONTHLY</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingAmount<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The amount to be billed for each cycle.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingCurrency<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The currency in which the billing amount is denominated.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INR</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingInterval<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The interval between billing cycles, specified in terms of the cycle frequency.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentStartDate<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date when the payment cycle begins.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2020-09-16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentEndDate<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The date when the payment cycle ends.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2020-10-16</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>siTokenRequestor<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::<br>1 : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.<br>2: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authpayuid<br><code>mandatory for modifying subscription</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>An identifier used for the authorization of payments via PayU.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>action<br><code>mandatory for cards</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field is used to modify or delete an existing subscription.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### billingDetails object field descriptions

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>firstName<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>First name of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Ashish</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>lastName<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Last name of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Kumar</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone number of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>9123456789</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Email address of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><a href="mailto:ashish@abc.com">ashish@abc.com</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>city<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>City of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bengaluru</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>state<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>State of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Karnatka</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>country<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Country of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Indiia</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>zipCode<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Postal/Zip code of the billing address</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>560071</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Thu, 27 Mar 2025 10:12:27 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="ec84843a663143bb89391f6fa2d4b9404bab1543a3eee81263b4a507ebf5d289d8fad1fbcdd59da820951e3e0f9b0b0b3d1bad9b41338804e7c42a8a6197c6e9"' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=sclorpmpb4ngion5e996os22ao' \
--data-raw '{
    "accountId": "smsplus",
    "referenceId": "b5f2d8785768087678fn4",
    "amount": 10,
    "currency": "INR",
    "paymentSource": "WEB",
    "paymentMethod": {
        "name": "NetBanking",	
        "bankCode": "TESTNB"
    },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "string",
                "quantity": 1
            }
        ],
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "udf6": "",
            "udf7": "",
            "udf8": "",
            "udf9": "",
            "udf10": ""
        },
        "paymentChargeSpecification": {
            "price": 10,
            "convenienceFee": "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55",
            "offers": {
                "applied": [
                    {
                        "offerId": "no_offer",
                        "amount": null
                    }
                ]
            }
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "createOrder": "false"
    },
    "callBackActions": {
        "successAction": "https://apitest.payu.in/test_response",
        "failureAction": "https://apitest.payu.in/test_response",
        "cancelAction": "https://apitest.payu.in/test_response"
    },
    "billingDetails": {
        "firstName": "sartaj",
        "lastName": "",
        "phone": "9876543210",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    },
     "beneficiaryDetail": {
                  "beneficiaryName": "Ram",
                  "beneficiaryAccountNumber": "115501029190",
                  "beneficiaryAccountType": "SAVINGS"
    }
}'
```

### Sample response

> 📘 Note:
> 
> Reverse hashing of the response is not required with that of v2/payment API.

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

## Step 2: Verify the payment

Verify the transaction details using the Verification APIs. For more information, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Tip
> 
> The transaction ID that you posted in Step 1 with PayU must be used here.

## Check Net Banking health

You can check whether the Net Banking server is up and running using the **getNetBankingStatus** API. If the Net Banking server is down for a bank, you can inform your customers that the Net Banking server is down. For more information on the **getNetBankingStatus** API, refer to [Get Net Banking Status API](https://docs.payu.in/v1/reference/get_net_banking_status_api).