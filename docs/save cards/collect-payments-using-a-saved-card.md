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
PayU offers you API to save the card details and retrieves them using the Store Card APIs. For example, the stored cards are displayed when your customer performs checkout and lands on the payment page.

This section explains the procedure for getting a customer’s card details and using a saved card to initiate payment.

***

For all the scenarios mentioned in this section you must follow the

1. **Get the saved card details**:  Get the customer’s card details your merchant key and customer’s registered mail ID to PayU using the **get\_user\_details** API. For more information, refer to <Anchor label="Get User Cards API - Model 3" target="_blank" href="https://docs.payu.in/v2/reference/v2_get_user_cards_api/">Get User Cards API - Model 3</Anchor> API  under API Reference.

2. **Post Payment to PayU and check response**: Make the transaction request with the payment details along with the card nickname to PayU based on the following scenarios of tokenization. For more information, refer to

   * [Using complete card details](#using-complete-card-details)

   * [Using network tokens](#using-network-tokens)

   > 📘 Notes:
   >
   > * In addition to the request parameters used for Merchant Hosted Checkout (Seamless integration) payment request, you need to ensure the additional parameters as specified in each scenario specified in this step. For more information on the complete list of parameters, refer to Integrate with Merchant Hosted Checkout.
   > * The additional response parameters (if any) are specified for each scenario. For the sample response for a card payment using Merchant Hosted Checkout response, refer to <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="https://docs.payu.in/v2/update/reference/v2_payment_seamless_integration/">Collect Payment API - Merchant Hosted Checkout</Anchor>

3. **Verify the Payment**: Verify the transaction details using the Verification APIs. Post the transaction ID using the **verify\_payment** API to verify the payment. For more information, refer to <Anchor label="Verify Payment API" target="_blank" href="https://docs.payu.in/v2/reference/v2_verify_payment_api/">Verify Payment API</Anchor>

## Using complete card details

This scenario is applicable where a customer is providing the complete card number do the transaction (Card number, Expiry, CVV, and name on card) 

### Applicable Scenarios

* It is a guest checkout  
* It is a standard checkout request where there is no need to save the card 

> 📘 Note:
>
> Plain card details coming from the merchant, so no changes are applicable in the request & response.

For the sample request and response, refer to <Anchor label="Using Complete Card Details" target="_blank" href="https://docs.payu.in/v2/reference/complete-card-details-payment/">Using Complete Card Details</Anchor>

## Using network tokens

This scenario is applicable if you wanted to collect payments using network tokens.

### Applicable scenarios

* Merchant has the `card token`, `TAVV`(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

> 📘 Note:
>
> This scenario is applicable if you are PCI compliant and got the network token and `TAVV` from any other aggregator or schemes and then sending the card transaction request in the form of authentication.

For the sample request and response, refer to <Anchor label="Using Network Tokens" target="_blank" href="https://docs.payu.in/v2/reference/using-network-tokens/">Using Network Tokens</Anchor>