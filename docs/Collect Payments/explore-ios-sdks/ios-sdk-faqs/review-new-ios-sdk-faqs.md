---
title: '[Review] New iOS SDK FAQs'
deprecated: false
hidden: true
metadata:
  robots: index
---
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
## Getting Started

#### What are the minimum requirements for integrating PayU iOS SDK?

**Answer**: The minimum requirements include:

* Xcode (latest version recommended)
* iOS Deployment Target: iOS 13.0 or higher (iOS 15.0+ recommended)
* Swift 5.0+ or Objective-C
* macOS compatible with Xcode requirements
* CocoaPods or Swift Package Manager for dependency management
* Internet permission in your app's Info.plist

For specific version requirements, refer to the integration documentation for the SDK you're using.

***

#### How do I get started with PayU iOS SDK integration?

**Answer**: To get started:

1. Register your application on the PayU developer dashboard
2. Obtain your Merchant Key and Salt from the dashboard
3. Choose your integration method (CocoaPods or Swift Package Manager)
4. Download and integrate the PayU iOS SDK into your project
5. Configure the SDK with your credentials
6. Test the integration using test credentials

For detailed steps, refer to the integration guide for your chosen SDK.

***

#### What is the difference between CocoaPods and Swift Package Manager for iOS SDK integration?

**Answer**: Both are dependency managers for iOS:

* **CocoaPods**: Traditional dependency manager, uses Podfile, requires `pod install` command
* **Swift Package Manager (SPM)**: Native to Xcode, integrated directly in Xcode, no external tools needed

PayU iOS SDK supports both methods. Choose based on your project's existing setup and preferences.

***

#### Do I need to use AppDelegate or SceneDelegate for PayU iOS SDK?

**Answer**: PayU iOS SDK works with both AppDelegate and SceneDelegate. However, if you encounter crashes related to window property, ensure you're using AppDelegate properly. Some SDK features may require AppDelegate configuration.

***

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

## Testing and Development

#### How do I test PayU iOS SDK integration without making real payments?

**Answer**: You can test using:

1. **Test Environment**: Use Test Key and Test Salt from your PayU dashboard
2. **Test Cards**: Use test card numbers provided in PayU documentation
3. **Test UPI IDs**: Use test UPI IDs for UPI payment testing
4. **Test Wallets**: Use test wallet credentials
5. **Sandbox Mode**: Configure the SDK for test environment

For test credentials, refer to [Test Cards, UPI ID and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).

***

#### Can I test PayU iOS SDK integration on an iOS Simulator?

**Answer**: Yes, you can test on an iOS Simulator. However, note that:

1. Some payment methods (like UPI apps) may not work on simulators
2. Network-related testing should work fine
3. For UPI and wallet testing, you may need a physical device
4. Ensure the simulator has proper network configuration
5. Some SDK features may require physical device testing

***

#### How do I enable debug logging for PayU iOS SDK?

**Answer**: Debug logging can be enabled by:

1. Setting appropriate log levels in your app
2. Checking Xcode console for SDK logs
3. Enabling verbose logging in development builds
4. Using PayU's debugging tools if available

Note: Disable verbose logging in production builds for security and performance.

***

#### What test scenarios should I cover before going live?

**Answer**: Before going live, test:

1. All payment methods (cards, UPI, net banking, wallets)
2. Success and failure scenarios
3. Network connectivity issues
4. App backgrounding during payment
5. Payment cancellation
6. Hash validation
7. Callback handling (surl/furl)
8. Error handling and user feedback
9. Different iOS versions and devices
10. Edge cases and error conditions

## Troubleshooting

#### Why am I getting "Library not loaded" error after adding PayU framework through CocoaPods?

**Answer**: This error occurs because PayU's frameworks are dynamic frameworks. If you're not using `use_frameworks!`, add the following code block at the end of your `Podfile`:

```ruby
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

This configuration ensures that PayU's dynamic frameworks are properly handled in your CocoaPods setup.

***

#### What should I do if the payment page is not loading in my iOS app?

**Answer**: If the payment page is not loading, check the following:

1. Verify your internet connection and permissions in Info.plist
2. Ensure you're using the correct environment (test/production) with matching Key and Salt
3. Check if the hash is generated correctly on your server
4. Verify that all required parameters are being passed correctly
5. Check the Xcode console for any error messages
6. Ensure your app has the necessary network security configuration
7. Verify CocoaPods/Swift Package Manager integration is correct

***

#### How do I handle payment failures in iOS SDK?

**Answer**: Payment failures can be handled through:

1. **Callback methods**: Implement the payment result callbacks to receive success/failure responses
2. **Error codes**: Check the error codes in the response to identify the specific failure reason
3. **Error messages**: Use `field9` and `error_message` parameters for detailed error information
4. **User feedback**: Display appropriate error messages to users based on the error code
5. **Retry mechanism**: Allow users to retry the payment if the failure is due to network or temporary issues

For detailed error handling, refer to [Error Handling](https://docs.payu.in/docs/error-handling).

***

#### What should I do if the SDK is not responding or payment page is blank?

**Answer**: If the SDK is not responding or showing a blank page:

1. Check your internet connection and network permissions
2. Verify that all required parameters are being passed correctly
3. Ensure the hash is generated correctly and matches the parameters
4. Check Xcode console for any error messages
5. Verify you're using the correct environment (test/production)
6. Try clearing app cache and data
7. Ensure you're using a supported iOS version
8. Verify CocoaPods/Swift Package Manager dependencies are properly installed

***

#### Why am I not receiving payment callbacks (surl/furl) in my iOS app?

**Answer**: If you're not receiving payment callbacks:

1. Verify that `surl` and `furl` are correctly configured in your payment request
2. Ensure your app can handle URL schemes or deep links
3. Check Info.plist for proper URL scheme configuration
4. Verify that your server endpoints are accessible and responding
5. For UPI Intent flow, note that callbacks may be handled differently
6. Check if the app was closed during payment - implement proper state handling
7. Verify AppDelegate or SceneDelegate is properly configured

***

#### How do I resolve dependency conflicts when integrating PayU iOS SDK?

**Answer**: If you encounter dependency conflicts:

1. Check the SDK documentation for required dependency versions
2. Use CocoaPods' dependency resolution strategies
3. Update your project's dependencies to compatible versions
4. Use `pod update` to update dependencies
5. Check for conflicts with other CocoaPods or Swift Package Manager dependencies
6. Contact PayU Support if conflicts persist

***

#### What should I do if payment transactions are failing with authentication errors?

**Answer**: If you're getting authentication errors:

1. Verify your Merchant Key and Salt are correct
2. Ensure the hash is generated correctly on your server
3. Check that you're using the correct environment (test/production)
4. Verify all required authentication parameters are included
5. Ensure your account is activated and in good standing
6. Check if there are any account-level restrictions
7. Verify hash generation formula and parameter order

***

#### Why are UPI payments not working in my iOS app?

**Answer**: If UPI payments are not working:

1. Verify UPI SDK is properly integrated
2. Check if UPI apps are installed on the device
3. Ensure VPA is provided for UPI Collect flow
4. Verify UPI is enabled for your merchant account
5. Check device compatibility and iOS version
6. Ensure `LSApplicationQueriesSchemes` is configured in Info.plist
7. Contact your Key Account Manager to enable `txn_s2s_flow` flag if needed
8. Review UPI integration documentation for specific requirements

## SDK Compatibility and Requirements

#### What is the minimum iOS version required for PayU iOS SDK?

**Answer**: The minimum iOS version (deployment target) varies by SDK:

* **CheckoutPro SDK**: iOS 13.0 or higher (iOS 15.0+ recommended)
* **Core SDK**: Check the specific SDK documentation for minimum iOS version
* **UPI SDK**: iOS 13.0 or higher
* **CustomBrowser SDK**: Check version-specific requirements

Refer to the specific SDK integration documentation for exact requirements.

***

#### Is PayU iOS SDK compatible with Swift and Objective-C?

**Answer**: Yes, PayU iOS SDK is compatible with both Swift and Objective-C. The SDK provides APIs that work with both languages. When using Swift, you may need to configure a bridging header for Objective-C components.

***

#### Can I use PayU iOS SDK with SwiftUI?

**Answer**: PayU iOS SDK is built using UIKit. While you can use it in a SwiftUI project, you'll need to use `UIViewControllerRepresentable` to embed the SDK's UI components. The SDK's payment flows will still use the UIKit system.

***

#### Does PayU iOS SDK support Swift Package Manager?

**Answer**: Yes, PayU iOS SDK supports Swift Package Manager (SPM). You can integrate the SDK using SPM by adding the package URL in Xcode or through Package.swift. Some SDKs may also support CocoaPods.

***

#### What permissions are required for PayU iOS SDK?

**Answer**: The required permissions typically include:

* Network access (configured in Info.plist with App Transport Security settings)
* URL schemes for payment callbacks (configured in Info.plist)

Some payment methods may require additional permissions:
* UPI payments may require specific URL schemes in `LSApplicationQueriesSchemes`
* Location permissions for certain features (if applicable)

Add these configurations in your `Info.plist` file.

***

#### Can I use PayU iOS SDK in a multi-target iOS project?

**Answer**: Yes, you can use PayU iOS SDK in a multi-target project. Add the SDK dependency to the targets where you'll be using it, or add it to a shared target if multiple targets need access. Ensure proper dependency management across targets.

## Security

#### Is it safe to store Merchant Key and Salt in my iOS app?

**Answer**: No, it is not safe to store Merchant Key and Salt in your iOS app. These credentials should be kept on your server. Always generate hashes on your server and pass them to the iOS app. Storing credentials in the app makes them vulnerable to reverse engineering.

***

#### How can I ensure secure payment processing with PayU iOS SDK?

**Answer**: To ensure secure payment processing:

1. Generate hashes on your server, not in the app
2. Never store Merchant Key and Salt in the app
3. Use HTTPS for all network communications
4. Configure App Transport Security (ATS) properly
5. Validate payment responses using reverse hash verification
6. Use code obfuscation if available
7. Keep the SDK updated to the latest version
8. Follow iOS security best practices
9. Use Keychain for any sensitive data storage if needed

***

#### Does PayU iOS SDK handle PCI-DSS compliance?

**Answer**: Yes, PayU CheckoutPro SDK is PCI-DSS compliant. When using CheckoutPro SDK, card details are handled by PayU's secure payment pages, so you don't need PCI-DSS certification. However, if you collect card details directly in your app, you'll need PCI-DSS certification.

***

#### How does PayU iOS SDK protect sensitive payment data?

**Answer**: PayU iOS SDK protects sensitive data by:

1. Using encrypted communication channels (HTTPS/TLS)
2. Not storing sensitive payment information locally
3. Using secure tokenization for saved payment methods
4. Implementing secure hash-based authentication
5. Following industry-standard security practices
6. Complying with iOS security guidelines

***

#### Can I implement additional security measures on top of PayU iOS SDK?

**Answer**: Yes, you can implement additional security measures:

1. Implement certificate pinning at the app level
2. Add additional validation layers
3. Implement fraud detection mechanisms
4. Use Keychain for secure storage of app-specific data
5. Implement proper session management
6. Add logging and monitoring for security events
7. Use code obfuscation tools

## Upgrade

#### How much time does it take to update the SDK in code to upgrade to the latest version of SDK?

**Answer**: To update the SDK it takes only 5 – 10 mins. If you are facing any issues in updating the SDK, you can contact [PayU Support](https://help.payu.in/).

***

#### How do I upgrade to the latest version of PayU iOS SDK?

**Answer**: To upgrade to the latest version:

1. Update the SDK version in your Podfile or Swift Package Manager
2. Run `pod update` for CocoaPods or update package in Xcode for SPM
3. Review the release notes for breaking changes
4. Update your code if there are any API changes
5. Test thoroughly in the test environment before going live
6. Update any customizations if they're affected by the upgrade

Check the SDK's version history or changelog for specific upgrade instructions.

***

#### What should I check before upgrading the PayU iOS SDK?

**Answer**: Before upgrading:

1. Review the release notes and changelog for the new version
2. Check for any deprecated methods or breaking changes
3. Verify compatibility with your current iOS and Xcode versions
4. Test the upgrade in a development environment first
5. Backup your current implementation
6. Check if any customizations need to be updated
7. Review migration guides if available
8. Ensure all dependencies are compatible

***

#### Will upgrading the SDK affect my existing integrations?

**Answer**: Upgrading the SDK may affect your integration if:

1. There are breaking changes in the API
2. Required parameters have changed
3. Callback methods have been modified
4. Dependencies have been updated
5. Minimum iOS version requirements have changed

Always review the release notes and test thoroughly before deploying to production. Most minor version updates are backward compatible, but major version updates may require code changes.

## General Questions

#### What is the amount data format in PayU iOS SDK?

**Answer**: In PayU SDK, always pass String value in amount field for iOS and Android.

***

#### Can I generate hashes on my iOS app?

**Answer**: PayU recommends you generate the hashes on your server. Do not generate the hashes locally in your app as it will compromise the security of the transactions.

***

#### Should I make a payment request using the Payment (_payment) API for iOS?

**Answer**: You need not use the Payment API if you are using PayU Mobile SDK, as PayU Mobile SDK will call all the APIs internally.

***

#### Should I use the customer's VPA to enable users to make payments through any UPI app installed on his/her mobile?

**Answer**: If you want to use collect flow, it is mandatory to enter VPA, otherwise, it is not required.

***

#### How do I switch between test and production environments in iOS SDK?

**Answer**: To switch between test and production environments:

1. Use Test Key and Test Salt for testing, and Production Key and Salt for production
2. Configure the SDK environment accordingly
3. Ensure you're using the correct API endpoints for each environment
4. Test thoroughly in test environment before switching to production

***

#### What payment methods require additional setup or configuration?

**Answer**: Some payment methods may require additional setup:

* **UPI**: May require VPA for collect flow and `LSApplicationQueriesSchemes` for intent flow
* **Google Pay**: Requires S2S (Server-to-Server) integration flag to be enabled
* **PhonePe**: Requires specific SDK integration and URL schemes
* **EMI**: Requires bank and card eligibility checks
* **BNPL**: Requires merchant approval and configuration

Contact your PayU Key Account Manager for enabling specific payment methods.

***

#### How do I debug issues with PayU iOS SDK integration?

**Answer**: To debug integration issues:

1. Enable logging in your app to see SDK logs
2. Check the Xcode console for error messages
3. Verify all parameters being sent to the SDK
4. Test with PayU's test credentials first
5. Use PayU's hash generation tool to verify hash calculations
6. Check network requests and responses
7. Review the integration documentation for common issues
8. Contact PayU Support with specific error codes and logs

***

#### Can I use multiple PayU SDKs together in the same iOS app?

**Answer**: Yes, you can use multiple PayU SDKs together, such as:

* CheckoutPro SDK with UPI SDK
* CheckoutPro SDK with Google Pay SDK
* Core SDK with CustomBrowser SDK

Ensure you follow the integration steps for each SDK and handle conflicts in dependencies if any. Refer to the specific SDK documentation for compatibility information.

***

#### What is the difference between static hash and dynamic hash in iOS SDK?

**Answer**:

* **Static Hash**: Generated once and can be reused for multiple transactions. Used for certain payment flows but less secure.
* **Dynamic Hash**: Generated fresh for each transaction with transaction-specific parameters. More secure and recommended for production use.

PayU recommends using dynamic hash for better security. For more information, refer to the hash generation documentation.

***

#### How do I handle deep links or URL schemes after payment in iOS SDK?

**Answer**: Deep links and URL schemes are handled through:

1. **surl (Success URL)**: Called when payment is successful
2. **furl (Failure URL)**: Called when payment fails
3. **URL Schemes**: Configure Info.plist to handle payment callbacks
4. **AppDelegate/SceneDelegate**: Implement URL handling methods

For detailed implementation, refer to the iOS SDK integration documentation.

***

#### What should I do if I receive an invalid hash error?

**Answer**: If you receive an invalid hash error:

1. Verify that you're using the correct Key and Salt (test vs production)
2. Ensure the hash is generated on your server, not in the app
3. Check that all parameters used in hash generation match the parameters sent to PayU
4. Verify the hash generation formula and parameter order
5. Use PayU's hash generation tool to test your hash calculation
6. Ensure there are no extra spaces or encoding issues in parameters

***

#### Can I customize the payment success/failure messages in iOS SDK?

**Answer**: Yes, you can customize payment success/failure messages:

1. Handle the payment callbacks in your app
2. Display custom messages based on the payment response
3. Use the SDK's customization options to modify the UI
4. Implement your own error handling and user feedback

The SDK provides callbacks that you can use to show custom messages to users.
