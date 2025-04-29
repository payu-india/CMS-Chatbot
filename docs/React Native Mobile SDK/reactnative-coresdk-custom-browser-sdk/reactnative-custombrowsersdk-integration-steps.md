---
title: 1. SDK Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: SDK Integration for React Native Customer Browser
  description: >-
    The React Native Custom Browser SDK integration involves installing the SDK,
    building payment parameters, generating a payment hash, making a payment,
    and registering listeners to handle responses.
  keywords:
    - SDK Integration for React Native Customer Browser
    - '  React Native Customer Browser SDK Integration'
    - Customer Browser SDK Integration for React Native
  robots: index
next:
  description: ''
---
The React Native Custom Browser SDK integration involves the following steps:

1. [Installation](https://docs.payu.in/docs/reactnative-custombrowsersdk-integration-steps#step-1-installation)
2. [Build the payment parameters](https://docs.payu.in/docs/reactnative-custombrowsersdk-integration-steps#step-2-build-the-payment-parameters)
3. [Generate payment hash](https://docs.payu.in/docs/reactnative-custombrowsersdk-integration-steps#step-3-generate-payment-hash)
4. [Make payment](https://docs.payu.in/docs/reactnative-custombrowsersdk-integration-steps#step-4-make-payment)
5. [Register listeners](https://docs.payu.in/docs/reactnative-custombrowsersdk-integration-steps#step-5-register-listeners)

## Step 1: Installation

The PayU Custom Browser SDK for React Native is offered through NPM:

**For Android**: To add the PayU CB plugin to your app run the following dependency in the root folder of your React native app:

```
npm install payu-custom-browser-react
import CBWrapper from  'payu-custom-browser-react'; 
```

**For iOS**: Install the pod using the following command.  Make sure your minimum deployment target is iOS 11.

```
pod install
```

***

## Step 2: Build the payment parameters

To initiate a payment, your app needs to send transactional information to the Custom Browser SDK. Build the payUPaymentParams object with the mandatory parameters as shown in the following code snippet:

```Text React.js
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

For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/ios-standing-instructions-parameters).

***

## Step 3: Generate payment hash

For hash generation testing salt needs to be put in the HASH generation method. For more information, refer to [Generate Hash](doc:generate-dynamic-hash-react).

> 📘 Remember
> 
> Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.

***

## Step 4: Make payment

Use the code snippet mentioned below to make the payment:

```Text React.js
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

***

## Step 5: Register listeners

Register Listener (in this case) Emitter to get the Response from Custom Browser SDK:

```Text React.js
import {NativeEventEmitter} from 'react-native';
const eventEmitter=new NativeEventEmitter(CBWrapper);
eventEmitter.addListener("CBListener",(event)=>{
     
    })
```

### Response

```Text JSON
{
  "eveneType": <String>, (onPaymentFailure | onPaymentTerminate | onPaymentTerminate | onCBErrorReceived | onBackButton | onBackApprove | onBackDismiss)
  "payuResult": <String>, //conditional
  "merchantResponse": <String>, //conditional
  "errorMessage":<String>,
  "errorCode": <String>, //conditional
}
```