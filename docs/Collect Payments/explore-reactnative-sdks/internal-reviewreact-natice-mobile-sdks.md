---
title: '[Internal Review]React Natice Mobile SDKs'
deprecated: false
hidden: true
metadata:
  robots: index
---
Before you begin integrating PayU React Native SDKs into your application, complete the following prerequisites to ensure a smooth integration process.

## Account Setup

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

| Credential        | Description                        |
| ----------------- | ---------------------------------- |
| **Merchant Key**  | Unique identifier for your account |
| **Merchant Salt** | Used for hash generation           |
| **Client ID**     | For OAuth-based authentication     |
| **Client Secret** | For OAuth-based authentication     |

</Accordion>

---

## Development Environment Requirements

<Accordion title="Minimum System Requirements" icon="fa-desktop">

| Requirement                    | Minimum Version | Recommended |
| ------------------------------ | --------------- | ----------- |
| **Node.js**                    | 16.x            | 18.x+       |
| **React Native**               | 0.63+           | 0.72+       |
| **npm**                        | 8.x             | 10.x+       |
| **Xcode** (for iOS)            | 13.0+           | 15.0+       |
| **Android Studio** (for Android) | Arctic Fox+   | Ladybug+    |
| **iOS Deployment Target**      | iOS 12.0        | iOS 15.0+   |
| **Android Min SDK Version**    | API 21 (5.0)    | API 24+     |

</Accordion>

<Accordion title="Package Manager Support" icon="fa-box">

PayU React Native SDKs are available through:

| Package Manager | Supported | Notes                         |
| --------------- | --------- | ----------------------------- |
| **npm**         | ✅ Yes     | Recommended for most projects |
| **yarn**        | ✅ Yes     | Fully supported               |

</Accordion>

<Accordion title="Installation Setup" icon="fa-cogs">

Install the PayU SDK package using npm or yarn:

```bash
# Using npm
npm install payu-non-seamless-react

# Using yarn
yarn add payu-non-seamless-react
```

For the Checkout Pro SDK:

```bash
# Using npm
npm install react-native-payu-payment-sdk

# Using yarn
yarn add react-native-payu-payment-sdk
```

<Accordion title="iOS Configuration" icon="fa-apple">

After installing the package, run pod install:

```bash
cd ios && pod install && cd ..
```

Add the following to your `ios/Podfile`:

```ruby
platform :ios, '12.0'
use_frameworks!

target 'YourApp' do
  # React Native pods
  # ...
  
  # PayU SDK will be automatically linked
end
```

</Accordion>

<Accordion title="Android Configuration" icon="fa-android">

Add the PayU repository to your `android/build.gradle`:

```groovy
allprojects {
    repositories {
        google()
        mavenCentral()
        maven { url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android" }
    }
}
```

Ensure your `android/app/build.gradle` has the correct minimum SDK:

```groovy
android {
    defaultConfig {
        minSdkVersion 21
        targetSdkVersion 34
    }
}
```

</Accordion>

</Accordion>

---

## React Native Privacy & Compliance

<Accordion title="iOS Permissions" icon="fa-apple">

Add the following to your `ios/YourApp/Info.plist`:

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
```

</Accordion>

<Accordion title="Android Permissions" icon="fa-android">

Add the following permissions to your `android/app/src/main/AndroidManifest.xml`:

```xml
<!-- Required for network operations -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

<!-- Required for UPI Intent (opening UPI apps) -->
<uses-permission android:name="android.permission.QUERY_ALL_PACKAGES"
    tools:ignore="QueryAllPackagesPermission" />

<!-- Optional: For SMS-based OTP auto-read -->
<uses-permission android:name="android.permission.RECEIVE_SMS" />
<uses-permission android:name="android.permission.READ_SMS" />
```

</Accordion>

<Accordion title="Package Visibility Configuration (Android 11+)" icon="fa-eye">

Starting with Android 11 (API level 30), apps must declare which packages they interact with. Add the following to your `AndroidManifest.xml`:

```xml
<queries>
    <!-- UPI Apps -->
    <intent>
        <action android:name="android.intent.action.VIEW" />
        <data android:scheme="upi" />
    </intent>
    
    <!-- Specific payment apps -->
    <package android:name="com.phonepe.app" />
    <package android:name="com.google.android.apps.nbu.paisa.user" />
    <package android:name="net.one97.paytm" />
    <package android:name="in.org.npci.upiapp" />
</queries>
```

</Accordion>

<Accordion title="ProGuard/R8 Rules (Android)" icon="fa-lock">

If you use ProGuard or R8, add the following rules to your `android/app/proguard-rules.pro`:

```proguard
# PayU SDK
-keep class com.payu.** { *; }
-keep class in.payu.** { *; }
-dontwarn com.payu.**
-dontwarn in.payu.**

# Keep models for serialization
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}
```

</Accordion>

---

## Server-Side Hash Generation Setup

PayU uses hash-based verification for security. **Hash must be generated on your server, never on the client.**

The dynamic hashes must be generated at runtime for each transaction and will vary based on the transaction parameters.

<Callout icon="📘" theme="info">
  **Hashing logic for SDK and Web Integration is different**: For the hashing logic for web integration, refer to [Generate Hash](doc:generate-hash-payu-hosted).
</Callout>

<Accordion title="Hash Generation Flow" icon="fa-random">

<Image border={false} src="https://files.readme.io/04949cb-Screenshot_2023-11-16_at_6.14.14_PM.png" />

</Accordion>

<Accordion title="Hash Formula" icon="fa-code">

```
hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
```

</Accordion>

<Accordion title="Sample Server-Side Code" icon="fa-server">

```javascript JavaScript (Node.js)
const crypto = require('crypto');

function generatePayUHash(params, salt) {
    const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${params.udf1 || ''}|${params.udf2 || ''}|${params.udf3 || ''}|${params.udf4 || ''}|${params.udf5 || ''}||||||${salt}`;
    
    return crypto.createHash('sha512').update(hashString).digest('hex');
}
```

```python Python
import hashlib

def generate_payu_hash(params, salt):
    hash_string = f"{params['key']}|{params['txnid']}|{params['amount']}|{params['productinfo']}|{params['firstname']}|{params['email']}|{params.get('udf1', '')}|{params.get('udf2', '')}|{params.get('udf3', '')}|{params.get('udf4', '')}|{params.get('udf5', '')}||||||{salt}"
    
    return hashlib.sha512(hash_string.encode()).hexdigest()
```

```php PHP
function generatePayUHash($params, $salt) {
    $hashString = $params['key'] . '|' . $params['txnid'] . '|' . $params['amount'] . '|' . $params['productinfo'] . '|' . $params['firstname'] . '|' . $params['email'] . '|' . ($params['udf1'] ?? '') . '|' . ($params['udf2'] ?? '') . '|' . ($params['udf3'] ?? '') . '|' . ($params['udf4'] ?? '') . '|' . ($params['udf5'] ?? '') . '||||||' . $salt;
    
    return hash('sha512', $hashString);
}
```

<Callout icon="🔒" theme="default">
  **Security Note:** Never embed your Salt in the React Native app. Always generate hashes server-side.
</Callout>

</Accordion>

<br />

## Choose Your SDK

Based on your requirements, select the appropriate SDK:

| Your Requirement                  | Recommended SDK                                                    | Integration Effort |
| --------------------------------- | ------------------------------------------------------------------ | ------------------ |
| Fastest integration, pre-built UI | [Checkout Pro SDK](/docs/react-native-checkoutpro-sdk)             | Low                |
| Full UI customization             | [Core SDK](/docs/react-native-core-sdk)                            | Medium             |
| UPI payments only                 | [UPI SDK](/docs/react-native-upi-sdk)                              | Low                |
| Net Banking payments              | [Custom Browser SDK](/docs/reactnative-coresdk-custom-browser-sdk) | Low                |
| One-click UPI payments            | [UPI Bolt SDK](/docs/upi-bolt-sdk-integration-react-native)        | Low                |

---

## Webhook Setup

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

<Accordion title="Webhook Configuration" icon="fa-wrench">

1. Navigate to **Dashboard → Settings → Webhooks**
2. Click **Create New Webhook**
3. Enter your webhook URL (must be HTTPS)
4. Select the events you want to receive
5. Save and note the webhook secret for verification

<Callout icon="📘" theme="info">
  **Note:** For detailed webhook setup, refer to [Webhooks for Payments](/docs/webhooks-for-payments).
</Callout>

</Accordion>

---

## Choose your integration

> ✅ **Note**: The best SDK for you will depend on your specific needs and requirements.

If you need a quick and easy way to integrate a payment interface into your app, then the Checkout Pro SDK is a good option. If you need more control over the look and feel of the payment interface, then the Core SDK is a good choice. And if you need to accept payments through UPI, then the UPI SDK is a good fit.

PayU offers various React Native SDKs that each serve a unique use case. Here is a brief overview of the most popular SDKs:

* **Checkout Pro SDK**: The Checkout Pro SDK is a complete, ready-to-use native checkout UI that allows you to integrate a payment interface with minimal effort and get started quickly. The SDK includes a variety of features, such as support for multiple payment methods, a secure payment gateway, and a user-friendly interface.

* **Core SDK**: The Core SDK allows you to integrate the PayU payment gateway into your own payment interface. This gives you more control over the look and feel of the payment interface, as well as the ability to add custom features and functionality.

* **UPI SDK**: The UPI SDK allows you to integrate Unified Payments Interface (UPI) payments into your React Native app. UPI is a popular payment method in India that allows users to make payments directly from their bank accounts.

* **Custom Browser SDK**: The Custom Browser SDK allows you to accept Netbanking payments on your app with a customized browser experience.

* **UPI Bolt SDK**: The UPI Bolt SDK provides a simpler and more efficient payment experience. It eliminates third-party redirection and provides higher success rates.

Here is a comparison table that summarizes the key features of the different SDKs:

| SDK                                                            | Features                                                                                                                                                                                                                             | Use Case                                                                             |
| :------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| [Checkout Pro SDK](doc:react-native-checkoutpro-sdk)           | Complete ready-to-use native checkout UI allows you to get started quickly with minimal effort. This SDK is a great choice for small and medium sized businesses that operates on limited tech resource.                             | **Low Effort Integration** \| **Non-Seamless Checkout** \| **Limited Tech Resource** |
| [Core SDK](doc:react-native-core-sdk)                          | Create your own UI for the payment flow by leveraging various methods exposed in the Core SDK. This SDK is more suitable for larger enterprises that can allocate dedicated engineering resource to develop customised payment flow. | **Seamless Checkout** \| **Medium Effort** \| **Enterprise Businesses**              |
| [UPI SDK](doc:react-native-upi-sdk)                            | This SDK is best suited for creating a custom payment UI for UPI only checkout.                                                                                                                                                      | **Low Effort Integration** \| **UPI Checkout**                                       |
| [Custom Browser SDK](doc:reactnative-coresdk-custom-browser-sdk) | Use this SDK to accept Netbanking payments on your app with a customized browser experience.                                                                                                                                        | **Low Effort Integration** \| **Net Banking Payments**                               |
| [UPI Bolt SDK](doc:upi-bolt-sdk-integration-react-native)      | Allows you to provide a simpler and more efficient payment experience. Eliminates third-party redirection with higher success rate.                                                                                                  | **One-Click Payment** \| **UPI Checkout**                                            |

---

## Next Steps

After you've completed the prerequisites above, proceed with your chosen SDK integration:

1. **[Integrate Checkout Pro SDK](/docs/react-native-checkoutpro-sdk)** - For quick, ready-to-use checkout
2. **[Integrate Core SDK](/docs/react-native-core-sdk)** - For custom payment flows
3. **[Test Your Integration](/docs/test-cards-upi-id-and-wallets)** - Using test credentials
4. **[Go Live Checklist](/docs/production-checklist)** - Before switching to production
