---
title: 1. SDK Integration Steps - Android PhonePe SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Step 1: Create a PayU account

First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

## Step 2: Set up build.gradle

Add the following URL in the root project’s build.gradle:

```
allprojects {
  repositories {
    maven {
    url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android"
    }
  }
}
```

Add the following dependency in your application’s build.gradle:

```Text build.gradle
implementation 'in.payu:phonepe-intent:1.8.4'
```

## Step 3: Create Callbacks Instance

PayUPhonePeCallback provides the following callback methods.

* onPaymentOptionFailure (String payuResponse, String merchantResponse): Calls when payment fails.
* onPaymentOptionSuccess (String payuResponse, String merchantResponse): Calls when payment succeeds.
* onPaymentOptionInitialisationFailure (int errorCode, String description): Called for PhonePe initialisation failure.
* onPaymentOptionInitialisationSuccess (boolean result): Callback when PhonePe is successfully initialised.

Following are error messages concerning PhonePe initialization failure.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Error Code
      </th>

      <th>
        Error Code
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        MERCHANT\_KEY\_NOT\_
        REGISTER\_FOR\_PHONEPE
      </td>

      <td>
        Merchant is not registered for PhonePe with PayU
      </td>
    </tr>
  </tbody>
</Table>

Create an instance of PayUPhonePeCallback similar to the following code block:

```Text JAVA
PayUPhonePeCallback payUPhonePeCallback = new PayUPhonePeCallback() {
@Override
public void onPaymentOptionFailure(String payuResponse, String merchantResponse) {
//Called when Payment gets failed.
}
@Override
public void onPaymentOptionInitialisationSuccess(boolean result) {
super.onPaymentOptionInitialisationSuccess(result);
// Merchants are advised to show PhonePe option on their UI after this callback is called.
}
@Override
public void onPaymentOptionSuccess(String payuResponse, String merchantResponse) {
//Called when Payment gets successful.
}
@Override
public void onPaymentOptionInitialisationFailure (int errorCode, String description) {
//Callback thrown in case PhonePe initialisation fails.
}
};
```

## Step 4: Set up for Test/Sandbox merchant

If you are using the SDK with a test merchant, provide the following metadata value to the manifest file:

```
<application
  <meta-data
    android:name="payu_web_service_url"
    android:value="https://test.payu.in" />
  <meta-data
    android:name="payu_post_url"
    android:value="https://test.payu.in" />
</application>
```

## Step 5: Check for PhonePe availability

SDK provides the checkForPaymentAvailability method to check if PhonePe payment is available or not on the device. This method must be executed before showing PhonePe as a checkout option.

```Text JAVA
PhonePe.getInstance().checkForPaymentAvailability(Activity activity, PayUPhonePeCallback callback, String paymentOptionHash, String merchantKey, String user_credentials)
```

Where:

* PayUPhonePeCallback: the class to provide callbacks
* Activity : Activity
* paymentOptionHash: Payment Related Details hash
* merchantKey: PayU Merchant Key
* user\_credentials: Provide user credentials or use “default”

> 📘 Generate PaymentOption Hash
>
> To generate `PaymentOption` Hash refer to  [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> * key=YOUR KEY
> * command="payment\_related\_details\_for\_mobile\_sdk" // Api Commands
> * salt= YOUR SALT
> * var1= default // Pass `default` value in var1

## Step 6: Make Payment by PhonePe

After successful initialization of PhonePe by calling checkForPaymentAvailability method, call makePayment method to make payment.

```Text JAVA
PhonePe.getInstance().makePayment(PayUPhonePeCallback callback, Activity activity, String postData,boolean isUserCacheEnabled, View customDialogView);
```

Where:

* **PayUPhonePeCallback**: the class to provide callbacks
* **Activity**: activity instance
* **postData**: PayU postdata
* **isUserCacheEnabled**: To Enable/Disable User Cache
* **customDialogView**: Provide your Custom Progress dialog view (Optional)

> 📘 Generate Payment Hash
>
> To generate a `Payment` Hash refer to [Hash Generation](https://docs.payu.in/docs/hash-generation#payment-hash).
>
> **Formula** :-sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)

### Sample PostData

```
txnid=1524122818080&productinfo=product_info&user_credentials=default&key=*****&surl=**SUCCESS_URL**&furl=**FAILURE_URL&firstname=firstname&email=test@gmail.com&amount=10&udf1=udf1&udf2=udf2&udf3=udf3&udf4=udf4&udf5=udf5&pg=CASH&bankcode=PPINTENT&hash=***PAYMENT_HASH***
```

## Step 7: Verify the transaction using Webhooks

After you get the response from SDK, make sure to confirm it with the PayU server.

> 🚧 Remember
>
> It is recommended to implement the PayU Webhook or backend verify call from your backend.

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended that the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend. For more information, refer to Verify the Transaction.