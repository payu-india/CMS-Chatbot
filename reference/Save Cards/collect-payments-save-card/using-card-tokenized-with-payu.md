---
title: Using Card Tokenized with PayU
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Learn how to use the _payment API to process transactions with Payu
    tokenized cards. This guide provides detailed instructions, request
    parameters, and sample responses for processing transactions with Payu
    tokenized cards.
  robots: index
next:
  description: ''
---
If the merchant has tokenized the card with PayU and needs to process the transaction using PayU token only.

HTTP Method: **POST**

<PaymentAPIEnvironment/>

## Applicable scenarios

* Merchant has created the token using PayU as the partner

> 📘 Note
>
> This scenario is applicable if any PCI or Non-PCI complied merchant sends the PayU token in a request for fulfilment purposes.

## Request parameters

## Response

The response is similar to plain card details.