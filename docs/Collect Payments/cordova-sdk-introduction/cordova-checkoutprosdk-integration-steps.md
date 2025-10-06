---
title: Steps to Integrate
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Cordova Checkout Pro SDK Integration Steps
  description: >-
    This document provides instructions on including the PayUCheckoutPro Cordova
    plugin in your app project, setting up callbacks, building payment
    parameters, generating payment hashes, initiating payments, and customizing
    the integration for iOS. It also includes information on distributing your
    app on the App Store or Ad-hoc.
  keywords:
    - Cordova Checkout Pro SDK Integration Steps
    - PayU Cordova SDK integration steps
    - Mobile payment integration with PayU Cordova SDK steps
    - PayU Cordova Checkout Pro set up for Mobile
    - Cordova CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Cordova SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
The Cordova Checkout SDK integration involves the following steps:

<Callout icon="📘" theme="info">
  **Note**: You can do iOS specific customization during integration. For more information, refer to [iOS-specific Integration customization (Optional)](#ios-specific-integration-customization-optional).
</Callout>

<Accordion title="Step 1: Include the Cordova plugin in your app project" icon="fa-code">

The PayUCheckoutPro for Cordova plugin is offered through npm. To Include the Cordova Plugin in your app project:

1. Include the PayUCheckoutPro Cordova Plugin in Ionic Capacitor app by running the following commands that install the dependencies in the root folder of your app:

```
npm install cordova-payu-checkoutpro  
npx cap sync //Sync the plugin added above
```

For IOS deployment, run the command pod installs to Install the pod inside the following folders:

* ios/App folder in ionic
* platform/ios folder in Cordova.

> Note: Ensure that your minimum deployment target is iOS 11.

2. Include the CheckOutPro Cordova plugin in Cordova app by running the following commands that depend in the root folder of your app:

```
cordova plugin add cordova-payu-checkoutpro
cordova build 
```

</Accordion>
<Accordion title="Step 2: Set up Callback" icon="fa-code">

Include the following callbacks and methods in your Cordova app to receive callbacks from the CheckOutPro SDK:

```js
var responseCallBack = function (response) {
  // payment successful
  if ("generateHash" in response) {
    generateHash(response);
  } else if ("onPaymentSuccess" in response) {
    onPaymentSuccess(response);
  } else if ("onPaymentFailure" in response) {
    onPaymentFailure(response);
  } else if ("onPaymentCancel" in response) {
    onPaymentCancel(response);
  } else if ("onError" in response) {
    onError(response);
  }
};
//Handle Callback methods from SDK
function generateHash(response) {
  // Pass response param to your backend server
  // Backend will generate the hash which you need to pass to SDK
  // hashResponse: is the response which you get from your server
  var merchantSalt = `<Salt>`; //Keep Salt in the backend only.
  var resultValue = response.generateHash;
  var hashString = resultValue.hashString;
  var hashName = resultValue.hashName;
  var hash = {};
  hash[hashName] = sha512(hashString + merchantSalt);
  //Convert the hash data using sh512 and pass it to SDK.
  cordova.plugins.PayUCheckoutProCordova.hashGenerated(hash);
}

function onPaymentSuccess(response) {
  //Handle on Payment Success Response
}
function onPaymentFailure(response) {
  //Handle on Payment Failure Response
}

function onPaymentCancel(response) {
  //Handle on Payment Cancel Response
}

function onError(response) {
  //Handle on Error Response
}
```

</Accordion>
<Accordion title="Step 3: Build the payment parameters" icon="fa-code">

Your app needs to send transactional information to the CheckoutPro SDK to initiate a payment. Build the transactional information using the following code snippet:

```js
var payUPaymentParams = {
  key: `<key>`,
  transactionId: `<transaction id should be less than 25 character>`,
  amount: "1.0",
  productInfo: `<string>`,
  firstName: `<string>`,
  email: `<customer email>`,
  phone: `<customer phone>`,
  ios_surl: `<ios_surl>`,
  ios_furl: `<ios_furl>`,
  android_surl: `<android_surl>`,
  android_furl: `<android_furl>`,
  environment: `<environment>`, //"0" = Prooduction,  "1" = Staging
  userCredential: `<userCredential>`, //Optional
  additionalParam: `<additionalParam>`, //Optional
  enableNativeOTP: `<boolean>`, //true:false, //Optional
  userToken: "", //Optional
  payUSIParams: `<Standing Instructions>`, //Optional
  splitPaymentDetails: `<Split Payment>`, //Optional
};

var additionalParam = {
  udf1: "user defined value 1",
  udf2: "user defined value 2",
  udf3: "user defined value 3",
  udf4: "user defined value 4",
  udf5: "user defined value 5",
  merchantAccessKey: "", //This is for lookup API, optional
  sourceId: "", //Sodexo source ID, optional
};

var spitPaymentDetails = [
  {
    type: "absolute",
    splitInfo: {
      imAJ7I: {
        aggregatorSubTxnId: "Testchild123",
        aggregatorSubAmt: "5",
      },
      qOoYIv: {
        aggregatorSubTxnId: "Testchild098",
        aggregatorSubAmt: "5",
      },
    },
  },
];

var siParamObject = {
  isFreeTrial: `<bool>`,
  billingAmount: `<number>`, //Required
  billingInterval: `<number>`, //Required
  paymentStartDate: "yyyy-dd-mm", //Required
  paymentEndDate: "yyyy-dd-mm", //Required
  billingCycle: "once", //Required //Can be any of 'daily','weekly','yearly','adhoc','once','monthly'
  remarks: "Test SI transcaction",
  billingCurrency: "INR",
  billingLimit: "ON", //ON, BEFORE, AFTER
  billingRule: "MAX", //MAX, EXACT
};
```

<Callout icon="📘" theme="info">
  **Note**: For more details on Standing Instructions parameters, refer to [PayU Standing Instructions Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).
</Callout>

</Accordion>
<Accordion title="Step 4: Set up payment hashes" icon="fa-code">

This step describes how to pass the dynamic hashes. For detailed information, refer to [Generate Hash](doc:generate-dynamic-hash-cordova).

The SDK will send the hash string without salt in `responseCallBacktoopenCheckoutScreen`. Use the generate hash key to get the HashMap `<HashName, HashString>` in the callback response. Pass that hashMap to the server to generate the hash. Get the Hash from the server and pass it to SDK using the `cordova.plugins.PayUCheckoutProCordova.hashGenerated`(`<HashName hash>`)

```js
var responseCallBack = function (response) {
  if ("generateHash" in response) {
    generateHash(response);
  }
  "generateHash";
  ...................
};

function generateHash(response) {
  var merchantSalt = `<salt>`; //keep this in the backend.
  var resultValue = response.generateHash;
  var hashStringWithoutSalt = resultValue.hashString;
  var hashName = resultValue.hashName;
  var hashType = resultValue.hashType;
  var postSalt = response[resultValue.postSalt];
  var hash = `<Get Hash Backend with < hashStringWithoutSalt, hashType , postSalt >`;
  //Convert the hash data using sh512.
  //Call Call hashGenerated with HashResponse< hashName, Hash> to pass the hash from server to SDK.
  cordova.plugins.PayUCheckoutProCordova.hashGenerated(hash);
}
```

<Callout icon="📘" theme="info">
  **Notes**:

  * You need the following type of hashes to be generated at your backend: v1 Hash, v2 Hashes, MCP Lookup, and Post Salt Hash.
  * You must generate the hashes on your server. Do not generate the hashes locally in your app, as it may compromise the security of the transactions.
</Callout>

The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) for CheckoutPro SDK.

</Accordion>
<Accordion title="Step 5: Initiate the payment" icon="fa-code">

Initialize and launch the Checkout Pro SDK by calling the following code snippet:

```js
let payuParams = {
  payUPaymentParams: `<PayUPaymentParams>`,
  payUCheckoutProConfig: `<PayUCheckoutProConfig>`,
};
cordova.plugins.PayUCheckoutProCordova.openCheckoutScreen(
  callbackResponse,
  payuParams
);
```

</Accordion>
<Accordion title="Step 6: Update AndroidManifest.xml" icon="fa-code">

To automatically fill OTP on bank pages, SDK requires `the RECEIVE_SMS` permission. Add the following code snippet to your `AndroidManifest.xml` like below.

```xml
<uses-permission android:name="android.permission.RECEIVE_SMS" />
```

</Accordion>
<Accordion title="iOS-specific Integration customization (Optional)" icon="fa-code">

* **UPI Intent**: Currently, PayU supports only PhonePe, Paytm, and GooglePay through Intent. Add the following query schemes in the `info.plist`.

```xml
<key>LSApplicationQueriesSchemes</key>
<array>
  <string>phonepe</string>
  <string>paytm</string>
  <string>tez</string>
</array>
```

* **Card Scanner, Camera Permission**:

```xml
<key>NSCameraUsageDescription</key>
<string>Please mention the description to give user info</string>
```

***

</Accordion>
## Step 6: Distributing your app (App Store / Ad-hoc)

What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayUChekoutPro, refer to [Releasing Apple App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).