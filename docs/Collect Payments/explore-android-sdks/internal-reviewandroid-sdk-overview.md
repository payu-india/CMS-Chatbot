---
title: '[Internal Review]Android SDK Overview'
deprecated: false
hidden: true
metadata:
  robots: index
---
Before you begin integrating PayU Android SDKs into your application, complete the following prerequisites to ensure a smooth integration process.

## Account Setup

### Register and Activate Your PayU Account

| Step | Action                                 | Link                                                            |
| ---- | -------------------------------------- | --------------------------------------------------------------- |
| 1    | Register for a PayU Merchant Account   | [Register](/docs/register-for-a-merchant-account)               |
| 2    | Complete KYC and activate your account | [Activate Account](/docs/activate-account)                      |
| 3    | Access your Test Merchant Key and Salt | [Get Test Credentials](/docs/access-test-merchant-key-and-salt) |

<Callout icon="⚠️" theme="warn">
  **Important:** Never use production credentials during development. Always use test credentials until you're ready for go-live.
</Callout>

### Obtain Your Credentials

You'll need the following credentials from the PayU Dashboard. Refer to [Access Merchant Key and Salt](doc:generate-merchant-key-and-salt-copy).

| Credential        | Description                        |
| ----------------- | ---------------------------------- |
| **Merchant Key**  | Unique identifier for your account |
| **Merchant Salt** | Used for hash generation           |
| **Client ID**     | For OAuth-based authentication     |
| **Client Secret** | For OAuth-based authentication     |

***

## Development Environment Requirements

### Minimum System Requirements

| Requirement                    | Minimum Version | Recommended |
| ------------------------------ | --------------- | ----------- |
| **Android Studio**             | Arctic Fox+     | Ladybug+    |
| **Android Min SDK Version**    | API 21 (5.0)    | API 24+     |
| **Android Target SDK Version** | API 34          | API 34      |
| **Kotlin**                     | 1.6+            | 1.9+        |
| **Java**                       | 8               | 11+         |
| **Gradle**                     | 7.0+            | 8.0+        |

### Package Manager Support

PayU Android SDKs are available through:

| Package Manager        | Supported | Notes                         |
| ---------------------- | --------- | ----------------------------- |
| **Maven (Gradle)**     | ✅ Yes     | Recommended for most projects |
| **Manual Integration** | ✅ Yes     | AAR files available           |

### Gradle Setup

Add the PayU repository to your project-level `build.gradle`:

```groovy
// Project-level build.gradle
allprojects {
    repositories {
        google()
        mavenCentral()
        maven { url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android" }
    }
}
```

Add the SDK dependency to your app-level `build.gradle`:

```groovy
// App-level build.gradle
dependencies {
    // Add the SDK you need
    implementation 'in.payu:payu-checkoutpro:3.0.0'  // For Checkout Pro SDK
    // implementation 'in.payu:payu-core:7.10.1'    // For Core SDK
}
```

Then sync your Gradle files.

## Android Privacy & Compliance

### Required App Permissions

Add the following permissions to your `AndroidManifest.xml`:

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

### Package Visibility Configuration (Android 11+)

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

### ProGuard/R8 Rules

If you use ProGuard or R8, add the following rules to your `proguard-rules.pro`:

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

***

## Server-Side Hash Generation Setup

PayU uses hash-based verification for security. **Hash must be generated on your server, never on the client.**

The dynamic hashes must be generated at runtime for each transaction and will vary based on the transaction parameters.

<Callout icon="📘" theme="info">
  **Hashing logic for SDK and Web Integration is different** : For the hashing logic for web integration, refer to [Generate Hash](doc:generate-hash-payu-hosted).
</Callout>

### Hash Generation Flow

<Image border={false} src="https://files.readme.io/04949cb-Screenshot_2023-11-16_at_6.14.14_PM.png" />

<br />

## Choose Your SDK

Based on your requirements, select the appropriate SDK:

| Your Requirement                  | Recommended SDK                                             | Integration Effort |
| --------------------------------- | ----------------------------------------------------------- | ------------------ |
| Fastest integration, pre-built UI | [Checkout Pro SDK](/docs/android-checkoutpro-sdk)           | Low                |
| Full UI customization             | [Core SDK](/docs/android-core-sdk)                          | Medium             |
| UPI payments only                 | [UPI SDK](/docs/android-upi-sdk)                            | Low                |
| Google Pay in-app payments        | [Google Pay SDK](/docs/android-google-pay-sdk)              | Low                |
| PhonePe in-app payments           | [PhonePe SDK](/docs/android-phonepe-sdk)                    | Low                |
| Improved card success rates       | Core SDK + [Native OTP Assist](/docs/native-otp-assist-sdk) | Medium             |
| One-click UPI payments            | [UPI Bolt SDK](/docs/payu-bolt-sdk)                         | Low                |
| Native 3D Secure experience       | [3DS 2.0 SDK](/docs/android-3ds20-sdk)                      | Medium             |

## Webhook Setup

Configure webhooks to receive real-time payment notifications.

### Required Webhook Events

| Event             | Description                    |
| ----------------- | ------------------------------ |
| `payment.success` | Payment completed successfully |
| `payment.failed`  | Payment failed                 |
| `payment.pending` | Payment is pending             |
| `refund.success`  | Refund processed successfully  |
| `refund.failed`   | Refund failed                  |

### Webhook Configuration

1. Navigate to **Dashboard → Settings → Webhooks**
2. Click **Create New Webhook**
3. Enter your webhook URL (must be HTTPS)
4. Select the events you want to receive
5. Save and note the webhook secret for verification

<Callout icon="📘" theme="info">
  **Note:** For detailed webhook setup, refer to [Webhooks for Payments](/docs/webhooks-for-payments).
</Callout>

## Choose your integration

> ✅ **Note**: The best SDK for you will depend on your specific needs and requirements.

If you need a quick and easy way to integrate a payment interface into your app, then the Checkout Pro SDK is a good option. If you need more control over the look and feel of the payment interface, then the Core SDK is a good choice. And if you need to accept payments through UPI, OlaMoney, PhonePe, or Native OTP Assist, then the respective SDKs are a good fit.

PayU offers various Android SDKs that each serve a unique use case. Here is a brief overview of the most popular SDKs:

* **Checkout Pro SDK**: The Checkout Pro SDK is a complete, ready-to-use native checkout UI that allows you to integrate a payment interface with minimal effort and get started quickly. The SDK includes a variety of features, such as support for multiple payment methods, a secure payment gateway, and a user-friendly interface.

* **Core SDK**: The Core SDK allows you to integrate the PayU payment gateway into your own payment interface. This gives you more control over the look and feel of the payment interface, as well as the ability to add custom features and functionality.

* **UPI SDK**: The UPI SDK allows you to integrate Unified Payments Interface (UPI) payments into your Android app. UPI is a popular payment method in India that allows users to make payments directly from their bank accounts.

* **PhonePe SDK**: PhonePe SDK offers in-app experience to start collecting payments through instruments saved on PhonePe. Supports UPI, card, and wallet payments along with UPI PIN authentication.

* **Google Pay SDK**: Google Pay SDK offers in-app experience to start collecting payments through instruments saved on Google Pay. Supports UPI, card, and wallet payments along with UPI PIN authentication.

* **OlaMoney SDK**: The OlaMoney SDK allows you to integrate OlaMoney payments into your Android app. OlaMoney is a digital wallet that allows users to make payments for goods and services online and offline.

* **Native OTP Assist SDK**: The Native OTP Assist SDK allows you to capture OTP (One-Time Password) directly from your Android app without redirecting the user to the bank's 3D secure page. This can help to improve the checkout experience and reduce the chances of abandonment.

* **3DS 2.0 SDK**: The 3DS 2.0 SDK provides you the ability to collect additional transaction data such as device location, user's location, and merchant's transaction history. It allows you to protect you and your customers from the threat of payment fraud.

Here is a comparison table that summarizes the key features of the different SDKs:

| SDK                                                        | Features                                                                                                                                                                                                                             | Use Case                                                                             |
| :--------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| [Android CheckoutPro SDK](doc:android-checkoutpro-sdk)     | Complete ready-to-use native checkout UI allows you to get started quickly with minimal effort. This SDK is a great choice for small and medium sized businesses that operates on limited tech resource.                             | **Low Effort Integration** \| **Non-Seamless Checkout** \| **Limited Tech Resource** |
| [Android Core SDK](doc:android-core-sdk)                   | Create your own UI for the payment flow by leveraging various methods exposed in the Core SDK. This SDK is more suitable for larger enterprises that can allocate dedicated engineering resource to develop customised payment flow. | **Seamless Checkout** \| **Medium Effort** \| **Enterprise Businesses**              |
| [Android UPI SDK](doc:android-upi-sdk)                     | This SDK best suited for creating a custom payment UI for UPI only checkout.                                                                                                                                                         | **Low Effort Integration** \| **UPI Checkout**                                       |
| [PhonePe SDK](doc:android-phonepe-sdk)                     | Allows you to integrate PhonePe payments into your Android app.                                                                                                                                                                      | **Low Effort Integration** \| **PhonePe InApp Support**                              |
| [Google Pay SDK](doc:android-google-pay-sdk)               | Allows you to integrate Google Pay payments into your Android app.                                                                                                                                                                   | **Low Effort Integration** \| **Google Pay InApp Support**                           |
| [Android Ola Money SDK](doc:ola-money-sdk)                 | Allows you to integrate OlaMoney payments into your Android app.                                                                                                                                                                     | **Low Effort Integration** \| **OlaMoney Checkout**                                  |
| [Android Custom Browser SDK](doc:custom-browser-sdk)       | Collect netbanking payment on the bank's page with a customized browser experience.                                                                                                                                                  | **Low Effort Integration** \| **Custom Browser Support**                             |
| [Android Native OTP Assist SDK](doc:native-otp-assist-sdk) | Allows you to capture OTP (One Time Password) directly from your Android app without redirecting the user to the bank's 3D secure page.                                                                                              | **Native OTP Support** \| **Low Effort Integration**                                 |
| [Android 3DS 2.0 SDK](doc:android-3ds20-sdk)               | Power native experience on the new 3DS 2.0 protocol for card transactions.                                                                                                                                                           | **3DS 2.0 Support** \| **Low Effort Integration**                                    |
| [Android UPI Bolt SDK](doc:payu-bolt-sdk)                  | Allows you to provide a simpler and more efficient payment experience. Eliminates third-party redirection with higher success rate.                                                                                                  | **One-Click Payment** \| **UPI Checkout**                                            |

***

## Size of SDK

| SDK Name                                       | Latest SDK Version | SDK Size |
| :--------------------------------------------- | :----------------- | :------- |
| [CheckoutPro SDK](doc:android-checkoutpro-sdk) | 3.0.0              | 293KB    |
| [Core PG SDK](doc:android-core-sdk)            | 7.10.1             | 163KB    |
| [CustomBrowser SDK](doc:custom-browser-sdk)    | 7.15.4             | 386KB    |
| [UPI SDK](doc:android-upi-sdk)                 | 1.8.7              | 163KB    |
| [PhonePe SDK](doc:android-phonepe-sdk)         | 1.8.7              | 68KB     |
| [Google Pay SDK](doc:android-google-pay-sdk)   | 4.0.0              | 94KB     |
| [OlaMoney SDK](doc:ola-money-sdk)              | 1.3.9              | 47KB     |
| [Native OTP SDK](doc:native-otp-assist-sdk)    | 1.6.2              | 194KB    |
| [3DS 2.0 SDK](doc:android-3ds20-sdk)           | 1.1.2              | 80KB     |

***

## Next Steps

Once you've completed the prerequisites above, proceed with your chosen SDK integration:

1. **[Integrate Checkout Pro SDK](/docs/android-checkoutpro-sdk)** - For quick, ready-to-use checkout
2. **[Integrate Core SDK](/docs/android-core-sdk)** - For custom payment flows
3. **[Test Your Integration](/docs/test-cards-upi-id-and-wallets)** - Using test credentials
4. **[Go Live Checklist](/docs/production-checklist)** - Before switching to production