---
title: 1. SDK Integration Steps - iOS Native OTP Assist
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
## Step 1: Include the SDK

The Native OTP SDK is offered via CocoaPods. To add the SDK to your app project, include the SDK framework in your `podfile`.

`// make sure to add below-mentioned line to use dynamic frameworksuse_frameworks!​
// Add this to include our SDK
pod 'PayUIndia-NativeOtpAssist'`

Install dependency using pod `installcommand `in `terminalNext`, add the following imports in the class where you need to initiate a payment:

```Text Objective-C
#import <PayUNativeOtpAssist/PayUNativeOtpAssist.h>
```
```Text Swift
import PayUNativeOtpAssist
```

> 📘 Compatibilty
> 
> - Min SDK Version: 21

> **Note**: Configure Excluded Architectures to arm64 in the Build Settings of your project to run in Simulator.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/23a362b-Screenshot_2023-08-12_at_8.48.27_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


In order to receive all the crashes related to our SDKs, add the below-mentioned line to your AppDelegate's `didFinishLaunchingWithOptions`.

**CrashReporter**  
In order to receive all the crashes related to our SDKs, add the below-mentioned line to your AppDelegate’s `didFinishLaunchingWithOptions`.

```Text Objective-C
[PayUOtpAssist start];
```
```Text Swift
PayUOtpAssist.start()
```

### Swift Package Manager integration

You can integrate PayUIndia-NativeOtpAssist with your app or SDK with the following methods:

- **Using Xcode**: Navigate to the File > Add Package menu and install the following package:  
  <https://github.com/payu-intrepos/PayUNativeOtpAssist-iOS>
- **Using Package.Swift**: Add the following line in the Package.swift dependencies:

`.package(name: "PayUIndia-NativeOtpAssist", url: "https://github.com/payu-intrepos/PayUNativeOtpAssist-iOS", from: "2.0.0")`

***

## Step 2: Generate payment hash

For detailed information on hash generation, refer to [Hash Generation](https://docs.payu.in/docs/ios-checkoutpro-generate-hash).

> ❗️ Callout
> 
> Every transaction (payment or non-payment) needs a hash by the merchant before sending the transaction details to PayU. This is required for PayU to validate the authenticity of the transaction. This should be done on your server.

***

## Create postData

To initiate a payment, your app will need to send transactional information to the Checkout Pro SDK. To pass this information, build a payment parameter object similar to the following code snippet:

> **Note**: TransactionId can’t have a special character and not more than 25 characters.

```Text Objective-C
PayUPaymentParam *paymentParam = [[PayUPaymentParam alloc] initWithKey:<#(NSString * _Nonnull)#>
                                                         transactionId:<#(NSString * _Nonnull)#>
                                                                amount:<#(NSString * _Nonnull)#>
                                                           productInfo:<#(NSString * _Nonnull)#>
                                                             firstName:<#(NSString * _Nonnull)#>
                                                                 email:<#(NSString * _Nonnull)#>
                                                                 phone:<#(NSString * _Nonnull)#>
                                                                  surl:<#(NSString * _Nonnull)#>
                                                                  furl:<#(NSString * _Nonnull)#>
                                                           environment:<#(enum Environment)#> /*EnvironmentProduction or EnvironmentTest*/];
paymentParam.hashes = [PayUHashes new];
paymentParam.hashes.paymentHash = <#T##SHA512 HashString#>;
CCDC *ccdc = [CCDC new];
ccdc.cardNumber = <#T##String#>;
ccdc.expiryYear = <#T##String#>;
ccdc.expiryMonth = <#T##String#>;
ccdc.cvv = <#T##String#>;
ccdc.txnS2SFlow = <#T##String#>; //"4" for transactions on native otp assist
ccdc.nameOnCard = <#T##String#>;
ccdc.shouldSaveCard = <#T##String#>;
paymentParam.paymentOption = ccdc;
paymentParam.userCredential = <#(NSString)#>; // For saving and fetching use saved 
```
```Text Swift
let paymentParam = PayUPaymentParam(key: <#T##String#>,
                                    transactionId: <#T##String#>,
                                    amount: <#T##String#>,
                                    productInfo: <#T##String#>,
                                    firstName: <#T##String#>,
                                    email: <#T##String#>,
                                    phone: <#T##String#>,
                                    surl: <#T##String#>,
                                    furl: <#T##String#>,
                                    environment: <#T##Environment#> /*.production or .test*/)

paymentParam.hashes = PayUHashes()
paymentParam.hashes?.paymentHash = <#T##SHA512 HashString#>
let ccdc = CCDC()
ccdc.cardNumber = <#T##String#>
ccdc.expiryYear = <#T##String#>
ccdc.expiryMonth = <#T##String#>
ccdc.cvv = <#T##String#>
ccdc.txnS2SFlow = <#T##String#> //"4" for transactions on native otp assist
ccdc.nameOnCard = <#T##String#>
ccdc.shouldSaveCard = <#T##String#>
paymentParam.paymentOption = ccdc
paymentParam.userCredential = <#T##String#> // For saving and fetching user’s saved card
```

> 📘 Note
> 
> Use Core SDK library to generate payment post data.

***

## Step 3: Initiate payment

Initialize the Native OTP Assist SDK by providing the PayUOtpAssistConfig object having the`postdata `and reference to the `PayUOtpAssistCallback` to listen to the SDK events.

```Text Objective-C
[PayUCheckoutPro openOn:self paymentParam:paymentParam config:<#(PayUOtpAssistConfig * _Nullable)#> delegate:self];
```
```Text Swift
PayUOtpAssist.open(
                    parentVC: self,
                    paymentParam: paymentParam,
                    config: <#T##PayUOtpAssistConfig?#>,
                    delegate: self
  )
```

> 📘 Note:
> 
> Initiate payment must be on the Main thread.

### Callbacks

The list of the callback function provided by PayUOtpAssistCallback class:

- `fun onPaymentSuccess(merchantResponse: String?, payUResponse: String?)`– Called when payment succeeds. merchantResponse:

- `fun onPaymentFailure(merchantResponse: String?, payUResponse: String?)`– Called when a payment fails.

- `fun onError(errorCode: String?, errorMessage: String?`)- Called when we got some error where,
  1. `errorCode`: Error Code
  2. `errorMessage`: Error Description

- `fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest):` Boolean – It’s an optional callback, override when you want to handle the Bank page redirection flow. You just need to change the return value to false. You can also open CustomBrowser in fallback scenarios. The following code snippet is used to open the CustomBrowser. For more information on using CustomBrowser, refer to [iOS CustomBrowser SDK](https://docs.payu.in/docs/ios-custombrowser-sdk).

```Text Swift
fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest) : Boolean {

val customBrowserConfig = CustomBrowserConfig(merchantKey, txnId)
   
  //Set the issuerUrl and issuerPostData to open in WebView for otp assist redirection to bank page
  if (!payUAcsRequest?.issuerUrl.isNullOrEmpty() && !payUAcsRequest?.issuerPostData.isNullOrEmpty()) {
    customBrowserConfig.postURL = payUAcsRequest?.issuerUrl
    customBrowserConfig.payuPostData = payUAcsRequest?.issuerPostData

}else if (!payUAcsRequest?.acsTemplate.isNullOrEmpty()){
    customBrowserConfig.htmlData = payUAcsRequest?.acsTemplate
}else {
    //Set the first url to open in WebView
    customBrowserConfig.postURL = url
    customBrowserConfig.payuPostData = payuConfig.data
}
return false
}
```

You will get `PayUAcsRequest on shouldHandleFallback(`) callback. whether you will get `issuerUrl` and `issuerPostData` or acsTemplate on `PayUAcsRequest` acsTemplate is the HTML string that you need to load to the Webview.

| PayUAcsRequest field | Description                                                                                                                                           |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| issuerUrl            | It’s the Bank/ACS page Url.                                                                                                                           |
| issuerPostData       | You need to load `issuerUrl` to the Webview along with this `issuerPostdata` string. Ex: `webView.postUrl`(`issuerUrl, issuerPostData.toByteArray()`) |
| acsTemplate          | If` issuerUr`l is empty, you need to load acsTemplate to the Webview. Ex: `webView.loadData`(`acsTemplate, “text/html”, “UTF-8”`);                    |

### Error codes

| Error Code | Description                                              |
| :--------- | :------------------------------------------------------- |
| 1001       | No Internet                                              |
| 1002       | Network timeout, please verify with your server.         |
| 1003       | Gateway timeout, please verify with your server.         |
| 1004       | The user canceled it, please verify with your server.    |
| 1005       | Something went wrong, please verify with your server.    |
| 1006       | The bank page timed out, please verify with your server. |

***

## Step 4: Verify the transaction

After you get the response from SDK, make sure to confirm it with the PayU server.

> 🚧 Remember
> 
> It is recommended to implement the PayU Webhook or backend verify call from your backend.

### Implementation of PayU Verify API

Since you already have the txnID (Order ID generated at your end) value for such cases, you simply need to execute the verify_payment API with the necessary input parameters. The output would return you the transaction status in the `status` key and various other parameters also. For more information, refer to the [Verify Payment Status ](https://docs.payu.in/reference/verify_payment_api)API.

Endpoint URL: <https://info.payu.in/merchant/postservice.php?form=2>

**Sample Request**

```Text Curl
curl --location --request POST '{{Url}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key={merchantKey}' \
--data-urlencode 'command=verify_payment' \
--data-urlencode 'hash=c6febddfaaf6986dd8bd982d3769f856ab149e4de92dbad995c8df808ffcfbcb2c227a3fae38b69eb39ad7b6ce4e06e6b12289f70cc500cea5a2cda449c7dcba' \
--data-urlencode 'var1=Txn1234'
```