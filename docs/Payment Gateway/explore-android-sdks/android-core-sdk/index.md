---
title: Android Core SDK
excerpt: >-
  Build a custom checkout experience for your Android app with the Android Core
  SDK.
deprecated: false
hidden: false
metadata:
  title: Android Core SDK
  description: >-
    The Core SDK allows integration of the PayU payment gateway into your own
    interface, offering more control over the payment process and access to
    additional APIs. PayU Core Android SDK version 3.0 is deprecated and users
    are advised to update their dependencies to the Maven central repository.
  keywords:
    - Android Core SDK
    - PayU Android SDK integration
    - Mobile payment integration with PayU Android SDK
    - PayU Android Core setup for Mobile
    - Core SDK for Android
  robots: index
next:
  description: ''
---
The Core SDK allows you to integrate the PayU payment gateway into your own payment interface. This gives you more control over the look and feel of the payment interface, as well as the ability to add custom features and functionality.

The Core SDK would help you to create post parameters hassle-free that can be posted to PayU over a WebView or PayU's custom browser. It also offers several value-added APIs like verify-payment, get-user-cards, get-offer-status, etc that helps you to use full capabilities of PayU's platform with minimal effort.

> ❗️ Deprecated
>
> PayU Core Android SDK version 3.0 is deprecated. PayU no longer supports Android SDK version 3.0.PayU has moved to Maven central repository, Update your existing dependency.

## Features

Supported payment options

* Credit Card/Debit Card/Stored Card(Use PayuConstants.CC)
* NetBanking (Use PayUConstants.NB)
* NEFT/RTGS(Use PayUConstants.NEFT_RTGS)
* EMI (Use PayUConstants.EMI)
* No Cost EMI (Use PayUConstants.EMI)
* Cash Cards/Wallets (Use PayUConstants.CASH)
* Intent (Use PayUConstants.UPI_INTENT)
* UPI (Use PayUConstants.UPI)
* Google Pay (Use PayUConstants.TEZ)
* PhonePe (Use PayUConstants.PHONEPE_INTENT)
* LazyPay (Use PayUConstants.LAZYPAY)
* TwidPay (Use PayUConstants.PAY_BY_REWARDS)
* Sodexo (Use PayUConstants.SODEXO)
* Offer

## Compatibility

* Min SDK Version: 21
* Compile SDK Version: 31 and above
* Kotlin version: 1.6.10

For the recommended integration workflow, refer to [Integration Steps](https://docs.payu.in/docs/integration-steps-android-core-sdk/). After you integrate with the above steps, you can use the APIs listed in the following to integrate web services or TPV integration:

* [Web Services for Core SDK](https://docs.payu.in/docs/web-services-for-android-core-sdk)
* [TPV with Android Core SDK](https://docs.payu.in/docs/android-coresdk-tpv-integration)
