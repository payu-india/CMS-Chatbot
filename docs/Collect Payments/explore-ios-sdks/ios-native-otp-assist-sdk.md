---
title: iOS Native OTP Assist SDK
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
The OTP Assist SDK provides a complete authentication flow for card transactions. It offers to capture OTP in the merchant app without any redirection to the bank's 3Dsecure/ACS page. This means that there's one less point of failure in the checkout process and a faster completion rate for transactions. The OTP Assist SDK will auto-read and submit OTP on behalf of the user.

## Features

The Native OTP Assist SDK gives you the following key capabilities:

* Read OTP on the merchant app without redirecting to the bank page, for eligible bins.
* If the bin is not eligible, then it will redirect to the bank's 3d-secure/ACS page.
* Support for Android native SMS permission, as well as Google Consent API.

<Accordion title="Step 1. SDK Integration" icon="fa-gear">
  The iOS Native OTP Assist SDK integration involves the following steps:

  <Accordion title="Step 1: Include the SDK" icon="fa-code">
    The Native OTP SDK is offered via CocoaPods. To add the SDK to your app project, include the SDK framework in your `podfile`.

    `// make sure to add below-mentioned line to use dynamic frameworksuse_frameworks!​
                                                            // Add this to include our SDK
                                                            pod 'PayUIndia-NativeOtpAssist'`

    Install dependency using pod `installcommand `in `terminalNext`, add the following imports in the class where you need to initiate a payment:

    ```swift Swift
    import PayUNativeOtpAssist
    ```
    ```objectivec Objective-C
    #import <PayUNativeOtpAssist/PayUNativeOtpAssist.h>
    ```

    > 📘 Compatibilty
    >
    > * Min SDK Version: 21

    > **Note**: Configure Excluded Architectures to arm64 in the Build Settings of your project to run in Simulator.

    <Image align="center" src="https://files.readme.io/23a362b-Screenshot_2023-08-12_at_8.48.27_PM.png" />

    In order to receive all the crashes related to our SDKs, add the below-mentioned line to your AppDelegate's `didFinishLaunchingWithOptions`.

    **CrashReporter**
    In order to receive all the crashes related to our SDKs, add the below-mentioned line to your AppDelegate's `didFinishLaunchingWithOptions`.

    ```swift Swift
    PayUOtpAssist.start()
    ```
    ```objectivec Objective-C
    [PayUOtpAssist start];
    ```

    #### Swift Package Manager integration

    You can integrate PayUIndia-NativeOtpAssist with your app or SDK with the following methods:

    * **Using Xcode**: Navigate to the File > Add Package menu and install the following package:
      [https://github.com/payu-intrepos/PayUNativeOtpAssist-iOS](https://github.com/payu-intrepos/PayUNativeOtpAssist-iOS)
    * **Using Package.Swift**: Add the following line in the Package.swift dependencies:

    `.package(name: "PayUIndia-NativeOtpAssist", url: "https://github.com/payu-intrepos/PayUNativeOtpAssist-iOS", from: "2.0.0")`

    ***
  </Accordion>

  <Accordion title="Step 2: Generate payment hash" icon="fa-code">
    For detailed information on hash generation, refer to [Hash Generation](doc:set-up-the-payment-hashes).

    > ❗️ Callout
    >
    > Every transaction (payment or non-payment) needs a hash by the merchant before sending the transaction details to PayU. This is required for PayU to validate the authenticity of the transaction. This should be done on your server.

    ***

    <Accordion title="Create postData" icon="fa-code">
      To initiate a payment, your app will need to send transactional information to the Checkout Pro SDK. To pass this information, build a payment parameter object similar to the following code snippet:

      > **Note**: TransactionId can't have a special character and not more than 25 characters.

      ```swift Swift
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
      paymentParam.userCredential = <#T##String#> // For saving and fetching user's saved card
      ```
      ```objectivec Objective-C
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

      > 📘 Note
      >
      > Use Core SDK library to generate payment post data.

      ***
    </Accordion>

    <Accordion title="Step 3: Initiate payment" icon="fa-code">
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

      <Callout icon="📘" theme="info">
        **Note**: Initiate payment must be on the Main thread.
      </Callout>

      #### Callbacks

      The list of the callback function provided by PayUOtpAssistCallback class:

      * `fun onPaymentSuccess(merchantResponse: String?, payUResponse: String?)`– Called when payment succeeds. merchantResponse:

      * `fun onPaymentFailure(merchantResponse: String?, payUResponse: String?)`– Called when a payment fails.

      * `fun onError(errorCode: String?, errorMessage: String?`)- Called when we got some error where,
        1. `errorCode`: Error Code
        2. `errorMessage`: Error Description

      * `fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest):` Boolean – It's an optional callback, override when you want to handle the Bank page redirection flow. You just need to change the return value to false. You can also open CustomBrowser in fallback scenarios. The following code snippet is used to open the CustomBrowser. For more information on using CustomBrowser, refer to [iOS CustomBrowser SDK](doc:ios-custombrowser-sdk).

      ```swift Swift
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
      | issuerUrl            | It's the Bank/ACS page Url.                                                                                                                           |
      | issuerPostData       | You need to load `issuerUrl` to the Webview along with this `issuerPostdata` string. Ex: `webView.postUrl`(`issuerUrl, issuerPostData.toByteArray()`) |
      | acsTemplate          | If` issuerUr`l is empty, you need to load acsTemplate to the Webview. Ex: `webView.loadData`(`acsTemplate, "text/html", "UTF-8"`);                    |

      <Accordion title="Error codes" icon="fa-code">
        | Error Code | Description                                              |
        | :--------- | :------------------------------------------------------- |
        | 1001       | No Internet                                              |
        | 1002       | Network timeout, please verify with your server.         |
        | 1003       | Gateway timeout, please verify with your server.         |
        | 1004       | The user canceled it, please verify with your server.    |
        | 1005       | Something went wrong, please verify with your server.    |
        | 1006       | The bank page timed out, please verify with your server. |

        ***
      </Accordion>
    </Accordion>
  </Accordion>

  <Accordion title="Step 4: Verify the transaction" icon="fa-code">
    After you get the response from SDK, make sure to confirm it with the PayU server.

    <Callout icon="🚧" theme="warn">
      **Remember**: It is recommended to implement the PayU Webhook or backend verify call from your backend. For more information, refer to [Webhooks](doc:webhooks-copy).
    </Callout>

    <Accordion title="Implementation of Verify Payment API" icon="fa-code">
      Since you already have the txnID (Order ID generated at your end) value for such cases, you simply need to execute the verify\_payment API with the necessary input parameters. The output would return you the transaction status in the `status` key and various other parameters also. For more information, refer to the <Anchor label="Verify Payment Status " target="_blank" href="ref:verify_payment_api">Verify Payment Status </Anchor>API.

      Endpoint URL: [https://info.payu.in/merchant/postservice.php?form=2](https://info.payu.in/merchant/postservice.php?form=2)

      **Sample Request**

      ```curl Curl
      curl --location --request POST '{{Url}}' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'key={merchantKey}' \
      --data-urlencode 'command=verify_payment' \
      --data-urlencode 'hash=c6febddfaaf6986dd8bd982d3769f856ab149e4de92dbad995c8df808ffcfbcb2c227a3fae38b69eb39ad7b6ce4e06e6b12289f70cc500cea5a2cda449c7dcba' \
      --data-urlencode 'var1=Txn1234'
      ```
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="Step 2. Test the Integration and Go-Live" icon="fa-code">
## Test the integration and Go-Live

<IOS_Test_the_Integration />

<IOS_Go_Live />
</Accordion>
