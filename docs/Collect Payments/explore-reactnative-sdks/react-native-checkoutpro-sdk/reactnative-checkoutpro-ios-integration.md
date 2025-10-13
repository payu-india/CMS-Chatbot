---
title: iOS Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: React Native Checkout Pro SDK for iOS Integration
  description: >-
    This document provides steps to integrate React Native Checkout Pro mobile
    SDK for iOS, including including the SDK in your app project, setting up
    payment hashes, building payment parameters, initiating the payment,
    handling payment completion, and customization.
  keywords:
    - React Native with IOS Checkout Pro SDK Integration Steps
    - PayU React Native with IOS SDK integration steps
    - Mobile payment integration with PayU React Native with IOS SDK steps
    - PayU React Native with IOS Checkout Pro set up for Mobile
    - React Native with IOS CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile React Native with IOS SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
To integrate with the CheckoutPro mobile SDK for React Native:

<Accordion title="SDK Integration Steps" icon="fa-code">
  <Accordion title="Step 1: Include the SDK in your app project" icon="fa-code">
    CheckoutPro is a dynamic framework. If you are not using 'use\_frameworks!', add the following entries at the end of your `podfile`:

    ```
    $dynamic_framework = ['PayUAssetLibraryKit', 'PayUBizCoreKit', 'PayUCheckoutProBaseKit', 'PayUCheckoutProKit', 'PayUCustomBrowser', 'PayULoggerKit', 'PayUNetworkingKit', 'PayUUPICoreKit', 'Socket.IO-Client-Swift', 'Starscream']
      $dynamic_framework = ['PayUAssetLibraryKit', 'PayUBizCoreKit', 'PayUCheckoutProBaseKit', 'PayUCheckoutProKit', 'PayUCustomBrowser', 'PayULoggerKit', 'PayUNetworkingKit', 'PayUUPICoreKit', 'Socket.IO-Client-Swift', 'Starscream','PayUParamsKit', 'PayUCrashReporter', 'PayUNetworkReachability']
      pre_install do |installer|
        Pod::Installer::Xcode::TargetValidator.send(:define_method, :verify_no_static_framework_transitive_dependencies) {}
        installer.pod_targets.each do |pod|
          if $dynamic_framework.include?(pod.name)
            def pod.build_type;
            Pod::BuildType.dynamic_framework
          end
        end
      end
    end
    ```

    After updating the` podfile`, install the pod using the command.

    ```
    pod install
    ```

    ***
  </Accordion>

  <Accordion title="Step 2: Set up Payment hashes" icon="fa-code">
    This step describes how to pass the static and dynamic hashes. For detailed information, refer to Hash Generation.

    <Accordion title="Pass Static Hashes" icon="fa-code">
      To pass static hashes during integration, use the following code snippet:

      ```Text React.js
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
    </Accordion>

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

  <Accordion title="Step 3: Build the payment parameters" icon="fa-code">
    To initiate a payment, your app needs to send transactional information to the Checkout Pro SDK.

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
            `String` Customer's first name.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Email
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer's email id.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Phone
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer's phone number, **Max character limit** : 10 Digits
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
            * *Sample URL*\*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ios\_furl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction fails, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for iOS integration
            * *Sample URL*\*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            android\_surl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for Android integration
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
            `String` This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:
            `<merchantKey>:<userId>`
            Here,
            UserId is any id/email/phone number to uniquely identify the user.
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

    For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/ios-standing-instructions-parameters).

    <Accordion title="Additional parameters" icon="fa-code">
      The additional parameters (optional) that can be passed to SDK are udf` `parameters, static hashes, and other parameters. For more details on Static Hash generation and passing them, refer to [Generate Hashes](https://docs.payu.in/docs/ios-checkoutpro-generate-hash). The following is a list of parameters that can be passed in additional parameters:

      | Parameter                                   | Description                                                                                                                                                              |
      | :------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | PayUCheckoutProConstants.CP\_UDF1           | `String`User-defined field, Merchant can store their customer id, etc.                                                                                                   |
      | PayUCheckoutProConstants.CP\_UDF2           | `String`User-defined field, Merchant can store their customer id, etc.                                                                                                   |
      | PayUCheckoutProConstants.CP\_UDF3           | `String`User-defined field, Merchant can store their customer id, etc.                                                                                                   |
      | PayUCheckoutProConstants.CP\_UDF4           | `String`User-defined field, Merchant can store their customer id, etc.                                                                                                   |
      | PayUCheckoutProConstants.CP\_UDF5           | `String`User-defined field, Merchant can store their customer id, etc.                                                                                                   |
      | Static hashes                               | `String` The static hashes are specified in this parameter. For more information, refer to the [Generate Hash](https://docs.payu.in/docs/ios-checkoutpro-generate-hash). |
      | PayUCheckoutProConstants.SODEX\_OSOURC\_EID | `String` Sodexo Source ID, Merchant can store it from the third field of the PayU response.                                                                              |
      | PaymentParamConstant.walletUrn              | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account.                                                                       |

      The payment parameters and additional parameters can be passed using the following code snippet:

      ```javascript React.js
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
          payUSIParams: {
            isFreeTrial:true,
          	billingAmount:'10',
          	billingInterval:1,
          	paymentStartDate:'2023-04-20',
          	paymentEndDate:'2023-04-30',
          	billingCycle:'daily', //Can be any of 'daily','weekly','yearly','adhoc','once','monthly'
          	remarks:'Test SI transcaction',
          	billingCurrency:'INR'
          }
      }
      ```

      ***
    </Accordion>
  </Accordion>

  <Accordion title="Step 4: Initiate the payment" icon="fa-code">
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

  <Accordion title="Step 5: Handle the payment completion" icon="fa-code">
    To get the callbacks for payment-related statuses, create a NativeEventEmitter object and subscribe to the below events.

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
  </Accordion>

  <Accordion title="Step 6: Customization (optional)" icon="fa-code">
    <Accordion title="For UPI Intent" icon="fa-code">
      Currently, PayU supports only PhonePe and GooglePay through Intent. Add the query schemes in `info.plist`.

      ```Text XML
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

  <Accordion title="Distributing your app (App Store / Ad-hoc)" icon="fa-code">
    What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayUChekoutPro, refer to [Releasing the app](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).
  </Accordion>
</Accordion>

<Accordion title="Test the Integration" icon="fa-gear">
<ReactNative_Test_the_Integration />
</Accordion>

<Accordion title="Go-live Checklist" icon="fa-gear">
<ReactNative_Go_Live />
</Accordion>
