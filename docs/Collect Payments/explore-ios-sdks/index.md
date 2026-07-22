---
title: ' iOS Mobile SDKs'
deprecated: false
hidden: false
icon: fab fa-apple
metadata:
  title: PayU iOS SDKs
  description: >-
    PayU offers various iOS SDKs for integrating payment interfaces into your
    app, including the Checkout Pro SDK for a quick and easy integration, the
    Core SDK for more control over the interface, and specific SDKs for UPI,
    OlaMoney, and Native OTP Assist payments. The best SDK for you depends on
    your specific needs and requirements.
  keywords:
    - PayU Mobile SDK
    - ' Payment Gateway for IOS Mobile'
    - ' PayU India IOS SDK'
    - PayU IOS SDK
    - ' PayU IOS SDK integration'
    - ' IOS payment SDK'
    - ' Mobile payment IOS SDK'
  robots: index
next:
  description: ''
---
PayU offers various iOS SDKs that each serve a unique use case. Before you begin integrating PayU iOS SDKs into your application, complete the following prerequisites to ensure a smooth integration process.

## 1. Account Setup

<Accordion title="Register and Activate Your PayU Account" icon="fa-user-plus">
  | Step | Action                                 | Link                                                          |
  | ---- | -------------------------------------- | ------------------------------------------------------------- |
  | 1    | Register for a PayU Merchant Account   | [Register](doc:register-for-a-merchant-account-on-dashboard)  |
  | 2    | Complete KYC and activate your account | [Activate Account](doc:complete-your-kyc)                     |
  | 3    | Access your Test Merchant Key and Salt | [Get Test Credentials](doc:generate-test-merchant-key-and-salt) |

  <Callout icon="⚠️" theme="warn">
    **Important:** Never use production credentials during development. Always use test credentials until you're ready for go-live.
  </Callout>
</Accordion>

<Accordion title="Obtain Your Credentials" icon="fa-key">
  You'll need the following credentials from the PayU Dashboard. Refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).

  | Credential        | Description                        |
  | ----------------- | ---------------------------------- |
  | **Merchant Key**  | Unique identifier for your account |
  | **Merchant Salt** | Used for hash generation           |
  | **Client ID**     | For OAuth-based authentication     |
  | **Client Secret** | For OAuth-based authentication     |
</Accordion>

## 2. Development Environment Requirements

<Accordion title="Minimum System Requirements" icon="fa-desktop">
  | Requirement               | Minimum Version | Recommended |
  | ------------------------- | --------------- | ----------- |
  | **Xcode**                 | 16.0+           | 26.0        |
  | **iOS Deployment Target** | iOS 13.0        | iOS 15.0+   |
  | **Swift**                 | 5.0+            | 5.7+        |
  | **macOS**                 | Sequoia 15.0    | Tahoe 26.0  |
</Accordion>

<Accordion title="Package Manager Support" icon="fa-cube">
  PayU iOS SDKs are available through:

  | Package Manager           | Supported | Notes                         |
  | ------------------------- | --------- | ----------------------------- |
  | **CocoaPods**             | ✅ Yes     | Recommended for most projects |
  | **Swift Package Manager** | ✅ Yes     | Available for select SDKs     |
  | **Manual Integration**    | ✅ Yes     | Framework files available     |
</Accordion>

<Accordion title="CocoaPods Setup" icon="fa-cogs">
  Add the following to your `Podfile`:

  ```ruby
  # Podfile example
  platform :ios, '12.0'
  use_frameworks!

  target 'YourApp' do
    # Add the SDK you need
    pod 'PayUIndia-CheckoutPro'  # For Checkout Pro SDK
    # pod 'PayUIndia-PG-SDK'     # For Core SDK
  end
  ```

  Then run:

  ```bash
  pod install
  ```
</Accordion>

## 3. Apple Privacy & Compliance

<Accordion title="Privacy Manifest Configuration" icon="fa-shield">
  Starting with iOS 17, Apple requires apps to declare the data they collect. PayU SDKs collect certain data for payment processing.

  <Accordion title="Required Privacy Manifest Entries" icon="fa-file-code">
    Add the following to your app's `PrivacyInfo.xcprivacy` file:

    ```xml
    <dict>
        <key>NSPrivacyTracking</key>
        <false/>
        <key>NSPrivacyTrackingDomains</key>
        <array/>
        <key>NSPrivacyCollectedDataTypes</key>
        <array>
            <dict>
                <key>NSPrivacyCollectedDataType</key>
                <string>NSPrivacyCollectedDataTypePaymentInfo</string>
                <key>NSPrivacyCollectedDataTypeLinked</key>
                <false/>
                <key>NSPrivacyCollectedDataTypeTracking</key>
                <false/>
                <key>NSPrivacyCollectedDataTypePurposes</key>
                <array>
                    <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
                </array>
            </dict>
        </array>
    </dict>
    ```
  </Accordion>
</Accordion>

<Accordion title="Required App Permissions" icon="fa-lock">
  Depending on the SDK and payment methods you enable, add these to your `Info.plist`:

  ```xml
  <!-- For UPI Intent (opening UPI apps) -->
  <key>LSApplicationQueriesSchemes</key>
  <array>
      <string>phonepe</string>
      <string>tez</string>
      <string>paytm</string>
      <string>bhim</string>
      <string>upi</string>
  </array>

  <!-- For camera access (card scanning, if enabled) -->
  <key>NSCameraUsageDescription</key>
  <string>Camera access is required to scan your card details</string>

  <!-- For network access -->
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <false/>
  </dict>
  ```
</Accordion>

## 4. Server-Side Hash Generation Setup

PayU uses hash-based verification for security. **Hash must be generated on your server, never on the client.**

<Accordion title="Hash Generation Flow" icon="fa-diagram-project">
  ![](https://files.readme.io/04949cb-Screenshot_2023-11-16_at_6.14.14_PM.png)
</Accordion>

<Accordion title="Hash Formula" icon="fa-calculator">
  **v1 Hashing**

  ```
  hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

  **v2 Hashing**

  ```
     hash = SHA512(hashStringWithoutSalt | salt)
  ```
</Accordion>

<Accordion title="Sample Server-Side Code" icon="fa-code">
  ```javascript
  const crypto = require('crypto');

  function generatePayUHash(params, salt) {
      const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${params.udf1 || ''}|${params.udf2 || ''}|${params.udf3 || ''}|${params.udf4 || ''}|${params.udf5 || ''}||||||${salt}`;
      
      return crypto.createHash('sha512').update(hashString).digest('hex');
  }
  ```
  ```python
  import hashlib

  def generate_payu_hash(params, salt):
      hash_string = f"{params['key']}|{params['txnid']}|{params['amount']}|{params['productinfo']}|{params['firstname']}|{params['email']}|{params.get('udf1', '')}|{params.get('udf2', '')}|{params.get('udf3', '')}|{params.get('udf4', '')}|{params.get('udf5', '')}||||||{salt}"
      
      return hashlib.sha512(hash_string.encode()).hexdigest()
  ```
  ```php
  function generatePayUHash($params, $salt) {
      $hashString = $params['key'] . '|' . $params['txnid'] . '|' . $params['amount'] . '|' . $params['productinfo'] . '|' . $params['firstname'] . '|' . $params['email'] . '|' . ($params['udf1'] ?? '') . '|' . ($params['udf2'] ?? '') . '|' . ($params['udf3'] ?? '') . '|' . ($params['udf4'] ?? '') . '|' . ($params['udf5'] ?? '') . '||||||' . $salt;
      
      return hash('sha512', $hashString);
  }
  ```
</Accordion>

<Callout icon="🔒" theme="default">
  **Security Note:** Never embed your Salt in the iOS app. Always generate hashes server-side.
</Callout>

## 5. Choose Your SDK

Based on your requirements, select the appropriate SDK:

| Your Requirement                  | Recommended SDK                                               | Integration Effort |
| --------------------------------- | ------------------------------------------------------------- | ------------------ |
| Fastest integration, pre-built UI | [Checkout Pro SDK](doc:ios-checkoutpro-sdk)                   | Low                |
| Full UI customization             | [Core SDK](doc:ios-core-sdk)                                  | Medium             |
| UPI payments only                 | [UPI SDK](docs:ios-upi-sdk)                                   | Low                |
| Improved card success rates       | Core SDK + [Native OTP Assist](doc:ios-native-otp-assist-sdk) | Medium             |
| One-click UPI payments            | [UPI Bolt SDK](doc:payu-upi-bolt-sdk-ios)                     | Low                |
| Native 3D Secure experience       | [3DS 2.0 SDK]doc:ios-3ds-sdk)                                 | Medium             |

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
    **Note:** For detailed webhook setup, refer to [Webhooks for Payments](doc:webhook-events-and-sample-payloads).
  </Callout>
</Accordion>

## Choose your integration

<Callout icon="✅" theme="okay">
  **Note**: The best SDK for you will depend on your specific needs and requirements.
</Callout>

If you need a quick and easy way to integrate a payment interface into your app, then the Checkout Pro SDK is a good option. If you need more control over the look and feel of the payment interface, then the Core SDK is a good choice. And if you need to accept payments through UPI, OlaMoney, PhonePe, or Native OTP Assist, then the respective SDKs are a good fit.

Here is a comparison table that summarizes the key features of the different SDKs:

| SDK                                                                  | Features                                                                                                                                                                                                                             | Use Case                                                                                           |
| :------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [iOS CheckoutPro SDK](doc:ios-checkoutpro-sdk) | Complete ready-to-use native checkout UI allows you to get started quickly with minimal effort. This SDK is a great choice for small and medium sized businesses that operates on limited tech resource.                             | \| **Low Effort Integration**, \| **Non-Seamless Checkout** \| **Limited Tech** \| **Resource** \| |
| [iOS Core SDK](doc:ios-core-sdk)                                     | Create your own UI for the payment flow by leveraging various methods exposed in the Core SDK. This SDK is more suitable for larger enterprises that can allocate dedicated engineering resource to develop customised payment flow. | \| **Seamless Checkout** \| **Medium Effort** \|  **Enterprise Businesses** \|                     |
| [iOS UPI SDK](doc:ios-upi-sdk)                                       | This SDK best suited for creating a custom payment UI for UPI only checkout.                                                                                                                                                         | **Low Effort Integration**\|**UPI Checkout**                                                       |
| [iOS Ola Money SDK](doc:ios-olamoney-sdk)                            | Allows you to integrate OlaMoney payments into your iOS app.                                                                                                                                                                         | **Low Effort Integration**\|**OlaMoney Checkout**                                                  |
| [iOS Custom Browser SDK](doc:ios-custombrowser-sdk)                  | Collect netbanking payment on the bank's page                                                                                                                                                                                        | **Low Effort Integration**\|**PhonePe Checkout**                                                   |
| [iOS Native OTP Assist SDK](doc:ios-native-otp-assist-sdk)           | Allows you to capture OTP (One Time Password) directly from your iOS app without redirecting the user to the bank's 3D secure page.                                                                                                  | **Native OTP Support**\| **Low Effort Integration**                                                |
| [iOS 3DS 2.0 SDK](doc:ios-3ds-sdk)                                   | provide a native experience rather than redirecting customer to a bank page. The UI is standardised according to EMVCO guidelines and offers customisation.                                                                          | **Native OTP Support**                                                                             |
| [iOS UPI Bolt SDK](doc:payu-upi-bolt-sdk-ios)                        | Allows you to  simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate.                                                                                | **One-Click Payment**\| **UPI Checkout**                                                           |

## Next Steps

Once you've completed the prerequisites above, proceed with your chosen SDK integration:

1. **[Integrate Checkout Pro SDK](doc:ios-checkoutpro-sdk)** - For quick, ready-to-use checkout
2. **[Integrate Core SDK](doc:ios-core-sdk)** - For custom payment flows