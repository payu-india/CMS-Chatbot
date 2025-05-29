---
title: Payment with Zero Code Change
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment using Saved Cards with Zero Code Change
  description: >-
    Explore how to use the _payment API to enable saved card functionality
    without any code changes. This section provides detailed instructions,
    request parameters, and sample responses for collecting payment from saved
    cards with zero code change.
  robots: index
next:
  description: ''
---
If the merchant wants PayU to tokenize the card using a zero code change approach (Model 2), use the [request parameters](#request-parameters) as described in this section.

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Applicable scenarios

* Merchant wants to create tokens without making any integration changes at their end
* Merchant is using PayU as a partner for tokenization 

This scenario is applicable if any merchant sends the plain card request to PayU and shares the consent for saving the card details. 

## Request parameters


## Response

PayU returns PayU token in response (the existing field **card\_token** in current response). If the merchant needs network and issuer token, they may call **get\_payment\_instument** with PayU token as input. For more information on **get\_payment\_instument**, refer to [Get User Cards API](ref:get_user_cards_api_model3).

## Sample response

### Success scenario

PayU will return the response (unformatted) similar to the following on the **surl** specified using **\_payment** API in JSON format:

```plaintext
{
  "mihpayid": "999000000001268",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "J****g",
  "txnid": "2b019fa0976d7480cf5",
  "amount": "10.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "net_amount_debit": "10",
  "addedon": "2021-11-29 11:51:35",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "1234567890",
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
  "hash": "82df12630b4e4083a90b314534872dfb22e97aaa191b1b93db2a76351561bd612a0b321609b0e31a3b7b62d1928c8e67e9fed5b2b5209deba4366c58706c1ffe",
  "field1": "3245029356632939671830",
  "field2": "302404",
  "field3": "10.00",
  "field4": "999000000001268",
  "field5": "100",
  "field6": "02",
  "field7": "AUTHPOSITIVE",
  "field8": "",
  "field9": "Transaction is Successful",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "3245029356632939671830",
  "bankcode": "CC",
  "error": "E000",
  "error_Message": "No Error",
  "cardToken": "28b99d39e83e8031caa7ad",
  "name_on_card": "Test User",
  "cardnum": "XXXXXXXXXXXX2346",
  "cardhash": "This field is no longer supported in postback params."
}

```

### Failure scenario

PayU will return the response (unformatted) similar to the following on the **furl** specified using **\_payment** API in JSON format:

```plaintext
{
  "mihpayid": "412345678912344659",
  "mode": "",
  "status": "failure",
  "unmappedstatus": "userCancelled",
  "key": "J****g",
  "txnid": "4ed74a05e1220e885f70",
  "amount": "10.00",
  "discount": "0.00",
  "net_amount_debit": "0.00",
  "addedon": "2019-12-20 11:58:49",
  "productinfo": "Product Info",
  "firstname": "Payu-Admin",
  "lastname": "",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@example.com",
  "phone": "1234567890",
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
  "hash": "159e1935d6a8e80c3fd2170bdc7397e1fac48be772f3515be0d728cd402b3420734944de45f8f70a4329dfafe2327200f41bc580d6c96fc0c2ce986ce3a67162",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "Cancelled by user",
  "payment_source": "payu",
  "PG_TYPE": "",
  "bank_ref_num": "",
  "bankcode": "",
  "error": "E1605",
  "error_Message": "Transaction failed due to customer pressing cancel button.",
  "card_token": ""
}

```