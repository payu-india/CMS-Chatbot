---
title: 1. SDK Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: SDK Integration Steps for Android Customer Browser
  description: >-
    This document provides a step-by-step guide on integrating PayU Android
    Custom Browser SDK to enable payment methods into your application,
    including creating a PayU account, setting up build.gradle, checking for
    payment availability, and invoking the CustomBrowser. It also includes
    sample post requests for card and net banking payments.
  keywords:
    - SDK Integration Steps - Android Customer Browser
    - Android Custom Browser SDK Integration Steps
    - PayU Android Custom Browser SDK integration steps
    - Mobile payment integration with PayU Android Custom Browser SDK steps
    - PayU Android Custom Browser set up for Mobile
    - Androi SDK integration stepsAndroid CB SDK Integration Steps
    - PayU Android CB SDK integration steps
    - Mobile payment integration with PayU Android CBSDK steps
    - PayU Android CB set up for Mobile
    - SDK Integration Steps - Android Customer Browser
    - Android Customer Browser SDK Integration
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: android-custombrowser-custombrowser-callback
      title: CustomBrowser Callback
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. PayU enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you. For more information, refer to [Configure Checkout Payment Methods](doc:checkout-payment-modes).

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

## Step 2: Set Up build.gradle

Add the following dependency in your application’s build.gradle:

```
implementation 'in.payu:payu-custom-browser:7.15.1'
```

> 🚧 Watch Out!
> 
> If you are getting the following error: `Default interface methods are only supported starting with Android N (--min-api 24): Landroidx/lifecycle/DefaultLifecycleObserver;onCreate(Landroidx/lifecycle/LifecycleOwner;)V`
> 
> Add the following compileOptions on your app's build.gradle:
> 
> ```
> android {
>  compileOptions {
>         sourceCompatibility 1.8
>         targetCompatibility 1.8
>     }
>     }
> ```

From version 7.4.0 onwards, it is mandatory to import UPI SDK dependency if you want to make payments through any of the following UPI options along with the changes mentioned in the Third-Party Payments Support section.

- UPI Intent
- Collect
- Google Pay
- PhonePe

```
<uses-permission android:name="android.permission.RECEIVE_SMS" />
```

> 👉 Tip
> 
> Merchants are advised to add this permission in the application’s `AndroidManifest.xml` to support OTP assist. In case your application supports a minimum SDK of less than 20, do these changes in your surl/furl.

## Step 3: Check for Payment Availability

The `CheckForPaymentAvailability` function in CustomBrowser class. Checks for payment option type availability:

```Text Input

      Activity : activity instance
      PaymentOption : Payment Option type e.g.PaymentOption.SAMSUNGPAY,PaymentOption.PHONEPE
      PayUCustomBrowserCallback : this class provide callbacks 
      paymentOptionHash : Payment Related Details Hash
      merchantKey : PayU Merchant Key
      user_credentials : User credentials or use "default"
```

> 📘 Generate PaymentOption Hash
> 
> To generate PaymentOption Hash refer to Hash Generation.
> 
> Formula :-sha512(key|command|var1|salt)
> 
> where
> 
> key= Provide your merchant key here  
> command= "payment_related_details_for_mobile_sdk" // Api Commands  
> salt=  Provide your merchant salt here  
> var1= Provide user credentials or use "default"
> 
> For more information, refer to  [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

**Sample**

```Text Java
new CustomBrowser().checkForPaymentAvailability(Activity activity, PaymentOption paymentOption, PayUCustomBrowserCallback payUCustomBrowserCallback, String paymentOptionHash, String merchantKey, String user_credentials)
```

## Step 2: Invoke CustomBrowser

To invoke CustomBrowser:

Create a basic object of CustomBrowserConfig similar to the following code snippet. For more information on configurations supported, refer to  [Android CustomBrowser Configurations](doc:android-custombrowser-configurations).

> 📘 Post URL can be any of the following:
> 
> Production - <https://secure.payu.in/_payment>  
> Staging - <https://test.payu.in/_payment>

```Text JAVA
CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey,txnId);
customBrowserConfig.setPayuPostData(<Post Data>);
customBrowserConfig.setPostUrl(<Post Url>);
```

1. Create an object of `PayUCustomBrowserCallback`.
2. Call method `addCustomBrowser()` similar to the following code snippet:

**Input:**

- `Activity`: activity instance.
- `CustomBrowserConfig`: configuration object of the custom browser.
- `PayUCustomBrowserCallback`: this class provides callbacks.

```Text JAVA
Input:
    Activity : activity instance
    CustomBrowserConfig : configuration object of the custom browser
    PayUCustomBrowserCallback : this class provide callbacks
```

**Sample** 

```Text Java
new CustomBrowser().addCustomBrowser( Activity activity, CustomBrowserConfig customBrowserConfig, PayUCustomBrowserCallback cbPayUCustomBrowserCallback)
```

## Sample Post Request

### Card

```
firstname=John&ccnum=5123456789012346&device_type=1&ccvv=123&ccexpyr=2025&key=gt****&email=snooze@payu.in
&bankcode=CC&txnid=1705055037779&amount=1.0&udf5=udf5&ccexpmon=05&surl=https://cbjs.payu.in/sdk/success
 &udf3=udf3&udf4=udf4&udf1=udf1&udf2=udf2&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"},{"platform":"android","name":"coresdk","version":"7.0.1"},
{"platform":"android","name":"pgsdk","version":"2.0.5"},{"platform":"android","name":"custombrowser","version":"7.11.14"}]
&phone=99999*****&pg=CC&furl=https://cbjs.payu.in/sdk/failure&productinfo=Macbook+Pro&ccname=PayuUser
&hash=a13d39d161c4377b4e81a97bc8b8bf06835628d208b379f3a15a4e352b88d1dc6fde878ff89e5c7d0eeb36f214d996313f4672432a92244c4950224a472c669b
```

### Net Banking

```
amount=1.0&firstname=John&udf5=udf5&device_type=1&surl=https://cbjs.payu.in/sdk/success&udf3=udf3&
udf4=udf4&udf1=udf1&udf2=udf2&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"},
{"platform":"android","name":"coresdk","version":"7.0.1"},{"platform":"android","name":"pgsdk","version":"2.0.5"},{"platform":"android","name":"custombrowser","version":"7.11.14"}]
&phone=99999*****&pg=NB&furl=https://cbjs.payu.in/sdk/failure&productinfo=Macbook+Pro&key=gt****&email=snooze@payu.in
&hash=84d0fe7da879adb22429f2f4c33334c31ed164d819356b5f8842d4c207560cc4251c76b4211a476ca029ffd5581b6f760afe97c35c635d2eaa75d379619e6145
&bankcode=SBIB&txnid=1705055218155
```

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "`pg` `**mandatory**`\t \t  \n\t ",
    "0-1": "`String` It defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page.  \nFor NetBanking, pg=NB.",
    "0-2": "TESTPG",
    "1-0": "`bankcode `**mandatory**\\`",
    "1-1": "`String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bank codes that can be used with the `bankcode` parameter, refer to [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes).  \nReference: For the test Net Banking credentials, refer to [Test Cards, UPI ID, and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).",
    "1-2": "TESTPGNB"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


For the supported payment method, refer to [Supported Payment Methods](doc:android-coresdk-supported-payment-method).