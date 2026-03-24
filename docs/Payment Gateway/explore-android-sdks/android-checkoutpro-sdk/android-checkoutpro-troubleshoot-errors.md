---
title: Troubleshooting CheckoutPro SDK
excerpt: >-
  Troubleshoot the errors that you may encounter during the integration
  lifecylce with Android checkoutpro SDK
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
1. `'verify your server' OR Something went wrong, please verify with your server.`

**Solution**: In PayUCheckotPro SDK, Native OTP feature is not supported in UAT. Please comment the below line of code from `build.gradle` file.

```Text build.gradle
implementation 'in.payu:native-otp-assist:1.3.9'
```

<Callout icon="📘" theme="info">
  **Info**: After you moved in Production environment, remove the commenting for above code from `build.gradle` file.
</Callout>

***

2. `Value &lt;!DOCTYPE of type java.lang.String cannot be converted to JSONObject`

**Solution**: This error occurs when you take the payment integration live without setting the value of the `setIsProduction` parameter to `true`. Check the integration code to make the necessary changes and try again.

***

## PhonePe

**Error**: `“Oops Something went Wrong”`

**Solution**: `txn-s2s_flow` flag is not enabled on your MID. Send an email to enable this flag on [mobile.integration@payu.in](mailto:mobile.integration@payu.in).

***

## GooglePay

Error: `"Something Went Wrong"`

**Solution**: Please check if the merchant VPAs are whitelisted at Google end for this merchant. Otherwise, you need to fill out the onboarding form and submit it to Google Console. Post that Google will whitelist the VPAs and then GPay in-app will start working. Use the following link for the onboarding form. [https://pay.google.com/business/console/](https://pay.google.com/business/console/)

***

## UPI

**Error**: `"Some Problem Occurred Issue"`

**Soultion**: This happens when incorrect parameters are passed in the payment request. Please check the parameter that you have sent.

**Error**: `"MERCHANT_INFO_NOT_PRESENT"`

**Solution**: `txn-s2s_flow` flag is not enabled on your MID. Contact [PayU Support](https://help.payu.in/query) to enable the `txn-s2s_flow` flag.

## How to fix the build error after adding PayUCheckoutPro SDK gradle dependency?

After adding PayUCheckoutPro SDK gradle dependency, if the below build error is received

Add the below code in the `<application>` tag of your App's AndroidManifest.xml file

```
tools:replace="android:theme"
```
