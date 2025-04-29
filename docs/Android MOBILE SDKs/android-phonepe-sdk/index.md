---
title: Android PhonePe SDK
excerpt: >-
  PhonePay SDK offers in app experience to start collecting payments through
  instruments saved on phone. Supports UPI, card and wallet payments along with
  UPI PIN authentication.
deprecated: false
hidden: false
metadata:
  title: Android PhonePe SDK
  description: >-
    This document outlines the features of PayU's integration with PhonePe,
    including support for UPI, card, and wallet payments, as well as in-app and
    web payment flows. It also specifies compatibility requirements such as
    minimum SDK version and Kotlin version.
  keywords:
    - PayU PhonePe SDK integration steps
    - PayU India PhonePe SDK for Android Integration Steps
    - Android PhonePe SDK integration Steps
    - PhonePe SDK integration steps
    - PayU PhonePe integration guide
    - >-
      How to integrate PayU PhonePe SDK in Android.Step-by-step PayU PhonePe SDK
      integration
    - PayU PhonePe SDK integration for Android apps
    - Detailed guide for PayU PhonePe SDK integration steps
    - PayU Phone Pe SDK integration steps
    - PayU India Phone Pe SDK steps
    - Android Phone Pe SDK integration
    - Phone Pe SDK integration steps
    - PayU Phone Pe integration guide
  robots: index
next:
  description: ''
---
## Features

* Supports  UPI, card, and wallet payment modes
* Opens as an in-app experience without any redirection
* UPI PIN authentication
* For Phonepe pay, no CVV rather an OTP with auto read/ submit is there
* Fallbacks to collect in case the app is not installed

## PayU offers two types of PhonePe flows:

* In-App Flow
* Web Flow

## In-App flow

Where the user device has the PhonePe application installed. We invoke the Installed PhonePe application to do the payment transaction. Users will see the Bottom-sheet (In-app) like the UI on the checkout screen of the following video:

<Image align="center" src="https://files.readme.io/82ae086-ezgif.com-resize_2.gif" />

## Web flow

If the user device doesn’t have the PhonePe application installed, we will show the Web checkout to make the payment, where the customer can make the payment by logging into the PhonePe and using the available payment methods.

## Compatibility

* Min SDK Version: 21
* Compile SDK Version: 31 and above
* Kotlin version: 1.6.10
