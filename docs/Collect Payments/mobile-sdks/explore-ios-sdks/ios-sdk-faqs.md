---
title: FAQs - iOS SDK
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
## PayU Checkout Pro

#### What are the customization options available for PayU Checkout Pro SDK for iOS?

**Answer**: PayU offers the following customization options:

* Customizing the PayU payment page's look and feel to match the merchant's branding
* Integrating with the merchant's own payment gateway or payment service provider
* Implementing custom payment methods or gateways not supported by PayU Checkout Pro SDK
* Implementing custom payment flows, such as split payments or installment payments

***

#### How can I customize the look and feel of the PayU payment page in iOS SDK?

**Answer**: The PayU payment page's look and feel can be customized using PayU Dashboard or customiseUIWithPrimaryColor config. Merchants can customize the page's layout, fonts, colors, and other visual elements to match their branding. For more information, refer to any of the following:

* [Using Dashboard
* Advanced Integration for iOS > Change Theme

***

#### Can I integrate PayU Checkout Pro SDK with my own payment gateway or payment service provider in iOS SDK?

**Answer**: Yes, PayU Checkout Pro SDK can be integrated with any payment gateway or service provider. Merchants can use the SDK to capture and process payment information and then send it to their own backend system for processing.

***

#### How can I implement custom payment methods or gateways not supported by PayU Checkout Pro SDK in iOS SDK?

**Answer**: Custom payment methods can be implemented using the PayU Custom Checkout SDK. This SDK provides a flexible and extensible framework for integrating with any payment method or gateway.

***

#### Can I implement custom payment flows using PayU Checkout Pro SDK in iOS SDK?

**Answer**: Yes, custom payment flows can be implemented using the SDK's flexible API. Merchants can use the API to implement complex payment flows, such as split payments, installment payments, or any other custom payment flow required for their business.

***

#### What is the difference between a "basic" and "advanced" integration with PayUCheckoutPro?

**Answer**: A basic integration involves using the pre-built user interface components provided by the PayUCheckoutPro SDK to collect payment information from the user. An advanced integration, on the other hand, allows developers to customize the payment flow and user interface using their own code and design, while still leveraging the underlying functionality provided by the SDK.

***

#### What are some benefits of PayU CheckoutPro Advanced Integration?

**Answer**: Some benefits of an Advanced Integration include greater flexibility and control over the payment flow and user interface, the ability to customize the payment experience to match the branding and design of the app, and the potential for improved conversion rates and user engagement. It offers the following customizations:

* Enable Offer
* Change Theme
* Configure Merchant Name & Logo
* Hide Checkout Screen Back Button dialog box
* Hide the Back button dialog box after Payment Initialisation
* Auto Select OTP
* Auto Submit OTP
* Configure Merchant Response Timeout
* Review Order
* Additional Payment options on the Checkout screen
* Configure Checkout Payment Modes Order
* Set Native OTP Assist
* Enforced Payment Modes

***

#### What is Server-to-Server integration, and how does it differ from client-side integration?

**Answer**: A server-to-server integration involves communicating with the PayU API directly from the app's or website's backend server, rather than from the client-side code running on the user's device. This can provide greater security and control over the payment process, as well as the ability to process payments without requiring the user to enter payment information directly into the app. For more information, refer to Server-to-Server Integration.

***

#### What is a Webhook, and how is it used in the PayUCheckoutPro integration?

**Answer**: A webhook is a way for the PayU server to send a notification to the app's backend server when certain events occur, such as a successful payment or a refund request. The app's backend server can then use this information to update its own database or trigger additional actions. Webhooks are used in the advanced integration to provide more fine-grained control over the payment process and to enable custom workflows and integrations. For more information, refer to Webhooks.

## Hashing

#### How do I set up payment hashes for my iOS app?

**Answer**: The process involves generating a secret key and using it to calculate the payment hashes for each transaction. For more information, refer to Set up the Payment Hashes.

***

#### What happens if the payment hash is incorrect or missing?

**Answer**: If the payment hash is incorrect or missing, the PayU server will reject the payment request and return an error code. This can result in the user being unable to complete the payment and may require them to restart the payment process or contact customer support.

***

#### Can I use the same secret key for multiple transactions?

**Answer**: No, it is recommended to use a different secret key for each transaction to ensure maximum security. Using the same key for multiple transactions can make it easier for attackers to compromise the security of the payment system.

***

#### What are some best practices for securing payment hashes and secret keys?

**Answer**: Some best practices for securing payment hashes and secret keys include storing them in a secure location, such as a keychain or secure file, using strong encryption algorithms, and limiting access to only authorized personnel. It is also recommended to periodically rotate the secret key to prevent it from being compromised over time.

## MCP Integration

#### What is MCP integration, and why is it useful?

**Answer**: MCP integration allows merchants to accept payments from multiple payment methods through a single integration with PayU. This can be useful for streamlining the payment process for customers and reducing the complexity of payment integrations for merchants.

***

#### How do I set up MCP integration for my iOS app?

**Answer**: The process involves configuring the SDK to accept multiple payment methods and handling the response from the PayU server to determine the success or failure of the payment. For more information, refer to MCP Integration for iOS.

***

#### What payment methods are supported by MCP integration?

**Answer**: MCP integration supports a variety of payment methods, including Credit and Debit cards, Net Banking, Wallets, and UPI. The specific payment methods supported may vary depending on the region and country.

***

#### How do I handle errors or exceptions during MCP integration?

**Answer**: The PayUCheckoutPro SDK provides error-handling mechanisms to help you handle exceptions or errors that may occur during the payment process. For more information, refer to MCP Integration for iOS.

## CocoaPods Integration

#### What is CocoaPods, and why is it useful for iOS development?

**Answer**: CocoaPods is a dependency manager for iOS projects that make it easy to include and manage third-party libraries and frameworks. It helps to simplify the process of integrating external dependencies into an iOS project and also provides features such as versioning and dependency resolution.

***

#### How do I integrate the PayUCheckoutPro SDK with CocoaPods?

**Answer**: The process involves adding the PayUCheckoutPro pod to your project's Podfile and running the pod install command to download and install the SDK. For more information, refer to CocoaPods Integration.

***

#### What are some best practices for managing dependencies with CocoaPods?

**Answer**: Some best practices for managing dependencies with CocoaPods include regularly updating your Podfile to ensure that you are using the latest versions of libraries and frameworks, using specific version numbers to ensure consistency across development environments, and setting up a private repository or cache to reduce dependency on external servers.

***

#### Can I customize the PayUCheckoutPro SDK after integrating it with CocoaPods?

**Answer**: Yes, after integrating the PayUCheckoutPro SDK with CocoaPods, you can customize various aspects of the SDK, such as the look and feel of the payment page, the payment methods supported, and the error handling mechanisms. The PayUCheckoutPro SDK provides a variety of customization options that can be configured through code.

***

#### How do I troubleshoot issues with CocoaPods integration?

**Answer**: If you encounter issues with CocoaPods integration, you can try some common troubleshooting steps, such as running the pod update command to ensure that you are using the latest version of the SDK, checking for conflicts with other dependencies, and verifying that your project's build settings are configured correctly. For more information on troubleshooting tips and resources, refer to CocoaPods Integration.

***

#### Can I use CocoaPods to manage other dependencies in addition to the PayUCheckoutPro SDK?

**Answer**:Yes, CocoaPods can be used to manage a wide variety of dependencies in addition to the PayUCheckoutPro SDK. Many third-party libraries and frameworks are available as CocoaPods, making it easy to integrate and manage external dependencies in your iOS project.

***

#### How to fix the build error after adding the PayU framework through pods?

```
dyld: Library not loaded: @rpath/SocketIO.framework/SocketIO
  Referenced from: /Users/umang.arya/Library/Developer/CoreSimulator/Devices/DE6170BD-7841-496B-B533-F22AE109FEB6/data/Containers/Bundle/Application/2540A914-43AA-45B4-A71E-5559942E3B94/app.app/Frameworks/PayUCheckoutProKit.framework/PayUCheckoutProKit
  Reason: image not found
```

Currently, PayU's frameworks are dynamic framework. If you are not using 'use_frameworks!', add the following code block at the end of your `podfile`.

```
  $dynamic_framework = ['PayUAssetLibraryKit', 'PayUBizCoreKit', 'PayUCheckoutProBaseKit', 'PayUCheckoutProKit', 'PayUCustomBrowser', 'PayULoggerKit', 'PayUNetworkingKit', 'PayUUPICoreKit', 'PayUUPIKit', 'Socket.IO-Client-Swift', 'Starscream', 'PayUOlaMoneySDK']
  pre_install do |installer|
    Pod::Installer::Xcode::TargetValidator.send(:define_method, :verify_no_static_framework_transitive_dependencies) {}
    installer.pod_targets.each do |pod|
      if $dynamic_framework.include?(pod.name)
        def pod.build_type;
        Pod::BuildType.dynamic_framework
      end
    end
  end
end
```

## UPI

#### When UPI Transaction getting failed with the following error message, what is the resolution to it?

**Answer**:

<Image align="center" border={false} width="150px" src="https://files.readme.io/907d2ed-Screenshot_2023-08-12_at_11.17.41_PM.png" />

Contact your Key Account manager and request to enable the txn_s2s_flow flag from the merchant panel.

#### If the app crash for the following reason, what could be a possible solution to it?

**Answer**:

```
Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[****.AppDelegate-93491BB4-2FFA-4DF5-9DEC-8F510DA9306F window]: unrecognized selector sent to instance 0x600001574480
```

You might be using `SceneDelegate` in your app, use `AppDelegate` instead.

#### How do I enable UPI Intent Flow in my iOS SDK integration?

**Answer**:  Add the query schemes in `info.plist` similar to the following code block. For more information, refer to the iOS SDK Integration guide.

```
<key>LSApplicationQueriesSchemes</key>
<array>
<string>phonepe</string>
<string>tez</string>
<string>paytm</string>
</array>
```

#### In the response, the error code in the callback does not indicate the actual reason for failure. Which other parameter's value in response has the status?

**Answer**: The `field9` & `error_message` parameter in the response has the actual reason. For more information on the `error_message` list, refer to the Error Codes.
