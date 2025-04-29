---
title: 1. SDK Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native UPI SDK Integration Steps
  description: >-
    The document provides steps for installing the PayU UPI SDK for React
    Native, building payment parameters, generating payment hash, making payment
    requests for Intent flow, Generic Intent flow, and Collect flow, as well as
    validating VPA and listing UPI apps.
  keywords:
    - PayU UPI SDK integration steps
    - PayU India UPI SDK integration steps
    - ' React Native UPI SDK integration steps'
    - ' UPI SDK integration steps'
    - ' How to integrate PayU UPI SDK in React Native'
    - Step-by-step PayU UPI SDK integration
    - PayU UPI SDK integration steps for React Native apps
    - Detailed steps for PayU UPI SDK integration
  robots: index
next:
  description: ''
---
The React Native UPI SDK integration involves the following steps:

1. [Installation](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-1-installation)
2. [Build the payment parameters](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-2-build-the-payment-parameters)
3. [Generate payment hash](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-3-generate-payment-hash)
4. [Payment request post data (Intent flow)](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-4-payment-request-post-data-intent-flow)
5. [Payment request post data (Generic Intent flow)](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-5-payment-request-post-data-generic-intent-flow)
6. [Payment request post data (Collect flow)](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-6-payment-request-post-data-collect-flow)
7. [Make payment](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-7-make-payment)
8. [VPA validation](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-8-vpa-validation)
9. [List the UPI apps](https://docs.payu.in/docs/reactnative-upisdk-integration-steps#step-9-list-the-upi-apps)

## Step 1: Installation

The PayU UPI SDK for React Native is offered through npm.

**For Android**: To add the PayU UPI plugin to your app run the following dependency in the root folder of your React native app:

```
npm install payu-upi-react --save
import PayUUPI from 'payu-upi-react'
```

**For iOS:** Install the pod using the following command. Make sure your minimum deployment target is iOS 11.

```
pod install
```

***

## Step 2: Build the payment parameters

To initiate a payment, your app needs to send transactional information to the UPI SDK. Build the payUPaymentParams object with the mandatory parameters as shown in the following code snippet:

```text React
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

For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/ios-standing-instructions-parameters).

***

## Step 3: Generate payment hash

Generate the payment hash and pass the hash in the JSON `payUPaymentParams.hashes.payment` parameter or in `payUPaymentParams.hashes.validate_vpa `as shown below:

```Text React.js
{
  payu_payment_params: {
    hashes:{
      payment: <String>, // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
      validate_vpa: <String>, // hash for validating VPA sha512(key|<validateVPA>|vpa|salt)
    }
  }
}
```

For hash generation logic refer to G[enerate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk).

> 📘 Remember
>
> You must always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.

***

## Step 4: Payment request post data (Intent flow)

Build Mandatory parameters for UPI intent flow in JSON as shown in the code snippet below:

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
        environment: <String>, // "1" for Stage,"0" for production
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

## Step 5: Payment request post data (Generic Intent flow)

> 📘 Generic Intent Flow is only supported for Android

Build Mandatory parameters for generic intent flow in JSON as shown in the code snippet below:

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
        environment: <String>, // "1" for Stage, "0" for production
        payment_mode: <String>, // for Intent flow use "INTENT", for collect flow use "upi"
        post_url: <String>, // "https://secure.payu.in/_payment" for production, "https://test.payu.in/_payment" for Stage
        user_credentials: <String>, // unique user identifier
    hashes:{
      payment: <String> // hash for payment sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
    }
  }
```

***

## Step 6: Payment request post data (Collect flow)

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
        environment: <String>, // "1" for Stage, "0" for production
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

## Step 7: Make payment

### (Launch with Activity)

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

### (Launch with Fragment)

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

## Step 8: VPA validation

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

### Response

The sample response of a VPA validation request is similar to the following:

```Text JSON
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

## Step 9: List the UPI apps

Initialise and launch the UPI SDK by calling the following code snippet to get the list of UPI apps installed on Android and iOS devices:

```Text React.js
PayUUPI.intentApps((intentApps) => {
        //list of installed UPI Apps
      });
```

### Response

Here is how a sample response of UPI list request looks like:

```Text JSON
{
  "data": {
    "value": "net.one97.paytm",
    "title": "Paytm"
  }
}
```

### For IOS, UPI Intent (Mandatory)

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
