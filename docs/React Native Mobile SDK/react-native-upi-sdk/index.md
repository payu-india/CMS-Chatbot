---
title: React Native UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native UPI SDK
  description: >-
    This document provides information on UPI transactions using React Native
    SDK, including the two types of transactions (Collect and Intent) and
    compatibility requirements for Android and iOS.
  keywords:
    - PayU India UPI SDK for React Native
    - PayU React Native UPI SDK
    - UPI SDK integration React Native
    - React Native UPI payment SDK
    - PayU UPI payment gateway
    - How to integrate PayU UPI SDK in React Native
    - PayU India UPI SDK for React Native apps
    - Guide to PayU UPI React Native SDK
    - PayU UPI payment gateway integration React Native
    - Step-by-step PayU UPI SDK React Native integration
  robots: index
next:
  description: ''
---
This cluster aims to document all the knowledge base for UPI transactions. Implementation of most of the UPI flows is different when compared to normal transactions.

There are broadly two types of UPI transactions, Collect and Intent(Pure Intent/In-App). For collect transactions, PayU informs the payment gateway to trigger a transaction to the app linked to the provided VPA, which asks the user for approval.

For intent transactions, we delegate the transaction process to an external app like BHIM, Google Pay, etc, which lets users transfer money to a VPA specified by us. After that, we use the PG (related to the specified VPA) for verification. PayU has a pre-configured VPA (distinct on the PG-Merchant level) on which the app makes the user pay the amount. To integrate UPI SDK with React Native, see Integrate UPI SDK with React Native.

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

The React Native UPI SDK integration involves the following steps:

1. [SDK Integration](https://docs.payu.in/docs/reactnative-upisdk-integration-steps)
2. [Test the Integration](https://docs.payu.in/docs/reactnative-upisdk-test-integration)
3. [Go-live Checklist](https://docs.payu.in/docs/reactnative-upisdk-golive-checklist)
