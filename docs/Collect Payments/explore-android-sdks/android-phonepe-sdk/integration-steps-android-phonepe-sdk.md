---
title: Integration Steps
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Android PhonePe SDK Integration Steps
  description: >-
    The Android PhonePe SDK integration involves following specific steps,
    testing the integration, and completing a go-live checklist, with guidance
    on generating a static hash for the process.
  keywords:
    - Android PhonePe SDK Integration Steps
    - ' Steps to Integrate Android PhonePe SDK'
    - ' Android PhonePe SDK Integration Steps'
  robots: index
---

---
title: Integration Steps
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Android PhonePe SDK Integration Steps
  description: >-
    Integrate PhonePe in-app payments on Android with PayU: SDK dependency, intent flow, hash, callbacks, and sandbox testing.
  robots: index
  keywords:
    - phonepe sdk android integration payu payment gateway
    - payu phonepe android in app payment integration steps
    - integrate phonepe android app native sdk payu india
    - android wallet payment sdk phonepe integration guide payu
    - google pay phonepe in app payment sdk android payu
    - mobile payment sdk android phonepe intent flow payu
    - payment gateway android phonepe sdk integration steps
    - payu android phonepe sdk hash callback integration
    - android native phonepe payment integration developer payu
    - payu phonepe sdk test environment android integration
    - wallet sdk android india phonepe payu integration
    - android in app wallet payment phonepe payu gateway
---
The Android PhonePe SDK integration involves the following steps:

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

First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

### Step 2: Set up build.gradle

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

```gradle
implementation 'in.payu:phonepe-intent:1.8.9'
```

### Step 3: Create Callbacks Instance

PayUPhonePeCallback provides the following callback methods.

* onPaymentOptionFailure (String payuResponse, String merchantResponse): Calls when payment fails.
* onPaymentOptionSuccess (String payuResponse, String merchantResponse): Calls when payment succeeds.
* onPaymentOptionInitialisationFailure (int errorCode, String description): Called for PhonePe initialisation failure.
* onPaymentOptionInitialisationSuccess (boolean result): Callback when PhonePe is successfully initialised.

Following are error messages concerning PhonePe initialization failure.

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Error Code</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Error Code</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT_KEY_NOT_ REGISTER_FOR_PHONEPE</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant is not registered for PhonePe with PayU</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

Create an instance of PayUPhonePeCallback similar to the following code block:

```java Java
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

### Step 4: Set up for Test/Sandbox merchant

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

### Step 5: Check for PhonePe availability

SDK provides the checkForPaymentAvailability method to check if PhonePe payment is available or not on the device. This method must be executed before showing PhonePe as a checkout option.

```java JAVA
PhonePe.getInstance().checkForPaymentAvailability(Activity activity, PayUPhonePeCallback callback, String paymentOptionHash, String merchantKey, String user_credentials)
```

Where:

* PayUPhonePeCallback: the class to provide callbacks
* Activity : Activity
* paymentOptionHash: Payment Related Details hash
* merchantKey: PayU Merchant Key
* user_credentials: Provide user credentials or use “default”

> 📘 Generate PaymentOption Hash
>
> To generate `PaymentOption` Hash refer to  [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> * key=YOUR KEY
> * command="payment_related_details_for_mobile_sdk" // Api Commands
> * salt= YOUR SALT
> * var1= default // Pass `default` value in var1

### Step 6: Make Payment by PhonePe

After successful initialization of PhonePe by calling checkForPaymentAvailability method, call makePayment method to make payment.

```java Java
PhonePe.getInstance().makePayment(PayUPhonePeCallback callback, Activity activity, String postData,boolean isUserCacheEnabled, View customDialogView);
```

Where:

* **PayUPhonePeCallback**: the class to provide callbacks
* **Activity**: activity instance
* **postData**: PayU postdata
* **isUserCacheEnabled**: To Enable/Disable User Cache
* **customDialogView**: Provide your Custom Progress dialog view (Optional)

<Callout icon="📘" theme="info">
  **Generate Payment Hash**: To generate a payment hash refer to [Hash Generation](https://docs.payu.in/docs/hash-generation#payment-hash).

  **Formula** :-sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
</Callout>

#### Sample PostData

```
txnid=1524122818080&productinfo=product_info&user_credentials=default&key=*****&surl=**SUCCESS_URL**&furl=**FAILURE_URL&firstname=firstname&email=test@gmail.com&amount=10&udf1=udf1&udf2=udf2&udf3=udf3&udf4=udf4&udf5=udf5&pg=CASH&bankcode=PPINTENT&hash=***PAYMENT_HASH***
```

### Step 7: Verify the transaction using Webhooks

After you get the response from SDK, make sure to confirm it with the PayU server.

<Callout icon="🚧" theme="warn">
  **Remember**: It is recommended to implement the PayU Webhook or backend verify call from your backend. For more information, refer to [Webhooks](doc:webhooks-copy).
</Callout>

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended that the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend. For more information, refer to [Verify Payment API](ref:verify_payment_api).

#### Step 7.1: Create a PayU account

First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

#### Step 7.2: Set up build.gradle

<Accordion title="Set up build.gradle" icon="fa-code">
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

  ```gradle
  implementation 'in.payu:phonepe-intent:1.8.7'
  ```
</Accordion>

#### Step 7.3: Create Callbacks Instance

PayUPhonePeCallback provides the following callback methods.

* onPaymentOptionFailure (String payuResponse, String merchantResponse): Calls when payment fails.
* onPaymentOptionSuccess (String payuResponse, String merchantResponse): Calls when payment succeeds.
* onPaymentOptionInitialisationFailure (int errorCode, String description): Called for PhonePe initialisation failure.
* onPaymentOptionInitialisationSuccess (boolean result): Callback when PhonePe is successfully initialised.

Following are error messages concerning PhonePe initialization failure.

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Error Code</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Error Code</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>MERCHANT_KEY_NOT_ REGISTER_FOR_PHONEPE</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant is not registered for PhonePe with PayU</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

<Accordion title="Create PayUPhonePeCallback instance" icon="fa-code">
  Create an instance of PayUPhonePeCallback similar to the following code block:

  ```java Java
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
</Accordion>

#### Step 7.4: Set up for Test/Sandbox merchant

If you are using the SDK with a test merchant, provide the following metadata value to the manifest file:

<Accordion title="Manifest file" icon="fa-code">
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
</Accordion>

#### Step 7.5: Check for PhonePe availability

SDK provides the checkForPaymentAvailability method to check if PhonePe payment is available or not on the device. This method must be executed before showing PhonePe as a checkout option.

<Accordion title="checkForPaymentAvailability method" icon="fa-code">
  ```java
  PhonePe.getInstance().checkForPaymentAvailability(Activity activity, PayUPhonePeCallback callback, String paymentOptionHash, String merchantKey, String user_credentials)
  ```

  Where:

  * PayUPhonePeCallback: the class to provide callbacks
  * Activity : Activity
  * paymentOptionHash: Payment Related Details hash
  * merchantKey: PayU Merchant Key
  * user\_credentials: Provide user credentials or use “default”
</Accordion>

> 📘 Generate PaymentOption Hash
>
> To generate `PaymentOption` Hash refer to  [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> * key=YOUR KEY
> * command="payment_related_details_for_mobile_sdk" // Api Commands
> * salt= YOUR SALT
> * var1= default // Pass `default` value in var1

#### Step 7.6: Make Payment by PhonePe

After successful initialization of PhonePe by calling checkForPaymentAvailability method, call makePayment method to make payment.

<Accordion title="makePayment method" icon="fa-code">
  ```java
  PhonePe.getInstance().makePayment(PayUPhonePeCallback callback, Activity activity, String postData,boolean isUserCacheEnabled, View customDialogView);
  ```

  Where:

  * **PayUPhonePeCallback**: the class to provide callbacks
  * **Activity**: activity instance
  * **postData**: PayU postdata
  * **isUserCacheEnabled**: To Enable/Disable User Cache
  * **customDialogView**: Provide your Custom Progress dialog view (Optional)
</Accordion>

<Callout icon="📘" theme="info">
  **Generate Payment Hash**: To generate a payment hash refer to [Hash Generation](https://docs.payu.in/docs/hash-generation#payment-hash).

  **Formula** :-sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
</Callout>

Sample PostData

```
txnid=1524122818080&productinfo=product_info&user_credentials=default&key=*****&surl=**SUCCESS_URL**&furl=**FAILURE_URL&firstname=firstname&email=test@gmail.com&amount=10&udf1=udf1&udf2=udf2&udf3=udf3&udf4=udf4&udf5=udf5&pg=CASH&bankcode=PPINTENT&hash=***PAYMENT_HASH***
```

#### Step 7.7: Verify the transaction using Webhooks

After you get the response from SDK, make sure to confirm it with the PayU server.

<Callout icon="🚧" theme="warn">
  **Remember**: It is recommended to implement the PayU Webhook or backend verify call from your backend. For more information, refer to [Webhooks](doc:webhooks).
</Callout>

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended that the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend. For more information, refer to Verify the Transaction.

## Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

### Test UPI Intent/InApp flow

> ❗️ **Not available in Test mode**: The UPI in-app and UPI intent flow is not available in the Test mode.

## Go-live Checklist

Ensure these steps before you deploy the integration in a live environment.

### Collect Live Payments

After testing the integration, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

> 🚧 Watch Out!
>
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 4: Configure Webhook

PayU recommends you to configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).

During the integration, refer the [Generate Static Hash](doc:generate-static-hash-android-sdk-pro) for hash generation details.