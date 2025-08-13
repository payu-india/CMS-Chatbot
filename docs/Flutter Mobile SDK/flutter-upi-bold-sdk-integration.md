---
title: Flutter UPI Bold SDK Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU UPI Bolt SDK enables efficient and seamless payment experiences within your Flutter applications. This SDK eliminates third-party redirection, provides one-click payment capabilities, and includes comprehensive profile management features.

PayU UPI Bolt SDK simplifies the payment process by:

* Eliminating third-party redirection for higher success rates
* Offering profile management for user accounts and balances
* Reducing customer drop-offs and enhancing overall experience
* Providing direct bank integration for faster transaction completion

## Advantages

### Key Benefits

* **One-click payments** without third-party UPI app redirection
* **Faster transaction completion** through direct bank integration
* **Seamless in-app payment experience** for better user retention
* **Easy integration** leveraging pre-existing customer profiles with banks
* **5-6% increase in success rates** with better transaction conversion
* **Complete user funnel insights** for understanding user behavior

## User Journeys in PayU UPI Bolt

### Registration and Pay Journey

For first-time users, the registration process includes:

1. **User consent** for SMS permissions
2. **Device verification** using SIM and mobile number
3. **UPI ID creation** and bank selection
4. **MPIN setup** (if needed) for first-time users
5. **Transaction completion** using the added bank account

### Payment Journey

For registered customers:

* **One-click payments** with existing bank accounts
* **Balance checking** to ensure transaction readiness
* **MPIN verification** for secure payment processing

### Profile Management Journey

Users can manage their payment profiles by:

* **Managing bank accounts** (add, delete, set/change MPIN, balance checks)
* **Accessing transaction history** and dispute resolution
* **Deregistering accounts** from PayU UPI Bolt SDK

## Prerequisites

Before integrating PayU UPI Bolt SDK, ensure you have:

* **iOS deployment target**: iOS 17 or higher
* **Flutter SDK**: Latest stable version
* **PayU merchant account** with valid merchant key
* **Required permissions** for SMS and device access

## Integration Steps

### Step 1: Add SDK Dependency

Add the PayU UPI Bolt Flutter SDK to your project:

```bash
flutter pub add payu_upi_bolt_ui_flutter 1.0.0.alpha
```

### Step 2: Platform-Specific Setup

#### iOS Setup

1. **Add Framework Files**

   Include the following `.xcframework` files in your iOS project:

   * `CommonLibrary.xcframework` (NPCI)
   * `OlivePayLibrary.xcframework` (AXIS)

2. **Update Framework Search Path**

   In Xcode, update the Framework Search Path to:

   ```
   $(PROJECT_DIR)/Frameworks
   ```

#### Android Setup

1. **Add Dependencies**

   Add the following dependencies to your `build.gradle` file:

   ```gradle
   dependencies {
       implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.1-dev4'
       implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
   }
   ```

2. **Add AAR File**

   Place the `SecureComponent-release-prod_05062024_9d3904ab.aar` file in the `libs` folder of your Android app module.

### Step 3: Initialize SDK

Initialize the PayU UPI Bolt SDK with your configuration:

```dart
import 'package:payu_upi_bolt_ui_flutter/PayUUPIConstantKeys.dart';
import 'package:payu_upi_bolt_ui_flutter/payu_upi_bolt_ui_flutter.dart';

var config = {
  "merchantName": "<merchantName>",  // String
  "merchantKey": "<merchantKey>",   // String
  "phone": "<phone>",               // String
  "email": "<email>",               // String
  "refId": "<refId>",               // String
  "pluginTypes": ["<pluginType>"],  // Array<String>
  "clientId": "clientId",           // String
  "issuingBanks": ["<issuingBanks>"], // Array<String>
  "excludedBanksIINs": ["<excludedBanksIIN>"], // Array<String>
  "isProduction": <isProduction>   // Bool (true = Production, false = Staging)
};

// To initialize the SDK
var payUUpiFlutter = PayUUPIBoltUIFlutter(this);
payUUpiFlutter.initSDK(params: config);

// To clear the SDK Instance
payUUpiFlutter.reset();
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
        <code>Bool</code><br/>
        True (Production), false (Staging)
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

### Step 4: Check UPI Bolt Availability

Before proceeding with payment flows, verify if UPI Bolt is enabled:

```dart
void checkUPIBoltStatus() {
  payUUpiFlutter.isUPIBoltEnabled();
}
```

### Step 5: Implement Payment Flow

#### Register and Pay

For first-time users or new transactions:

```dart
// Payment Parameters
var paymentParams = {
  "amount": "<txn_amount>",          // Transaction Amount
  "txnId": "<transaction_id>",       // Transaction ID
  "productInfo": "<product_info>",   // Description of Product
  "firstName": "<first_name>",       // Customer First Name
  "surl": "<success_url>",           // Success Callback URL (Optional)
  "furl": "<failure_url>",           // Failure Callback URL (Optional)
  "additionalParam": {},             // (Optional) Additional Parameters
  "udf1": "<user_defined_field_1>",  // (Optional)
  "udf2": "<user_defined_field_2>",  // (Optional)
  "udf3": "<user_defined_field_3>",  // (Optional)
  "udf4": "<user_defined_field_4>",  // (Optional)
  "udf5": "<user_defined_field_5>",  // (Optional)
  "udf6": "<user_defined_field_6>"   // (Optional)
};

payUUpiFlutter.registerAndPay(params: paymentParams);
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
        udf1 to udf6<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>String</code><br/>
        User-defined fields
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        additionalParam<br/>
        <code>optional</code>
      </td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">
        <code>Object</code><br/>
        Additional Parameters
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

### Step 6: Profile Management

#### UPI Management Screens

Open various UPI management screens:

```dart
// Managing UPI Profiles
var params = {
  "screenType": "ALL" // Other options: "TRANSACTIONHISTORY", "MANAGEUPIACCOUNTS", "DISPUTE", "DEREGISTERUPI"
};

payUUpiFlutter.openUPIManagement(params: params);
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

### Step 7: Implement Callbacks

Implement the required callback methods:

```dart
// Listener Class:
class PayUListener implements PayUUPIBoltUiListener {
  @override
  void onPayUSuccess(Map response) {
    print("Transaction Successful: $response");
    // Handle successful payment
  }

  @override
  void onPayUFailure(Map response) {
    print("Transaction Failed: $response");
    // Handle payment failure
  }

  @override
  void onPayUCancel(Map response) {
    print("Transaction Cancelled: $response");
    // Handle payment cancellation
  }

  @override
  void onErrorReceived(Map response) {
    print("Error Received: $response");
    // Handle errors
  }

  @override
  void onUPIBoltEnabled(Map response) {
    print("UPI Bolt Enabled: $response");
  }

  @override
  void onReset(Map response) {
    print("SDK Reset Successful: $response");
  }

  @override
  void generateHash(Map response) {
    // SHA-512 Hash Generation Logic
    var hashValue = "<SHA-512-Hash>";  // Use backend/server to generate
    
    var hashResponse = {
      "hashName": response["hashName"], // Name of Hash
      "hash": hashValue
    };
    payUUpiFlutter.hashGenerated(params: hashResponse);
  }
}
```

**Callback Response Methods:**

1. **`onPayUSuccess(Map response)`**: Called if payment succeeds.
2. **`onPayUFailure(Map response)`**: Triggered on payment failure.
3. **`onPayUCancel(Map response)`**: Called when the transaction is cancelled.
4. **`onErrorReceived(Map response)`**: Invoked when an error occurs.
5. **`onUPIBoltEnabled(Map response)`**: Checks if UPI Bolt is enabled.
6. **`onReset(Map response)`**: Confirms SDK has been reset.
7. **`generateHash(Map response)`**: Invoked to compute required hash.

### Step 8: Hash Generation

Implement secure hash generation for transaction security:

```dart
@override
generateHash(Map response) {
  let commandName = response["PayUUPIBoltHashConstants.hashName"];
  let hashStringWithoutSalt = response["PayUUPIBoltHashConstants.hashString"];
  let postSalt = response["PayUUPIBoltHashConstants.postSalt"]; 

  let hashValue;  
  if (postSalt != null) {
    hashValue = "<SHA-512 Hash of (hashStringWithoutSalt + salt + postSalt)>";
  } else {
    hashValue = "<SHA-512 Hash of (hashStringWithoutSalt + salt)>";
  }

  var hashResponse = {"commandName": commandName, "hash": hashValue};
  payUUpiFlutter.hashGenerated(params: hashResponse);
}
```

<Callout icon="📘" theme="info">
  **Note**: Always generate hashes on your secure server. Never expose your salt values in client-side code.
</Callout>

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
      <td style="border: 1px solid #dee2e6; padding: 12px;">Failure/Invalid Response/Missing Params</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Request failed due to invalid or missing parameters</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>2</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">User Cancelled Transaction</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">User cancelled the transaction</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>100</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction Timeout</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Transaction exceeded time limit</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>103</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Handshake Failed</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Initial connection establishment failed</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>104</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">UPI Bolt Not Supported</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Feature not available for merchant</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dee2e6; padding: 12px;"><code>501</code></td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">No Internet Connection</td>
      <td style="border: 1px solid #dee2e6; padding: 12px;">Network connectivity issue</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

**Error Handling Example:**

```dart
@override
void onErrorReceived(Map response) {
  int errorCode = response["errorCode"] ?? -1;
  String errorMessage = response["errorMessage"] ?? "Unknown error";
  
  switch (errorCode) {
    case 100:
      // Handle timeout
      showTimeoutError();
      break;
    case 501:
      // Handle network issues
      showNetworkError();
      break;
    default:
      // Handle general errors
      showGeneralError(errorMessage);
  }
}
```