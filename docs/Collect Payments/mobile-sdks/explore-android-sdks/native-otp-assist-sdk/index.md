---
title: Android Native OTP Assist SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Android Native OTP Assist SDK
  description: >-
    The Android Native OTP Assist SDK for Android allows for capturing OTP
    in-app without redirection to the bank's page, improving checkout completion
    rates. It supports top banks and card schemes, with a growing list of
    supported institutions.
  keywords:
    - Android Native OTP Assist SDK
    - PayU Android SDK integration
    - Mobile payment integration with PayU Android SDK
    - PayU Android Native OTP Assist setup for Mobile
    - Native OTP Assist SDK for Android
    - PayU Hosted Checkout SDK for Mobile
    - ' Android CB SDK'
    - PayU Android SDK integration
    - PayU Android CB setup for Mobile
    - Native OTP Assist SDK for Android
  robots: index
next:
  description: ''
---
## Native OTP Assist – Android

The OTP Assist SDK provides a complete authentication flow for card transactions. It offers to capture OTP in your app without any redirection to the bank’s 3Dsecure/ACS page. This means that there’s one less point of failure in the checkout process and a faster completion rate for transactions. The OTP Assist SDK will auto-read and submit OTP on behalf of the user.

**Watch the video to quickly get started with Native OTP Assist Android SDK**

### Features

The Native OTP Assist SDK gives you the following key capabilities:

* Read OTP on your app without redirecting to the bank page, for eligible bins.
* If the bin is not eligible, then it will redirect to the bank’s 3d-secure/ACS page.
* Support for Android native SMS permission, as well as Google Consent API.

<Image align="center" width="350px" src="https://files.readme.io/a108e0f-otp-Assist.gif" />

## Supported Banks

Native OTP flow is supported for most debit and credit cards issued by top banks. The list keeps growing and we recommend connecting with your account manager to have the new flows activated for your account.

| Bank Name               | Card Scheme                 |
| :---------------------- | :-------------------------- |
| State Bank of India     | Visa, Master, Rupay         |
| HDFC Bank               | Visa, Master, Rupay, Diners |
| ICICI Bank              | Visa, Master                |
| Axis Bank               | Visa, Master                |
| Kotak Bank              | Visa, Master                |
| Citibank                | Visa, Master                |
| Standard Chartered Bank | Visa, Master                |

> 🚧 Watch Out
>
> * The SDK runs a BIN check before proceeding with the Native OTP experience. You may run BIN check independently if you wish. Reach out to our support team to get started using “[mobile.integration@payu.in](mailto:mobile.integration@payu.in)“.\
>   There are few bins that are not eligible for native OTP flow even the Bank and card scheme are eligible.
> * Bank downtime will affect the performance of this flow.

## Compatibility

* Min SDK Version: 21
* Compile SDK Version: 31 or later
