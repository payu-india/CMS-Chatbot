---
title: Using Issuer Tokens
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collect Payment using Card Issuer Tokens
  description: >-
    Discover how to use the _paymenb API to collect payments using issuer tokens
    for a saved card. This section provides detailed instructions, request
    parameters, and sample responses to to collect payments using issuer tokens
    for a saved card.
  keywords:
    - Using Issuer Tokens API
    - ' issuer tokens'
    - ' card management'
    - ' tokenization'
    - ' secure card storage'
    - ' process payments'
    - ' collect payments'
  robots: index
next:
  description: ''
---
This scenario is applicable if you wanted to collect payments using issuer tokens.

HTTP Method: **POST**

<PaymentAPIEnvironment />

## Applicable scenarios

* Merchant has the card token, trMerchantId, tokenReferenceId, and the last four digits of the card 
* The token could be created by the issuer

> 📘 Note
>
> This scenario is applicable if you are PCI compliant and got the issuer token, trMerchantId, and tokenReferenceId and then sending the card transaction request in the form of authentication.

## Request parameters


## Response

There are no changes in the response, it will remain as it is like the existing plain card number.