---
title: Flashpay Decoupled Flow Android Integration
deprecated: false
hidden: true
metadata:
  title: FlashPay Decoupled Flow Android Integration
  description: >-
    FlashPay decoupled flow with MFA on Android. 3DS and multi-factor
    authentication integration steps.
  keywords:
    - FlashPay decoupled flow Android
    - 3DS Android MFA
    - PayU FlashPay integration
  robots: index
---
---
title: Flashpay Decoupled Flow Android Integration
deprecated: false
hidden: false
metadata:
  robots: index
---

FlashPay solution primarily offers advanced biometric-based out-of-band (OOB) authentication. The Wibmo Tridentity SDK enables seamless integration of FlashPay functionality using various API methods and configuration options tailored to business needs.

<Cards columns={3}>
  <Card title="1. Gradle Changes" href="#step-1-gradle-changes">
    Add Tridentity SDK dependency and minimum requirements to build.gradle
  </Card>

  <Card title="2. Android Manifest Permissions" href="#step-2-android-manifest-permissions">
    Declare required permissions for biometric auth and SIM binding
  </Card>

  <Card title="3. SDK Configuration" href="#step-3-sdk-configuration">
    Initialize the SDK with client-specific config and configSdk
  </Card>

  <Card title="4. Customer Enrollment" href="#step-4-customer-enrollment">
    Enroll users for Tridentity-based biometric authentication
  </Card>

  <Card title="5. Check Registration Status" href="#step-5-check-registration-status">
    Verify if a customer is already registered in Tridentity
  </Card>

  <Card title="6. Process Transaction" href="#step-6-process-transaction">
    Process transactions with biometric OOB authentication
  </Card>

  <Card title="7. UI Customization" href="#step-7-ui-customization">
    Customize SDK UI via themeConfig and text configurations
  </Card>

</Cards>

## Step 1: Gradle Changes

<Accordion title="Minimum Requirements" icon="fa-info-circle">
  * **Minimum SDK Version:** `v23`
  * **Compile SDK Version:** `v33` or later
</Accordion>

<Accordion title="Maven Dependency" icon="fa-info-circle">
  To include the Tridentity SDK, add the following line to your `app/build.gradle` file:

  ```groovy
  implementation 'in.payu:tridentity-sdk:x.x.x-SNAPSHOT'
  ```
</Accordion>

## Step 2: Android Manifest Permissions

The SDK requires specific application-level permissions to enable its functionalities. As per business needs and enabled modes, these permissions must be declared in the `AndroidManifest.xml` file.

<Accordion title="Supported Modes in SDK" icon="fa-info-circle">
  * **Biometric Based Authentication**
</Accordion>

<Accordion title="Required Permissions" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Phone State<br/><code>mandatory</code></td>
          <td>Mandatory to detect SIM swap scenarios.</td>
          <td>android.permission.READ_PHONE_STATE</td>
        </tr>
        <tr>
          <td>SMS<br/><code>conditional</code></td>
          <td>For auto send of SMS if SDK is enabled for binding the device.</td>
          <td>android.permission.SEND_SMS</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>

  Include the following permissions in your AndroidManifest.xml file to enable the SDK functionalities:

  ```xml
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.READ_PHONE_STATE" />
  <uses-permission android:name="android.permission.SEND_SMS" />
  ```
</Accordion>

## Step 3: SDK Configuration

This is a prerequisite step where you invoke the SDK's configuration method to initialize client-specific details. Validation of security checks and required permissions also occurs during this phase.

<Accordion title="Configuration Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>context<br/><code>mandatory</code></td>
          <td>Application Context</td>
          <td>this</td>
        </tr>
        <tr>
          <td>clientId<br/><code>mandatory</code></td>
          <td><code>String</code>. Will be shared offline.</td>
          <td>"CLIENT_123"</td>
        </tr>
        <tr>
          <td>env<br/><code>mandatory</code></td>
          <td><code>String</code>. Build Environment.</td>
          <td>"UAT" or "PROD"</td>
        </tr>
        <tr>
          <td>authType<br/><code>mandatory</code></td>
          <td><code>String</code>. Must be passed as "Biometric".</td>
          <td>"Biometric"</td>
        </tr>
        <tr>
          <td>bin<br/><code>mandatory</code></td>
          <td><code>String</code>. First 6 digits of the card used for the transaction.</td>
          <td>"123456"</td>
        </tr>
        <tr>
          <td>bankLogoUrl<br/><code>optional</code></td>
          <td><code>String</code>. Logo of the issuer bank associated with the card.</td>
          <td>"https://example.com/bank-logo.png"</td>
        </tr>
        <tr>
          <td>merchantName<br/><code>optional</code></td>
          <td><code>String</code>. Name of the recipient.</td>
          <td>"Sample Merchant"</td>
        </tr>
        <tr>
          <td>themeConfig<br/><code>optional</code></td>
          <td>Theme configuration. Configures SDK appearance. If not passed, default settings or server-configured settings will be used.</td>
          <td>themeConfigObject</td>
        </tr>
        <tr>
          <td>bankId<br/><code>mandatory</code></td>
          <td><code>String</code>. Identifier for the bank.</td>
          <td>"BANK_001"</td>
        </tr>
        <tr>
          <td>bindingType<br/><code>conditional</code></td>
          <td><code>String</code>. Indicates if the card is the first for that bank. This parameter is mandatory if present in ACS response during Registration flow. Possible values: "01", "02", "03".</td>
          <td>"01"</td>
        </tr>
        <tr>
          <td>customerId<br/><code>conditional</code></td>
          <td><code>String</code>. Mandatory for transaction/de-registration flows. Mandatory in registration flow if bindingType is available.</td>
          <td>"CUST_12345"</td>
        </tr>
        <tr>
          <td>registrationTimeout<br/><code>conditional</code></td>
          <td><code>Int</code>. Specifies the maximum duration allowed for registration completion within the SDK. This value is mandatory during registration flow.</td>
          <td>300</td>
        </tr>
        <tr>
          <td>transactionTimeout<br/><code>conditional</code></td>
          <td><code>Int</code>.  Specifies the maximum duration allowed for authentication of transaction within the SDK. This value is mandatory during transaction flow.</td>
          <td>120</td>
        </tr>
        <tr>
          <td>uid<br/><code>mandatory</code></td>
          <td><code>String</code>. A unique identifier for the card. (dynamically retrieved from ACS).</td>
          <td>"CARD_UID_789"</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>

  The SDK must be configured with client-specific details before any other methods can be used. Create a configuration object with the required parameters and call the configSdk method to initialize the SDK properly. Check the message flag in the onSuccess callback for configuration status:

  ```kotlin
  TridentitySDK.getInstance().configSdk(context, configObject, object : ConfigStatusCallback {
      override fun onSuccess(event: JSONObject) {
          // Check the message flag in the event for configuration status
      }
      override fun onError(errorCode: Int, errorDesc: String) {
          // Handle configuration error
      }
  })
  ```

  Once populated with these parameters, the configuration object is passed to the configSdk method to properly initialize the SDK, with callback handlers managing the configuration success or failure responses.

  ```kotlin
  val configObject = JSONObject()  

  configObject.put("env", "UAT") // UAT or PROD 

  configObject.put("clientId", "")   

   configObject.put(“themeConfig”, “{themeConfig}”)

  configObject.put(“bankId”,"8045")

  configObject.put(“bindingType”, “02”)

  configObject.put(“customerId”, "B81AEBFD8013D2F92B7DF38C00B20F168B18B3C27E78BAA721280189A5B86664")

  configObject.put(“registrationTimeout”, 60)
  ```

  <Callout icon="📘" theme="info">
    From the response object in the onSuccess method check for the **message** flag to get Configuration status.
  </Callout>
</Accordion>

## Step 4: Customer Enrollment

This method facilitates user enrollment for Tridentity-based authentication.

<Accordion title="Enrollment Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>activity<br/><code>mandatory</code></td>
          <td>Instance of AppCompatActivity.</td>
          <td>this</td>
        </tr>
        <tr>
          <td>uid<br/><code>mandatory</code></td>
          <td>Card ID.</td>
          <td>"CARD_UID_789"</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>

  To enable biometric authentication for users, they must first be enrolled in the Tridentity system. Call the initiateRegistration method with the activity instance and registration object to begin the enrollment process. Check the message in the onSuccess response object for the registration status:

  ```kotlin
  TridentitySDK.getInstance().initiateRegistration(activity, regObject, object : RegistrationStatusCallBack {
      override fun onSuccess(event: JSONObject) {
          // Check message in the event response object for the status
      }
      override fun onError(code: Int, error: String) {
          // Handle registration error
      }
  })
  ```

  The registration object is then passed to the initiateRegistration method to begin the enrollment process, with callback handlers to manage success and error responses during the biometric setup workflow.

  ```kotlin
  val regObject = JSONObject()  

  regObject.put("uid", "<>")  

  ```

  <Callout icon="📘" theme="info">
    From the response object in the onSuccess method, check for the message flag to get the status
  </Callout>
</Accordion>

## Step 5: Check Registration Status

This method retrieves the customer's current registration status in the Tridentity system.

<Accordion title="Registration Status Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>context<br/><code>mandatory</code></td>
          <td>Application Context</td>
          <td>this</td>
        </tr>
        <tr>
          <td>clientId<br/><code>mandatory</code></td>
          <td>Will be shared offline.</td>
          <td>"CLIENT_123"</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>

  Use the checkRegistrationStatus method to verify if a customer is already registered in the Tridentity system:

  ```kotlin
  TridentitySDK.getInstance().checkRegistrationStatus(context, custObject, object : RegistrationStatusCallBack {
      override fun onSuccess(event: JSONObject) {
        // Handle successful status check
        // Note: customerStatus : registration_comm_success is only considered as successful Registration.  

      }
      override fun onError(code: Int, error: String) {
          // Handle status check error
      }
  })
  ```

  The customer object is then passed to the checkRegistrationStatus method to perform the verification, with success callbacks specifically looking for a "registration\_comm\_success" status to confirm successful registration.

  ```kotlin
  val custObject = JSONObject()  

  custObject.put("clientId", "<>")     
  ```
</Accordion>

## Step 6: Process Transaction

This method processes transactions and validates them using biometric OOB authentication.

<Accordion title="Transaction Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>context<br/><code>mandatory</code></td>
          <td>Application Context.</td>
          <td>this</td>
        </tr>
        <tr>
          <td>jsonObject<br/><code>mandatory</code></td>
          <td>JSON Object containing transaction parameters.</td>
          <td>transactionObject</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Transaction JSON Object Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>txnId<br/><code>mandatory</code></td>
          <td>Unique for each transaction. Max length: 25 characters. No special chars like _,$,%,&.</td>
          <td>"TXN123456789"</td>
        </tr>
        <tr>
          <td>clientID<br/><code>mandatory</code></td>
          <td>Will be shared offline.</td>
          <td>"CLIENT_123"</td>
        </tr>
        <tr>
          <td>amount<br/><code>optional</code></td>
          <td>Total transaction amount.</td>
          <td>"100.00"</td>
        </tr>
        <tr>
          <td>merchantName<br/><code>optional</code></td>
          <td>Merchant issuer name.</td>
          <td>"Sample Merchant"</td>
        </tr>
        <tr>
          <td>hashKey<br/><code>mandatory</code></td>
          <td>Dynamically retrieved from the ACS.</td>
          <td>"ABC123DEF456"</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>

  Create a JSON object with the transaction details and call the processTransaction method to initiate biometric authentication for the transaction:

  ```kotlin
  TridentitySDK.getInstance().processTransaction(context, jsonObject, object : UpdateTransactionCallback {
      override fun onSuccess(event: JSONObject) {
          // Handle successful transaction
      }
      override fun onError(code: Int, error: String) {
          // Handle transaction error
      }
  })
  ```

  The populated transaction object is then passed to the processTransaction method to trigger the biometric authentication flow, allowing users to authorize transactions using their enrolled biometric credentials.

  ```kotlin
  val custObject = JSONObject()  

  custObject.put("clientId", "<>")  

  custObject.put("txnId", "<>")  

  custObject.put("hashKey", "<>")  
  ```
</Accordion>

## Step 7:  UI Customization

The SDK allows UI customizations through a configuration object passed in as `themeConfig`.

<Accordion title="UI Customization Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Description</th>
          <th>Example</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>LabelCustomization<br/><code>optional</code></td>
          <td>Configurations: headingCustomization, subHeadingCustomization. Sub Components: textColor, fontSize, fontName</td>
          <td>labelConfigObject</td>
        </tr>
        <tr>
          <td>ToolbarCustomization<br/><code>optional</code></td>
          <td>Configurations: backgroundColor, textColor, fontSize, fontName</td>
          <td>toolbarConfigObject</td>
        </tr>
        <tr>
          <td>ButtonCustomization<br/><code>optional</code></td>
          <td>Configurations: primaryButtonCustomization, secondaryButtonCustomization. Sub Components: buttonCornerRadius, fontSize, fontName, Enabled/disabled text & background color</td>
          <td>buttonConfigObject</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Text Customization Parameters" icon="fa-info-circle">
  <HTMLBlock>{`
    <table>
      <thead>
        <tr>
          <td>bottomSheetPermissionPopupConfiguration<br/><code>optional</code></td>
          <td>Text customization for permission popup: topHeaderText, topSubHeaderText, buttonText, etc.</td>
          <td>permissionPopupConfig</td>
        </tr>
        <tr>
          <td>bottomSheetSimBindingProcessingPopupConfiguration<br/><code>optional</code></td>
          <td>Texts for SIM binding, number verification, biometric setup, etc.</td>
          <td>simBindingConfig</td>
        </tr>
        <tr>
          <td>bottomSheetRegistrationSuccessfulPopupConfiguration<br/><code>optional</code></td>
          <td>Success messages and buttonText</td>
          <td>registrationSuccessConfig</td>
        </tr>
        <tr>
          <td>bottomSheetFailureScreenConfiguration<br/><code>optional</code></td>
          <td>Error messages and buttonText</td>
          <td>failureScreenConfig</td>
        </tr>
      </tbody>
    </table>
  `}</HTMLBlock>
</Accordion>

## Deregistration

This method is used to deregister a customer from the Tridentity service.

Call the deRegistration method to remove a customer from the Tridentity authentication system:

```kotlin
TridentitySDK.getInstance().deRegistration(context, object : DeregisterCallBack {
    override fun onSuccess(event: JSONObject) {
        // Handle successful deregistration
    }
    override fun onError(code: Int, error: String) {
        // Handle deregistration error
    }
})
```

##