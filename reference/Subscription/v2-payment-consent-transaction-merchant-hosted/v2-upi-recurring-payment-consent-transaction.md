---
title: UPI Consent Transaction
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: UPI Recurring Payment Consent Transaction
  description: >-
    Explore how to set up a UPI Recurring Payment Consent Transaction using
    Merchant Hosted Checkout. This API documentation for integrating PayU's
    Netbanking or Net Banking consent feature, enabling secure and efficient
    recurring payments for your customers.
  keywords:
    - PayU UPI Recurring Payment for Custom Checkout
    - ' UPI Consent Transaction for Custom Checkout'
    - ' PayU UPI Recurring Payment for Merchant Hosted Checkout'
    - ' UPI Consent Transaction for Merchant Hosted Checkout'
    - ' PayU recurring payments for UPI'
    - ' UPI Autopay'
    - ' Autopay for UPI non-PACB flow'
    - ' UPI Autopay Consent Transaction'
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
This section provides the request parameters, sample request and response for a UPI Recurring Payment <<glossary:Consent transaction>>.

> 📘 Note:
> 
> During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.

HTTP Method: **POST**

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
    "0-0": "accountId  \n `mandatory`",
    "0-1": "`String`This must contain the key provided by PayU while onboarding.",
    "1-0": "referenceId  \n `mandatory`",
    "1-1": "`String`Reference ID for transaction tracking and this must be unique for every transaction.",
    "2-0": "amount  \n `optional`",
    "2-1": "`String`Amount of the transaction.  \n**Note**: This value will not be considered as the transaction. Only the details in the ` order.paymentChargeSpecificationparameter` field will be considered.",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String`Currency of the transaction (e.g., INR).  By default, **INR** is posted.",
    "4-0": "order  \n `mandatory`",
    "4-1": "`JSON Object`Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)",
    "5-0": "additionalInfo  \n `mandatory`",
    "5-1": "`JSON Object`Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description).  \n**Note**: The `txnFlow` field in this JSON object must be set to **nonseamless**.",
    "6-0": "callBackActions  \n `mandatory`",
    "6-1": "`JSON Object`Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to[ callbackActions object fields description](#callbackactions-object-fields-description)",
    "7-0": "billingDetails  \n `mandatory`",
    "7-1": "`JSON Object`Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to[ billingDetails object fields descriptions](#billingdetails-object-fields-descriptions).",
    "8-0": "siDetails  \n `mandatory`",
    "8-1": "`JSON Object` Subscription or SI details for the consent transaction. For more information, refer to[ siDetails object fields description](#sidetails-object-fields-description)."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    null,
    null
  ]
}
[/block]


<br />

### paymentMethod object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "name  \n `mandatory`",
    "0-1": "`String` This field must contain the payment mode code. For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/docs/payment-mode-codes). For UPI, this must contain **UPI**.",
    "1-0": "bankCode  \n`mandatory`",
    "1-1": "`String`This field must contain the bank code. For UPI, this must contain **UPI**."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


### additionalInfo object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "vpa  \n`mandatory for UPI`",
    "0-1": "`String`UPI handle of the customer.",
    "1-0": "si  \n`mandatory for Subscriptions`",
    "1-1": "`String`This parameter must contain any of the following:  \n  \n- **1**: SI is not enabled.\n- **2**: SI is enabled.",
    "2-0": "userCredentials  \n `optional`",
    "2-1": "`String`Credentials for user authentication during payment."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


| Field | Description |
| ----- | ----------- |
|       |             |

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

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "udf1  \n `optional`",
    "0-1": "User defined field.",
    "1-0": "udf2  \n `optional`",
    "1-1": "User defined field.",
    "2-0": "udf3  \n `optional`",
    "2-1": "User defined field.",
    "3-0": "udf4  \n `optional`",
    "3-1": "User defined field.",
    "4-0": "udf5  \n `optional`",
    "4-1": "User defined field.",
    "5-0": "udf6  \n `optional`",
    "5-1": "User defined field.",
    "6-0": "udf7  \n `optional`",
    "6-1": "User defined field.",
    "7-0": "udf8  \n `optional`",
    "7-1": "User defined field.",
    "8-0": "udf9  \n `optional`",
    "8-1": "User defined field.",
    "9-0": "udf10  \n `optional`",
    "9-1": "User defined field."
  },
  "cols": 2,
  "rows": 10,
  "align": [
    null,
    null
  ]
}
[/block]


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
        "name": "UPI",	
        "bankCode": "UPI" 		
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
    "additionalInfo": { 
        "vpa": "xyz@axis",
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

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws\_online\_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](https://docs.payu.in/v1/reference/set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank)