---
title: Flutter UPI Bolt UI SDK
deprecated: false
hidden: true
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

<Accordion title="Registration and Pay" icon="fa-folder">
  1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
  2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card. If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
  3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
  4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.
  5. Finally, customers can make a transaction using the added bank account. If the customer is using the bank account for the first time, he will also need to set the MPIN.

  <Image align="center" src="https://files.readme.io/477aa57e491d8be306be606858728a809e562aed4a65bef8663d03703a82d98f-0.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Pay Flow" />
</Accordion>

<Accordion title="Pay" icon="fa-folder">
  1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
  2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
  3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

  <Image align="center" src="https://files.readme.io/b3050b0d3581a62b29ddccb4d183cf14f0251e6cbd033cea8916eae364209586-1.jpg" alt="Flutter UPI Bolt UI SDK Integration Pay Flow" />
</Accordion>

<Accordion title="Profile Management Journey" icon="fa-folder">
  1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
  2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
  3. Customers can see all the raised disputes from the Dispute history screen.
  4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

  <Image align="center" src="https://files.readme.io/f6649179d1e3193799da08174d44e0d4a021da5b3bcfbf62b6c7863d13fd26ed-2.jpg" alt="Flutter UPI Bolt UI SDK Integration Registration and Profile Management Flow" />
</Accordion>

## Steps to Integrate

<Accordion title="Prerequisites" icon="folder">
  <h5> SDK Compatibility: Ensure that the application's minimum development target is set to version 13 or higher. </h5>

  Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use PayU UPI Bolt UI SDK for customer registration, payment, and profile management.

  <Accordion title="iOS Integration" icon="folder">
    To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile.

    **Supported iOS deployment target - iOS 17 and above.**

    The following xcframework files will be provided by PayU during onboarding:

    1. NPCI - CommonLibrary.xcframework
    2. AXIS - OlivePayLibrary.xcframework

    Add these framework in your project. The added framework is similar to the following screeshot:

    <Image align="center" src="https://files.readme.io/ab49c1c2aad9cb456436a7bf17437ea1797620f6bb650deb37f4a798c1328419-3.png" alt="NPCI - CommonLibrary.xcframework and AXIS - OlivePayLibrary.xcframework added to project" />

    In Build Settings > Framework Search Path, add `$(PROJECT_DIR)/Frameworks` if it is not added automatically by Xcode.

    <Image align="center" src="https://files.readme.io/dfbfe5bb1b9bd93ea6c30e191556643e8a0e870550a40f46225ea071e4eaab0c-4.png" alt="Flutter UPI Bolt UI SDK Integration PROJECT_DIR config" />
  </Accordion>

  <br />

  <Accordion title="Android Integration" icon="folder">
    Add the following dependency in the build.gradle file of your android app module:

    ```gradle
    implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.1-dev4'
    implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
    ```

    Add the given aar file in the libs folder of your android app module:

    ```
    <your_project>/android/app/libs/SecureComponent-release-prod_05062024_9d3904ab.aar
    ```

    Install the Flutter package:

    ```bash
    flutter pub add payu_upi_bolt_ui_flutter:^1.0.0-alpha.1
    ```
  </Accordion>

  <br />
</Accordion>

<Accordion title="Step 1: Initialization" icon="folder">
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

<br />

<Accordion title="Clear SDK Cache of PayUBolt SDK" icon="folder">
  The `clearCache` method is used to clear the cache corresponding to the passed PG value.

  <br />

  ```dart
  payUUpiFlutter.clearCache(params: Map);
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

  **Response**: [SDK Response JSON Format:](<SDK Response JSON Format:>)

  <br />
</Accordion>

<Accordion title="Clear SDK Cache of PayUBolt SDK" icon="folder">
  The `clearCache` method is used to clear the cache corresponding to the passed PG value.

  <br />

  ```dart
  payUUpiFlutter.clearCache(params: Map);
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
          `String` PG value to check clear pg specific data
        </td>
      </tr>
    </tbody>
  </Table>

  <br />

  **Response:** [SDK Response JSON Format:](<SDK Response JSON Format:>)

  <br />
</Accordion>

<Accordion title="Check Plugin Registration Status of PayUBolt SDK" icon="folder">
  The `isRegistered` method is used to check pg registration status.

  <br />

  ```dart
  payUUpiFlutter.isRegistered(params: Map);
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

  **Response:** [SDK Response JSON Format:](<SDK Response JSON Format:>)

  **Callback:** The callback will have the below response format.

  <br />
</Accordion>

<Accordion title="Step 2. Check if UPI Bolt is Enabled" icon="folder">
  This method is used to check whether the upi bolt is enabled for the merchant or not.

  <br />

  ```dart
  payUUpiFlutter.isUPIBoltEnabled();
  ```

  <br />
  
**Response:** 

  | Field   | Definition                                       |
  | ------- | ------------------------------------------------ |
  | code    | `Integer` Status code (Success = 0, Failure = 1) |
  | message | `String` Message                                 |

  <br />

  **Response:** [SDK Response JSON Format:](<SDK Response JSON Format:>)

  <br />
</Accordion>

<Accordion title="Step 3. Register and Pay" icon="folder">
  This API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.
</Accordion>

[SDK Response JSON Format:](<SDK Response JSON Format:>)

<br />
