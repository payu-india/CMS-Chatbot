---
title: Using Network Tokens
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collecting Payments from Saved card using Tokens
  description: >-
    Discover how to use the _payment API to process payments with saved card
    tokens. This guide provides detailed instructions, request parameters, and
    sample responses for collecting payment with saved card tokens.
  robots: index
next:
  description: ''
---
This scenario is applicable if you wanted to collect payments using network tokens.

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Applicable scenarios

* Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

> 📘 Note
>
> This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sending the card transaction request in the form of authentication.

## Request Parameters


> 📘 Notes for additional\_info:
>
> * The last 4 digits of cards is mandatory for all transactions.
> * Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
> * Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.

## Response

There are no changes in the response, it will remain as it is like the existing plain card number.