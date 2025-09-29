---
title: Flutter Checkout Pro SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Flutter Checkout Pro SDK
  description: >-
    The CheckoutPro SDK offers a complete Mobile Checkout solution for Flutter
    Apps, allowing integration with PayU PG for fast payment acceptance with
    minimal effort. It supports various payment options, customization, and
    compatibility with iOS 11+ and Android SDK 21+.
  keywords:
    - Flutter Checkout Pro SDK
    - PayU Flutter SDK integration
    - Mobile payment integration with PayU Flutter SDK
    - PayU Flutter Checkout Pro setup for Mobile
    - Flutter CheckoutPro SDK
    - PayU Hosted Checkout SDK for Mobile
  robots: index
next:
  description: ''
---
The Checkout Pro SDK provides a complete Mobile Checkout solution for the Flutter App. The Checkout Pro experience allows you to integrate with the PayU PG with minimal integration effort and accept payments faster.

## Capabilities

* A complete, ready-to-use native Checkout GUI
* Support for multiple payment options:
* All major Credit/Debit card providers (Amex, Mastercard, Rupay, Visa, and more)
* Netbanking with 150+ Indian banks
* UPI Payments (Intent & Collect)
* Google Pay™ InApp & Cards
* Native OTP Assist
* Recurring Payments
* Convenience Fee support
* Offers support
* Multi-Currency Payments Support
* Prepaid Wallets
* CC & DC EMI Payments
* OTP read for faster and improved OTP authentication
* Enforce Payment Mode
* Customization capabilities to make the SDK your own

## Compatibility

### iOS

* Minimum iOS version: iOS 11
* Xcode version: Xcode 11.4 and above

### Android

* Min SDK Version: 21
* Compile SDK Version: 29+

## SDK Integration

To integrate PayU CheckoutPro with Flutter SDK:

* [Step 1: Include the SDK in your app project](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-1-include-the-sdk-in-your-app-project)
* [Step 2: Initialize PayU Checkout Pro Flutter object](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step2-initialize-payu-checkout-pro-flutter-object)
* [Step 3: Setup PayU Checkout Pro protocol](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step3-setup-payu-checkout-pro-protocol)
* [Step 4: Setup payment hashes](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step4-setup-payment-hashes)
* [Step 5: Build the Payment Parameters](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-5-build-the-payment-parameters)
* [Step 6: Initiate payment](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-6-initiate-payment)
* [Step 7: Configure AndroidManifest.xml](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-7-configure-androidmanifestxml)

For IOS, refer to iOS Specific Integration and check Distributing Your App (App Store/ Ad-hoc) to deploy your application. For more information, refer to [Explore iOS SDKs](doc:explore-ios-sdks)

### Step 1: Include the SDK in your app project

The CheckoutPro SDK for Flutter is offered through Flutter `pub.dev`

* To add the PayU Checkout Pro Flutter plugin add the following dependency in your app: `$ flutter pub add payu_checkoutpro_flutter`

```d Dart
import 'package:payu_checkoutpro_flutter/payu_checkoutpro_flutter.dart'; 
import 'package:payu_checkoutpro_flutter/PayUConstantKeys.dart'; 
 
```

* **For iOS**: Install the pod using the following command inside `ios` folder: `$ pod install`

***

### Step2: Initialize PayU Checkout Pro Flutter object

* Create PayUCheckout Pro Flutter instance.
  ```d Dart
  late PayUCheckoutProFlutter \_checkoutPro;
  ```

Initialize the PayUCheckoutProFlutter object using the current object.

```d Dart
@override 
void initState() 
{ 
_checkoutPro = PayUCheckoutProFlutter(this); 
} 
```

> Note: Make sure your minimum deployment target is iOS 11.

### Step 3: Setup PayU Checkout Pro protocol

* Implement Checkout Pro protocol methods to get hash generation callback and transaction status callback from Checkout Pro SDK: `class MyClass extends SupeprClass implements PayUCheckoutProProtocol`
* Implement the following methods in your class to get a callback from the SDK.

```d Dart
@override 
  generateHash(Map response) { 
    // Pass response param to your backend server 
    // Backend will generate the hash which you need to pass to SDK 
    // hashResponse: is the response which you get from your server 
    Map hashResponse = {}; 
    _checkoutPro.hashGenerated(hash: hashResponse); 
  } 

@override 
  onPaymentSuccess(dynamic response) { 
//Handle Success response 
  } 
 
  @override 
  onPaymentFailure(dynamic response) { 
//Handle Failure response 
  } 
 
  @override 
  onPaymentCancel(Map? response) { 
//Handle Payment cancel response 
  } 
 
  @override 
  onError(Map? response) { 
//Handle on error response 
  } 
```

***

## Step4: Setup payment hashes

This step describes how to pass the static and dynamic hashes. For detailed information, refer to [Generate Hash](doc:generate-dynamic-hash-flutter).

#### Pass static hashes

To pass static hashes during integration, use the following code snippet:

```d Dart
var payUPaymentParams = { 

   “key”: "Merchant key", 

   ... 

   ... 

   ... 

  “additionalParam”: { 
       “payment_related_details_for_mobile_sdk”: "payment_related_details_for_mobile_sdk hash", 
  “vas_for_mobile_sdk”: "vas_for_mobile_sdk hash", 
 “payment": "Payment Hash" 
   } 
} 
```

#### Pass dynamic hashes

To pass dynamic hashes, the merchant will receive a call on the generateHash method. In the method parameter, you will receive a dictionary or hashMap, then extract the value of hashString from that. Pass that value to the server to append the Salt at the end and generate the sha512 hash over it. The server gives that hash back to your app, and the app will pass that hash to PayU through a callback mechanism.

To pass the dynamic hashes during integration, use the following code snippet:

```d Dart
var hashName = response[PayUHashConstantsKeys.hashName]; 
var hashStringWithoutSalt = response[PayUHashConstantsKeys.hashString]; 
var hashType = response[PayUHashConstantsKeys.hashType]; 
var postSalt = response[PayUHashConstantsKeys.postSalt]; 
var hash = <Get Hash Backend with < hashString, merchantSalt , postSalt > 
Call hashGenerated with HashResponse< hashName , Hash> 
_checkoutPro.hashGenerated(hash: hashResponse); 
```

You need to generate the hashes at your backend: V1 Hash, V2 Hashes, MCP Lookup, and Post Salt Hash.

Use the following code snippet to generate the required hashes:

```d Dart
if (hashType == “V2”) { 
hash = <Get HmacSHA256Hash with (hashStringWithoutSalt, merchantSalt)> 
} else if (hashName == “mcpLookup”) { 
hash = <Get HmacSHA1Hash with (hashStringWithoutSalt, 	merchantSecretKey)> 
} else if (postSalt != null) 
{ 
//Add salt first then add post salt to create final hash 	string. 
hash = <Get SHA512Hash with <hashStringWithoutSalt + merchantSalt + <postSalt)>> 
} 
else 
{ 
hash = <Get SHA512Hash from Backend with <hashStringWithoutSalt > + <merchantSalt>> 
} 
```

> 📘 Remember
>
> * Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
> * The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) for CheckoutPro SDK.

***

### Step 5: Build the payment parameters

To initiate the payment, your app needs to send transactional information to the Checkout Pro SDK.

### Payment parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Key
        `mandatory`
      </td>

      <td>
        `String` This parameter must contain your merchant key received from PayU.
      </td>
    </tr>

    <tr>
      <td>
        transactionId
        `mandatory`
      </td>

      <td>
        `String` It should be unique for each transaction.
        Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "_,$,%,&, etc"
      </td>
    </tr>

    <tr>
      <td>
        Amount
        `mandatory`
      </td>

      <td>
        `String` Total transaction amount.
      </td>
    </tr>

    <tr>
      <td>
        productInfo
        `mandatory`
      </td>

      <td>
        `String` Information about the product.
      </td>
    </tr>

    <tr>
      <td>
        firstName
        `mandatory`
      </td>

      <td>
        `String` Customer’s first name
      </td>
    </tr>

    <tr>
      <td>
        Email
        `mandatory`
      </td>

      <td>
        `String` Customer’s email id
      </td>
    </tr>

    <tr>
      <td>
        Phone
        `mandatory`
      </td>

      <td>
        `String` Customer’s phone number,**Max character limit** : 10 Digits
      </td>
    </tr>

    <tr>
      <td>
        ios_surl
        `mandatory`
      </td>

      <td>
        `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.

        * _Note_*: This field is applicable for iOS integration
      </td>
    </tr>

    <tr>
      <td>
        ios_furl
        mandatory
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.

        * _Note_*: This field is applicable for iOS integration
      </td>
    </tr>

    <tr>
      <td>
        android_surl
        `mandatory`
      </td>

      <td>
        `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.
        `Note`: This field is applicable for Android integration

        * _Sample URL_*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
      </td>
    </tr>

    <tr>
      <td>
        android_furl
        `mandatory`
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.
        When the transaction gets successful, PayU will load this URL and pass the transaction response.
        `Note`: This field is applicable for Android integration

        * _Sample URL_*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
      </td>
    </tr>

    <tr>
      <td>
        Environment
        `mandatory`
      </td>

      <td>
        `String` Environment of SDK
      </td>
    </tr>

    <tr>
      <td>
        User Credential
        `mandatory`
      </td>

      <td>
        * _String_* This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:
          `<merchantKey>:<userId>  `
          Here,
          UserId is any id/email/phone number to uniquely identify the user.
      </td>
    </tr>
  </tbody>
</Table>

For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).

#### Additional Parameters (Optional)

The additional parameters that are optional that can be passed for the SDK are udf parameters, static hashes, and other parameters. For more details on Static Hash generation and passing them, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk). The following is a list of parameters that can be passed in additional parameters:

| Parameter                                 | Description                                                                                                                                                                                                         |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PayUCheckoutProConstants.CP_UDF1          | `String` User defined field, Merchant can store their customer id, etc.                                                                                                                                             |
| PayUCheckoutProConstants.CP_UDF2          | `String` User defined field, Merchant can store their customer id, etc.                                                                                                                                             |
| PayUCheckoutProConstants.CP_UDF3          | `String` User defined field, Merchant can store their customer id, etc.                                                                                                                                             |
| PayUCheckoutProConstants.CP_UDF4          | `String` User defined field, Merchant can store their customer id, etc.                                                                                                                                             |
| PayUCheckoutProConstants.CP_UDF5          | `String` User defined field, Merchant can store their customer id, etc.                                                                                                                                             |
| Static hashes                             | `String` The static hashes is specified in this parameter. For more information, refer to [Hash Generation](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step4-setup-payment-hashes) section. |
| PayUCheckoutProConstants.SODEX_OSOURC_EID | `String` Sodexo Source ID, Merchant can store it from the third field of PayU response.                                                                                                                             |
| PaymentParamConstant.walletUrn            | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account.                                                                                                                  |

The payment parameters and additional parameters can be passed using the following code snippet:

```d Dart
class PayUTestCredentials { 
  static const merchantKey = "<ADD YOUR MERCHANT KEY>"; 
  static const iosSurl = "<ADD YOUR iOS SURL>"; 
  static const iosFurl = "<ADD YOUR iOS FURL>"; 
  static const androidSurl = "<ADD YOUR ANDROID SURL>"; 
  static const androidFurl = "<ADD YOUR ANDROID FURL>"; 
  static const merchantAccessKey = "<ADD YOUR MERCHNAT ACCESS KEY>"; // Optional 
  static const sodexoSourceId = "<ADD YOUR SODEXO SOURCE ID>"; // Optional 
} 
var siParams = { 
      PayUSIParamsKeys.isFreeTrial: true, 
      PayUSIParamsKeys.billingAmount: '1', //REQUIRED 
      PayUSIParamsKeys.billingInterval: '1', //REQUIRED 
      PayUSIParamsKeys.paymentStartDate: '2023-04-20', //REQUIRED 
      PayUSIParamsKeys.paymentEndDate: '2023-04-30', //REQUIRED 
      PayUSIParamsKeys.billingCycle: 
          'daily', //REQUIRED //Can be any of 'daily','weekly','yearly','adhoc','once','monthly' 
      PayUSIParamsKeys.remarks: 'Test SI transaction', 
      PayUSIParamsKeys.billingCurrency: 'INR', 
      PayUSIParamsKeys.billingLimit: 'ON', //ON, BEFORE, AFTER 
      PayUSIParamsKeys.billingRule: 'MAX', //MAX, EXACT 
    }; 
    var additionalParam = { 
      PayUAdditionalParamKeys.udf1: "udf1", 
      PayUAdditionalParamKeys.udf2: "udf2", 
      PayUAdditionalParamKeys.udf3: "udf3", 
      PayUAdditionalParamKeys.udf4: "udf4", 
      PayUAdditionalParamKeys.udf5: "udf5", 
      PayUAdditionalParamKeys.merchantAccessKey: 
          PayUTestCredentials.merchantAccessKey, 
      PayUAdditionalParamKeys.sourceId: PayUTestCredentials.sodexoSourceId, 
    }; 
    var spitPaymentDetails = [ 
      { 
        "type": "absolute", 
        "splitInfo": { 
          "imAJ7I": { 
            "aggregatorSubTxnId": "Testchild123", 
            "aggregatorSubAmt": "5" 
          }, 
          "qOoYIv": { 
            "aggregatorSubTxnId": "Testchild098", 
            "aggregatorSubAmt": "5" 
          }, 
        } 
      } 
    ]; 
 
    var payUPaymentParams = { 
      PayUPaymentParamKey.key: ", //REQUIRED 
      PayUPaymentParamKey.amount: "1", //REQUIRED 
      PayUPaymentParamKey.productInfo: "Info", //REQUIRED 
      PayUPaymentParamKey.firstName: "Abc", //REQUIRED 
      PayUPaymentParamKey.email: "test@gmail.com", //REQUIRED 
      PayUPaymentParamKey.phone: "9999999999", //REQUIRED 
      PayUPaymentParamKey.ios_surl: PayUTestCredentials.iosSurl, //REQUIRED 
      PayUPaymentParamKey.ios_furl: PayUTestCredentials.iosFurl, //REQUIRED 
      PayUPaymentParamKey.android_surl: 
          PayUTestCredentials.androidSurl, //REQUIRED 
      PayUPaymentParamKey.android_furl: 
          PayUTestCredentials.androidFurl, //REQUIRED 
      PayUPaymentParamKey.environment: "0", //0 => Production 1 => Test 
      PayUPaymentParamKey.userCredential: 
          null, //Pass user credential to fetch saved cards => A:B - OPTIONAL 
      PayUPaymentParamKey.transactionId: "<ADD TRANSACTION ID>", //REQUIRED 
      PayUPaymentParamKey.additionalParam: additionalParam, // OPTIONAL 
      PayUPaymentParamKey.enableNativeOTP: true, // OPTIONAL 
      PayUPaymentParamKey.userToken: 
          "<Pass a unique token to fetch offers>", // OPTIONAL 
      PayUPaymentParamKey.payUSIParams: siParams, // OPTIONAL 
      PayUPaymentParamKey.splitPaymentDetails: spitPaymentDetails, // OPTIONAL 
    }; 
```

***

### Step 6: Initiate payment

Initialize and launch the Checkout Pro SDK by calling the following code snippet:

```d Dart
_checkoutPro.openCheckoutScreen( 
payUPaymentParams: < payUPaymentParams >, 
payUCheckoutProConfig: <payUConfigParams>, 

); 
```

***

### Step 7: Configure AndroidManifest.xml

To automatically fill OTP on bank pages, SDK requires the RECEIVE_SMS permission, configure the AndroidManifest.xml by adding receive sms permission as shown below.

```
<uses-permission android:name="android.permission.RECEIVE_SMS" /> 
```

***

### iOS specific integration

Flutter SDK offers a few optional customizations for IOS as mentioned below:

Customization (Optional)

* **For UPI Intent**

Currently, PayU supports only PhonePe and GooglePay through Intent. Add the query schemes in the `info.plist.`

```xml XML
<key>LSApplicationQueriesSchemes</key> 
<array> 
<string>phonepe</string> 
<string>paytm</string> 
<string>tez</string> 
<string>credpay</string>
<string>bhim</string.
</array> 
```

* Card Scanner, Camera Permission

```xml XML
<key>NSCameraUsageDescription</key> 

<string>Please mention the description to give user info</string> 
```

***

### Distributing your app (App Store / Ad-hoc)

What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayU ChekoutPro, refer to [Releasing Apple App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).

## Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

> 🚧 Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

> 👍 Testing checklist
>
> Things to remember while testing an integration:
>
> 1. To test the integration make sure that you are making a transaction call to the test endpoint.
> 2. Use your test key and salt for the transaction requests. See [Genearate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
> 3. Set the value of the `environment` parameters to `1`.

***

<TestCardsCallout />

You can make test payments using one of the payment methods configured at the Checkout.

### Test credentials for supported payment methods

Following are the payment methods supported in PayU Test mode.

#### Test Credential for Card

| Card Number      | Expiry | CVV | OTP    |
| :--------------- | :----- | :-- | :----- |
| 5123456789012346 | 05/25  | 123 | 123456 |

#### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

* **user name:** payu
* **password**: payu
* **OTP**: 123456

#### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

* [anything@upi](anything@upi)
* [9999999999@upi](mailto:9999999999@payu.in)

For Testing the UPI Collect flow, Please follow the below steps:- 

1. Once you enter the VPA click on the verify button and proceed to pay.
2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

[https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)`<Txn_id>`

**For Android**

You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

> 🚧 Ensure to remove the code from the manifest file before going live.

```xml xml
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</application>
```

**Test cards for EMI**

You can use the following Debit and Credit cards to test EMI integration.

<EMITestCards />

<br />

**Test Wallets**

You can use the following wallets and their corresponding credentials to test wallet integration.

<EMITestWallets />

## Go-live Checklist

Ensure these steps before you deploy the integration in a live environment.

### Collect Live Payments

After [testing the integration](https://docs.payu.in/docs/flutter-checkoutprosdk-test-integration) end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

> 🚧 Watch Out!
>
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `environment()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3:- Configure your SURL/FURL

PayU recommends you design or use your own SURL and FURL after testing is completed.

Refer to the link below for Handling SURL and FURL doc details.

> 🚧 We are not recommended to go live with PayU SURL and FURL.

### Checklist 4:- Remove/comment meta -data code from manifest file :-

#### For Android

You must be comment/remove the below metadata code from the manifest file to use the UPI Collect flow on Production env:-

```xml XML
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</appliction>
```

### Checklist 5: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 6: Configure Webhook

We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).

## Advanced Integration

### Prerequisites

Before you start with the advanced integration with PayUCheckoutPro, the payUCheckoutProConfig object needs to be passed with payUPaymentParams in the openCheckoutScreen method of the PayU SDK. The sample code snippet is similar to the following:

```d Dart
_checkoutPro.openCheckoutScreen(
payUPaymentParams: payUPaymentParams,
payUCheckoutProConfig: payUCheckoutProConfig,
);
```

***

### Change theme

#### For iOS

You can change the primary and the secondary color of the UI to match the theme of your app:

```d Dart
var payUCheckoutProConfig = {
 PayUCheckoutProConfigKeys.primaryColor: "<Color Hex Code e.g. #aabbcc>",
 PayUCheckoutProConfigKeys.secondaryColor: "<Color Hex Code e.g. #000000>",
}
```

#### For Android

You can modify the color scheme and theme used in the PayUCheckoutPro SDK by providing your own set of colors. To change the color theme of the SDK, add the following color configuration to your **colors.xml** file.

If you don’t have a **colors.xml**, create an empty file in your app project with this name, and include the following configuration settings:

```xml color.xml
<color name="one_payu_colorPrimary">#053bc1</color>  //primary color has changed the appbar/toolbar and background color.  
<color name="one_payu_colorPrimaryDark">#053bc1</color> //primaryDark color has changed statusbar and contextual app bar.  
<color name="one_payu_colorAccent">#053bc1</color> //colorAccent has changed such as check boxes, radio buttons, and edit text boxes, cursor.  
<color name="one_payu_baseTextColor">#ffffff</color> //baseTextcolor as changed header and button text
```

***

### Customise font

You can customize the font used in the PayU checkout page as per your preference. To customize the font, add the following code snippet in the `style.xml` file of your Android app.

```xml XML
<style name="PayU_header">
    <item name="android:fontFamily">@font/font_name</item>
</style>
```

Here, we are setting the fontFamily attribute to the font file that you want to access. See Add a font as an XML resource in the Android developer documentation to learn more.

> 📘 Note
>
> See[ Add a font as an XML resource](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml)  in the Android developer documentation to learn more.

## Set merchant logo

You can customize the logo to personalize the checkout screen for iOS or Android platforms.

#### For iOS

```d Dart
var payUCheckoutProConfig = {
 PayUCheckoutProConfigKeys.merchantLogo: "<Image asset name like 'Jio'>",
}
```

#### For Android

Add the image in the app/res/drawable folder of the native Android app and pass the same under the merchantLogo key.

***

### Set merchant name

You can customize the name to personalize the checkout screen.

```d Dart
var payUCheckoutProConfig = {
 	PayUCheckoutProConfigKeys.merchantName: "<Merchant Name>",
}
```

***

### Hide Checkout screen Back button dialog box

You can choose to hide the dialog box that is displayed when the Back button is clicked from the L1 screen. The default value is true.

```d Dart
var payUCheckoutProConfig = {
 	PayUCheckoutProConfigKeys.showExitConfirmationOnCheckoutScreen: true/false,
}
```

***

### Hide Back button dialog box after payment initialisation

You can choose to hide the dialog that is displayed when the Back button is clicked after payment is initialized. The default value is true.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.showExitConfirmationOnPaymentScreen: true/false,
}
```

***

### Auto Select OTP

You can choose to auto-select OTP flow on the bank page with the flag as in the following code block. The default value is false.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.autoSelectOtp:: true/false,
}
```

***

### Set merchant response timeout

The merchant response timeout is the time interval that PayU waits for merchant surl/furl to load before passing the transaction response back to the app. If merchant surl/furl pages take longer to load, PayU has a response timeout of 5000 milliseconds by default. However, if you feel that their surl/furl can take longer than 5000 milliseconds, you can set this flag.

```d Dart
var payUCheckoutProConfig = {
 PayUCheckoutProConfigKeys.merchantResponseTimeout: 5000,
}
```

***

### Review order

You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow.

```d Dart
var payUCheckoutProConfig = {
 PayUCheckoutProConfigKeys.cartDetails: [{ 'Order': 'Value' }, { 'Key Name': 'Value1' }]
}
```

For example:

```d Dart
var cartDetails = [ 
         {"GST": "5%"},      
         {"Delivery Date": "25 Dec"},      
         {"Status": "In Progress"}    
];
```

***

### Additional payment options on the Checkout screen

The following code snippet is used to display Google Pay, PhonePe, and Paytm on the primary Checkout screen.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.paymentModesOrder: [{ 'UPI': 'TEZ' }, { 'Wallets': 'PAYTM' }, { 'Wallets': 'PHONEPE' }]
}
```

***

This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options.

***

### Configure checkout payment modes order

Default payment modes order on the checkout screen, as illustrated in the following code block, is:

* Card
* NetBanking
* UPI
* Wallets

You can configure the checkout payment options order. You need to provide a list of payment modes to configure the payment options order. Checkout order will be the order of items in the list. If not all payment modes' order is mentioned in the list, all other payment modes will be displayed in their default order as shown above.

The following code snippet is used to order the payment modes on the L1 screen:

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.paymentModesOrder: [{ 'cards': '' }, { 'net banking': '' }, { 'upi': '' }, { 'wallets':'' }, { 'emi': '' }]
}
```

The resulting payment order on the initial Checkout screen will be:

* Cards (Credit or Debit)
* Net Banking
* UPI
* Wallets
* EMI

***

### Offers integration

To pass offers in the CheckoutPro SDK, use the following code snippet:

```d Dart
	var payUPaymentParams = {
PayUPaymentParamKey.userToken:           "<Pass a unique token to fetch offers>", // OPTIONAL
}
```

***

### Native OTP assist

To enable Native OTP assistance in iOS, use the following code. In Android, this will be added by default.

```d Dart
var payUPaymentParams = {
PayUPaymentParamKey.enableNativeOTP: true, // OPTIONAL
}
```

***

### Custom Note integration

This subsection describes how to integrate custom notes in PayUCheckoutPro SDK. To integrate custom notes in PayUCheckoutPro SDK:

* Create a custom note list
* Pass custom note list to SDK

#### Step 1: Create a Custom Note list

Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom_note and custom_note_category need to be passed.

```d Dart
var customNotes = [       {         "custom_note": "Its Common custom note for testing purpose",         "custom_note_category": [           PayUPaymentTypeKeys.emi,           PayUPaymentTypeKeys.card         ]       },       {         "custom_note": "Payment options custom note",         "custom_note_category": null       }     ];
```

#### Step 2: Add in PayU Checkout config

Add in the PayU Checkout Config similar to the following code snippet:

```d Dart
var payUCheckoutProConfig = {  		     	PayUCheckoutProConfigKeys.customNotes: customNotes
}
```

***

### Enforced Payment Modes

You can directly open a specific payment mode like NB, WALLET, UPI, CARD, etc in SDK. To enforce payments:

1. Create an enforced payment list
2. Add in PayU Checkout Config

#### Step 1: Create an enforced payment list

Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each enforce payment, payment_type and enforce_ibiboCode needs to be passed.

```d Dart
var enforcePaymentList = [       {"payment_type": "CARD", "enforce_ibiboCode": "UTIBENCC"},  ];
```

#### Step 2: Add in PayU Checkout config

Add in PayU Checkout Config similar to the following snippet:

```d Dart
var payUCheckoutProConfig = {
 PayUCheckoutProConfigKeys.enforcePaymentList: enforcePaymentList, 
}
```

### Android specific configurations

#### Runtime SMS permission

You can set this flag to false if you do not want CheckoutPro SDK to ask for runtime SMS permission on the bank OTP page. The default value is true.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys .merchantSMSPermission: true/false
}
```

#### Auto Approve OTP

You can choose to automatically approve OTP flow on the bank page with the flag specified in the following code block. The default value is false.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.autoApprove: true/false
}
```

**Hide toolbar in the Custom Browser (CB)**

You can choose to hide the toolbar on CB. By default, the CB toolbar is displayed.

```d Dart
var payUCheckoutProConfig = {
PayUCheckoutProConfigKeys.showCbToolbar: true/false
}
```

## Sample App

The sample application for integration with Flutter PayUCheckoutPro SDK :

[https://github.com/payu-intrepos/PayUCheckoutPro-Flutter.git](https://github.com/payu-intrepos/PayUCheckoutPro-Flutter.git)

<br />
