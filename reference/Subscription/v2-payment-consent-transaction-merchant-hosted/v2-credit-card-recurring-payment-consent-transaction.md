---
title: Cards Consent Transaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: >-
    Explore how to set up a Cards (Debit or Credit) Recurring Payment Consent
    Transaction using PayU Hosted Checkout. This API documentation provides
    details for integrating Cards consent API, enabling secure and efficient
    recurring payments for your customers
  keywords:
    - PayU Cards Recurring Payment for Custom Checkout
    - ' Cards Consent Transaction for Custom Checkout'
    - ' PayU Cards Recurring Payment for Merchant Hosted Checkout'
    - ' Cards Consent Transaction for Merchant Hosted Checkout'
    - ' PayU recurring payments for Cards'
    - ' PayU subscription payments registration for Credit Cards'
    - ' Credit Card Registration transaction for Custom Checkout'
    - Credit Cards Registration transaction for Merchant Hosted Checkout
    - ' Cards Autopay'
    - ' Autopay for Cards non-PACB flow'
    - ' Cards Autopay Consent Transaction'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
---
This section provides the request parameters, sample request and response for a Cards Recurring Payment \<\<glossary:Consent transaction>>.

> 📘 Note:
> 
> During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

HTTP Method: **POST**

**Environment**

|                            |                                       |
| :------------------------- | :------------------------------------ |
| **Test Environment**       | \<https://apitest.payu.in/v2/payments> |
| **Production Environment** | \<https://api.payu.in/v2/payments>     |

## Request parameters

### Request header

| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Field     | Description                                                                                                                                                                      |
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

### Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>accountId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This must contain the key provided by PayU while onboarding.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Reference ID for transaction tracking and this must be unique for every transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Amount of the transaction.<br><strong>Note</strong>: This value will not be considered as the transaction. Only the details in the <code> order.paymentChargeSpecificationparameter</code> field will be considered.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Currency of the transaction (e.g., INR).  By default, <strong>INR</strong> is posted.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalInfo<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to <a href="#additionaiinfo-object-fields-description">additionalInfo object fields description</a>.<br><strong>Note</strong>: The <code>txnFlow</code> field in this JSON object must be set to <strong>nonseamless</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to<a href="#callbackactions-object-fields-description"> callbackActions object fields description</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to<a href="#billingdetails-object-fields-descriptions"> billingDetails object fields descriptions</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>siDetails<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code> Subscription or SI details for the consent transaction. For more information, refer to<a href="#sidetails-object-fields-description"> siDetails object fields description</a>.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>. For cards, this must contain any of the following:  </p>
<ul>
<li>creditcard for credit card</li>
<li>debitcard for debit card</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the bank code. For more information, refer to <a href="https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCard<br> <code>mandatory for cards</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code>This object will contain the physical card or saved card token details. For more information, refer to<a href="#paymentcard-object-fields-description"> paymentCard object fields description</a>.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


#### paymentCard object fields description

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardNumber<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card number. For validating the card number, refer to <a href="https://docs.payu.in/v1/docs/card-number-formats">Card Number Formats</a>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>validThrough<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card expiry in MM/YYYY format.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ownerName<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the name of the card holder as printed on card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cvv<br> <code>mandatory for physical card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the CVV printed on the back of the card.  </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>tavv<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the cryptogram of card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>last4Digits<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the last four digits of card.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardTokenType<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the any of the following based on the:  </p>
<ul>
<li>PAYU</li>
<li>NETWORK</li>
<li>ISSUER&quot;</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardToken<br> <code>mandatory for saved card</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the card token of stored card.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


### additionalInfo object fields description

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>forcePgid<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Force identification for payment gateway integration.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>si<br><code>mandatory for Subscriptions</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain any of the following:  </p>
<ul>
<li><strong>1</strong>: SI is not enabled.</li>
<li><strong>2</strong>: SI is enabled.</li>
</ul>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>partnerHoldTime<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Time held by partner for the transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>userCredentials<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Credentials for user authentication during payment.</p>
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


> ❗️ Error Handling
> 
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

<br />

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


<br />

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


## Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
    "accountId": "UMXDPA",
    "referenceId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",	
        "bankCode": "CC", 		
        "paymentCard": {	
            "cardNumber": 5004461234560000,	
            "validThrough": "04/2022",
            "ownerName": "Sartaj",
            "cvv": 987,		
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
            "last4Digits": "0000",
            "cardTokenType": "NETWORK",	
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1"
        }
    },
    "order": {
        "productInfo": "string",
        "orderedItem": [
            {
                "itemId": null,	
                "description": "AAA", 
                "quantity": null,
                "amount" : 10.0
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
        }
  },   
    },
    "additionalInfo": { 
        "enforcePaymethod": "CC,DC",
        "si": "2"
    },
    "callBackActions": {
        "successAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction",
        "failureAction": "https://testapi.payu.in/admin/testresponsev2?action=failureAction",
        "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction",
        "codAction": "https://testapi.payu.in/admin/testresponsev2?action=codAction",
        "termAction": "string",
        "timeOutAction": null,
        "returnAction": "https://testapi.payu.in/admin/testresponsev2?action=successAction"
    },
  "billingDetails": {
    "firstName": "sartaj",
    "lastName": "",
    "address1": "Test Payu Gurgaon",
    "address2": "",
    "city": "Bharatpur",
    "state": "Rajasthan",
    "country": "India",
    "zipCode": "321028",
    "phone": "9876543210",
    "email": "testv2@example.in"
  },
     "siDetails": {
       "billingCycle": "MONTHLY",
       "billingAmount": "1.00",
       "billingCurrency": "INR",
       "billingInterval": 1,
       "paymentStartDate": "2020-09-16",
       "paymentEndDate": "2020-10-16",
       "siTokenRequestor": "",
       "authpayuid": "",
       "action": ""
      }

}'
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the reference ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the payment ID of the transaction.<br>statusCode</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the status message of the transaction.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


## Sample response

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
> 
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](https://docs.payu.in/v1/reference/set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).