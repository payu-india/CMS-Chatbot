---
title: Cards Direct Authorization Flow S2S - v2 Payment API
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
PayU enables merchants to process direct authorization for pre-authenticated transactions (external MPI/3DSS). This section describes how to integrate with PayU’s direct authorization flow. Initiate an authorization request with the payment details provided post a successful authentication through the MPI/3DSS as explained in this API Reference. 

> 📘 Note:
> 
> This API is backward compatible and you can continue to the existing integration parameters to process the 3DS 1.0.2 transactions.

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
    "3-1": "`String` Currency of the transaction (e.g., INR). By default, `INR` is posted.",
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
    "9-0": "deviceInfo  \n`mandatory for S2S`",
    "9-1": "`Object`Device info of the customer.  For more information, refer to[ deviceInfo object field descriptions](#deviceinfo-object-field-descriptions)  .",
    "9-2": "",
    "10-0": "authorization  \n`mandatory for S2S Direct Auth`",
    "10-1": "`Object`3DS authorization information.  For more information, refer to refer to[ authorization object field descriptions](#authorization-object-field-descriptions)   .",
    "10-2": "",
    "11-0": "threeDS2RequestData  \n`mandatory for S2S`",
    "11-1": "`Object` 3DS authorization information.  For more information, refer to refer to[threeDS2RequestData object field description](#threeds2requestdata-object-field-descriptions)   .",
    "11-2": ""
  },
  "cols": 3,
  "rows": 12,
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
    "0-1": "`String` This field must contain the payment mode code. For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/reference/payment-mode-codes). For cards, this must contain any of the following:  \n  \n- **creditcard** for credit card\n- **debitcard** for debit card",
    "1-0": "bankCode  \n `mandatory`",
    "1-1": "`String`This field must contain the bank code. For more information, refer to [Card Type Codes and Supported Banks for Cards](https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards)",
    "2-0": "paymentCard `mandatory for cards`",
    "2-1": "`Object`This object will contain the physical card or saved card token details. For more information, refer to[ paymentCard object fields description](#paymentcard-object-fields-description)."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


#### paymentCard object fields description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "cardNumber  \n `mandatory for physical card`",
    "0-1": "`String`This field must contain the card number. For validating the card number, refer to [Card Number Formats](https://docs.payu.in/v1/docs/card-number-formats).",
    "1-0": "validThrough  \n `mandatory for physical card`",
    "1-1": "`String`This field must contain the card expiry in MM/YYYY format.",
    "2-0": "ownerName  \n `mandatory for physical card`",
    "2-1": "`String`This field must contain the name of the card holder as printed on card.",
    "3-0": "cvv  \n `mandatory for physical card`",
    "3-1": "`String`This field must contain the CVV printed on the back of the card.  ",
    "4-0": "tavv  \n `mandatory for saved card`",
    "4-1": "`String`This field must contain the cryptogram of card.",
    "5-0": "last4Digits  \n `mandatory for saved card`",
    "5-1": "`String`This field must contain the last four digits of card.",
    "6-0": "cardTokenType  \n `mandatory for saved card`",
    "6-1": "`String`This field must contain the any of the following based on the:  \n  \n- PAYU\n- NETWORK\n- ISSUER\"",
    "7-0": "cardToken  \n `mandatory for saved card`",
    "7-1": "`String`This field must contain the card token of stored card."
  },
  "cols": 2,
  "rows": 8,
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
    "0-0": "txnS2sFlow  \n `mandatory for S2S`",
    "0-1": "`String` Indicates the transaction S2S flow type and must be set to **4** for Classic Integration.",
    "1-0": "authenticationFlow  \n `mandatory for S2S`",
    "1-1": "`String` Indicates the authentication flow type and must be set to **REDIRECT** for Classic Integration.",
    "2-0": "decodedS2sResponse  \n `mandatory for S2S`",
    "2-1": "`String` Indicates whether you want to use acsTemplate format and want to post data by the merchant (on your own).  Post it as **1** only if you do not want to use acsTemplate format and want to post data on your own."
  },
  "cols": 2,
  "rows": 3,
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


#### deviceInfo object field descriptions

| Field        | Description                                         | Example                         |
| ------------ | --------------------------------------------------- | ------------------------------- |
| platform     | The operating system or platform of the device      | Android                         |
| version      | The version of the platform or app                  | 11.0                            |
| ip           | The IP address of the device                        | 192.168.1.1                     |
| userAgent    | The user agent string from the device's browser     | Mozilla/5.0 (Linux; U)          |
| acceptHeader | The accept header information from the device       | text/html,application/xhtml+xml |
| language     | The preferred language setting of the device        | en-US                           |
| colorDepth   | The color depth of the device's display             | 24                              |
| screenHeight | The height of the device's screen in pixels         | 1920                            |
| screenWidth  | The width of the device's screen in pixels          | 1080                            |
| timeZone     | The time zone setting of the device                 | GMT+5:30                        |
| javaEnabled  | Boolean indicating if Java is enabled on the device | true                            |

#### authorization object field descriptions

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "eci  \n`mandatory`",
    "0-1": "`String`The electronic commerce indicator is used in payer authentication to indicate the level of security used when the cardholder provided payment information to the merchant. Its value corresponds to the authentication result and the characteristics of the merchant checkout process.",
    "0-2": "05",
    "1-0": "cavv  \n`mandatory`",
    "1-1": "`String`The Cardholder Authentication Verification Value (CAVV) is specified here.",
    "1-2": "AAABAWFlmQAAAABjRWWZEEFgFz",
    "2-0": "flowType  \n`mandatory`",
    "2-1": "`String`This field must contain any of the following flow types:  \n  \n- Frictionless\n- Challenge.",
    "2-2": "Frictionless",
    "3-0": "threeDSTransID  \n`mandatory`",
    "3-1": "`String`This field must contain the 3DS transaction ID.",
    "3-2": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
    "4-0": "threeDSServerTransID  \n`mandatory`",
    "4-1": "`String`This field must contain the 3DS server transaction ID.",
    "4-2": "eea30d14-71cf-41af-b961-f95b7d67dc93",
    "5-0": "threeDSTransStatus  \n`mandatory`",
    "5-1": "`String`This field must contain the 3DS transaction status. It can be any of the following: Y, N, U or R.",
    "5-2": "Y",
    "6-0": "threeDSTransStatusReason  \n`mandatory`",
    "6-1": "This field must contain the 3DS transaction reason. It can be an integer in the range 0-99.",
    "6-2": "01",
    "7-0": "acquirer_bin  \n`mandatory`",
    "7-1": "`String` This field must contain the Bank Identification Number (BIN) that is used to clear and settle the transaction within Visa and the country in which it is licensed for use.",
    "7-2": "401200",
    "8-0": "additionalInfo  \n`mandatory`",
    "8-1": "`Object` This contains the following fields to include the additional authentication information:  \n  \n- authudf1\n- authudf2",
    "8-2": "1_1665637507_954_104  \n\\_l73c004m_IAMRB"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


#### threeDS2RequestData object field description

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "threeDSVersion  \n`mandatory`",
    "0-1": "`String`The message protocol version is to be specified in this field.",
    "0-2": "2.2.0",
    "1-0": "deviceChannel  \n`mandatory`",
    "1-1": "`String`The channel of transaction is to be specified in this field.",
    "1-2": "APP"
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


> ❗️ Error Handling
> 
> If any error message is displayed with an error code, refer to the [Error Codes](https://docs.payu.in/v1/reference/error-codes) section to understand the reason for these error codes.

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
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": 5497774415170603,
            "validThrough": "05/2025",
            "cvv": 123,
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
            "ownerName": "Ashish",
            "issuer": "ICICI",
            "bin": "500446",
            "last4Digits": "0000",
            "cardHash": null,
            "cardTokenType": "NETWORK",
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA="
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
        "txnS2sFlow": "3",
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
}'
```

## Response parameters

| Field                 | Description                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| redirectUrl           | URL to which the user is redirected after the payment process is completed.                       |
| authAction            | URL for authentication actions like OTP submission during the payment process.                    |
| paymentId             | Unique identifier for the payment transaction.                                                    |
| redirectTemplate      | Encoded HTML template used for auto-redirecting or displaying information post-payment.           |
| card.binData          | Contains information about the card used in the transaction.                                      |
| card.pureS2SSupported | Boolean indicating if the card supports pure server-to-server transactions.                       |
| card.issuingBank      | Name of the bank that issued the card.                                                            |
| card.category         | Category of the card, e.g., credit card, debit card.                                              |
| card.cardType         | Type of the card, for example, MAST for Mastercard.                                               |
| card.isDomestic       | Boolean indicating if the card is a domestic card (issued within the country of the transaction). |

## Sample response

```
{
  "result": {
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
    "authAction": "https://api.payu.in/payments/21667772394/otps",
    "paymentId": "21667772394",
    "redirectTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vbmV0YmFua2luZy5oZGZjYmFuay5jb20vbmV0YmFua2luZy9tZXJjaGFudD9DbGllbnRDb2RlPTE1NDkxMyZNZXJjaGFudENvZGU9UEFZVUZBQ0VCT09LJlR4bkN1cnJlbmN5PUlOUiZUeG5BbW91bnQ9MjUwMDAuMDAmVHhuU2NBbW91bnQ9MCZNZXJjaGFudFJlZk5vPWs0cWh3NGVsYXY2MmxwNjJjbSZTdWNjZXNzU3RhdGljRmxhZz1OJkZhaWx1cmVTdGF0aWNGbGFnPU4mRGF0ZT0yNi8xMS8yMDI0IDAwOjAwOjAwJlJlZjE9JlJlZjI9NDAzYmIzODkxY2Y5NGEzNmI0ZGQxOTlkOWNjZWVjNmUmUmVmMz0mUmVmND0mUmVmNT0mRHluYW1pY1VybD1odHRwczovL3NlY3VyZS5wYXl1LmluL2I0NDdmZmViZDg4NDNjZTEzYzlmODVhZjhlOTA0ZmQyL0NvbW1vblBnUmVzcG9uc2VIYW5kbGVyLnBocCZDaGVja1N1bT0zMTAxMzgyNDM2IiBtZXRob2Q9InBvc3QiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",
    "card": {
      "binData": {
        "pureS2SSupported": false,
        "issuingBank": "INDUSIND",
        "category": "debitcard",
        "cardType": "MAST",
        "isDomestic": true
      }
    }
  },
  "status": "PENDING"
}
```

> 📘 Reference:
> 
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).