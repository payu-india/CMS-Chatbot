---
title: Cordova UPI Bolt UI SDK
deprecated: false
hidden: false
metadata:
  robots: index
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
  cordova plugin add payu-upi-bolt-ui-cordova@0.0.1-alpha.14
  ```

  **PRODUCTION:**

  ```
  cordova plugin add payu-upi-bolt-ui-cordova@0.0.3
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

<Accordion title="Step 1: Initialization" icon="folder" id="step-1-initialization">
  It is used to initialize the SDK. This method returns an object that will be used to access other methods available in PayUUPIBoltUI.

  Initialize the SDK with configuration:

  ```Cordova
    const config = {
              merchantName: "<merchantName>", // String
              merchantKey: "<merchantKey>" // String,
              phone: "<phone>", // String
              email: "<email>", // String
              refId: "<refId>", // String
              pluginTypes: ["<pluginType>"], // Array<String>
              clientId: [<clientId>], // String
              issuingBanks: ["<issuingBanks>"], // Array<String>
              excludedBanksIINs: ["<excludedBanksIIN>"], // Array<String>
              isProduction: <isProduction> // Bool
             };

  // To initialize the SDK
  cordova.plugins.PayUUpiBoltUiCordova.initSDK(this.responseCallBack, config);

  // To clear the SDK Instance
  cordova.plugins.PayUUpiBoltUiCordova.reset(this.responseCallBack);

  ```

  <h5> The following fields are needed as a request for this API: </h5>

  <br />

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
                                                                                                                                                                                                                                    <td style="border: 1px solid #ddd; padding: 8px;"><code>Boolean</code> Prod - true, staging - false</td>
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
</Accordion>

<Accordion title="Clear SDK Cache of PayUBolt SDK" icon="folder" id="clear-sdk-cache">
  The `clearCache` method is used to clear the cache corresponding to the passed PG value.

  <br />

  ```Cordova
  PayUUpiBoltUiCordova.clearCache(this.responseCallBack, pg);
  ```

  **The following fields are needed as a request for this API:**

  <br />

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
          pg
          `mandatory`
        </td>

        <td>
          `String` PG value to check clear pg specific data
        </td>
      </tr>
    </tbody>
  </Table>

  <br />

  <br />

  **Response**: \`[Refer to SDK Response JSON Format](#sdk-response-json-format)

  <br />
</Accordion>

<Accordion title="Check Plugin Registration Status of PayUBolt SDK" icon="folder" id="check-registration-status">
  The `isRegistered` method is used to check pg registration status.

  <br />

  ```Cordova
  cordova.plugins.PayUUpiBoltUiCordova.isRegistered(this.responseCallBack, pg);
  ```

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
          pg
          `mandatory`
        </td>

        <td>
          `String` PG value to check pg specific registration status
        </td>
      </tr>
    </tbody>
  </Table>

  <br />

  **Response:** \`[Refer to SDK Response JSON Format](#sdk-response-json-format)

  **Callback:** The callback will have the below response format.

  <br />
</Accordion>

<Accordion title="Step 2. Check if UPI Bolt is Enabled" icon="folder" id="step-2-check-enabled">
  This method is used to check whether the upi bolt is enabled for the merchant or not.

  <br />

  ```Cordova
  cordova.plugins.PayUUpiBoltUiCordova.isUPIBoltEnabled(this.responseCallBack);
  ```

  <br />

  **Response:** \`[Refer to SDK Response JSON Format](#sdk-response-json-format)

  <br />

  | Field   | Definition                                       |
  | ------- | ------------------------------------------------ |
  | code    | `Integer` Status code (Success = 0, Failure = 1) |
  | message | `String` Message                                 |

  <br />
</Accordion>

<Accordion title="Step 3. Register and Pay" icon="folder" id="step-3-register-and-pay">
  This API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

  <br />

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

  <br />

  **Sample Code**

  <br />

  ```Cordova
  const currentTimeMillis = new Date().getTime();

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

  cordova.plugins.PayUUpiBoltUiCordova.registerAndPay(responseCallBack, paymentParams);
  ```

  <br />

  **Response:** `Map` [Refer to SDK Response JSON Format](#sdk-response-format).

  <br />

  | Field  | Definition       |
  | ------ | ---------------- |
  | result | Payment Response |

  <br />
</Accordion>

<Accordion title="Step 4. Open UPI Management" icon="folder" id="step-4-upi-management">
  This API allows you to manage UPI accounts and transaction history.

  ```Cordova
  // Screen Types
  const screenType = <screenType> // String

  cordova.plugins.PayUUpiBoltUiCordova.openUPIManagement(responseCallBack, screenType);
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

  **Response:** `Map` [Refer to SDK Response JSON Format](#sdk-response-json-format)
</Accordion>

<Accordion title="Step 5. Listener/Callback logic" icon="folder" id="step-6-listener-callback">
  The listener/callback contains following methods where the merchant app will get the API response and hash-related callbacks.

  ```Cordova
  var responseCallBack = function (response) {
  console.log('responseCallBack:', JSON.stringify(response));

  // 1. onPayUSuccess(Map response): Triggered when the payment is successful.
  if ('onPayUSuccess' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 2. onPayUFailure(Map response): Triggered when the payment fails.
  if ('onPayUFailure' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 3. onPayUCancel(Map response): Triggered when the user cancels the payment.
  if ('onPayUCancel' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 4. onError(Map response): Triggered when an error occurs in the SDK.
  if ('onError' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 5. isUPIBoltEnabled(Map response): Indicates whether the UPI Bolt SDK is enabled.
  if ('isUPIBoltEnabled' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 6. onReset(Map response): Confirms that the SDK instance has been reset successfully.
  if ('onReset' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 7. onClearCache(Map response): Confirms that the SDK cache has been cleared.
  if ('onClearCache' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 8. onIsRegistered(Map response): Indicates the user's registration status with the plugin.
  if ('onIsRegistered' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 9. onInitSDK(Map response): Triggered after SDK initialization, including any initialization errors.
  if ('onInitSDK' in response) {
    showAlert(JSON.stringify(response));
    return;
  }

  // 10. generateHash(Map response): Triggered when the SDK requests hash generation.
  if ('generateHash' in response) {
    handleHashGeneration(response);
    return;
  }
  };  
  ```
</Accordion>

<Accordion title="Step 6. Hash Generation Logic" icon="folder" id="step-7-hash-generation">
  The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

  For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUUPIBoltUiListener.  The generateHash() method is called by the SDK each time it needs an individual hash.

  ```Cordova
  /**
  * Handles hash generation requested by the PayU UPI Bolt SDK.
  *
  * The merchant receives a JSON object containing details required to generate the hash.
  * The following keys must be checked in the response:
  * 1. hashString – The string that needs to be hashed
  * 2. hashName   – The name of the hash
  * 3. postSalt   – (Optional) Additional salt value
  *
  * Hash Generation Steps:
  * - Append your merchant salt to the hashString
  * - If postSalt is present, append it after the merchant salt
  * - Generate the hash using the SHA-512 algorithm
  * - Pass the generated hash back to the SDK using hashGenerated()
  */
  function handleHashGeneration(response) {
  const resultValue = response.generateHash;

  const hashString = resultValue.hashString;
  const hashName = resultValue.hashName;
  const postSalt = resultValue.postSalt;

  /*
   * NOTE:
   * For security reasons, hash generation should be done on the server.
   * Fetch the generated hash from your backend using hashString.
   */

  // Fetch the hash value from your server
  const hash = <fetch_hash_from_server>;

  // Prepare hash map to send back to SDK
  const hashMap = {};
  hashMap["hashName"] = hashName;
  hashMap[hashName] = hash;

  // Pass the generated hash to the PayU UPI Bolt SDK
  cordova.plugins.PayUUpiBoltUiCordova.hashGenerated(hashMap);
  }
  ```
</Accordion>

## SDK Response JSON Format

| Field        | Data Type | Definition                                                                      |
| :----------- | :-------- | :------------------------------------------------------------------------------ |
| result       | Any?      | Contains response model if received success callback                            |
| code         | Int       | [Ref. Response Codes and Messages section](#error-codes-and-error-message-list) |
| message      | String?   | [Ref. Response Codes and Messages section](#error-codes-and-error-message-list) |
| responseType | Int       | Ref. [ResponseType](#response-type)                                             |

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

## SMS Hash generation for Android OTP auto read

Copy AppSignatureHelper class given below in your project.

```
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
 * Without the correct hash, your app won't recieve the message callback. This only needs to be
 * generated once per app and stored. Then you can remove this helper class from your code.
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

<br />

Log the value generated by following statement

```
Log.d("appSignature", AppSignatureHelper(requireContext()).appSignatures[0])
```

Share the value to PayU team for configuring SMS hash at BE.

<br />
