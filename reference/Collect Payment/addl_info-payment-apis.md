---
title: Additional Info for Payment APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request parameters for \_payment API

### Common request parameters

| Parameter | Description | Example |
| --- | --- | --- |
| key `mandatory` | `varchar` Unique Merchant Key provided by PayU for your merchant account. | Your Test Key |
| txnid `mandatory` | `varchar` Transaction ID (or Order ID) generated at the merchant end. Must be unique for every new transaction. `Character limit`: 25.<br /><br />**Note:** Ensure the transaction ID has not been successful earlier. Reusing a successful transaction ID returns a duplicate Order ID error. | fd3e847h2 |
| amount `mandatory` | `float` Payment amount for the transaction.<br /><br />**Note:** Type-cast the amount to float type. Depending on the merchant use case, this value will vary.<br /><br />- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards and UPI) in penny transaction use cases.<br />- In first instalment use cases, this amount can equal the initiate setup amount. This is supported only for selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI. | 1000 |
| productinfo `mandatory` | `varchar` Brief product description. `Character limit`: 100 | Time Magazine Subscription |
| firstname `mandatory` | `varchar` First name of the customer. `Character limit`: 60 | Ashish |
| email `mandatory` | `varchar` Email of the customer. Required for fraud detection, chargebacks, and MIS reporting for SI transactions. `Character limit`: 50 | Ashish@test.com |
| phone `mandatory` | `varchar` Phone number of the customer. Required for fraud detection, chargebacks, and MIS reporting for SI transactions. `Character limit`: 50 | 9843176540 |
| surl `mandatory` | Success URL. PayU redirects the final response here when the transaction is successful. |  |
| furl `mandatory` | Failure URL. PayU redirects the final response here when the transaction fails. |  |
| api\_version `mandatory` | API version. Must be passed as **7**. | 7 |
| hash `mandatory` | SHA-512 hash to ensure request data is not tampered while redirecting the customer to PayU. For registration transactions: `HASH = SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|si_details\|SALT)`<br /><br />**Note:** For `_payment` API version 19, use: `key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|user_token\|offer_key\|offer_auto_apply\|cart_details\|extra_charges\|phone` |  |

### Seamless integration parameters

| Parameter | Description | Example |
| --- | --- | --- |
| pg `mandatory for seamless flow` | `String` Payment method. Defaults to **CC** if not specified.<br /><br />- Net Banking: **NB**<br />- Card: **DC** (Debit Card), **CC** (Credit Card)<br />- UPI: **UPI**<br />- Wallets: **CASH**<br />- EMI: **EMI**<br />- BNPL: **BNPL**<br />- EFTNET (NEFT/RTGS): **NEFTRTGS**<br />- QR: **QR** |  |
| bankcode `mandatory for seamless flow` | Unique bank code for the payment option. Refer based on **pg**:<br /><br />- Net Banking: [Net Banking Codes](doc:net-banking-codes)<br />- Cards: [Card Number Formats](doc:card-number-formats) and [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)<br />- UPI: [UPI Handles](doc:upi-handles)<br />- Wallets: [Wallet Codes](doc:wallet-codes)<br />- EMI: [EMI Codes](doc:emi-codes)<br />- BNPL: [BNPL Codes](doc:bnpl-codes) |  |
| udf1 `optional for seamless flow` | User-defined field for transaction-specific information. `Character limit`: 255 |  |
| udf2 `optional for seamless flow` | User-defined field for transaction-specific information. `Character limit`: 255 |  |
| udf3 `optional for seamless flow` | User-defined field for transaction-specific information. `Character limit`: 255 |  |
| udf4 `optional for seamless flow` | User-defined field for transaction-specific information. `Character limit`: 255 |  |
| udf5 `optional for seamless flow` | User-defined field for transaction-specific information. `Character limit`: 255 |  |
| ccnum `mandatory for cards in seamless flow` | `String` 13–19 digit card number (15 digits for AMEX, 13–19 for Maestro). Validate with LUHN algorithm. Refer to [Card Number Formats](doc:card-number-formats). |  |
| ccvv `mandatory for cards in seamless flow` | `String` CVV number of the card – as entered by the customer for the transaction. |  |
| ccexpmon `mandatory for cards in seamless flow` | `String` Card expiry month in MM format (01–12). |  |
| ccexpyr `mandatory for cards in seamless flow` | `String` Card expiry year in four digits. |  |
| threeDS2RequestData `mandatory for cards in seamless flow` | `String` 3DS2 request data for card authentication. For more information, refer to [Request Parameter for 3DS Secure 2.0 Transaction](doc:collect-payments-with-cards-seamless#request-parameter-for-3ds-secure-20-transaction). |  |

### Server-to-Server integration parameters

| Parameter | Description | Example |
| --- | --- | --- |
| s2s\_client\_ip `mandatory for S2S` | `String` Source IP of the customer.<br /><br />**Note:** Required for fraud detection and chargeback handling. |  |
| s2s\_device\_info `mandatory for S2S` | `String` Customer device user agent.<br /><br />**Note:** Required for fraud detection and chargeback handling. |  |
| txn\_s2s\_flow `mandatory for S2S` | `String` S2S flow type:<br /><br />- **4** for S2S<br />- **3** for Direct Authorization |  |
| authentication\_flow `mandatory for S2S` | Must be **REDIRECT** for classic S2S integration. | REDIRECT |

### Webhook parameters

| Parameter | Description | Example |
| --- | --- | --- |
| partner\_webhook\_success | Webhook URL for successful transaction responses. Multiple URLs can be comma-separated. Use HTTPS URLs only. Pass non-URL-encoded URLs. | https://test.payu.in/admin/test_response |
| partner\_webhook\_failure | Webhook URL for failed transaction responses. Multiple URLs can be comma-separated. Use HTTPS URLs only. Pass non-URL-encoded URLs. | https://test.payu.in/admin/test_response |


### Additional parameters for Guest Checkout

| **Parameter**                | **Description**                                                                                                                           | **Example** |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| alt\_id `mandatory`          | `String` This parameter must contain Alt ID for the guest checkout.                                                                       |             |
| ccexpmon `mandatory`         | `String` This parameter must contain the Alt ID expiry month. For VISA cards, Plain card's expiry month need to be posted this parameter. | 10          |
| ccexpyr `mandatory`          | `String` This parameter must contain the Alt ID expiry year. For VISA cards, Plain card's expiry year need to be posted this parameter.   | 2021        |
| additional\_info `mandatory` | `JSON`The fields which are included in this JSON are described in the next table.                                                         |             |

The description of the fields in the additional\_info JSON.

| Field            | Description                                                                                                                                                                   |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
| tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
| TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

### Additional parameters for Saved Card

#### Using Network tokens

| Parameter | Description | Example |
| --- | --- | --- |
| ccnum `optional` | `varchar` 13 to 19-digit card number for credit or debit cards. | 512***6789012346 |
| ccname `optional` | `varchar` Customer name on card. | Ashish |
| ccvv `optional` | `varchar` CVV number of the card. | 123 |
| ccexpmon `mandatory` | `integer` Expiry month on card validity. | 10 |
| ccexpyr `mandatory` | `integer` Expiry year on card validity. | 2022 |
| store_card_token `mandatory` | `varchar` Network token generated at your end. | 1234 4567 2456 3566 |
| storecard_token_type `mandatory` | `integer` Store card token type. For network tokens, use **1**. | 1 |
| additional_info `mandatory` | JSON with `last4Digits`, `tavv`, `trid`, and `tokenRefNo`. | See sample JSON below. |

```json
{"last4Digits": "1234", "tavv": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}
```

#### Using Issuer tokens

| Parameter | Description | Example |
| --- | --- | --- |
| ccvv `optional` | `varchar` CVV number of the card. | 123 |
| ccexpmon `mandatory` | `integer` Network token expiry month. | 10 |
| ccexpyr `mandatory` | `integer` Network token expiry year. | 2024 |
| store_card_token `mandatory` | `varchar` Token generated by PayU for the card. | 1234 4567 2456 3566 |
| storecard_token_type `mandatory` | `integer` Store card token type. For issuer tokens, use **0**. | 0 |
| additional_info `mandatory` | JSON with `trMerchantId`, `tokenReferenceId`, `tokenBank`, and `last4Digits`. | See sample JSON below. |

```json
{"trMerchantId":"INBANPAYUWIBPAY011","tokenReferenceId":"02ac786d-0081-4b1a-a2a6-b0755a83964c","tokenBank":"HDFC","last4Digits":"8179"}
```

<br />

#### Using card tokenized with PayU

| Parameter | Description | Example |
| --- | --- | --- |
| ccvv `optional` | `varchar` CVV number of the card. | 123 |
| storecard_token_type `mandatory` | `integer` Store card token type. For PayU tokenization, use **0**. | 0 |
| user_credentials `mandatory` | `varchar` User credentials. | a:b |
| store_card_token `mandatory` | `varchar` Token generated by PayU for the card. | 1234 4567 2456 3566 |

<br />

## Using card on a decoupled Flow with Network token or other partner tokenization

| Parameter | Description | Example |
| --- | --- | --- |
| ccvv `optional` | `varchar` CVV number of the card as entered by the customer. | 123 |
| storecard\_token\_type `mandatory` | `integer` Store card token type (tokenization partner). For network or partner tokenization, use **1**. | 1 |
| store\_card\_token `mandatory` | `varchar` Token generated for the card. | 1234 4567 2456 3566 |
| additional\_info `mandatory` | JSON with `last4Digits`, `tavv`, `trid`, and `tokenRefNo`. | See sample JSON below. |

```json
{"last4Digits": "1234", "tavv": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}
```

#### Using Card on a decoupled flow with PayU tokenization

| Parameter | Description | Example |
| --- | --- | --- |
| ccvv `optional` | `varchar` CVV number of the card as entered by the customer. | 123 |
| storecard\_token\_type `mandatory` | `integer` Store card token type (tokenization partner). For PayU tokenization, use **0**. | 0 |
| store\_card\_token `mandatory` | `varchar` Token generated by PayU for the card. | 1234 4567 2456 3566 |
| additional\_info `mandatory` | JSON with `last4Digits`, `tavv`, `trid`, and `tokenRefNo`. | See sample JSON below. |

```json
{"last4Digits": "1234", "tavv": "ABCDEFGH", "trid": "1234567890", "tokenRefNo": "abcde123456"}
```

## Character Limit for Request Parameters

| Parameter   | Production Environment | Test Environment |
| --- | --- | --- |
| productinfo | 100                    | 100              |
| firstname   | 60                     | 20               |
| email       | 50                     | 50               |
| lastname    | 20                     | 20               |
| address1    | 100                    | 100              |
| address2    | 100                    | 100              |
| city        | 50                     | 50               |
| state       | 50                     | 50               |
| country     | 50                     | 50               |
| zipcode     | 20                     | 20               |
| surl        | 50                     | 50               |
| furl        | 50                     | 50               |
| curl        | 50                     | 50               |
| udf1 - udf5 | 255                    | 255              |

## Response parameters

## General response parameters for all Web Checkout integrations

| Variable | Description |
| --- | --- |
| mihpayid | Transaction ID assigned by PayU for each transaction. Keep this for inquiry or refund. |
| mode | Payment category for the completed or attempted transaction. For values, refer to [Payment Mode Codes](doc:payment-mode-codes). |
| status | Transaction outcome: `success`, `failed`, or `pending`. Treat `failure` and `pending` as failed unless verified otherwise. |
| key | Merchant PayU account key. Same as the key used in the transaction request. |
| txnid | Transaction ID posted by the merchant in the request. |
| amount | Original amount sent in the transaction request. |
| productinfo | Product information echoed from the transaction request. |
| firstname | First name echoed from the transaction request. |
| lastname | Last name echoed from the transaction request. |
| email | Email echoed from the transaction request. |
| phone | Phone echoed from the transaction request. |
| udf | User-defined fields echoed from the request (`udf1` to `udf5`). |
| hash | PayU-calculated hash. Verify before marking the transaction success or failure. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted). |
| error | Failure reason for failed transactions.<br /><br />**Note:** Failure reasons vary by bank error codes. |
| error\_message | Error message text. For the list of error messages, refer to [Error Codes](ref:error-codes). |
| bankcode | Payment option code used in the transaction (for example, VISA, MAST). |
| PG\_TYPE | Payment gateway used (for example, `CC-PG` for credit card). |
| bank\_ref\_num | Bank reference number for successful transactions. |
| unmappedstatus | Internal PayU transaction status. Possible values include `dropped`, `bounced`, `captured`, `auth`, `failed`, `usercancelled`, or `pending`. For more information, refer to [Payment State Explanations](ref:payment-state-explanations). |

## Response for initial Server-to-Server request

| **Parameter**     | **Description**                                                                                                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| result            | This parameter contains a JSON Object that includes **post\_uri** and **post\_data** fields.                                                                                                                                                                                 |
| result.post\_uri  | This field contains the redirect URL.                                                                                                                                                                                                                                        |
| result.post\_data | post\_data is a base64 encoded string. The merchant needs to decode post\_data, which is an HTML format with auto submit, which then needs to be shown on the customer’s browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |
| status            | This field contains the status for the transaction.                                                                                                                                                                                                                          |
| error             | For the failed transactions, this parameter provides the reason for failure.                                                                                                                                                                                               |
| message           | This field contains any additional message about the transaction.                                                                                                                                                                                                            |

<Callout icon="📘" theme="info">
  ### Note:

  The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.
</Callout>

#### metaData JSON Fields Description

| **Field**      | **Description**                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message        | This field contains any additional message about the transaction.                                                                                       |
| referenceId    | This field contains the reference ID of the transaction.                                                                                                |
| statusCode     | This field contains the status code for the transaction.                                                                                                |
| txnId          | This field contains the transaction ID of the transaction that was posted in the request.                                                               |
| unmappedStatus | This field contains the unmapped status of the transaction. For more information, refer to [Payment State Explanations](ref:payment-state-explanations) |

#### result JSON Fields Description

| Field | Description |
| --- | --- |
| mihpayid | Unique PayU transaction reference. Use for inquiry, refund, and future actions. |
| mode | Payment category for the completed or attempted transaction. For values, refer to [Payment Mode Codes](doc:payment-mode-codes). |
| status | Transaction status: `success`, `failure`, or `pending`. If `status` is `failure` or `pending`, treat as failed unless verified otherwise. |
| key | Merchant key for the PayU account. Same as the key used in the request. |
| txnid | Transaction ID posted by the merchant in the request. |
| amount | Original amount sent in the transaction request. |
| productinfo | Product information echoed from the request. |
| firstname | First name echoed from the request. |
| lastname | Last name echoed from the request. |
| email | Email echoed from the request. |
| phone | Phone echoed from the request. |
| udf | User-defined fields echoed from the request (`udf1` to `udf5`). |
| hash | PayU-calculated reverse hash. Verify before marking success or failure. Calculation: `sha512(SALT\|status\|\|\|\|\|\|udf5\|udf4\|udf3\|udf2\|udf1\|email\|firstname\|productinfo\|amount\|txnid\|key)`<br /><br />**Note:** Include only the `udf` fields that were posted in the request; leave others empty in the hash string. |
| error | Failure reason for failed transactions.<br /><br />**Note:** Failure reasons vary by bank error codes. |
| bankcode | Payment option code (for example, VISA, MAST). |
| PG\_TYPE | Payment gateway used (for example, `CC-PG`). |
| bank\_ref\_num | Bank reference number for successful transactions. |
| unmappedstatus | Internal PayU status. For more information, refer to [Payment State Explanations](ref:payment-state-explanations). |


#### binData fields description (applicable for only for Cards)

| Field | Description |
| --- | --- |
| pureS2SSupported | Indicates whether the card supports S2S: **true** (supports S2S) or **false** (does not support S2S). |
| issuingBank | The card issuing bank. |
| cardType | The card type such as VISA, MasterCard, etc. |
| isDomestic | Indicates whether the card is domestic or international: **true** (domestic) or **false** (international). |

#### Sample S2S response

```json
{
  "mihpayid": "403993715531077182",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "JPM7Fg",
  "txnid": "ypl938459435dfdfdf",
  "amount": "1000.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "addedon": "2024-02-27 15:00:42",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "ashish@gmail.com",
  "phone": "9876543210",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "896193988312194700",
  "field2": "857712",
  "field3": "1000.00",
  "field4": "",
  "field5": "00",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "AUTHORIZED",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "896193988312194700",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params.",
  "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
}
```

## Merchant Hosted Checkout

### Cards

#### Sample request

```curl
curl --location 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=nbn8otc350bsv6u5fqvhcbo73b; PHPSESSID=63a0499eaf13e' \
--data-urlencode 'key=JF****g' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'amount=10' \
--data-urlencode 'phone= 9876543210' \
--data-urlencode 'productinfo=Product_info' \
--data-urlencode 'surl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'furl=http://pp30admin.payu.in/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'lastname=Test' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=06' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid=jYhbOYH9o4' \
--data-urlencode 'hash=e5b286a9c8545038de9d4e4ee4d8a2fd02e821015aff7e0323807ba174997d8643f9aa174981385e3e4dfe60b918650806ccb97b3e8e3471e1985ecadefd0184' \
--data-urlencode 'ccnum=4012000000002004' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'threeDS2RequestData={
    "browserInfo": {
        "userAgent": "Mozilla\/5.0 (X11 Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) HeadlessChrome\/93.0.4577.0 Safari\/537.36",
        "acceptHeader": "*\/*",
        "language": "en-US",
        "colorDepth": "24",
        "screenHeight": "600",
        "screenWidth": "800",
        "timeZone": "-300",
        "javaEnabled": true,
        "ip": "10.248.2.71"
    }
}'
```

#### Sample response

**Formatted response**

```
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

### UPI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => 5jJ9xRceXX1ydT
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => vpa-anything@payu
    [field2] => 5jJ9xRceXX1ydT
    [field3] =>
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] =>
    [field7] => Transaction completed successfully
    [field8] =>
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
)
```

### Wallets

#### Sample request

```
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => CASH
    [status] => success
    [unmappedstatus] => captured
    [key] => J*****g
    [txnid] => HC13glcAkssIkl
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-10-21 17:45:24
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
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => CASH-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => CASH
    [error] => E000
    [error_Message] => No Error
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
)
```

### EMI

#### Sample request

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9123412345&productinfo=iPhone&pg=EMI&bankcode=ICICID03&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=43754118*****12346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523602563
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => v2tWbbdUOuacK9
    [amount] => 20000.00
    [discount] => 0.00
    [net_amount_debit] => 20000.00
    [addedon] => 2021-07-27 11:14:44
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
    [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => EMI-PG
    [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
    [bankcode]=> EMIA3
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] =>512345XXXXXX2346
)
```

### BNPL

#### Sample request

```
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => BNPL
    [status] => success
    [unmappedstatus] => captured
    [key] => J****g
    [txnid] => 5jJ9xYceXX1ydT
    [amount] => 1000.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => 9876543210
    [field2] => 5jJ9xRceXX1ydT
    [field3] =>
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] =>
    [field7] => Transaction completed successfully
    [field8] =>
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => BNPL-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => LAZYPAY
    [error] => E000
    [error_Message] => No Error
)
```

### QR

#### Sample response

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H \
 "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=ewP8oRopzdHEtC&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=QR&bankcode=UPIQR&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=bff508ec0974b20fe4be6c86cceab8c8dde88c4061a2a70373ddd0bbd3d24b21ae13984915fad06f9802f56b01a30da4e367e4e749959a76c3b2e5f12eb43319"
```

#### Sample response

```
(
    [mihpayid] => 403993715524045752
    [mode] => QR
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => ewP8oRopzdHEtC
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:27:08
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
    [hash] => 1be7e6e97ab1ea9034b9a107e7cf9718308aa9637b4dbbd1a3343c91b0da02b34a40d00ac7267ebe81c20ea1129b931371c555d565bc6e11f470c3d2cf69b5a3
    [field1] =>
    [field2] =>
    [field3] =>
    [field4] =>
    [field5] =>
    [field6] =>
    [field7] =>
    [field8] =>
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => QR-PG
    [bank_ref_num] => 87d3b2a1-5a60-4169-8692-649f61923b3d
    [bankcode] => UPIQR
    [error] => E000
    [error_Message] => No Error
)
```

<br />