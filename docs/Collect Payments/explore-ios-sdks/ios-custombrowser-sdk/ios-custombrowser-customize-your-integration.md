---
title: Customize your Integration
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
---
title: Customize your Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Customize PayU Custom Browser on iOS: WebView checkout UI, payment modes, branding, and Custom Browser SDK configuration options.
  keywords:
    - payu ios custom browser sdk customize integration guide
    - ios custom browser payment gateway sdk customization payu
    - integrate custom browser ios app webview checkout payu
    - iphone payment sdk custom browser customize payu india
    - payment gateway ios custom browser sdk integration payu
    - payu ios custombrowser sdk ui branding configuration
    - mobile payment sdk ios custom browser integration steps
    - ios webview payment integration custom browser payu sdk
    - payu custom browser ios sdk developer customization guide
    - native ios custom browser payment integration payu gateway
    - ios in app payment custom browser sdk integration payu
    - swift ios custom browser payment sdk integration india
  robots: index
next:
  description: ''
---
After the basic payment collection is done, you can improve success rates and provide a better user experience with CB. There are many features that are provided along with CB. To use them, you need to create the `PUCBConfiguration` object.

```Text Objective-C
PUCBConfiguration *cbConfig = [PUCBConfiguration getSingletonInstance];
```

In the `PUCBConfiguration` object, you can let CB know which feature you would want to use. Ensure that you create a configuration object before creating the `PUCBWebVC` object. After you create this object, you can perform the following customization:

* ~~Review Order (Deprecated)~~
* ~~SurePay (Deprecated)~~
* Miscellaneous Configuration

> 📘 Note:
>
> Review Order and SurePay features are deprecated from v9.0.0 onwards.

## Miscellaneous configuration

You need to make an instance of PUCBConfiguration. This is a singleton class. The following configuration is available to be customized for Custom Browser:

* **merchantResponseTimeout**: The merchant response timeout value is configured in seconds. This is the maximum time for which CB waits for your success URL (surl)/ failure URL (furl) to give the response back to CB. Its default value is 5. CB forwards this response to your app immediately. If CB does not get any response within the time stipulated by merchantResponseTimeout, it sends nil as the response in the callbacks.
* **enableWKWebView**: By default, this flag is disabled or set to NO. If set to use, CB internally uses WKWebView to carry out the transaction. It is recommended to set it to YES as its memory footprint is far less than UIWebView.
* **merchantKey**: It is the merchant identifier (key) given to you by PayU
* **transactionId**: Set the ID of your current transaction.
* **isMagicRetry**: By default, this flag is enabled or set to YES by default. You can choose to disable it. If this flag is set to YES, try to increase the success rate of a transaction if the internet connection was lost while making payment.
* **isAutoOTPSelect**: By default, this flag is set to NO. You can choose to select it if you want to always select OTP as a method of authentication on the bank page.
* **isAutoOTPSubmit**: By default, this flag is set to NO. You can choose to submit the OTP automatically whenever you will tap the auto-detected OTP that comes in the keyboard.

The sample code block for the above settings:

```Text Objective-C
cbConfig.merchantResponseTimeout = 30;
cbConfig.enableWKWebView = 'YES';
cbConfig.merchantKey = @”gtKFFx”   //your merchant key here
cbConfig.transactionId = self.paymentParam.transactionID;   //give transaction id to cbConfig
cbConfig.isMagicRetry = YES;
cbConfig.isAutoOTPSelect = NO;
cbConfig.isAutoOTPSubmit = YES;
```