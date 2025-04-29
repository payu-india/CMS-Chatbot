---
title: 1. Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Flutter Check Out SDK Integration Steps
  description: ''
  keywords:
    - Flutter Checkout Pro SDK Integration Steps
    - PayU Flutter SDK integration steps
    - Mobile payment integration with PayU Flutter SDK steps
    - PayU Flutter Checkout Pro set up for Mobile
    - Flutter CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Flutter SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
To integrate PayU CheckoutPro with Flutter SDK:

- [Step 1: Include the SDK in your app project](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-1-include-the-sdk-in-your-app-project)
- [Step 2: Initialize PayU Checkout Pro Flutter object](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step2-initialize-payu-checkout-pro-flutter-object)
- [Step 3: Setup PayU Checkout Pro protocol](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step3-setup-payu-checkout-pro-protocol)
- [Step 4: Setup payment hashes](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step4-setup-payment-hashes)
- [Step 5: Build the Payment Parameters](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-5-build-the-payment-parameters)
- [Step 6: Initiate payment](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-6-initiate-payment)
- [Step 7: Configure AndroidManifest.xml](https://docs.payu.in/docs/flutter-checkoutprosdk-integration-steps#step-7-configure-androidmanifestxml)

For IOS, refer to iOS Specific Integration and check Distributing Your App (App Store/ Ad-hoc) to deploy your application. For more information, refer to [Explore iOS SDKs](doc:explore-ios-sdks)

## Step 1: Include the SDK in your app project

The CheckoutPro SDK for Flutter is offered through Flutter `pub.dev`

- To add the PayU Checkout Pro Flutter plugin add the following dependency in your app: `$ flutter pub add payu_checkoutpro_flutter`

```Text Dart
import 'package:payu_checkoutpro_flutter/payu_checkoutpro_flutter.dart'; 
import 'package:payu_checkoutpro_flutter/PayUConstantKeys.dart'; 
 
```

- **For iOS**: Install the pod using the following command inside `ios` folder: `$ pod install`

***

## Step2: Initialize PayU Checkout Pro Flutter object

- Create PayUCheckout Pro Flutter instance.
  ```
  late PayUCheckoutProFlutter \_checkoutPro;
  ```

Initialize the PayUCheckoutProFlutter object using the current object.

```Text Dart
@override 
void initState() 
{ 
_checkoutPro = PayUCheckoutProFlutter(this); 
} 
```

> Note: Make sure your minimum deployment target is iOS 11.

## Step3: Setup PayU Checkout Pro protocol

- Implement Checkout Pro protocol methods to get hash generation callback and transaction status callback from Checkout Pro SDK: `class MyClass extends SupeprClass implements PayUCheckoutProProtocol`
- Implement the following methods in your class to get a callback from the SDK.

```Text Dart
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

### Pass static hashes

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

### Pass dynamic hashes

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

We need the following type of hashes to be generated at your backend: V1 Hash, V2 Hashes, MCP Lookup, and Post Salt Hash.

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
> - Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
> - The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) for CheckoutPro SDK.

***

## Step 5: Build the payment parameters

To initiate the payment, your app needs to send transactional information to the Checkout Pro SDK.

### Payment parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "Key  \n`mandatory`",
    "0-1": "`String` This parameter must contain your merchant key received from PayU.",
    "1-0": "transactionId  \n`mandatory`",
    "1-1": "`String` It should be unique for each transaction.  \nCannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - \"\\_,$,%,&, etc\"",
    "2-0": "Amount  \n`mandatory`",
    "2-1": "`String` Total transaction amount.",
    "3-0": "productInfo  \n`mandatory`",
    "3-1": "`String` Information about the product.",
    "4-0": "firstName  \n`mandatory`",
    "4-1": "`String` Customer’s first name",
    "5-0": "Email  \n`mandatory`",
    "5-1": "`String` Customer’s email id",
    "6-0": "Phone  \n`mandatory`",
    "6-1": "`String` Customer’s phone number,** Max character limit** : 10 Digits",
    "7-0": "ios_surl  \n`mandatory`",
    "7-1": "`String` When the transaction gets successful, PayU will load this URL and pass the transaction response.  \n**Note**: This field is applicable for iOS integration",
    "8-0": "ios_furl  \nmandatory",
    "8-1": "`String` When the transaction fails, PayU will load this URL and pass the transaction response.  \n**Note**: This field is applicable for iOS integration",
    "9-0": "android_surl  \n`mandatory`",
    "9-1": "`String` When the transaction gets successful, PayU will load this URL and pass the transaction response.  \n`Note`: This field is applicable for Android integration  \n**Sample URL**: <https://cbjs.payu.in/sdk/success>",
    "10-0": "android_furl  \n`mandatory`",
    "10-1": "`String` When the transaction fails, PayU will load this URL and pass the transaction response.  \nWhen the transaction gets successful, PayU will load this URL and pass the transaction response.  \n`Note`: This field is applicable for Android integration  \n**Sample URL**: <https://cbjs.payu.in/sdk/failure>",
    "11-0": "Environment  \n`mandatory`",
    "11-1": "`String` Environment of SDK",
    "12-0": "User Credential  \n`mandatory`",
    "12-1": "**String** This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:  \n`<merchantKey>:<userId>  `  \nHere,  \nUserId is any id/email/phone number to uniquely identify the user."
  },
  "cols": 2,
  "rows": 13,
  "align": [
    "left",
    "left"
  ]
}
[/block]


For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters). 

### Additional Parameters (Optional)

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

## Step 6: Initiate payment

Initialize and launch the Checkout Pro SDK by calling the following code snippet:

```Text Dart
_checkoutPro.openCheckoutScreen( 
payUPaymentParams: < payUPaymentParams >, 
payUCheckoutProConfig: <payUConfigParams>, 

); 
```

***

## Step 7: Configure AndroidManifest.xml

To automatically fill OTP on bank pages, SDK requires the RECEIVE_SMS permission, configure the AndroidManifest.xml by adding receive sms permission as shown below.

```
<uses-permission android:name="android.permission.RECEIVE_SMS" /> 
```

***

## IOS specific integration

Flutter SDK offers a few optional customizations for IOS as mentioned below:

Customization (Optional)

- **For UPI Intent**

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

- Card Scanner, Camera Permission

```Text XML
<key>NSCameraUsageDescription</key> 

<string>Please mention the description to give user info</string> 
```

***

## Distributing your app (App Store / Ad-hoc)

What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayU ChekoutPro, refer to [Releasing Apple App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).