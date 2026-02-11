---
title: '[Review]New Android SDK FAQs'
deprecated: false
hidden: true
metadata:
  robots: index
---
## Getting Started

* **I am getting a build error after adding PayUCheckoutPro SDK gradle dependency. How do I fix it?**

If you encounter a build error similar to the following after adding the PayUCheckoutPro SDK gradle dependency:

```
Task :app:compileDebugJavaWithJavac FAILED
Execution failed for task ':app:compileDebugJavaWithJavac'.
> Compilation failed; see the compiler error output for details.
```

Try upgrading your Gradle version. Update the line in your `build.gradle` file:

```gradle
classpath 'com.android.tools.build:gradle:4.1.0'
```

Upgrade to a newer version like `4.2.0` or higher. Also ensure your Java version is compatible with the Gradle version you're using.

* **I am getting a Java compiler exception when compiling my Android implementation. What should I do?**

If you encounter an exception like:

```
java.lang.AssertionError: annotationType(): unrecognized Attribute name MODULE
```

This typically indicates a Java version compatibility issue. Try upgrading your Gradle version. Update the line:

```gradle
classpath 'com.android.tools.build:gradle:4.1.0'
```

Upgrade to a newer version and ensure your Java Development Kit (JDK) version is compatible with the Gradle version.

* **What are the minimum requirements for integrating PayU Android SDK?**

The minimum requirements include:
- Android Studio with Gradle build system
- Minimum Android SDK version (API level) as specified in the SDK documentation
- Java Development Kit (JDK) compatible with your Gradle version
- Internet permission in your AndroidManifest.xml

For specific version requirements, refer to the integration documentation for the SDK you're using.

* **How do I get started with PayU Android SDK integration?**

To get started:
1. Register your application on the PayU developer dashboard
2. Obtain your Merchant Key and Salt from the dashboard
3. Download and integrate the PayU Android SDK into your project
4. Configure the SDK with your credentials
5. Test the integration using test credentials

For detailed steps, refer to the integration guide for your chosen SDK.

## Key/Salt

* **I am facing the following error while trying to integrate Android Mobile SDK.**

Value \<!DOCTYPE of type java.lang.String cannot be converted to JSONObject (Error code 5014)

If you are using Test Key & Test Salt, configure the **setIsProduction** parameter as false. Otherwise, if you are using Production Key and Salt, configure the **setIsProduction** parameter as true. For more information, refer to [CheckoutPro SDK go-live checklist](https://docs.payu.in/docs/android-checkoutpro-golive-checklist).

## **PayU CheckoutPro**

### **General**

* **Is PayU CheckoutPro for Mobile SDK PCI-DSS compliant?**

Yes, PayU CheckoutPro for Mobile SDK is PCI-DSS compliant, ensuring secure payment processing for your mobile app users.

* **PayU Android SDK has various SDKs and how do I choose them for my app?**

The best SDK for you will depend on your specific needs and requirements.

The [Choose your SDK](https://docs.payu.in/docs/explore-android-sdks#choose-your-integration) table in the explore android SDK document outlines the process you need to follow and decide which SDK to use for your app, based on your specific needs and requirements.

* **What are the different customization options available for PayU Checkout Pro SDK for Android?**

There are several customization options available, including:

* Customizing the PayU payment page’s look and feel to match your app branding
* Integrating with the payment gateway or payment service provider
* Implementing custom payment flows, such as split payments or installment payments

For more information, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).

* **Can I customize the payment modes in PayU Checkout Pro?**
  Yes, you can customize the payment modes. For more information, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).
* **How can I modify the color scheme in Android SDK integration?**

You can modify the color scheme and theme used in the PayUCheckoutPro SDK by providing your own set of colors. For more information on how to change the color theme of the SDK, refer to [Modify Theme](https://docs.payu.in/docs/android-checkoutpro-custom-integrations#modify-theme).

* **How can I customize the look and feel of the PayU payment page?**

The PayU payment page’s look and feel can be customized using CSS stylesheets and JavaScript. You can customize the page’s layout, fonts, colors, and other visual elements to match their branding. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **Can I integrate PayU Checkout Pro SDK with my own payment gateway or payment service provider?**

Yes, PayU Checkout Pro SDK can be integrated with any payment gateway or service provider. You can use the SDK to capture and process payment information and then send it to their own backend system for processing. For more information, refer to [Customize your Integration](https://docs.payu.in/docs/android-checkoutpro-custom-integrations).

* **How can I implement custom payment methods or gateways not supported by PayU Checkout Pro SDK?**

Custom payment methods or gateways can be implemented using the PayU Custom Checkout SDK. This SDK provides a flexible and extensible framework for integrating with any payment method or gateway. For more information, refer to [Customize Your Integration](https://docs.payu.in/docs/android-checkoutpro-custom-integrations).

* **Can I implement custom payment flows using PayU Checkout Pro SDK?**

Yes, custom payment flows can be implemented using the SDK’s flexible API. You can use the API to implement complex payment flows, such as split payments, installment payments, or any other custom payment flow required for their business.

* **What is the difference between the implementation of PayU CheckoutPro in the Android and Apple iOS platforms?**
  * **Development Environment**: The Android SDK requires Android Studio and Gradle to be installed, while the iOS SDK requires Xcode and CocoaPods to be installed.
  * **Language**: The Android SDK is written in Java, while the iOS SDK is written in Objective-C and Swift.
  * **Integration Method**: The Android SDK is integrated using the Gradle build system, while the iOS SDK is integrated using the CocoaPods dependency manager.
  * **UI Components**: The UI components used in the Android and iOS SDKs are different due to the differences in the platform’s design guidelines. For example, the Android SDK uses Android-specific UI components such as the EditText view, while the iOS SDK uses iOS-specific UI components such as the UITextField view.
  * **Payment Methods**: The payment methods supported by the Android and iOS SDKs are the same, including credit cards, debit cards, net banking, and UPI.
  * **Tokenization**: Both the Android and iOS SDKs support tokenization, which allows users to save their payment information for future transactions.
  * **Testing**: The Android SDK provides a test mode that allows developers to test the integration without making actual payments, while the iOS SDK provides a sandbox environment for testing.
* **What are the steps involved in integrating PayU CheckoutPro for Mobile SDK?**

The integration process involves registering your application on the PayU developer dashboard, downloading and integrating the PayU CheckoutPro Mobile SDK into your Android project, and then using the SDK to initiate and process payment requests from your mobile app.

* **What payment methods are supported by PayU CheckoutPro for Mobile SDK?**

PayU CheckoutPro for Mobile SDK supports multiple payment methods including credit/debit cards, UPI, Wallets, and Net Banking.

* **Does PayU SDK supports SSL Pinning?**

No, PayU SDKs does not support SSL Pinning due to business continuity.

* **Can I change the order of payment modes displayed on PayU Payment page that is implemented using CheckoutPro?**

Yes, you can change the order of payment modes displayed on the PayU Payment page by PayU either using SDK manually or using Dashboard. For more information, refer to:

* **Manually**: [Customize Your Integration](https://docs.payu.in/docs/android-checkoutpro-custom-integrations) > [Set Checkout Payment Modes Order](https://docs.payu.in/docs/android-checkoutpro-custom-integrations#set-checkout-payment-modes-order).
* **Dashboard**: [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).
* **Can I customize the PayU CheckoutPro for Mobile SDK UI to match my app’s design?**

Yes, PayU CheckoutPro for Mobile SDK provides a customizable UI that allows you to adjust the look and feel of the payment gateway to match your app’s design. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy#/).

* **What is Dynamic configuration in PayU Checkout Pro SDK for Android?**

Dynamic configuration allows you to update various payment-related settings in real-time using the PayU Dashboard. These settings can include payment methods, transaction limits, and other checkout-related parameters. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **What are the use cases for dynamic configuration in PayU Checkout Pro SDK for Android?**

Dynamic configuration can be useful in the following scenarios:

* Adding or removing payment methods based on user preferences or availability in different countries or regions.
* Changing transaction limits or fees based on business requirements or market conditions.
* Updating payment-related settings based on user feedback or analytics data.
* Configuring payment-related settings for testing and debugging purposes.

For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **How can I use Dynamic Configuration in PayU Checkout Pro SDK for Android?**

To use dynamic configuration, you can log in to the PayU Dashboard and update the relevant settings in the Checkout Pro section. The SDK will automatically fetch the updated settings and apply them to the payment flow. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy#/).

* **Can I update payment methods dynamically using the PayU Dashboard**?

Yes, payment methods can be added or removed dynamically using the Dashboard. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **What other payment-related settings can be updated dynamically using the Dashboard?**

Other payment-related settings that can be updated dynamically include transaction limits, payment fees, checkout flow settings, and more. These settings can be customized based on the your business requirements and market conditions. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **Can I customize the PayU CheckoutPro Mobile SDK without modifying the SDK code?**

Yes, PayU CheckoutPro Mobile SDK allows customization without modifying the SDK code. This is achieved by using the SDK’s XML and resource files to override the default UI elements. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **How do I customize the PayU CheckoutPro Mobile SDK for my Android app?**

To customize the PayU CheckoutPro Mobile SDK, you need to create an XML file that defines the custom styles and layouts, and then use the SDK’s resource files to override the default GUI elements. You can also customize the colors and images used in the payment screens.

* **Can I customize the PayU CheckoutPro Mobile SDK to match my app’s branding?**

Yes, you can customize the PayU CheckoutPro Mobile SDK to match your app’s branding by using your app’s color scheme, fonts, and logos in the payment screens. For more information, refer to [Dynamic Configuration using Dashboard](https://docs.payu.in/docs/dynamic-configuration-using-dashboard-copy).

* **What is the impact of customizing the PayU CheckoutPro Mobile SDK on future updates?**

If you customize the PayU CheckoutPro Mobile SDK, future updates to the SDK may require you to update your customizations as well. You should carefully review the release notes before updating to a new version of the SDK.

* **Is technical support available for customized integration with PayU CheckoutPro Mobile SDK?**

Yes, PayU provides technical support for customized integration with PayU CheckoutPro Mobile SDK. You can reach out to [PayU Support] (https://help.payu.in) for assistance with any customization issues or questions.

* **What is CustomBrowser Configuration?**

CustomBrowser Configuration is the process of configuring the PayU Mobile Android SDK to use a custom browser for payment processing.

* **How can I configure the PayU Mobile Android SDK to use a CustomBrowser?**

To configure the PayU Mobile Android SDK to use a custom browser, you need to implement the CustomBrowser class and configure the SDK to use this class for payment processing. For more information, refer to [Integration with CustomBrowser](https://docs.payu.in/docs/integration-steps-android-customer-browser).

* **What are the advantages of using a CustomBrowser for payment processing?**

Using a custom browser for payment processing provides a more seamless payment experience for the user, as the payment screens can be customized to match the look and feel of the app. For more information, refer to [Integration with CustomBrowser](https://docs.payu.in/docs/custom-browser-sdk/).

* **How does the CustomBrowser affect the security of payment processing?**

CustomBrowser does not affect the security of the payment processing, as the SDK still uses the same secure encryption and authentication mechanisms to process payment requests.

### **Convenience Fee**

* **What is a convenience fee in the context of payment processing?**

A convenience fee is an additional fee charged to customers for the convenience of using a particular payment method. It is often used to cover the costs of processing credit card payments, which can be more expensive for merchants than other payment methods. For more information, refer to [Convenience Fee Integration for Android](https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee#/).

* **How can I integrate a convenience fee using PayU Checkout Pro SDK for iOS?**

To integrate a convenience fee, you can use the SDK’s Convenience Fee API to add an additional fee to the payment amount based on the selected payment method. For more information, refer to [Convenience Fee Integration for Android](https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee).

* **Can I customize the convenience fee calculation logic using PayU Checkout Pro SDK for iOS?**

Yes, you can customize the convenience fee calculation logic based on their business requirements. The SDK provides a flexible API that allows you to set the convenience fee amount based on various criteria, such as the payment method selected, transaction amount, or customer location. For more information, refer to [Convenience Fee Integration for Android](https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee).

* **What are the different types of convenience fees that can be charged using PayU Checkout Pro SDK for iOS?**

You can charge convenience fees based on different criteria, such as:

* A percentage of the transaction amount
* A fixed amount per transaction
* A combination of both percentage and fixed-amount fees

For more information, refer to [Convenience Fee Integration for Android](https://docs.payu.in/docs/android-checkoutpro-setupconveniencefee).

* **How can I display the convenience fee to customers during the checkout process using PayU Checkout Pro SDK for iOS?**

The convenience fee amount can be displayed to customers on the payment page using the SDK’s convenience fee API. You can customize the display format and location of the convenience fee on the payment page to provide a transparent and seamless checkout experience for customers.

## **Hashing**

* **What is hashing?**

Hashing is a process of converting a string of data into a fixed-length string of characters. Hashing is used to generate a secure hash key that is sent along with payment information to ensure the transaction’s integrity.

* **How is the hash key generated in PayU?**

The hash key is generated using a hashing algorithm called SHA-512, which is a secure one-way hash function. The SDK takes all the transaction details and a merchant salt key as input and computes the hash key using the SHA-512 algorithm.

* **What is a merchant key and Salt in PayU Checkout Pro SDK?**

The merchant Key and Salt is a secret key provided by PayU to merchants, which is used in conjunction with the transaction details to generate the hash key. The Key and Salt must be kept secret and is not shared with anyone else.

* **How is reverse hashing used in PayU Checkout Pro SDK?**

Reverse hashing is used to verify the authenticity of the payment response received from PayU. The SDK computes the hash key using the same algorithm and merchant salt key used for generating the original hash key and compares it with the hash key received in the payment response. If they match, it confirms that the payment response is authentic.

* **What happens if the hash key generated by the SDK does not match the one received in the payment response?**

If the hash keys do not match, it indicates that the payment response has been tampered with or is not authentic. In such cases, the payment transaction should be rejected, and you should contact [PayU Support](https://help.payu.in/) for further assistance.

* **What is the formula used for hashing in PayU Checkout Pro SDK?**

The formula used for hashing in PayU Checkout Pro SDK is as follows:

```plaintext
hash_key = SHA512(transaction_details + '|' + merchant_salt)
```

* **What does the Hash calculation formula consist of?**

The formula consists of two main components:

* **Transaction details**: This includes all the relevant transaction details, such as the transaction amount, payment mode, currency, etc. These details are concatenated together in a specific format and used as input for the hashing algorithm.
* **Merchant Key and Salt**: This is a secret key provided by PayU to merchants, which is used to add an extra layer of security to the hashing process.
* **What is SHA512?**

SHA512 is a hashing algorithm that generates a fixed-length, 512-bit hash value from input data. It is a one-way function, meaning that the input cannot be retrieved from the output hash value.

* **Why is the tilde symbol (‘|’) used in the Hash calculation formula?**

The ‘|’ character is used as a separator between the transaction_details and the merchant_salt in the formula. This helps to ensure that the hashing algorithm processes the input data correctly and generates a consistent hash value.

## **Native OTP Integration**

* **What is Native OTP?**

Native OTP is a feature provided by PayU that allows the user to enter the OTP directly in the app, instead of being redirected to a third-party website or app for OTP verification.

* **How can I integrate Native OTP with PayU Android SDK?**

To integrate Native OTP with PayU Android SDK, you need to use the `setOtpFetchHandler` method provided by the SDK to fetch the OTP from the user and pass it to the SDK for verification.

* **Can I customize the Native OTP user interface in my app?**

Yes, you can customize the Native OTP user interface in your app by using the PayU Mobile Android SDK’s customization options.

* **Which payment methods support Native OTP integration with PayU Android SDK?**

PayU Android SDK supports Native OTP integration for the following payment modes:

* Credit Card
* Debit Card
* EMI (Credit Card or Debit Card)
* BNPL
* **Is there a limit to the number of attempts to enter OTP for verification?**

Yes, there is a limit to the number of attempts to enter OTP for verification. After a certain number of failed attempts, the transaction is declined.

* **Can I test the Native OTP integration before going live?**

Yes, you can test the Native OTP integration in a test environment before going live. PayU provides a test environment for testing the Native OTP integration.

## **UPI Integration**

* **How can I integrate UPI with PayU Android SDK?**

To integrate UPI with PayU Android SDK, you need to use the `setPaymentOption` method provided by the SDK to select UPI as the payment option and configure the UPI payment parameters.

* **Which UPI apps are supported by PayU Android SDK?**

PayU Android SDK supports all UPI apps that are compatible with the UPI payment system.

* **Can I customize the UPI payment user interface in my app?**

Yes, you can customize the UPI payment user interface in your app by using the PayU Mobile Android SDK’s customization options.

* **What are the different types of UPI transactions supported by PayU Android SDK?**

PayU Android SDK supports UPI transactions for sending money, requesting money, and checking the balance in the user’s bank account.

* **Is technical support available for UPI integration with PayU Android SDK?**

Yes, PayU provides technical support for UPI integration with PayU Android SDK. You can reach out to the [PayU support team] (https://help.payu.in) for assistance with any integration issues or questions.

* **Can I test the UPI integration before going live?**

Yes, you can test the UPI integration in a test environment before going live. PayU provides a test environment for testing UPI integration.

* **Why Android and iOS are sending different responses in UPI and Intent app flow?**

Based on the Android or iOS platform, PayU sends different responses in both payment Modes (UPI Collect/UPI Intent). Hence, you have to handle those responses at your end.

**For Android:**

* In the case of UPI intent/InApp flow,  you will not receive a callback response in the`surl` or `furl`. In this case, the format of the PayU response received will be different from other payment options that you can handle accordingly. For handling `surl` or `furl`, refer to [Handling Redirect URLs](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).
* If you get **mihpayid** in the PayU response, consider it as a **PayU ID/ID**

**For IOS**:

* In the case of UPI intent and Collect flow, you will not receive a callback response in SURL/FURL. In this case, the format of the PayU response received will be different from other payment options that you can handle accordingly. For handling `surl` or `furl`, refer to [Handling Redirect URLs](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).
* If you get **mihpayid** in the PayU response, consider it as a PayU ID/ ID.

## **PhonePe Integration**

* **How can I integrate PhonePe with PayU Android SDK?**

To integrate PhonePe with PayU Android SDK, you need to use the `setPaymentOption` method provided by the SDK to select PhonePe as the payment option and configure the PhonePe payment parameters.

* **Which countries are supported for PhonePe integration with PayU Android SDK?**

PhonePe integration with PayU Android SDK is currently available only in India.

* **Can I customize the PhonePe payment user interface in my app?**

Yes, you can customize the PhonePe payment user interface in your app by using the PayU Mobile Android SDK’s customization options.

* **What are the different types of PhonePe transactions supported by PayU Android SDK?**

PayU Android SDK supports PhonePe transactions for making payments, requesting payments, and checking the status of a payment.

* **What is the difference between PayU CheckoutPro and Non-Seamless?**

**PayU CheckoutPro** and **Non-Seamless** integration are the same. For more information, refer to the (Explore Android SDKs)[[https://docs.payu.in/docs/explore-android-sdks/](https://docs.payu.in/docs/explore-android-sdks/)]

* **Why do we need so many hashes?**

For security purposes, the hash is mandatory. Whenever you connect to the PayU server you need a hash. For every API, there is a separate hash because all APIs are public.

* **Do we need to calculate Reverse Hash?**

It is mandatory to calculate the reverse hash on your surl/furl to validate a transaction at your end. Otherwise, the transaction may be hacked or tampered with.

For more information, refer to [Server Side Document](https://github.com/payu-intrepos/Documentations/wiki/Server-Side).

* **Does the merchant need PCI/DSS certificate?**

When the merchant collects the customer’s card details on their website/server and posts them to PayU. The merchant must be PCI-DSS certified in this case. For further information on PCI-DSS certification please contact your Account Manager at PayU.

* **Do all the Mobile SDKs support UPI Intent flow?**

Only the following integrations in Android SDK work through Intent:

* [PhonePe](doc:android-phonepe-sdk)
* [Google Pay](doc:android-google-pay-sdk)
* PayTM
* **Can merchants generate hash from PayU SDK?**

Yes, merchants can also generate a hash from PayU SDK but it’s not recommended because in this case key and salt will be hardcoded so anyone can use key and salt for making payment and it’s not secure.

* **We want our users to make in-app payments using UPI apps installed on our customer’s mobile. We don’t want to enter any security-related details such as merchant key, secret, or hash on the Android app to avoid security risks. We want the Android-side implementation to be as simple as possible. The Android app should be able to initiate the transaction using a unique transaction ID provided by our backend. Our backend will get this transaction ID using PG-provided APIs. Please suggest how is this possible if possible.**

You can use PayU CheckoutPro SDK or Non-seamless SDK (PayU UI) in PayU Android SDK integration. For more information, refer to the following:

* [Android SDK Integration Docs. > PayU CheckoutPro SDK](https://docs.payu.in/docs/android-checkoutpro-sdk)
* Sample App: [https://github.com/payu-intrepos/PayUCheckoutPro-Android/tree/JavaSampleApp](https://github.com/payu-intrepos/PayUCheckoutPro-Android/tree/JavaSampleApp)
* **Is there a tool to test hash generation?**

For more information on using the tools to test hash, refer to [Hash generation Tool](https://payuhashgeneration.herokuapp.com/).

The merchant can check if he is calculating hash correctly by entering the same parameters using the above tool and then test the hashes generated with the hashes he is getting from his code.

* **Why do we need to use surl and furl in CustomBrowser?**

When the transaction succeeds, PayU posts the response to the surl, and if the transaction fails PayU posts the response to the furl provided in post parameters while making a payment request.

For information on using surl and furl, refer [Server Side Document](https://github.com/payu-intrepos/Documentations/wiki/Server-Side).

* **What is the session time-out period for the PayU gateway? That is, if I do not enter any details, confirm, or cancel payment for a significant amount of time, will I get a session expired message? If yes, what is that time and is it configurable?**

The PayU page will not expire, however, the PayU ID generated will be expired or bounce if the customer lands on the payment page for three hours and is left idle. Also, after three hours if the customer enters the card details, a new PayUid will be generated and the transaction will go through.

* **​Does PayU accept the following card types?**
  * **Master**
  * **Visa**
  * **Maestro(both 19 & 16 Digit)**
  * **Rupay**
  * **Amex**

Yes, the above-listed card types are accepted.

* **What is the maximum character length for a card number?**

For Maestro 19, 16 otherwise. For more information, refer to [Card Number Formats](https://docs.payu.in/docs/card-number-formats).

* **What is the maximum character length for CVV?**

The maximum character length is 4 for Amex cardholders, and 3 otherwise.

* **I am using CustomBrowser version\<7.4.0. How can I update the SDK to avail UPI payment modes?**

With version 7.4.0, PayU has optimized the SDK Offerings for you. After you update this SDK, the UPI transaction offering will be removed. The UPI Transactions offering is added in another SDK that supports the complete UPI portfolio – UPI Collect transactions, UPI Intent transactions, Tez(GPay) (In-App, Intent & Collect) Flows and PhonePe Flows, and SamsungPay. For more information on UPI SDK to accept UPI payments, refer to [Android UPI integration](https://docs.payu.in/docs/card-number-formats).

* **I am a CustomBrowser Merchant version >=7.4.0. I have added UPI SDK for UPI offering(Generic Intent and UPI Collect). I would like to add Google, PhonePe, and Samsung Pay payment options. What should I do?**

You just need to add PayU Gradle dependencies for [GooglePay](doc:android-google-pay-sdk), [Phonepe](https://docs.payu.in/docs/android-phonepe-sdk), and Samsung Pay. Generate _PostData_ according to the payment option you choose.

* **I am a UPI SDK merchant(Directly UPI SDK not through CustomBrowser), I would like to add GooglePay, PhonePe, or SamsungPay.**

You just need to add PayU Gradle dependencies for [Googlepay](doc:android-google-pay-sdk), [Phonepe](https://docs.payu.in/docs/android-phonepe-sdk), and Samsung Pay and generate `PostData` for the same reference [Postdata through UPI SDK](https://docs.payu.in/docs/android-upisdk-integration-steps#step-4-payment-request-post-data).

* **Is PG SDK mandatory to use with CustomBrowser?**

PG SDK is not mandatory to make payments with CustomBrowser. You can create `PostData` of its own.

* **How to switch the environment from Testing to Production in PayU SDK?**

Refer to the . You need to change the value of the environment variable accordingly for testing or production, in MainActivity in the sample app. Refer following code snippet**:**

```node
int env = PayuConstants.PRODUCTION_ENV; _//for production_

int env = PayuConstants.STAGING_ENV; _//for testing_
```

Remove the following metadata from the manifest file:

```xml
<meta-data
     android:name="payu_web_service_url"
     android:value="https://test.payu.in" />
 <meta-data
     android:name="payu_post_url"
     android:value="https://test.payu.in" />
```

* **Why is enter OTP manually button not visible on CB when the Material theme is used?**

To fix this problem, use the following code block in your **styles.xml** file:

```xml
 <style name="cb_approve_otp" parent="android:Widget.Button">
        <item name="android:textSize">@dimen/cb_fourteenScaled</item>
        <item name="android:textColor">#FFFFFF</item>
        <item name="backgroundTint">@color/cb_otpColor</item>
</style>
```

* **How to fix the** build error after adding the **PayUCheckoutPro SDK gradle dependency?**

After adding the _PayUCheckoutPro_ SDK gradle dependency, if the build error similar to the following is received, include the parameter as indicated (after the error screenshot):

<Image align="center" border={false} src="https://files.readme.io/cc69622a5272a649cbe36381aed4ec5e391ed71704966ae3a05feb8a3aba1924-android-faq_error1.png" />

Add the following parameter in the \<application> tag of your app’s **AndroidManifest.xml** file.

```plaintext
tools:replace="android:theme"
```

* **When I was compiling my Android implementation, the following exception occurred in the compiler:**

```java
Task :app:compileDebugJavaWithJavac FAILED
An exception has occurred in the compiler (1.8.0_301). Please file a bug against the Java compiler via the Java bug reporting page (http://bugreport.java.com) after checking the Bug Database (http://bugs.java.com) for duplicates. Include your program and the following diagnostic in your report. Thank you.
java.lang.AssertionError: annotationType(): unrecognized Attribute name MODULE (class com.sun.tools.javac.util.UnsharedNameTable$NameImpl)
    at com.sun.tools.javac.util.Assert.error(Assert.java:133)
    at com.sun.tools.javac.code.TypeAnnotations.annotationType(TypeAnnotations.java:231)
    at com.sun.tools.javac.code.TypeAnnotations$TypeAnnotationPositions.separateAnnotationsKinds(TypeAnnotations.java:294)
    at com.sun.tools.javac.code.TypeAnnotations$TypeAnnotationPositions.visitMethodDef(TypeAnnotations.java:1066)
    at com.sun.tools.javac.tree.JCTree$JCMethodDecl.accept(JCTree.java:778)
    at com.sun.tools.javac.tree.TreeScanner.scan(TreeScanner.java:49)
    at com.sun.tools.javac.code.TypeAnnotations$TypeAnnotationPositions.scan(TypeAnnotations.java:275)
    at com.sun.tools.javac.tree.TreeScanner.scan(TreeScanner.java:57)
    at com.sun.tools.javac.code.TypeAnnotations$TypeAnnotationPositions.visitClassDef(TypeAnnotations.java:1042)
    at com.sun.tools.javac.tree.JCTree$JCClassDecl.accept(JCTree.java:693)
    at com.sun.tools.javac.tree.TreeScanner.scan(TreeScanner.java:49)
    at com.sun.tools.javac.code.TypeAnnotations$TypeAnnotationPositions.scan(TypeAnnotations.java:275)
    at com.sun.tools.javac.code.TypeAnnotations$1.run(TypeAnnotations.java:127)
    at com.sun.tools.javac.comp.Annotate.flush(Annotate.java:152)
    at com.sun.tools.javac.comp.Annotate.enterDone(Annotate.java:129)
    at com.sun.tools.javac.comp.Enter.complete(Enter.java:512)
    at com.sun.tools.javac.comp.Enter.main(Enter.java:471)
    at com.sun.tools.javac.main.JavaCompiler.enterTrees(JavaCompiler.java:982)
    at com.sun.tools.javac.main.JavaCompiler.compile(JavaCompiler.java:857)
    at com.sun.tools.javac.main.Main.compile(Main.java:523)
    at com.sun.tools.javac.api.JavacTaskImpl.doCall(JavacTaskImpl.java:129)
    at com.sun.tools.javac.api.JavacTaskImpl.call(JavacTaskImpl.java:138)
    at org.gradle.internal.compiler.java.IncrementalCompileTask.call(IncrementalCompileTask.java:74)
    at org.gradle.api.internal.tasks.compile.AnnotationProcessingCompileTask.call(AnnotationProcessingCompileTask.java:94)
    at org.gradle.api.internal.tasks.compile.ResourceCleaningCompilationTask.call(ResourceCleaningCompilationTask.java:57)
    at org.gradle.api.internal.tasks.compile.JdkJavaCompiler.execute(JdkJavaCompiler.java:55)
    at org.gradle.api.internal.tasks.compile.JdkJavaCompiler.execute(JdkJavaCompiler.java:40)
    at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.delegateAndHandleErrors(NormalizingJavaCompiler.java:97)
    at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.execute(NormalizingJavaCompiler.java:51)
    at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.execute(NormalizingJavaCompiler.java:37)
    at org.gradle.api.internal.tasks.compile.AnnotationProcessorDiscoveringCompiler.execute(AnnotationProcessorDiscoveringCompiler.java:51)
    at org.gradle.api.internal.tasks.compile.AnnotationProcessorDiscoveringCompiler.execute(AnnotationProcessorDiscoveringCompiler.java:37)
    at org.gradle.api.internal.tasks.compile.ModuleApplicationNameWritingCompiler.execute(ModuleApplicationNameWritingCompiler.java:46)
    at org.gradle.api.internal.tasks.compile.ModuleApplicationNameWritingCompiler.execute(ModuleApplicationNameWritingCompiler.java:36)
    at org.gradle.api.internal.tasks.compile.CleaningJavaCompiler.execute(CleaningJavaCompiler.java:53)
    at org.gradle.api.internal.tasks.compile.incremental.IncrementalCompilerFactory.lambda$createRebuildAllCompiler$0(IncrementalCompilerFactory.java:98)
    at org.gradle.api.internal.tasks.compile.incremental.IncrementalResultStoringCompiler.execute(IncrementalResultStoringCompiler.java:61)
    at org.gradle.api.internal.tasks.compile.incremental.IncrementalResultStoringCompiler.execute(IncrementalResultStoringCompiler.java:45)
    at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler$2.call(CompileJavaBuildOperationReportingCompiler.java:59)
    at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler$2.call(CompileJavaBuildOperationReportingCompiler.java:51)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:200)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:195)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:75)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:153)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:62)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.lambda$call$2(DefaultBuildOperationExecutor.java:76)
    at org.gradle.internal.operations.UnmanagedBuildOperationWrapper.callWithUnmanagedSupport(UnmanagedBuildOperationWrapper.java:54)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:76)
    at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler.execute(CompileJavaBuildOperationReportingCompiler.java:51)
    at org.gradle.api.tasks.compile.JavaCompile.performCompilation(JavaCompile.java:343)
    at org.gradle.api.tasks.compile.JavaCompile.performIncrementalCompilation(JavaCompile.java:237)
    at org.gradle.api.tasks.compile.JavaCompile.compile(JavaCompile.java:209)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:104)
    at org.gradle.api.internal.project.taskfactory.IncrementalInputsTaskAction.doExecute(IncrementalInputsTaskAction.java:32)
    at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:51)
    at org.gradle.api.internal.project.taskfactory.AbstractIncrementalTaskAction.execute(AbstractIncrementalTaskAction.java:25)
    at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:29)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter$3.run(ExecuteActionsTaskExecuter.java:555)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:29)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:26)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:75)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:153)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:56)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.lambda$run$1(DefaultBuildOperationExecutor.java:71)
    at org.gradle.internal.operations.UnmanagedBuildOperationWrapper.runWithUnmanagedSupport(UnmanagedBuildOperationWrapper.java:45)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.run(DefaultBuildOperationExecutor.java:71)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeAction(ExecuteActionsTaskExecuter.java:540)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:523)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.access$300(ExecuteActionsTaskExecuter.java:108)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter$TaskExecution.executeWithPreviousOutputFiles(ExecuteActionsTaskExecuter.java:271)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter$TaskExecution.execute(ExecuteActionsTaskExecuter.java:260)
    at org.gradle.internal.execution.steps.ExecuteStep.lambda$execute$0(ExecuteStep.java:33)
    at java.util.Optional.map(Optional.java:215)
    at org.gradle.internal.execution.steps.ExecuteStep.execute(ExecuteStep.java:33)
    at org.gradle.internal.execution.steps.ExecuteStep.execute(ExecuteStep.java:26)
    at org.gradle.internal.execution.steps.CleanupOutputsStep.execute(CleanupOutputsStep.java:67)
    at org.gradle.internal.execution.steps.CleanupOutputsStep.execute(CleanupOutputsStep.java:36)
    at org.gradle.internal.execution.steps.ResolveInputChangesStep.execute(ResolveInputChangesStep.java:49)
    at org.gradle.internal.execution.steps.ResolveInputChangesStep.execute(ResolveInputChangesStep.java:34)
    at org.gradle.internal.execution.steps.CancelExecutionStep.execute(CancelExecutionStep.java:43)
    at org.gradle.internal.execution.steps.TimeoutStep.executeWithoutTimeout(TimeoutStep.java:73)
    at org.gradle.internal.execution.steps.TimeoutStep.execute(TimeoutStep.java:54)
    at org.gradle.internal.execution.steps.CreateOutputsStep.execute(CreateOutputsStep.java:44)
    at org.gradle.internal.execution.steps.SnapshotOutputsStep.execute(SnapshotOutputsStep.java:54)
    at org.gradle.internal.execution.steps.SnapshotOutputsStep.execute(SnapshotOutputsStep.java:38)
    at org.gradle.internal.execution.steps.BroadcastChangingOutputsStep.execute(BroadcastChangingOutputsStep.java:42)
    at org.gradle.internal.execution.steps.CacheStep.executeWithoutCache(CacheStep.java:159)
    at org.gradle.internal.execution.steps.CacheStep.execute(CacheStep.java:72)
    at org.gradle.internal.execution.steps.CacheStep.execute(CacheStep.java:43)
    at org.gradle.internal.execution.steps.StoreExecutionStateStep.execute(StoreExecutionStateStep.java:44)
    at org.gradle.internal.execution.steps.StoreExecutionStateStep.execute(StoreExecutionStateStep.java:33)
    at org.gradle.internal.execution.steps.RecordOutputsStep.execute(RecordOutputsStep.java:38)
    at org.gradle.internal.execution.steps.RecordOutputsStep.execute(RecordOutputsStep.java:24)
    at org.gradle.internal.execution.steps.SkipUpToDateStep.executeBecause(SkipUpToDateStep.java:92)
    at org.gradle.internal.execution.steps.SkipUpToDateStep.lambda$execute$0(SkipUpToDateStep.java:85)
    at java.util.Optional.map(Optional.java:215)
    at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:55)
    at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:39)
    at org.gradle.internal.execution.steps.ResolveChangesStep.execute(ResolveChangesStep.java:76)
    at org.gradle.internal.execution.steps.ResolveChangesStep.execute(ResolveChangesStep.java:37)
    at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:36)
    at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:26)
    at org.gradle.internal.execution.steps.ResolveCachingStateStep.execute(ResolveCachingStateStep.java:94)
    at org.gradle.internal.execution.steps.ResolveCachingStateStep.execute(ResolveCachingStateStep.java:49)
    at org.gradle.internal.execution.steps.CaptureStateBeforeExecutionStep.execute(CaptureStateBeforeExecutionStep.java:79)
    at org.gradle.internal.execution.steps.CaptureStateBeforeExecutionStep.execute(CaptureStateBeforeExecutionStep.java:53)
    at org.gradle.internal.execution.steps.ValidateStep.execute(ValidateStep.java:74)
    at org.gradle.internal.execution.steps.SkipEmptyWorkStep.lambda$execute$2(SkipEmptyWorkStep.java:78)
    at java.util.Optional.orElseGet(Optional.java:267)
    at org.gradle.internal.execution.steps.SkipEmptyWorkStep.execute(SkipEmptyWorkStep.java:78)
    at org.gradle.internal.execution.steps.SkipEmptyWorkStep.execute(SkipEmptyWorkStep.java:34)
    at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsStartedStep.execute(MarkSnapshottingInputsStartedStep.java:39)
    at org.gradle.internal.execution.steps.LoadExecutionStateStep.execute(LoadExecutionStateStep.java:40)
    at org.gradle.internal.execution.steps.LoadExecutionStateStep.execute(LoadExecutionStateStep.java:28)
    at org.gradle.internal.execution.impl.DefaultWorkExecutor.execute(DefaultWorkExecutor.java:33)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeIfValid(ExecuteActionsTaskExecuter.java:187)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:179)
    at org.gradle.api.internal.tasks.execution.CleanupStaleOutputsExecuter.execute(CleanupStaleOutputsExecuter.java:109)
    at org.gradle.api.internal.tasks.execution.FinalizePropertiesTaskExecuter.execute(FinalizePropertiesTaskExecuter.java:46)
    at org.gradle.api.internal.tasks.execution.ResolveTaskExecutionModeExecuter.execute(ResolveTaskExecutionModeExecuter.java:62)
    at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:57)
    at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:56)
    at org.gradle.api.internal.tasks.execution.CatchExceptionTaskExecuter.execute(CatchExceptionTaskExecuter.java:36)
    at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.executeTask(EventFiringTaskExecuter.java:77)
    at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:55)
    at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter$1.call(EventFiringTaskExecuter.java:52)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:200)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:195)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:75)
    at org.gradle.internal.operations.DefaultBuildOperationRunner$3.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:153)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:68)
    at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:62)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.lambda$call$2(DefaultBuildOperationExecutor.java:76)
    at org.gradle.internal.operations.UnmanagedBuildOperationWrapper.callWithUnmanagedSupport(UnmanagedBuildOperationWrapper.java:54)
    at org.gradle.internal.operations.DefaultBuildOperationExecutor.call(DefaultBuildOperationExecutor.java:76)
    at org.gradle.api.internal.tasks.execution.EventFiringTaskExecuter.execute(EventFiringTaskExecuter.java:52)
    at org.gradle.execution.plan.LocalTaskNodeExecutor.execute(LocalTaskNodeExecutor.java:41)
    at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:372)
    at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$InvokeNodeExecutorsAction.execute(DefaultTaskExecutionGraph.java:359)
    at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:352)
    at org.gradle.execution.taskgraph.DefaultTaskExecutionGraph$BuildOperationAwareExecutionAction.execute(DefaultTaskExecutionGraph.java:338)
    at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.lambda$run$0(DefaultPlanExecutor.java:127)
    at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.execute(DefaultPlanExecutor.java:191)
    at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.executeNextNode(DefaultPlanExecutor.java:182)
    at org.gradle.execution.plan.DefaultPlanExecutor$ExecutorWorker.run(DefaultPlanExecutor.java:124)
    at org.gradle.internal.concurrent.ExecutorPolicy$CatchAndRecordFailures.onExecute(ExecutorPolicy.java:64)
    at org.gradle.internal.concurrent.ManagedExecutorImpl$1.run(ManagedExecutorImpl.java:48)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
    at org.gradle.internal.concurrent.ThreadFactoryImpl$ManagedThreadRunnable.run(ThreadFactoryImpl.java:56)
    at java.lang.Thread.run(Thread.java:748)

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':app:compileDebugJavaWithJavac'.
> Compilation failed; see the compiler error output for details.

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 6s
17 actionable tasks: 2 executed, 15 up-to-date
```

Try to upgrade your gradle version, this line: classpath ‘com.android.tools.build:gradle:4.1.0’

* **I want to use GPay for collecting payments and it requires the S2S (Server-to-Server integration) flag to be enabled. How do I enable Server-to-Server integration for my account?**

You need to contact your PayU Key Account Manager to enable Server-to-Server integration.

* **Can I generate hashes on my app?**

PayU recommends you generate the hashes on your server. Do not generate the hashes locally in your app as it will compromise the security of the transactions.

* **I was checking the** [**PayU Github**](https://github.com/payu-intrepos) **code for Ionic Cordova files and was unable to find the integration code.**

The JS code for Ionic Cordova can be accessed from the following location:

[https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js](https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js)

* **Should I make a payment request using the Payment (_payment) API for Android**?

You need not use the Payment API if you are using PayU Mobile SDK, as PayU Mobile SDK will call all the APIs internally.

* **Should I use the customer’s VPA to enable users to make payments through any UPI app installed on his/her mobile?**

If you want to use collect flow, it is mandatory to enter VPA, otherwise, it is not required.

* **What is the amount data format in PayU SDK?**

In PayU SDK, always pass String value in amount field for iOS and Android.

* **How do I test my Android SDK integration before going live?**

You can test your integration using PayU's test environment:
1. Use Test Key and Test Salt from your PayU dashboard
2. Set the `setIsProduction` parameter to `false` in your code
3. Use test card numbers and test credentials provided in the documentation
4. Test various payment methods (cards, UPI, net banking, etc.)
5. Verify the payment callbacks and responses

For more information, refer to [Test Cards, UPI ID and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).

* **What should I do if the payment page is not loading in my Android app?**

If the payment page is not loading, check the following:
1. Verify your internet connection and permissions in AndroidManifest.xml
2. Ensure you're using the correct environment (test/production) with matching Key and Salt
3. Check if the hash is generated correctly on your server
4. Verify that all required parameters are being passed correctly
5. Check the logs for any error messages
6. Ensure your app has the necessary network security configuration

* **How do I handle payment failures in Android SDK?**

Payment failures can be handled through:
1. **Callback methods**: Implement the payment result callbacks to receive success/failure responses
2. **Error codes**: Check the error codes in the response to identify the specific failure reason
3. **User feedback**: Display appropriate error messages to users based on the error code
4. **Retry mechanism**: Allow users to retry the payment if the failure is due to network or temporary issues

For detailed error handling, refer to [Error Handling](https://docs.payu.in/docs/error-handling).

* **Can I use PayU Android SDK in a background service or worker thread?**

PayU Android SDK operations should be performed on the main/UI thread. Payment UI components require the Android main thread to function properly. However, hash generation and network calls can be performed on background threads, but ensure you switch back to the main thread before calling SDK methods that display UI.

* **What happens if the user closes the app during a payment transaction?**

If the user closes the app during a payment transaction:
1. The transaction may still be processing on PayU's servers
2. You should implement proper callback handling to receive the payment response when the app is reopened
3. Use `surl` and `furl` to receive payment responses even if the app is closed
4. Implement proper state management to handle such scenarios

* **How do I switch between test and production environments in Android SDK?**

To switch between test and production environments:
1. Use Test Key and Test Salt for testing, and Production Key and Salt for production
2. Set the `setIsProduction` parameter accordingly:
   - `false` for test environment
   - `true` for production environment
3. Remove test metadata from AndroidManifest.xml when going to production
4. Ensure you're using the correct API endpoints for each environment

* **What payment methods require additional setup or configuration?**

Some payment methods may require additional setup:
- **UPI**: May require VPA for collect flow
- **Google Pay**: Requires S2S (Server-to-Server) integration flag to be enabled
- **PhonePe**: Requires specific SDK integration
- **EMI**: Requires bank and card eligibility checks
- **BNPL**: Requires merchant approval and configuration

Contact your PayU Key Account Manager for enabling specific payment methods.

* **How do I debug issues with PayU Android SDK integration?**

To debug integration issues:
1. Enable logging in your app to see SDK logs
2. Check the Android logcat for error messages
3. Verify all parameters being sent to the SDK
4. Test with PayU's test credentials first
5. Use PayU's hash generation tool to verify hash calculations
6. Check network requests and responses
7. Review the integration documentation for common issues
8. Contact PayU Support with specific error codes and logs

* **Can I use multiple PayU SDKs together in the same Android app?**

Yes, you can use multiple PayU SDKs together, such as:
- CheckoutPro SDK with UPI SDK
- CheckoutPro SDK with Google Pay SDK
- CheckoutPro SDK with PhonePe SDK

Ensure you follow the integration steps for each SDK and handle conflicts in dependencies if any. Refer to the specific SDK documentation for compatibility information.

* **What is the difference between static hash and dynamic hash in Android SDK?**

- **Static Hash**: Generated once and can be reused for multiple transactions. Used for certain payment flows but less secure.
- **Dynamic Hash**: Generated fresh for each transaction with transaction-specific parameters. More secure and recommended for production use.

PayU recommends using dynamic hash for better security. For more information, refer to [Generate Dynamic Hash](https://docs.payu.in/docs/android-checkoutpro-generate-dynamic-hash) or [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash-android-sdk-pro).

* **How do I handle deep links or redirects after payment in Android SDK?**

Deep links and redirects are handled through:
1. **surl (Success URL)**: Called when payment is successful
2. **furl (Failure URL)**: Called when payment fails
3. **Intent filters**: Configure AndroidManifest.xml to handle payment callbacks
4. **Activity result**: Use Activity result callbacks for SDK-based flows

For detailed implementation, refer to [Handling Redirect URLs](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).

* **What should I do if I receive an invalid hash error?**

If you receive an invalid hash error:
1. Verify that you're using the correct Key and Salt (test vs production)
2. Ensure the hash is generated on your server, not in the app
3. Check that all parameters used in hash generation match the parameters sent to PayU
4. Verify the hash generation formula and parameter order
5. Use PayU's hash generation tool to test your hash calculation
6. Ensure there are no extra spaces or encoding issues in parameters

* **Can I customize the payment success/failure messages in Android SDK?**

Yes, you can customize payment success/failure messages:
1. Handle the payment callbacks in your app
2. Display custom messages based on the payment response
3. Use the SDK's customization options to modify the UI
4. Implement your own error handling and user feedback

The SDK provides callbacks that you can use to show custom messages to users.

## Troubleshooting

* **Why am I getting "Value \<\!DOCTYPE of type java.lang.String cannot be converted to JSONObject" error?**

This error (Error code 5014) typically occurs when:
1. You're using Test Key & Test Salt but have set `setIsProduction` to `true`
2. You're using Production Key and Salt but have set `setIsProduction` to `false`

**Solution**: Ensure the `setIsProduction` parameter matches your Key and Salt:
- Use `setIsProduction(false)` with Test Key & Test Salt
- Use `setIsProduction(true)` with Production Key and Salt

For more information, refer to [CheckoutPro SDK go-live checklist](https://docs.payu.in/docs/android-checkoutpro-golive-checklist).

* **Why is the "Enter OTP manually" button not visible when using Material theme in CustomBrowser?**

This issue occurs due to theme conflicts. To fix it, add the following code block in your `styles.xml` file:

```xml
<style name="cb_approve_otp" parent="android:Widget.Button">
    <item name="android:textSize">@dimen/cb_fourteenScaled</item>
    <item name="android:textColor">#FFFFFF</item>
    <item name="backgroundTint">@color/cb_otpColor</item>
</style>
```

* **How do I fix build errors related to theme conflicts after adding PayUCheckoutPro SDK?**

If you encounter build errors related to theme conflicts, add the following parameter in the `<application>` tag of your app's `AndroidManifest.xml` file:

```xml
tools:replace="android:theme"
```

Also ensure you have the tools namespace declared in your manifest:
```xml
xmlns:tools="http://schemas.android.com/tools"
```

* **What should I do if the SDK is not responding or payment page is blank?**

If the SDK is not responding or showing a blank page:
1. Check your internet connection and network permissions
2. Verify that all required parameters are being passed correctly
3. Ensure the hash is generated correctly and matches the parameters
4. Check Android logcat for any error messages
5. Verify you're using the correct environment (test/production)
6. Try clearing app cache and data
7. Ensure you're using a supported Android version

* **Why am I not receiving payment callbacks (surl/furl) in my Android app?**

If you're not receiving payment callbacks:
1. Verify that `surl` and `furl` are correctly configured in your payment request
2. Ensure your app can handle deep links or URL schemes
3. Check AndroidManifest.xml for proper intent filters
4. Verify that your server endpoints are accessible and responding
5. For UPI Intent flow, note that callbacks may be handled differently
6. Check if the app was closed during payment - implement proper state handling

For more information, refer to [Handling Redirect URLs](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).

* **How do I resolve dependency conflicts when integrating PayU Android SDK?**

If you encounter dependency conflicts:
1. Check the SDK documentation for required dependency versions
2. Use Gradle's dependency resolution strategies
3. Exclude conflicting transitive dependencies if necessary
4. Update your project's dependencies to compatible versions
5. Use `./gradlew dependencies` to identify conflict sources
6. Contact PayU Support if conflicts persist

* **What should I do if payment transactions are failing with authentication errors?**

If you're getting authentication errors:
1. Verify your Merchant Key and Salt are correct
2. Ensure the hash is generated correctly on your server
3. Check that you're using the correct environment (test/production)
4. Verify all required authentication parameters are included
5. Ensure your account is activated and in good standing
6. Check if there are any account-level restrictions

* **Why are UPI payments not working in my Android app?**

If UPI payments are not working:
1. Verify UPI SDK is properly integrated
2. Check if UPI apps are installed on the device
3. Ensure VPA is provided for UPI Collect flow
4. Verify UPI is enabled for your merchant account
5. Check device compatibility and Android version
6. Review UPI integration documentation for specific requirements

For more information, refer to [Android UPI SDK Integration](https://docs.payu.in/docs/android-upisdk-integration-steps).

## Upgrade

* **How much time does it take to update the SDK in code to upgrade to the latest version of SDK?**

To update the SDK it takes only 5 – 10 mins. If you are facing any issues in updating the SDK, you can contact [PayU Support] (https://help.payu.in/).

* **How do I upgrade to the latest version of PayU Android SDK?**

To upgrade to the latest version:
1. Update the SDK version in your `build.gradle` file
2. Sync your project with Gradle files
3. Review the release notes for breaking changes
4. Update your code if there are any API changes
5. Test thoroughly in the test environment before going live
6. Update any customizations if they're affected by the upgrade

Check the SDK's version history or changelog for specific upgrade instructions.

* **What should I check before upgrading the PayU Android SDK?**

Before upgrading:
1. Review the release notes and changelog for the new version
2. Check for any deprecated methods or breaking changes
3. Verify compatibility with your current Android and Gradle versions
4. Test the upgrade in a development environment first
5. Backup your current implementation
6. Check if any customizations need to be updated
7. Review migration guides if available

* **Will upgrading the SDK affect my existing integrations?**

Upgrading the SDK may affect your integration if:
1. There are breaking changes in the API
2. Required parameters have changed
3. Callback methods have been modified
4. Dependencies have been updated

Always review the release notes and test thoroughly before deploying to production. Most minor version updates are backward compatible, but major version updates may require code changes.

## SDK Compatibility and Requirements

* **What is the minimum Android version required for PayU Android SDK?**

The minimum Android version (API level) varies by SDK:
- **CheckoutPro SDK**: Check the specific SDK documentation for minimum API level
- **Core SDK**: Typically requires API level 21 (Android 5.0) or higher
- **CustomBrowser SDK**: Check version-specific requirements
- **UPI SDK**: Requires API level 21 or higher

Refer to the specific SDK integration documentation for exact requirements.

* **Is PayU Android SDK compatible with Kotlin?**

Yes, PayU Android SDK is compatible with Kotlin. You can use the SDK in both Java and Kotlin projects. The SDK provides Java APIs that work seamlessly with Kotlin through interoperability.

* **Can I use PayU Android SDK with Jetpack Compose?**

PayU Android SDK is built using traditional Android Views. While you can use it in a Jetpack Compose project, you'll need to use `AndroidView` composable to embed the SDK's UI components. The SDK's payment flows will still use the traditional View system.

* **Does PayU Android SDK support ProGuard/R8 code obfuscation?**

Yes, PayU Android SDK supports ProGuard and R8. However, you may need to add specific ProGuard rules to prevent the SDK from being obfuscated. Check the SDK documentation for required ProGuard rules, or contact PayU Support for the latest rules.

* **What permissions are required for PayU Android SDK?**

The required permissions typically include:
- `INTERNET`: For network communication
- `ACCESS_NETWORK_STATE`: To check network connectivity (optional but recommended)

Some payment methods may require additional permissions:
- UPI payments may require specific UPI app permissions
- Location permissions for certain features (if applicable)

Add these permissions in your `AndroidManifest.xml` file.

* **Can I use PayU Android SDK in a multi-module Android project?**

Yes, you can use PayU Android SDK in a multi-module project. Add the SDK dependency to the module where you'll be using it, or add it to a shared module if multiple modules need access. Ensure proper dependency management across modules.

* **Is PayU Android SDK compatible with Android App Bundle (AAB) format?**

Yes, PayU Android SDK is compatible with Android App Bundle (AAB) format. You can build and publish your app using AAB without any special configuration for the PayU SDK.

## Security

* **Is it safe to store Merchant Key and Salt in my Android app?**

No, it is not safe to store Merchant Key and Salt in your Android app. These credentials should be kept on your server. Always generate hashes on your server and pass them to the Android app. Storing credentials in the app makes them vulnerable to reverse engineering.

* **How can I ensure secure payment processing with PayU Android SDK?**

To ensure secure payment processing:
1. Generate hashes on your server, not in the app
2. Never store Merchant Key and Salt in the app
3. Use HTTPS for all network communications
4. Implement proper SSL certificate pinning if required (note: PayU SDK doesn't support SSL pinning)
5. Validate payment responses using reverse hash verification
6. Use ProGuard/R8 to obfuscate your code
7. Keep the SDK updated to the latest version
8. Follow Android security best practices

* **Does PayU Android SDK handle PCI-DSS compliance?**

Yes, PayU CheckoutPro SDK is PCI-DSS compliant. When using CheckoutPro SDK, card details are handled by PayU's secure payment pages, so you don't need PCI-DSS certification. However, if you collect card details directly in your app, you'll need PCI-DSS certification.

* **How does PayU Android SDK protect sensitive payment data?**

PayU Android SDK protects sensitive data by:
1. Using encrypted communication channels (HTTPS/TLS)
2. Not storing sensitive payment information locally
3. Using secure tokenization for saved payment methods
4. Implementing secure hash-based authentication
5. Following industry-standard security practices

* **Can I implement additional security measures on top of PayU Android SDK?**

Yes, you can implement additional security measures:
1. Implement certificate pinning at the app level (though PayU SDK doesn't support it internally)
2. Add additional validation layers
3. Implement fraud detection mechanisms
4. Use secure storage for any app-specific data
5. Implement proper session management
6. Add logging and monitoring for security events

## Testing and Development

* **How do I test PayU Android SDK integration without making real payments?**

You can test using:
1. **Test Environment**: Use Test Key and Test Salt from your PayU dashboard
2. **Test Cards**: Use test card numbers provided in PayU documentation
3. **Test UPI IDs**: Use test UPI IDs for UPI payment testing
4. **Test Wallets**: Use test wallet credentials
5. **Sandbox Mode**: Set `setIsProduction(false)` in your code

For test credentials, refer to [Test Cards, UPI ID and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets).

* **Can I test PayU Android SDK integration on an emulator?**

Yes, you can test on an Android emulator. However, note that:
1. Some payment methods (like UPI apps) may not work on emulators
2. Network-related testing should work fine
3. For UPI and wallet testing, you may need a physical device
4. Ensure the emulator has proper network configuration

* **How do I enable debug logging for PayU Android SDK?**

Debug logging can be enabled by:
1. Setting appropriate log levels in your app
2. Checking Android logcat for SDK logs
3. Enabling verbose logging in development builds
4. Using PayU's debugging tools if available

Note: Disable verbose logging in production builds for security and performance.

* **What test scenarios should I cover before going live?**

Before going live, test:
1. All payment methods (cards, UPI, net banking, wallets)
2. Success and failure scenarios
3. Network connectivity issues
4. App backgrounding during payment
5. Payment cancellation
6. Hash validation
7. Callback handling (surl/furl)
8. Error handling and user feedback
9. Different Android versions and devices
10. Edge cases and error conditions
