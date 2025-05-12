---
title: Handling Guest Checkout Transactions
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Handling Guest Checkout Transaction
  description: >-
    RBI regulations mandate that acquirers cannot store card details post-31st
    Oct. 2023, requiring tokenization of card numbers for guest checkouts, with
    three scenarios for handling Alternative IDs involving PayU.
  keywords:
    - Alternative ID
    - ' Alt ID'
    - ' Guest Checkout'
    - ' additional_info for Guest Checkout'
    - ' alt_id'
  robots: index
next:
  description: ''
---
Guest Checkout is a valuable feature that can provided be enabled for your e-commerce websites. It allows your customers to make purchases without the need to sign in or create a user account. This streamlined process benefits one-time or occasional shoppers, as it eliminates the registration step, leading to faster transactions and enhanced customer satisfaction.

> 📘 Enable this feature:
>
> To enable this feature, contact your PayU Key Account Manager or PayU Integration Support.

As per RBI compliances, acquirers are also not allowed to store card details after a stipulated timeline. As per recommendations from RBI end, Guest checkout transactions won’t be allowed post 31st Oct. 2023. Guest checkout PAN should be replaced with some alternative number for transaction processing. As per the new regulations on guest checkout, where we have to tokenise plain card numbers. This token is called Alternative ID or Alt ID.

There are three scenarios with Alternative ID:

<Image align="center" width="900px" src="https://files.readme.io/f84108124634526cf547dac1d59ff3272600f8cfd26f486baba8425033ddf5c8-Guest-checkout-alt-id-implementation-methods.png" />

## Scenario 1: Provision & processes guest transaction with PayU

No changes required in the **\_payment** request used to collect payments.

## Scenario 2: Provision Alt ID outside PayU and use PayU to Process Transaction

### Request parameters

Along with the parameters listed in the [Collect Payment API - Cards (Merchant Hosted Checkout)](ref:payment_merchant_hosted_cards), you have to pass alt ID as a variable and pass TAVV (Cryptogram), last four digits and **par** parameter as part of **additional\_info** JSON. There is no change in the response and it remains the same. 

> 📘 Note:
>
> The **par** parameter is optional as part of **additional\_info** JSON.

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
        <Glossary>pg</Glossary>
        **mandatory**
      </td>

      <td>
        `String` The pg parameter determines which payment tabs will be displayed on the PayU page.  For cards, 'CC' will be the value.
      </td>

      <td>
        CC
      </td>
    </tr>

    <tr>
      <td>
        <Glossary>bankcode</Glossary> **mandatory**
      </td>

      <td>
        `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it.
      </td>

      <td>
        AMEX
      </td>
    </tr>

    <tr>
      <td>
        alt\_id\
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain Alt ID for the guest checkout.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        ccexpmon\
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain the Alt ID expiry month.\
        For VISA cards, Plain card's expiry month need to be posted this parameter. 
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        ccexpyr\
        **mandatory**
      </td>

      <td>
        `String` This parameter must contain the Alt ID expiry year.\
        For VISA cards, Plain card's expiry year need to be posted this parameter.
      </td>

      <td>
        2021
      </td>
    </tr>

    <tr>
      <td>
        additional\_info\
        **mandatory**
      </td>

      <td>
        `JSON`The fields which are included in this JSON are described in the [additional\_info JSON sample and field description](#additional_info-json-sample-and-field-description) section. 
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> **tokenReferenceid** field is required in the additional\_info parameter if you are provisioning Alt ID outside PayU for Diners card.

#### additional\_info JSON sample and field description

```
{  
"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==",  
"last4Digits":"2346",  
"par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1",  
"tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"  
}
```

The description of the fields in the additional\_info JSON.

| Field            | Description                                                                                                                                                                   |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| trid             | trid is the acronym for Token Requestor ID and it is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider. |
| tokenReferenceID | The Token Reference ID is generated along with the network token. You should be able to get the same from your token provider.                                                |
| TAVV             | It is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.                                                                   |

### Sample Request

```curl
curl --location 'http://local.secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=smsplus' \
--data-urlencode 'firstname={{firstname}}' \
--data-urlencode 'email={{email}}' \
--data-urlencode 'amount={{amount}}' \
--data-urlencode 'phone=9999999999' \
--data-urlencode 'productinfo={{productinfo}}' \
--data-urlencode 'surl=your own success url'  \
--data-urlencode 'furl=your own failure url'  \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=MASTERCARD' \
--data-urlencode 'alt_id=5123456789012346' \
--data-urlencode 'additional_info={"tavv":"AKF/FaM3BPWoAAEWYTiQAAADFA==","last4Digits":"2346","par":"799F3ED865F5965CC760A32682BA8A80F19E99ECB3F7F03574C14F5B6C3EB2C1","tokenReferenceId":"3acdd709-3c4b-4280-a6db-3f02271d09a3"}' \
--data-urlencode 'ccname=Flipkart' \
--data-urlencode 'ccvv=126' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2024' \
--data-urlencode 'txnid={{txnid}}' \
--data-urlencode 'hash={{hash}}' \
```

### Sample response

> 📘 Notes:
>
> The **authRefNo** response parameter contains:
>
> * <Glossary>AEVV</Glossary> number for an AMEX card transaction. This is mandatory for AMEX for compliance for token (<Glossary>CoFT</Glossary>) provisioning. 
> * rupayAuthRefId for a Rupay card transaction
>
> To enable the  **authRefNo** response parameter in response, contact your PayU Key Account Manager or [PayU Support](https://help.payu.in).

```
Array
(
    [mihpayid] => 20869277619
    [mode] => CC
    [status] => failure
    [unmappedstatus] => failed
    [key] => L43t1c
    [txnid] => 26ba7cd6a67b0a010542
    [amount] => 1.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 0.00
    [addedon] => 2024-09-05 17:46:10
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
    [hash] => ac7720e4bc33e5494bec6d37302e522171175a987f9d47286bfd29e8a7fc794f56433fcacf0bc120db781c4dc1d05a4857d71e83f00f6ed6aa9c97a1938b9467
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 05
    [field6] => 
    [field7] => AUTHNEGATIVE
    [field8] => 
    [field9] => Authorization failed at Bank
    [payment_source] => payu
    [pa_name] => PayU
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 2409052690
    [bankcode] => AMEX
    [error] => E1903
    [error_Message] => Authorization failed at Bank
    [cardnum] => XXXXXXXXXXXX2003
    [cardhash] => This field is no longer supported in postback params.
    [authRefNo] => AAAXXXlxAAICQkXXXEAEAAXXXX=
    [corporate_card] => 0
    [cobranded_card] => AMEX_CONSUMER
    [splitInfo] => {"splitStatus":"","splitSegments":[]}
)
```

<br />

### Scenario 3: Provision Alt ID from PayU

The Provision Alt ID API is used to provision Alt ID from PayU, but process transaction outside PayU. For more information, refer to [Provision Alt ID API](ref:provision-alt-id-api).