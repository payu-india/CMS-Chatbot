---
title: iOS Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: iOS Core SDK
  description: >-
    This document provides an overview of the Core SDK components and
    implementation, including two variants: Seamless Integration and
    Non-seamless Integration for iOS.
  keywords:
    - IOS Core SDK
    - PayU IOS SDK integration
    - Mobile payment integration with PayU IOS SDK
    - PayU IOS Core setup for Mobile
    - Core SDK for IOS
    - PayU Hosted Checkout SDK for Mobile
  robots: index
next:
  description: ''
---
This part of the documentation describes how to integrate PayU iOS Core SDK.

## When to Use Core SDK

* Use Core SDK when you need complete UI control
* Use Checkout Pro when you want a pre-built UI

### Quick Decision Matrix

| If you need...                       | Choose               |
| :----------------------------------- | :------------------- |
| Fastest time-to-market               | **Checkout Pro SDK** |
| Complete UI customization            | **Core SDK**         |
| Minimal developer effort             | **Checkout Pro SDK** |
| Brand-consistent checkout experience | **Core SDK**         |
| Pre-built, tested payment UI         | **Checkout Pro SDK** |
| Custom payment flow logic            | **Core SDK**         |

### Detailed Comparison

#### User Interface

| Feature                    | Checkout Pro SDK        | Core SDK                   |
| :------------------------- | :---------------------- | :------------------------- |
| **Payment screen**         | Ready-to-use PayU UI    | You design & build         |
| **Branding**               | Add logo, change colors | Full brand control         |
| **Layout**                 | Fixed PayU layout       | Custom layout              |
| **Payment method display** | Automatic, optimized    | You decide order & display |
| **Error messages**         | Pre-defined             | Custom messaging           |
| **Loading states**         | Built-in                | You implement              |

<br />

#### Supported Payment Methods

Both SDKs support the same payment methods:

#### &#x20;Integration Complexity

**Checkout Pro SDK**

```swift
// Complete payment in ~20 lines of code
let paymentParam = PayUPaymentParam(
    key: "merchantKey",
    transactionId: "TXN123",
    amount: "100.00",
    productInfo: "Product",
    firstName: "John",
    email: "john@email.com",
    phone: "9876543210",
    surl: "https://yoursite.com/success",
    furl: "https://yoursite.com/failure",
    environment: .test
)

// One line to show payment UI
PayUCheckoutPro.open(on: self, paymentParam: paymentParam, config: nil, delegate: self)

// SDK handles everything: UI, validation, bank pages, response
```

**Core SDK**

```swift
// You need to build:
// 1. Payment method selection UI
// 2. Card input form with validation
// 3. Bank selection dropdown
// 4. UPI ID input field
// 5. OTP handling UI
// 6. Loading states
// 7. Error handling UI
// 8. Success/failure screens

// Then use SDK to create payment request
let paymentParams = PayUModelPaymentParams()
// ... configure all parameters ...

let createRequest = PayUCreateRequest()
createRequest.createRequestWithCardForMerchant(
    withDetails: paymentParams,
    cardNumber: userEnteredCardNumber,  // From your UI
    cvv: userEnteredCVV,                // From your UI
    expiryYear: userSelectedYear,       // From your UI
    expiryMonth: userSelectedMonth,     // From your UI
    nameOnCard: userEnteredName,        // From your UI
    storeCardToken: 0,
    withCompletionBlock: { (request, postParam, error) in
        // Load in WebView/Custom Browser
        // Handle response
        // Show result in your UI
    }
)
```

##### Features Comparison

| Feature                            | Checkout Pro SDK |         Core SDK        |
| :--------------------------------- | :--------------: | :---------------------: |
| **Offers/Discounts display**       |    ✅ Automatic   |     🔧 You implement    |
| **EMI calculator**                 |    ✅ Built-in    |  🔧 Use API + build UI  |
| **Card BIN validation**            |    ✅ Automatic   |  🔧 Use API + build UI  |
| **Saved cards display**            |    ✅ Automatic   |     🔧 You implement    |
| **Payment recommendations**        |   ✅ AI-powered   |     ❌ Not available     |
| **Convenience fee display**        |    ✅ Automatic   | 🔧 You calculate & show |
| **OTP auto-read**                  |    ✅ Built-in    | 🔧 Integrate separately |
| **3D Secure handling**             |    ✅ Automatic   |  🔧 Use Custom Browser  |
| **Split payments**                 |    ✅ Supported   |       ✅ Supported       |
| **Recurring payments**             |    ✅ Supported   |       ✅ Supported       |
| **TPV (Third-party verification)** |    ✅ Supported   |       ✅ Supported       |

***

#### Customization Capabilities

**Checkout Pro SDK Customization**

| What You Can Customize        | How                        |
| :---------------------------- | :------------------------- |
| Primary color                 | `config.primaryColor`      |
| Secondary color               | `config.secondaryColor`    |
| Merchant logo                 | `config.merchantLogo`      |
| Payment modes order           | `config.paymentModesOrder` |
| Hide specific payment modes   | `config.hidePaymentModes`  |
| Auto-select OTP               | `config.autoSelectOtp`     |
| Custom notes per payment mode | `config.customNotes`       |

```swift
let config = PayUCheckoutProConfig()
config.primaryColor = UIColor(hex: "#FF6B00")
config.merchantLogo = UIImage(named: "your_logo")
config.paymentModesOrder = [.upi, .cards, .netBanking, .emi]
```

**Core SDK Customization**

**Everything** — You build the entire UI from scratch.

## Requirements

* iOS 13.0+
* Xcode 26+
* Swift 5.0+ / Objective-C

## Next Steps

This part of document describes the Core SDK components and implementation:

* [Objective - Seamless Integration](doc:ios-coresdk-seamless-integration)
* [Web Services for iOS Core SDK](https://docs.payu.in/docs/ios-coresdk-web-services)
* [Setup Recurring Payments](https://docs.payu.in/docs/ios-coresdk-setup-recurring-payments)
* [Integrate TPV](https://docs.payu.in/docs/ios-coresdk-integrate-tpv)
* [Release on App Store](https://docs.payu.in/docs/ios-coresdk-distribute-your-ios-app)
* [Sample App](https://docs.payu.in/docs/ios-coresdk-sample-app)
