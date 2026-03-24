---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps  - Android Google Pay SDK
  description: >-
    The document outlines the steps for integrating the Android Google Pay SDK,
    including integration, testing, and a go-live checklist, with a reference
    for generating a static hash.
  keywords:
    - Integration Steps  for Android Google Pay SDK
    - Android Google Pay SDK Integration Steps
  robots: index
next:
  description: ''
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

<Cards columns={3}>
  <Card title="1. SDK Integration" href="#sdk-integration">
    Set up build.gradle, create callbacks, and make payment using PhonePe

    <br />
  </Card>

  <Card title="2. Test the Integration" href="#test-the-integration">
    Test the integration before going live and start collecting payments

    <br />
  </Card>

  <Card title="3. Go-live Checklist" href="#go-live-checklist">
    Configure production settings, verify payment method, and webhooks
  </Card>

  <br />
</Cards>

## SDK Integration

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

### Step 2: Gradle dependency

Add the following dependency in the application’s build.gradle.

```
implementation 'in.payu:payu-gpay:4.0.1'
```

### Step 3: Create Callbacks Instance

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

<Accordion title="Create an instance of `PayUGPayCallback" icon="fa-code">
  ```java Java
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
</Accordion>

## Step 4: Set up for Test/Sandbox Merchant

If you are using the SDK with a test merchant, provide this metadata value to the manifest file:

<Accordion title="Manifest File" icon="fa-code">
  ```xml XML
  <application>
    <meta-data
      android:name="payu_web_service_url"
      android:value="https://test.payu.in" />
    <meta-data
      android:name="payu_post_url"
      android:value="https://test.payu.in" />
  </application>
  ```
</Accordion>

### Step 5: Check Payment Availability

Call the checkForPaymentAvailability method available in Google Pay to check if Google Pay payment is available or not on the device. The checkForPaymentAvailability method is called before showing Google Pay as a checkout option.

<Accordion title="Call checkForPaymentAvailability method" icon="fa-code">
  ```java
  GPay.getInstance().checkForPaymentAvailability(Activity activity, PayUGPayCallback callback, String paymentOptionHash, String merchantKey, String user_credentials)
  ```

  Where

  * PayUGPayCallback : the class to provide callbacks
  * Activity : Activity
  * paymentOptionHash : Payment Related Details hash (payment\_related\_details\_for\_mobile\_sdk)
  * merchantKey : PayU Merchant Key
  * user\_credentials : Provide user credentials or use "default"
</Accordion>

> 📘 Generate PaymentOption Hash
>
> To generate PaymentOption Hash, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> * key= "Your Key"
> * command= \<"payment_related_details_for_mobile_sdk"> // Pass Command Name
> * salt= "Your SALT"
> * var1= \<"default"> // Pass the "default" value in var1

### Step 6: Make Payment by Google Pay

After the successful initialization of Google Pay using the checkForPaymentAvailability method, call the makePayment method to make a payment.

```java
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

### Step 7: Verify the transaction using Webhooks

After you get the response from SDK, make sure to confirm it with the PayU server.

<Callout icon="🚧" theme="warn">
  **Remember**: It is recommended to implement the PayU Webhook or backend verify call from your backend.
</Callout>

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended that the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend.

## Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

### Test UPI Intent/InApp flow

> ❗️ Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

## Go-live Checklist

Ensure these steps before you deploy the integration in a live environment.

### Collect live payments

After testing the integration end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

> 🚧 **Generate Production Key and Salt**: Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 4: Configure Webhook

We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).

During the integration, refer the [Generate Static Hash](doc:generate-static-hash-android-sdk-pro) for hash generation details.
