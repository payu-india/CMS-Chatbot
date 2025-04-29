---
title: Flutter UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Flutter UPI SDK
  description: >-
    This document outlines the knowledge base for UPI transactions, detailing
    the differences between Collect and Intent transactions, and provides
    guidance on integrating UPI SDK with React Native and Flutter, including
    compatibility requirements and integration steps.
  keywords:
    - Flutter UPI SDK
    - Integrate Flutter UPI SDK
    - ' Flutter UPI SDK Integration'
    - Integrate Mobile Flutter UPI SDK
    - PayU Mobile Flutter UPI SDK
  robots: index
next:
  description: ''
---
This cluster aims to document all the knowledge base for UPI transactions. Implementation of most of the UPI flows is different when compared to normal transactions.

There are broadly two types of UPI transactions, Collect and Intent(Pure Intent/In-App). For collect transactions, PayU informs the payment gateway to trigger a transaction to the app linked to the provided VPA, which asks the user for approval.

For intent transactions, we delegate the transaction process to an external app like BHIM, Google Pay, etc, which lets users transfer money to a VPA specified by us. After that, we use the PG (related to the specified VPA) for verification. PayU has a pre-configured VPA (distinct on the PG-Merchant level) on which the app makes the user pay the amount. To integrate UPI SDK with React Native, see Integrate UPI SDK with Flutter.

> ❗️ Callout
>
> * To start transacting through Google Pay™, register your business on Google using the Google Onboarding form, In this registration process, you need to add the merchant VPAs created by PayU for you. In the case of multiple VPAs, all of them need to be registered with Google.
> * To enable Google Pay, contact your Point of Contact at Google. For any further queries or help with onboarding, send a mail to PayU Mobile Integration Team.

***

## Compatibility

### Android

* Min SDK Version: 21
* Compile SDK Version: 31+
* Kotlin 1.6.10

## iOS

* iOS version: 11

## Integration Steps

The Flutter UPI SDK integration involves the following steps:

1. [Integration Steps](https://docs.payu.in/docs/integration-steps-flutterupi)
2. [Test the Integration](https://docs.payu.in/docs/test-the-integration-flutterupi)
3. [Go-live Checklist](https://docs.payu.in/docs/go-live-checklist-flutterupi)
