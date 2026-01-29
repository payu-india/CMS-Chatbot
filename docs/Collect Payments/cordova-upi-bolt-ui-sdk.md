---
title: Cordova UPI Bolt UI SDK
deprecated: false
hidden: true
metadata:
  robots: index
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

<Accordion title="Registration and Pay" icon="fa-folder">
  <br />

  1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
  2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
  3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
  4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
  5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

  <br />

  <Image align="center" src="https://files.readme.io/a2d41854641a44082dcb2bc0e38a3bea213ef7c25ca0ce9429d8c8221581ab75-upi_bolt_reactnative_customer_journey_register_pay.jpeg" alt="UPI Bolt React Native Custome Journey for Registration and Pay" />
</Accordion>

<Accordion title="Pay" icon="fa-folder">
  <br />

  1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
  2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
  3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

  <br />

  <Image align="center" src="https://files.readme.io/fad794f25f0f6b108bc694ee13f79f7a3b5de220f6f90990409f7267e86446bb-upi_bolt_reactnative_customer_journey_pay.jpeg" alt="UPI Bolt React Native Custome Journey for Pay" />

  <br />
</Accordion>

<Accordion title="Profile Management Journey" icon="fa-folder">
  <br />

  1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
  2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
  3. Customers can see all the raised disputes from the Dispute history screen.
  4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

  <br />

  <Image align="center" src="https://files.readme.io/556315528c71a4e06f9cb9c4edb40fd651eef3c10b20a9418d569231877d98a7-upi_bolt_reactnative_customer_journey_profile_mgmt.jpeg" alt="UPI Bolt React Native Custome Journey for Profile Management" />
</Accordion>

## Steps to Integrate PayU Bolt SDK

<Accordion title="Prerequisites" icon="folder" id="prerequisites">
  <Callout icon="🚧" theme="warn">
    Supported iOS deployment target - iOS 17 and above.
  </Callout>

  Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use PayU UPI Bolt UI SDK for customer registration, payment, and profile management.

  <br />

  To include the PayU UPI Bolt UI SDK in your project, add the following dependency to your package.json file:

  **UAT:**

  ```
  cordova plugin add payu-upi-bolt-ui-cordova\@0.0.1-alpha.14
  ```

  **PRODUCTION:**

  ```
  cordova plugin add payu-upi-bolt-ui-cordova\@0.0.3
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

  ```React-Native
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
</Accordion>

<Accordion title="Step 6. Hash Generation Logic" icon="folder" id="step-7-hash-generation">
  The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

  For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUUPIBoltUiListener.  The generateHash() method is called by the SDK each time it needs an individual hash.

  ```React-Native
  function handleHashGeneration(hashName, hashString) {  // Merchant will get Map/ JSON with type of hash and hash string as value of dictionary.
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

    // get hash for "hashName" from server
    // get hash for "hashString" from server
    
    var hashValue = <fetch_hash_from_server>;

    // After fetching hash set its value in below variable "hashMap"
    
    const result = { "hashName": <hashName>, <hashName>: <hashValue> };
    PayUBizSdk.hashGenerated(result);
  }
  ```
</Accordion>
