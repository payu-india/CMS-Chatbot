---
title: iOS UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: iOS UPI SDK
  description: >-
    PayU's UPI SDK allows for easy integration of UPI payments in your app,
    supporting intent payments, UPI collect payments, and Google Pay fallback
    options. The SDK is API-based, quick, and does not involve a WebView in any
    payment flow.
  keywords:
    - PayU India UPI SDK
    - PayU UPI SDK
    - UPI SDK integration IOS
    - IOS UPI payment SDK
    - PayU UPI payment gateway
    - How to integrate PayU UPI SDK in IOS
    - PayU India UPI SDK for IOS apps
    - Guide to PayU UPI IOS SDK
    - PayU UPI payment gateway integration IOS
    - Step-by-step PayU UPI SDK IOS integration
  robots: index
next:
  description: ''
---
PayU’s UPI SDK is a framework for integrating UPI payments in your app in an easy, efficient, and stable way. The following types of payments are currently supported:

- Intent payments\* (Make UPI payments by transitioning users from your app to UPI app like Google Pay/PhonePe )

> **Note**: ‘intent’ as in Android, not in iOS. Using this word here due to its widespread understanding across domains.)

- UPI Collect Payments.
- Google Pay fallback options (If Google Pay is not installed on iOS device). It can use Google Pay registered mobile number instead of VPA for UPI collect payments.

## UPI SDK frameworks

PayU provides the following UPI modular SDKs that perform different functions related to UPI Payments:

- **PayU UPI Core SDK**: This contains all APIs, Error Codes, Response Handlers etc. With this SDK alone, you can make intent payments. If you want to make UPI Collect payments also, either you can use PayU UPI SDK (given below) to collect VPA from the user or pass Core SDK the required parameters. Core SDK contains only one UI Screen, the final loader page. On this screen, we fetch the payment response from PayU.UPI Core SDK internally uses sockets to fetch payment responses as quickly as possible.
- **PayU UPI SDK**: This contains the UI screen screens and related resources to support UPI collection payment in a hassle-free way. You might find it useful to save time in creating checkout screens for UPI Collect.

The following dependencies (automatically added if integrated via Cocoapods) are required:

- **PayU Networking**: This is used by CoreSDK to handle network requests.

## Unique features of UPI SDK

There is no WebView involved in any payment flow. Every payment flow is completely API based and super quick.  
Make intent Payments on iOS just like Android. The PSP app (PhonePe/Google Pay etc.) does not automatically switches the user to your app. User manually comes back to your app)  
Hassle-free integration

## Integration Steps

The iOS Native OTP Assist SDK integration involves the following steps:

1. [SDK Integration](https://docs.payu.in/docs/ios-upisdk-integration-steps)
2. [Test the Integration](https://docs.payu.in/docs/ios-upisdk-test-integration)
3. [Go-live Checklist](https://docs.payu.in/docs/ios-upisdk-go-live-checklist)

During the integration, refer the [Generate Static Hash](doc:generate-static-hash-ios) for hash generation details.