---
title: Absolute Split During Transaction - v2 Payment API
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
You can split during the transaction by amount, where you must ensure that the sum of all splits is equal to the parent transaction amount.

> 📘 Note:
> 
> You must specify two decimal places for each split, but ensure that the sum of split amounts equals the transaction amount.

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Long</code> Amount of the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>currency<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Currency of the transaction (e.g., INR). By default, <strong>INR</strong> is posted.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>INR</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to <a href="#additionaiInfo-object-fields-description">additionalInfo object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>callBackActions<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to <a href="#callbackactions-object-fields-description">callbackActions object fields description</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>billingDetails <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-field-descriptions">billingDetails object field descriptions</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitRequest <code>mandatory for Split Settlement</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Details about the split payment. For more information, refer to <a href="#splitrequest-object-fields-description">splitRequest object fields description.</a></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> {<br>                  &quot;type&quot;: &quot;absolute&quot;,<br>                  &quot;splitInfo&quot;: {<br>                    &quot;123412&quot;: {<br>                      &quot;aggregatorSubTxnId&quot;: &quot;12312941&quot;,<br>                      &quot;aggregatorSubAmt&quot;: &quot;2000.55&quot;<br>                    },<br>                    &quot;2300019&quot;: {<br>                      &quot;aggregatorSubTxnId&quot;: &quot;12312941&quot;,<br>                      &quot;aggregatorSubAmt&quot;: &quot;134.23&quot;<br>                    }<br>                  }</p>
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>. For example, for credit card, this must contain <strong>CreditCard</strong>.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br> <code>mandatory</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This field must contain the bank code. For more information, refer to <a href="https://docs.payu.in/v1/docs/bank-and-card-codes-for-integration">Bank and Card Codes for Integration</a> based on payment mode code in the <strong>name</strong> filed.</p>
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


### splitRequest object fields description

The following fields are included in the **splitRequest** parameter in a JSON format to specify the absolute split details. The fields in the JSON format are described in the following table:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>type<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Specify the <strong>absolute</strong> type of split in this field. The absolute amount is specified in the <strong>aggregatorSubAmt</strong> field of the JSON for each child or aggregator.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>absolute</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>splitInfo<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>JSON</code> This parameter must include the list of aggregator sub transaction IDs and sub amounts as follows:  </p>
<ul>
<li><strong>aggregatorSubTxnId</strong>: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.</li>
<li><strong>aggregatorSubAmt</strong>: The transaction amount or percentage split for the aggregator is posted in this parameter. This field is mandatory.</li>
<li><strong>aggregatorCharges</strong> (optional): The transaction amount or percentage split for aggregator charges is posted in this parameter. This field is optional.<br><strong>Note</strong>: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>{<br>&quot;merchantKey1&quot;: {<br>&quot;aggregatorSubTxnId&quot;: &quot;30nknyhkhib&quot;,<br>&quot;aggregatorSubAmt&quot;: &quot;8&quot;<br>} </p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


#### JSON request structure of splitInfo

The sample JSON structure for the **splitInfo** field:

> 📘 Notes:
> 
> - Before peruse the following sample code, remove the white spaces as some editors may introduce junk characters.

```plaintext
{
   "type":"absolute",
   "splitInfo":{
      "P****Y":{
         "aggregatorSubTxnId":"9a70ea0155268**1001ba",
         "aggregatorSubAmt":"50",
         "aggregatorCharges":"20"
      },
      "P***K":{
         "aggregatorSubTxnId":"9a70ea0155268**1001bb",
         "aggregatorSubAmt":"30"
      }
   }
}
```

## Sample request

```
curl --location 'http://localhost:8080/apilayer/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
--data-raw '{
                "accountId": "smsplus",
                "referenceId": "b5f2d8785768087678fn4",
                "amount": 10,
                "currency": "INR",
                "paymentSource": "WEB",
                "paymentMethod": {
                  "name": "CC",
                  "bankCode": "CC",
                  "paymentCard": {
                    "cardNumber": 5123456789012346,
                    "validThrough": "04/2022",
                    "ownerName": "Sartaj",
                    "alternateName": "doe,John",
                    "cvv": 987
                  }
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
                    "price": 10
                  }
                },
                "additionalInfo": {
                  "createOrder": "false"
                },
                "callBackActions": {
                  "successAction": "https://pp78admin.payu.in/test_response",
                  "failureAction": "https://pp78admin.payu.in/test_response",
                  "cancelAction": "https://pp78admin.payu.in/test_response"
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
                "splitRequest": {
                  "type": "absolute",
                  "splitInfo": {
                    "123412": {
                      "aggregatorSubTxnId": "12312941",
                      "aggregatorSubAmt": "2000.55"
                    },
                    "2300019": {
                      "aggregatorSubTxnId": "12312941",
                      "aggregatorSubAmt": "134.23"
                    }
                  }
                }
              }
            }
          }'
```

## Check the response from PayU

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

### Sample response with Verify Payment API for Split payments

#### TDR model

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 4123**678**2383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => A****J
    [txnid] => 9a70ea0155268101001b
    [amount] => 100.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 100
    [addedon] => 2021-12-22 19:02:15
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
    [hash] => 6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a
    [field1] => 558**9955**14671900181
    [field2] => 113476
    [field3] => 100.00
    [field4] => 412*456789***83977
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 55**299554**4671900181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 5**345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[{"merchantKey":"P****Y","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba"},{"merchantKey":"P****K","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb"},{"merchantKey":"s****r","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b"}]}
)
```

> 📘 Note:
> 
> In the response, the amount shown in the **amount** field includes the amount shown in the **subvention\_amount** field.

#### Convenience model

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 412**567**12383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => A****J
    [txnid] => 9a70ea0155268101001b
    [amount] => 110.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 110
    [addedon] => 2021-12-22 19:02:15
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
    [hash] => 6e700275583072c0361bac771a4166a4be5334112d59e40181c5668895c477a047c7be250068186fd26ca72928d7e168f92bb96003a7fffbf4933bb818f4c48a
    [field1] => 5582299554914671900181
    [field2] => 113476
    [field3] => 110.00
    [field4] => 4123**67891**83977
    [field5] => 110
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 55**2995549**6719**181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 5**2345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[
				{"merchantKey":"P****Y","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba", “discount":0,"additionalCharges":0,”transaction_fee":0”},
				{"merchantKey":"P****K","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb", “discount":0,"additionalCharges":0,”transaction_fee":0”},
				{"merchantKey":"s****r","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b", “discount":0,"additionalCharges":0,”transaction_fee”:10”}
			]}
)
```