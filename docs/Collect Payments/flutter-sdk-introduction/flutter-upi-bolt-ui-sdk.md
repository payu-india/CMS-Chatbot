---
title: Flutter UPI Bolt UI SDK
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Flutter UPI Bolt UI SDK
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU UPI Bolt UI SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs.

## Advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion.
6. Merchants can take advantage of a complete user funnel to understand user behavior.

## User Journeys in PayU UPI Bolt UI SDK

<Accordion title="Registration and Pay" icon="fa-folder" id="registration-and-pay">
  1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
  2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
  3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
  4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
  5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

  <Image align="center" src="https://files.readme.io/477aa57e491d8be306be606858728a809e562aed4a65bef8663d03703a82d98f-0.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Pay Flow" />
</Accordion>

<Accordion title="Pay" icon="fa-folder" id="pay">
  1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
  2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
  3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

  <Image align="center" src="https://files.readme.io/b3050b0d3581a62b29ddccb4d183cf14f0251e6cbd033cea8916eae364209586-1.jpg" alt="Flutter UPI Bolt UI SDK Integration Pay Flow" />
</Accordion>

<Accordion title="Profile Management Journey" icon="fa-folder" id="profile-management">
  1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
  2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
  3. Customers can see all the raised disputes from the Dispute history screen.
  4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

  <Image align="center" src="https://files.readme.io/f6649179d1e3193799da08174d44e0d4a021da5b3bcfbf62b6c7863d13fd26ed-2.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Profile Management Flow" />
</Accordion>

## Steps to Integrate

<Accordion title="Prerequisites" icon="folder" id="prerequisites">
  <Callout icon="🚧" theme="warn">
    Supported iOS deployment target - iOS 17 and above.
  </Callout>

  Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use PayU UPI Bolt UI SDK for customer registration, payment, and profile management.

  <br />

  To include the PayU UPI Bolt UI SDK in your project, add the following dependency to your pubspec.yaml file:

  ```Text
  payu_upi_bolt_ui_flutter: 1.1.0
  ```

  Install the Flutter package:

  ```bash
  flutter pub add payu_upi_bolt_ui_flutter:^1.1.0
  ```

  <Accordion title="iOS Integration" icon="folder" id="ios-integration">
    To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile.

    **Supported iOS deployment target - iOS 17 and above.**

    <br />

    The following xcframework files will be provided by PayU during onboarding:

    1. **NPCI** - CommonLibrary.xcframework
    2. **AXIS** - OlivePayLibrary.xcframework

    Add the above frameworks in your project. The added framework is similar to the following screenshot:

    <br />

    <Image align="center" src="https://files.readme.io/ab49c1c2aad9cb456436a7bf17437ea1797620f6bb650deb37f4a798c1328419-3.png" alt="NPCI - CommonLibrary.xcframework and AXIS - OlivePayLibrary.xcframework added to project" />

    <br />

    In Build Settings > Framework Search Path, add `$(PROJECT_DIR)/Frameworks` if it is not added automatically by Xcode.

    <br />

    <Image align="center" src="https://files.readme.io/dfbfe5bb1b9bd93ea6c30e191556643e8a0e870550a40f46225ea071e4eaab0c-4.png" alt="Flutter UPI Bolt UI SDK Integration PROJECT_DIR config" />

    <br />
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

<Accordion title="Step 1: Initialization" icon="folder" id="step-1-initialization">
  It is used to initialize the SDK. This method returns an object that will be used to access other methods available in PayUUPIBoltUI.

  <h5> Add the following imports:</h5>

  ```dart
  import 'package:payu_upi_bolt_ui_flutter/PayUUPIConstantKeys.dart';
  import 'package:payu_upi_bolt_ui_flutter/payu_upi_bolt_ui_flutter.dart';
  ```

  Initialize the SDK with configuration:

  ```dart
  var config = {
    "merchantName": "<merchantName>", // String
    "merchantKey": "<merchantKey>", // String
    "phone": "<phone>", // String
    "email": "<email>", // String
    "refId": "<refId>", // String
    "pluginTypes": ["<pluginType>"], // Array \<String>
    "clientId": "<clientId>", // String
    "issuingBanks": ["<issuingBanks>"], // Array \<String>
    "excludedBanksIINs": ["<excludedBanksIIN>"], // Array \<String>
    "isProduction": <isProduction> // Boolean
  };

  // To initialize the SDK
  var payUUpiFlutter = PayUUPIBoltUIFlutter(this);
  payUUpiFlutter.initSDK(params: config);

  // To clear the SDK Instance
  payUUpiFlutter.reset();
  ```

  <h5> The following fields are needed as a request for this API: </h5>

  <br />

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>config<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Map</code> PayUUPIBoltBaseConfig includes the below fields.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>{...}</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantName<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant Name</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"MyStore Inc"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantKey<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> PayU Merchant Key</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"gtKFFx"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Phone number for registration</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"+919876543210"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer Email Id</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"customer@example.com"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pluginTypes<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array&lt;String&gt;</code> List of Supported Plugin (Values - AXIS or HDFC or BHIM)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>["AXIS", "HDFC", "BHIM"]</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>isProduction<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Prod - true, staging - false</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>excludedBanksIINs<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array&lt;String&gt;</code> List of Bank's IIN to exclude</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>["123456", "789012"]</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>clientId<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique client ID</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"CLIENT_001"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>refId<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique reference ID</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"REF_12345678"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>issuingBanks<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array&lt;String&gt;</code> List of Issuing Bank's (Values - AXIS or HDFC)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>["AXIS", "HDFC"]</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Clear SDK Cache of PayUBolt SDK" icon="folder" id="clear-sdk-cache">
  The `clearCache` method is used to clear the cache corresponding to the passed PG value.

  <br />

  ```dart
  payUUpiFlutter.clearCache(params: Map);
  ```

  **The following fields are needed as a request for this API:**

  <br />

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pg<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> PG value to clear PG-specific data</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  <br />

  **Response:** [Refer to SDK Response JSON Format](#sdk-response-json-format)

  <br />
</Accordion>

<Accordion title="Check Plugin Registration Status of PayUBolt SDK" icon="folder" id="check-registration-status">
  The `isRegistered` method is used to check pg registration status.

  <br />

  ```dart
  payUUpiFlutter.isRegistered(params: Map);
  ```

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pg<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> PG value to check PG-specific registration status</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  <br />

  **Response:** [Refer to SDK Response JSON Format](#sdk-response-json-format)

  **Callback:** The callback will have the below response format.

  <br />
</Accordion>

<Accordion title="Step 2. Check if UPI Bolt is Enabled" icon="folder" id="step-2-check-enabled">
  This method is used to check whether the upi bolt is enabled for the merchant or not.

  <br />

  ```dart
  payUUpiFlutter.isUPIBoltEnabled();
  ```

  <br />

  **Response:** [Refer to SDK Response JSON Format](#sdk-response-json-format)

  <br />

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> Status code (Success = 0, Failure = 1)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Message</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  <br />
</Accordion>

<Accordion title="Step 3. Register and Pay" icon="folder" id="step-3-register-and-pay">
  This API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

  <br />

  **Payment Parameters**

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction amount.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>productInfo<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Information about the product or service.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>firstName<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer's first name.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Android success URL.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Android failure URL.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>ios_surl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> iOS success URL.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>ios_furl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> iOS failure URL.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>initiationMode<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Mode of initiation (e.g., "10").</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>purpose<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Purpose code (e.g., "00").</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique transaction ID.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1 - udf6<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Any</code> User-defined fields for additional transaction metadata.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>isCCTxnEnabled<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Enables card fallback if supported – true or false.</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  <br />

  **Sample Code**

  ```dart
  var params = {
  "amount": <amount>, // String
  "productInfo": <productInfo>, // String
  "firstName": <firstName>, // String
  "surl": <success_url>, // String (Android success URL)
  "furl": <failure_url>, // String (Android failure URL)
  "udf1": <udf1>,   // String (Optional)
  "udf2": <udf2>,   // String (Optional)
  "udf3": <udf3>,   // String (Optional)
  "udf4": <udf4>,   // String (Optional)
  "udf5": <udf5>,   // String (Optional)
  "txnId": <txnId>, // String (Unique transaction ID)
  "isCCTxnEnabled": <isCCTxnEnabled>, // Boolean (Enable card fallback if supported)
  "ios_surl": <ios_success_url>, // String (iOS success URL)
  "ios_furl": <ios_failure_url>, // String (iOS failure URL)
  "initiationMode": <initiationMode>,
  "purpose": <purpose>,
  // Optional for TPV txns
  "beneficiaryDetails": [ 
    {
      "accountNumber": <beneficiary1_accountNumber>,
      "ifsc": <beneficiary1_ifsc>
    },
    {
      "accountNumber": <beneficiary2_accountNumber>,
      "ifsc": <beneficiary2_ifsc>
    }
  ]
  }

  payUUpiFlutter.registerAndPay(params: Map);
  ```

  <br />

  **Response:** `Map` [Refer to SDK Response JSON Format](#sdk-response-json-format).

  <br />

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Payment Response</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  <br />
</Accordion>

<Accordion title="Step 4. Open UPI Management" icon="folder" id="step-4-upi-management">
  This API allows you to manage UPI accounts and transaction history.

  ```dart
  // Screen Types
  var params = {
  screenType: <String> 
  }

  payUUpiFlutter.openUPIManagement(params: Map);
  ```

  **Request Parameters**

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>screenType<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;">
        <p><code>String</code> Specifies the type of management screen. Valid values:</p>
        <p>• ALL</p>
        <p>• TRANSACTIONHISTORY</p>
        <p>• MANAGEUPIACCOUNTS</p>
        <p>• DISPUTE</p>
        <p>• DEREGISTERUPI</p>
      </td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

  **Response:** `Map` [Refer to SDK Response JSON Format](#sdk-response-json-format)
</Accordion>

<Accordion title="Step 5. Listener/Callback logic" icon="folder" id="step-6-listener-callback">
  The listener/callback contains following methods where the merchant app will get the API response and hash-related callbacks.

  ```dart
  @override
  void onPayUSuccess(Map response) {
  // Contains the success response after a completed payment
  }

  @override
  void onPayUFailure(Map response) {
  // Contains the failure response if the payment fails
  }

  @override
  void onPayUCancel(Map response) {
  // Called when the user cancels the payment
  }

  @override
  void onErrorReceived(Map response) {
  // Called when any SDK or transaction error occurs
  }

  @override
  void onUPIBoltEnabled(Map response) {
  // Indicates whether UPI Bolt is enabled for the merchant
  }

  @override
  void onReset(Map response) {
  // Called when the SDK instance is reset successfully
  }

  @override
  void onIsRegistered(Map response) {
  // Returns the registration status with the selected plugin
  }

  @override
  void onInitSDK(Map response) {
  // Called after SDK initialization (success or failure)
  }

  @override
  void generateHash(Map response) {
  // Triggered when the SDK requests hash generation
  // Refer to the Hash Generation section for implementation details
  }
         
  ```
</Accordion>

<Accordion title="Step 6. Hash Generation Logic" icon="folder" id="step-7-hash-generation">
  The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

  For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUUPIBoltUiListener.  The generateHash() method is called by the SDK each time it needs an individual hash.

  ```dart
  @override 
  void generateHash(Map response) {
    // Merchant will get Map with type of hash and hash string as value of dictionary.
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
    
    let commandName = (param[PayUUPIBoltHashConstants.hashName] ?? "");
    let hashStringWithoutSalt = (param[PayUUPIBoltHashConstants.hashString] ?? "");
    let postSalt = param[PayUUPIBoltHashConstants.postSalt];
    
    // get hash for "commandName" from server
    // get hash for "hashStringWithoutSalt" from server
    
    // After fetching hash set its value in below variable "hashValue"
    var hashValue = "";
    if let postSalt = postSalt {
      let hashString = hashStringWithoutSalt + salt + postSalt;
      hashValue = "<SHA-512 hash of hashString>";
    } else {
      hashValue = "<SHA-512 hash of hashString>";
    }
    
    var hashResponse = {commandName: hashValue};
    payUUpiFlutter.hashGenerated(params: hashResponse);
  }
  ```
</Accordion>

## SDK Response JSON Format

| Field   | Definition                                                                      |
| :------ | :------------------------------------------------------------------------------ |
| result  | Contains response model if received success callback                            |
| code    | [Ref. Response Codes and Messages section](#error-codes-and-error-message-list) |
| message | [Ref. Response Codes and Messages section](#error-codes-and-error-message-list) |

## Error Codes and Error Message List

| Response Code | Message                                |
| :------------ | :------------------------------------- |
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

<br />
