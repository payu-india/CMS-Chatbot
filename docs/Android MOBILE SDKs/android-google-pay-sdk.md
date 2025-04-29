---
title: Android Google Pay SDK
excerpt: >-
  Gpay SDK offers in app experience to start collecting payments through
  instruments saved on gpay and phone. Supports UPI, card and wallet payments
  along with UPI PIN authentication.
deprecated: false
hidden: false
metadata:
  title: Android Google Pay SDK
  description: >-
    This document outlines the features of PayU's integration with Google Pay or
    GPay, including support for UPI, card, and wallet payments, as well as
    onboarding requirements and different transaction flows. It also specifies
    compatibility requirements such as minimum SDK version and Kotlin version.
  keywords:
    - PayU Google Pay SDK integration
    - PayU India Google Pay SDK
    - Android Google Pay SDK integration
    - Google Pay SDK integration steps
    - PayU Google Pay integration guide
    - >-
      How to integrate PayU Google Pay SDK in Android.Step-by-step PayU Google
      Pay SDK integration
    - PayU Google Pay SDK integration for Android apps
    - Detailed guide for PayU Google Pay SDK integration
    - PayU GPay SDK integration
    - PayU India GPay SDK
    - Android GPay SDK integration
    - GPay SDK integration steps
    - PayU GPay integration guide
  robots: index
next:
  description: ''
---
## Feature

* Supports  UPI, card and wallet payment modes
* Opens as an in app experience without any redirection
* UPI PIN authentication
* For Google pay, no CVV rather an OTP with auto read/ submit is there.
* Fallbacks to collect in case app is not installed

### Onboarding Requirements

To start transacting through Google Pay™, register your business on Google using the Google Onboarding form, In this registration process, you need to add the merchant VPAs created by PayU for you. In the case of multiple VPAs, all of them need to be registered with Google.\
To enable Google Pay, contact your Point of Contact at Google.\
For any further queries or help with onboarding, send a mail to PayU Mobile Integration Team.

### Offerings

PayU supports three types of Google Pay transactions:

### Tokenized Cards Flow

In the latest Google Pay app version, users can opt to save their cards to make payments. These tokenized cards can be used to pay on merchant apps whitelisted by Google only.\
Within the merchant app, selecting Google Pay invokes the in-app bottom sheet shown below with the list of saved cards and UPI options. Users can select a saved card from the list and complete OTP authentication within the fragment itself.

> 📘 Note
>
> The OTP auto-read and submit handled by Google Pay Fragment

To enable the tokenized card flow, contact your Key Account Manager at PayU.

<Image align="center" src="https://files.readme.io/c6b8fd8-imgonline-com-ua-twotoone-UvibC88neamhvn.jpg" />

## In-App UPI Flow

If the user wishes to proceed with UPI Payment, the VPA can be selected from the Google Pay fragment. The user will have to authorize the payment with UPI PIN in the Google Pay app.

If the Google Pay app version that is installed doesn’t support this experience on the device, payment will be made through Intent flow. In the Intent flow, the Google Pay app is opened in full screen.

<Image align="center" src="https://files.readme.io/bfa7f5e-ezgif.com-resize.gif" />

## Web Flow

If the user’s device does not have the Google Pay application installed, PayU shows the Web UI to enter the VPA. This triggers a collect request to the user’s Google Pay application where he would need to authorize the transaction.

## Compatibility

* Min SDK Version: 21
* Compile SDK Version: 31 and above
* Kotlin version: 1.6.10
