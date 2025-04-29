---
title: v2 S2S Direct Authentication Integration
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
This is server-to-server integration over the Redirect experience for cards involves the following steps:

### Steps to Integrate

1. [Post the transaction to PayU](#step-1-post-the-transaction-to-payu)
2. [Check Response from PayU](#step-2-check-response-from-payu)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Post the transaction to PayU

Initiate an authorization request with the payment details provided post a successful authentication via the MPI/3DSS.  For the request parameters, refer to  <a href="https://docs.payu.in/v2/reference/_payment_s2s_direct_authorization_flow" target="_blank">Cards Direct Authorization Flow</a>.

### Request header

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

<br />

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

### Body

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountId
         `mandatory`
      </td>

      <td>
        `String` The merchant key provided by PayU during onboarding.
      </td>

      <td>
        MERCHANT123
      </td>
    </tr>

    <tr>
      <td>
        referenceId\
         `mandatory`
      </td>

      <td>
        `String` Reference ID for transaction tracking and this must be unique for every transaction.
      </td>

      <td>
        REF123456
      </td>
    </tr>

    <tr>
      <td>
        amount\
         `optional`
      </td>

      <td>
        `Long` Amount of the transaction.
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        currency\
         `mandatory`
      </td>

      <td>
        `String` Currency of the transaction (e.g., INR). By default, `INR` is posted.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentMethod\
         `mandatory`
      </td>

      <td>
        `Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentmethod-object-fields-description).
      </td>

      <td>
         \{\
                "name": "NetBanking",	\
                "bankCode": "TESTNB"\
            }
      </td>
    </tr>

    <tr>
      <td>
        order\
         `mandatory`
      </td>

      <td>
        `Object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        additionalInfo\
         `mandatory`
      </td>

      <td>
        `Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        callBackActions\
         `mandatory`
      </td>

      <td>
        `Object` Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to [callbackActions object fields description](#callbackactions-object-fields-description)
      </td>

      <td>
         \{
      </td>
    </tr>

    <tr>
      <td>
        billingDetails `mandatory`
      </td>

      <td>
        `Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        deviceInfo\
        `mandatory for S2S`
      </td>

      <td>
        `Object`Device info of the customer.  For more information, refer to[ deviceInfo object field descriptions](#deviceinfo-object-field-descriptions)  .
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        authorization\
        `mandatory for S2S Direct Auth`
      </td>

      <td>
        `Object`3DS authorization information.  For more information, refer to refer to[ deviceInfo object field descriptions](#authorization-object-field-descriptions)   .
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        threeDS2RequestData\
        `mandatory for S2S`
      </td>

      <td>
        `Object` 3DS authorization information.  For more information, refer to refer to [threeDS2RequestData object field description](threeds2requestdata-object-field-description)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

#### paymentMethod object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
         `mandatory`
      </td>

      <td>
        `String` This field must contain the payment mode code. For cards, this must contain any of the following:  

        * **creditcard** for credit card
        * **debitcard** for debit card
      </td>
    </tr>

    <tr>
      <td>
        bankCode\
         `mandatory`
      </td>

      <td>
        `String`This field must contain the bank code. For more information, refer to [Card Type Codes and Supported Banks for Cards](https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards)
      </td>
    </tr>

    <tr>
      <td>
        paymentCard `mandatory for cards`
      </td>

      <td>
        `Object`This object will contain the physical card or saved card token details. For more information, refer to[ paymentCard object fields description](#paymentcard-object-fields-description).
      </td>
    </tr>
  </tbody>
</Table>

##### paymentCard object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        cardNumber
         `mandatory for physical card`
      </td>

      <td>
        `String`This field must contain the card number. For validating the card number, refer to [Card Number Formats](https://docs.payu.in/v1/docs/card-number-formats).
      </td>
    </tr>

    <tr>
      <td>
        validThrough\
         `mandatory for physical card`
      </td>

      <td>
        `String`This field must contain the card expiry in MM/YYYY format.
      </td>
    </tr>

    <tr>
      <td>
        ownerName\
         `mandatory for physical card`
      </td>

      <td>
        `String`This field must contain the name of the card holder as printed on card.
      </td>
    </tr>

    <tr>
      <td>
        cvv\
         `mandatory for physical card`
      </td>

      <td>
        `String`This field must contain the CVV printed on the back of the card.  
      </td>
    </tr>

    <tr>
      <td>
        tavv\
         `mandatory for saved card`
      </td>

      <td>
        `String`This field must contain the cryptogram of card.
      </td>
    </tr>

    <tr>
      <td>
        last4Digits\
         `mandatory for saved card`
      </td>

      <td>
        `String`This field must contain the last four digits of card.
      </td>
    </tr>

    <tr>
      <td>
        cardTokenType\
         `mandatory for saved card`
      </td>

      <td>
        `String`This field must contain the any of the following based on the:  

        * PAYU
        * NETWORK
        * ISSUER"
      </td>
    </tr>

    <tr>
      <td>
        cardToken\
         `mandatory for saved card`
      </td>

      <td>
        `String`This field must contain the card token of stored card.
      </td>
    </tr>
  </tbody>
</Table>

#### additionalInfo object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        txnS2sFlow
         `mandatory for S2S`
      </td>

      <td>
        `String` Indicates the transaction S2S flow type and must be set to **4** for Classic Integration.
      </td>
    </tr>

    <tr>
      <td>
        authenticationFlow\
         `mandatory for S2S`
      </td>

      <td>
        `String` Indicates the authentication flow type and must be set to **REDIRECT** for Classic Integration.
      </td>
    </tr>

    <tr>
      <td>
        decodedS2sResponse\
         `mandatory for S2S`
      </td>

      <td>
        `String` Indicates whether you want to use acsTemplate format and want to post data by the merchant (on your own).  Post it as **1** only if you do not want to use acsTemplate format and want to post data on your own.
      </td>
    </tr>
  </tbody>
</Table>

#### order object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        productInfo
         `mandatory`
      </td>

      <td>
        `String`Details about the product being purchased. For more information, refer to[ userDefinedFields object fields description](#userdefinedfields-object-fields-description).
      </td>
    </tr>

    <tr>
      <td>
        userDefinedFields\
         `optional`
      </td>

      <td>
        `Object`Custom fields defined by the user for additional information.
      </td>
    </tr>

    <tr>
      <td>
        paymentChargeSpecification\
         `mandatory`
      </td>

      <td>
        `Object` Payment details including amount, additional charges and PayU offers to be applied. For more information, refer to [paymentChargeSpecification object fields description](#paymentchargespecification-object-fields-description).
      </td>
    </tr>
  </tbody>
</Table>

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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        price
        `mandatory`
      </td>

      <td>
        This field must contain the price or transaction amount to be posted.
      </td>

      <td>
        10.00
      </td>
    </tr>
  </tbody>
</Table>

#### callbackActions object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        successAction
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to upon successful payment.
      </td>
    </tr>

    <tr>
      <td>
        failureAction\
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to if the payment is failed.
      </td>
    </tr>

    <tr>
      <td>
        cancelAction\
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to if the transaction is cancelled.
      </td>
    </tr>

    <tr>
      <td>
        codAction\
         `optional`
      </td>

      <td>
        `String`URL to handle Cash on Delivery actions.
      </td>
    </tr>

    <tr>
      <td>
        termAction\
         `optional`
      </td>

      <td>
        `String`URL for completing terms and conditions actions.
      </td>
    </tr>

    <tr>
      <td>
        returnAction\
         `optional`
      </td>

      <td>
        `String`URL to return to after successful payment action is completed.
      </td>
    </tr>
  </tbody>
</Table>

#### billingDetails object field descriptions

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        firstName
        `mandatory`
      </td>

      <td>
        First name of the billing contact
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        lastName\
        `optional`
      </td>

      <td>
        Last name of the billing contact
      </td>

      <td>
        Kumar
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `mandatory`
      </td>

      <td>
        Phone number of the billing contact
      </td>

      <td>
        9123456789
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        Email address of the billing contact
      </td>

      <td>
        [ashish@abc.com](mailto:ashish@abc.com)
      </td>
    </tr>

    <tr>
      <td>
        city\
        `optional`
      </td>

      <td>
        City of the billing address
      </td>

      <td>
        Bengaluru
      </td>
    </tr>

    <tr>
      <td>
        state\
        `optional`
      </td>

      <td>
        State of the billing address
      </td>

      <td>
        Karnatka
      </td>
    </tr>

    <tr>
      <td>
        country\
        `optional`
      </td>

      <td>
        Country of the billing address
      </td>

      <td>
        Indiia
      </td>
    </tr>

    <tr>
      <td>
        zipCode\
        `optional`
      </td>

      <td>
        Postal/Zip code of the billing address
      </td>

      <td>
        560071
      </td>
    </tr>
  </tbody>
</Table>

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

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        eci
        `mandatory`
      </td>

      <td>
        `String`The electronic commerce indicator is used in payer authentication to indicate the level of security used when the cardholder provided payment information to the merchant. Its value corresponds to the authentication result and the characteristics of the merchant checkout process.
      </td>

      <td>
        05
      </td>
    </tr>

    <tr>
      <td>
        cavv\
        `mandatory`
      </td>

      <td>
        `String`The Cardholder Authentication Verification Value (CAVV) is specified here.
      </td>

      <td>
        AAABAWFlmQAAAABjRWWZEEFgFz
      </td>
    </tr>

    <tr>
      <td>
        flowType\
        `mandatory`
      </td>

      <td>
        `String`This field must contain any of the following flow types:  

        * Frictionless
        * Challenge.
      </td>

      <td>
        Frictionless
      </td>
    </tr>

    <tr>
      <td>
        threeDSTransID\
        `mandatory`
      </td>

      <td>
        `String`This field must contain the 3DS transaction ID.
      </td>

      <td>
        67b4c71f-19bf-4d97-bd09-4e3687dc9e42
      </td>
    </tr>

    <tr>
      <td>
        threeDSServerTransID\
        `mandatory`
      </td>

      <td>
        `String`This field must contain the 3DS server transaction ID.
      </td>

      <td>
        eea30d14-71cf-41af-b961-f95b7d67dc93
      </td>
    </tr>

    <tr>
      <td>
        threeDSTransStatus\
        `mandatory`
      </td>

      <td>
        `String`This field must contain the 3DS transaction status. It can be any of the following: Y, N, U or R.
      </td>

      <td>
        Y
      </td>
    </tr>

    <tr>
      <td>
        threeDSTransStatusReason\
        `mandatory`
      </td>

      <td>
        This field must contain the 3DS transaction reason. It can be an integer in the range 0-99.
      </td>

      <td>
        01
      </td>
    </tr>

    <tr>
      <td>
        acquirer\_bin\
        `mandatory`
      </td>

      <td>
        `String` This field must contain the Bank Identification Number (BIN) that is used to clear and settle the transaction within Visa and the country in which it is licensed for use.
      </td>

      <td>
        401200
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo\
        `mandatory`
      </td>

      <td>
        `Object` This contains the following fields to include the additional authentication information:  

        * authudf1
        * authudf2
      </td>

      <td>
        1\_1665637507\_954\_104  

        * l73c004m\_IAMRB
      </td>
    </tr>
  </tbody>
</Table>

#### threeDS2RequestData object field description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        threeDSVersion
        `mandatory`
      </td>

      <td>
        `String`The message protocol version is to be specified in this field.
      </td>

      <td>
        2.2.0
      </td>
    </tr>

    <tr>
      <td>
        deviceChannel\
        `mandatory`
      </td>

      <td>
        `String`The channel of transaction is to be specified in this field.
      </td>

      <td>
        APP
      </td>
    </tr>
  </tbody>
</Table>

<ErrorHandling />

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

### Sample response

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

## Step 2: Verify the payment

> 📘 Note:
>
> This API is backward compatible and you can continue to the existing integration parameters to process the 3DS 1.0.2 transactions.

### Sample response

The sample response after the customer makes payment will be similar to v2 merchant hosted checkout payments. 

> 📘 Note:
>
> Reverse hashing of the response is not required with that of v2/payment API.

```plaintext
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Tip
>
> The transaction ID that you posted in Step 1 with PayU must be used here.
