---
title: UPI Bolt Capacitor-Ionic-Angular SDK Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
UPI Bolt UI SDK allows you to manage the checkout options on their checkout screen. You use **PayU UPI Bolt UI SDK** for customer registration, payment, and profile management. This integration involves the following steps:

1. [Add SDK Dependency](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-1-add-sdk-dependency)
2. [Platform-Specific Setup](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-2-platform-specific-setup)
3. [Initialize SDK](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-3-initialize-sdk)
4. [Check UPI Bolt Availability](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-4-check-upi-bolt-availability)
5. [Implement Payment Flow](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-5-implement-payment-flow)
6. [Profile Management](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-6-profile-management)
7. [Implement Callbacks](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-7-implement-callbacks)
8. [Hash Generation](https://docs.payu.in/docs/upi-bolt-capacitor-ionic-angular-sdk-integration?isFramePreview=true#step-8-hash-generation)

## Prerequisites

Before integrating PayU UPI Bolt SDK, ensure you have:

* **iOS deployment target**: iOS 17 or higher
* **Capacitor**: Latest stable version
* **Ionic-Angular**: Compatible version
* **PayU merchant account** with valid merchant key
* **Required permissions** for SMS and device access

## Step 1: Add SDK Dependency

Add the PayU UPI Bolt Capacitor plugin to your project:

```bash
npm add payu-upi-bolt-ui-capacitor@0.0.1-alpha.4
```

## Step 2: Platform-Specific Setup

### iOS Setup

1. **Add Dependencies to Podfile**

   ```ruby
   pod 'PayUIndia-UPIBoltCoreKit', '1.0.0-alpha.7'
   ```

2. **Add Framework Files**

   Include the following `.xcframework` files in your iOS project:

   * `CommonLibrary.xcframework` (NPCI)
   * `OlivePayLibrary.xcframework` (AXIS)

<Image align="center" border={false} src="https://files.readme.io/faccd901e8819e5ea87d9cc523c1ae4316dde6c1f5fdc940eeed1b6c182decb3-ionic_react_sdk_integration_uibolt_screen1.png" />

3. **Update Framework Search Path**

   In Xcode, update the Framework Search Path to:

   ```
   $(PROJECT_DIR)/Frameworks
   ```

   <br />

<Image align="center" border={false} src="https://files.readme.io/0aa44949d3de2f3949cf7b59e353efea8f7997da6ff98b2c0cbfd4a7ab257494-ionic_react_sdk_integration_screen2.png" />

### Android Setup

1. **Add Permissions**

   Add the following permissions to your `AndroidManifest.xml`:

   ```xml
   <uses-permission android:name="android.permission.SEND_SMS"/>
   <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
   <uses-permission android:name="android.permission.INTERNET" />
   <uses-permission android:name="android.permission.READ_PHONE_STATE" />
   <uses-permission android:name="android.permission.RECEIVE_SMS" />
   ```

2. **Add Dependencies**

   Add the following dependencies to your `build.gradle` file:

   ```gradle
   dependencies {
       implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.1-dev4'
       implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
   }
   ```

3. **Add AAR File**

   Place the `SecureComponent-release-prod_05062024_9d3904ab.aar` file in the `libs` folder of your Android app module.

## Step 3: Initialize SDK

Initialize the PayU UPI Bolt SDK with your configuration:

```typescript
import { PayUUPIBoltUICapacitorPlugin } from 'payu-upi-bolt-ui-capacitor';

const config = {
  merchantName: "<merchantName>",
  merchantKey: "<merchantKey>",
  phone: "<phone>",
  email: "<email>",
  refId: "<refId>",
  pluginTypes: ["<pluginType>"], // e.g., ["AXIS", "HDFC"]
  clientId: "<clientId>",
  issuingBanks: ["<issuingBanks>"],
  excludedBanksIINs: ["<excludedBanksIIN>"],
  isProduction: <trueOrFalse>, // true for production, false for staging
};

PayUUPIBoltUICapacitorPlugin.initSDK({ config: JSON.stringify(config) });

// Optional: Clear SDK instance
PayUUPIBoltUICapacitorPlugin.reset();
```

**Configuration Parameters:**

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Parameter</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        merchantName<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Name of your merchant
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        merchantKey<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        PayU merchant key
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        phone<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Phone number for registration
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        email<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Customer Email ID
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        refId<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Reference ID
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        pluginTypes<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Array&lt;String&gt;</code><br/>
        List of Supported Plugin (e.g., [AXIS, HDFC])
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        isProduction<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Boolean</code><br/>
        True (Production), false (Staging)
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        clientId<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Unique Client ID
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        issuingBanks<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Array&lt;String&gt;</code><br/>
        List of Issuing Banks
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        excludedBanksIINs<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Array&lt;String&gt;</code><br/>
        Excluded Bank IINs
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Step 4: Check UPI Bolt Availability

Before proceeding with payment flows, verify if UPI Bolt is enabled:

```typescript
PayUUPIBoltUICapacitorPlugin.isUPIBoltEnabled();
```

## Step 5: Implement Payment Flow

### Register and Pay

For first-time users or new transactions:

```typescript
const paymentParams = {
  amount: "<amount>",
  productInfo: "<productInfo>",
  firstName: "<firstName>",
  surl: "<successUrl>",
  furl: "<failureUrl>",
  ios_surl: "<iosSuccessUrl>",
  ios_furl: "<iosFailureUrl>",
  initiationMode: "<initiationMode>",  // e.g., "10"
  purpose: "<purpose>",              // e.g., "00"
  txnId: "<uniqueTransactionId>",
  isCCTxnEnabled: true               // Enable fallback for card transactions
};

PayUUPIBoltUICapacitorPlugin.registerAndPay({ paymentParams: JSON.stringify(paymentParams) });
```

**Payment Parameters:**

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Parameter</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        amount<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Transaction amount
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        txnId<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Unique transaction identifier
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        productInfo<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Description of Product
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        firstName<br/>
        <code>mandatory</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Customer First Name
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        surl<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Success Callback URL
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        furl<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Failure Callback URL
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        ios_surl<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        iOS Success Callback URL
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        ios_furl<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        iOS Failure Callback URL
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        initiationMode<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Payment initiation mode (e.g., "10")
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        purpose<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        Payment purpose code (e.g., "00")
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        isCCTxnEnabled<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Boolean</code><br/>
        Enable fallback for card transactions
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Step 6: Profile Management

### UPI Management Screens

Open various UPI management screens:

```typescript
PayUUPIBoltUICapacitorPlugin.openUPIManagement({ 
  screenType: "ALL" // Alternatives: TRANSACTIONHISTORY, MANAGEUPIACCOUNTS, DISPUTE, DEREGISTERUPI
});
```

**Available Screen Types:**

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Screen Type</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">ALL</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Complete profile management interface</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">TRANSACTIONHISTORY</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction history view</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">MANAGEUPIACCOUNTS</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">UPI account management</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">DISPUTE</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Dispute resolution interface</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">DEREGISTERUPI</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Account deregistration</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Step 7: Implement Callbacks

Implement the required callback methods:

```typescript
import { Plugins } from '@capacitor/core';

  private listeners: { remove: () => void }[] = [];

  ngOnInit() {
    // Helper to register listeners and push them to the array for easy cleanup
    const addListener = (eventName: string, handler: (data: any) => void) => {
      const listener = Plugins['PayUUPIBoltUICapacitorPlugin']['addListener'](eventName, handler);
      this.listeners.push(listener);
    };

    // Specific handler for generateHash
    addListener('generateHash', (data: any) => this.handleHashGeneration(data));

    // Common handler for all other events
    const alertHandler = (data: any) => this.showAlert(data);

    // Attach other PayU event listeners using the shared alert handler
    const eventNames = [
      'onPayUSuccess',
      'onPayUCancel',
      'onPayUFailure',
      'reset',
      'clearCache',
      'isRegistered',
      'isUPIBoltEnabled'
    ];

    eventNames.forEach(event => addListener(event, alertHandler));
  }

  ngOnDestroy() {
    // Clean up all event listeners
    this.listeners.forEach(listener => listener.remove());
  }


```

**Callback Methods:**

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Callback Method</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onPayUSuccess</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Called if payment succeeds
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onPayUFailure</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Triggered on payment failure
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onPayUCancel</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Called when the transaction is cancelled
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onErrorReceived</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Invoked when an error occurs
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onUPIBoltEnabled</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Checks if UPI Bolt is enabled
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>onReset</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Confirms SDK has been reset
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>generateHash</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        Invoked to compute required hash
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Step 8: Hash Generation

Implement secure hash generation for transaction security:

```typescript
async handleHashGeneration(data: HashData): Promise<void> {
  const { hashString, hashName, postSalt } = data;
  
  // Generate hash on your secure server
  const finalHash = await this.generateSecureHash(hashString + "<salt>" + postSalt);
  
  const response = { [hashName]: finalHash };
  PayUUPIBoltUICapacitorPlugin.hashGenerated({ hashData: JSON.stringify(response) });
}

private async generateSecureHash(input: string): Promise<string> {
  // Implement SHA-512 hash generation
  // This should be done on your secure server
  return "<SHA-512-Hash>";
}
```

<Callout icon="📘" theme="info">
  **Note**: Always generate hashes on your secure server. Never expose your salt values in client-side code.
</Callout>

## SMS Hash Generation for Android

For Android OTP auto-read functionality, add the AppSignatureHelper class to your project:

```java
public class AppSignatureHelper {
    private static final String HASH_TYPE = "SHA-256";
    private static final int NUM_HASHED_BYTES = 9;
    private static final int NUM_BASE64_CHAR = 11;
    private Context context;

    public AppSignatureHelper(Context context) {
        this.context = context;
    }

    public ArrayList<String> getAppSignatures() {
        ArrayList<String> appCodes = new ArrayList<>();
        try {
            String packageName = context.getPackageName();
            PackageManager packageManager = context.getPackageManager();
            Signature[] signatures = packageManager.getPackageInfo(packageName,
                    PackageManager.GET_SIGNATURES).signatures;

            for (Signature signature : signatures) {
                String hash = hash(packageName, signature.toCharsString());
                if (hash != null) {
                    appCodes.add(String.format("%s", hash));
                }
            }
        } catch (PackageManager.NameNotFoundException e) {
            Log.e("AppSignatureHelper", "Unable to find package to obtain hash.", e);
        }
        return appCodes;
    }

    private static String hash(String packageName, String signature) {
        String appInfo = packageName + " " + signature;
        try {
            MessageDigest messageDigest = MessageDigest.getInstance(HASH_TYPE);
            messageDigest.update(appInfo.getBytes(StandardCharsets.UTF_8));
            byte[] hashSignature = messageDigest.digest();

            hashSignature = Arrays.copyOfRange(hashSignature, 0, NUM_HASHED_BYTES);
            String base64Hash = Base64.encodeToString(hashSignature, Base64.NO_PADDING | Base64.NO_WRAP);
            base64Hash = base64Hash.substring(0, NUM_BASE64_CHAR);

            return base64Hash;
        } catch (NoSuchAlgorithmException e) {
            Log.e("AppSignatureHelper", "Hash algorithm does not exist.", e);
        }
        return null;
    }
}
```

**Usage:**

```java
Log.d("appSignature", new AppSignatureHelper(requireContext()).getAppSignatures().get(0));
```

Share the generated signature with PayU team for SMS integration setup.

## Error Handling

Handle various error scenarios with these error codes:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Code</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Message</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>0</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Success</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction completed successfully</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>1</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Fail/Invalid Response</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Request failed due to invalid or missing parameters</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>2</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">User cancelled</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">User cancelled the transaction</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>100</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction timeout</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction exceeded time limit</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>104</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">UPI Bolt not supported</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Feature not available for merchant</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>500</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Something went wrong</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Unexpected error occurred</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

**Error Handling Example:**

```typescript
handleError(data: any) {
  const errorCode = data.errorCode || -1;
  const errorMessage = data.errorMessage || "Unknown error";
  
  switch (errorCode) {
    case 100:
      this.showTimeoutError();
      break;
    case 104:
      this.showUPIBoltNotSupported();
      break;
    default:
      this.showGeneralError(errorMessage);
  }
}
```

## Testing

### Test Environment Setup

1. **Use Test Configuration**
   ```typescript
   isProduction: false
   ```

2. **Test Phone Numbers**  
   Use sandbox phone numbers provided by PayU for testing

3. **Test Scenarios**
   * First-time registration and payment
   * Repeat payments for registered users
   * Error scenarios (network issues, timeouts)
   * Profile management flows

## Best Practices

> 📘 **Implementation Tips**
>
> * Always validate user inputs before SDK calls
> * Implement proper error handling for all callback methods
> * Use secure hash generation on server-side
> * Test thoroughly in sandbox environment before production
> * Handle device permissions gracefully
> * Implement proper loading states during SDK operations
> * Always cleanup listeners in ngOnDestroy to prevent memory leaks

## SDK Methods Reference

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse; margin: 20px 0;">
  <thead>
    <tr style="background-color: #f8f9fa;">
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Method</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Description</th>
      <th style="border: 1px solid #dee2e6; padding: 12px; text-align: left; font-weight: 600;">Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>initSDK()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Initialize the SDK</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Configuration object</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>isUPIBoltEnabled()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Check UPI Bolt availability</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">None</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>registerAndPay()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Register user and process payment</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Payment parameters</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>openUPIManagement()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Open profile management screens</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Screen type</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>hashGenerated()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Provide generated hash to SDK</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Hash object</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>reset()</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Reset SDK instance</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">None</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Support

For additional support and documentation:

* **PayU Developer Portal**: [https://docs.payu.in](https://docs.payu.in)
* **Support Email**: [support@payu.in](mailto:support@payu.in)
* **Integration Help**: Contact your PayU integration manager

***

<Callout icon="💡" theme="default">
  ### **Next Steps**

  After successful integration, consider implementing:

  * Advanced error handling and retry mechanisms
  * Analytics tracking for payment flows
  * Custom UI themes to match your app design
  * Server-side webhook handling for payment confirmations
  * Proper lifecycle management for listeners
</Callout>
