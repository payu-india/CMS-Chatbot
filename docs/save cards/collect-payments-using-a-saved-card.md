---
title: Collect Payments using a Saved Card
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
PayU offers you API to save the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page, similar to the following screenshot where they need to enter only the CVV:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2021/11/save_card_checkout-1024x817.jpeg)

This section explains the procedure for getting a customer’s card details and using a saved card to initiate payment.

***

For all the scenarios mentioned in this section you must follow the 

1. **Get the saved card details**:  Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **get\_user\_details** API. For more information, refer to [Get User Cards API - Model 3](ref:get_user_cards_api_model3) API  under API Reference.

2. **Post Payment to PayU and check response**: Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization:

   * [Using zero code change approach](#using-zero-code-change-approach)
   * [Using complete card details](#using-complete-card-details)
   * [Using network tokens](#using-network-tokens)
   * [Using issuer tokens](#using-issuer-tokens)
   * [Using card tokenized with PayU](#using-card-tokenized-with-payu)
   * [Using card on a decoupled flow with network token or other partner tokenization](#using-card-on-a-decoupled-flow-with-network-token-or-other-partner-tokenization)
   * [Using card on a decoupled flow with PayU tokenization](#using-card-on-a-decoupled-flow-with-payu-tokenization)

   > 📘 Notes:
   >
   > * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to Integrate with Merchant Hosted Checkout.
   > * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)

3. **Verify the Payment**: Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify\_payment** API to verify the payment. For more information, refer to [Verify Payment API](ref:verify_payment_api)

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
* It is a standard checkout request where there is no need to save the card 

> 📘 Note:
>
> Plain card details coming from the merchant, so no changes are applicable in the request & response.

For the sample request and response, refer to [Using Complete Card Details](ref:complete-card-details-payment)

## Using network tokens

This scenario is applicable if you wanted to collect payments using network tokens.

### Applicable scenarios

* Merchant has the `card token`, `TAVV`(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the network token and `TAVV` from any other aggregator or schemes and then sending the card transaction request in the form of authentication.

For the sample request and response, refer to [Using Network Tokens](ref:using-network-tokens)

## Using issuer tokens

This scenario is applicable if you wanted to collect payments using issuer tokens.

### Applicable scenarios

* Merchant has the `card token`, `trMerchantId`, `tokenReferenceId`, and the last four digits of the card 
* The token could be created by the issuer

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the `issuer token`, `trMerchantId`, and `tokenReferenceId` and then sending the card transaction request in the form of authentication.

For the sample request and response, refer to [Using Issuer Tokens](ref:using-issuer-tokens).

## Using card tokenized with PayU

If the merchant has tokenized the card with PayU and needs to process the transaction using PayU token only. 

### Applicable scenarios

* Merchant has created the token using PayU  as the partner 

> 📘 Note:
>
> This scenario is applicable if any PCI or Non-PCI complied merchant sends the PayU token in a request for fulfilment purposes.

For the sample request and response, refer to [Using Card Tokenized with PayU](ref:using-card-tokenized-with-payu).

## Using card on a decoupled flow with network token or other partner tokenization

This scenario is applicable where you are on a decoupled flow. This is where you are using the PayU for either authentication or authorization only while using tokens created by the network or some other partner. 

**Decoupled flow**: You are sending the authentication request to PayU and if the merchant wishes to send the authorization request eventually or to other aggregators.

For the sample request and response, refer to [Using Card on a Decoupled Flow with Network Token or Other Partner Tokenization](ref:using-card-tokenized-with-payu-1).

## Using card on a decoupled flow with PayU tokenization

This scenario is the application on a decoupled flow using the PayU for either authentication or authorization only with tokens created in partnership with PayU.

**Direct Authorisation Flow**: When you have done the authentication from some other aggregator and authorization request is coming to PayU.

For the sample request and response, refer to [Using Card on a Decoupled Flow with PayU Tokenization](ref:using-card-on-a-decoupled-flow-with-payu-tokenization).
