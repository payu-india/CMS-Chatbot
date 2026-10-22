---
title: '[Internal Review]Capacitor Checkout Pro Integration'
deprecated: false
hidden: true
icon: fad fa-air-conditioner
link:
  new_tab: false
metadata:
  robots: index
---
---
title: Capacitor Checkout Pro Integration
excerpt: Integrate the PayU Checkout Pro plugin into your Ionic Capacitor app to accept payments on Android and iOS with a ready-to-use native checkout UI.
metadata:
  title: Capacitor Checkout Pro Integration | PayU Developer Docs
  description: Step-by-step guide to integrate the PayU Checkout Pro Capacitor plugin on Android and iOS, including server-side hash generation, recurring payments, SKU offers and payment callbacks.
  keywords: PayU, Capacitor, Ionic, Checkout Pro, mobile SDK, Android, iOS, payment plugin, hash generation, recurring payments
  robots: index
next:
  pages:
    - type: basic
      slug: integration-steps-android-checkout-pro
      title: Android Checkout Pro Integration
---

<Banner color="yellow">
**Integration effort:** Low. You install one plugin, build the payment parameters, generate hashes on your server and handle four callbacks.
</Banner>

The PayU Checkout Pro plugin for Capacitor gives your Ionic Capacitor app a complete, ready-to-use native checkout UI on both Android and iOS. Your app passes the payment details to the plugin, and the plugin handles payment method selection, authentication and the payment itself.

***

## Before you start

### Prerequisites

- A PayU merchant account. For more information, refer to [Register for a Merchant Account](/docs/register-for-a-merchant-account).
- Your test **key** and **salt** from the PayU Dashboard. Keep the salt on your server only.
- A backend endpoint that generates SHA-512 hashes for the plugin (see [Step 5](#step-5-generate-the-hash-on-your-server)).
- The payment methods you want to offer, enabled from **Dashboard > Settings > Payment methods**.

### Compatibility

| Platform | Requirement |
| :--- | :--- |
| Android | Min SDK version 21 and above |
| Android | Compile SDK version 31 and above |
| iOS | Minimum deployment target iOS 11 |

{/* SME-CHECK: Android values are from the Confluence source (21 / 31). CTP-377 moved the native Android SDKs (including Checkout Pro) to Min SDK 24 / Compile SDK 36. Confirm which values apply to this plugin. */}

### Plugin version

| Item | Value |
| :--- | :--- |
| npm package (install) | `payu-checkoutpro-capacitor` |
| Import module | `capacitor-payu-checkoutpro` |
| Current version | `0.0.0-alpha.1` |

<Callout icon="📘" theme="info">
### **Note**

The package name you install and the module name you import are different. This is expected. Use `payu-checkoutpro-capacitor` with `npm install`, and `capacitor-payu-checkoutpro` in your `import` statement.
</Callout>

***

## Integration steps

1. Install the plugin and sync the native projects.
2. Complete the platform-specific setup (Android and iOS).
3. Import the plugin.
4. Build the payment parameters and checkout configuration.
5. Generate the hash on your server.
6. Launch the checkout screen.
7. Handle the payment callbacks.
8. Verify the payment on your server.

***

## Step 1: Install the plugin and sync

Run the following commands from the root folder of your Capacitor project:

```bash
npm install payu-checkoutpro-capacitor@0.0.0-alpha.1
npx cap sync
```

`npx cap sync` copies the installed plugin into the native Android and iOS projects. Run it again whenever you update the plugin.

{/* SME-CHECK: The Confluence source installs "@capacitor/payu-checkoutpro-capacitor@0.0.0-alpha.1" (scoped). The SME confirmed the unscoped name "payu-checkoutpro-capacitor". Confirm that "payu-checkoutpro-capacitor@0.0.0-alpha.1" resolves on npm. */}

**Expected output:** the plugin appears in `package.json`, and `npx cap sync` completes for both the `android` and `ios` platforms without errors.

***

## Step 2: Complete the platform-specific setup

<Tabs>
<Tab title="Android">

No extra step is needed after `npx cap sync` in most projects.

If your build fails with the following manifest merger error:

```text
Attribute application@theme value=(@style/Theme.TestApp) from AndroidManifest.xml:13:9-45 is also present at [in.payu:payu-checkout-pro-ui:1.9.20] AndroidManifest.xml:29:9-44 value=(@style/OnePayuTheme). Suggestion: add 'tools:replace="android:theme"' to <application> element at AndroidManifest.xml:5:5-24:19 to override.
```

Add `tools:replace="android:theme"` to the `<application>` tag of your app's `android/app/src/main/AndroidManifest.xml`:

```xml
<manifest xmlns:android="<redacted URL>"
    xmlns:tools="<redacted URL>">

    <application
        tools:replace="android:theme"
        ... >
    </application>
</manifest>
```

</Tab>
<Tab title="iOS">

1. Make sure the minimum deployment target of your iOS app is **iOS 11** or later.
2. Install the CocoaPods dependencies from the `ios/App` folder of your Capacitor project:

```bash
cd ios/App
pod install
```

3. Open `ios/App/App.xcworkspace` (not the `.xcodeproj`) in Xcode to build and run the app.

</Tab>
</Tabs>

**Expected output:** the app builds and launches on an Android device or emulator and on an iOS device or simulator.

***

## Step 3: Import the plugin

Import the plugin in the TypeScript page where you start the payment:

```typescript
import { PayUCheckoutProCapacitor } from 'capacitor-payu-checkoutpro';
```

***

## Step 4: Build the payment parameters

The plugin needs two objects:

- `payUPaymentParams`: details of the current payment.
- `payUCheckoutProConfig`: how the checkout screen looks and behaves.

### 4.1 Payment parameters

```typescript
let payUPaymentParams: any = {
  key: 'YOUR_MERCHANT_KEY',
  transactionId: 'TXN1729580000123',      // unique, max 25 characters, no special characters
  amount: '100.0',
  productInfo: 'Macbook Pro',
  firstName: 'John',
  email: 'john@example.com',
  phone: '9999999999',
  ios_surl: 'https://cbjs.payu.in/sdk/success',     // test only
  ios_furl: 'https://cbjs.payu.in/sdk/failure',     // test only
  android_surl: 'https://cbjs.payu.in/sdk/success', // test only
  android_furl: 'https://cbjs.payu.in/sdk/failure', // test only
  environment: '1',       // '1' = Test, '0' = Production
  isProduction: false,    // false = Test mode, true = Production mode
  userCredential: 'YOUR_MERCHANT_KEY:john@example.com', // optional, for saved cards
  userToken: 'User123456',                              // optional, for offers
  additionalParam: {
    udf1: null,
    udf2: null,
    udf3: null,
    udf4: null,
    udf5: null
    // walletUrn: '<Wallet URN>',        // optional, pass only when applicable
    // SodexoSourceId: '<Source ID>'     // optional, pass only when applicable
  },
  enableNativeOtp: true
};
```

### 4.2 Environment parameters

The plugin uses two parameters to select the environment. Set both of them, and keep them consistent: Test with Test, Production with Production.

| Parameter | Type | Purpose | Test value | Production value |
| :--- | :--- | :--- | :--- | :--- |
| `environment` | `String` | Selects the PayU environment that the plugin connects to. | `'1'` | `'0'` |
| `isProduction` | `Boolean` | Sets the plugin's mode (test or production). | `false` | `true` |

{/* SME-CHECK: Confirm whether both parameters are mandatory, and what happens if they don't match (for example environment '0' with isProduction false). */}

<Callout icon="❗️" theme="error">
### **Watch out!**

Use your **test** key with `environment: '1'` and `isProduction: false`. Use your **production** key with `environment: '0'` and `isProduction: true`. Mixing them causes the payment to fail.
</Callout>

### 4.3 Payment parameter reference

**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `key` | `String` Your merchant key from PayU. | `"sms***"` |
| `transactionId` | `String` Unique for each transaction. Cannot be null or empty. Maximum 25 characters. It cannot contain special characters such as `_`, `$`, `%` or `&`. | `"TXN1729580000123"` |
| `amount` | `String` Total transaction amount. | `"100.0"` |
| `productInfo` | `String` Information about the product. | `"Macbook Pro"` |
| `firstName` | `String` Customer's first name. | `"John"` |
| `email` | `String` Customer's email ID. | `"john@example.com"` |
| `phone` | `String` Customer's phone number. | `"9999999999"` |
| `android_surl` / `ios_surl` | `String` URL that PayU loads when the payment succeeds. For testing, use `https://cbjs.payu.in/sdk/success`. Don't go live with this URL. | `"https://cbjs.payu.in/sdk/success"` |
| `android_furl` / `ios_furl` | `String` URL that PayU loads when the payment fails. For testing, use `https://cbjs.payu.in/sdk/failure`. Don't go live with this URL. | `"https://cbjs.payu.in/sdk/failure"` |
| `environment` | `String` `'1'` for Test, `'0'` for Production. | `"1"` |
| `isProduction` | `Boolean` `false` for Test mode, `true` for Production mode. | `false` |
| `additionalParam` | `Object` Must include `udf1`–`udf5`. See [4.4 Additional parameters](#44-additional-parameters). | See below |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `userCredential` | `String` Used for saved cards. PayU saves cards against this value and uses it to show the customer's saved cards. Format: `<merchantKey>:<userId>`, where `userId` is any ID, email or phone number that uniquely identifies the customer. | `"merchantKey:userId"` |
| `userToken` | `String` Lets the offer engine apply user-level velocity rules. For card offers (credit card, debit card, EMI), the rules apply to this token if you pass it, or to the card number if you don't. For UPI, Net Banking and Wallet offers, it's required; without it the rules aren't applied. Pass it only if you use offers. | `"User123456"` |
| `enableNativeOtp` | `Boolean` Turns on native OTP for card payments. | `true` |
| `payUSIParams` | `Object` Recurring payment (standing instruction) details. See [4.5 Recurring payments](#45-recurring-payments-optional). | See below |
| `skuDetails` | `Object` SKU details for SKU-based offers. Required only when you use SKU-based offers. See [4.6 SKU details](#46-sku-details-optional). | See below |

### 4.4 Additional parameters

| Parameter | Required | Description | Example |
| :--- | :--- | :--- | :--- |
| `udf1`–`udf5` | Mandatory (value can be `null`) | User-defined fields, for example to store your customer ID or order reference. You must include all five keys in the request. Pass `null` when you have no value. | `"udf1"` or `null` |
| `walletUrn` | Optional | Wallet URN for closed-loop wallet payments. Pass it only when it applies to your integration. | `"67890987"` |
| `SodexoSourceId` | Optional | Source ID used to show the customer's saved Sodexo card. Pass it only when it applies to your integration. | `"456788765678"` |

<Callout icon="📘" theme="info">
### **Remember**

If you pass values in `udf1`–`udf5`, the same values must be used when your server builds the hash. The plugin includes them in the `hashString` it sends you, so always hash the string exactly as you receive it.
</Callout>

### 4.5 Recurring payments (optional)

To take a recurring payment (standing instruction), create a `payUSIParams` object and add it to `payUPaymentParams`:

```typescript
const payUSIParams = {
  isFreeTrial: false,
  billingAmount: '200',
  billingCycle: 'MONTHLY',
  billingCurrency: 'INR',
  billingInterval: '1',
  paymentStartDate: '2027-05-06',
  paymentEndDate: '2028-05-10',
  remarks: 'Subscription payment',
  billingDate: '' // Optional
};

payUPaymentParams.payUSIParams = payUSIParams;
```

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `isFreeTrial` | `Boolean` | Set to `true` for a free trial. | `false` |
| `billingAmount` | `String` | Amount charged in each billing cycle. | `"200"` |
| `billingCycle` | `String` | How often the customer is charged. Allowed values: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ADHOC`, `ONCE`. | `"MONTHLY"` |
| `billingCurrency` | `String` | Billing currency. | `"INR"` |
| `billingInterval` | `String` | Number of billing cycles between charges, passed as a string. For example, `'1'` with `MONTHLY` means every month. | `"1"` |
| `paymentStartDate` | `String` | Date of the first payment, in `YYYY-MM-DD` format. | `"2027-05-06"` |
| `paymentEndDate` | `String` | Date of the last payment, in `YYYY-MM-DD` format. Must be later than `paymentStartDate`. | `"2028-05-10"` |
| `remarks` | `String` | Description of the recurring payment. | `"Subscription payment"` |
| `billingDate` | `String` | Optional. | `""` |

{/* SME-CHECK: Add a one-line description and format for billingDate. */}

For more information, refer to [Recurring Payments Integration](/docs/introduction-recurring-payments-integration).

### 4.6 SKU details (optional)

`skuDetails` is optional if you don't use SKU-based offers. If you use SKU-based offers, it's required.

Create one SKU entry for each product in the cart and assign the list to `payUPaymentParams`:

```typescript
const skuDetails = {
  skus: [
    {
      skuId: 'SKU-1001',        // Product ID used when creating the offer on the Dashboard
      skuName: 'Macbook Pro',   // Product name
      skuAmount: '60.0',        // Price of one unit
      quantity: 1,              // Quantity in the cart
      offerKeys: null           // Optional: offer keys to restrict the offer to this product, else null
    },
    {
      skuId: 'SKU-1002',
      skuName: 'Laptop Sleeve',
      skuAmount: '20.0',
      quantity: 2,
      offerKeys: null
    }
  ]
};

payUPaymentParams.skuDetails = skuDetails;
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `skuId` | `String` | Product ID that you used when you created the offer on the Dashboard. |
| `skuName` | `String` | Name of the product. |
| `skuAmount` | `String` | Amount for one unit of the product. |
| `quantity` | `Number` | Total quantity of the product in the cart. |
| `offerKeys` | `Array<String>` or `null` | Optional. Pass offer keys only if you want to restrict the offer to this product. Otherwise, pass `null`. |

<Callout icon="❗️" theme="error">
### **Watch out!**

When you pass SKU details, `amount` in `payUPaymentParams` must equal the sum of `quantity × skuAmount` for all items. In the example above, that's `1 × 60.0 + 2 × 20.0 = 100.0`.
</Callout>

{/* SME-CHECK: Confirm the Capacitor property name ("skuDetails") and the object shape ({ skus: [...] }). The shape follows the Android Checkout Pro SkuDetails/SKU classes. */}

For more information, refer to [SKU-based offers](/docs/sku-based-offer-payu-hosted-checkout).

### 4.7 Checkout configuration

```typescript
let payUCheckoutProConfig: any = {
  primaryColor: '#4A90E2',
  secondaryColor: '#FFFFFF',
  merchantName: 'Your Store',
  merchantLogo: this.merchantLogo,
  showExitConfirmationOnCheckoutScreen: true,
  showExitConfirmationOnPaymentScreen: true,
  cartDetails: [{ 'Order total': '100.0' }],
  merchantResponseTimeout: '10000',
  autoSelectOtp: true,
  // Android-specific properties
  autoApprove: false,
  merchantSMSPermission: true,
  showCbToolbar: true,
  showMerchantLogo: true,
  enableSavedCard: true,
  enableSslDialog: true,
  baseTextColor: '#000000',
  enableREOptions: true
};
```

| Parameter | Type | Platform | Description |
| :--- | :--- | :--- | :--- |
| `primaryColor` | `String` | Android, iOS | Primary colour of the checkout screen (hex). |
| `secondaryColor` | `String` | Android, iOS | Secondary colour of the checkout screen (hex). |
| `merchantName` | `String` | Android, iOS | Your business name shown on the checkout screen. |
| `merchantLogo` | `String` | Android, iOS | Your logo shown on the checkout screen. |
| `showExitConfirmationOnCheckoutScreen` | `Boolean` | Android, iOS | Shows a confirmation dialog when the customer tries to leave the checkout screen. |
| `showExitConfirmationOnPaymentScreen` | `Boolean` | Android, iOS | Shows a confirmation dialog when the customer tries to leave the payment (bank) screen. |
| `cartDetails` | `Array` | Android, iOS | Order details shown to the customer, as key-value pairs. |
| `merchantResponseTimeout` | `String` | Android, iOS | Time, in milliseconds, that the plugin waits for the response from your surl/furl. |
| `autoSelectOtp` | `Boolean` | Android, iOS | Automatically selects the OTP option on the bank page. |
| `autoApprove` | `Boolean` | Android | Automatically submits the OTP after it's read. |
| `merchantSMSPermission` | `Boolean` | Android | Asks for SMS permission to read the OTP. |
| `showCbToolbar` | `Boolean` | Android | Shows the toolbar on the bank page. |
| `showMerchantLogo` | `Boolean` | Android | Shows your logo on the checkout screen. |
| `enableSavedCard` | `Boolean` | Android | Shows the customer's saved cards. Requires `userCredential`. |
| `enableSslDialog` | `Boolean` | Android | Shows a dialog to the customer when an SSL error occurs on the bank page. |
| `baseTextColor` | `String` | Android | Base text colour of the checkout screen (hex). |
| `enableREOptions` | `Boolean` | Android | |

{/* SME-CHECK: Confirm the descriptions of autoApprove, merchantResponseTimeout (unit), showMerchantLogo, enableSslDialog and baseTextColor, and provide a description for enableREOptions. These six are retained per SME; descriptions are inferred from the parameter names and the native Checkout Pro SDK. */}

***

## Step 5: Generate the hash on your server

The plugin uses SHA-512 hashes to secure each payment request. When the plugin needs a hash, it emits a `generateHash` event with two values:

- `hashName`: the name of the hash it needs.
- `hashString`: the string to hash, **without** your salt.

Your app sends these values to your server. Your server appends the salt, creates the SHA-512 hash and returns it. Your app then passes the hash back to the plugin.

```text
Plugin ──generateHash(hashName, hashString)──▶ App ──▶ Your server
                                                         sha512(hashString + salt)
Plugin ◀──hashGenerated({ [hashName]: hash })── App ◀── hash
```

<Callout icon="❗️" theme="error">
### **Watch out!**

Never put your salt in the app. Anyone can extract it from the app package and use it to tamper with payments. Always generate hashes on your server.
</Callout>

### 5.1 Listen for the `generateHash` event in the app

```typescript
import { Plugins } from '@capacitor/core';

private generateHashListener: any;

this.generateHashListener = Plugins['PayUCheckoutProCapacitor']['addListener']('generateHash', async (data: any) => {
  if (data == null) {
    return;
  }
  try {
    const hashName: string = data.hashName;
    const hashString: string = data.hashString;

    // Send the hash data to your server. The salt stays on the server.
    const res = await fetch('<redacted URL>', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ hashName, hashString })
    });
    const { hash } = await res.json();

    // Return the hash to the plugin, using hashName as the key
    PayUCheckoutProCapacitor.hashGenerated({
      hashData: JSON.stringify({ [hashName]: hash })
    });
  } catch (error) {
    console.error('Hash generation failed:', error);
  }
});
```

### 5.2 Generate the hash on your server

<Tabs>
<Tab title="Node.js">

```javascript
const express = require('express');
const crypto = require('crypto');

const app = express();
app.use(express.json());

const MERCHANT_SALT = process.env.PAYU_SALT; // never hard-code or ship the salt

app.post('/payu/hash', (req, res) => {
  const { hashName, hashString } = req.body;
  if (!hashName || !hashString) {
    return res.status(400).json({ error: 'hashName and hashString are required' });
  }
  const hash = crypto
    .createHash('sha512')
    .update(hashString + MERCHANT_SALT)
    .digest('hex');
  res.json({ hashName, hash });
});

app.listen(3000);
```

</Tab>
<Tab title="Python">

```python
import hashlib
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
MERCHANT_SALT = os.environ["PAYU_SALT"]  # never hard-code or ship the salt

@app.post("/payu/hash")
def generate_hash():
    body = request.get_json()
    hash_name = body.get("hashName")
    hash_string = body.get("hashString")
    if not hash_name or not hash_string:
        return jsonify(error="hashName and hashString are required"), 400
    digest = hashlib.sha512((hash_string + MERCHANT_SALT).encode("utf-8")).hexdigest()
    return jsonify(hashName=hash_name, hash=digest)
```

</Tab>
<Tab title="PHP">

```php
<?php
$salt = getenv('PAYU_SALT'); // never hard-code or ship the salt
$body = json_decode(file_get_contents('php://input'), true);

$hashName   = $body['hashName']   ?? '';
$hashString = $body['hashString'] ?? '';

if ($hashName === '' || $hashString === '') {
    http_response_code(400);
    echo json_encode(['error' => 'hashName and hashString are required']);
    exit;
}

$hash = hash('sha512', $hashString . $salt);
header('Content-Type: application/json');
echo json_encode(['hashName' => $hashName, 'hash' => $hash]);
```

</Tab>
</Tabs>

<Callout icon="📘" theme="info">
### **Critical rules**

- Hash the `hashString` exactly as you receive it. Don't trim, re-order or re-encode it.
- Append the salt at the end: `sha512(hashString + salt)`.
- Return the hash in lowercase hex.
- The plugin can ask for several hashes during one payment. Handle each `generateHash` event separately and always use the `hashName` you received as the key.
- Protect your hash endpoint (for example, with your app's user session) so it can't be used by others.
</Callout>

{/* SME-CHECK: The Android Checkout Pro SDK also passes a postSalt value for additional charges and split payments (sha512(hashString + salt + postSalt)). Confirm whether the Capacitor generateHash event includes postSalt. */}

***

## Step 6: Launch the checkout screen

Combine the payment parameters and checkout configuration, and open the checkout screen:

```typescript
const payuParams = {
  payUPaymentParams,
  payUCheckoutProConfig
};

// Launches the PayU Checkout screen with payment params and config
PayUCheckoutProCapacitor.openCheckoutScreen({ params: JSON.stringify(payuParams) });
```

<Callout icon="📘" theme="info">
### **Remember**

Register the `generateHash` listener (Step 5) and the payment callback listeners (Step 7) **before** you call `openCheckoutScreen`.
</Callout>

**Expected output:** the PayU checkout screen opens and shows the payment methods enabled for your account.

***

## Step 7: Handle the payment callbacks

The plugin emits the following events:

| Event | When it's emitted |
| :--- | :--- |
| `onPaymentSuccess` | The payment succeeded. |
| `onPaymentFailure` | The payment failed. |
| `onPaymentCancel` | The customer cancelled the payment. |
| `onError` | An error occurred, for example a validation error or a failure to fetch payment options. |

```typescript
private onPayUSuccessListener: any;
private onPayUCancelListener: any;
private onPayUFailureListener: any;
private onPayUErrorListener: any;

this.onPayUSuccessListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentSuccess', (data: any) => {
  // Payment succeeded. Verify it on your server before you fulfil the order.
});

this.onPayUFailureListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentFailure', (data: any) => {
  // Payment failed. Show a message and let the customer retry.
});

this.onPayUCancelListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentCancel', (data: any) => {
  // Customer cancelled. If the payment had already reached the bank page, check its status on your server.
});

this.onPayUErrorListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onError', (data: any) => {
  // Show the error message and log it.
});
```

<Callout icon="👍" theme="okay">
### **Tip**

Remove the listeners when the page is destroyed, so they aren't registered twice on the next payment:

```typescript
ngOnDestroy() {
  this.generateHashListener?.remove();
  this.onPayUSuccessListener?.remove();
  this.onPayUFailureListener?.remove();
  this.onPayUCancelListener?.remove();
  this.onPayUErrorListener?.remove();
}
```
</Callout>

### Sample responses

The success and failure events return the PayU response for the payment. The samples below are based on the [Android Checkout Pro sample responses](/docs/integration-steps-android-checkout-pro).

{/* SME-CHECK: Confirm the Capacitor event structure. These samples assume the event data contains "payuResponse" (the PayU response, as a JSON string) and "merchantResponse" (the response from your surl/furl), matching the Android SDK's CP_PAYU_RESPONSE and CP_MERCHANT_RESPONSE. Also confirm the payload of onPaymentCancel (Android passes isTxnInitiated) and onError (Android passes errorMessage). */}

**Event data structure**

```json
{
  "payuResponse": "<PayU response as a JSON string>",
  "merchantResponse": "<response from your surl/furl>"
}
```

<Tabs>
<Tab title="Card / NB / Wallet – success">

```json
{
  "id": 403993715526100438,
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "gt***",
  "txnid": "1651831862726",
  "transaction_fee": "1.00",
  "amount": "1.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "addedon": "2022-05-06 15:41:38",
  "productinfo": "Macbook Pro",
  "firstname": "John",
  "email": "john@example.com",
  "phone": "7879*******",
  "udf1": "udf1",
  "udf2": "udf2",
  "udf3": "udf3",
  "udf4": "udf4",
  "udf5": "udf5",
  "hash": "<response hash>",
  "field1": "711633",
  "field2": "393337",
  "field3": "20220506",
  "field4": "0",
  "field5": "341867702575",
  "field6": "00",
  "field7": "AUTHPOSITIVE",
  "field8": "Approved or completed successfully",
  "field9": "No Error",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_no": "711633",
  "ibibo_code": "MASTCC",
  "error_code": "E000",
  "Error_Message": "No Error",
  "name_on_card": "PayuUser",
  "card_no": "512345XXXXXX2346",
  "issuing_bank": "HDFC",
  "card_type": "MAST",
  "is_seamless": 1,
  "surl": "https://cbjs.payu.in/sdk/success",
  "furl": "https://cbjs.payu.in/sdk/failure"
}
```

</Tab>
<Tab title="Card / NB / Wallet – failure">

```json
{
  "id": "15130876153",
  "mode": "CC",
  "status": "failure",
  "unmappedstatus": "failed",
  "key": "sm*****",
  "txnid": "1651832033713",
  "transaction_fee": "1.00",
  "amount": "1.00",
  "cardCategory": "domestic",
  "addedon": "2022-05-06 15:44:09",
  "productinfo": "Macbook Pro",
  "firstname": "John",
  "email": "john@example.com",
  "phone": "7879*******",
  "udf1": "udf1",
  "udf2": "udf2",
  "udf3": "udf3",
  "udf4": "udf4",
  "udf5": "udf5",
  "hash": "<response hash>",
  "field7": "EVNEGATIVE",
  "field9": "PROCEED",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "ibibo_code": "CC",
  "error_code": "E1302",
  "Error_Message": "Bank failed to authenticate the customer due to 3D Secure Enrollment decline",
  "name_on_card": "PayuUser",
  "card_no": "512345XXXXXX2346",
  "issuing_bank": "HDFC",
  "card_type": "MAST",
  "is_seamless": 1,
  "surl": "https://cbjs.payu.in/sdk/success",
  "furl": "https://cbjs.payu.in/sdk/failure"
}
```

</Tab>
<Tab title="UPI Intent / In-app – success">

```json
{
  "status": "success",
  "result": {
    "mihpayid": 15130530926,
    "mode": "UPI",
    "status": "success",
    "key": "sm*****",
    "txnid": "1651828235258",
    "amount": "1.00",
    "addedon": "2022-05-06 14:40:48",
    "productinfo": "Macbook Pro",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "7879*******",
    "udf1": "udf1",
    "udf2": "udf2",
    "udf3": "udf3",
    "udf4": "udf4",
    "udf5": "udf5",
    "field3": "andy**********@okhdfcbank",
    "field7": "APPROVED OR COMPLETED SUCCESSFULLY|00",
    "field9": "Success|Completed Using Callback",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "UPI-PG",
    "error": "E000",
    "error_Message": "No Error",
    "net_amount_debit": 1,
    "unmappedstatus": "captured",
    "hash": "<response hash>",
    "bank_ref_no": "212631548690",
    "bank_ref_num": "212631548690",
    "bankcode": "INTENT"
  }
}
```

</Tab>
<Tab title="UPI Intent / In-app – failure">

```json
{
  "status": "success",
  "result": {
    "mihpayid": "15130540072",
    "mode": "UPI",
    "status": "failure",
    "key": "sm*****",
    "txnid": "1651828340011",
    "amount": "1.00",
    "addedon": "2022-05-06 14:42:25",
    "productinfo": "Macbook Pro",
    "firstname": "John",
    "email": "john@example.com",
    "phone": "7879******",
    "udf1": "udf1",
    "udf2": "udf2",
    "udf3": "udf3",
    "udf4": "udf4",
    "udf5": "udf5",
    "field9": "response_from_psp",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "UPI-PG",
    "error": "E308",
    "error_Message": "Transaction Failed at bank end.",
    "net_amount_debit": "0",
    "unmappedstatus": "failed",
    "hash": "<response hash>",
    "bankcode": "INTENT"
  }
}
```

</Tab>
</Tabs>

<Callout icon="🚧" theme="warn">
### **Callback response notes**

- For UPI Intent and in-app payments, you don't receive a callback on your surl or furl, and the response format is different from other payment methods (the payment details are inside `result`). Handle both formats.
- Use `mihpayid` (or `id`) in the PayU response as the PayU ID for the payment.
- In the outer UPI response, `status: "success"` means the response was received. Always read the payment status from `result.status`.
</Callout>

***

## Step 8: Verify the payment on your server

Don't rely on the app callback alone to fulfil an order. Before you deliver the goods or service:

1. Check the reverse hash of the response on your server, using your salt.
2. Confirm the payment status with the [Verify Payment API](/reference/verify_payment_api) or a [Webhook](/docs/webhooks).
3. If the customer cancelled after reaching the bank page, or the app closed before a callback, use the Verify Payment API to get the final status.

{/* SME-CHECK: Confirm the Verify Payment API and Webhooks slugs. */}

***

## Test the integration

<Callout icon="📘" theme="info">
### **Testing checklist**

- Use your **test** key and salt.
- Set `environment: '1'` and `isProduction: false`.
- Use the test surl and furl: `https://cbjs.payu.in/sdk/success` and `https://cbjs.payu.in/sdk/failure`.
- UPI Intent and in-app flows aren't available in test mode.
</Callout>

Use the test credentials in the [Android Checkout Pro integration guide](/docs/integration-steps-android-checkout-pro) (test card, Net Banking and UPI VPAs). Test credentials work only in the test environment.

Test at least these scenarios on both Android and iOS:

| Scenario | Expected result |
| :--- | :--- |
| Successful card payment | `onPaymentSuccess` is emitted, and your server verifies the payment. |
| Failed card payment | `onPaymentFailure` is emitted. |
| Customer closes the checkout | `onPaymentCancel` is emitted. |
| Wrong hash returned | The payment fails or `onError` is emitted. |
| Recurring payment with `payUSIParams` | The mandate is created with the billing details you passed. |
| SKU offer with `skuDetails` | The offer is applied and `amount` matches the cart total. |

***

## Go-live checklist

1. **Production key and salt:** replace the test key and salt with your production key and salt. Log in to the PayU Dashboard, switch to **Live Mode** and go to **Developers > API Keys**.
2. **Environment:** set `environment: '0'` and `isProduction: true`.
3. **surl and furl:** replace the `cbjs.payu.in` test URLs with your own. For more information, refer to [Handling SURL and FURL](/docs/handling-redirect-surlfurl-urls).
4. **Hash endpoint:** your production server uses the production salt, and the salt isn't in the app.
5. **Verify Payment and Webhooks:** set up the Verify Payment API and Webhooks as a back-up for missed callbacks.
6. **Listeners:** listeners are removed when the page closes.

{/* SME-CHECK: Confirm whether the Android manifest meta-data entries used for test mode in the native SDK (payu_debug_mode_enabled, payu_web_service_url, payu_post_url) also apply to this plugin, and the slug for Handling SURL and FURL. */}

***

## FAQs

<Accordion title="Why are the install package name and the import name different?" icon="fa-circle-question">
This is how the plugin is published. Install `payu-checkoutpro-capacitor` with npm, and import from `capacitor-payu-checkoutpro` in your code.
</Accordion>

<Accordion title="Do I need to pass both environment and isProduction?" icon="fa-circle-question">
Yes. `environment` selects the PayU environment (`'1'` Test, `'0'` Production), and `isProduction` sets the plugin's mode (`false` Test, `true` Production). Keep them consistent.
</Accordion>

<Accordion title="Can I generate the hash in the app?" icon="fa-circle-question">
No. Always generate hashes on your server. If the salt is in the app, it can be extracted and misused.
</Accordion>

<Accordion title="Do I have to pass udf1–udf5 even if I don't use them?" icon="fa-circle-question">
Yes. Include all five keys in `additionalParam`, and pass `null` when you have no value.
</Accordion>

<Accordion title="When should I pass walletUrn or SodexoSourceId?" icon="fa-circle-question">
Only when they apply to your integration: `walletUrn` for closed-loop wallet payments, and `SodexoSourceId` to show a customer's saved Sodexo card. Both are optional.
</Accordion>

<Accordion title="What date format do recurring payments use?" icon="fa-circle-question">
`YYYY-MM-DD`, for example `2027-05-06`.
</Accordion>

***

## Next steps

<Cards columns={3}>
  <Card title="Android Checkout Pro" href="/docs/integration-steps-android-checkout-pro" icon="fa-mobile">
    Native Android integration and sample responses.
  </Card>
  <Card title="Recurring Payments" href="/docs/introduction-recurring-payments-integration" icon="fa-repeat">
    Set up subscriptions and standing instructions.
  </Card>
  <Card title="Webhooks" href="/docs/webhooks" icon="fa-bell">
    Receive payment updates on your server.
  </Card>
</Cards>
