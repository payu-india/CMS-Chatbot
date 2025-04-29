---
title: BNPL - v2 Payment API
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
Buy Now Pay Later (<<glossary:BNPL>>) allows your customers to spread their payments over a relatively short period instead of paying upfront. You can collect payments from customers with BNPL using the Merchant Hosted Checkout integration.

You can collect payments from customers in EMI using the Merchant Hosted integration. You need to ensure that **BNPL** for the **paymentMethod.name** parameter and BNPL code based on the provider and tenure for the **paymentMethod.bankcode** parameter is posted.

**Environment**

|                            |                                       |
| :------------------------- | :------------------------------------ |
| **Test Environment**       | <https://apitest.payu.in/v2/payments> |
| **Production Environment** | <https://api.payu.in/v2/payments>     |

## Request parameters

### Request Header

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

<br />

### Request Body

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
    "2-1": "`String` Amount of the transaction.  \n**Note**: This value will not be considered as the transaction. Only the details in the `order.paymentChargeSpecificationparameter.price`field will be considered.",
    "2-2": "1000",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String` Currency of the transaction. By default, `INR` is posted.",
    "3-2": "INR",
    "4-0": "paymentSource`\noptional`",
    "4-1": "`String`Contains the payment source.",
    "4-2": "WEB",
    "5-0": "paymentMethod  \n `mandatory`",
    "5-1": "`Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentmethod-object-fields-description).",
    "5-2": " {  \n        \"name\": \"NetBanking\",\t  \n        \"bankCode\": \"TESTNB\"  \n    }",
    "6-0": "order  \n `mandatory`",
    "6-1": "`Object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)",
    "6-2": "",
    "7-0": "additionalInfo  \n `mandatory`",
    "7-1": "`Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description)",
    "7-2": "",
    "8-0": "callBackActions  \n `mandatory`",
    "8-1": "`Object` Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to [callbackActions object fields description](#callbackactions-object-fields-description)",
    "8-2": " ",
    "9-0": "billingDetails  \n`mandatory`",
    "9-1": "`Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).",
    "9-2": ""
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
    "0-1": "`String` This field must contain the payment mode code. For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/docs/payment-mode-codes). For UPI, this must contain **BNPL**.",
    "1-0": "bankCode  \n`mandatory`",
    "1-1": "`String`This field must contain the bank code. For BNPL bank codes, refer to [BNPL Codes](https://docs.payu.in/v1/docs/bnpl-codes)."
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
    "0-1": "`String`Details about the product being purchased. For more information, refer to[ userDefinedFields object fields description](#userdefinedFields-object-fields-description).",
    "1-0": "userDefinedFields  \n `optional`",
    "1-1": "`Object`Custom fields defined by the user for additional information.",
    "2-0": "paymentChargeSpecification  \n `mandatory`",
    "2-1": "`Object` Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to [paymentChargeSpecification object fields description](#paymentchargeSpecification-object-fields-description)."
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


### callbackActions object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "successAction  \n `mandatory`",
    "0-1": "`String`URL to redirect to upon successful payment.",
    "1-0": "failureAction  \n `mandatory`",
    "1-1": "`String`URL to redirect to if the payment is failed.",
    "2-0": "cancelAction  \n `mandatory`",
    "2-1": "`String`URL to redirect to if the transaction is cancelled.",
    "3-0": "codAction  \n `optional`",
    "3-1": "`String`URL to handle Cash on Delivery actions.",
    "4-0": "termAction  \n `optional`",
    "4-1": "`String`URL for completing terms and conditions actions.",
    "5-0": "returnAction  \n `optional`",
    "5-1": "`String`URL to return to after successful payment action is completed."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


> ❗️ Error Handling
> 
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

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


## Sample request

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
        "name": "BNPL",	
        "bankCode": "LAZYPAY" 		
     },
    "order": {
        "productInfo": "qwertyuiopasdfghjkl",
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
        "txnS2sFlow": "4",
        "createOrder": "false"
    },
    "callBackActions": {
        "successAction": "https://apitest.payu.in/test_response",
        "failureAction": "https://apitest.payu.in/test_response",
        "cancelAction": "https://apitest.payu.in//test_response"
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
    }
}'
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "referenceId",
    "0-1": "This parameter contains the reference ID of the transaction.  \nstatusCode",
    "1-0": "paymentId",
    "1-1": "This parameter contains the payment ID of the transaction.  \nstatusCode",
    "2-0": "message",
    "2-1": "This parameter contains the status message of the transaction."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


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