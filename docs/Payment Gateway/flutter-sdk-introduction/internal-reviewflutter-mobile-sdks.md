---
title: '[Internal Review]Flutter Mobile SDKS'
deprecated: false
hidden: true
metadata:
  robots: index
---
Before you begin integrating PayU Flutter SDKs into your application, complete the following prerequisites to ensure a smooth integration process.

## 1. Account Setup

<Accordion title="Register and Activate Your PayU Account" icon="fa-user-plus">
  | Step | Action                                 | Link                                                            |
  | ---- | -------------------------------------- | --------------------------------------------------------------- |
  | 1    | Register for a PayU Merchant Account   | [Register](/docs/register-for-a-merchant-account)               |
  | 2    | Complete KYC and activate your account | [Activate Account](/docs/activate-account)                      |
  | 3    | Access your Test Merchant Key and Salt | [Get Test Credentials](/docs/access-test-merchant-key-and-salt) |

  <Callout icon="⚠️" theme="warn">
    **Important:** Never use production credentials during development. Always use test credentials until you're ready for go-live.
  </Callout>
</Accordion>

<Accordion title="Obtain Your Credentials" icon="fa-key">
  You'll need the following credentials from the PayU Dashboard. Refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).

  | Credential              | Description                                     |
  | ----------------------- | ----------------------------------------------- |
  | **Merchant Key**        | Unique identifier for your account              |
  | **Merchant Salt**       | Used for hash generation                        |
  | **Client ID**           | For OAuth-based authentication                  |
  | **Client Secret**       | For OAuth-based authentication                  |
  | **Merchant Access Key** | For offers and recommendation engine (optional) |
</Accordion>

***

## 2. Development Environment Requirements

<Accordion title="Minimum System Requirements" icon="fa-desktop">
  <Accordion title="Android Requirements" icon="fa-android">
    | Requirement             | Minimum Version | Recommended |
    | ----------------------- | --------------- | ----------- |
    | **Min SDK Version**     | 21              | 24+         |
    | **Compile SDK Version** | 29+             | 33+         |
    | **Kotlin Version**      | 1.6.10          | 1.8+        |
  </Accordion>

  <Accordion title="iOS Requirements" icon="fa-apple">
    | Requirement               | Minimum Version | Recommended |
    | ------------------------- | --------------- | ----------- |
    | **iOS Deployment Target** | iOS 11.0        | iOS 15.0+   |
    | **Xcode**                 | 11.4+           | 15.0+       |
    | **Swift**                 | 5.0+            | 5.7+        |
  </Accordion>
</Accordion>

<Accordion title="Flutter Environment Setup" icon="fa-flutter">
  Ensure you have Flutter installed and configured:

  | Requirement     | Minimum Version | Recommended |
  | --------------- | --------------- | ----------- |
  | **Flutter SDK** | 2.0+            | 3.10+       |
  | **Dart**        | 2.12+           | 3.0+        |

  Run the following command to verify your Flutter installation:

  ```bash
  flutter doctor
  ```
</Accordion>

<Accordion title="Package Installation" icon="fa-cube">
  PayU Flutter SDKs are available through **pub.dev**. Add the required dependency:

  <Accordion title="Checkout Pro SDK" icon="fa-shopping-cart">
    ```bash
    flutter pub add payu_checkoutpro_flutter
    ```

    Import in your Dart file:

    ```dart
    import 'package:payu_checkoutpro_flutter/payu_checkoutpro_flutter.dart';
    import 'package:payu_checkoutpro_flutter/PayUConstantKeys.dart';
    ```

    **For iOS**, run inside the `ios` folder:

    ```bash
    pod install
    ```
  </Accordion>

  <Accordion title="UPI SDK" icon="fa-mobile">
    ```bash
    flutter pub add payu_upi_flutter
    ```
  </Accordion>

  <Accordion title="Custom Browser SDK" icon="fa-globe">
    ```bash
    flutter pub add payu_custombrowser_flutter
    ```
  </Accordion>
</Accordion>

***

## 3. Platform-Specific Configuration

<Accordion title="Android Configuration" icon="fa-android">
  <Accordion title="AndroidManifest.xml Permissions" icon="fa-file-code">
    Add the following permissions to your `android/app/src/main/AndroidManifest.xml`:

    ```xml
    <!-- For OTP auto-read on bank pages -->
    <uses-permission android:name="android.permission.RECEIVE_SMS" />

    <!-- For internet access -->
    <uses-permission android:name="android.permission.INTERNET" />
    ```
  </Accordion>

  <Accordion title="Test Environment Metadata" icon="fa-bug">
    For testing, add the following metadata inside the `<application>` tag:

    ```xml
    <application>
        <!-- Remove or set to false for production -->
        <meta-data android:name="payu_debug_mode_enabled" android:value="true" />
        
        <!-- Comment these lines for production -->
        <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" />
        <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/>
    </application>
    ```

    <Callout icon="⚠️" theme="warn">
      **Important:** Remove or comment out the test metadata before going live!
    </Callout>
  </Accordion>
</Accordion>

<Accordion title="iOS Configuration" icon="fa-apple">
  <Accordion title="UPI Intent Setup (Info.plist)" icon="fa-link">
    Add the following query schemes to enable UPI app launching:

    ```xml
    <key>LSApplicationQueriesSchemes</key>
    <array>
        <string>phonepe</string>
        <string>paytm</string>
        <string>tez</string>
        <string>credpay</string>
        <string>bhim</string>
    </array>
    ```
  </Accordion>

  <Accordion title="Camera Permission (Card Scanner)" icon="fa-camera">
    If using card scanning feature, add camera permission:

    ```xml
    <key>NSCameraUsageDescription</key>
    <string>Camera access is required to scan your card details</string>
    ```
  </Accordion>

  <Accordion title="App Store Distribution" icon="fa-app-store">
    Before archiving your app for the App Store, you need to remove simulator slices from the framework. For detailed instructions, refer to [Releasing to App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).
  </Accordion>
</Accordion>

***

## 4. Server-Side Hash Generation Setup

PayU uses hash-based verification for security. **Hash must be generated on your server, never on the client.**

<Accordion title="Hash Generation Flow" icon="fa-diagram-project">
  ![](https://files.readme.io/04949cb-Screenshot_2023-11-16_at_6.14.14_PM.png)
</Accordion>

<Accordion title="Hash Types Required" icon="fa-list">
  The Flutter SDK requires the following hash types:

  | Hash Type      | Algorithm   | Use Case                |
  | -------------- | ----------- | ----------------------- |
  | **V1 Hash**    | SHA-512     | Payment initiation      |
  | **V2 Hash**    | HMAC-SHA256 | API calls               |
  | **MCP Lookup** | HMAC-SHA1   | Multi-currency payments |
  | **Post Salt**  | SHA-512     | Additional verification |
</Accordion>

<Accordion title="Hash Formula" icon="fa-calculator">
  ```
  hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```
</Accordion>

<Accordion title="Sample Server-Side Code" icon="fa-code">
  ```javascript
  const crypto = require('crypto');

  function generatePayUHash(params, salt) {
      const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${params.udf1 || ''}|${params.udf2 || ''}|${params.udf3 || ''}|${params.udf4 || ''}|${params.udf5 || ''}||||||${salt}`;
      
      return crypto.createHash('sha512').update(hashString).digest('hex');
  }

  // For V2 Hash (HMAC-SHA256)
  function generateV2Hash(hashString, salt) {
      return crypto.createHmac('sha256', salt).update(hashString).digest('hex');
  }
  ```
  ```python
  import hashlib
  import hmac

  def generate_payu_hash(params, salt):
      hash_string = f"{params['key']}|{params['txnid']}|{params['amount']}|{params['productinfo']}|{params['firstname']}|{params['email']}|{params.get('udf1', '')}|{params.get('udf2', '')}|{params.get('udf3', '')}|{params.get('udf4', '')}|{params.get('udf5', '')}||||||{salt}"
      
      return hashlib.sha512(hash_string.encode()).hexdigest()

  # For V2 Hash (HMAC-SHA256)
  def generate_v2_hash(hash_string, salt):
      return hmac.new(salt.encode(), hash_string.encode(), hashlib.sha256).hexdigest()
  ```
  ```dart
  // Client-side hash request handling
  @override
  generateHash(Map response) {
    var hashName = response[PayUHashConstantsKeys.hashName];
    var hashStringWithoutSalt = response[PayUHashConstantsKeys.hashString];
    var hashType = response[PayUHashConstantsKeys.hashType];
    var postSalt = response[PayUHashConstantsKeys.postSalt];
    
    // Send to your server for hash generation
    // Then pass back to SDK:
    Map hashResponse = {'hashName': hash};
    _checkoutPro.hashGenerated(hash: hashResponse);
  }
  ```

  <Callout icon="🔒" theme="default">
    **Security Note:** Never embed your Salt in the Flutter app. Always generate hashes server-side.
  </Callout>
</Accordion>

***

## 5. Choose Your SDK

Based on your requirements, select the appropriate SDK:

| SDK                                                       | Features                                                                                             | Use Case                                   |
| :-------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| [Flutter Checkout Pro](/docs/flutter-checkoutpro-sdk)     | Complete ready-to-use native checkout UI with all payment methods, offers, and customization support | **Low Effort** \| **Full Payment Support** |
| [Flutter UPI SDK](/docs/flutter-upi-sdk)                  | UPI Collect and Intent flow support for UPI-only checkouts                                           | **Low Effort** \| **UPI Only**             |
| [Flutter Custom Browser](/docs/flutter-custombrowser-sdk) | OTP assist and optimized bank pages for custom checkout flows                                        | **Medium Effort** \| **Custom Checkout**   |

<Accordion title="Flutter Checkout Pro SDK" icon="fa-shopping-cart">
  **Best for:** Quick integration with ready-to-use UI

  The Checkout Pro SDK provides a complete Mobile Checkout solution with:

  * ✅ Ready-to-use native Checkout UI
  * ✅ All major Credit/Debit card providers (Amex, Mastercard, Rupay, Visa)
  * ✅ Netbanking with 150+ Indian banks
  * ✅ UPI Payments (Intent & Collect)
  * ✅ Google Pay™ InApp & Cards
  * ✅ Native OTP Assist
  * ✅ Recurring Payments (Standing Instructions)
  * ✅ Convenience Fee support
  * ✅ Offers support
  * ✅ Multi-Currency Payments
  * ✅ Prepaid Wallets
  * ✅ CC & DC EMI Payments
  * ✅ Customization capabilities

  **Integration Steps:**

  1. [Integration Steps](/docs/flutter-checkoutprosdk-integration-steps)
  2. [Test the Integration](/docs/flutter-checkoutprosdk-test-integration)
  3. [Go-live Checklist](/docs/flutter-checkoutprosdk-golive-checklist)
</Accordion>

<Accordion title="Flutter UPI SDK" icon="fa-mobile">
  **Best for:** UPI-only payment flows

  Supports both UPI transaction types:

  * **Collect Flow**: PayU triggers transaction to the app linked to the provided VPA
  * **Intent Flow**: Delegates transaction to external apps (BHIM, Google Pay, PhonePe)

  <Callout icon="❗" theme="warn">
    To transact through Google Pay™, register your business using the Google Onboarding form with merchant VPAs created by PayU.
  </Callout>

  **Integration Steps:**

  1. [Integration Steps](/docs/integration-steps-flutterupi)
  2. [Test the Integration](/docs/test-the-integration-flutterupi)
  3. [Go-live Checklist](/docs/go-live-checklist-flutterupi)
</Accordion>

<Accordion title="Flutter Custom Browser SDK" icon="fa-globe">
  **Best for:** Custom checkout with optimized bank pages

  Features:

  * **OTP Assist**: Automatically reads OTP messages on bank pages
  * **Bank Page Optimizations**: PayU optimizes bank pages for better payment experience

  **Integration Steps:**

  1. [Integration Steps](/docs/1-integration-steps)
  2. [Test the Integration](/docs/test-the-integration-fluttercb)
  3. [Go-live Checklist](/docs/go-live-checklist-fluttercb)
</Accordion>

***

## 6. Webhook Setup

Configure webhooks to receive real-time payment notifications.

<Accordion title="Required Webhook Events" icon="fa-bell">
  | Event             | Description                    |
  | ----------------- | ------------------------------ |
  | `payment.success` | Payment completed successfully |
  | `payment.failed`  | Payment failed                 |
  | `payment.pending` | Payment is pending             |
  | `refund.success`  | Refund processed successfully  |
  | `refund.failed`   | Refund failed                  |
</Accordion>

<Accordion title="Webhook Configuration" icon="fa-gear">
  1. Navigate to **Dashboard → Settings → Webhooks**
  2. Click **Create New Webhook**
  3. Enter your webhook URL (must be HTTPS)
  4. Select the events you want to receive
  5. Save and note the webhook secret for verification

  <Callout icon="📘" theme="info">
    **Note:** For detailed webhook setup, refer to [Webhooks for Payments](/docs/webhooks-for-payments).
  </Callout>
</Accordion>

## Next Steps

Once you've completed the prerequisites above, proceed with your chosen SDK integration:

1. **[Integrate Checkout Pro SDK](/docs/flutter-checkoutprosdk-integration-steps)** - For quick, ready-to-use checkout
2. **[Integrate UPI SDK](/docs/integration-steps-flutterupi)** - For UPI-only payments
3. **[Test Your Integration](/docs/test-cards-upi-id-and-wallets)** - Using test credentials
4. **[Go Live Checklist](/docs/flutter-checkoutprosdk-golive-checklist)** - Before switching to production
