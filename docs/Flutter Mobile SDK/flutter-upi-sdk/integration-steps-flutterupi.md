---
title: 1. Integration Steps
excerpt: >-
  Steps to integrate UPI payments in your mobile application bulit on Flutter
  framework.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To integrate the Flutter UPI SDK, perform the following steps:

1. [Step 1: Include the Flutter UPI SDK in Your App](https://docs.payu.in/docs/integration-steps-flutterupi#step-1-include-the-sdk-in-your-app)
2. [Step 2: Intialise the Flutter SDK](https://docs.payu.in/docs/integration-steps-flutterupi#step-2-sdk-initialisation)
3. [Step 3: Implement the Callback protocol](https://docs.payu.in/docs/integration-steps-flutterupi#step-3-implement-the-callback-protocol)
4. [Step 4: Setup Payment Hashes](https://docs.payu.in/docs/integration-steps-flutterupi#step-4-setup-payment-hashes)
5. [Step 5: Generate Payment Params](https://docs.payu.in/docs/integration-steps-flutterupi#step-4-setup-payment-hashes)
6. [Step 6: Initiate Payment](https://docs.payu.in/docs/integration-steps-flutterupi#step-6-initiate-the-payment)

## Step 1: Include the SDK in your App

The UPI SDK for Flutter is offered through Flutter` pub.dev.` To add the SDK plugin use the following dependency in your app:

```
//Add plugin in your app 
$ flutter pub add payu_upi_flutter

//Import UPI Plugin in your dart code
import 'package:payu_upi_flutter/payu_upi_flutter.dart'; 
```

> 📘 Note:
>
> If you are developing for iOS, Install the pod using the following command inside “ios” folder.
>
> ```
> //Install payu dependencies in your ios project. 
> $ pod install 
> ```

## Step 2: Initialize Flutter SDK

Declare the `PayUUpiFlutter` instance and initialize the object.

```Text dart
class _MyAppState extends State<MyApp> implements PayUUPIProtocol {
    late PayUUpiFlutter payUUpiFlutter;

  @override
  void initState() {
    super.initState();
    payUUpiFlutter = PayUUpiFlutter(this);
  }
}
```

> 🚧 Keep in mind
>
> If you are developing for iOS, make sure your minimum deployment target is iOS 11.

## Step 3: Implement the Callback protocol

1. Implement PayUPIProtocol to receive hash and transaction callback. 

```Text dart
class _MyAppState extends State<MyApp> implements PayUUPIProtocol 
```

2. Implement the following methods in your class to receive the callbacks. 

```Text dart
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

## Step 4: Setup Payment Hashes

> 🚧 Warning
>
> Always generate the hash at your backend to ensure security.

Hash is required to authenticate the request and to make sure MiTM has not happened while data was traveling over the network. You have to set the hash in the hash parameter during the creation of payment parameters.  Use the following format to generate the hash:

`sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`

> 📘 Note
>
> For TPV transactions, use the following format to generate the hash:
>
> `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)`
>
> The **beneficiarydetail** parameter value will be at last or the last value to be appended.`{"beneficiaryAccountNumber":<Account No>,"ifscCode":<IFSC>}`

Here is a sample hash value for your reference:

 `smsplus|1695662774012|1|Info|Abc|[test@gmail.com](mailto:test@gmail.com)|udf1|udf2|udf3|udf4|udf5||||||  {"beneficiaryAccountNumber":"1234567890","ifscCode":"IFSC0000024"}|1b1b0`

## Step 5: Generate Payment Parameters

Set up the payment parameters for the SDK to initiate a transaction request. Use the following sample code for a quick integration:

```Text dart
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
  user_credentials: <unique user identifier>
  transaction_id:<Transaction ID>,
  additional_param: additionalParam,
  beneficiary_account_number: <Beneficiary Account Number>,
  beneficiary_ifsc: <ifsc code>,
  payment_mode:<String> // for Intent flow use "INTENT", for collect flow use "upi",
  disable_intent_seamless_failure:  <String>, // -1 | 0 ,
  package_name: <String>, //package name for the specific UPI intent (i.e. 				'net.one97.paytm') // package_name parameter used for Android only
  intent_app : <String>, //scheme name for the specific UPI intent (i.e. 'phonepe') // intent_app parameter used for IOS only
};

var si_details = {
    is_free_trial: "0", // 1 | 0 (true | false)
    si: '1',
    si_params: {
      is_free_trial: "0", // 1 | 0 (true | false)
      billing_amount: '1.00', //Required
      billing_interval: 1, //Required
      payment_start_date: '2022-12-24', //Required Ex: yyyy-mm-dd
      payment_end_date: '2023-12-24', //Required Ex: yyyy-mm-dd
      billing_cycle: //Required
      'ONCE', // YEARLY | MONTHLY | WEEKLY | DAILY | ONCE | ADHOC
      billing_currency: 'INR',  //Currency Code
      billing_limit: 'ON', //ON, BEFORE, AFTER
      billing_rule: 'MAX', //MAX, EXACT
      si: '1', //MAX, EXACT
    }
  };
```

### Payment Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `String` This parameter must contain your merchant key received from PayU.
      </td>

      <td>
        Cannot be null or empty
      </td>
    </tr>

    <tr>
      <td>
        transaction\_id\
        `mandatory`
      </td>

      <td>
        `String` It should be unique for each transaction.
      </td>

      <td>
        Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: -\_/
      </td>
    </tr>

    <tr>
      <td>
        amount\
        `mandatory`
      </td>

      <td>
        `String` Total transaction amount.
      </td>

      <td>
        Cannot be null or empty and should be a valid double-stringified example: “100.0”
      </td>
    </tr>

    <tr>
      <td>
        product\_info\
        `mandatory`
      </td>

      <td>
        `String`Product information.
      </td>

      <td>
        Cannot be null or empty
      </td>
    </tr>

    <tr>
      <td>
        first\_name\
        `mandatory`
      </td>

      <td>
        `String` Customer’s first name
      </td>

      <td>
         Cannot be null or empty
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        `String` Customer’s email id
      </td>

      <td>
        Cannot be null or empty
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `mandatory`
      </td>

      <td>
         `String` Customer’s phone number.
      </td>

      <td>
        There should be a valid phone number
      </td>
    </tr>

    <tr>
      <td>
        ios\_surl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction is successful, PayU will load this URL and pass the transaction response.  

        * \*Note\*\*: This field is applicable for iOS integration
      </td>

      <td>
        Should be a valid URL
      </td>
    </tr>

    <tr>
      <td>
        ios\_furl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.\
        No\*\*\*\*te: This field is applicable for iOS integration
      </td>

      <td>
         Should be a valid URL
      </td>
    </tr>

    <tr>
      <td>
        android\_surl\
        `mandatory`
      </td>

      <td>
         `String` When the transaction is successful, PayU will load this URL and pass the transaction response.  

        * \*Note\*\*: This field is applicable for Android integration
      </td>

      <td>
        Should be a valid URL
      </td>
    </tr>

    <tr>
      <td>
        android\_furl\
        `mandatory`
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.\
        When the transaction is a success, PayU will load this URL and pass the transaction response.  

        * \*Note\*\*: This field is applicable for Android integration
      </td>

      <td>
        Should be a valid URL
      </td>
    </tr>

    <tr>
      <td>
        environment\
        `mandatory`
      </td>

      <td>
        `String` Environment of SDK
      </td>

      <td>
         "0" for Production and "1" for Test
      </td>
    </tr>

    <tr>
      <td>
        user\_credentials\
        `mandatory`
      </td>

      <td>
        `String`User bank account number for TPV transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        beneficiary\_ifsc\
        `no`
      </td>

      <td>
        `String` IFSC of bank account for TPV transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        beneficiary\_account\_number 
      </td>

      <td>
        Users bank account number for TPV transaction.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Step 6: Initiate the payment

Initialise and launch the SDK by calling the following code snippet:

```Text dart
payUUpiFlutter.makeUPIPayment(params: <PayU Payment Params>);
```

## Step 7: VPA validation

Initialise and launch the Flutter UPI SDK by calling the following code snippet to validate the VPA

```Text dart
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

### Response

The sample response of a VPA validation request is similar to the following:

```Text JSON
{
  "status": "SUCCESS",
  "vpa": "9999999999@upi",
  "isVPAValid": 0,
  "payerAccountName": "PayUNeer",
  "isAutoPayVPAValid": 0,
  "isAutoPayBankValid": "NA"
}
```

## Step 8: List the UPI apps

Initialise and launch the Flutter UPI SDK by calling the following code snippet to get the list of UPI apps installed on Android and iOS devices

```Text dart
  intentApps() async {
    var data = await payUUpiFlutter.intentApps();
    showAlertDialog(context, "intentApps", "$data");
  }
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
    <string>gpay</string>
		<string>paytm</string>
		<string>bhim</string>
		<string>credpay</string>
	</array>
```