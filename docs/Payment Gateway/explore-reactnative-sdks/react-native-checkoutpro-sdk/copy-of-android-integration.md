---
title: Copy of Android Integration
deprecated: false
hidden: true
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
---
This section describes how to integrate React Native with Android Checkout Pro SDK.

## 🔴 IMPORTANT NOTICE - React Native 0.82.0+ Users

<Callout icon="❗️" theme="error">
  **Breaking Change for React Native 0.82.0 and Above**

  If you are using **React Native version 0.82.0 or above**, or planning to upgrade your SDK, you **MUST** use the new `makeHttpRequest` method for hash generation.

  The traditional `fetch` or other HTTP methods will **NOT work** with React Native 0.82.0+.
</Callout>

<Accordion title="New Hash Generation Method (React Native >= 0.82.0)" icon="fa-exclamation-triangle">
  For React Native version **0.82.0 and above**, you must use the `PayUBizSdk.makeHttpRequest` method inside the `generateHash` callback:

  ```javascript React Native
  generateHash = async (e) => {
      var hashStringWithoutSalt = e.hashString;
      var hashName = e.hashName;
      var postSalt = e.postSalt;  // Compulsory for Additional Charges and Split Payment
      
      try {
          // Prepare request body
          const rawBody = JSON.stringify({
              hashString: hashStringWithoutSalt,
              postSalt: postSalt
          });
          
          // Prepare headers
          const headers = {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer YOUR_API_TOKEN'  // If required
          };
          
          // NEW METHOD - Use PayUBizSdk.makeHttpRequest
          var response = await PayUBizSdk.makeHttpRequest(
              "https://yourserver.com/generate-hash",  // API URL
              "POST",                                    // Method Type
              rawBody,                                   // Body
              headers                                    // Headers
          );
          
          console.log('Raw Response:', response);
          
          // Parse the JSON response
          const parsedResponse = typeof response === 'string' 
              ? JSON.parse(response) 
              : response;
          
          var hashValue = parsedResponse.hash;
          var result = { [hashName]: hashValue };
          
          // Return hash to SDK
          PayUBizSdk.hashGenerated(result);
          
      } catch (error) {
          console.error('Hash generation error:', error);
      }
  };
  ```

  <Callout icon="📘" theme="info">
    **For React Native versions below 0.82.0**, you can continue using the standard `fetch` approach. See detailed implementation in Step 5 below.
  </Callout>
</Accordion>

<Callout icon="👍" theme="okay">
  **Why This Change?**

  * Required for compatibility with React Native 0.82.0+
  * Ensures network requests work correctly in newer React Native versions
</Callout>

***

## SDK Integration

To integrate with the CheckoutPro mobile SDK for Android:

  <Accordion title="Step 1: Include the SDK in your app project" icon="fa-code">
    The CheckoutPro SDK is offered through npm.

    Add the following entries to include CheckoutPro SDK in your app:

    <Accordion title="Install the SDK" icon="fa-code">
      ```
      npm install payu-non-seam-less-react --save
      react-native link payu-non-seam-less-react
      ```
    </Accordion>

    <Accordion title="Import the SDK in your payment component" icon="fa-code">
      Add the following imports in the class where you need to initiate a payment:

      ```Text React
      import PayUBizSdk from 'payu-non-seam-less-react';
      ```
    </Accordion>

    <Accordion title="Update Root build.gradle" icon="fa-code">
      Add the repository details for SDK dependencies under `allprojects` in `android/build.gradle`::

      ```
      allprojects {
        repositories {
          maven {
          url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android"
          }
        }
      }
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Step 2: Build the payment parameters" icon="fa-code">
    To initiate a payment, your app needs to send transactional information to the Checkout Pro SDK.

    <Accordion title="Payment parameters" icon="fa-code">
      <Table align={["left","left"]}>
        <thead>
          <tr>
            <th style={{ textAlign: "left" }}>
              Parameter
            </th>

            <th style={{ textAlign: "left" }}>
              Description
            </th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td style={{ textAlign: "left" }}>
              Key
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` This parameter must contain your merchant key received from PayU.
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              transactionId
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` It should be unique for each transaction.
              Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "\_,$,%,&, etc"
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              Amount
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Total transaction amount.
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              productInfo
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Information about the product.
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              firstName
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Customer's first name
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              Email
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Customer's email id
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              Phone
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Customer's phone number. **Max character limit** : 10 Digits
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              ios\_surl
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.

              * *Note*\*: This field is applicable for iOS integration
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              ios\_furl
              mandatory
            </td>

            <td style={{ textAlign: "left" }}>
              `String` When the transaction fails, PayU will load this URL and pass the transaction response.

              * *Note*\*: This field is applicable for iOS integration
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              android\_surl
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.
              `Note`: This field is applicable for Android integration

              * *Sample URL*\*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              android\_furl
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` When the transaction gets fail, PayU will load this url and pass transaction response.
              When the transaction gets success, PayU will load this url and pass transaction response.
              `Note`: This field is applicable for Android integration

              * *Sample URL*\*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              Environment
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              `String` Environment of SDK
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              User Credential
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              * *String*\* This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:
                `<merchantKey>:<userId>  `
                Here,
                UserId is any id/email/phone number to uniquely identify the user.
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              user\_token
              `mandatory`
            </td>

            <td style={{ textAlign: "left" }}>
              String The use for this param is to allow the offer engine to apply velocity rules at a user level.

              -\*\*Card Based Offers (CC, DC, EMI):\*\*For card payment mode offers, if this parameter is passed then the velocity rules would be applied on this token, if not passed the same would be applied to the card number.

              -**NB, Wallet:** It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
              Note:- When we use Offer features then it's a mandatory parameter otherwise it's not required.
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              additionalCharges
            </td>

            <td style={{ textAlign: "left" }}>
              String
              This parameter is required if merchant want to take additional charge from user,	should be string with PG:Amount or IBIBOCode:Amount
              Sample : CC:10,NB:20,SBIB:15
            </td>
          </tr>

          <tr>
            <td style={{ textAlign: "left" }}>
              percentageAdditionalCharges
            </td>

            <td style={{ textAlign: "left" }}>
              String
              This parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable,
              should be string with PG:Amount or IBIBOCode:Amount
              Sample : CC:100,NB:50,SBIB:25
            </td>
          </tr>
        </tbody>
      </Table>

      > 📘 Note:
      >
      > The sample URLs mentioned in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.

      For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).
    </Accordion>

    <Accordion title="Additional parameters (Optional)" icon="fa-code">
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
    </Accordion>

    <Accordion title="For split Payments details (Optional)" icon="fa-code">
      For a split payment transaction, create a JSON string with the split payment parameters as shown below:

      JSON Request Structure of splitInfo Field
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
    </Accordion>
  </Accordion>

  <Accordion title="Step 3: Initiate the payment" icon="fa-code">
    Initialize and launch the Checkout Pro SDK by calling the following code snippet:

    ```javascript React.js
    var paymentObject = {
    payUPaymentParams: payUPaymentParams,
    // payUCheckoutProConfig is optional
    // Detail can be found in latter section
    payUCheckoutProConfig: payUCheckoutProConfig
    }
    PayUBizSdk.openCheckoutScreen(paymentObject);
    ```

    ***
  </Accordion>

  <Accordion title="Step 4: Handle Payment Completion (Callbacks)" icon="fa-code">
    To get the callbacks for payment-related statuses, create a NativeEventEmitter object and subscribe to the following events.

    ```javascript React.js
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

    ***
  </Accordion>

  <Accordion title="Step 5: Generate Hash (Dynamic Hash Generation)" icon="fa-code">
    This step describes how to pass the dynamic hashes. For detailed information, refer to [Hash Generation](doc:generate-dynamic-hash-react).

    <Accordion title="Passing dynamic hashes" icon="fa-code">
      To pass dynamic hashes, the merchant will receive a call on the generateHash method. In the method parameter, you will receive a dictionary or hashMap, then extract the value of hashString from that. Pass that value to the server to append the Salt at the end and generate the sha512 hash over it. The server gives that hash back to your app, and the app will pass that hash to PayU through a callback mechanism. For passing dynamic hashes during integration, use the following code snippet:

      ```javascript React.js
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
    </Accordion>
  </Accordion>

  <Callout icon="📘" theme="info">
    **Notes:**

    * Always generate hashes on your backend.
    * URLs like [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success) are placeholders; replace with your backend URLs post-testing.
    * Split payment and SI (Standing Instruction) are optional features—only use them if needed.
  </Callout>

## Test the Integration and Go-Live

<Accordion title="Test the Integration" icon="fa-gear">
  <ReactNative_Test_the_Integration />
</Accordion>

<Accordion title="Go-live Checklist" icon="fa-gear">
  <ReactNative_Go_Live />
</Accordion>