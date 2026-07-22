---
title: UPI Bolt UI SDK Integration -Capacitor-Ionic
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use PayU UPI Bolt UI SDK for customer registration, payment, and profile management.

## Steps to Integrate PayU Bolt SDK

<Accordion title="Prerequisites" icon="folder" id="prerequisites">
  <Callout icon="🚧" theme="warn">
    Supported iOS deployment target - iOS 17 and above.
  </Callout>

  <br />

  To include the PayU UPI Bolt UI SDK in your project, add the following dependency to your package.json file:

  **UAT:**

  ```
  npm add payu-upi-bolt-ui-capacitor@0.0.1-alpha.4
  ```

  **PRODUCTION:**

  ```
  npm add payu-upi-bolt-ui-capacitor@0.0.1
  ```

  Ensure that the application's minimum development target is set to version 13 or higher.

  <Accordion title="iOS Integration" icon="folder" id="ios-integration">
    To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile.

    **Supported iOS deployment target - iOS 17 and above.**

    <br />

    The following xcframework files will be provided by PayU during onboarding:

    1. **NPCI** - CommonLibrary.xcframework
    2. **AXIS** - OlivePayLibrary.xcframework

    Add these framework in your project. The added framework is similar to the following screeshot:

    <br />

    <Image align="center" src="https://files.readme.io/ab49c1c2aad9cb456436a7bf17437ea1797620f6bb650deb37f4a798c1328419-3.png" alt="NPCI - CommonLibrary.xcframework and AXIS - OlivePayLibrary.xcframework added to project" />

    <br />

    In Build Settings > Framework Search Path, add `$(PROJECT_DIR)/Frameworks` if it is not added automatically by Xcode.

    <br />

    <Image align="center" src="https://files.readme.io/dfbfe5bb1b9bd93ea6c30e191556643e8a0e870550a40f46225ea071e4eaab0c-4.png" alt="Flutter UPI Bolt UI SDK Integration PROJECT_DIR config" />

    <br />

    Also, add the following dependency to the podfile of your Xcode app if not exists.

    **UAT:**

    ```
    pod 'PayUIndia-UPIBoltCoreKit', '3.0.0-alpha.1'
    ```

    **PRODUCTION:**

    ```
    pod 'PayUIndia-UPIBoltCoreKit', '1.1.0'
    ```
  </Accordion>

  <br />

  <Accordion title="Android Integration" icon="folder" id="android-integration">
    Add the following permissions in your AndroidManifest file.

    ```manifest.xml
    <uses-permission android:name="android.permission.SEND_SMS"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    ```

    **UAT:**

    ```
    implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.6-SNAPSHOT'
    ```

    **Project-level build.gradle :**

    ```
    allprojects {
     repositories {
            maven {url "https://central.sonatype.com/repository/maven-snapshots/"}
       }
    }
    ```

    **PRODUCTION:**

    ```
    implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.5’
    ```

    Add the following dependency in the build.gradle file of your android app module:

    ```gradle
    implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
    ```

    Add the given aar file in the libs folder of your android app module:

    ```
    <your_project>/android/app/libs/SecureComponent-release-prod_05062024_9d3904ab.aar
    ```
  </Accordion>

  <br />
</Accordion>

<Accordion title="Step 1: Initialize SDK" icon="fa-code">
  **Import the Plugin**

  ```javascript
  import { PayUUPIBoltUICapacitorPlugin } from 'payu-upi-bolt-ui-capacitor';
  ```

  **Configuration Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        merchantName<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Merchant's name.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        merchantKey<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Merchant key provided by PayU.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        phone<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Customer's phone number for registration.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        email<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Customer email address.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        refId<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Unique reference ID for tracking the transaction.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        pluginTypes<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>Array&lt;String&gt;</code><br/>
                        Supported plugin types (e.g., AXIS, HDFC, BHIM).
                      </td>
                    </tr>
                    <tr>
                      <td>
                        clientId<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Unique client ID.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        issuingBanks<br/>
                        <code>optional</code>
                      </td>
                      <td>
                        <code>Array&lt;String&gt;</code><br/>
                        List of issuing banks supported (e.g., AXIS or HDFC).
                      </td>
                    </tr>
                    <tr>
                      <td>
                        excludedBanksIINs<br/>
                        <code>optional</code>
                      </td>
                      <td>
                        <code>Array&lt;String&gt;</code><br/>
                        List of banks to exclude using IIN values.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        isProduction<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>Boolean</code><br/>
                        Environment configuration: true for production, false for staging.
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>

  **Sample Code**

  ```javascript
  const config = {
    merchantName: "<merchantName>",
    merchantKey: "<merchantKey>",
    phone: "<phone>",
    email: "<email>",
    refId: "<refId>",
    pluginTypes: ["<pluginType>"],
    clientId: "<clientId>",
    issuingBanks: ["<issuingBanks>"],
    excludedBanksIINs: ["<excludedBanksIIN>"],
    isProduction: <isProduction>,
  };

  // Initialize the SDK
  PayUUPIBoltUICapacitorPlugin.initSDK({ config: JSON.stringify(config) });

  // Clear SDK Instance
  PayUUPIBoltUICapacitorPlugin.reset();
  ```
</Accordion>

<Accordion title="Step 2: Clear SDK Cache" icon="fa-code">
  ```javascript
  PayUUPIBoltUICapacitorPlugin.clearCache({ pg: "<pg>" });
  ```

  **Request Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        pg<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        PG value to check pg specific registration status
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Plugin Registration Status" icon="fa-code">
  ```javascript
  PayUUPIBoltUICapacitorPlugin.isRegistered({ pg: "<pg>" });
  ```

  **Request Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        pg<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        PG value to check pg specific registration status
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 3:isUPIBoltEnabled" icon="fa-code">
  This method is used to check whether the upi bolt is enabled for the merchant or not.

  ```javascript
  PayUUPIBoltUICapacitorPlugin.isUPIBoltEnabled();
  ```
</Accordion>

<Accordion title="Step 4: Register and Pay" icon="fa-code">
  **Payment Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        amount<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Transaction amount.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        productInfo<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Information about the product or service.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        firstName<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Customer's first name.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        surl<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Android success URL.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        furl<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Android failure URL.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        ios_surl<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        iOS success URL.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        ios_furl<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        iOS failure URL.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        initiationMode<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Mode of initiation (e.g., "10").
                      </td>
                    </tr>
                    <tr>
                      <td>
                        purpose<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Purpose code (e.g., "00").
                      </td>
                    </tr>
                    <tr>
                      <td>
                        txnId<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Unique transaction ID.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        udf1 - udf6<br/>
                        <code>optional</code>
                      </td>
                      <td>
                        <code>Any</code><br/>
                        User-defined fields for additional transaction metadata.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        isCCTxnEnabled<br/>
                        <code>optional</code>
                      </td>
                      <td>
                        <code>Boolean</code><br/>
                        Enables card fallback if supported – true or false.
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>

  **Sample Code**

  ```javascript
  const paymentParams = {
    amount: "<amount>",
    productInfo: "<productInfo>",
    firstName: "<firstName>",
    surl: "<successUrl>",
    furl: "<failureUrl>",
    ios_surl: "<iosSuccessUrl>",
    ios_furl: "<iosFailureUrl>",
    initiationMode: "<initiationMode>",
    purpose: "<purpose>",
    txnId: "<txnId>",
    isCCTxnEnabled: <trueOrFalse>,
  };

  PayUUPIBoltUICapacitorPlugin.registerAndPay({ paymentParams: JSON.stringify(paymentParams)});
  ```
</Accordion>

<Accordion title="Step 5: UPI Management" icon="fa-code">
  ```javascript
  PayUUPIBoltUICapacitorPlugin.openUPIManagement({ screenType: "<screenType>" });
  ```

  **Request Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        screenType<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Specifies the type of management screen. Valid values:<br/>
                        • ALL<br/>
                        • TRANSACTIONHISTORY<br/>
                        • MANAGEUPIACCOUNTS<br/>
                        • DISPUTE<br/>
                        • DEREGISTERUPI
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 6 : Listener Implementation" icon="fa-code">
  The listener/callback contains following methods where the merchant app will get the API response and hash-related callbacks.

  **Setup Event Listeners**

  ```javascript
  useEffect(() => {
  // List of listener registrations
  const listeners: { remove: () => void }[] = [];

  // Helper to register and store listeners
  const addListener = (eventName: string, handler: (data: any) => void) => {
    const listener = Plugins.PayUUPIBoltUICapacitorPlugin.addListener(eventName, handler);
    listeners.push(listener);
  };

  // Event: generateHash - handled separately
  addListener('generateHash', handleHashGeneration);

  // Common handler for other events - just alert JSON response
  const alertHandler = (data: any) => {
    presentAlert(JSON.stringify(data));
  };

  // Register all event listeners using the shared alert handler
  addListener('onPayUSuccess', alertHandler);
  addListener('onPayUCancel', alertHandler);
  addListener('onPayUFailure', alertHandler);
  addListener('reset', alertHandler);
  addListener('clearCache', alertHandler);
  addListener('isRegistered', alertHandler);
  addListener('isUPIBoltEnabled', alertHandler);

  // Cleanup all listeners on component unmount
  return () => {
    listeners.forEach(listener => listener.remove());
  };
  }, []);
  ```
</Accordion>

<Accordion title="Step 7: Hash Generation" icon="fa-code">
  The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

  For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUUPIBoltUiListener.  The generateHash() method is called by the SDK each time it needs an individual hash.

  **Hash Parameters**

  <HTMLBlock>{`
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        hashString<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        String to be signed dynamically.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        hashName<br/>
                        <code>mandatory</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Indicates the type of hash.
                      </td>
                    </tr>
                    <tr>
                      <td>
                        postSalt<br/>
                        <code>optional</code>
                      </td>
                      <td>
                        <code>String</code><br/>
                        Additional salt that can be appended to the hash if provided.
                      </td>
                    </tr>
                  </tbody>
                </table>
  `}</HTMLBlock>

  **Sample Code**

  ```javascript
  const handleHashGeneration = async (map) => {
    const hashData = map.hashString;
    const hashName = map.hashName;
    // Fetch hash from your server
    const hash = <fetch_hash_from_server>;
    const hashMap = {
      hashName: hashName,
      [hashName]: hash
    };
    PayUUPIBoltUICapacitorPlugin.hashGenerated({ hashData: JSON.stringify(hashMap) });
  };
  ```
</Accordion>

## Error Codes and Messages

**Response Codes**

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Code</th>
      <th>Message</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Success</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Fail / Invalid Response / Missing params</td>
    </tr>
    <tr>
      <td>2</td>
      <td>User cancelled the transaction</td>
    </tr>
    <tr>
      <td>100</td>
      <td>Transaction timeout</td>
    </tr>
    <tr>
      <td>103</td>
      <td>Handshake failed</td>
    </tr>
    <tr>
      <td>104</td>
      <td>UPI bolt not supported</td>
    </tr>
    <tr>
      <td>105</td>
      <td>Device not supported for UPI Bolt</td>
    </tr>
    <tr>
      <td>500</td>
      <td>Something went wrong</td>
    </tr>
    <tr>
      <td>501</td>
      <td>No internet connection</td>
    </tr>
    <tr>
      <td>502</td>
      <td>SDK not found</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## SMS Hash Generation for Android OTP Auto-Read

To enable OTP auto-read functionality on Android, you need to generate an SMS hash for your application. Copy the following `AppSignatureHelper` class to your Android project:

<Accordion title="Sample Code to Enable OTP auto-read functionality on Android" icon="fa-code">
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
       * @return ArrayList of app signatures
       */
      public ArrayList<String> getAppSignatures() {
          ArrayList<String> appCodes = new ArrayList<>();
          
          try {
              String packageName = getPackageName();
              PackageManager packageManager = getPackageManager();
              Signature[] signatures = packageManager.getPackageInfo(packageName, 
                      PackageManager.GET_SIGNATURES).signatures;
              
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

  **Usage Example**

  ```java
  // In your Android activity or application class
  AppSignatureHelper appSignatureHelper = new AppSignatureHelper(this);
  ArrayList<String> appSignatures = appSignatureHelper.getAppSignatures();

  // Share the generated hash with PayU for configuration
  for (String signature : appSignatures) {
      Log.d("SMS_HASH", "App Signature: " + signature);
  }
  ```

  <Callout icon="📘" theme="info">
    **Note**: Share the generated SMS hash with PayU team for configuration to enable OTP auto-read functionality.
  </Callout>
</Accordion>
