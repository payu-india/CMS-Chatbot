---
title: Non-seamless - Preauth Transaction API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Non-seamless - Preauth Transaction
deprecated: false
hidden: false
metadata:
  robots: index
---
The Collect Payment API (**v2 Payment** API) with the **preAuthorize=1** in the **additionalInfo** object.

> 📘 Note:
>
> You must use the **additionalInfo.txnFlow** must be set to **nonseamless** for PayU Hosted Checkout.

> 📘 Reference:
>
> To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](https://docs.payu.in/v1/docs/handling-the-redirect-urls).

**Environment**

|                            |                                                                              |
| :------------------------- | :--------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://apitest.payu.in/v2/payments](https://apitest.payu.in/v2/payments) |
| **Production Environment** | \<[https://api.payu.in/v2/payments>](https://api.payu.in/v2/payments>)       |

## Request header

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

Where, \<Body data> contains the request Body posted with the request.

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

## Request body

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>The merchant key provided by PayU during onboarding.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Reference ID for transaction tracking. This must be unique for each transaction.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentStatus<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Indicates the status of the payment. For example, SUCCESS.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Amount of the transaction.<br><strong>Note</strong>: This value will not be considered as the transaction. Only the details in the <code> order.paymentChargeSpecification.price</code> field will be considered.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Currency of the transaction. For example, INR.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentSource<code> optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Contains the payment source. For example, WEB.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON Object</code>Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.<br><strong>Note</strong>: The <code>txnFlow</code> field in this JSON object must be set to <strong>nonseamless</strong>.</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>enforcePaymethod<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Methods of payment that are enforced in the payment process. For more information, refer to <a href="https://docs.payu.in/v2/docs/enforce-pay-method-or-remove-category">Enforce Pay Method or Remove Category</a>.</p>
</td>
  </tr><tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnFlow<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Specify "nonseamless" for non-seamless integration.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>createOrder<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Indicates whether to create an order on PayU's side. Set to "true" to create an order, or "false" otherwise.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>preAuthorize<br> <code>mandatory for Preauth</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When set to "1", the transaction will be in pre-authorized state and funds will be captured later.</p>
</td>
</tr></tbody>
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

<V2_Error_Handling />

#### order object fields description

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Details about the product being purchased.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderedItem<br> <code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array</code>List of items included in the order. Each item can include details such as <code>itemId</code>, <code>description</code>, and <code>quantity</code>.</p>
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

##### userDefinedFields object fields description

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

##### paymentChargeSpecification object fields description

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

#### billingDetails object field descriptions

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address1<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Primary address line of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Test Payu Gurgaon</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>address2<br><code>optional</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Secondary address line of the billing contact</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Sector 32</p>
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
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data '{
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fm9",
  "paymentStatus": "SUCCESS",
  "amount": 10,
  "currency": "INR",
  "paymentSource": "WEB",
  "order": {
    "productInfo": "string",
    "orderedItem": [
      {
        "itemId": null,
        "description": "AAA",
        "quantity": null
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
      "price": 10
    }
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder": "false",
    "preAuthorize": "1"
  },
  "callBackActions": {
    "successAction": "https://pp78admin.payu.in/test_response",
    "failureAction": "https://pp78admin.payu.in/test_response",
    "cancelAction": "https://testapi.payu.in/admin/testresponsev2?action=cancelAction"
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
  }
}'
```

### Response parameters

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
{
  "result": {
    "checkoutUrl": "https://pp78secure.payu.in/_payment_options?mihpayid=<mihpayuid>&userToken="
  },
  "status": "PENDING"
}

```

> 📘 Reference:
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).