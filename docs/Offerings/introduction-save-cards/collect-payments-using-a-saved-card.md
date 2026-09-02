---
title: Collect Payments using a Tokenized Card
excerpt: >-
  When your customer has an account on your shopping website, they may store
  their card details to use when they revisit your website (repeat payment).
deprecated: false
hidden: false
metadata:
  title: Collect Payments using a Saved Card
  description: >-
    Find out how to collect payments using a saved card on PayU India. This
    guide shows you how to use the Merchant Hosted Checkout integration to offer
    a seamless and secure payment experience to your customers.
  keywords:
    - Collect payments using saved cards
    - Collect payments with saved cards on PayU
    - Process transactions using saved cards
    - Payment with saved card
    - Payment using saved card
    - Payment using tokenised cards
    - Collect payment with tokenised cards
  robots: index
next:
  description: ''
---
PayU offers you API to tokenize the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page, similar to the following screenshot where they need to enter only the CVV:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/save_card_checkout-1024x817.jpeg)

This section explains the procedure for getting a customer’s card details and using a tokenized card to initiate payment.

***

For all the scenarios mentioned in this section you must follow the

1. **Get the tokenized card details**:  Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **get_user_details** API. For more information, refer to <Anchor target="_blank" href="ref:get_user_cards_api_model3">Get User Cards API - Model 3</Anchor> API  under API Reference.

2. **Post Payment to PayU and check response**: Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization:

   * [Using zero code change approach](#using-zero-code-change-approach)

   * [Using complete card details](#using-complete-card-details)

   * [Using network tokens](#using-network-tokens)

   * [Using issuer tokens](#using-issuer-tokens)

   * [Using card tokenized with PayU](#using-card-tokenized-with-payu)

   * [Using card on a decoupled flow with network token or other partner tokenization](#using-card-on-a-decoupled-flow-with-network-token-or-other-partner-tokenization)

   * [Using card on a decoupled flow with PayU tokenization](#using-card-on-a-decoupled-flow-with-payu-tokenization)

   <Callout icon="📘" theme="info">
     ### Notes:

     * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to Integrate with Merchant Hosted Checkout.
     * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to <Anchor target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor>
   </Callout>

3. **Verify the Payment**: Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify_payment** API to verify the payment. For more information, refer to [Verify Payment API](ref:verify_payment_api)

## Using zero code change approach

If the merchant wants PayU to tokenize the card using a zero code change approach (Model 2), use the request parameters as described in this section.

### Applicable Scenarios

* Merchant wants to create tokens without making any integration changes at their end
* Merchant is using PayU as a partner for tokenization

This scenario is applicable if any merchant sends the plain card request to PayU and shares the consent for saving the card details.

For the sample request and response, refer to [Zero Code Change - Model 2](doc:zero-code-change-for-vault-integration-model-2).

## Using complete card details

This scenario is applicable where a customer is providing the complete card number do the transaction (Card number, Expiry, CVV, and name on card) 

### Applicable Scenarios

* It is a guest checkout  
* It is a standard checkout request where there is no need to tokenize the card 

<Callout icon="📘" theme="info">
  Note: Plain card details coming from the merchant, so no changes are applicable in the request & response.
</Callout>

<Tabs>
  <Tab title="Request Parameters">
    | Parameter                    | Description                                                                                                                                                                                                                    | Example                                                                                                                                                    |
    | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | key<br />`mandatory`         | `String` The merchant key is a unique identifier for a merchant account in PayU's database.                                                                                                                                    | Your Test Key                                                                                                                                              |
    | api_version<br />`optional`  | `String` The API version for this API.                                                                                                                                                                                         | 1                                                                                                                                                          |
    | txnid<br />`mandatory`       | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. It is used to track the order and must be unique. PayU's system will not accept duplicate transaction IDs.           | s7hhDQVWvbhBdN                                                                                                                                             |
    | amount<br />`mandatory`      | `String` This field should contain the payment amount for the transaction. If you want to use the cardless EMI option, the amount must be at least Rs. 8000                                                                    | 10.00                                                                                                                                                      |
    | productinfo<br />`mandatory` | `String` It should be a string containing a brief description of the product.<br />`<br/>Character Limit-100<br/>`                                                                                                             | iPhone                                                                                                                                                     |
    | firstname<br />`mandatory`   | `String` The first name of the customer.<br />`<br/>Character Limit-60<br/>`                                                                                                                                                   | Ashish                                                                                                                                                     |
    | email<br />`mandatory`       | `String` The email of the customer.<br />`<br/>Character Limit-50<br/>`                                                                                                                                                        | [test@gmail.com](mailto:test@gmail.com)                                                                                                                    |
    | phone<br />`mandatory`       | `String` The phone number of the customer.<br /><br />**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.          | 9876543210                                                                                                                                                 |
    | lastname<br />`mandatory`    | `String` The last name of the customer.<br />`<br/>Character Limit-60<br/>`                                                                                                                                                    | Verma                                                                                                                                                      |
    | address1<br />`optional`     | `String` The first line of the billing address.<br />`<br/>Character Limit-100<br/>`                                                                                                                                           | H.No- 17, Block C, Kalyan Bldg, <br />Khardilkar Road, Mumbai                                                                                              |
    | address2<br />`optional`     | `String` The second line of the billing address.<br />`Character Limit-100`                                                                                                                                                    | 34 Saikripa-Estate, Tilak Nagar                                                                                                                            |
    | city<br />`optional`         | `String` The city where your customer resides as part of the billing address.                                                                                                                                                  | Mumbai                                                                                                                                                     |
    | state<br />`optional`        | `String` The state where your customer resides as part of the billing address.                                                                                                                                                 | Maharashtra                                                                                                                                                |
    | country<br />`optional`      | `String` The country where your customer resides.<br />`Character Limit-50`                                                                                                                                                    | India                                                                                                                                                      |
    | zipcode<br />`optional`      | `String` Billing address zip code is mandatory for the cardless EMI option.<br />`<br/>Character Limit-20<br/>`                                                                                                                | 400004                                                                                                                                                     |
    | surl<br />`mandatory`        | `String` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.               | [https://apiplayground<br />-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                       |
    | furl<br />`mandatory`        | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                   | [https://apiplayground-response.<br />herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                       |
    | hash<br />`mandatory`        | `String` It is used to avoid the possibility of transaction tampering. For more information on hash generation process, refer to Generate Hash.                                                                                | `eabec285da28fd0e3054d41a4d24fe9f`<br />`7599c9d0b66646f7a9984303fd612404`<br />`4b6206daf831e9a8bda28a6200d318293`<br />`a13d6c193109b60bd4b4f8b09c90972` |
    | pg<br />`mandatory`          | `String` The pg parameter determines which payment tabs will be displayed. Here, use 'CC' as the value.                                                                                                                        | CC                                                                                                                                                         |
    | bankcode<br />`mandatory`    | `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it.                                               | AMEX                                                                                                                                                       |
    | udf1 - udf5<br />`optional`  | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5.<br />`Character Limit-255` | Payment Preference, <br />Shipping Method, <br />Shipping Address1, <br />Shipping City, Shipping Zip Code, etc.                                           |
    | ccnum<br />`optional`        | `varchar` This parameter must contain the 13 to 19-digit card number for credit or debit cards in general.                                                                                                                     | 512\*\*\*6789012346                                                                                                                                        |
    | ccname<br />`optional`       | `varchar` It is the customer's name on card.                                                                                                                                                                                   | Ashish                                                                                                                                                     |
    | ccvv<br />`optional`         | `varchar` This parameter must contain the CVV number of the card – as entered by the customer for the transaction.                                                                                                             | 123                                                                                                                                                        |
    | ccexpmon<br />`mandatory`    | `integer` This parameter must contain the Expiry month that is mentioned under card validity.                                                                                                                                  | 10                                                                                                                                                         |
    | ccexpyr<br />`mandatory`     | `integer` This parameter must contain the Expiry year that is mentioned under card validity.                                                                                                                                   | 2022                                                                                                                                                       |
  </Tab>

  <Tab title="Sample Request">
    ```curl
    ```
  </Tab>
</Tabs>

## Using network tokens

This scenario is applicable if you wanted to collect payments using network tokens.

### Applicable scenarios

* Merchant has the `card token`, `TAVV`(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if you are PCI compliant and got the network token and `TAVV` from any other aggregator or schemes and then sending the card transaction request in the form of authentication.
</Callout>

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-network-tokens">Using Network Tokens</Anchor>

## Using issuer tokens

This scenario is applicable if you wanted to collect payments using issuer tokens.

### Applicable scenarios

* Merchant has the `card token`, `trMerchantId`, `tokenReferenceId`, and the last four digits of the card 
* The token could be created by the issuer

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if you are PCI compliant and got the `issuer token`, `trMerchantId`, and `tokenReferenceId` and then sending the card transaction request in the form of authentication.
</Callout>

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-issuer-tokens">Using Issuer Tokens</Anchor>.

## Using card tokenized with PayU

If the merchant has tokenized the card with PayU and needs to process the transaction using PayU token only. 

### Applicable scenarios

* Merchant has created the token using PayU  as the partner 

<Callout icon="📘" theme="info">
  ### Note:

  This scenario is applicable if any PCI or Non-PCI complied merchant sends the PayU token in a request for fulfilment purposes.
</Callout>

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-tokenized-with-payu">Using Card Tokenized with PayU</Anchor>.

## Using card on a decoupled flow with network token or other partner tokenization

This scenario is applicable where you are on a decoupled flow. This is where you are using the PayU for either authentication or authorization only while using tokens created by the network or some other partner. 

**Decoupled flow**: You are sending the authentication request to PayU and if the merchant wishes to send the authorization request eventually or to other aggregators.

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-tokenized-with-payu">Using Card on a Decoupled Flow with Network Token or Other Partner Tokenization</Anchor>.

## Using card on a decoupled flow with PayU tokenization

This scenario is the application on a decoupled flow using the PayU for either authentication or authorization only with tokens created in partnership with PayU.

**Direct Authorisation Flow**: When you have done the authentication from some other aggregator and authorization request is coming to PayU.

For the sample request and response, refer to <Anchor target="_blank" href="ref:using-card-on-a-decoupled-flow-with-payu-tokenization">Using Card on a Decoupled Flow with PayU Tokenization</Anchor>.

<br />
