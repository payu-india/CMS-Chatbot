---
title: '[Internal Review]iOS Mobile SDKs'
deprecated: false
hidden: true
metadata:
  robots: index
---
Before you begin integrating PayU iOS SDKs into your application, complete the following prerequisites to ensure a smooth integration process.

## 1. Account Setup

### Register and Activate Your PayU Account

| Step | Action                                 | Link                                                            |
| ---- | -------------------------------------- | --------------------------------------------------------------- |
| 1    | Register for a PayU Merchant Account   | [Register](/docs/register-for-a-merchant-account)               |
| 2    | Complete KYC and activate your account | [Activate Account](/docs/activate-account)                      |
| 3    | Access your Test Merchant Key and Salt | [Get Test Credentials](/docs/access-test-merchant-key-and-salt) |

> ⚠️ **Important:** Never use production credentials during development. Always use test credentials until you're ready for go-live.

### Obtain Your Credentials

You'll need the following credentials from the PayU Dashboard:

| Credential        | Description                        | Where to Find                   |
| ----------------- | ---------------------------------- | ------------------------------- |
| **Merchant Key**  | Unique identifier for your account | Dashboard → Settings → API Keys |
| **Merchant Salt** | Used for hash generation           | Dashboard → Settings → API Keys |
| **Client ID**     | For OAuth-based authentication     | Dashboard → Settings → OAuth    |
| **Client Secret** | For OAuth-based authentication     | Dashboard → Settings → OAuth    |

***

## 2. Development Environment Requirements

### Minimum System Requirements

| Requirement               | Minimum Version | Recommended           |
| ------------------------- | --------------- | --------------------- |
| **Xcode**                 | 14.0+           | Latest stable version |
| **iOS Deployment Target** | iOS 12.0        | iOS 13.0+             |
| **Swift**                 | 5.0+            | 5.7+                  |
| **macOS**                 | Monterey (12.0) | Ventura (13.0)+       |

### Package Manager Support

PayU iOS SDKs are available through:

| Package Manager           | Supported  | Notes                              |
| ------------------------- | ---------- | ---------------------------------- |
| **CocoaPods**             | ✅ Yes      | Recommended for most projects      |
| **Swift Package Manager** | ✅ Yes      | Available for select SDKs          |
| **Carthage**              | ⚠️ Limited | Check individual SDK documentation |
| **Manual Integration**    | ✅ Yes      | Framework files available          |

### CocoaPods Setup

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

***

## 3. Apple Privacy & Compliance

### Privacy Manifest Configuration

Starting with iOS 17, Apple requires apps to declare the data they collect. PayU SDKs collect certain data for payment processing.

#### Required Privacy Manifest Entries

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

### Required App Permissions

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

***

## 4. Server-Side Hash Generation Setup

PayU uses hash-based verification for security. **Hash must be generated on your server, never on the client.**

#### Hash Generation Flow

<Image align="center" border={false} src="https://files.readme.io/8b56580f2ac5ff0cb20c9a3aefc14d20a43c892d9b9ca98f0607ae283aef40ca-iOS_SDK_Hash_flow.png" />

#### Hash Formula

```
hash = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
```

#### Sample Server-Side Code

**Node.js:**

```javascript
const crypto = require('crypto');

function generatePayUHash(params, salt) {
    const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${params.udf1 || ''}|${params.udf2 || ''}|${params.udf3 || ''}|${params.udf4 || ''}|${params.udf5 || ''}||||||${salt}`;
    
    return crypto.createHash('sha512').update(hashString).digest('hex');
}
```

**Python:**

```python
import hashlib

def generate_payu_hash(params, salt):
    hash_string = f"{params['key']}|{params['txnid']}|{params['amount']}|{params['productinfo']}|{params['firstname']}|{params['email']}|{params.get('udf1', '')}|{params.get('udf2', '')}|{params.get('udf3', '')}|{params.get('udf4', '')}|{params.get('udf5', '')}||||||{salt}"
    
    return hashlib.sha512(hash_string.encode()).hexdigest()
```

**PHP:**

```php
function generatePayUHash($params, $salt) {
    $hashString = $params['key'] . '|' . $params['txnid'] . '|' . $params['amount'] . '|' . $params['productinfo'] . '|' . $params['firstname'] . '|' . $params['email'] . '|' . ($params['udf1'] ?? '') . '|' . ($params['udf2'] ?? '') . '|' . ($params['udf3'] ?? '') . '|' . ($params['udf4'] ?? '') . '|' . ($params['udf5'] ?? '') . '||||||' . $salt;
    
    return hash('sha512', $hashString);
}
```

<Callout icon="🔒" theme="default">
  **Security Note:** Never embed your Salt in the iOS app. Always generate hashes server-side.
</Callout>

***

## 5. Choose Your SDK

Based on your requirements, select the appropriate SDK:

| Your Requirement                  | Recommended SDK                                                 | Integration Effort | Time Estimate |
| --------------------------------- | --------------------------------------------------------------- | ------------------ | ------------- |
| Fastest integration, pre-built UI | [Checkout Pro SDK](/docs/ios-checkoutpro-sdk)                   | Low                | ~2-3 days     |
| Full UI customization             | [Core SDK](/docs/ios-core-sdk)                                  | Medium             | ~1-2 weeks    |
| UPI payments only                 | [UPI SDK](/docs/ios-upi-sdk)                                    | Low                | ~1-2 days     |
| Improved card success rates       | Core SDK + [Native OTP Assist](/docs/ios-native-otp-assist-sdk) | Medium             | ~1 week       |
| One-click UPI payments            | [UPI Bolt SDK](/docs/payu-upi-bolt-sdk-ios)                     | Low                | ~1-2 days     |
| Native 3D Secure experience       | [3DS 2.0 SDK](/docs/ios-3ds-sdk)                                | Medium             | ~3-5 days     |

### SDK Compatibility Matrix

| SDK          | Can Be Combined With                                |
| ------------ | --------------------------------------------------- |
| Checkout Pro | Native OTP Assist, 3DS 2.0                          |
| Core SDK     | Native OTP Assist, 3DS 2.0, UPI SDK, Custom Browser |
| UPI SDK      | Core SDK                                            |
| UPI Bolt SDK | Standalone                                          |

***

## 6. Webhook Setup

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

***

## 7. Support Resources

| Resource                | Description                      | Link                                              |
| ----------------------- | -------------------------------- | ------------------------------------------------- |
| **API Reference**       | Complete API documentation       | [API Docs](/reference)                            |
| **Sample Apps**         | Working code examples            | Check individual SDK docs                         |
| **Dashboard**           | Manage transactions and settings | [PayU Dashboard](https://dashboard.payu.in)       |
| **Integration Support** | Technical assistance             | Contact your Account Manager                      |
| **Email Support**       | General queries                  | [integration@payu.in](mailto:integration@payu.in) |

***

## Next Steps

Once you've completed the prerequisites above, proceed with your chosen SDK integration:

1. **[Integrate Checkout Pro SDK](/docs/ios-checkoutpro-sdk)** - For quick, ready-to-use checkout
2. **[Integrate Core SDK](/docs/ios-core-sdk)** - For custom payment flows
3. **[Test Your Integration](/docs/test-cards-upi-id-and-wallets)** - Using test credentials
4. **[Go Live Checklist](/docs/production-checklist)** - Before switching to production
