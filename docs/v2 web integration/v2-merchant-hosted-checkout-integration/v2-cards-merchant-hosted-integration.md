---
title: v2 Cards Integration
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
PayU supports the following debit cards and credit cards:

* American Express (AMEX)
* Visa
* Mastercard
* Diners
* Rupay

> 📘 Note:
>
> PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).

If you are storing or transmitting cardholder data, you must fill the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form. For more information on Save Cards API integration, refer to PayU Save Cards API Integration docs.

### Steps to Integrate

1. [Validate the card type](#step-1-validate-the-card-type)
2. [Initiate the payment to PayU](#step-2-initiate-the-payment-to-payu)
3. [Verify the payment](#step-4-verify-the-payment)

> 👍 Before you begin:
>
> PayU recommends you to integrate with Test environment initially. For more information, contact you PayU Key Account Manager (KAM) or PayU Support.

## Step 1: Validate the card type

When customers use debit cards or credit cards on your website, you can validate the card type with the first six digits. Use the **check\_isDomestic** API (known as BIN API) to validate the type of card. For more information, refer to  <a href="bin-apis" target="_blank"> BIN APIs</a>.

After the customer enters the card number, you can validate the first six digits with the **check\_isDomestic** API. For more information, refer to <a href="https://docs.payu.in/v1/reference/check_is_domestic_api" target="_blank">Check is Domestic API</a>.

## Step 2: Initiate the payment to PayU

Post the following parameters for the card payment to PayU using the Merchant Hosted integration.

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
        `String` Amount of the transaction.  

        * \*Note\*\*: This value will not be considered as the transaction. Only the details in the `order.paymentChargeSpecificationparameter.price`field will be considered.
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
        `String` Currency of the transaction. By default, `INR` is posted.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentSource
```

        optional
        ```
      </td>

      <td>
        `String`Contains the payment source.
      </td>

      <td>
        WEB
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
        `Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionaiInfo-object-fields-description)
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

      </td>
    </tr>

    <tr>
      <td>
        billingDetails\
        `mandatory`
      </td>

      <td>
        `Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<br />

### paymentMethod object fields description

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

        * creditcard for credit card
        * debitcard for debit card
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

#### paymentCard object fields description

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

### order object fields description

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

### callbackActions object fields description

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

`<ErrorHandling />`

#### paymentChargeSpecification object fields description

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

### billingDetails object field descriptions

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

## Sample request

```curl
curl --location 'https://pp78api.payu.in/v2/payments' \
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
        }
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

## Sample response

> 📘 Note:
>
> Reverse hashing of the response is not required with that of v2/payment API.

```
Array
(
    [referenceId] => b5f2d8785768087678fm9
    [paymentId] => 1999110000001769
    [message] => Please call verify api to get the transaction status
)
```

## Step 3: Verify the Payment

Verify the transaction details using the Verification APIs. For API reference, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api) under API Reference.

> 📘 Note:
>
> The transaction ID that you posted in Step 1 with PayU must be used here.