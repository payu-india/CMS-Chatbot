---
title: Verify Payment API v2
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
To know the status of the payment, you need to integrate the** Verify Payment** API as below. You need post the **referenceId** sent by the **v2/payments** API in the **txnId** parameter.

HTTP Method: **POST**

**Environment**

|                        |                                       |
| :--------------------- | :------------------------------------ |
| Test Environment       | <https://test.payu.in/v1/transaction> |
| Production Environment | <https://info.payu.in/v1/transaction> |

## Request parameters

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

## Body parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "txnId  \n**mandatory**",
    "0-1": "You need post the **referenceId** sent by the **v2/payments** API. For more information, refer to any of the following:  \n  \n- [Collect Payment API for PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)\n- [Collect Payment API for Merchant Hosted Checkout](ref:_payment_merchant_hosted)",
    "0-2": "54dzPX68BZzE46Q2VYWw"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```
curl --location 'https://test.payu.in/v1/transaction' \
--header 'Content-Type: application/json' \
--header 'date: Thu, 27 Mar 2025 06:35:21 GMT' \
--header 'authorization: hmac username="PRiQvJ", algorithm="sha512", headers="date", signature="42a54cc7450fe1e7a3cf35ebfaed1b828e37062964266fd33186c7b2526e85e3ea2d46946a728ca50e46423ea9a6b2edb8c1315b58fa69297e1e91d3d34804a1"' \
--header 'Info-Command: verify_payment' \
--data '{
    "txnId":["512345678901234"]
}'
```

## Response parameters

The fields in the result parameter JSON are described in the following table:

| Field               | Description                                                                                                                          | Example                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| mihpayId            | Transaction ID is a unique number assigned by PayU for each transaction. Keep note of it for future reference for inquiry or refund. | 21612493009                  |
| bankReferenceNumber | For each successful transaction – this parameter would contain the bank reference number generated by the bank.                      | 2411194544                   |
| amount              | This parameter would contain the actual amount involved in the transaction.                                                          | 0.00                         |
| mode                | This parameter describes the payment mode by which the transaction was completed (e.g., CC for Credit Card).                         | CC                           |
| requestId           | A unique identifier for the request.                                                                                                 |                              |
| originalAmount      | The original transaction amount before applying charges or discounts.                                                                | 100.00                       |
| additionalCharges   | Additional charges, if any, applied to the transaction amount.                                                                       | 0.00                         |
| discount            | Any discount amount applied to the transaction.                                                                                      | 0.00                         |
| netDebitAmount      | Total amount debited from the payer's account after additional charges and discounts.                                                | 100.00                       |
| productInfo         | A brief description of the product or service for which the payment was being made.                                                  | cred_product                 |
| firstName           | The payer’s first name involved in the transaction.                                                                                  | CRED                         |
| bankcode            | The code of the bank used for the transaction.                                                                                       | AMEX                         |
| nameOnCard          | Cardholder's name (null if the value is not captured).                                                                               | (null)                       |
| cardNo              | Masked card number for enhanced security.                                                                                            | XXXXXXXXXXXX2001             |
| cardType            | The type of card used, such as AMEX for American Express.                                                                            | AMEX                         |
| udf1 to udf5        | User-defined fields for additional optional data during the transaction process.                                                     | (null)                       |
| field2              | Context-specific information from the bank, such as codes or values relevant to verification.                                        | 140455                       |
| field9              | Describes the status of the transaction.                                                                                             | Transaction is Successful    |
| errorCode           | This parameter provides error code information.                                                                                      | E000                         |
| errorMessage        | Provides a human-readable error message for failed transactions.                                                                     | No Error                     |
| addedOn             | Timestamp when the transaction was initiated.                                                                                        | 2024-11-19 21:17:55          |
| settledAt           | Timestamp when funds were settled.                                                                                                   | 0000-00-00 00:00:00          |
| paymentSource       | The source of payment handling.                                                                                                      | payuS2S                      |
| pgType              | Indicates the type of payment gateway used.                                                                                          | CC-PG                        |
| status              | Displays the overall status of the transaction.                                                                                      | success                      |
| unmappedStatus      | Internal transaction status in PayU’s system, mapped separately.                                                                     | captured                     |
| merchantUTR         | Merchant's Unique Transaction Reference.                                                                                             | (null)                       |
| message             | General status message for the transaction.                                                                                          | Found TxnId                  |
| txnId               | The transaction ID provided by the merchant for tracking purposes.                                                                   | 54dzPX68BZzE46Q2VYWw         |
| rupayAuthRefNo      | Reference ID specific to RuPay Cards.                                                                                                | AAACAVJIggICQyRYdUiCEAAAAAA= |
| authRefNo           | A bank-specific authorization reference number.                                                                                      | AAACAVJIggICQyRYdUiCEAAAAAA= |
| originalCurrency    | The currency used for the transaction.                                                                                               | INR                          |
| threeDSVersion      | Version of the 3D Secure protocol used for securing the transaction.                                                                 | 2.2.0                        |

## Sample response

### Success scenario

Formatted JSON Response:

If successfully fetched:

```plaintext
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "mihpayId": 21612493009,
            "bankReferenceNumber": "2411194544",
            "amount": 0.00,
            "mode": "CC",
            "requestId": "",
            "originalAmount": 100.00,
            "additionalCharges": 0.00,
            "discount": 0.00,
            "netDebitAmount": 100.00,
            "productInfo": "cred_product",
            "firstName": "CRED",
            "bankcode": "AMEX",
            "nameOnCard": null,
            "cardNo": "XXXXXXXXXXXX2001",
            "cardType": "AMEX",
            "udf1": null,
            "udf2": null,
            "udf3": null,
            "udf4": null,
            "udf5": null,
            "field2": "140455",
            "field9": "Transaction is Successful",
            "errorCode": "E000",
            "errorMessage": "No Error",
            "addedOn": "2024-11-19 21:17:55",
            "settledAt": "0000-00-00 00:00:00",
            "paymentSource": "payuS2S",
            "pgType": "CC-PG",
            "status": "success",
            "unmappedStatus": "captured",
            "merchantUTR": null,
            "mcpLookupId": null,
            "mcpAmount": null,
            "mcpCurrency": null,
            "mcpExchangeRate": null,
            "rupayAuthRefNo": "AAACAVJIggICQyRYdUiCEAAAAAA=",
            "authRefNo": "AAACAVJIggICQyRYdUiCEAAAAAA=",
            "originalCurrency": "INR",
            "threeDSVersion": "2.2.0",
            "merNetAmount": null,
            "offerAvailed": null,
            "message": "Found TxnId",
            "txnId": "54dzPX68BZzE46Q2VYWw"
        }
    ]
}
```

#### Failure scenarios

- If **var3** (input bank name) does not match with the bank name in the PayU Database, the bin given in the input is of a different bank name:

```plaintext
Array (
[status] => 0
[msg] => Invalid Bin )
```