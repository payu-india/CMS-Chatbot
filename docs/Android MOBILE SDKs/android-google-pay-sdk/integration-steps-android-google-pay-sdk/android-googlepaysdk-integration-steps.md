---
title: 1. SDK Integration
excerpt: This section describes how to integrate with Google Pay SDK.
deprecated: false
hidden: false
metadata:
  title: Android Google Pay SDK Integration Steps
  description: >-
    This document provides a step-by-step guide on integrating Google Pay SDK
    with PayU, including creating a PayU account, adding dependencies, setting
    up callbacks, checking payment availability, making payments, and verifying
    transactions using webhooks.
  keywords:
    - PayU Google Pay SDK integration steps
    - PayU India Google Pay SDK for Android Integration Steps
    - Android Google Pay SDK integration Steps
    - Google Pay SDK integration steps
    - PayU Google Pay integration guide
    - >-
      How to integrate PayU Google Pay SDK in Android.Step-by-step PayU Google
      Pay SDK integration
    - PayU Google Pay SDK integration for Android apps
    - Detailed guide for PayU Google Pay SDK integration steps
    - PayU GPay SDK integration steps
    - PayU India GPay SDK steps
    - Android GPay SDK integration
    - GPay SDK integration steps
    - PayU GPay integration guide
  robots: index
next:
  description: ''
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Step 2: Gradle dependency

Add the following dependency in the application’s build.gradle.

```
implementation 'in.payu:payu-gpay:3.1.5'
```

## Step 3: Create Callbacks Instance

The following is of list callback functions provided by PayU Google Pay:

* `onPaymentFailure (String payuResponse, String merchantResponse)`: Calls when payment fails
* `onPaymentSuccess (String payuResponse, String merchantResponse)`: Calls when payment succeeds
* `onPaymentOptionInitialisationFailure (int errorCode, String description)`: Called for Google Pay `initialisationfailure `where:
  * `errorCode`: Error Code
  * `description`: Error Description
* `onPaymentInitialisationSuccess()`: Callback when Google Pay is successfully initialized.
* `onGpayErrorReceived(int errorCode, String description)`: Callback when found any error while making a payment transaction.

The following are error messages when the Google Pay Payment fail:

| Error Code | Error Message                                          | Description                                             |
| :--------- | :----------------------------------------------------- | :------------------------------------------------------ |
| 1          | Google Pay payment is not enabled on this merchant key |                                                         |
| 2          | Please check the input data.                           | Input Data is missing to make payments with Google Pay. |
| 3          | Payment APIs Error                                     |                                                         |

Create an instance of `PayUGPayCallback` similar to the following code block:

```Text Java
PayUGPayCallback payUGPayCallback = new PayUGPayCallback() {
            @Override
            public void onPaymentSuccess(String payuResponse, String merchantResponse) {
                Log.d(TAG, "onPaymentSuccess: " + payuResponse + "-------------------" + merchantResponse);
            }

            @Override
            public void onPaymentFailure(String payuResponse, String merchantResponse) {
                Log.d(TAG, "onPaymentFailure: " + payuResponse + "-------------------" + merchantResponse);
            }

            @Override
            public void onPaymentInitialisationSuccess() {
                Log.d(TAG, "onPaymentInitialisationSuccess: ");
            }

            @Override
            public void onPaymentInitialisationFailure(int errorCode, String description) {
                Log.d(TAG, "onPaymentInitialisationFailure: " + errorCode + "---------------------" + description);
            }

            @Override
            public void onGpayErrorReceived(int errorCode, String description) {
                Log.d(TAG, "onGpayErrorReceived: " + errorCode + "---------------------" + description);
            }
        };
```

## Step 4: Set up for Test/Sandbox Merchant

If you are using the SDK with a test merchant, provide this metadata value to the manifest file:

```text XML
<application>
  <meta-data
    android:name="payu_web_service_url"
    android:value="https://test.payu.in" />
  <meta-data
    android:name="payu_post_url"
    android:value="https://test.payu.in" />
</application>
```

## Step 5: Check Payment Availability

Call the checkForPaymentAvailability method available in Google Pay to check if Google Pay payment is available or not on the device. The checkForPaymentAvailability method is called before showing Google Pay as a checkout option.

```Text JAVA
GPay.getInstance().checkForPaymentAvailability(Activity activity, PayUGPayCallback callback, String paymentOptionHash, String merchantKey, String user_credentials)
```

Where

* PayUGPayCallback : the class to provide callbacks
* Activity : Activity
* paymentOptionHash : Payment Related Details hash (payment\_related\_details\_for\_mobile\_sdk)
* merchantKey : PayU Merchant Key
* user\_credentials : Provide user credentials or use "default"

> 📘 Generate PaymentOption Hash
>
> To generate PaymentOption Hash, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> * key= "Your Key"
> * command= \<"payment\_related\_details\_for\_mobile\_sdk"> // Pass Command Name
> * salt= "Your SALT"
> * var1= \<"default"> // Pass the "default" value in var1

## Step 6: Make Payment by Google Pay

After the successful initialization of Google Pay using the checkForPaymentAvailability method, call the makePayment method to make a payment.

```Text JAVA
GPay.getInstance().makePayment(Activity activity, String postData, final PayUGPayCallback payUGPayCallback, String merchantKey, View loadingDialogView);
```

The PayUGPayCallback class provides the following callbacks:

* `Activity`: activity instance
* `postData`: PayU postdata
* `merchantKey`: Your Merchant Key
* `loadingDialogView`: ProgressDialog View

> 📘 Generate Payment Hash
>
> To generate a Payment Hash refer to [Hash Generation](https://docs.payu.in/docs/hash-generation#payment-hash).
>
> **Formula** :-sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)

### **Sample PostData**

```
txnid=1524122818080&productinfo=product_info&user_credentials=default&key=*****&surl=**SUCCESS_URL**&furl=**FAILURE_URL&firstname=firstname&email=test@gmail.com&amount=10&udf1=udf1&udf2=udf2&udf3=udf3&udf4=udf4&udf5=udf5&pg=UPI&bankcode=TEZ&hash=***PAYMENT_HASH***
```

## Step 7: Verify the transaction using Webhooks

After you get the response from SDK, make sure to confirm it with the PayU server.

> 🚧 Remember
>
> It is recommended to implement the PayU Webhook or backend verify call from your backend.

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended that the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend.