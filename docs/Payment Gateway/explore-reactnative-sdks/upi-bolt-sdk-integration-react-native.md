---
title: UPI Bolt SDK Integration - React Native
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU UPI Bolt SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs.

## Advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion.
6. Merchants can take advantage of a complete user funnel to understand user behavior.

## User Journeys in PayU UPI Bolt

### Registration and Pay

<Image align="center" alt="UPI Bolt React Native Custome Journey for Registration and Pay" border={false} src="https://files.readme.io/a2d41854641a44082dcb2bc0e38a3bea213ef7c25ca0ce9429d8c8221581ab75-upi_bolt_reactnative_customer_journey_register_pay.jpeg" />

1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

### Pay

<Image align="center" alt="UPI Bolt React Native Custome Journey for Pay" border={false} src="https://files.readme.io/fad794f25f0f6b108bc694ee13f79f7a3b5de220f6f90990409f7267e86446bb-upi_bolt_reactnative_customer_journey_pay.jpeg" />

1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

### Profile Management Journey

<Image align="center" alt="UPI Bolt React Native Custome Journey for Profile Management" border={false} src="https://files.readme.io/556315528c71a4e06f9cb9c4edb40fd651eef3c10b20a9418d569231877d98a7-upi_bolt_reactnative_customer_journey_profile_mgmt.jpeg" />

1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
3. Customers can see all the raised disputes from the Dispute history screen.
4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

## Steps to Integrate PayU Bolt SDK

### Prerequisites

SDK Compatibility: Ensure that the application's minimum development target is set to version 13 or higher.

### UI Bolt Integration

Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use PayU UPI Bolt UI SDK for customer registration, payment, and profile management.

### iOS Integration

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile.

**Supported iOS deployment target - iOS 17 and above.**

Add the following imports in the class where you need to initiate SDK:

```typescript
import PayUUPIBoltUiSdk from 'payu-upi-bolt-ui-rn';
```

Ensure that the application's minimum development target is set to version 13 or higher.

The following xcframework files will be provided by PayU during onboarding:

1. NPCI - CommonLibrary.xcframework
2. AXIS - OlivePayLibrary.xcframework

<Image align="center" border={false} src="https://files.readme.io/0b4b62bde986356a30777d54104c56e3e195a9b9d33a57f621f9d84be9b2dce4-upi_bolt_reactnative_ios_integration.jpeg" />

Add these framework in your project.

In Build Settings > Framework Search Path, add `$(PROJECT_DIR)/Frameworks` if it is not added automatically by Xcode.

Install the npm package:

```bash
npm install payu-upi-bolt-ui-rn --save
react-native link payu-upi-bolt-ui-rn
```

<Image align="center" border={false} src="https://files.readme.io/c9528432186e3c248c2598fc5121eb0d1fdd3acb109737141b6d437b583b5329-upi_bolt_reactnative_ios_integration2.jpeg" />

Also, add the following dependency to the podfile of your Xcode app if not exists:

```ruby
pod 'PayUIndia-UPIBoltCoreKit', '1.0.0-alpha.7'
```

### Android Integration

Add the following permissions in your AndroidManifest file:

```xml
<uses-permission android:name="android.permission.SEND_SMS"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

Add the following dependency in the build.gradle file of your android app module:

```gradle
implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.1-dev4'
implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
```

Add the given aar file in the libs folder of your android app module:

```
<your_project>/android/app/libs/SecureComponent-release-prod_05062024_9d3904ab.aar
```

## SDK Methods

### 1. init

It is used to initialize the SDK. This method returns an object that will be used to access other methods available in PayUUPIBoltUI.

#### Request

```javascript
// Function to create SDK configuration
createSDKConfig = () => {
  const requestId = 'payu_' + Math.random();

  const config = {
    merchantName: merchantName,
    merchantKey: key,
    phone: phone,
    email: email,
    requestId: requestId,
    pluginTypes: ["AXIS"],
    isProduction: true,
    excludedBanksIINs: [],
  };

  return config;
};

// Initialize the SDK
const initConfig = createSDKConfig();
PayUUPIBoltUISdk.initSDK(initConfig);

// To clear the SDK instance
PayUUPIBoltUISdk.reset(reactContext);
```

#### Request Parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">config<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Map</code> PayUUPIBoltBaseConfig includes the below fields.</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{...}</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">merchantName<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Merchant Name</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"MyStore Inc"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">merchantKey<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> PayU Merchant Key</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"gtKFFx"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">phone<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Phone number for registration</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"+919876543210"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">email<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Customer Email Id</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"customer@example.com"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">pluginTypes<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Array&lt;String&gt;</code> List of Supported Plugin (Values - AXIS or HDFC or BHIM)</td>
            <td style="border: 1px solid #ddd; padding: 8px;">["AXIS", "HDFC", "BHIM"]</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">isProduction<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Bool</code> Prod - true, staging - false</td>
            <td style="border: 1px solid #ddd; padding: 8px;">true</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">excludedBanksIINs<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Array&lt;String&gt;</code> List of Bank's IIN to exclude</td>
            <td style="border: 1px solid #ddd; padding: 8px;">["123456", "789012"]</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">clientId<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Unique client ID</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"CLIENT_001"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">refId<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Unique reference ID</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"REF_12345678"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">issuingBanks<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Array&lt;String&gt;</code> List of Issuing Bank's (Values - AXIS or HDFC)</td>
            <td style="border: 1px solid #ddd; padding: 8px;">["AXIS", "HDFC"]</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

#### Response

Refer to [Response Type](#response-type) table

### 2. isUPIBoltEnabled

This method is used to check whether the upi bolt is enabled for the merchant or not.

#### Request

```javascript
PayUUPIBoltUISdk.isUPIBoltSDKAvailable((response) => {
  if (response.isSDKAvailable === 'true') {
    console.log("SDK is available. Proceed with payment or other operations.");
  } else {
    console.log("UPI Bolt SDK is not available.");
  }
});
```

#### Response

Refer to [Response Type](#response-type) table

### 3. registerAndPay

This API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

#### Request

```javascript
const txnId = new Date().getTime().toString();

const paymentParams = {
  amount: "<amount>", // String
  productInfo: "<productInfo>", // String
  firstName: "<firstName>", // String
  surl: "<successUrl>", // String (Android success URL)
  furl: "<failureUrl>", // String (Android failure URL)
  ios_surl: "<iosSuccessUrl>", // String (iOS success URL)
  ios_furl: "<iosFailureUrl>", // String (iOS failure URL)
  initiationMode: "<initiationMode>", // String (e.g., "10")
  purpose: "<purpose>", // String (e.g., "00")
  udf1: "<udf1>", // String (Optional)
  udf2: "<udf2>", // String (Optional)
  udf3: "<udf3>", // String (Optional)
  udf4: "<udf4>", // String (Optional)
  udf5: "<udf5>", // String (Optional)
  txnId: "<txnId>", // String (Unique transaction ID)
  isCCTxnEnabled: <trueOrFalse> // Boolean (Enable card fallback if supported)
};

PayUUPIBoltUISdk.payURegisterAndPay(paymentParams);
```

#### Request Parameters

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        params  
        `mandatory`
      </td>

      <td>
        `map` Refer to Payment Params section
      </td>
    </tr>
  </tbody>
</Table>

#### Response

Refer to SDK Response JSON Format.

| Field  | Definition                                                        |
| ------ | ----------------------------------------------------------------- |
| result | Payment Response. Refer to [Response Type](#response-type)  table |

### 4. openUPIManagement

This API allows you to manage UPI accounts and transaction history.

#### Request

```javascript
// Screen Types
const screenType = <screenType> // String

// Values
"ALL" or "TRANSACTIONHISTORY" or "MANAGEUPIACCOUNTS" or "DISPUTE" or "DEREGISTERUPI"

PayUUPIBoltUISdk.openUPIManagement(screenType);
```

#### Request Parameters

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        screenType  
        `mandatory`
      </td>

      <td>
        `String` To enforce the management screen
      </td>
    </tr>
  </tbody>
</Table>

#### Response

Refer to [Response Type](#response-type) table

## PayUPaymentParams

The following fields are needed as a request:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">amount<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Txn Amount</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"100.00"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">txnId<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Txn Id</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"TXN_123456789"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">productInfo<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Product Info</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Product Purchase"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">firstName<br><code>mandatory</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> First Name</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"John"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">surl<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Success URL</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"https://example.com/success"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">furl<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>String</code> Failure URL</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"https://example.com/failure"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">additionalParam<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Map</code> Additional params if any</td>
            <td style="border: 1px solid #ddd; padding: 8px;">{"param1": "value1"}</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf1<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields1</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 1"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf2<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields2</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 2"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf3<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields3</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 3"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf4<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields4</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 4"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf5<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields5</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 5"</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">udf6<br><code>optional</code></td>
            <td style="border: 1px solid #ddd; padding: 8px;"><code>Any</code> User Defined Fields6</td>
            <td style="border: 1px solid #ddd; padding: 8px;">"Custom Value 6"</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

## Listener/Callback Logic

The listener/callback contains following methods where the merchant app will get the API response and hash-related callbacks.

#### Request

```javascript
// Register event emitters
useEffect(() => {
  const eventEmitter = new NativeEventEmitter(PayUBizSdk);

  onPayUSuccessListener = eventEmitter.addListener('onPayUSuccess', onPayUSuccess);
  onPayUFailureListener = eventEmitter.addListener('onPayUFailure', onPayUFailure);
  onPayUCancelListener = eventEmitter.addListener('onPayUCancel', onPayUCancel);
  payUGenerateHashListener = eventEmitter.addListener('generateHash', generateHash);
  permissionListener = eventEmitter.addListener('permissionCallback', permissionCallback);

  // Clean up listeners on unmount or merchantSalt change
  return () => {
    console.log("Unsubscribed!");
    onPayUSuccessListener.remove();
    onPayUFailureListener.remove();
    onPayUCancelListener.remove();
    payUGenerateHashListener.remove();
    permissionListener.remove();
  };
}, [merchantSalt]);

// Handler: PayU success
onPayUSuccess = (response) => {
  displayAlert('onPayUSuccess', JSON.stringify(response));
};

// Handler: PayU failure
onPayUFailure = (response) => {
  displayAlert('onPayUFailure', JSON.stringify(response));
};

// Handler: PayU cancel
onPayUCancel = (response) => {
  displayAlert('onPayUCancel', JSON.stringify(response));
};

// Handler: Generate hash event
generateHash = (e) => {
  handleHashGeneration(e.hashName, e.hashString + merchantSalt);
};
```

#### Response

Refer to SDK Response JSON Format.

## Hash Generation Logic

The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUUPIBoltUiListener. The generateHash() method is called by the SDK each time it needs an individual hash.

#### Request

```javascript
function handleHashGeneration(hashName, hashString) {  
  // Merchant will get Map/ JSON with type of hash and hash string as value of dictionary.
  /*
  They have to sign that string using salt to create hash value and pass that to onCompletion
  In the map you have to check for three keys to generate hash.
  1. hashString
  2. hashName
  3. postSalt
  
  At the end of that hashString append your salt and use SHA-512 algo on that final string to generate hash.
  Note: If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algo on that final string to generate hash.
  Once the hash is generated use hashGenerationListener parameter to pass the hash to SDK. Example code:
  */

  // get hash for "commandName" from server
  // get hash for "hashString" from server

  var hash = <fetch_hash_from_server>;

  // After fetching hash set its value in below variable "hashMap"

  const result = { hashName: hashName, [hashName]: hashValue };
  PayUBizSdk.hashGenerated(result);
}
```

#### Response

Refer to SDK Response JSON Format.

| Field        | Definition                                               |
| ------------ | -------------------------------------------------------- |
| result       | Contains response model if received success callback     |
| code         | `Integer` Status code                                    |
| message      | `String` Message                                         |
| responseType | `Integer` Refer to [Response Type](#response-type) table |

## Response type

| Response Code | Message                                |
| ------------- | -------------------------------------- |
| 0             | Success                                |
| 1             | Fail/ Invalid Response/ Missing params |
| 2             | User cancelled the transaction         |
| 100           | Transaction timeout                    |
| 103           | Handshake failed                       |
| 104           | UPI bolt not supported                 |
| 105           | Device not supported for UPI Bolt      |
| 500           | Something went wrong                   |
| 501           | No internet connection                 |
| 502           | SDK not found                          |

### Response Type

| Response Type       | Response Code | Definition       |
| ------------------- | ------------- | ---------------- |
| REQUEST_UPI_BOLT    | 100           | UPI Bolt Status  |
| REQUEST_TRANSACTION | 124           | Register And Pay |
| REQUEST_MANAGE      | 125           | UPI Management   |

## SMS Hash Generation for Android OTP Auto-read

Copy AppSignatureHelper class given below in your project.

```java
package com.payu.upipluginsampleapp;

import android.content.Context;
import android.content.ContextWrapper;
import android.content.pm.PackageManager;
import android.content.pm.Signature;
import android.util.Base64;
import android.util.Log;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * This is a helper class to generate your message hash to be included in your SMS message.
 *
 * Without the correct hash, your app won't recieve the message callback. This only needs to
 * be generated once per app and stored. Then you can remove this helper class from your code.
 */
public class AppSignatureHelper extends ContextWrapper {
  public static final String TAG = AppSignatureHelper.class.getSimpleName();

  private static final String HASH_TYPE = "SHA-256";
  public static final int NUM_HASHED_BYTES = 9;
  public static final int NUM_BASE64_CHAR = 11;

  public AppSignatureHelper(Context context) {
    super(context);
  }

  /**
   * Get all the app signatures for the current package
   * @return
   */
  public ArrayList<String> getAppSignatures() {
    ArrayList<String> appCodes = new ArrayList<>();

    try {
      // Get all package signatures for the current package
      String packageName = getPackageName();
      PackageManager packageManager = getPackageManager();
      Signature[] signatures = packageManager.getPackageInfo(packageName,
          PackageManager.GET_SIGNATURES).signatures;

      // For each signature create a compatible hash
      for (Signature signature : signatures) {
        String hash = hash(packageName, signature.toCharsString());
        if (hash != null) {
          appCodes.add(String.format("%s", hash));
        }
      }
    } catch (PackageManager.NameNotFoundException e) {
      Log.e(TAG, "Unable to find package to obtain hash.", e);
    }
    return appCodes;
  }

  private static String hash(String packageName, String signature) {
    String appInfo = packageName + " " + signature;
    try {
      MessageDigest messageDigest = MessageDigest.getInstance(HASH_TYPE);
      messageDigest.update(appInfo.getBytes(StandardCharsets.UTF_8));
      byte[] hashSignature = messageDigest.digest();

      // truncated into NUM_HASHED_BYTES
      hashSignature = Arrays.copyOfRange(hashSignature, 0, NUM_HASHED_BYTES);
      // encode into Base64
      String base64Hash = Base64.encodeToString(hashSignature, Base64.NO_PADDING | Base64.NO_WRAP);
      base64Hash = base64Hash.substring(0, NUM_BASE64_CHAR);

      Log.d(TAG, String.format("pkg: %s -- hash: %s", packageName, base64Hash));
      return base64Hash;
    } catch (NoSuchAlgorithmException e) {
      Log.e(TAG, "hash:NoSuchAlgorithm", e);
    }
    return null;
  }
}
```

To get the hash value, log the value generated by following statement:

```java
Log.d("appSignature", AppSignatureHelper(requireContext()).appSignatures[0]);
```

Share the value to PayU team for configuring SMS hash at BE.
