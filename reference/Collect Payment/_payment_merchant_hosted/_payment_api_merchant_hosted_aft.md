---
title: AFT
deprecated: false
hidden: true
metadata:
  robots: index
---
An Account Funding Transaction (AFT) is a secure, electronic, "pull" payment method that moves money from a cardholder’s account (credit/debit) to a non-merchant account, such as a digital wallet, prepaid card, or investment account. It is primarily used to "load" or "top-up" funds, rather than for purchasing goods or services. This section describes the request parameters, sample request/response for _payment API using AFT.

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Request Parameters

<br />

### additional_info JSON Parameters Description

#### Sample JSON

```json
{
  "senderInformation": {
    "firstName": "Sharp",
    "lastName": "Shooter"
  },
  "recipientInformation": {
    "firstName": "Table",
    "lastName": "Cable",
    "account": {
      "number": "619"
    },
    "address": {
      "city": "",
      "country": "",
      "postCodeZip": "",
      "stateProvinceCode": "",
      "street": "",
      "street2": ""
    },
    "KYCInfo": {
      "GovtIdType": "",
      "GovtIdNumber": "2222"
    }
  }
}
```

#### Fields Description

| Field                    | Description                                                                                                | Example |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- | ------- |
| **senderInformation**    |                                                                                                            |         |
| `firstName`              | The first name of the sender.                                                                              | Sharp   |
| `lastName`               | The last name of the sender.                                                                               | Shooter |
| **recipientInformation** |                                                                                                            |         |
| `firstName`              | The first name of the recipient.                                                                           | Table   |
| `lastName`               | The last name of the recipient.                                                                            | Cable   |
| **account**              |                                                                                                            |         |
| `number`                 | The account number associated with the recipient.                                                          | 619     |
| **address**              |                                                                                                            |         |
| `city`                   | The city where the recipient resides.                                                                      | (Empty) |
| `country`                | The country where the recipient resides.                                                                   | (Empty) |
| `postCodeZip`            | The postal code or ZIP code of the recipient's address.                                                    | (Empty) |
| `stateProvinceCode`      | The state or province code of the recipient's address.                                                     | (Empty) |
| `street`                 | The primary street address of the recipient.                                                               | (Empty) |
| `street2`                | The secondary street address or additional address information for the recipient.                          | (Empty) |
| **KYCInfo**              |                                                                                                            |         |
| `GovtIdType`             | The type of government-issued identification provided by the recipient (e.g., passport, driver's license). | (Empty) |
| `GovtIdNumber`           | The number of the government-issued identification provided by the recipient.                              | 2222    |

The table now includes **bold sub-headers** for each parameter group (`senderInformation`, `recipientInformation`, `account`, `address`, and `KYCInfo`) to clearly show the hierarchical structure from the JSON. 📊

## Sample Request

```curl
```

<br />

## Sample Response

There are no changes in the response, it will remain as it is like the existing plain card number.

```json
Array
(
    [mihpayid] => 403993715524069222
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JF***g
    [txnid] => EaE4ZO3vU4iPsp
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-08 19:37:19
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => ed99957adb08fea56c907b88e8d158a79c3562c67f96c298461509826f77a7ae9e88b2a176b3234c25f50bcd451271728719656f3bb59c13a52bebabc468615a
    [field1] => 0608273386032718000015
    [field2] => 986987
    [field3] => 10.00
    [field4] => 403993715524069222
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 0608273386032718000015
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
)
```

<br />
