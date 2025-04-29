---
title: Android Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native Checkout Pro SDK for Android Integration
  description: >-
    This document provides a step-by-step guide on integrating React Native
    Checkout Pro mobile SDK for Android, including setting up payment hashes,
    building payment parameters, initiating payments, handling payment
    completion, and customization options.
  keywords:
    - React Native with Android Checkout Pro SDK Integration Steps
    - PayU React Native with Android SDK integration steps
    - Mobile payment integration with PayU React Native with Android SDK steps
    - PayU React Native with Android Checkout Pro set up for Mobile
    - React Native with Android CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile React Native with Android SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
To integrate with the CheckoutPro mobile SDK for Android: 

* Include the SDK in your app project​
* ​Set up the payment hashes​
* ​Build the payment parameters​
* ​Initiate the payment​
* ​Handle the payment completion​
* Customization

## Step 1: Include the SDK in your app project

The CheckoutPro SDK is offered through npm. 

Add the following entries to include CheckoutPro SDK in your app:

```
npm install payu-non-seam-less-react --save
react-native link payu-non-seam-less-react
```

Add the following imports in the class where you need to initiate a payment:

```Text React
import PayUBizSdk from 'payu-non-seam-less-react';
```

***

## Step 2: Set up payment hashes

This step describes how to pass the static and dynamic hashes. For detailed information, refer to [Hash Generation](doc:generate-dynamic-hash-react).

### Pass Static Hashes

To pass static hashes during integration, use the following code snippet:

```Text React
var payUPaymentParams = {
    key: "Merchant key",
    ...
    ...
    ...
    additionalParam: {
        payment_related_details_for_mobile_sdk: "payment_related_details_for_mobile_sdk hash",
        vas_for_mobile_sdk: "vas_for_mobile_sdk hash",
        payment: "Payment Hash"
    }
}
```

### Passing dynamic hashes

To pass dynamic hashes, the merchant will receive a call on the generateHash method. In the method parameter, you will receive a dictionary or hashMap, then extract the value of hashString from that. Pass that value to the server to append the Salt at the end and generate the sha512 hash over it. The server gives that hash back to your app, and the app will pass that hash to PayU through a callback mechanism. For passing dynamic hashes during integration, use the following code snippet:

```Text React
generateHash = (e) => {
    console.log(e.hashName);
    console.log(e.hashString);
    var hashStringWithoutSalt = e.hashString;
    var hashName = e.hashName;
	  var postSalt = e.postSalt; // compulsory for Additional Charges and Split Payment
// Pass hashStringWithoutSalt to server
// Server will append salt at the end and generate sha512 hash over it
//  "<create SHA -512 hash of 'hashString+salt+postSalt'>"
    var hashValue = "<Set hash here which is fetched from server>";
    var result = { [hashName]: hashValue };
    PayUBizSdk.hashGenerated(result);
}
```

***

## Step 3: Build the payment parameters

To initiate a payment, your app needs to send transactional information to the Checkout Pro SDK.

### Payment parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Key
        `mandatory`
      </td>

      <td>
        `String` This parameter must contain your merchant key received from PayU.
      </td>
    </tr>

    <tr>
      <td>
        transactionId\
        `mandatory`
      </td>

      <td>
        `String` It should be unique for each transaction.\
        Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "\_,$,%,&, etc"
      </td>
    </tr>

    <tr>
      <td>
        Amount\
        `mandatory`
      </td>

      <td>
        `String` Total transaction amount.
      </td>
    </tr>

    <tr>
      <td>
        productInfo\
        `mandatory`
      </td>

      <td>
        `String` Information about the product.
      </td>
    </tr>

    <tr>
      <td>
        firstName\
        `mandatory`
      </td>

      <td>
        `String` Customer’s first name
      </td>
    </tr>

    <tr>
      <td>
        Email\
        `mandatory`
      </td>

      <td>
        `String` Customer’s email id
      </td>
    </tr>

    <tr>
      <td>
        Phone\
        `mandatory`
      </td>

      <td>
        `String` Customer’s phone number. **Max character limit** : 10 Digits
      </td>
    </tr>

    <tr>
      <td>
        ios\_surl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.  

        * \*Note\*\*: This field is applicable for iOS integration
      </td>
    </tr>

    <tr>
      <td>
        ios\_furl\
        mandatory
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.  

        * \*Note\*\*: This field is applicable for iOS integration
      </td>
    </tr>

    <tr>
      <td>
        android\_surl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.\
        `Note`: This field is applicable for Android integration  

        * \*Sample URL\*\*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
      </td>
    </tr>

    <tr>
      <td>
        android\_furl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction gets fail, PayU will load this url and pass transaction response.\
        When the transaction gets success, PayU will load this url and pass transaction response.\
        `Note`: This field is applicable for Android integration  

        * \*Sample URL\*\*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
      </td>
    </tr>

    <tr>
      <td>
        Environment\
        `mandatory`
      </td>

      <td>
        `String` Environment of SDK
      </td>
    </tr>

    <tr>
      <td>
        User Credential\
        `mandatory`
      </td>

      <td>
        * \*String\*\* This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:\
          `<merchantKey>:<userId>  `\
          Here,\
          UserId is any id/email/phone number to uniquely identify the user.
      </td>
    </tr>

    <tr>
      <td>
        user\_token\
        `mandatory`
      </td>

      <td>
        String The use for this param is to allow the offer engine to apply velocity rules at a user level.  

        -**Card Based Offers (CC, DC, EMI):**&#x46;or card payment mode offers, if this parameter is passed then the velocity rules would be applied on this token, if not passed the same would be applied to the card number.  

        \-**NB, Wallet:** It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.\
        Note:- When we use Offer features then it's a mandatory parameter otherwise it's not required.
      </td>
    </tr>

    <tr>
      <td>
        additionalCharges
      </td>

      <td>
        String\
        This parameter is required if merchant want to take additional charge from user,	should be string with PG:Amount or IBIBOCode:Amount\
        Sample : CC:10,NB:20,SBIB:15
      </td>
    </tr>

    <tr>
      <td>
        percentageAdditionalCharges
      </td>

      <td>
        String\
        This parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable,\
        should be string with PG:Amount or IBIBOCode:Amount\
        Sample : CC:100,NB:50,SBIB:25
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> The sample URLs mentioned in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.

For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).

### Additional parameters (Optional)

The additional parameters that are optional that can be passed to SDK are udf parameters, static hashes, and other parameters. For more details on Static Hash generation and passing them, refer to [generate hashes](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk). The following is a list of parameters that can be passed in additional parameters:

| Parameter                                   | Description                                                                                                                                                                         |
| :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PayUCheckoutProConstants.CP\_UDF1           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
| PayUCheckoutProConstants.CP\_UDF2           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
| PayUCheckoutProConstants.CP\_UDF3           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
| PayUCheckoutProConstants.CP\_UDF4           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
| PayUCheckoutProConstants.CP\_UDF5           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
| Static hashes                               | `String` The static hashes is specified in this parameter. For more information, refer to [Hash Generation](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) section. |
| PayUCheckoutProConstants.SODEX\_OSOURC\_EID | `String` Sodexo Source ID, Merchant can store it from the third field of PayU response.                                                                                             |
| PaymentParamConstant.walletUrn              | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account.                                                                                  |

## For split Payments details (Optional)

For a split payment transaction, create a JSON string with the split payment parameters as shown below:

JSON Request Structure of splitInfo Field\
Here is a sample JSON structure for the splitPaymentDetails field:

```
{  
   "type":"absolute",  
   "splitInfo":{  
      "P**\*_Y":{  
         "aggregatorSubTxnId":"9a70ea0155268101001ba",  
         "aggregatorSubAmt":"50",  
         "aggregatorCharges":"20"  
      },  
      "P_**K":{  
         "aggregatorSubTxnId":"9a70ea0155268101001bb",  
         "aggregatorSubAmt":"30"  
      }  
   }  
}
```

Then create an object of the PayUPaymentParam class and set the splitPaymentDetails property of the object to the JSON string you created in the earlier step.

```
splitPaymentDetails = '<pass the splitPayment Json Data>';
```

Kindly refer to the below link for more details about the [Split During Transaction](https://docs.payu.in/reference/split-during-transaction-using-_payment)

The payment parameters and additional parameters can be passed using the following code snippet:

```Text React.js
var payUPaymentParams = {
    key: "Merchant key",
    transactionId: "Transaction Id",
    amount: "Transaction amount",
    productInfo: "product Info",
    firstName: "Customer firstName",
    email: "Customer email",
    phone: "Customer phone",
    ios_surl: "Success Url for iOS",
    ios_furl: "Failure Url for iOS",
    android_surl: "Success Url for Android",
    android_furl: "Failure Url for Android",
    environment: "0 or 1",//<0 for Production/1 for Staging>
    userCredential: "key:CustomerID",
    userToken: "<pass the User Token>", //Optional, Only use for Offer
    additionalCharges:"CC:10,NB:20,SBIB:15", //Optional, Only use if want to take addional charges from user
    percentageAdditionalCharges:"CC:10,NB:20,SBIB:15", //Optional, Only use if want to take addional charges dynamically from user
    additionalParam: {
        udf1: "user defined value 1",
        udf2: "user defined value 2",
        udf3: "user defined value 3",
        udf4: "user defined value 4",
        udf5: "user defined value 5",
        payment_related_details_for_mobile_sdk: "payment_related_details_for_mobile_sdk hash",
        vas_for_mobile_sdk: "vas_for_mobile_sdk hash",
        payment: "Payment Hash",
        walletUrn: "<walletUrn>"
    },
    splitPaymentDetails: splitPaymentData, // //Optional, Only use for Split Payment
    payUSIParams: {
      isFreeTrial:true,
    	billingAmount:'10',
    	billingInterval:'1',
    	paymentStartDate:'2023-04-20',
    	paymentEndDate:'2023-04-30',
      billingCycle:"DAILY", //Can be any of  YEARLY | MONTHLY | WEEKLY | DAILY | ONCE | ADHOC
    	remarks:'Test SI transcaction',
    	billingCurrency:'INR'
    }
}
```

For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).

***

## Step 4: Initiate the payment

Initialize and launch the Checkout Pro SDK by calling the following code snippet:

```Text React.js
var paymentObject = {
payUPaymentParams: payUPaymentParams,
// payUCheckoutProConfig is optional
// Detail can be found in latter section
payUCheckoutProConfig: payUCheckoutProConfig
}
PayUBizSdk.openCheckoutScreen(paymentObject);
```

***

## Step 5: Complete the payment

To get the callbacks for payment-related statuses, create a NativeEventEmitter object and subscribe to the following events.

```Text React.js
import { NativeEventEmitter } from 'react-native';
//Register event emitters here.
componentDidMount() {
const eventEmitter = new NativeEventEmitter(PayUBizSdk);
this.paymentSuccess = eventEmitter.addListener('onPaymentSuccess', this.onPaymentSuccess);
this.paymentFailure = eventEmitter.addListener('onPaymentFailure', this.onPaymentFailure);
this.paymentCancel = eventEmitter.addListener('onPaymentCancel', this.onPaymentCancel);
this.error = eventEmitter.addListener('onError', this.onError);
this.generateHash = eventEmitter.addListener('generateHash', this.generateHash);
}
onPaymentSuccess = (e) => {
console.log(e.merchantResponse);
console.log(e.payuResponse);
}
onPaymentFailure = (e) => {
console.log(e.merchantResponse);
console.log(e.payuResponse);
}
onPaymentCancel = (e) => {
console.log('onPaymentCancel isTxnInitiated -' + e);
}
onError = (e) => {
console.log(e);
}
generateHash = (e) => {
console.log(e.hashName);
console.log(e.hashString);
var hashStringWithoutSalt = e.hashString;
var hashName = e.hashName;
var postSalt = e.postSalt; // compulsory for Additional Charges and Split Payment
// Pass hashStringWithoutSalt to server
// Server will append salt at the end and generate sha512 hash over it
//  "<create SHA -512 hash of 'hashString+salt+postSalt'>"
var hashValue = "<Set hash here which is fetched from server>";
var result = { [hashName]: hashValue };
PayUBizSdk.hashGenerated(result);
}
//Do remember to unregister eventEmitters here
componentWillUnmount() {
this.paymentSuccess.remove();
this.paymentFailure.remove();
this.paymentCancel.remove();
this.error.remove();
this.generateHash.remove();
}
```

***

## Step 6: Customization (Optional)

### Build.gradle

```Text React.js
allprojects {
    repositories {
        maven {
            url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android"
        }
    }
}
```

### AndroidManifest.xml

To automatically fill OTP on bank pages, SDK requires the **RECEIVE\_SMS** permission so kindly add the same in your `AndroidManifest.xml` like below.

```Text XML
<uses-permission android:name="android.permission.RECEIVE_SMS" />
```
