---
title: Cards Consent Transaction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Explore how to set up a Cards (Debit or Credit) Recurring Payment Consent
    Transaction using PayU Hosted Checkout. This API documentation provides
    details for integrating Cards consent API, enabling secure and efficient
    recurring payments for your customers
  keywords:
    - PayU Cards Recurring Payment for Custom Checkout
    - ' Cards Consent Transaction for Custom Checkout'
    - ' PayU Cards Recurring Payment for Merchant Hosted Checkout'
    - ' Cards Consent Transaction for Merchant Hosted Checkout'
    - ' PayU recurring payments for Cards'
    - ' PayU subscription payments registration for Credit Cards'
    - ' Credit Card Registration transaction for Custom Checkout'
    - Credit Cards Registration transaction for Merchant Hosted Checkout
    - ' Cards Autopay'
    - ' Autopay for Cards non-PACB flow'
    - ' Cards Autopay Consent Transaction'
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
This section provides the request parameters, sample request and response for a Cards Recurring Payment.

<Callout icon="📘" theme="info">
  **Note**: During integration with PayU, first integrate with the Test Server environment. PayU will provide you the necessary Merchant Key for the test serve. After testing is done, you are ready to move to the Production server.
</Callout>

HTTP Method: **POST**

**Environment**

|                        |                                                                        |
| :--------------------- | :--------------------------------------------------------------------- |
| Test Environment       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| Production Environment | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |

**Content Type**: application/x-www-form-urlencoded

## Request parameters

| Parameter                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Value                                                                                                                              |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| key<br />`mandatory`                    | `String` The merchant key is a unique identifier for a merchant account in PayU's database. For more information, [Check your API Key and Salt](http://docs.payu.in/docs/check-api-key-and-salt).                                                                                                                                                                                                                                                                                                                                                                                                                    | Your Test Key                                                                                                                      |
| api_version<br />`optional`             | `String` The API version for this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 7                                                                                                                                  |
| txnid<br />`mandatory`                  | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.                                                                                                                                                                                                                                                                                                                                                                                                 | s7hhDQVWvbhBdN                                                                                                                     |
| amount<br />`mandatory`                 | `String` This field should contain the payment amount for the transaction.<br />**Note**: The transaction limit are as per the card holders limit or Rs.10,00,000 (if the card limit is more than Rs.10,00,000).                                                                                                                                                                                                                                                                                                                                                                                                     | 10.00                                                                                                                              |
| productinfo<br />`mandatory`            | `String` It should be a string containing a brief description of the product. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | iPhone                                                                                                                             |
| firstname<br />`mandatory`              | `String` The first name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ashish                                                                                                                             |
| email<br />`mandatory`                  | `String` The email of the customer. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [test@gmail.com](mailto:test@gmail.com)                                                                                            |
| phone<br />`mandatory`                  | `String` The phone number of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 9876543210                                                                                                                         |
| lastname<br />`mandatory`               | `String` The last name of the customer. `Character Limit-60`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Verma                                                                                                                              |
| address1<br />`optional`                | `String` The first line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai                                                                            |
| address2<br />`optional`                | `String` The second line of the billing address. `Character Limit-100`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 34 Saikripa-Estate, Tilak Nagar                                                                                                    |
| city<br />`optional`                    | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Mumbai                                                                                                                             |
| state<br />`optional`                   | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Maharashtra                                                                                                                        |
| country<br />`optional`                 | `String` The country where your customer resides. `Character Limit-50`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | India                                                                                                                              |
| zipcode<br />`optional`                 | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit-20`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 400004                                                                                                                             |
| si<br />`mandatory`                     | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections:<br />- [Manage Recurring Payment for Cards](http://docs.payu.in/reference/manage-recurring-payment-for-cards)                                                                                                                                                                   | 1                                                                                                                                  |
| si_details<br />`mandatory`             | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers (for more details refer – [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)).<br />This is a JSON object and it includes a set of fields. For more information, refer to [SI Parameter JSON Details](http://docs.payu.in/reference/si-parameter-json-details). |                                                                                                                                    |
| hash<br />`mandatory`                   | `String` It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to [Hashing Request and Response](http://docs.payu.in/docs/generate-hash-merchant-hosted).<br />In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br />`HASH = SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|si_details\|SALT)`                                                                                                                                         | `eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972` |
| pg<br />`mandatory`                     | `String` Determines the payment method (or category) used for the transaction. Possible values: <ul><li>`DC`: For debit cards</li> <li>`CC`: For credit cards</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                              | CC                                                                                                                                 |
| bankcode<br />`mandatory`               | `String` A unique bank code of a payment option. Possible values: <ul><li>`CC`: For Visa and Mastercard credit cards</li> <li>`AMEX`: For American Express credit and debit cards</li> <li>`RUPAYCC`: For RuPay credit cards</li> <li>`VISA`: For Visa debit cards</li> <li>`MAST`: For Mastercard debit cards</li> <li>`RUPAY`: For RuPay debit cards</li></ul>                                                                                                                                                                                                                                                     | RUPAYCC                                                                                                                            |
| udf1 - udf5<br />`optional`             | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. `Character Limit-255`                                                                                                                                                                                                                                                                                                                                                                                            | Payment Preference, Shipping Method, Shipping Address1, Shipping City, Shipping Zip Code, etc.                                     |
| ccnum<br />`conditional`                | `Integer` This parameter must contain the card number.<br />This parameter is required if you are trying to create a mandate using the card details.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |
| ccvv<br />`mandatory`                   | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.<br />**Note**: If your customer is returning to your website to shop, you must fetch all the customer's stored cards from PayU, collect the CVV for the card the customer will be using to make payment and then post the CVV number to PayU.                                                                                                                                                                                                                                                     | 123                                                                                                                                |
| ccexpmon<br />`mandatory`               | `integer` This parameter must contain the network token expiry month. For stored card using network or issuer, enter the expiry month of the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 10                                                                                                                                 |
| ccexpyr<br />`mandatory`                | `integer` This parameter must contain the network token expiry year. For stored card using network or issuer, enter the expiry year of the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 2022                                                                                                                               |
| store_card_token<br />`conditional`     | `varchar` This must include the Network token generated at your end.<br />This parameter is required if you are using the stored card token to register the mandate.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1234 4567 2456 3566                                                                                                                |
| storecard_token_type<br />`conditional` | `integer` This parameter is used to specify the store card token type. It must include any of the following values:<br />- **0**: If PayU token is used.<br />- **1**: If Network token is used.<br />- **2**: If Issuer token is used.<br />This parameter is required if you are using the stored card token to register the mandate.                                                                                                                                                                                                                                                                              | 1                                                                                                                                  |
| additional_info<br />`conditional`      | `varchar` This parameter will contain the additional information in the following JSON format: `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`<br />This parameter is required if you are using the stored card token to register the mandate, where network or issuer token is used.                                                                                                                                                                                                                                                                                  | `{"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}`                                      |
| free_trial<br />`conditional`           | This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.<br />In this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.<br />This parameter has no significance in the case of seamless flow.                                                                                                                                                                        |                                                                                                                                    |

> 📘 Notes for **additional_info** parameter:
>
> The JSON format contains the following fields:
>
>  
>
> * **trid** (Token Requestor ID) is the identifier given by the networks for creating the tokens. You should be able to get the same from your token provider.
> * **tokenRefNo** (Token Reference Number) is generated along with the network token. You should be able to get the same from your token provider.
> * **TAVV** is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.
>
> Additional notes:
>
> * The last 4 digits of cards is mandatory for all transactions.   
> * Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
> * Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.

> 📘 Notes for bankcode
>
> Debit Card or Credit Card: There are different options like Visa Debit Card, Mastercard, Maestro, etc. For each option, a unique bank code exists and it would be returned in this bankcode parameter. For more information, refer to Card Type Codes. For example, VISA for VISA Debit Card.

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

* Characters: A to Z, a to z, 0 to 9
* – (Minus)
* _ (Underscore)
* @ ()
* / (Slash)
* (Space)
* . (Dot)

## Sample request

The sample code block for cards Seamless integration (Merchant-Hosted Checkout) is similar to the following:

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68ed52caaaf5e' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_42683' \
--data-urlencode 'amount=1' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_42683' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=RUPAYCC' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response/' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'ccnum=5123456789012346' \
--data-urlencode 'ccexpmon=05' \
--data-urlencode 'ccexpyr=2027' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'si_details={"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2027-12-01"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```

## Sample response

In the case of Cards, you must ensure that the payment response from PayU has the expected values as described in the following table so that they successfully registered for a recurring plan or subscription for the customer:

| Response Parameter | Expected Value                   | Description                                                                     |
| ------------------ | -------------------------------- | ------------------------------------------------------------------------------- |
| status             | success                          | This indicates that the transaction is successful                               |
| cardToken          | \<card_token> sent by PayU       | Indicates that card details are saved correctly in PayUBiz Database             |
| payment_source     | sist                             | Indicates that card details have been marked correctly for Standing Instruction |
| mihpayid           | \<mihpayid number> sent. by PayU | Indicates PayU’s transaction acknowledgment for a Consent transaction           |

<Callout icon="📘" theme="info">
  **Notes**:

  * If any of the above four checks are not satisfied, that means the transaction has not been correctly authorized for Standing Instruction. The merchant must not consider this transaction eligible for the Recurring platform.
  * Registration transaction must be successful in making it eligible for the Recurring platform.
</Callout>

At this step, if the status of the consent transaction is returned as success along with the other three conditions explained above, you can consider that the subscription setup is completed successfully.

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Parsed response

```
Array
(
    [mihpayid] => 25600342065
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => 1d1a28fe1281c04b1968
    [amount] => 1.00
    [cardCategory] => signature_premium
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-14 11:06:59
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
    [hash] => f67284c77d6fe59b092ef98a735ba78bd8c484b14b364cad42520fb8724d5d72b6f3c05439a56c7fe921a262027699de14edb92b03ca2e6284e66b6a81d98bcc
    [field1] => 7604202397746612005910
    [field2] => 175975
    [field3] => 1.00
    [field4] => 
    [field5] => 00
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => AUTHORIZED
    [field9] => Transaction is Successful
    [payment_source] => sist
    [meCode] => {"MID":"hdfc_89051842","TKey":"0wMbyodmbgzwIOejqyUOpAkCJdBC01zQGwHS+Pm1rGGxBki5xPR60G948KUmnPR5l7xDpxYOWIOLfE1q0z5ezIA7dG/yVAkp4nZmbddhWyNpdLusIKmiJzXH6ASAMJKZJ0dH3NyQypy9w51PfUKAz80I4y4Udq8zCKB+yiDP3JqkOfz366Y5SjKI/BWNMXCMXOXIvzVNSinDVi4bVW+WtimdJ1BS9WACx8zkYjPjTkuGB6TMYeJGYt0JJ6oSQce4xk4yW3al+fFABVC26S+2wNuHYMMFvhd09AK4nUvFMh9SHjhWWw6T81miW2kqxi0o+rdvCCYEO3Aa3R5kH8kmIw=="}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 7604202397746612005910
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [cardToken] => 6a3b14bce0ae8634d70be
    [card_token] => 6a3b14bce0ae8634d70be
    [cardnum] => XXXXXXXXXXXX4879
)
```

## Webhook for Getting Transaction Details

You can expose a webhook by requesting the PayU Integration team to configure the same against the **ws_online_response** parameter. If this webhook is configured, you will receive the above response object over HTTP form post method similar to the following:

```plaintext
unmappedstatus=success&phone=9999999999&txnid=FCDA1R100870163781&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&curl=https://www.abc.in/payment/handlepayuresposne&firstname=NA&card_no=519619XXXXXX5049&furl=https://www.abc.in/payment/handlepayuresposne&productinfo=2&mode=DC&amount=800.00&field4=6807112311042810&field3=6807112311042810&field2=838264&field9=SUCCESS&email=NA&mihpayid=175477248&surl=https://www.ABC.in/payment/handlepayuresposne&card_hash=9e88cb0573d4a826b61d808c0a870ed4a990682459b0ec9e95ea421e8e47be8c&field1=42812&payment_source=sist
```

If the mandate is not confirmed by the customer or the mandate is confirmed by the customer, but the mandate registration is rejected from the banks, the status is communicated as a “failure” over webhook. For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).
