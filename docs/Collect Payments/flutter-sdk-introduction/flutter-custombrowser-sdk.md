---
title: Flutter Custom Browser SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Flutter Custom Browser SDK
  description: >-
    This document provides instructions for integrating the Custom Browser SDK
    with Flutter, highlighting features like OTP assist and bank page
    optimizations, and includes compatibility details for Android and iOS.
  keywords:
    - Flutter Custom Browser SDK
    - ' Integrate Flutter Custom Browser'
    - Flutter Custom Browser SDK Integration
    - Integration of Flutter Custom Browser SDK
    - Custom Browser SDK integration on Mobile Flutter SDK
  robots: index
next:
  description: ''
---
This document describes how to integrate Custom Browser SDK with Flutter.

## Features

**OTP assist**: This feature helps you automatically read OTP messages on bank pages to ease the payment experience.
**Bank Page Optimizations**: PayU optimizes bank pages for a good payment experience.

## Compatibility

### Android

* Min SDK Version: 21
* Compile SDK Version: 31
* Kotlin 1.6.10

### iOS

* iOS version 11

## SDK Integration

To integrate PayU CustomBrowser with flutter SDK, perform the following steps:

<Accordion title="Step 1: Include the SDK in your app" icon="fa-code">
  The CustomBrowser SDK for Flutter is offered through Fluter Pub.dev

  To add the SDK plugin use the following dependency in your app: `$ flutter pub add payubiz_cb_flutter`:

  ```
  import 'package:payubiz_cb_flutter/payubiz_cb_flutter.dart';
  import 'package:payubiz_cb_flutter/PayUCBConstantKeys.dart';
  ```

  <Callout icon="📘" theme="info">
    **Note**: If you are developing for iOS, Install the pod using the following command inside “ios” folder.

    ```
    $ pod install 
    ```
  </Callout>
</Accordion>

<Accordion title="Step 2: SDK initialisation" icon="fa-code">
  Declare PayuCustomBrowserFlutter instance and initialise the object.

  ```d Dart
  class _MyAppState extends State<MyApp> implements PayUCustomBrowserProtocol {

    late PayUCustomBrowserFlutter payUCustomBrowserFlutterPlugin;

    @override
    void initState() {
      super.initState();
      payUCustomBrowserFlutterPlugin = PayUCustomBrowserFlutter(this);
    }
  }
  ```

  > 🚧 Keep in mind
  >
  > If you are developing for iOS, ensure that your minimum deployment target is iOS 11.
</Accordion>

<Accordion title="Step 3: Callback/ Protocol implementation" icon="fa-code">
  * Implement protocol at class level and override it’s methods to get hash generation and transaction callbacks.

  ```d Dart
  class _MyAppState extends State<MyApp> implements PayUCustomBrowserProtocol
  ```

  * Implement the following methods in your class to get callback.

  ```d Dart
  @override
  onPayuCBResponse(Map? response) {
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

        case PayUEventType.onBackButton: {
          String eventResponse = parsePayUResponse(response);
          //handle PayU response
        }
        break;

        case PayUEventType.onPaymentTerminate: {
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

<Accordion title="Step 4: Set up Payment Hashes" icon="fa-code">
  Hash is required to authenticate the request and to make sure MiTM has not happened while data was travelling over the network. You have to set the hash in hash parameter during creation of payment params.  Use the following format to generate the hash:

  `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`

  > 📘 Note
  >
  > For TPV transactions, use the following format to generate the hash:
  >
  > `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)`
  >
  > The beneficiarydetail parameter value will be at last or the last value to be appended.\{"beneficiaryAccountNumber":,"ifscCode":}

  Here is a sample hash logic with sample value of the parameters for your reference:

  `smsplus|1695662774012|1|Info|Abc|[test@gmail.com](mailto:test@gmail.com)|udf1|udf2|udf3|udf4|udf5||||||  {"beneficiaryAccountNumber":"1234567890","ifscCode":"IFSC0000024"}|1b1b0`
</Accordion>

<Accordion title="Step 5: Generate the Payment Parameters" icon="fa-code">
  Set up the payment parameters for the SDK to initiate a transaction request. Use the following sample code for a quick integration:

  ```Text dart
    var cbConfig = {
        first_name: < Name>,
        email: <email id>,
        phone: <phone number>,
        url:"https://secure.payu.in/_payment",
        payment_type:<NB/CC/CASH>,
        auto_approve:<true/false>, //pass false if you don't want to auto submit
        auto_select_otp: <true/false>, //pass false if you don't want to auto read the OTP
        merchant_response_timeout: 10,
        post_data: postData // create post data as defined in next block
      }
    
    var payUPaymentParams = {
        key: <Merchant Key>,
        transaction_id: <Transaction ID>,
        amount: <Amount>,
        surl: <SURL>,
        furl: <FURL>,
        product_info: <Product Info>,
        user_credentials: <pass user_credential>,
        cb_config: cbConfig // object from above
      };
  }
  ```

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
          `Mandatory`
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
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` It should be unique for each transaction.
        </td>

        <td style={{ textAlign: "left" }}>
          Cannot be null or empty and should be unique for each transaction. Maximum allowed length is 25 characters. It cannot contain special characters like: -\_/
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Total transaction amount.
        </td>

        <td style={{ textAlign: "left" }}>
          Cannot be null or empty and should be valid double stringified example: “100.0”
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          product\_info
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Information about product.
        </td>

        <td style={{ textAlign: "left" }}>
          Cannot be null or empty
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          first\_name
          `Mandatory`
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
          `Mandatory`
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
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Customer’s phone number.
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid phone number
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          User Credential
          `mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. **Format**: `<merchantKey>:<userId>`
          Here, the UserId is any ID/email/phone number to uniquely identify the user. \*\*
        </td>

        <td style={{ textAlign: "left" }}>
          "merchantKey:userId"
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ios\_surl
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` When the transaction gets success, PayU will load this url and pass transaction response.
          Note: This field is applicable for iOS integration
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid URL
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          ios\_furl
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` When the transaction gets fail, PayU will load this url and pass transaction response.
          Note: This field is applicable for iOS integration
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid URL
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          android\_surl
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` When the transaction gets success, PayU will load this url and pass transaction response.
          Note: This field is applicable for Android integration
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid URL
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          android\_furl
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` When the transaction gets fail, PayU will load this url and pass transaction response.
          When the transaction gets success, PayU will load this url and pass transaction response.
          Note: This field is applicable for Android integration
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid URL
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          environment
          `Mandatory`
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
          url
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` The post URL
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          post\_data
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` call `getPostData` method defined in next block to generate post request
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          payment\_type
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `String` Payment option using which payment is being done. Example: CC, NB, CASH etc.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          auto\_approve
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `boolean` It will auto submit the OTP without user intervention
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          merchant\_response\_timeout
          `Mandatory`
        </td>

        <td style={{ textAlign: "left" }}>
          `integer` If the SDK does not get response from bank it will give control to Merchant app when this timeout will exceed. PayU response will be send back to Merchant.
        </td>

        <td style={{ textAlign: "left" }}>
          Should be a valid positive number
        </td>
      </tr>
    </tbody>
  </Table>

<Accordion title="Credit / Debit Card" icon="fa-code">
  To pay using a credit card or debit card, perform the following steps.

  The bankcode and pg should be as below :-

  ```
  "&pg=" + "CC" +  
  "&bankcode=" + "CC"
  ```

  Set the following credit card parameters:

  ```
  "&ccnum=" +
  PayUTestCredentials.ccnum + //Here you can pass your Card No
  "&ccvv=" +
  PayUTestCredentials.cvv + //Here you can pass your CVV
  "&ccexpyr=" +
  PayUTestCredentials.ccexpyr + //Here you can pass your EXPYear 2025
  "&ccexpmon=" +
  PayUTestCredentials.ccexpmon + //Here you can pass your ExpMonth 05
  "&ccname=" +
  PayUTestCredentials.ccname ;
  ```

  <Accordion title="Store Credit / Debit card" icon="fa-code">
    To Pay using StoredCard, perform the following steps.

    Set the StoredCard parameter similar to the following code snippet

    ```
    "&ccnum=" +
    PayUTestCredentials.ccnum + //Here you can pass your Card No
    "&ccvv=" +
    PayUTestCredentials.cvv + //Here you can pass your CVV
    "&ccexpyr=" +
    PayUTestCredentials.ccexpyr + //Here you can pass your EXPYear 2025
    "&ccexpmon=" +
    PayUTestCredentials.ccexpmon + //Here you can pass your ExpMonth 05
    "&ccname=" +
    PayUTestCredentials.ccname +
    "&store_card=" +
    PayUTestCredentials.storedCard + // storedCard value should be 1
    ```
  </Accordion>

  <Accordion title="Card Tokenization with PayU" icon="fa-code">
    For cards tokenized with the PayU platform merchant needs to pass the below parameters

    ```
    "&ccvv=" +
    PayUTestCredentials.cvv + // pass the correct CVV.
    "&store_card_token=" +
    PayUTestCredentials.storeCardToken + // pass the store card token
    &storecard_token_type=" +
    PayUTestCredentials.storecardTokenType+ // storecardTokenType value should be 0
    ```
  </Accordion>

  <Accordion title="Third Party-Card Tokenization" icon="fa-code">
    For cards tokenized outside the PayU platform merchant needs to pass the below parameters.

    ```
    "&ccvv=" +
    PayUTestCredentials.cvv + //Either pass the correct CVV or omit the parameter completely.
    "&ccexpyr=" +
    PayUTestCredentials.ccexpyr + //This parameter must contain the network token expiry year.
    "&ccexpmon=" +
    PayUTestCredentials.ccexpmon + //This parameter must contain the network token expiry month.
    "&store_card_token=" +
    PayUTestCredentials.storeCardToken + // This must include the Network token generated at your end.
    &storecard_token_type=" +
    PayUTestCredentials.storecardTokenType+ // storecardTokenType value should be 1
    "&additional_info=" +
    PayUTestCredentials.addtionalDetails;   // {
        "last4Digits": "<last digit of card>",
        "tavv": "<will be given by tokenisation partner>",
        "trid": "<will be given by tokenisation partner>",
        "tokenRefNo": "<will be given by tokenisation partner>"
      }

    ```
  </Accordion>

  <Accordion title="SI Payment" icon="fa-code">
    ```d Dart
    PayUPaymentParamKey.si_details: {
          PayUSIParamsKeys.billingAmount: "1.00",
          PayUSIParamsKeys.billingCurrency: "INR",
          PayUSIParamsKeys.billingCycle:
          "DAILY", // YEARLY | MONTHLY | WEEKLY | DAILY | ONCE | ADHOC
          PayUSIParamsKeys.billingInterval: "1",
          PayUSIParamsKeys.paymentEndDate: "2023-12-12", // YYYY-MM-DD
          PayUSIParamsKeys.paymentStartDate: "2022-12-12" // YYYY-MM-DD
        }
    PayUSIParamsKeys.is_free_trial: "0", // 1 | 0 (true | false)
    PayUSIParamsKeys.si: "1"
    ```
  </Accordion>

  <Accordion title="Recurring Payments in NetBanking" icon="fa-code">
    ```d Dart
    PayUSIParamsKeys.beneficiarydetail: {
          PayUSIBeneDetailsKeys.beneficiaryAccountNumber:
          PayUTestCredentials.accountNumber,
          PayUSIBeneDetailsKeys.beneficiary_ifsc:
          PayUTestCredentials.accountIFSC,
          PayUSIBeneDetailsKeys.beneficiaryName: 'Name',
          PayUSIBeneDetailsKeys.beneficiaryAccountType:
          "0" // 1 for CURRENT ,0 for Saving
        }
    ```
  </Accordion>
</Accordion>
</Accordion>

<Accordion title="Step 6: Initiate Payment" icon="fa-code">
  Initialise and launch the SDK by calling the following code snippet:

  ```d Dart
  payUCustomBrowserFlutterPlugin.openCB(params: <PayU Payment Params>);
  ```
</Accordion>

## Test the Integration and Go-live
  <Accordion title="Test the integration" icon="fa-code">

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

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

***

<TestCardsCallout />

You can make test payments using one of the payment methods configured at the Checkout.

<Accordion title="Test credentials for supported payment methods" icon="fa-code">
  Following are the payment methods supported in PayU Test mode.

  <Accordion title="Test Credential for Card" icon="fa-code">
    | Card Number      | Expiry | CVV | OTP    |
    | :--------------- | :----- | :-- | :----- |
    | 5123456789012346 | 05/25  | 123 | 123456 |
  </Accordion>

  <Accordion title="Test credentials for Net Banking" icon="fa-code">
    Use the following credentials to test the Net Banking integration:

    * **user name:** payu
    * **password**: payu
    * **OTP**: 123456
  </Accordion>

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

    > ❗️ Callout
    >
    > The UPI in-app and UPI intent flow is not available in the Test mode.

    **Test cards for EMI**

    You can use the following Debit and Credit cards to test Emi integration.

    |              |                                         |
    | :----------- | :-------------------------------------- |
    | Kotak DC EMI | 1. **Card Number**: 4706-1378-0509-9594 |

    2. **Expiry**: any future date (mm/yy)
    3. **CVV**: 123
    4. **OTP**: 111111
    5. **Name**: Any name
    6. **Mobile Number**: 9123412345 (mandatory for EMI) |
       \| AXIS DC EMI  | 1) **Card Number**: 4011-5100-0000-0007

    2) **Expiry**: any future date (mm/yy)
    3) **CVV**: 123
    4) **OTP**: 111111
    5) **Name**: Any name
    6) **Mobile Number**: 9123412345 (mandatory for EMI) |
       \| HDFC CC EMI  | 1. **Card Number**: 4453-3410-65876437

    2. **Expiry**: any future date (mm/yy)
    3. **CVV**: 123
    4. **OTP**: 111111
    5. **Name**: Any name
    6. **Mobile Number**: 9123412345 (mandatory for EMI)  |
       \| ICICI CC EMI | 1) **Card Number**: 4453-3410-65876437

    2) **Expiry**: any future date (mm/yy)
    3) **CVV**: 123
    4) **OTP**: 111111
    5) **Name**: Any name
    6) **Mobile Number**: 9123412345 (mandatory for EMI)  |
  </Accordion>

  <Accordion title="Test wallets" icon="fa-code">
    You can use the following wallets and their corresponding credentials to test wallet integration.

    <Table align={["left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Wallet
          </th>

          <th style={{ textAlign: "left" }}>
            Mobile Number
          </th>

          <th style={{ textAlign: "left" }}>
            OTP
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            PayTM
          </td>

          <td style={{ textAlign: "left" }}>
            7777777777
          </td>

          <td style={{ textAlign: "left" }}>
            888888
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            PhonePe
          </td>

          <td style={{ textAlign: "left" }}>
            Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)
            Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.
          </td>

          <td style={{ textAlign: "left" }}>
            NA
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            AmazonPay
          </td>

          <td style={{ textAlign: "left" }}>
            You can test using your original Amazon account details.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>
      </tbody>
    </Table>
  </Accordion>
</Accordion>
</Accordion>

<Go_Live_Checklist />

## Sample app

The sample app for Flutter Custom Browser SDK can be found in the following Github location:

[https://github.com/payu-intrepos/PayUCustomBrowser-Flutter.git](https://github.com/payu-intrepos/PayUCustomBrowser-Flutter.git)
