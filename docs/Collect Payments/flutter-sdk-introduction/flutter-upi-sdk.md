---
title: Flutter UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Flutter UPI SDK
  description: >-
    This document outlines the knowledge base for UPI transactions, detailing
    the differences between Collect and Intent transactions, and provides
    guidance on integrating UPI SDK with React Native and Flutter, including
    compatibility requirements and integration steps.
  keywords:
    - Flutter UPI SDK
    - Integrate Flutter UPI SDK
    - ' Flutter UPI SDK Integration'
    - Integrate Mobile Flutter UPI SDK
    - PayU Mobile Flutter UPI SDK
  robots: index
next:
  description: ''
---
This cluster aims to document all the knowledge base for UPI transactions. Implementation of most of the UPI flows is different when compared to normal transactions.

There are broadly two types of UPI transactions, Collect and Intent(Pure Intent/In-App). For collect transactions, PayU informs the payment gateway to trigger a transaction to the app linked to the provided VPA, which asks the user for approval.

For intent transactions, we delegate the transaction process to an external app like BHIM, Google Pay, etc, which lets users transfer money to a VPA specified by us. After that, we use the PG (related to the specified VPA) for verification. PayU has a pre-configured VPA (distinct on the PG-Merchant level) on which the app makes the user pay the amount. To integrate UPI SDK with React Native, see Integrate UPI SDK with Flutter.

<Callout icon="❗️" theme="error">
  **Prerequisites for Google Pay:**

  * To start transacting through Google Pay™, register your business on Google using the Google Onboarding form, In this registration process, you need to add the merchant VPAs created by PayU for you. In the case of multiple VPAs, all of them need to be registered with Google.
  * To enable Google Pay, contact your Point of Contact at Google. For any further queries or help with onboarding, send a mail to PayU Mobile Integration Team.
</Callout>

***

## Compatibility

<Accordion title="Android" icon="fa-code">
  * Min SDK Version: 21
  * Compile SDK Version: 31+
  * Kotlin 1.6.10
</Accordion>

## iOS

* iOS version: 11

## SDK Integration

To integrate the Flutter UPI SDK, perform the following steps:

<Accordion title="Step 1: Include the SDK in your App" icon="fa-code">
  The UPI SDK for Flutter is offered through Flutter` pub.dev.` To add the SDK plugin use the following dependency in your app:

  ```
  //Add plugin in your app 
  $ flutter pub add payu_upi_flutter

  //Import UPI Plugin in your dart code
  import 'package:payu_upi_flutter/payu_upi_flutter.dart'; 
  ```

  <Callout icon="📘" theme="info">
    **Note**: If you are developing for iOS, Install the pod using the following command inside “ios” folder.

    ```
    //Install payu dependencies in your ios project. 
    $ pod install 
    ```
  </Callout>
</Accordion>

<Accordion title="Step 2: Initialize Flutter SDK" icon="fa-code">
  Declare the `PayUUpiFlutter` instance and initialize the object.

  ```d Dart
  class _MyAppState extends State<MyApp> implements PayUUPIProtocol {
      late PayUUpiFlutter payUUpiFlutter;

    @override
    void initState() {
      super.initState();
      payUUpiFlutter = PayUUpiFlutter(this);
    }
  }
  ```

  <Callout icon="📘" theme="info">
    **Note**: If you are developing for iOS, make sure your minimum deployment target is iOS 11.
  </Callout>
</Accordion>

<Accordion title="Step 3. Implement the Callback protocol" icon="fa-code">
  1. Implement PayUPIProtocol to receive hash and transaction callback.

  ```d Dart
  class _MyAppState extends State<MyApp> implements PayUUPIProtocol 
  ```

  2. Implement the following methods in your class to receive the callbacks.

  ```d Dart
  @override
  onPayUUPIMakePayment(Map response) {

    String eventType = response[PayUEventType.eventType];
    switch(eventType) { 
        case PayUEventType.onPaymentSuccess: { 
             String eventResponse = parsePayUResponse(response);
             //handle PayU response 
        } 
        break; 
        case PayUEventType.onPaymentFailure: { 
             String eventResponse = parsePayUResponse(response);
             //handle PayU response
        } 
        break; 

        case PayUEventType.onErrorReceived: { 
             String eventResponse = parsePayUResponse(response);
             //handle PayU response
        } 
        break; 
      
        case PayUEventType.onPaymentTerminate: 
        {  
             String eventResponse = parsePayUResponse(response);
             //handle PayU response
        } 
        break; 
      
        default: { 
             //handle unknown events
         } 
        break; 
    } 
  }

  @override
  onPayUUPIValidateVPA(Map response) {
     String eventType = response[PayUEventType.eventType];
    switch(eventType) { 
        case PayUEventType.onValidateSuccess: { 
             String eventResponse = parsePayUResponse(response);
             //handle PayU response
        } 
        break; 
      
        case PayUEventType.onErrorReceived: { 
             String eventResponse = parsePayUResponse(response);
             //handle PayU response
        } 
        break; 
      
        default: { 
             //handle unknown events
         } 
        break; 
    } 
  }

  String parsePayUResponse(Map response){
    var eventResponse = response[PayUEventType.eventResponse];
    return eventResponse != null ? eventResponse.toString() : "";
  }
  ```
</Accordion>

<Accordion title="Step 4: Setup Payment Hashes" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **Warning**: Always generate the hash at your backend to ensure security.
  </Callout>

  Hash is required to authenticate the request and to make sure MiTM has not happened while data was traveling over the network. You have to set the hash in the hash parameter during the creation of payment parameters.  Use the following format to generate the hash:

  `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`

  > 📘 TPV Hash
  >
  > For TPV transactions, use the following format to generate the hash:
  >
  > `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)`
  >
  > The **beneficiarydetail** parameter value will be at last or the last value to be appended.`{"beneficiaryAccountNumber":<Account No>,"ifscCode":<IFSC>}`

  Here is a sample hash value for your reference:

  `smsplus|1695662774012|1|Info|Abc|[test@gmail.com](mailto:test@gmail.com)|udf1|udf2|udf3|udf4|udf5||||||  {"beneficiaryAccountNumber":"1234567890","ifscCode":"IFSC0000024"}|1b1b0`

  > 📘 SI Hash
  >
  > For SI Trasnaction, use the following format to generate the hash :-
  >
  > SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si\_details|SALT)
  >
  > Here is sample hash value for reference :-
  >
  > `3TnMpV|PayU_1752232075823|1|Info|Abc|[test@gmail.com](mailto:test@gmail.com)|udf1|udf2|udf3|udf4|udf5||||||\{"paymentStartDate":"2025-07-28","paymentEndDate":"2028-08-28","billingAmount":"100.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"billingRule":"MAX"}|g0nGFe03`
</Accordion>

<Accordion title="Step 5: Generate Payment Parameters" icon="fa-code">
  Set up the payment parameters for the SDK to initiate a transaction request. Use the following sample code for a quick integration:

  ```d Dart
  var additionalParam = {
    PayUAdditionalParamKeys.udf1: <user defined value 1>,
    PayUAdditionalParamKeys.udf2: <user defined value 2>,
    PayUAdditionalParamKeys.udf3: <user defined value 3>,
    PayUAdditionalParamKeys.udf4: <user defined value 4>,
    PayUAdditionalParamKeys.udf5: <user defined value 5>,
  };
  var payUPaymentParams = {
    key: <Merchant Key>,
    amount: <Amount>,
    product_info: <Product Info>,
    first_name: <First Name>,
    email: <Email>,
    phone: <Phone>,
    ios_surl: <SURL>,
    ios_furl: <FURL>,
    android_surl: <SURL>,
    android_furl: <FURL>,
    environment: <String>, //0 => Production 1 => Test 
    isProduction: <Boolean>, //Set environment for android
    user_credentials: <unique user identifier>
    transaction_id:<Transaction ID>,
    additional_param: additionalParam,
  	hash: <Pass Hash Value>,
    beneficiary_account_number: <Beneficiary Account Number>,
    beneficiary_ifsc: <ifsc code>,
    payment_mode:<String> // for Intent flow use "INTENT", for collect flow use "upi",
    disable_intent_seamless_failure:  <String>, // -1 | 0 ,
  	// package_name parameter used for Android only
    package_name: <String>, //package name for the specific UPI intent (i.e. 				'net.one97.paytm') // 
  	// intent_app parameter used for IOS only
    intent_app : <String>, //scheme name for the specific UPI intent (i.e. 'phonepe') // 
  };

  var si_params = {
      "is_free_trial": "0",
      "si": '1',
      "si_details": {
        "is_free_trial": "0",
        "billing_amount": '100.00', //Required
        "billing_currency": 'INR',
        "billing_cycle": //Required
        'MONTHLY', // YEARLY | MONTHLY | WEEKLY | DAILY | ONCE | ADHOC
        "billing_interval": 1, //Required
        "payment_start_date": '2025-07-28', //Required
        "payment_end_date": '2028-08-28', //Required
        "billing_limit": 'ON', //ON, BEFORE, AFTER
        "billing_rule": 'MAX', //MAX, EXACT
      }
    };
  ```

  <Accordion title="Payment Parameters" icon="fa-code">
    <Table align={["left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Parameter
          </th>

          <th style={{ textAlign: "left" }}>
            Description
          </th>

          <th style={{ textAlign: "left" }}>
            Notes
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            key
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` This parameter must contain your merchant key received from PayU.
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            transaction\_id
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` It should be unique for each transaction.
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: -\_/
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            amount
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Total transaction amount.
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty and should be a valid double-stringified example: “100.0”
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            product\_info
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String`Product information.
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            first\_name
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer’s first name
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            email
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer’s email id
          </td>

          <td style={{ textAlign: "left" }}>
            Cannot be null or empty
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            phone
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer’s phone number.
          </td>

          <td style={{ textAlign: "left" }}>
            There should be a valid phone number
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ios\_surl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction is successful, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for iOS integration
          </td>

          <td style={{ textAlign: "left" }}>
            Should be a valid URL
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ios\_furl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction fails, PayU will load this URL and pass the transaction response.
            No\*\*\*\*te: This field is applicable for iOS integration
          </td>

          <td style={{ textAlign: "left" }}>
            Should be a valid URL
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            android\_surl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction is successful, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for Android integration
          </td>

          <td style={{ textAlign: "left" }}>
            Should be a valid URL
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            android\_furl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction fails, PayU will load this URL and pass the transaction response.
            When the transaction is a success, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for Android integration
          </td>

          <td style={{ textAlign: "left" }}>
            Should be a valid URL
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            environment
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Environment of SDK
          </td>

          <td style={{ textAlign: "left" }}>
            "0" for Production and "1" for Test
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            user\_credentials
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String`User bank account number for TPV transaction.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            beneficiary\_ifsc
            `no`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` IFSC of bank account for TPV transaction.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            beneficiary\_account\_number
          </td>

          <td style={{ textAlign: "left" }}>
            Users bank account number for TPV transaction.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>
      </tbody>
    </Table>
  </Accordion>
</Accordion>

<Accordion title="Step 6: Initiate the payment" icon="fa-code">
  Initialise and launch the SDK by calling the following code snippet:

  ```d Dart
  payUUpiFlutter.makeUPIPayment(params: <PayU Payment Params>);
  ```
</Accordion>

<Accordion title="Step 7: VPA validation" icon="fa-code">
  Initialise and launch the Flutter UPI SDK by calling the following code snippet to validate the VPA

  ```d Dart
    validateVPA() async {
      // ignore: prefer_interpolation_to_compose_strings
      var vpaHash = HashService.calculateHash(PayUTestCredentials.merchantKey +
          '|' +
          "validateVPA" +
          '|' +
          PayUTestCredentials.vpa +
          '|' +
          PayUTestCredentials.merchantSalt);
      var params = PayUParams.createPayUPaymentParams(PayUPaymentModeKeys.upi);
      params[PayUPaymentParamKey.vpa] = PayUTestCredentials.vpa;
      params[PayUPaymentParamKey.hashes] = {
        PayUPaymentParamKey.validate_vpa: vpaHash
      };
      var data = await payUUpiFlutter.validateVPA(params: params);
      showAlertDialog(context, "Validate VPA", "$data");
    }
  ```

  <Accordion title="Response" icon="fa-code">
    The sample response of a VPA validation request is similar to the following:

    ```json JSON
    {
      "status": "SUCCESS",
      "vpa": "9999999999@upi",
      "isVPAValid": 0,
      "payerAccountName": "PayUNeer",
      "isAutoPayVPAValid": 0,
      "isAutoPayBankValid": "NA"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 8: List the UPI apps" icon="fa-code">
  Initialise and launch the Flutter UPI SDK by calling the following code snippet to get the list of UPI apps installed on Android and iOS devices

  ```d Dart
    intentApps() async {
      var data = await payUUpiFlutter.intentApps();
      showAlertDialog(context, "intentApps", "$data");
    }
  ```

  <Accordion title="Response" icon="fa-code">
    Here is how a sample response of UPI list request looks like:

    ```json JSON
    {
      "data": {
        "value": "net.one97.paytm",
        "title": "Paytm"
      }
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="For IOS, UPI Intent (Mandatory)" icon="fa-code">
  For fetch the Installed UPI apps, Kindly add the query schemes in the`info.plist`:

  ```Text Info.plist Code for Intent
  	<key>LSApplicationQueriesSchemes</key>
  	<array>
  		<string>phonepe</string>
  		<string>tez</string>
      <string>gpay</string>
  		<string>paytm</string>
  		<string>bhim</string>
  		<string>credpay</string>
  	</array>
  ```

  <br />
</Accordion>

## Test the Integration and Go-Live

<Accordion title="Test the integration" icon="fa-code">
  After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

  > 🚧 Callout
  >
  > The UPI in-app and UPI intent flow is not available in the Test mode.

  > 👍 Testing checklist
  >
  > Things to remember while testing an integration:
  >
  > 1. To test the integration make sure that you are making a transaction call to the test endpoint.
  > 2. Use your test key and salt for the transaction requests. See [Genearate test key and salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
  > 3. Set the value of the `environment` parameters to `1`.

  You can make test payments using one of the payment methods configured at the Checkout.

  > 🚧 Watch Out!
  >
  > You must only use the Test merchant Key and Test Salt to carry out a test transaction.

  ***

  <TestCardsCallout />

  <Accordion title="Test credentials for supported payment methods" icon="fa-code">
    Following are the payment methods supported in PayU Test mode.

    <Accordion title="Test VPA for UPI" icon="fa-code">
      You can use either of the following VPAs to test your UPI-related integration:

      * [anything@payu](anything@payu)
      * [9999999999@payu.in](mailto:9999999999@payu.in)

      For Testing the UPI Collect flow, Please follow the below steps:- 

      1. Once you enter the VPA click on the verify button and proceed to pay.
      2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
      3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

      [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)\<Txn\_id>

      **For Android**

      You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

      > 🚧 Ensure to remove the code from the manifest file before going live.

      ```Text xml
      <application>
      <meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
      <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
      <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
      </appliction>
      ```
    </Accordion>

    <Accordion title="Test UPI Intent/InApp flow" icon="fa-code">
      > ❗️ Callout
      >
      > The UPI in-app and UPI intent flow is not available in the Test mode.

      <br />
    </Accordion>
  </Accordion>
</Accordion>

<Go_Live_Checklist />

## Sample app

The sample app for Flutter UPI SDK can be found in the following Github location:

[https://github.com/payu-intrepos/PayU-UPI-Flutter.git](https://github.com/payu-intrepos/PayU-UPI-Flutter.git)
