---
title: Complete Card Details
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment from Saved Card with Complete Card Details
  description: >-
    Learn how to use the _ayment API to process transactions using full card
    details. This sectoin provides detailed instructions, request parameters,
    and sample responses for efficient card management.
  robots: index
next:
  description: ''
---
This scenario is applicable where a customer is providing the complete card number do the transaction (Card number, Expiry, CVV, and name on card) 

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Applicable scenarios

* It is a guest checkout  
* It is a standard checkout request where there is no need to save the card 

> 📘 Note
>
> Plain card details coming from the merchant, so no changes are applicable in the request & response.

Request and response elements will remain intact as it is.

## Request parameters


## Response

In addition to the parameters in the response of a Merchant Hosted Checkout transaction with a card, PayU returns network token, network token expiry for PCI complied or PayU token & its expiry for non-PCI complied merchants.