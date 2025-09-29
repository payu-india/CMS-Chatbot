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

```Text Dart
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

```Text Dart
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

```Text Dart
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

```Text Dart
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

```Text Dart
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

```Text XML
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

```Text XML
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

```Text xml
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

```Text XML
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

## Sample App

[https://github.com/payu-intrepos/PayUCheckoutPro-Flutter.git](https://github.com/payu-intrepos/PayUCheckoutPro-Flutter.git)

<br />
