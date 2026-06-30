---
title: '[Review]New Android SDK FAQs'
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: '[Review]New Android SDK FAQs'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section contains **new FAQs** proposed for the live [FAQs - Android SDK](doc:faqs-android-sdk) page. Content already published in the live page has been removed from this review draft.


## Getting Started

<Accordion title="I am getting a build error after adding PayUCheckoutPro SDK gradle dependency. How do I fix it?" icon="fa-info-circle">


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

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="I am getting a Java compiler exception when compiling my Android implementation. What should I do?" icon="fa-info-circle">


  If you encounter an exception like:

  ```
  java.lang.AssertionError: annotationType(): unrecognized Attribute name MODULE
  ```

  This typically indicates a Java version compatibility issue. Try upgrading your Gradle version. Update the line:

  ```gradle
  classpath 'com.android.tools.build:gradle:4.1.0'
  ```

  Upgrade to a newer version and ensure your Java Development Kit (JDK) version is compatible with the Gradle version.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What are the minimum requirements for integrating PayU Android SDK?" icon="fa-info-circle">


  The minimum requirements include:
  - Android Studio with Gradle build system
  - Minimum Android SDK version (API level) as specified in the SDK documentation
  - Java Development Kit (JDK) compatible with your Gradle version
  - Internet permission in your AndroidManifest.xml

  For specific version requirements, refer to the integration documentation for the SDK you're using.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).


</Accordion>

<Accordion title="How do I get started with PayU Android SDK integration?" icon="fa-info-circle">


  To get started:
  1. Register your application on the PayU developer dashboard
  2. Obtain your Merchant Key and Salt from the dashboard
  3. Download and integrate the PayU Android SDK into your project
  4. Configure the SDK with your credentials
  5. Test the integration using test credentials

  For detailed steps, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) or choose your SDK from [Explore Android SDKs](doc:explore-android-sdks).

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="How do I fix build errors related to theme conflicts after adding PayUCheckoutPro SDK?" icon="fa-info-circle">


  If you encounter build errors related to theme conflicts, add the following parameter in the `<application>` tag of your app's `AndroidManifest.xml` file:

  ```xml
  tools:replace="android:theme"
  ```

  Also ensure you have the tools namespace declared in your manifest:
  ```xml
  xmlns:tools="http://schemas.android.com/tools"
  ```

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).


</Accordion>

## PayU CheckoutPro

<Accordion title="How do I test my Android SDK integration before going live?" icon="fa-info-circle">


  You can test your integration using PayU's test environment:
  1. Use Test Key and Test Salt from your PayU dashboard
  2. Set the `setIsProduction` parameter to `false` in your code
  3. Use test card numbers and test credentials provided in the documentation
  4. Test various payment methods (cards, UPI, net banking, etc.)
  5. Verify the payment callbacks and responses

  For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

</Accordion>

<Accordion title="What should I do if the payment page is not loading in my Android app?" icon="fa-info-circle">


  If the payment page is not loading, check the following:
  1. Verify your internet connection and permissions in AndroidManifest.xml
  2. Ensure you're using the correct environment (test/production) with matching Key and Salt
  3. Check if the hash is generated correctly on your server
  4. Verify that all required parameters are being passed correctly
  5. Check the logs for any error messages
  6. Ensure your app has the necessary network security configuration

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).


</Accordion>

<Accordion title="How do I handle payment failures in Android SDK?" icon="fa-info-circle">


  Payment failures can be handled through:
  1. **Callback methods**: Implement the payment result callbacks to receive success/failure responses
  2. **Error codes**: Check the error codes in the response to identify the specific failure reason
  3. **User feedback**: Display appropriate error messages to users based on the error code
  4. **Retry mechanism**: Allow users to retry the payment if the failure is due to network or temporary issues

  For detailed error handling, refer to [Error Handling](doc:error-handling).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

<Accordion title="Can I use PayU Android SDK in a background service or worker thread?" icon="fa-info-circle">


  PayU Android SDK operations should be performed on the main/UI thread. Payment UI components require the Android main thread to function properly. However, hash generation and network calls can be performed on background threads, but ensure you switch back to the main thread before calling SDK methods that display UI.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).


</Accordion>

<Accordion title="What happens if the user closes the app during a payment transaction?" icon="fa-info-circle">


  If the user closes the app during a payment transaction:
  1. The transaction may still be processing on PayU's servers
  2. You should implement proper callback handling to receive the payment response when the app is reopened
  3. Use `surl` and `furl` to receive payment responses even if the app is closed
  4. Implement proper state management to handle such scenarios

  **Related documentation**

  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).


</Accordion>

<Accordion title="How do I switch between test and production environments in Android SDK?" icon="fa-info-circle">


  To switch between test and production environments:
  1. Use Test Key and Test Salt for testing, and Production Key and Salt for production
  2. Set the `setIsProduction` parameter accordingly:
  - `false` for test environment
  - `true` for production environment
  3. Remove test metadata from AndroidManifest.xml when going to production
  4. Ensure you're using the correct API endpoints for each environment

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What payment methods require additional setup or configuration?" icon="fa-info-circle">


  Some payment methods may require additional setup:
  - **UPI**: May require VPA for collect flow
  - **Google Pay**: Requires S2S (Server-to-Server) integration flag to be enabled
  - **PhonePe**: Requires specific SDK integration
  - **EMI**: Requires bank and card eligibility checks
  - **BNPL**: Requires merchant approval and configuration

  Contact your PayU Key Account Manager for enabling specific payment methods.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For payment method details, refer to [Error Handling](doc:error-handling), [Card Number Formats](doc:card-number-formats), and [Additional Info for Payment APIs](ref:addl_info-payment-apis).


</Accordion>

<Accordion title="How do I debug issues with PayU Android SDK integration?" icon="fa-info-circle">


  To debug integration issues:
  1. Enable logging in your app to see SDK logs
  2. Check the Android logcat for error messages
  3. Verify all parameters being sent to the SDK
  4. Test with PayU's test credentials first
  5. Use PayU's hash generation tool to verify hash calculations
  6. Check network requests and responses
  7. Review the integration documentation for common issues
  8. Contact PayU Support with specific error codes and logs

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="Can I use multiple PayU SDKs together in the same Android app?" icon="fa-info-circle">


  Yes, you can use multiple PayU SDKs together, such as:
  - CheckoutPro SDK with UPI SDK
  - CheckoutPro SDK with Google Pay SDK
  - CheckoutPro SDK with PhonePe SDK

  Ensure you follow the integration steps for each SDK and handle conflicts in dependencies if any. Refer to the specific SDK documentation for compatibility information.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).


</Accordion>

<Accordion title="What is the difference between static hash and dynamic hash in Android SDK?" icon="fa-info-circle">


  - **Static Hash**: Generated once and can be reused for multiple transactions. Used for certain payment flows but less secure.
  - **Dynamic Hash**: Generated fresh for each transaction with transaction-specific parameters. More secure and recommended for production use.

  PayU recommends using dynamic hash for better security. For more information, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk) or [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

</Accordion>

<Accordion title="How do I handle deep links or redirects after payment in Android SDK?" icon="fa-info-circle">


  Deep links and redirects are handled through:
  1. **surl (Success URL)**: Called when payment is successful
  2. **furl (Failure URL)**: Called when payment fails
  3. **Intent filters**: Configure AndroidManifest.xml to handle payment callbacks
  4. **Activity result**: Use Activity result callbacks for SDK-based flows

  For detailed implementation, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).

</Accordion>

<Accordion title="What should I do if I receive an invalid hash error?" icon="fa-info-circle">


  If you receive an invalid hash error:
  1. Verify that you're using the correct Key and Salt (test vs production)
  2. Ensure the hash is generated on your server, not in the app
  3. Check that all parameters used in hash generation match the parameters sent to PayU
  4. Verify the hash generation formula and parameter order
  5. Use PayU's hash generation tool to test your hash calculation
  6. Ensure there are no extra spaces or encoding issues in parameters

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="Can I customize the payment success/failure messages in Android SDK?" icon="fa-info-circle">


  Yes, you can customize payment success/failure messages:
  1. Handle the payment callbacks in your app
  2. Display custom messages based on the payment response
  3. Use the SDK's customization options to modify the UI
  4. Implement your own error handling and user feedback

  The SDK provides callbacks that you can use to show custom messages to users.

  **Related documentation**

  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).


</Accordion>

## Troubleshooting

<Accordion title="Why is the &quot;Enter OTP manually&quot; button not visible when using Material theme in CustomBrowser?" icon="fa-info-circle">


  This issue occurs due to theme conflicts. To fix it, add the following code block in your `styles.xml` file:

  ```xml
  <style name="cb_approve_otp" parent="android:Widget.Button">
  <item name="android:textSize">@dimen/cb_fourteenScaled</item>
  <item name="android:textColor">#FFFFFF</item>
  <item name="backgroundTint">@color/cb_otpColor</item>
  </style>
  ```

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For Native OTP setup and customisation, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist) and [Native OTP Assist Customisations](doc:android-nativeotpassist-customisations).
  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).


</Accordion>

<Accordion title="What should I do if the SDK is not responding or payment page is blank?" icon="fa-info-circle">


  If the SDK is not responding or showing a blank page:
  1. Check your internet connection and network permissions
  2. Verify that all required parameters are being passed correctly
  3. Ensure the hash is generated correctly and matches the parameters
  4. Check Android logcat for any error messages
  5. Verify you're using the correct environment (test/production)
  6. Try clearing app cache and data
  7. Ensure you're using a supported Android version

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).


</Accordion>

<Accordion title="Why am I not receiving payment callbacks (surl/furl) in my Android app?" icon="fa-info-circle">


  If you're not receiving payment callbacks:
  1. Verify that `surl` and `furl` are correctly configured in your payment request
  2. Ensure your app can handle deep links or URL schemes
  3. Check AndroidManifest.xml for proper intent filters
  4. Verify that your server endpoints are accessible and responding
  5. For UPI Intent flow, note that callbacks may be handled differently
  6. Check if the app was closed during payment - implement proper state handling

  For more information, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).

</Accordion>

<Accordion title="How do I resolve dependency conflicts when integrating PayU Android SDK?" icon="fa-info-circle">


  If you encounter dependency conflicts:
  1. Check the SDK documentation for required dependency versions
  2. Use Gradle's dependency resolution strategies
  3. Exclude conflicting transitive dependencies if necessary
  4. Update your project's dependencies to compatible versions
  5. Use `./gradlew dependencies` to identify conflict sources
  6. Contact PayU Support if conflicts persist

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).


</Accordion>

<Accordion title="What should I do if payment transactions are failing with authentication errors?" icon="fa-info-circle">


  If you're getting authentication errors:
  1. Verify your Merchant Key and Salt are correct
  2. Ensure the hash is generated correctly on your server
  3. Check that you're using the correct environment (test/production)
  4. Verify all required authentication parameters are included
  5. Ensure your account is activated and in good standing
  6. Check if there are any account-level restrictions

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="Why are UPI payments not working in my Android app?" icon="fa-info-circle">


  If UPI payments are not working:
  1. Verify UPI SDK is properly integrated
  2. Check if UPI apps are installed on the device
  3. Ensure VPA is provided for UPI Collect flow
  4. Verify UPI is enabled for your merchant account
  5. Check device compatibility and Android version
  6. Review UPI integration documentation for specific requirements

  For more information, refer to [Android UPI SDK Integration](doc:integration-steps-android-upi-sdk).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

<Accordion title="Does `offerKey` format differ between Android and iOS in wrapper SDKs?" icon="fa-info-circle">


  Yes. In hybrid or wrapper SDKs (React Native, Flutter), platform-specific handling may be required:

  * **Android (native)**: Pass `offerKey` as a **String** (comma-separated for multiple offers).
  * **iOS (native)**: Pass `offerKey` as an **Array** of strings.

  If you use a cross-platform wrapper, apply conditional handling per platform. For native Android CheckoutPro, refer to [Create SKU-based Offers](doc:create-sku-based-offers-for-android-checkout-pro) and [Integration Steps](doc:integration-steps-android-checkout-pro).

</Accordion>

<Accordion title="How do I pass `offerKey` in PayU CheckoutPro for Android?" icon="fa-info-circle">


  Pass `offerKey` in your payment parameters when creating the CheckoutPro payment request. For SKU-based or enforcement offers, use `setEnforcementOfferKeys()` with a list of offer keys.

  For more information, refer to:

  * [Create SKU-based Offers for Android CheckoutPro](doc:create-sku-based-offers-for-android-checkout-pro)
  * [Integration Steps – Offers](doc:integration-steps-android-checkout-pro)

</Accordion>

<Accordion title="The PayU payment screen is stuck at the PayU logo and does not proceed. What should I check?" icon="fa-info-circle">


  If the SDK opens but hangs on the loading screen with no callbacks:

  1. **Hash generation**: Ensure your server returns a valid hash for every `generateHash()` callback from the SDK, including configuration hashes (for example, `get_sdk_configuration`). An "Invalid Command Name" error often indicates a missing or incorrect hash for a new SDK command.
  2. **Environment mismatch**: Confirm Test Key/Salt with `setIsProduction(false)`, or Production Key/Salt with `setIsProduction(true)`.
  3. **Network**: Verify internet permission and that the device can reach PayU endpoints.
  4. **SDK version**: Upgrade to the latest CheckoutPro SDK version and review [Version History](doc:change-logs) for breaking changes.
  5. **Logs**: Check Android logcat for hash or API errors before the screen hangs.

  For more information, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

<Accordion title="After upgrading CheckoutPro to version 3.2.0 or later, I get &quot;Invalid Command Name&quot; and the SDK does not open. How do I fix this?" icon="fa-info-circle">


  CheckoutPro 3.2.0+ introduces additional hash commands (for example, for SDK configuration and timer features). Your server-side hash endpoint must handle **all** hash names returned in the `generateHash()` callback—not only the payment hash.

  When the SDK requests a hash with a new command name (such as `get_sdk_configuration`), calculate the hash using the `CP_HASH_STRING` provided by the SDK:

  ```
  SHA-512(key|command|var1|salt)
  ```

  Return the computed hash in `onHashGenerated()` with the same hash name. Upgrade to the latest CheckoutPro version (3.2.0 or later) for timer and configuration support. For more information, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk) and [Version History](doc:change-logs).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

<Accordion title="Google Play Console shows a warning about orientation restrictions in PayU SDK activities. What should I do?" icon="fa-info-circle">


  Google Play may flag PayU SDK activities that set `android:screenOrientation="PORTRAIT"` (for example, `CheckoutActivity`, `CBActivity`, `NFCActivity`). From Android 16, these restrictions may be ignored on large-screen devices such as foldables and tablets.

  **Recommended actions:**

  1. Upgrade to the latest PayU Android SDK version, which includes orientation and large-screen compatibility fixes.
  2. Test the payment flow on tablets and foldables after upgrading.
  3. If the warning persists after upgrading, contact [PayU Support](https://help.payu.in/) with your SDK version and Play Console warning details.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="I am seeing ANR (Application Not Responding) reports related to PayU crash logger in Firebase. How do I resolve this?" icon="fa-info-circle">


  ANR reports pointing to `com.payu.crashlogger` during app startup are often caused by the SDK's crash reporting initialiser running on the main thread. Try the following:

  1. Upgrade to the latest recommended SDK versions for CheckoutPro, CustomBrowser, and Native OTP Assist.
  2. Apply any manifest changes recommended by PayU Support for your SDK combination.
  3. Exclude conflicting Material Design dependencies if advised (for example, when using Native OTP Assist).
  4. If ANRs persist, share Firebase ANR traces and your `build.gradle` dependencies with [PayU Support](https://help.payu.in/).

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For Native OTP setup and customisation, refer to [Integration Steps - Native OTP Assist SDK](doc:integration-steps-android-native-otp-assist) and [Native OTP Assist Customisations](doc:android-nativeotpassist-customisations).
  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).


</Accordion>

<Accordion title="Why are my UPI Intent payments not returning surl/furl callbacks?" icon="fa-info-circle">


  For UPI Intent and In-App flows on Android, you typically **do not** receive a callback on `surl` or `furl`. The SDK returns the payment result through its callback listener with a different response format.

  Handle the SDK callback directly and use the Verify Payment API on your server to confirm the final status. If you receive `mihpayid` or `id` in the response, treat it as the PayU transaction ID. For more information, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).

</Accordion>

## Upgrade

<Accordion title="How do I upgrade to the latest version of PayU Android SDK?" icon="fa-info-circle">


  To upgrade to the latest version:
  1. Update the SDK version in your `build.gradle` file
  2. Sync your project with Gradle files
  3. Review the release notes for breaking changes
  4. Update your code if there are any API changes
  5. Test thoroughly in the test environment before going live
  6. Update any customizations if they're affected by the upgrade

  Check the SDK's version history or changelog for specific upgrade instructions.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What should I check before upgrading the PayU Android SDK?" icon="fa-info-circle">


  Before upgrading:
  1. Review the release notes and changelog for the new version
  2. Check for any deprecated methods or breaking changes
  3. Verify compatibility with your current Android and Gradle versions
  4. Test the upgrade in a development environment first
  5. Backup your current implementation
  6. Check if any customizations need to be updated
  7. Review migration guides if available

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For customisation options, refer to [Customize Your Integration](doc:android-checkoutpro-custom-integrations) and [Dynamic Configuration using Dashboard](doc:dynamic-configuration-using-dashboard-copy).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="Will upgrading the SDK affect my existing integrations?" icon="fa-info-circle">


  Upgrading the SDK may affect your integration if:
  1. There are breaking changes in the API
  2. Required parameters have changed
  3. Callback methods have been modified
  4. Dependencies have been updated

  Always review the release notes and test thoroughly before deploying to production. Most minor version updates are backward compatible, but major version updates may require code changes.

  **Related documentation**

  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What is the timer feature in CheckoutPro SDK 3.2.0 and later?" icon="fa-info-circle">


  CheckoutPro SDK version 3.2.0 and later supports a transaction timeout timer on the payment page. This feature requires server-side hash support for the additional SDK configuration commands introduced in 3.2.x.

  To use the timer feature:

  1. Upgrade to CheckoutPro `3.2.0` or later (check [Version History](doc:change-logs) for the latest version).
  2. Update your server-side hash logic to handle all hash commands requested by the SDK.
  3. Test in the PayU test environment before going live.

  If the SDK does not open after upgrade, verify that your hash endpoint handles the new command names.

</Accordion>

## SDK Compatibility and Requirements

<Accordion title="What is the minimum Android version required for PayU Android SDK?" icon="fa-info-circle">


  The minimum Android version (API level) varies by SDK:
  - **CheckoutPro SDK**: Check the specific SDK documentation for minimum API level
  - **Core SDK**: Typically requires API level 21 (Android 5.0) or higher
  - **CustomBrowser SDK**: Check version-specific requirements
  - **UPI SDK**: Requires API level 21 or higher

  Refer to the specific SDK integration documentation for exact requirements.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).
  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).


</Accordion>

<Accordion title="Is PayU Android SDK compatible with Kotlin?" icon="fa-info-circle">


  Yes, PayU Android SDK is compatible with Kotlin. You can use the SDK in both Java and Kotlin projects. The SDK provides Java APIs that work seamlessly with Kotlin through interoperability.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).


</Accordion>

<Accordion title="Can I use PayU Android SDK with Jetpack Compose?" icon="fa-info-circle">


  PayU Android SDK is built using traditional Android Views. While you can use it in a Jetpack Compose project, you'll need to use `AndroidView` composable to embed the SDK's UI components. The SDK's payment flows will still use the traditional View system.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).


</Accordion>

<Accordion title="Does PayU Android SDK support ProGuard/R8 code obfuscation?" icon="fa-info-circle">


  Yes, PayU Android SDK supports ProGuard and R8. However, you may need to add specific ProGuard rules to prevent the SDK from being obfuscated. Check the SDK documentation for required ProGuard rules, or contact PayU Support for the latest rules.

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What permissions are required for PayU Android SDK?" icon="fa-info-circle">


  The required permissions typically include:
  - `INTERNET`: For network communication
  - `ACCESS_NETWORK_STATE`: To check network connectivity (optional but recommended)

  Some payment methods may require additional permissions:
  - UPI payments may require specific UPI app permissions
  - Location permissions for certain features (if applicable)

  Add these permissions in your `AndroidManifest.xml` file.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).
  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).


</Accordion>

<Accordion title="Can I use PayU Android SDK in a multi-module Android project?" icon="fa-info-circle">


  Yes, you can use PayU Android SDK in a multi-module project. Add the SDK dependency to the module where you'll be using it, or add it to a shared module if multiple modules need access. Ensure proper dependency management across modules.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).


</Accordion>

<Accordion title="Is PayU Android SDK compatible with Android App Bundle (AAB) format?" icon="fa-info-circle">


  Yes, PayU Android SDK is compatible with Android App Bundle (AAB) format. You can build and publish your app using AAB without any special configuration for the PayU SDK.

  **Related documentation**

  * For integration prerequisites and setup, refer to [Integration Steps](doc:integration-steps-android-checkout-pro) and [Explore Android SDKs](doc:explore-android-sdks).


</Accordion>

## Security

<Accordion title="Is it safe to store Merchant Key and Salt in my Android app?" icon="fa-info-circle">


  No, it is not safe to store Merchant Key and Salt in your Android app. These credentials should be kept on your server. Always generate hashes on your server and pass them to the Android app. Storing credentials in the app makes them vulnerable to reverse engineering.

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).


</Accordion>

<Accordion title="How can I ensure secure payment processing with PayU Android SDK?" icon="fa-info-circle">


  To ensure secure payment processing:
  1. Generate hashes on your server, not in the app
  2. Never store Merchant Key and Salt in the app
  3. Use HTTPS for all network communications
  4. Implement proper SSL certificate pinning if required (note: PayU SDK doesn't support SSL pinning)
  5. Validate payment responses using reverse hash verification
  6. Use ProGuard/R8 to obfuscate your code
  7. Keep the SDK updated to the latest version
  8. Follow Android security best practices

  **Related documentation**

  * For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).
  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For version updates and release notes, refer to [Version History](doc:change-logs) and [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="Does PayU Android SDK handle PCI-DSS compliance?" icon="fa-info-circle">


  Yes, PayU CheckoutPro SDK is PCI-DSS compliant. When using CheckoutPro SDK, card details are handled by PayU's secure payment pages, so you don't need PCI-DSS certification. However, if you collect card details directly in your app, you'll need PCI-DSS certification.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For payment method details, refer to [Error Handling](doc:error-handling), [Card Number Formats](doc:card-number-formats), and [Additional Info for Payment APIs](ref:addl_info-payment-apis).


</Accordion>

<Accordion title="How does PayU Android SDK protect sensitive payment data?" icon="fa-info-circle">


  PayU Android SDK protects sensitive data by:
  1. Using encrypted communication channels (HTTPS/TLS)
  2. Not storing sensitive payment information locally
  3. Using secure tokenization for saved payment methods
  4. Implementing secure hash-based authentication
  5. Following industry-standard security practices

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).


</Accordion>

<Accordion title="Can I implement additional security measures on top of PayU Android SDK?" icon="fa-info-circle">


  Yes, you can implement additional security measures:
  1. Implement certificate pinning at the app level (though PayU SDK doesn't support it internally)
  2. Add additional validation layers
  3. Implement fraud detection mechanisms
  4. Use secure storage for any app-specific data
  5. Implement proper session management
  6. Add logging and monitoring for security events

  **Related documentation**

  * For hash generation and server-side security, refer to [Hash Generation](doc:hash-generation) and [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk).

</Accordion>

## Testing and Development

<Accordion title="How do I test PayU Android SDK integration without making real payments?" icon="fa-info-circle">


  You can test using:
  1. **Test Environment**: Use Test Key and Test Salt from your PayU dashboard
  2. **Test Cards**: Use test card numbers provided in PayU documentation
  3. **Test UPI IDs**: Use test UPI IDs for UPI payment testing
  4. **Test Wallets**: Use test wallet credentials
  5. **Sandbox Mode**: Set `setIsProduction(false)` in your code

  For test credentials, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

</Accordion>

<Accordion title="Can I test PayU Android SDK integration on an emulator?" icon="fa-info-circle">


  Yes, you can test on an Android emulator. However, note that:
  1. Some payment methods (like UPI apps) may not work on emulators
  2. Network-related testing should work fine
  3. For UPI and wallet testing, you may need a physical device
  4. Ensure the emulator has proper network configuration

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="How do I enable debug logging for PayU Android SDK?" icon="fa-info-circle">


  Debug logging can be enabled by:
  1. Setting appropriate log levels in your app
  2. Checking Android logcat for SDK logs
  3. Enabling verbose logging in development builds
  4. Using PayU's debugging tools if available

  Note: Disable verbose logging in production builds for security and performance.

  **Related documentation**

  * For test credentials and go-live steps, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) and the Go-live Checklist in [Integration Steps](doc:integration-steps-android-checkout-pro).


</Accordion>

<Accordion title="What test scenarios should I cover before going live?" icon="fa-info-circle">


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

  **Related documentation**

  * For hash implementation details, refer to [Generate Dynamic Hash](doc:hash-generation-for-checkoutpro-sdk), [Generate Static Hash](doc:generate-static-hash-android-sdk-pro), and [Hash Generation](doc:hash-generation).
  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For callback handling and verification, refer to [Handling Redirect URLs (surl/furl) with Android SDK](doc:handling-redirect-urls-surlfurl-with-android-sdk), [Web Services for Android Core SDK](doc:web-services-for-android-core-sdk), and [Webhooks](doc:webhooks).


</Accordion>

## Payment Response and Verification

<Accordion title="The payment response does not include `mihpayid`. I see `id` instead. Is this expected?" icon="fa-info-circle">


  Yes. Depending on the SDK version and payment flow, the PayU transaction identifier may appear as `mihpayid` or `id` in the response. Treat either field as the **PayU ID** for reconciliation, status checks, and refunds.

  If you receive `id` instead of `mihpayid`, use `id` as the PayU transaction reference. For UPI Intent and In-App flows, the response format may also differ from card or net banking flows. For more information, refer to [Handling Redirect URLs](doc:handling-redirect-urls-surlfurl-with-android-sdk).

</Accordion>

<Accordion title="Should I use the Verify Payment API with PayU Android SDK?" icon="fa-info-circle">


  Yes. PayU recommends verifying every transaction on your server using the Verify Payment API, even when you receive a success or failure callback from the SDK. Network issues, app backgrounding, or UPI Intent flows can cause callbacks to be missed or delayed.

  For CheckoutPro, UPI SDK, and Core SDK integrations, call the Verify Payment API from your backend after the SDK callback. For more information, refer to [Verify Payment API](doc:web-services-for-android-core-sdk).

</Accordion>

<Accordion title="Can I use webhooks with PayU Android SDK instead of surl/furl?" icon="fa-info-circle">


  Yes. Webhooks are a server-side complement to `surl`/`furl` callbacks. Configure your webhook URL in the PayU Dashboard and ensure it returns HTTP `200 OK` when PayU posts transaction updates.

  For mobile SDK integrations:

  1. Continue handling SDK callbacks in your app for immediate user feedback.
  2. Use webhooks on your server for reliable, asynchronous transaction reconciliation.
  3. Whitelist PayU webhook IP addresses on your server if your firewall blocks incoming requests.

  For more information, refer to [Transaction Callback API](ref:transaction-callback-api).

</Accordion>

<Accordion title="What mandatory post parameters must I pass when initiating payment through Android SDK?" icon="fa-info-circle">


  At minimum, include:

  * `key` — Merchant Key
  * `txnid` — Unique transaction ID per request
  * `amount` — Transaction amount as a **String** (for example, `"100.00"`)
  * `productinfo` — Product or order description
  * `firstname`, `email`, `phone` — Customer details
  * `surl`, `furl` — Success and failure redirect URLs
  * `hash` — Server-generated SHA-512 hash

  Optional fields such as `udf1`–`udf10`, `offerKey`, and payment-mode-specific parameters depend on your integration. Missing or mismatched parameters are a common cause of SDK errors. For parameter limits and optional fields, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

</Accordion>

## Wrapper SDKs (Flutter, React Native, Cordova)

<Accordion title="Where can I find PayU Android SDK integration docs for Flutter?" icon="fa-info-circle">


  PayU provides Flutter wrapper SDKs that use the native Android SDK under the hood. For integration steps, refer to:

  * [Flutter CheckoutPro SDK](doc:flutter-checkoutprosdk-integration-steps)
  * [Flutter UPI SDK](doc:flutter-upi-sdk)
  * [Generate Dynamic Hash for Flutter](doc:generate-dynamic-hash-flutter)

</Accordion>

<Accordion title="Where can I find PayU Android SDK integration docs for React Native?" icon="fa-info-circle">


  For React Native integrations that wrap the native Android SDK, refer to:

  * [React Native CheckoutPro Android Integration](doc:reactnative-checkoutpro-android-integration)
  * [React Native UPI SDK](doc:react-native-upi-sdk)

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For wrapper SDK guides, refer to [Flutter CheckoutPro SDK](doc:flutter-checkoutprosdk-integration-steps), [React Native CheckoutPro Android Integration](doc:reactnative-checkoutpro-android-integration), and [Explore React Native SDKs](doc:explore-reactnative-sdks).


</Accordion>

<Accordion title="Where can I find PayU integration code for Ionic Cordova?" icon="fa-info-circle">


  The JS integration code for Ionic Cordova is available in the PayU sample repository:

  [https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js](https://github.com/payu-intrepos/payu-checkoutpro-cordova-ionic-sample/tree/main/PayUCheckoutProIonicSample/www/js)

  **Related documentation**

  * For wrapper SDK guides, refer to [Flutter CheckoutPro SDK](doc:flutter-checkoutprosdk-integration-steps), [React Native CheckoutPro Android Integration](doc:reactnative-checkoutpro-android-integration), and [Explore React Native SDKs](doc:explore-reactnative-sdks).


</Accordion>

## EMI and Offers

<Accordion title="Why is mobile number mandatory for debit card EMI on the PayU checkout screen?" icon="fa-info-circle">


  For debit card EMI, banks and card networks require the customer's mobile number to validate eligibility and send OTP or mandate-related communication. This is a compliance requirement from issuing banks and is not configurable at the merchant level for standard EMI flows.

  If you have a specific business requirement, contact your PayU Key Account Manager (KAM) to discuss available options.

  **Related documentation**

  * For UPI integration details, refer to [Integration Steps - Android UPI SDK](doc:integration-steps-android-upi-sdk), [Android Google Pay SDK](doc:android-google-pay-sdk), and [Android PhonePe SDK](doc:android-phonepe-sdk).
  * For payment method details, refer to [Error Handling](doc:error-handling), [Card Number Formats](doc:card-number-formats), and [Additional Info for Payment APIs](ref:addl_info-payment-apis).


</Accordion>

<Accordion title="How do I restrict or enforce specific payment modes in CheckoutPro for Android?" icon="fa-info-circle">


  Use the **enforcement list** to open a specific payment mode directly (for example, only UPI, only Net Banking, or a particular bank). Create an `enforceList` with `CP_PAYMENT_TYPE` and optional `ENFORCED_IBIBOCODE` or `CP_CARD_TYPE` values.

  For more information, refer to [Customize Your Integration – Enforced Payment Modes](doc:android-checkoutpro-custom-integrations).

</Accordion>

## UPI Integration

<Accordion title="I am getting Error Code 1022: &quot;Please provide payment type through config. Use setPaymentType method of UpiConfig.&quot; What should I do?" icon="fa-info-circle">


  Error 1022 means the Android UPI SDK requires a payment type in `UpiConfig` before `makePayment()` is called. Set the payment type using `setPaymentType()` with a supported `PaymentOption` value:

  * `PaymentOption.UPI_INTENT` — UPI Intent flow (opens installed UPI apps)
  * `PaymentOption.UPI_COLLECT` — UPI Collect flow (VPA-based)
  * `PaymentOption.TEZ` — Google Pay
  * `PaymentOption.PHONEPE` — PhonePe
  * `PaymentOption.SAMSUNGPAY` — Samsung Pay

  Example:

  ```java
  UpiConfig upiConfig = new UpiConfig();
  upiConfig.setMerchantKey("your_merchant_key");
  upiConfig.setPayuPostData(postData);
  upiConfig.setPaymentType(PaymentOption.UPI_INTENT);
  upiConfig.setIsProduction(false); // true for production
  ```

  Also ensure you generate `postData` for the selected payment option. For more information, refer to [Android UPI SDK Integration Steps](doc:integration-steps-android-upi-sdk).

  For detailed troubleshooting steps, refer to [Troubleshooting CheckoutPro SDK](doc:android-checkoutpro-troubleshoot-errors).

</Accordion>

<Accordion title="Can I handle the entire UPI payment flow within my own app UI without PayU screens?" icon="fa-info-circle">


  PayU UPI SDK supports Intent and Collect flows. For Google Pay, PhonePe, and Samsung Pay, you can integrate dedicated SDKs and generate `postData` for the chosen payment option. However, card OTP, 3DS, and bank authentication steps may still require PayU-hosted or bank-hosted screens for PCI and regulatory compliance.

  For UPI Intent, the customer is redirected to their UPI app to approve the payment; the approval screen is controlled by the UPI app, not your app. For a fully custom card checkout, consider [Custom Checkout](doc:custom-checkout-merchant-hosted) with appropriate PCI-DSS certification.

</Accordion>

<Accordion title="How do I integrate UPI Autopay (recurring mandates) in my Android app?" icon="fa-info-circle">


  UPI Autopay uses standing instruction (SI) parameters in the payment request along with UPI SDK or CheckoutPro. Your backend must handle mandate registration, pre-debit notifications, and recurring debit APIs.

  Contact your PayU Key Account Manager (KAM) to enable UPI Autopay for your account. For integration steps, refer to [Integrate Parallel Sequencing for UPI Autopay](doc:integrate-parallel-sequencing-for-upi-autopay) and [Recurring Payments FAQs](doc:faqs-recurring-payments).

</Accordion>