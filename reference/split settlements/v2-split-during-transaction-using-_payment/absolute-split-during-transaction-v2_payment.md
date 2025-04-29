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
| **Test Environment**       | <https://apitest.payu.in/v2/payments> |
| **Production Environment** | <https://api.payu.in/v2/payments>     |

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

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "accountId  \n `mandatory`",
    "0-1": "`String` The merchant key provided by PayU during onboarding.",
    "0-2": "MERCHANT123",
    "1-0": "referenceId  \n `mandatory`",
    "1-1": "`String` Reference ID for transaction tracking and this must be unique for every transaction.",
    "1-2": "REF123456",
    "2-0": "amount  \n `optional`",
    "2-1": "`Long` Amount of the transaction.",
    "2-2": "1000",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String` Currency of the transaction (e.g., INR). By default, **INR** is posted.",
    "3-2": "INR",
    "4-0": "paymentMethod  \n `mandatory`",
    "4-1": "`Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentmethod-object-fields-description).",
    "4-2": " {  \n        \"name\": \"NetBanking\",\t  \n        \"bankCode\": \"TESTNB\"  \n    }",
    "5-0": "order  \n `mandatory`",
    "5-1": "`Object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)",
    "5-2": "",
    "6-0": "additionalInfo  \n `mandatory`",
    "6-1": "`Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionaiInfo-object-fields-description)",
    "6-2": "",
    "7-0": "callBackActions  \n `mandatory`",
    "7-1": "`Object` Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to [callbackActions object fields description](#callbackactions-object-fields-description)",
    "7-2": " {",
    "8-0": "billingDetails `mandatory`",
    "8-1": "`Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).",
    "8-2": "",
    "9-0": "splitRequest `mandatory for Split Settlement`",
    "9-1": "`Object` Details about the split payment. For more information, refer to [splitRequest object fields description.](#splitrequest-object-fields-description)",
    "9-2": " {  \n                  \"type\": \"absolute\",  \n                  \"splitInfo\": {  \n                    \"123412\": {  \n                      \"aggregatorSubTxnId\": \"12312941\",  \n                      \"aggregatorSubAmt\": \"2000.55\"  \n                    },  \n                    \"2300019\": {  \n                      \"aggregatorSubTxnId\": \"12312941\",  \n                      \"aggregatorSubAmt\": \"134.23\"  \n                    }  \n                  }"
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### paymentMethod object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "name  \n `mandatory`",
    "0-1": "`String` This field must contain the payment mode code. For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/docs/payment-mode-codes). For example, for credit card, this must contain **CreditCard**.",
    "1-0": "bankCode  \n `mandatory`",
    "1-1": "`String`This field must contain the bank code. For more information, refer to [Bank and Card Codes for Integration](https://docs.payu.in/v1/docs/bank-and-card-codes-for-integration) based on payment mode code in the **name** filed."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


### order object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "productInfo  \n `mandatory`",
    "0-1": "`String`Details about the product being purchased. For more information, refer to[ userDefinedFields object fields description](#userdefinedfields-object-fields-description).",
    "1-0": "userDefinedFields  \n `optional`",
    "1-1": "`Object`Custom fields defined by the user for additional information.",
    "2-0": "paymentChargeSpecification  \n `mandatory`",
    "2-1": "`Object` Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to [paymentChargeSpecification object fields description](#paymentchargespecification-object-fields-description)."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "price  \n`mandatory`",
    "0-1": "This field must contain the price or transaction amount to be posted.",
    "0-2": "10.00"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

### billingDetails object field descriptions

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "firstName  \n`mandatory`",
    "0-1": "First name of the billing contact",
    "0-2": "Ashish",
    "1-0": "lastName  \n`optional`",
    "1-1": "Last name of the billing contact",
    "1-2": "Kumar",
    "2-0": "phone  \n`mandatory`",
    "2-1": "Phone number of the billing contact",
    "2-2": "9123456789",
    "3-0": "email  \n`mandatory`",
    "3-1": "Email address of the billing contact",
    "3-2": "[ashish@abc.com](mailto:ashish@abc.com)",
    "4-0": "city  \n`optional`",
    "4-1": "City of the billing address",
    "4-2": "Bengaluru",
    "5-0": "state  \n`optional`",
    "5-1": "State of the billing address",
    "5-2": "Karnatka",
    "6-0": "country  \n`optional`",
    "6-1": "Country of the billing address",
    "6-2": "Indiia",
    "7-0": "zipCode  \n`optional`",
    "7-1": "Postal/Zip code of the billing address",
    "7-2": "560071"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### splitRequest object fields description

The following fields are included in the **splitRequest** parameter in a JSON format to specify the absolute split details. The fields in the JSON format are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "type  \n**mandatory**",
    "0-1": "`string` Specify the **absolute** type of split in this field. The absolute amount is specified in the **aggregatorSubAmt** field of the JSON for each child or aggregator.",
    "0-2": "absolute",
    "1-0": "splitInfo  \n**mandatory**",
    "1-1": "`JSON` This parameter must include the list of aggregator sub transaction IDs and sub amounts as follows:  \n  \n- **aggregatorSubTxnId**: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.\n- **aggregatorSubAmt**: The transaction amount or percentage split for the aggregator is posted in this parameter. This field is mandatory.\n- **aggregatorCharges** (optional): The transaction amount or percentage split for aggregator charges is posted in this parameter. This field is optional.  \n  **Note**: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.",
    "1-2": "{  \n\"merchantKey1\": {  \n\"aggregatorSubTxnId\": \"30nknyhkhib\",  \n\"aggregatorSubAmt\": \"8\"  \n} "
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


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