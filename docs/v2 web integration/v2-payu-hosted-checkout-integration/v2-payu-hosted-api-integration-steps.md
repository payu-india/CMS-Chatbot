---
title: API Integration - PayU Hosted
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
To integrate with PayU Hosted Checkout, you need to send a request and check the response. This will redirect the customer from the merchant’s website to PayU’s payment page to complete the payment. You can use the sample request and response in the provided documentation to get started.

> 👍 Before you begin:
> 
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

The steps involved in PayU Hosted Checkout integration are:

1. [Make the transaction request to PayU](#step-1-make-the-transaction-request-to-payu)
2. [Redirect the URL for Payment on customer browser](#step-2-redirect-the-url-for-payment-on-customer-browser)
3. [Handle the redirection on surl/furl](#step-3-handle-the-redirection-on-surlfurl)
4. [Verify the payment](#step-4-verify-the-payment)

## Step 1: Make the transaction request to PayU

Make the transaction request to the PayU Test server.

The Collect Payment (**v2/payments**) API is used for collecting payments in Web Checkout integration. For request and response, refer to <a href="https://docs.payu.in/v2/reference/collect-payment-api-payu-hosted-v2-_payment" target="_blank">Collect Payments API</a> under API Reference.

|                            |                                       |
| :------------------------- | :------------------------------------ |
| **Test Environment**       | <https://apitest.payu.in/v2/payments> |
| **Production Environment** | <https://api.payu.in/v2/payments>     |

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

### Request body

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "accountId  \n `mandatory`",
    "0-1": "`String`The merchant key provided by PayU during onboarding.",
    "1-0": "referenceId  \n `mandatory`",
    "1-1": "`String`Reference ID for transaction tracking. This must be unique for each transaction.",
    "2-0": "amount  \n `optional`",
    "2-1": "`String`Amount of the transaction.  \n**Note**: This value will not be considered as the transaction. Only the details in the ` order.paymentChargeSpecification.price` field will be considered.",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String`Currency of the transaction. For example, INR.",
    "4-0": "paymentSource`\noptional`",
    "4-1": "`String`Contains the payment source. For example, WEB.",
    "5-0": "order  \n `mandatory`",
    "5-1": "`JSON Object`Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)        ",
    "6-0": "additionalInfo  \n `mandatory`",
    "6-1": "`JSON Object`Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description)        .  \n**Note**: The `txnFlow` field in this JSON object must be set to **nonseamless**.",
    "7-0": "callBackActions  \n `mandatory`",
    "7-1": "`JSON Object`Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to[ callbackActions object fields description](#callbackactions-object-fields-description)        ",
    "8-0": "billingDetails  \n `mandatory`",
    "8-1": "`JSON Object`Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to[ billingDetails object fields descriptions](#billingdetails-object-fields-descriptions)        .",
    "9-0": "enforced_payment  \n`optional`",
    "9-1": "`String `This parameter is to customize the payment options for each transaction. You can enforce specific payment modes, cards scheme, and specific banks under Net Banking using this method. For more information, refer to [Enforce Pay Method or Remove Category.](https://docs.payu.in/v2/docs/enforce-pay-method-or-remove-category)    ",
    "10-0": "drop_category  \n`optional`",
    "10-1": "`String `This parameter is used if you want to hide one or multiple payment options. For example, if you consider the payment options such as credit card, debit card, and net banking, you can hide the credit card mode of payment. For more information, refer to [Enforce Pay Method or Remove Category.](https://docs.payu.in/v2/docs/enforce-pay-method-or-remove-category)    "
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


#### additionalInfo object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "enforcePaymethod  \n `optional`",
    "0-1": "`String`Methods of payment that are enforced in the payment process. For more information, refer to [Enforce Pay Method or Remove Category](https://docs.payu.in/v1/docs/enforce-pay-method-or-remove-category)        ."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


#### callbackActions object fields description

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

#### order object fields description

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


#### billingDetails object field descriptions

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


### Sample request

```curl
curl --location 'https://apitest.payu.in/v2/payments' \
--header 'date: Tue, 05 Nov 2024 06:12:57 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="d583ff8069c7dfa8340464a24bdd01cbebf4432b4dfe4de862065cc9c9dc622c24c77cb1ac1142bf581ec07eca8d0ec78a66db93f6cd557d0da552f05c0825e3"' \
--header 'Content-Type: application/json' \
--header 'mid: 8390470' \
--header 'X-CREDENTIAL-USERNAME: UMXDPA' \
{
  "accountId": "smsplus",
  "referenceId": "b5f2d8785768087678fm9",
  "paymentStatus": "SUCCESS",
  "amount": 10,
  "currency": "INR",
  "paymentSource": "WEB",
  },
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
  },
  "additionalInfo": {
    "txnFlow": "nonseamless",
    "createOrder" : "false"
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
}
```

## Step 2: Redirect the URL for Payment on customer browser

### Sample response

The response is similar to the following when parsed:

> 📘 Note:
> 
> Reverse hashing of the response is not required with that of v2/payment API.

```
{
  "result": {
    "checkoutUrl": "https://pp78secure.payu.in/_payment_options?mihpayid=<mihpayuid>&userToken="
  },
  "status": "PENDING"
}
```

You must get the URL in **checkoutUrl** parameter of response and redirect this URL in customer browser so that they make the payment.

## Step 3: Handle the redirection on surl/furl

After the payment is complete, you need redirect to surl (on success) or furl (on failure) based on the  response

## Step 4: Verify the payment

PayU recommends this step to reconcile with PayU’s database after you receive the response. Verify the transaction details using the Verification APIs. For API reference, refer to <a href="https://docs.payu.in/v2/reference/v2_verify_payment_api" target="_blank">Verify Payment API</a> under API Reference.

> 📘 Tip
> 
> The Transaction ID (txnid) value that you passed in request of Step 1 with PayU must be used here.

[block:tutorial-tile]
{
  "backgroundColor": "#018FF4",
  "emoji": "🦉",
  "id": "6799e9a9831cd5000f2328f1",
  "link": "https://docs.payu.in/v1/recipes/parse-the-verify-payment-api-response",
  "slug": "parse-the-verify-payment-api-response",
  "title": "Parse the Verify Payment API response"
}
[/block]


### Webhooks

For configuring webhooks, refer to [Webhooks for Payments](doc:webhooks).