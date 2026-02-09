---
title: React Native UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native UPI SDK
  description: >-
    This document provides information on UPI transactions using React Native
    SDK, including the two types of transactions (Collect and Intent) and
    compatibility requirements for Android and iOS.
  keywords:
    - PayU India UPI SDK for React Native
    - PayU React Native UPI SDK
    - UPI SDK integration React Native
    - React Native UPI payment SDK
    - PayU UPI payment gateway
    - How to integrate PayU UPI SDK in React Native
    - PayU India UPI SDK for React Native apps
    - Guide to PayU UPI React Native SDK
    - PayU UPI payment gateway integration React Native
    - Step-by-step PayU UPI SDK React Native integration
  robots: index
next:
  description: ''
---
This cluster aims to document all the knowledge base for UPI transactions. Implementation of most of the UPI flows is different when compared to normal transactions.

There are broadly two types of UPI transactions, Collect and Intent(Pure Intent/In-App). For collect transactions, PayU informs the payment gateway to trigger a transaction to the app linked to the provided VPA, which asks the user for approval.

For intent transactions, we delegate the transaction process to an external app like BHIM, Google Pay, etc, which lets users transfer money to a VPA specified by us. After that, we use the PG (related to the specified VPA) for verification. PayU has a pre-configured VPA (distinct on the PG-Merchant level) on which the app makes the user pay the amount. To integrate UPI SDK with React Native, see Integrate UPI SDK with React Native.

> ❗️ Callout
>
> * To start transacting through Google Pay™, register your business on Google using the Google Onboarding form, In this registration process, you need to add the merchant VPAs created by PayU for you. In the case of multiple VPAs, all of them need to be registered with Google.
> * To enable Google Pay, contact your Point of Contact at Google. For any further queries or help with onboarding, send a mail to PayU Mobile Integration Team.

***

## Compatibility

### Android

* Min SDK Version: 21
* Compile SDK Version: 31+
* Kotlin 1.6.10

### iOS

* iOS version: 11

## SDK Integration

The React Native UPI SDK integration involves the following steps:

<Accordion title="Step 1: Installation" icon="fa-code">
  The PayU UPI SDK for React Native is offered through npm.

  <Tabs>
    <Tab title="Android">
      To add the PayU UPI plugin to your app run the following dependency in the root folder of your React native app:

      ```
      npm install payu-upi-react --save
      import PayUUPI from 'payu-upi-react'
      ```
    </Tab>

    <Tab title="iOS">
      Install the pod using the following command. Make sure your minimum deployment target is iOS 11.

      ```
      pod install
      ```

      ***
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 2: Build the payment parameters" icon="fa-code">
  To initiate a payment, your app needs to send transactional information to the UPI SDK. Build the payUPaymentParams object with the mandatory parameters as shown in the following code snippet:

  ```javascript React.js
   var payUPaymentParams = {
        payu_payment_params: {
          key: <String>, //merchant key 
          transaction_id: <String>, // i.e. new Date().getTime().toString()
          amount: <String>, // amount in Double format
          product_info: <String>,
          first_name: <String>,
          email: <String>,
          phone: <10 digit Numeric>,
          ios_surl: <String>,
          ios_furl: <String>,
          android_surl: <String>,
          android_furl: <String>,
          environment: <String>, // "1" for Stage,"0" for production
          isProduction: <Boolean>, //Set environment for android
          disable_intent_seamless_failure: <String>, // -1 | 0 
          merchant_response_timeout: <String>, //numeric time millis
          phone_pe_user_cache_enabled: <String>, // true | false
          beneficiary_account_number: <String> , //for TPV transaction
          beneficiary_ifsc: <String> , // for TPV transaction
          vpa: <String>, //virtual payment address for UPI (i.e. 1234567890@payu)
          post_url: <String>, // "https://secure.payu.in/_payment" for production, "https://test.payu.in/_payment" for Stage
          payment_mode: <String>, // for Intent flow use "INTENT", for collect flow use "upi"
          user_credentials: <String>, // unique user identifier
          package_name: <String>, //package name for the specific UPI intent (i.e. 			'net.one97.paytm') // package_name parameter used for Android only
          intent_app : <String>, //scheme name for the specific UPI intent (i.e. 'phonepe') // intent_app parameter used for IOS only
          hashes: {
            payment: <String>, // generated hash for payment
            validate_vpa: <String> // generated hash for validating virtual payment address
            },
          additional_param:{
            udf1: "user defined value 1",
            udf2: "user defined value 2",
            udf3: "user defined value 3",
            udf4: "user defined value 4",
            udf5: "user defined value 5",
           merchant_access_key:"", //This is for lookup API, optional
           source_id:"", //Sodexo source ID, optional 
        },
        si_params:{
          si_details:{
              billing_amount:"1.00",
              billing_currency:"INR",
              billing_cycle:"DAILY", // YEARLY | MONTHLY | WEEKLY | DAILY | ONCE | ADHOC
              billing_interval:"1",
              payment_end_date:"2023-12-24", // yyyy-mm-dd
              payment_start_date:"2022-12-24" // yyyy-mm-dd
              billing_limit:'ON',      //ON, BEFORE, AFTER
              billing_rule:'MAX',      //MAX, EXACT
            },
          is_free_trial:"0", // 1 | 0 (true | false) //Optional
          si:"1" //Mandatory
      }
    }
  }
  ```

  For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](doc:ios-standing-instructions-parameters).

  ***
</Accordion>

<Accordion title="Step 3: Generate payment hash" icon="fa-code">
  Generate the payment hash and pass the hash in the JSON `payUPaymentParams.hashes.payment` parameter or in `payUPaymentParams.hashes.validate_vpa `as shown below:

  ```javascript React.js
  {
    payu_payment_params: {
      hashes:{
        payment: <String>, // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
        validate_vpa: <String>, // hash for validating VPA sha512(key|<validateVPA>|vpa|salt)
      }
    }
  }
  ```

  For hash generation logic refer to [Generate Hash](doc:hash-generation-for-checkoutpro-sdk).

  <Callout icon="📘" theme="info">
    **Note**: You must always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
  </Callout>

  ***
</Accordion>

<Accordion title="Step 4: Payment request post data (Intent flow)" icon="fa-code">
  Build Mandatory parameters for UPI intent flow in JSON as shown in the code snippet below:

  ```javascript React.js
  var params={
    payu_payment_params: {
          key: <String>, //merchant key 
          transaction_id: <String>, // i.e. new Date().getTime().toString()
          amount: <String>, // amount in Double format
          product_info: <String>,
          first_name: <String>,
          email: <String>,
          phone: <10 digit Numeric>,
          ios_surl: <String>,
          ios_furl: <String>,
          android_surl: <String>,
          android_furl: <String>,
          environment: <String>, // "1" for Stage,"0" for production
          isProduction: <Boolean>, //Set environment for android
          payment_mode: <String>, // for Intent flow use "INTENT", for collect flow use "upi"
          user_credentials: <String>, // unique user identifier
          package_name: <String>, //package name for the specific UPI intent (i.e. 'net.one97.paytm') // package_name parameter used for Android only
          intent_app : <String>, //scheme name for the specific UPI intent (i.e. 'phonepe') // intent_app parameter used for IOS only
      hashes:{
        payment: <String> // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
      }
    }
  ```

  ***
</Accordion>

<Accordion title="Step 5: Payment request post data (Generic Intent flow)" icon="fa-code">
  <Callout icon="📘" theme="info">
    **Note**: Generic Intent Flow is only supported for Android
  </Callout>

  Build Mandatory parameters for generic intent flow in JSON as shown in the code snippet below:

  ```javascript React.js
  var params={
    payu_payment_params: {
          key: <String>, //merchant key 
          transaction_id: <String>, // i.e. new Date().getTime().toString()
          amount: <String>, // amount in Double format
          product_info: <String>,
          first_name: <String>,
          email: <String>,
          phone: <10 digit Numeric>,
          ios_surl: <String>,
          ios_furl: <String>,
          android_surl: <String>,
          android_furl: <String>,
          environment: <String>, // "1" for Stage,"0" for production
          isProduction: <Boolean>, //Set environment for android
          payment_mode: <String>, // for Intent flow use "INTENT", for collect flow use "upi"
          post_url: <String>, // "https://secure.payu.in/_payment" for production, "https://test.payu.in/_payment" for Stage
          user_credentials: <String>, // unique user identifier
      hashes:{
        payment: <String> // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
      }
    }
  ```

  ***
</Accordion>

<Accordion title="Step 6: Payment request post data (Collect flow)" icon="fa-code">
  Build Mandatory parameters for Collect flow in JSON as shown in the code snippet below:

  ```Text React.js
  var params={
    payu_payment_params: {
          key: <String>, //merchant key 
          transaction_id: <String>, // i.e. new Date().getTime().toString()
          amount: <String>, // amount in Double format
          product_info: <String>,
          first_name: <String>,
          email: <String>,
          phone: <10 digit Numeric>,
          ios_surl: <String>,
          ios_furl: <String>,
          android_surl: <String>,
          android_furl: <String>,
          vpa: <String>, //virtual payment address for UPI (i.e. 1234567890@payu)
          environment: <String>, // "1" for Stage,"0" for production
          isProduction: <Boolean>, //Set environment for android
          payment_mode: <String>, // for Intent flow use "INTENT", for collect flow use "upi"
          post_url: <String>, // "https://secure.payu.in/_payment" for production, "https://test.payu.in/_payment" for Stage
          user_credentials: <String>, // unique user identifier
      hashes:{
        payment: <String>, // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  			validate_vpa: <String> // hash for validating virtual payment address -  sha512(key|command|var1|salt)
      }
    }
  ```

  ***
</Accordion>

<Accordion title="Step 7: Make payment" icon="fa-code">
  <Accordion title="Launch with Activity" icon="fa-code">
    Use the code snippet mentioned below to make the payment:

    ```Text React.js
    PayUUPI.makeUPIPayment(params,
          (error) => {
            //Failure or error response
          },
          (result) => {
            //success response
          }
        );
    ```
  </Accordion>

  <Accordion title="Launch with Fragment" icon="fa-code">
    Use the code snippet mentioned below to make the payment:

    ```Text React Native
    PayUUPI.makeUPIPaymentSeamless(params,
          (error) => {
            //Failure or error response
          },
          (result) => {
            //success response
          }
        );
    ```

    ***
  </Accordion>
</Accordion>

<Accordion title="Step 8: VPA validation" icon="fa-code">
  Initialise and launch the React Native UPI SDK by calling the following code snippet to validate the VPA:

  ```Text React
  PayUUPI.validateVPA(
        params,
        (error) => {
         //Failure or error response
        },
        (params) => {
          //success response
        }
      );
  ```

  <Accordion title="Response" icon="fa-code">
    The sample response of a VPA validation request is similar to the following:

    ```json JSON
    {
      "status": "SUCCESS",
      "vpa": "1234567890@payu",
      "isVPAValid": 0,
      "payerAccountName": "PayUNeer",
      "isAutoPayVPAValid": 0,
      "isAutoPayBankValid": "NA"
    }
    ```

    ***
  </Accordion>
</Accordion>

<Accordion title="Step 9: List the UPI apps" icon="fa-code">
  Initialise and launch the UPI SDK by calling the following code snippet to get the list of UPI apps installed on Android and iOS devices:

  ```javascript React.js
  PayUUPI.intentApps((intentApps) => {
          //list of installed UPI Apps
        });
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

  <Accordion title="For IOS, UPI Intent (Mandatory)" icon="fa-code">
    For fetch the Installed UPI apps, Kindly add the query schemes in the`info.plist`:

    ```Text Info.plist Code for Intent
    	<key>LSApplicationQueriesSchemes</key>
    	<array>
    		<string>phonepe</string>
    		<string>tez</string>
    		<string>paytm</string>
    		<string>bhim</string>
    		<string>credpay</string>
    	</array>
    ```
  </Accordion>
</Accordion>

## Test the Integration and Go-Live

<Accordion title="Test the Integration" icon="fa-gear">
  <ReactNative_Test_the_Integration />
</Accordion>

<Accordion title="Go-live Checklist" icon="fa-gear">
  <ReactNative_Go_Live />
</Accordion>

## Sample app

The sample application for integration with React-Native UPI SDK :
[https://github.com/payu-intrepos/payu-core-pg-react.git](https://github.com/payu-intrepos/payu-core-pg-react.git)
