---
title: Cards  - v2 Payment API
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
You can collect payments from customers with leading wallets using the Merchant Hosted integration. You need to ensure that **CreditCard** or **DebitCard** for the **paymentMethod.name** parameter and  card code based on the desired card provider for the **paymentMethod.bankcode** parameter is posted.

> 📘 Note:
>
> PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).

**Environment**

|                            |                                                                                |
| :------------------------- | :----------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://apitest.payu.in/v2/payments>](https://apitest.payu.in/v2/payments>) |
| **Production Environment** | \<[https://api.payu.in/v2/payments>](https://api.payu.in/v2/payments>)         |

## Request parameters

### Request header

| Parameter     | Description                                                                                                                                                                                                    |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date          | The current date and time. For example,  format of the date is Wed, 28 Jun 2023 11:25:19 GMT.                                                                                                                  |
| authorization | The actual HMAC signature generated using the specified algorithm (sha512) and includes the hashed data. For more information, refer to[ authorization fields description](#authorization-fields-description). |

#### authorization fields description

| Field     | Description                                                                                                                         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| username  | Represents the username or identifier for the client or merchant, for example smsplus.                                              |
| algorithm | Indicates the hashing algorithm used for the HMAC signature, for example sha512.                                                    |
| headers   | Specifies which headers have been used in generating the hash, for example date.                                                    |
| signature | The HMAC signature generated using the specified algorithm. For more information, refer to [hashing algorithm](#hashing-algorithm). |

#### hashing algorithm

Yo must hash the request parameters using the following hash logic:

**Hash logic**: sha512(`<Body data>` + '|' + date + '|' + merchant\_secret)

Where `<Body data>` contains the request body posted with the request.

<details>
  <summary>Sample header code</summary>

  ```javascript
  var merchant_key = 'smsplus';
  var merchant_secret = 'izF09TlpX4ZOwmf9MvXijwYsBPUmxYHD';
  // date
  var date = new Date();
  date = date.toUTCString();

  // authorization
  var authorization = getAuthHeader(date);

  function getAuthHeader(date) {
      var AUTH_TYPE = 'sha512';
      var data = isEmpty(request['data']) ? "" : request['data'];
      var hash_string = data + '|' + date + '|' + merchant_secret;
      var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
      return `hmac username="${merchant_key}", algorithm="${AUTH_TYPE}", headers="date", signature="${hash}"`;
  }
  ```
</details>

## Request body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>accountId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the merchant key provided by PayU during onboarding.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">MERCHANT123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Transaction ID for transaction tracking. Must be unique for every transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">TXN123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>amount</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Amount of the transaction. This will not be considered as the transaction amount, only the order.paymentChargeSpecification.price field will be considered.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentMethod</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains details of the payment method.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>order</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains transaction order details such as product info, ordered items, user-defined fields, and payment charge details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Additional metadata for the transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>callBackActions</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL actions for payments (e.g., success, failure, cancel).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>billingDetails</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Customer billing details including name, phone, and address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authorization</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Authorization details for the payment process, including 3DS metadata.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDS2RequestData</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Version and device details for advanced authentication flows.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>siDetails</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Standing Instructions details for recurring payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>splitDetails</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Split payment details for multi-recipient transactions.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentMethod

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>name</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Represents the payment method used. Valid values: CreditCard, DebitCard, NetBanking, UPI, EMI, Wallet, CashCard, COD, Challan, LazyPay, PayPal, Sodexo, Payout, CLEMI, ENACH, qr, neftrtgs.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains the bank code. Valid values: CC, MAST, VISA.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentCard</strong><br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardNumber</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card number.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">5497774415170603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>validThrough</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Expiry date in MM/YYYY format.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05/2025</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>ownerName</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Name of the card owner.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Ashish</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cvv</strong><br/><code>mandatory for physical card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">CVV number of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>tavv</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cryptogram of the card for tokenized payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>last4Digits</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Last four digits of the card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">0603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardTokenType</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token type. Valid values: PAYU, NETWORK, ISSUER.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">PAYU</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cardToken</strong><br/><code>mandatory for saved card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card token of the stored card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">b5f2d8785768087678fm9</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### order

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>productInfo</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Product details.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Product details</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>orderedItem</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Details about the items ordered.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Array of Objects</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userDefinedFields</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Custom fields for additional information. Fields: udf1, udf2, udf3, udf4, udf5, udf6, udf7, udf8, udf9, udf10.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentChargeSpecification</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Includes amount and charges.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### orderedItem

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>itemId</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Unique product item ID in the order.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>description</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Description of the ordered item.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Product A</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>quantity</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Quantity of the ordered item.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>amount</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Price per unit of the item.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentChargeSpecification

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>price</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">The transaction amount.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>netAmountDebit</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Net amount to be debited.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">1000</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>taxSpecification</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Tax details of the product/order.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>convenienceFee</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Fees format (e.g., CC:12).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC:12</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>offers</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Offers applied or available for the payment.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### additionalInfo

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>enforcePaymethod</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Force a transaction with a specified method (e.g., CC, DC).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>forcePgid</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Forces identification for payment gateway.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">PG123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>partnerHoldTime</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Time held by the partner for the transaction.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">60</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userCredentials</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Credentials for user authentication.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">string</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>userToken</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Token for the customer.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">user_token_123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>subventionAmount</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Amount paid through EMI subvention payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">100</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>authOnly</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Initiates an authentication-only payment (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">false</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">A flag to store the order details (true/false).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">For defining seamless/non-seamless flows in handling payments.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">seamless</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### callBackActions

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>successAction</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called on payment success.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/success</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>failureAction</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called on payment failure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/failure</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cancelAction</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL to be called if user cancels the payment.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/cancel</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>codAction</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">URL for Cash on Delivery (COD) action.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">https://example.com/cod</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### billingDetails

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>firstName</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">First name of the billing contact.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Ashish</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>lastName</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Last name of the billing contact.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Kumar</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>address1</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Primary billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">123 Main Street</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>address2</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Secondary billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Apt 4B</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>phone</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Phone number of the billing contact.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">9123456789</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>email</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Email address of the billing contact.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">testv2@example.in</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>city</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">City of the billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Bharatpur</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>state</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">State of the billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Rajasthan</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>country</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Country of the billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">India</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>zipCode</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Postal/Zip code of the billing address.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">321028</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### authorization

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>eci</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Electronic Commerce Indicator.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">05</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>cavv</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cardholder Authentication Verification Value.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">AAABAWFlmQAAAABjRWWZEEFgFz</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>flowType</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Flow type for 3D Secure.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Frictionless</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransID</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">67b4c71f-19bf-4d97-bd09-4e3687dc9e42</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSServerTransID</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS Server Transaction ID.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">eea30d14-71cf-41af-b961-f95b7d67dc93</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransStatus</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Y</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSTransStatusReason</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Reason for 3DS transaction status.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">01</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>aquirer_bin</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Bank Identification Number of the acquirer.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">401200</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>additionalInfo</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object containing authUdf1 and authUdf2.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### threeDS2RequestData

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>threeDSVersion</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">The version of 3D Secure used.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">2.2.0</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>deviceChannel</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">The device used for the transaction channel.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">APP</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```json
{
    "accountId": "smsplus",
    "txnId": "b5f2d8785768087678fm9",
    "amount": "1000",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5497774415170603",
            "validThrough": "05/2025",
            "cvv": "123",
            "ownerName": "Ashish"
        }
    },
    "order": {
        "productInfo": "Product details",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product A",
                "quantity": 1,
                "amount": 1000
            }
        ],
        "userDefinedFields": {
            "udf1": "test1",
            "udf2": "test2",
            "udf3": "test3",
            "udf4": "test4",
            "udf5": "test5"
        },
        "paymentChargeSpecification": {
            "price": "1000"
        }
    },
    "additionalInfo": {
        "enforcePaymethod": "CC",
        "createOrder": true,
        "authOnly": false
    },
    "callBackActions": {
        "successAction": "https://checkout.payu.in/testCB/success",
        "failureAction": "https://checkout.payu.in/testCB/failure",
        "cancelAction": "https://checkout.payu.in/testCB/cancel"
    },
    "billingDetails": {
        "firstName": "Ashish",
        "lastName": "Kumar",
        "address1": "123 Main Street",
        "phone": "9123456789",
        "email": "testv2@example.in",
        "city": "Bharatpur",
        "state": "Rajasthan",
        "country": "India",
        "zipCode": "321028"
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "aquirer_bin": "401200",
        "additionalInfo": {
            "authUdf1": "string",
            "authUdf2": "string"
        }
    },
    "threeDS2RequestData": {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "APP"
    }
}
```

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnId</strong></td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter contains the transaction ID of the transaction.</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentId</strong></td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter contains the payment ID of the transaction.</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>message</strong></td>
  <td style="border: 1px solid #ddd; padding: 8px;">This parameter contains the status message of the transaction.</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

```
Array
(
    [txnId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

> 📘 Reference:
>
> To check the transaction status, refer to[Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).