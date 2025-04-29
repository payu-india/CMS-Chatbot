---
title: Seamless Integration
excerpt: Build a seamless integration to create your own UI for payment flow.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Before you begin
>
> * To download iOS SDK through CocoaPod, refer to CocoaPods Integration.
> * Run the sample app:\
>   i. Download latest SDK version and unzip it.\
>   ii. Unzip Release-Universal, now drag and drop the content of unzipped file into Sample App

***

## Step 1: Initial set up

To perform the initial setup:

1. Download the latest SDK version from the following location and unzip it: [https://github.com/payu-intrepos/iOS-SDK/releases](https://github.com/payu-intrepos/iOS-SDK/releases)
2. Unzip Release-Universal, drag and drop the content of the unzipped file into Sample App.

```Text Swift
import PayUBizCoreKit
```
```Text Objective-C
#import <PayUBizCoreKit/PayUBizCoreKit.h>
```

> **Note**: While working with the Swift project add the above code in Bridging-Header.h file.

3. Get all the required parameters.
4. Create an object of PayUModelPaymentParams and set all the parameters in it.

```Text Swift
let paymentParamForPassing = PayUModelPaymentParams()
paymentParamForPassing.key = "0MQaQP"
paymentParamForPassing.transactionID = "Ywism0Q9XC88qvy"
paymentParamForPassing.amount = "10.0"
paymentParamForPassing.productInfo = "Nokia"
paymentParamForPassing.firstName = "Ram"
paymentParamForPassing.email = "email@testsdk1.com"
paymentParamForPassing.userCredentials = "ra:ra"
paymentParamForPassing.phoneNumber = "1111111111"
paymentParamForPassing.surl = "https://payu.herokuapp.com/ios_success"
paymentParamForPassing.furl = "https://payu.herokuapp.com/ios_failure"
paymentParamForPassing.udf1 = "u1"
paymentParamForPassing.udf2 = "u2"
paymentParamForPassing.udf3 = "u3"
paymentParamForPassing.udf4 = "u4"
paymentParamForPassing.udf5 = "u5"
paymentParamForPassing.environment = ENVIRONMENT_PRODUCTION
paymentParamForPassing.offerKey = "offertest@1411"
```
```Text Objective-C
  @property (strong, nonatomic) PayUModelPaymentParams *paymentParamForPassing;
  self.paymentParamForPassing = [PayUModelPaymentParams new];
  self.paymentParamForPassing.key = @"0MQaQP";
  self.paymentParamForPassing.transactionID = @"Ywism0Q9XC88qvy";
  self.paymentParamForPassing.amount = @"10.0";
  self.paymentParamForPassing.productInfo = @"Nokia";
  self.paymentParamForPassing.firstName = @"Ram";
  self.paymentParamForPassing.email = @"email@testsdk1.com";
  self.paymentParamForPassing.userCredentials = @"ra:ra";
  self.paymentParamForPassing.phoneNumber = @"1111111111";
  self.paymentParamForPassing.SURL = @"https://cbjs.payu.in/sdk/success";
  self.paymentParamForPassing.FURL = @"https://cbjs.payu.in/sdk/failure";
  self.paymentParamForPassing.udf1 = @"u1";
  self.paymentParamForPassing.udf2 = @"u2";
  self.paymentParamForPassing.udf3 = @"u3";
  self.paymentParamForPassing.udf4 = @"u4";
  self.paymentParamForPassing.udf5 = @"u5";
  self.paymentParamForPassing.environment= ENVIRONMENT_PRODUCTION;
  self.paymentParamForPassing.offerKey = @"offertest@1411";
//You don't need to set udf1-5 in case you are not using them email and firstname can be empty strings "" if you don't want to use them For store user card feature you need to set userCredentials
```

> **Note**: You don’t need to set the udf1 – udf5 parameters. In case you are not using them, the email and firstname parameters can be empty strings (“”).

5. Set `paymentParamForPassing.userCredentials` to store the user card:

```Text Swift
paymentParamForPassing.userCredentials = "ra:ra"
```
```Text Objective-c
  self.paymentParamForPassing.userCredentials = @"ra:ra"
```

6. Set `offerKey` for offers:

```Text Swift
paymentParamForPassing.offerKey = "offertest@1411"
```
```Text Objective-C
  self.paymentParamForPassing.offerKey = @"offertest@1411"
```

7. Set default param (like phone and others) for any other payment:

```Text Swift
paymentParamForPassing.phoneNumber = "1111111111"
```
```Text Objective-C
self.paymentParamForPassing.phoneNumber = @"1111111111";
```

8. Get the required hashes by using your own server. Set the hashes as follows:

```Text Swift
paymentParamForPassing.hashes.paymentHash = "ade84bf6dd9da35d0aab50a5bf61d6272ab0fc488b361b65c66745054aacf1900e3c60b5022d2114bae7360174ebcb3cd7185a5d472e5c99701e5e7e1eccec34"
paymentParamForPassing.hashes.paymentRelatedDetailsHash = "915299224c80eff0eb2407b945a5087556292f58baca25fd05a0bceb6826aa9eb531810001dd4b4677dd928dd60d39eecf843b2189f213f9bb82c5a9483e3aac"
paymentParamForPassing.hashes.vasForMobileSDKHash = "5c0314c2781876f7e0a53676b0d08e1457dafe904d2d15d948626b57409538d51093eef4f15c792b1b9651be7b5659efdd45926e43a1145d68cea094687011ca"
paymentParamForPassing.hashes.deleteUserCardHash = "03e10e892005755f91061121036fb1b10f46202b4138d182f153c5de5c7fd44930ed94b32fac230e59bac1e4ca123aca3297e4b9d25024bf13237db9721fec1a"
paymentParamForPassing.hashes.offerHash = "1e99fdb59bd91c1a85624104c0fcfae34d7fcb850dd17a0b75e7efe49857d15fdefc47dd0d86ca34cbc3a8b580839aea6341a573e4e60dc1ddcf7ecc32bf9cae"
```
```Text Objective-C
  self.paymentParamForPassing.hashes.paymentHash = @"ade84bf6dd9da35d0aab50a5bf61d6272ab0fc488b361b65c66745054aacf1900e3c60b5022d2114bae7360174ebcb3cd7185a5d472e5c99701e5e7e1eccec34";
  self.paymentParamForPassing.hashes.paymentRelatedDetailsHash = @"915299224c80eff0eb2407b945a5087556292f58baca25fd05a0bceb6826aa9eb531810001dd4b4677dd928dd60d39eecf843b2189f213f9bb82c5a9483e3aac";
  self.paymentParamForPassing.hashes.VASForMobileSDKHash = @"5c0314c2781876f7e0a53676b0d08e1457dafe904d2d15d948626b57409538d51093eef4f15c792b1b9651be7b5659efdd45926e43a1145d68cea094687011ca";
  self.paymentParamForPassing.hashes.deleteUserCardHash = @"03e10e892005755f91061121036fb1b10f46202b4138d182f153c5de5c7fd44930ed94b32fac230e59bac1e4ca123aca3297e4b9d25024bf13237db9721fec1a";
  self.paymentParamForPassing.hashes.offerHash = @"1e99fdb59bd91c1a85624104c0fcfae34d7fcb850dd17a0b75e7efe49857d15fdefc47dd0d86ca34cbc3a8b580839aea6341a573e4e60dc1ddcf7ecc32bf9cae";
```

***

## Step 2: Generate URL request for payment

To generate an URL request (and post parameters), you need to create an object as `createRequest `of the PayUCreateRequest class as shown in the following code block:

```Text Swift
let createRequest = PayUCreateRequest()
```
```Text Objective-C
@property (nonatomic, strong) PayUCreateRequest *createRequest;
```

The callbacks give your URLRequest as well as post parameters (NSString format). You can use these post parameters to initialize the Custom Browser Instance.

The following payment types are supported by SDK, and additional parameters are supported. The additional parameters that can be configured in the createRequest object created earlier are described in the following sections:

* [Credit Card/Debit Card Integration](https://docs.payu.in/docs/credit-carddebit-card-integration-ios-core-sdk)
* [Stored Card Integration](https://docs.payu.in/docs/stored-card-integration-ios-core-sdk)
* [Tokenized Card Payments](https://docs.payu.in/docs/tokenized-card-payment-ios-core-sdk)
* [Net Banking Integration](https://docs.payu.in/docs/net-banking-integration-ios-core-sdk)
* [Cash Card Integration](https://docs.payu.in/docs/cash-card-ios-core-sdk)
* [EMI Payment Integration](https://docs.payu.in/docs/emi-payment-integration-ios-core-sdk)
* [LazyPay BNPL Integration](https://docs.payu.in/docs/lazypay-bnpl-integration-ios-core-sdk)
* [TwidPay BNPL Integration](https://docs.payu.in/docs/twidpay-integration-ios-core-sdk)
* [Pluxee Card Integration](https://docs.payu.in/docs/pluxee-card-integration-ios-core-sdk)
