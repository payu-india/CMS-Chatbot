---
title: React Native Custom Browser SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native Customer Browser SDK
  description: >-
    This document provides instructions on integrating Custom Browser SDK with
    React Native, including features like OTP assist and bank page
    optimizations, with compatibility for Android and iOS.
  keywords:
    - React Native Custom Browser SDK
    - PayU React Native SDK integration
    - Mobile payment integration with PayU React Native SDK
    - PayU React Native Custom Browser setup for Mobile
    - Custom Browser SDK for React Native
    - ' React Native CB SDK'
    - PayU React Native SDK integration
    - PayU React Native CB setup for Mobile
    - Custom Browser SDK for React Native
  robots: index
next:
  description: ''
---
This document describes how to integrate Custom Browser SDK with React Native. To integrate Custom Browser SDK with React Native, see Integrate Custom Browser SDK with React Native.

> 🚧 Watch Out!
>
> React Native Custom Browser SDK has dependancy on React Native Core SDK. See React Native Core SDK to learn more.

## Features

**OTP assist**: This feature helps you automatically read OTP messages on bank pages to ease the payment experience.
**Bank Page Optimization**: PayU optimizes bank pages for a good payment experience.

## Compatibility

### Android

* Min SDK Version: 21
* Compile SDK Version: 31
* Kotlin 1.6.10

### iOS

* iOS version 11

The React Native Custom Browser SDK integration involves the following steps:

## SDK Installation

<Accordion title="Step 1: Installation" icon="fa-code">
  The PayU Custom Browser SDK for React Native is offered through NPM:

  <Tabs>
    <Tab title="Android">
      To add the PayU CB plugin to your app run the following dependency in the root folder of your React native app:

      ```
      npm install payu-custom-browser-react
      import CBWrapper from  'payu-custom-browser-react'; 
      ```
    </Tab>

    <Tab title="iOS">
      Install the pod using the following command. Make sure your minimum deployment target is iOS 11.

      ```
      pod install
      ```
    </Tab>
  </Tabs>

  <br />
</Accordion>

<Accordion title="Step 2: Build the payment parameters" icon="fa-code">
  To initiate a payment, your app needs to send transactional information to the Custom Browser SDK. Build the payUPaymentParams object with the mandatory parameters as shown in the following code snippet:

  <Accordion title="Sample code" icon="fa-code">
    ```javascript React.js
    var payUPaymentParams = {
          payu_payment_params: {
            key: <String>, //merchant key (Mandatory)
            transaction_id: new Date().getTime().toString(), //Mandatory
            cb_config:{
              url: <String>,  //Mandatory (This can be generated using PayU Core PG SDK)
              post_data: <String>, //Mandatory (This can be generated using PayU Core PG SDK)
              view_port_wide_enable : <String>, // "true","false"
              auto_approve: <String>, // "true","false"
              auto_select_otp: <String>, // "true","false"
              internet_restored_window_ttl: <String>, //numeric
              sms_permission: <String >, // "true","false"
              html_data: <String>,
              disable_intentseamless_failure: <String>, //numeric
              disable_backbutton_dialog: <String>, // "true","false"
              enable_ssl_dialog: <String>,// "true","false"
              email: <String>,
              first_name: <String>,
              last_name: <String>,
              package_name_for_specific_app: <String>,
              payment_type: <String>,
              phone_pe_user_cache_enabled: <String>, //numeric
              merchant_response_timeout: <String>, //numeric
          }
        }
      }
    }
    ```
  </Accordion>

  For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/ios-standing-instructions-parameters).
</Accordion>

<Accordion title="Step 3: Generate payment hash" icon="fa-code">
  For hash generation testing salt needs to be put in the HASH generation method. For more information, refer to [Generate Hash](doc:generate-dynamic-hash-react).

  <Callout icon="📘" theme="info">
    **Note**: Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
  </Callout>
</Accordion>

<Accordion title="Step 4: Make payment" icon="fa-code">
  Use the code snippet mentioned below to make the payment:

  <Accordion title="Sample code" icon="fa-code">
    ```javascript React.js
    CBWrapper.openCB(
    Request Data <Map>, //payment params defined above
          (error) => {
            console.log("-----------Error Callback---------");
            console.log(error);
            console.log("------------------------------------");
          },
          (payuResponse) => {
           
            console.log("-----------Success Callback---------");
            console.log(payuResponse);
            console.log("--------------------------------------");
          }
      );
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 5: Register listeners" icon="fa-code">
  Register Listener (in this case) Emitter to get the Response from Custom Browser SDK:

  <Accordion title="Sample code" icon="fa-code">
    ```javascript React.js
    import {NativeEventEmitter} from 'react-native';
    const eventEmitter=new NativeEventEmitter(CBWrapper);
    eventEmitter.addListener("CBListener",(event)=>{
         
        })
    ```
  </Accordion>

  <Accordion title="Response" icon="fa-code">
    ```json JSON
    {
      "eveneType": <String>, (onPaymentFailure | onPaymentTerminate | onPaymentTerminate | onCBErrorReceived | onBackButton | onBackApprove | onBackDismiss)
      "payuResult": <String>, //conditional
      "merchantResponse": <String>, //conditional
      "errorMessage":<String>,
      "errorCode": <String>, //conditional
    }
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
The sample application for integration with React-Native CustomBrowser SDK :
[https://github.com/payu-intrepos/payu-core-pg-react.git](https://github.com/payu-intrepos/payu-core-pg-react.git)