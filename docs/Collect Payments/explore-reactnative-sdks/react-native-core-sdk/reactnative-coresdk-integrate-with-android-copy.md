---
title: Integrate with iOS
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate React Native Core SDK for iOS
  description: >-
    This document provides a step-by-step guide on how to install and use the
    PayU Core PG SDK for React Native, including generating payment hashes,
    building payment parameters, making payments, registering listeners, and
    checking responses from the Custom Browser SDK.
  keywords:
    - React Native Core SDK Integration for IOS
    - PayU React Native Core SDK integration for IOS
    - Mobile payment integration with PayU React Native Core SDK for IOS
    - PayU React Native  Core SDK with IOS for Mobile
  robots: index
next:
  description: ''
---
The React Native Core SDK integration with iOS involves the following steps:

1. [Installation](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-1-installation)
2. [Generate payment hash](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-2-generate-payment-hash)
3. [Build the Payment Parameters](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-3-build-the-payment-parameters)
   * [Set Net Banking params for payment](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#set-net-banking-params-for-payment)
   * [Set Card payment parameters](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#set-card-payment-parameters)
   * [Set Wallet payment parameters](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#set-wallet-payment-parameters)
4. [Make Payment](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-4-make-payment)
5. [Register Listeners](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-5-register-listeners)
6. [Check the Response](https://docs.payu.in/docs/reactnative-coresdk-integrate-with-android-copy#step-6-check-the-response)

## Step 1: Installation

React Native SDK for PayU’s Core PG is offered through Node Package Manager (NPM). Run the following command to install PayU Core PG SDK for React:

```
npm i payu-core-pg-react 
```

### Setup Command

```
git clone https://github.com/payu-intrepos/payu-core-pg-react.git payuSdkExample
  cd payuSdkExample
  npm i
  cd example
  npm i
  react-native start
  react-native run-android
```

***

## Step 2: Generate payment hash

Generate the payment hash and pass the hash in the JSON payUPaymentParams.hashes.payment parameter as shown below:

```javascript React.js
{
  payUPaymentParams: {
    hashes:{
      payment: <String>, // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
    }
  }
}
```

To learn more about sash generation, see Hash Generation.

> 📘 Remember
>
> Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.

***

## Step 3: Build the payment parameters

To initiate a payment, your app needs to send Transactional Information to the Custom Browser SDK. Build the payUPaymentParams object with the mandatory parameters as shown in the following code snippet:

```javascript React.js
 var payUPaymentParams = {
      payUPaymentParams: {
        key: <String>, //merchant key 
        transaction_id: new Date().getTime().toString(),
        amount: <String>, // amount in Double format
        product_info: <String>,
        first_name: <String>,
        email: <String>,
        phone: <phoneNumber>,
        ios_surl: <String>,
        ios_furl: <String>,
        android_surl: <String>,
        android_furl: <String>,
        environment: <String>, // "1" for Stage, "0" for production
        user_credentials: <String>, // "user:password"
        hashes: {
          payment: <String>, // generated hash for payment
          },
        additional_param:{
          udf1: "user defined value 1",
          udf2: "user defined value 2",
          udf3: "user defined value 3",
          udf4: "user defined value 4",
          udf5: "user defined value 5",
         merchantAccessKey:"", //This is for lookup API, optional
         sourceId:"", //Sodexo source ID, optional 
      },
    }
  }
}
```

Build parameters for different payment methods:

### Set Net Banking params for payment

To build the mandatory parameters to integrate Net Banking as a payment Method in JSON, use the following code snippet:

```javascript React.js
var params={
  payUPaymentParams: {
        bankcode:<String>, // ex: ICIB,AXIB 
  }
```

### Set Card payment parameters

To build the mandatory parameters to integrate Cards as a payment Method in JSON, use the following code snippet:

```javascript React.js
var params={
  payUPaymentParams: {
        bankcode:"CC", 
        card_number:<String>,
        cvv: <String>,
        expiry_year: <String>,
        expiry_month: <String>,
        name_on_card: <String>,
        shouldSaveCard: <boolean>, //(true | false)
        user_credentials: <String>, // "user:password"
  }
```

### Set Wallet payment parameters

To build the mandatory parameters to integrate wallets as a payment Method in JSON, use the following code snippet:

```javascript React.js
var params={
  payUPaymentParams: {
        bankcode: <String>, // Payu provide Wallet Id (ex: AMON) 
  }
```

***

## Step 4: Make payment

Use the following code snippet to start a payment:

```javascript React.js
CBWrapper.startPayment(
params,
Payment Mode <String> , // CC(CARD), CASH(WALLET), NB (NET BANKING)
      (error) => {
        console.log("-----------Error Callback---------");
        console.log(error);
        console.log("------------------------------------");
      },
      (payuResponse) => {
       
        console.log("-----------Success Callback---------");
        console.log(payuResponse);
        console.log("--------------------------------------");
      }
  );
```

***

## Step 5: Register listeners

Register event listener (DeviceEventEmitter for this SDK)to capture the response of the transaction from Custom Browser SDK. Use the following code snippet to register the listener:

```javascript React.js
DeviceEventEmitter.addListener("CBListener",(event)=>{
     
})
```

***

## Step 6: Check the response

This is what a sample response from the Custom Browser SDK looks like:

```javascript React.js
{
  "eveneType": <String>, (onPaymentFailure | onPaymentTerminate | onPaymentTerminate | onCBErrorReceived | onBackButton | onBackApprove | onBackDismiss)
  "payuResult": <String>, //conditional
  "merchantResponse": <String>, //conditional
  "errorMessage":<String>,
  errorCode: <String>, //conditional
}
```

<br />

## Testing and Go-live

### Test the integration

<Accordion title="Step 1: Installation" icon="fa-code">
  After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

  You can make test payments using one of the payment methods configured at the Checkout.

  <UPIIntentCallout />

  <TestingChecklist />

  ***

  <TestCardsCallout />

  <Accordion title="Test credentials for supported payment methods" icon="fa-code">
    Following are the payment methods supported in PayU Test mode.

    <Accordion title="Test credentials for Net Banking" icon="fa-code">
      Use the following credentials to test the Net Banking integration:

      * **user name:** payu
      * **password**: payu
      * **OTP**: 123456
    </Accordion>

    <Accordion title="Test VPA for UPI" icon="fa-code">
      > ❗️ Callout
      >
      > The UPI in-app and UPI intent flow is not available in the Test mode.

      You can use either of the following VPAs to test your UPI-related integration:

      * [anything@upi](anything@upi)
      * [9999999999@upi](mailto:9999999999@upi)

      For Testing the UPI Collect flow, Please follow the below steps:-

      1. Once you enter the VPA click on the verify button and proceed to pay.
      2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
      3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

      [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/) `<Txn_id>`

      #### For Android

      You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

      > 🚧 Ensure to remove the code from the manifest file before going live.

      ```xml
      <application>
      <meta-data android:name="payu_debug_mode_enabled" android:value="true" /> <!-- set the value to false for production environment -->
      <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> <!-- Comment in case of Production -->
      <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> <!-- Comment in case of Production -->
      </application>
      ```
    </Accordion>

    <Accordion title="Test cards for EMI" icon="fa-code">
      You can use the following Debit and Credit cards to test EMI integration.

      <EMITestCards />

      <br />
    </Accordion>

    <Accordion title="Test wallets" icon="fa-code">
      You can use the following wallets and their corresponding credentials to test wallet integration.

      <EMITestWallets />
    </Accordion>
  </Accordion>
</Accordion>

<Go_Live_Checklist />
