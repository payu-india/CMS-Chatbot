---
title: Split by Percentage During Transaction - v2 Payment API
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
You can split during a transaction made using **\_payment** API by percentage, where you must ensure that the sum of percentage of all splits is equal to 100.

> 📘 Note:
>
> You must specify two decimal places for each split, but ensure the sum of percentage of all splits is equal to 100.

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
        `String` Reference ID for transaction tracking.
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
        `String` Currency of the transaction. By default, **INR** is posted.
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
        `Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentMethod-object-fields-description).
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
        splitRequest `mandatory for Split Settlement`
      </td>

      <td>
        `Object` Details about the split payment. For more information, refer to [splitRequest object fields description.](#splitrequest-object-fields-description)
      </td>

      <td>
         \{\
                          "type": "absolute",\
                          "splitInfo": \{\
                            "123412": \{\
                              "aggregatorSubTxnId": "12312941",\
                              "aggregatorSubAmt": "2000.55"\
                            },\
                            "2300019": \{\
                              "aggregatorSubTxnId": "12312941",\
                              "aggregatorSubAmt": "134.23"\
                            }\
                          }
      </td>
    </tr>
  </tbody>
</Table>

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
        `String` This field must contain the payment mode code. For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/docs/payment-mode-codes). For example, for credit card, this must contain **CreditCard**.
      </td>
    </tr>

    <tr>
      <td>
        bankCode\
         `mandatory`
      </td>

      <td>
        `String`This field must contain the bank code. For more information, refer to [Bank and Card Codes for Integration](https://docs.payu.in/v1/docs/bank-and-card-codes-for-integration) based on payment mode code in the **name** filed.
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
        `String`Details about the product being purchased.
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

### splitRequest object fields description

The following fields are included in the **splitRequest** parameter in a JSON format to specify the absolute split details. The fields in the JSON format are described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
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
        type
        **mandatory**
      </td>

      <td>
        `string` Specify the **percentage** type of split in this field. The absolute amount is specified in the **aggregatorSubAmt** field of the JSON for each child or aggregator.
      </td>

      <td>
        percentage
      </td>
    </tr>

    <tr>
      <td>
        splitInfo\
        **mandatory**
      </td>

      <td>
        `JSON` This parameter must include the list of aggregator sub transaction IDs and sub amounts as follows:  

        * **aggregatorSubTxnId**: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.
        * **aggregatorSubAmt**: The transaction amount or percentage split for the aggregator is posted in this parameter. This field is mandatory.
        * **aggregatorCharges** (optional): The transaction amount or percentage split for aggregator charges is posted in this parameter. This field is optional.  
          * \*Note\*\*: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.
      </td>

      <td>
        \{\
        "merchantKey1": \{\
        "aggregatorSubTxnId": "30nknyhkhib",\
        "aggregatorSubAmt": "8"\
        } 
      </td>
    </tr>
  </tbody>
</Table>

#### JSON request structure of splitInfo

The sample JSON structure for the **splitInfo** field:

> 📘 Notes:
>
> Before peruse the following sample code, remove the white spaces as some editors may introduce junk characters.

```plaintext
{
   "type":"precentage",
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

<br />

#### **TDR model**

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 41**45678912383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => Ax4j7J
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
    [field1] => 5582299554914671900181
    [field2] => 113476
    [field3] => 100.00
    [field4] => 41**45678912383977
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 5582299554914671900181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 512345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[{"merchantKey":"P41sCY","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba"},{"merchantKey":"P41sCK","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb"},{"merchantKey":"sd3fsmr","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b"}]}
)
```

#### **Convenience fee model**

The formatted response for the above sample request is similar to the following:

```plaintext
Array
(
    [mihpayid] => 41**45678912383977
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => Ax4j7J
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
    [field4] => 41**45678912383977
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => AxisCYBER
    [bank_ref_num] => 5582299554914671900181
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => Test User
    [cardnum] => 512345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
    [splitInfo] => {"splitStatus":"success","splitSegments":[
				{"merchantKey":"P41sCY","amount":50,"subvention_amount":0,"txnId":"9a70ea0155268101001ba, “discount":0,"additionalCharges":0,”transaction_fee":0”},
				{"merchantKey":"P41sCK","amount":30,"subvention_amount":0,"txnId":"9a70ea0155268101001bb, “discount”:0,"additionalCharges":0,"transaction_fee":0"}
				,{"merchantKey":"sd3fsmr","amount":20,"subvention_amount":0,"txnId":"9a70ea0155268101001b, “discount”:0,"additionalCharges":10,"transaction_fee":0"}
				]
   			}
)
```
