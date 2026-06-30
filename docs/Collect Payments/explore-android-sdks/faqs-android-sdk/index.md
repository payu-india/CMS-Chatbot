---
title: FAQs - Android SDK
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
title: FAQs - Android SDK
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
This page answers common questions about PayU Android SDK integration. For step-by-step guides, use the links below.

## Related documentation

| Topic | Guide |
| --- | --- |
| SDK overview and selection | [Explore Android SDKs](doc:explore-android-sdks) |
| CheckoutPro integration | [Integration Steps](doc:integration-steps-android-checkout-pro) |
| Hash generation | [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk) |
| Callbacks and verification | [Handling Redirect URLs (surl/furl)](doc:handling-redirect-urls-surlfurl-with-android-sdk) |
| Troubleshooting | [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors) |

## Key/Salt

<Accordion title="I am facing the following error while trying to integrate Android Mobile SDK." icon="fa-info-circle">


  Value \<!DOCTYPE of type java.lang.String cannot be converted to JSONObject (Error code 5014)

  If you are using Test Key & Test Salt, configure the **setIsProduction** parameter as false. Otherwise, if you are using Production Key and Salt, configure the **setIsProduction** parameter as true. For more information, refer to [CheckoutPro SDK go-live checklist](doc:integration-steps-android-checkout-pro).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

## **PayU CheckoutPro**

### **General**

<Accordion title="Is PayU CheckoutPro for Mobile SDK PCI-DSS compliant?" icon="fa-info-circle">


  Yes, PayU CheckoutPro for Mobile SDK is PCI-DSS compliant, ensuring secure payment processing for your mobile app users.

  **Related documentation**

  * For CheckoutPro security and PCI scope, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Android Checkout Pro SDK](doc:android-checkoutpro-sdk).


</Accordion>

<Accordion title="PayU Android SDK has various SDKs and how do I choose them for my app?" icon="fa-info-circle">


  The best SDK for you will depend on your specific needs and requirements.

  The [Choose your SDK](doc:explore-android-sdks) table in the explore android SDK document outlines the process you need to follow and decide which SDK to use for your app, based on your specific needs and requirements.

</Accordion>

<Accordion title="What are the different customization options available for PayU Checkout Pro SDK for Android?" icon="fa-info-circle">


  There are several customization options available, including:

  * Customizing the PayU payment page’s look and feel to match your app branding
  * Integrating with the payment gateway or payment service provider
  * Implementing custom payment flows, such as split payments or installment payments

  For more information, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="Can I customize the payment modes in PayU Checkout Pro?" icon="fa-info-circle">

  Yes, you can customize the payment modes. For more information, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="How can I modify the color scheme in Android SDK integration?" icon="fa-info-circle">


  You can modify the color scheme and theme used in the PayUCheckoutPro SDK by providing your own set of colors. For more information on how to change the color theme of the SDK, refer to [Modify Theme](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="How can I customize the look and feel of the PayU payment page?" icon="fa-info-circle">


  The PayU payment page’s look and feel can be customized using CSS stylesheets and JavaScript. You can customize the page’s layout, fonts, colors, and other visual elements to match their branding. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Can I integrate PayU Checkout Pro SDK with my own payment gateway or payment service provider?" icon="fa-info-circle">


  Yes, PayU Checkout Pro SDK can be integrated with any payment gateway or service provider. You can use the SDK to capture and process payment information and then send it to their own backend system for processing. For more information, refer to [Customize your Integration](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="How can I implement custom payment methods or gateways not supported by PayU Checkout Pro SDK?" icon="fa-info-circle">


  Custom payment methods or gateways can be implemented using the PayU Custom Checkout SDK. This SDK provides a flexible and extensible framework for integrating with any payment method or gateway. For more information, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="Can I implement custom payment flows using PayU Checkout Pro SDK?" icon="fa-info-circle">


  Yes, custom payment flows can be implemented using the SDK’s flexible API. You can use the API to implement complex payment flows, such as split payments, installment payments, or any other custom payment flow required for their business.

  **Related documentation**

  * For advanced configuration, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations).

</Accordion>

<Accordion title="What is the difference between the implementation of PayU CheckoutPro in the Android and Apple iOS platforms?" icon="fa-info-circle">

  * **Development Environment**: The Android SDK requires Android Studio and Gradle to be installed, while the iOS SDK requires Xcode and CocoaPods to be installed.
  * **Language**: The Android SDK is written in Java, while the iOS SDK is written in Objective-C and Swift.
  * **Integration Method**: The Android SDK is integrated using the Gradle build system, while the iOS SDK is integrated using the CocoaPods dependency manager.
  * **UI Components**: The UI components used in the Android and iOS SDKs are different due to the differences in the platform’s design guidelines. For example, the Android SDK uses Android-specific UI components such as the EditText view, while the iOS SDK uses iOS-specific UI components such as the UITextField view.
  * **Payment Methods**: The payment methods supported by the Android and iOS SDKs are the same, including credit cards, debit cards, net banking, and UPI.
  * **Tokenization**: Both the Android and iOS SDKs support tokenization, which allows users to save their payment information for future transactions.
  * **Testing**: The Android SDK provides a test mode that allows developers to test the integration without making actual payments, while the iOS SDK provides a sandbox environment for testing.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="What are the steps involved in integrating PayU CheckoutPro for Mobile SDK?" icon="fa-info-circle">


  The integration process involves registering your application on the PayU developer dashboard, downloading and integrating the PayU CheckoutPro Mobile SDK into your Android project, and then using the SDK to initiate and process payment requests from your mobile app.

  **Related documentation**

  * For step-by-step integration, refer to [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="What payment methods are supported by PayU CheckoutPro for Mobile SDK?" icon="fa-info-circle">


  PayU CheckoutPro for Mobile SDK supports multiple payment methods including credit/debit cards, UPI, Wallets, and Net Banking.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Does PayU SDK supports<Glossary>SSL Pinning</Glossary>?" icon="fa-info-circle">


  No, PayU SDKs does not support <Glossary>SSL Pinning</Glossary> due to business continuity.

  **Related documentation**

  * For security best practices, refer to [Hash Generation](doc:hash-generation) and [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Can I change the order of payment modes displayed on PayU Payment page that is implemented using CheckoutPro?" icon="fa-info-circle">


  Yes, you can change the order of payment modes displayed on the PayU Payment page by PayU either using SDK manually or using Dashboard. For more information, refer to:

  * **Manually**: [Customize Your Integration](doc:android-checkoutpro-custom-integrations) > [Set Checkout Payment Modes Order](doc:android-checkoutpro-custom-integrations).
  * **Dashboard**: [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Can I customize the PayU CheckoutPro for Mobile SDK UI to match my app’s design?" icon="fa-info-circle">


  Yes, PayU CheckoutPro for Mobile SDK provides a customizable UI that allows you to adjust the look and feel of the payment gateway to match your app’s design. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What is Dynamic configuration in PayU Checkout Pro SDK for Android?" icon="fa-info-circle">


  Dynamic configuration allows you to update various payment-related settings in real-time using the PayU Dashboard. These settings can include payment methods, transaction limits, and other checkout-related parameters. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What are the use cases for dynamic configuration in PayU Checkout Pro SDK for Android?" icon="fa-info-circle">


  Dynamic configuration can be useful in the following scenarios:

  * Adding or removing payment methods based on user preferences or availability in different countries or regions.
  * Changing transaction limits or fees based on business requirements or market conditions.
  * Updating payment-related settings based on user feedback or analytics data.
  * Configuring payment-related settings for testing and debugging purposes.

  For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="How can I use Dynamic Configuration in PayU Checkout Pro SDK for Android?" icon="fa-info-circle">


  To use dynamic configuration, you can log in to the PayU Dashboard and update the relevant settings in the Checkout Pro section. The SDK will automatically fetch the updated settings and apply them to the payment flow. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Can I update payment methods dynamically using the PayU Dashboard?" icon="fa-info-circle">

  ?

  Yes, payment methods can be added or removed dynamically using the Dashboard. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What other payment-related settings can be updated dynamically using the Dashboard?" icon="fa-info-circle">


  Other payment-related settings that can be updated dynamically include transaction limits, payment fees, checkout flow settings, and more. These settings can be customized based on the your business requirements and market conditions. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Can I customize the PayU CheckoutPro Mobile SDK without modifying the SDK code?" icon="fa-info-circle">


  Yes, PayU CheckoutPro Mobile SDK allows customization without modifying the SDK code. This is achieved by using the SDK’s XML and resource files to override the default UI elements. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="How do I customize the PayU CheckoutPro Mobile SDK for my Android app?" icon="fa-info-circle">


  To customize the PayU CheckoutPro Mobile SDK, you need to create an XML file that defines the custom styles and layouts, and then use the SDK’s resource files to override the default GUI elements. You can also customize the colors and images used in the payment screens.

  **Related documentation**

  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Can I customize the PayU CheckoutPro Mobile SDK to match my app’s branding?" icon="fa-info-circle">


  Yes, you can customize the PayU CheckoutPro Mobile SDK to match your app’s branding by using your app’s color scheme, fonts, and logos in the payment screens. For more information, refer to [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What is the impact of customizing the PayU CheckoutPro Mobile SDK on future updates?" icon="fa-info-circle">


  If you customize the PayU CheckoutPro Mobile SDK, future updates to the SDK may require you to update your customizations as well. You should carefully review the release notes before updating to a new version of the SDK.

  **Related documentation**

  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).
  * For version updates, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Is technical support available for customized integration with PayU CheckoutPro Mobile SDK?" icon="fa-info-circle">


  Yes, PayU provides technical support for customized integration with PayU CheckoutPro Mobile SDK. You can reach out to <Anchor label="PayU Support" target="_blank" href="https://help.payu.in/">PayU Support</Anchor> for assistance with any customization issues or questions.

  **Related documentation**

  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What is CustomBrowser Configuration?" icon="fa-info-circle">


  CustomBrowser Configuration is the process of configuring the PayU Mobile Android SDK to use a custom browser for payment processing.

  **Related documentation**

  * For CustomBrowser setup, refer to [Integration Steps - CustomBrowser](doc:integration-steps-android-customer-browser) and [CustomBrowser SDK](doc:custom-browser-sdk).

</Accordion>

<Accordion title="How can I configure the PayU Mobile Android SDK to use a CustomBrowser?" icon="fa-info-circle">


  To configure the PayU Mobile Android SDK to use a custom browser, you need to implement the CustomBrowser class and configure the SDK to use this class for payment processing. For more information, refer to [Integration with CustomBrowser](doc:integration-steps-android-customer-browser).

</Accordion>

<Accordion title="What are the advantages of using a CustomBrowser for payment processing?" icon="fa-info-circle">


  Using a custom browser for payment processing provides a more seamless payment experience for the user, as the payment screens can be customized to match the look and feel of the app. For more information, refer to [Integration with CustomBrowser](doc:custom-browser-sdk).

</Accordion>

<Accordion title="How does the CustomBrowser affect the security of payment processing?" icon="fa-info-circle">


  CustomBrowser does not affect the security of the payment processing, as the SDK still uses the same secure encryption and authentication mechanisms to process payment requests.

  **Related documentation**

  * For CustomBrowser integration details, refer to [Integration Steps - CustomBrowser](doc:integration-steps-android-customer-browser).

</Accordion>

### **Convenience Fee**

<Accordion title="What is a convenience fee in the context of payment processing?" icon="fa-info-circle">


  A convenience fee is an additional fee charged to customers for the convenience of using a particular payment method. It is often used to cover the costs of processing credit card payments, which can be more expensive for merchants than other payment methods. For more information, refer to [Convenience Fee Integration for Android](doc:android-checkoutpro-setupconveniencefee).

</Accordion>

<Accordion title="How can I integrate a convenience fee using PayU Checkout Pro SDK for iOS?" icon="fa-info-circle">


  To integrate a convenience fee, you can use the SDK’s Convenience Fee API to add an additional fee to the payment amount based on the selected payment method. For more information, refer to [Convenience Fee Integration for Android](doc:android-checkoutpro-setupconveniencefee).

</Accordion>

<Accordion title="Can I customize the convenience fee calculation logic using PayU Checkout Pro SDK for iOS?" icon="fa-info-circle">


  Yes, you can customize the convenience fee calculation logic based on their business requirements. The SDK provides a flexible API that allows you to set the convenience fee amount based on various criteria, such as the payment method selected, transaction amount, or customer location. For more information, refer to [Convenience Fee Integration for Android](doc:android-checkoutpro-setupconveniencefee).

</Accordion>

<Accordion title="What are the different types of convenience fees that can be charged using PayU Checkout Pro SDK for iOS?" icon="fa-info-circle">


  You can charge convenience fees based on different criteria, such as:

  * A percentage of the transaction amount
  * A fixed amount per transaction
  * A combination of both percentage and fixed-amount fees

  For more information, refer to [Convenience Fee Integration for Android](doc:android-checkoutpro-setupconveniencefee).

</Accordion>

<Accordion title="How can I display the convenience fee to customers during the checkout process using PayU Checkout Pro SDK for iOS?" icon="fa-info-circle">


  The convenience fee amount can be displayed to customers on the payment page using the SDK’s convenience fee API. You can customize the display format and location of the convenience fee on the payment page to provide a transparent and seamless checkout experience for customers.

  **Related documentation**

  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

## **Hashing**

<Accordion title="What is hashing?" icon="fa-info-circle">


  Hashing is a process of converting a string of data into a fixed-length string of characters. Hashing is used to generate a secure hash key that is sent along with payment information to ensure the transaction’s integrity.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="How is the hash key generated in PayU?" icon="fa-info-circle">


  The hash key is generated using a hashing algorithm called SHA-512, which is a secure one-way hash function. The SDK takes all the transaction details and a merchant salt key as input and computes the hash key using the SHA-512 algorithm.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="What is a merchant key and Salt in PayU Checkout Pro SDK?" icon="fa-info-circle">


  The merchant Key and Salt is a secret key provided by PayU to merchants, which is used in conjunction with the transaction details to generate the hash key. The Key and Salt must be kept secret and is not shared with anyone else.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="How is reverse hashing used in PayU Checkout Pro SDK?" icon="fa-info-circle">


  Reverse hashing is used to verify the authenticity of the payment response received from PayU. The SDK computes the hash key using the same algorithm and merchant salt key used for generating the original hash key and compares it with the hash key received in the payment response. If they match, it confirms that the payment response is authentic.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="What happens if the hash key generated by the SDK does not match the one received in the payment response?" icon="fa-info-circle">


  If the hash keys do not match, it indicates that the payment response has been tampered with or is not authentic. In such cases, the payment transaction should be rejected, and you should contact [PayU Support](https://help.payu.in/) for further assistance.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="What is the formula used for hashing in PayU Checkout Pro SDK?" icon="fa-info-circle">


  The formula used for hashing in PayU Checkout Pro SDK is as follows:

  ```plaintext
  hash_key = SHA512(transaction_details + '|' + merchant_salt)
  ```

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="What does the Hash calculation formula consist of?" icon="fa-info-circle">


  The formula consists of two main components:

  * **Transaction details**: This includes all the relevant transaction details, such as the transaction amount, payment mode, currency, etc. These details are concatenated together in a specific format and used as input for the hashing algorithm.
  * **Merchant Key and Salt**: This is a secret key provided by PayU to merchants, which is used to add an extra layer of security to the hashing process.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="What is SHA512?" icon="fa-info-circle">


  SHA512 is a hashing algorithm that generates a fixed-length, 512-bit hash value from input data. It is a one-way function, meaning that the input cannot be retrieved from the output hash value.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="Why is the tilde symbol (‘|’) used in the Hash calculation formula?" icon="fa-info-circle">


  The ‘|’ character is used as a separator between the transaction_details and the merchant_salt in the formula. This helps to ensure that the hashing algorithm processes the input data correctly and generates a consistent hash value.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

## **Native OTP Integration**

<Accordion title="What is Native OTP?" icon="fa-info-circle">


  Native OTP is a feature provided by PayU that allows the user to enter the OTP directly in the app, instead of being redirected to a third-party website or app for OTP verification.

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).
  * For callback handling, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk) and [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk).

</Accordion>

<Accordion title="How can I integrate Native OTP with PayU Android SDK?" icon="fa-info-circle">


  To integrate Native OTP with PayU Android SDK, you need to use the `setOtpFetchHandler` method provided by the SDK to fetch the OTP from the user and pass it to the SDK for verification.

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).

</Accordion>

<Accordion title="Can I customize the Native OTP user interface in my app?" icon="fa-info-circle">


  Yes, you can customize the Native OTP user interface in your app by using the PayU Mobile Android SDK’s customization options.

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="Which payment methods support Native OTP integration with PayU Android SDK?" icon="fa-info-circle">


  PayU Android SDK supports Native OTP integration for the following payment modes:

  * Credit Card
  * Debit Card
  * EMI (Credit Card or Debit Card)
  * BNPL

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).

</Accordion>

<Accordion title="Is there a limit to the number of attempts to enter OTP for verification?" icon="fa-info-circle">


  Yes, there is a limit to the number of attempts to enter OTP for verification. After a certain number of failed attempts, the transaction is declined.

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).

</Accordion>

<Accordion title="Can I test the Native OTP integration before going live?" icon="fa-info-circle">


  Yes, you can test the Native OTP integration in a test environment before going live. PayU provides a test environment for testing the Native OTP integration.

  **Related documentation**

  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

## **UPI Integration**

<Accordion title="How can I integrate UPI with PayU Android SDK?" icon="fa-info-circle">


  To integrate UPI with PayU Android SDK, you need to use the `setPaymentOption` method provided by the SDK to select UPI as the payment option and configure the UPI payment parameters.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Which UPI apps are supported by PayU Android SDK?" icon="fa-info-circle">


  PayU Android SDK supports all UPI apps that are compatible with the UPI payment system.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Can I customize the UPI payment user interface in my app?" icon="fa-info-circle">


  Yes, you can customize the UPI payment user interface in your app by using the PayU Mobile Android SDK’s customization options.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What are the different types of UPI transactions supported by PayU Android SDK?" icon="fa-info-circle">


  PayU Android SDK supports UPI transactions for sending money, requesting money, and checking the balance in the user’s bank account.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Is technical support available for UPI integration with PayU Android SDK?" icon="fa-info-circle">


  Yes, PayU provides technical support for UPI integration with PayU Android SDK. You can reach out to the <Anchor label="PayU support team" target="_blank" href="https://help.payu.in">PayU support team</Anchor> for assistance with any integration issues or questions.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Can I test the UPI integration before going live?" icon="fa-info-circle">


  Yes, you can test the UPI integration in a test environment before going live. PayU provides a test environment for testing UPI integration.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="Why Android and iOS are sending different responses in UPI and Intent app flow?" icon="fa-info-circle">


  Based on the Android or iOS platform, PayU sends different responses in both payment Modes (UPI Collect/UPI Intent). Hence, you have to handle those responses at your end.

  **For Android:**

  * In the case of UPI intent/InApp flow,  you will not receive a callback response in the`surl` or `furl`. In this case, the format of the PayU response received will be different from other payment options that you can handle accordingly. For handling `surl` or `furl`, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).
  * If you get **mihpayid** in the PayU response, consider it as a **PayU ID/ID**

  **For IOS**:

  * In the case of UPI intent and Collect flow, you will not receive a callback response in SURL/FURL. In this case, the format of the PayU response received will be different from other payment options that you can handle accordingly. For handling `surl` or `furl`, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).
  * If you get **mihpayid** in the PayU response, consider it as a PayU ID/ ID.

</Accordion>

## **PhonePe Integration**

<Accordion title="How can I integrate PhonePe with PayU Android SDK?" icon="fa-info-circle">


  To integrate PhonePe with PayU Android SDK, you need to use the `setPaymentOption` method provided by the SDK to select PhonePe as the payment option and configure the PhonePe payment parameters.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Which countries are supported for PhonePe integration with PayU Android SDK?" icon="fa-info-circle">


  PhonePe integration with PayU Android SDK is currently available only in India.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Can I customize the PhonePe payment user interface in my app?" icon="fa-info-circle">


  Yes, you can customize the PhonePe payment user interface in your app by using the PayU Mobile Android SDK’s customization options.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="What are the different types of PhonePe transactions supported by PayU Android SDK?" icon="fa-info-circle">


  PayU Android SDK supports PhonePe transactions for making payments, requesting payments, and checking the status of a payment.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="What is the difference between PayU CheckoutPro and Non-Seamless?" icon="fa-info-circle">


  **PayU CheckoutPro** and **Non-Seamless** integration are the same. For more information, refer to [Explore Android SDKs](doc:explore-android-sdks).

</Accordion>

<Accordion title="Why do we need so many hashes?" icon="fa-info-circle">


  For security purposes, the hash is mandatory. Whenever you connect to the PayU server you need a hash. For every API, there is a separate hash because all APIs are public.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="Do we need to calculate Reverse Hash?" icon="fa-info-circle">


  It is mandatory to calculate the reverse hash on your surl/furl to validate a transaction at your end. Otherwise, the transaction may be hacked or tampered with.

  For more information, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk) and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="Does the merchant need PCI/DSS certificate?" icon="fa-info-circle">


  When the merchant collects the customer’s card details on their website/server and posts them to PayU. The merchant must be PCI-DSS certified in this case. For further information on PCI-DSS certification, contact your PayU Key Account Manager (KAM).

  **Related documentation**

  * For hosted checkout PCI scope, refer to [Android Checkout Pro SDK](doc:android-checkoutpro-sdk) and [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Do all the Mobile SDKs support UPI Intent flow?" icon="fa-info-circle">


  Only the following integrations in Android SDK work through Intent:

  * [PhonePe](doc:android-phonepe-sdk)
  * [Google Pay](doc:android-google-pay-sdk)
  * PayTM

</Accordion>

<Accordion title="Can merchants generate hash from PayU SDK?" icon="fa-info-circle">


  Yes, merchants can also generate a hash from PayU SDK but it’s not recommended because in this case key and salt will be hardcoded so anyone can use key and salt for making payment and it’s not secure.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="We want our users to make in-app payments using UPI apps installed on our customer’s mobile. We don’t want to enter any security-related details such as merchant key, secret, or hash on the Android app to avoid security risks. We want the Android-side implementation to be as simple as possible. The Android app should be able to initiate the transaction using a unique transaction ID provided by our backend. Our backend will get this transaction ID using PG-provided APIs. Please suggest how is this possible if possible." icon="fa-info-circle">


  You can use PayU CheckoutPro SDK or Non-seamless SDK (PayU UI) in PayU Android SDK integration. For more information, refer to the following:

  * [Android Checkout Pro SDK](doc:android-checkoutpro-sdk)
  * Sample App: [CheckoutPro Sample App](doc:sample-app)

</Accordion>

<Accordion title="Is there a tool to test hash generation?" icon="fa-info-circle">


  For more information on using the tools to test hash, refer to [Hash generation Tool](https://payuhashgeneration.herokuapp.com/).

  The merchant can check if he is calculating hash correctly by entering the same parameters using the above tool and then test the hashes generated with the hashes he is getting from his code.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="Why do we need to use surl and furl in CustomBrowser?" icon="fa-info-circle">


  When the transaction succeeds, PayU posts the response to the surl, and if the transaction fails PayU posts the response to the furl provided in post parameters while making a payment request.

  For information on using surl and furl, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk).

</Accordion>

<Accordion title="What is the session time-out period for the PayU gateway? That is, if I do not enter any details, confirm, or cancel payment for a significant amount of time, will I get a session expired message? If yes, what is that time and is it configurable?" icon="fa-info-circle">


  The PayU page will not expire, however, the PayU ID generated will be expired or bounce if the customer lands on the payment page for three hours and is left idle. Also, after three hours if the customer enters the card details, a new PayUid will be generated and the transaction will go through.

  **Related documentation**

  * For transaction timeout behaviour, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Does PayU accept the following card types?" icon="fa-info-circle">

  * **Master**
  * **Visa**
  * **Maestro(both 19 & 16 Digit)**
  * **Rupay**
  * **Amex**

  Yes, the above-listed card types are accepted.

  **Related documentation**

  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="What is the maximum character length for a card number?" icon="fa-info-circle">


  For Maestro 19, 16 otherwise. For more information, refer to [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="What is the maximum character length for CVV?" icon="fa-info-circle">


  The maximum character length is 4 for Amex cardholders, and 3 otherwise.

  **Related documentation**

  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="I am using CustomBrowser version\<7.4.0. How can I update the SDK to avail UPI payment modes?" icon="fa-info-circle">


  With version 7.4.0, PayU has optimized the SDK Offerings for you. After you update this SDK, the UPI transaction offering will be removed. The UPI Transactions offering is added in another SDK that supports the complete UPI portfolio – UPI Collect transactions, UPI Intent transactions, Tez(GPay) (In-App, Intent & Collect) Flows and PhonePe Flows, and SamsungPay. For more information on UPI SDK to accept UPI payments, refer to [Android UPI integration](doc:card-number-formats).

</Accordion>

<Accordion title="I am a CustomBrowser Merchant version >=7.4.0. I have added UPI SDK for UPI offering(Generic Intent and UPI Collect). I would like to add Google, PhonePe, and Samsung Pay payment options. What should I do?" icon="fa-info-circle">


  You just need to add PayU Gradle dependencies for [GooglePay](doc:android-google-pay-sdk), [Phonepe](doc:android-phonepe-sdk), and Samsung Pay. Generate _PostData_ according to the payment option you choose.

</Accordion>

<Accordion title="I am a UPI SDK merchant(Directly UPI SDK not through CustomBrowser), I would like to add GooglePay, PhonePe, or SamsungPay." icon="fa-info-circle">


  You just need to add PayU Gradle dependencies for [Googlepay](doc:android-google-pay-sdk), [Phonepe](doc:android-phonepe-sdk), and Samsung Pay and generate `PostData` for the same reference [Postdata through UPI SDK](doc:integration-steps-android-upi-sdk).

</Accordion>

<Accordion title="Is PG SDK mandatory to use with CustomBrowser?" icon="fa-info-circle">


  PG SDK is not mandatory to make payments with CustomBrowser. You can create `PostData` of its own.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="How to switch the environment from Testing to Production in PayU SDK?" icon="fa-info-circle">


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

  **Related documentation**

  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="Why is enter OTP manually button not visible on CB when the Material theme is used?" icon="fa-info-circle">


  To fix this problem, use the following code block in your **styles.xml** file:

  ```xml
  <style name="cb_approve_otp" parent="android:Widget.Button">
        <item name="android:textSize">@dimen/cb_fourteenScaled</item>
        <item name="android:textColor">#FFFFFF</item>
        <item name="backgroundTint">@color/cb_otpColor</item>
  </style>
  ```

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For Native OTP setup, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="How to fix the build error after adding the PayUCheckoutPro SDK gradle dependency?" icon="fa-info-circle">


  After adding the _PayUCheckoutPro_ SDK gradle dependency, if the build error similar to the following is received, include the parameter as indicated (after the error screenshot):

  <Image align="center" border={false} src="https://files.readme.io/cc69622a5272a649cbe36381aed4ec5e391ed71704966ae3a05feb8a3aba1924-android-faq_error1.png" />

  Add the following parameter in the \<application> tag of your app’s **AndroidManifest.xml** file.

  ```plaintext
  tools:replace="android:theme"
  ```

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).

</Accordion>

<Accordion title="When I was compiling my Android implementation, the following exception occurred in the compiler:" icon="fa-info-circle">


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

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For version updates, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

<Accordion title="I want to use GPay for collecting payments and it requires the S2S (Server-to-Server integration) flag to be enabled. How do I enable Server-to-Server integration for my account?" icon="fa-info-circle">


  You need to contact your PayU Key Account Manager to enable Server-to-Server integration.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="Can I generate hashes on my app?" icon="fa-info-circle">


  PayU recommends you generate the hashes on your server. Do not generate the hashes locally in your app as it will compromise the security of the transactions.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).

</Accordion>

<Accordion title="I was checking the [PayU Github](https://github.com/payu-intrepos) code for Ionic Cordova files and was unable to find the integration code." icon="fa-info-circle">


  The JS code for Ionic Cordova can be accessed from the following location:

  [https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js](https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js)

  **Related documentation**

  * For CheckoutPro integration, refer to [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Should I make a payment request using the Payment (_payment) API for Android?" icon="fa-info-circle">

  You need not use the Payment API if you are using PayU Mobile SDK, as PayU Mobile SDK will call all the APIs internally.

  **Related documentation**

  * For mobile SDK integration, refer to [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="Should I use the customer’s VPA to enable users to make payments through any UPI app installed on his/her mobile?" icon="fa-info-circle">


  If you want to use collect flow, it is mandatory to enter VPA, otherwise, it is not required.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).

</Accordion>

<Accordion title="What is the amount data format in PayU SDK?" icon="fa-info-circle">


  In PayU SKD, always pass String value in amount field for iOS and Android.

  **Related documentation**

  * For parameter formats, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

</Accordion>

## Upgrade

<Accordion title="How much time does it take to update the SDK in code to upgrade to the latest version of SDK?" icon="fa-info-circle">


  To update the SDK it takes only 5 – 10 mins. If you are facing any issues in updating the SDK, you can contact <Anchor label="PayU Support" target="_blank" href="https://help.payu.in/">PayU Support</Anchor>.

  **Related documentation**

  * For version updates, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).
  * For test credentials and parameter formats, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and [Card Number Formats](doc:card-number-formats).

</Accordion>

