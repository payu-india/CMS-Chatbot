---
title: 1. Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To integrate PayU CustomBrowser with flutter SDK, perform the following steps:

1. [Include the SDK in your app](https://docs.payu.in/docs/1-integration-steps#step-1-include-the-sdk-in-your-app)
2. [Initialise the SDK ](https://docs.payu.in/docs/1-integration-steps#step-2-sdk-initialisation)
3. [Implement Callback protocol](https://docs.payu.in/docs/1-integration-steps#step-3-callback-protocol-implementation)
4. [Set up payment hashes](https://docs.payu.in/docs/1-integration-steps#step-4-setup-payment-hashes)
5. [Generate the payment parameters](https://docs.payu.in/docs/1-integration-steps#payment-parameters)
6. [Initiate payment](https://docs.payu.in/docs/1-integration-steps#step-6-initiate-payment)

## Step 1: Include the SDK in your app

The CustomBrowser SDK for Flutter is offered through Fluter Pub.dev 

To add the SDK plugin use the following dependency in your app: `$ flutter pub add payubiz_cb_flutter`:

```
import 'package:payubiz_cb_flutter/payubiz_cb_flutter.dart';
import 'package:payubiz_cb_flutter/PayUCBConstantKeys.dart';
```

> 📘 Note
> 
> If you are developing for iOS, Install the pod using the following command inside “ios” folder.
> 
> ```
> $ pod install 
> ```

## Step 2: SDK initialisation

Declare PayuCustomBrowserFlutter instance and initialise the object.

```Text dart
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

## Step 3: Callback/ Protocol implementation

- Implement protocol at class level and override it’s methods to get hash generation and transaction callbacks.

```Text dart
class _MyAppState extends State<MyApp> implements PayUCustomBrowserProtocol
```

- Implement the following methods in your class to get callback.

```
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

## Step 4: Set up Payment Hashes

Hash is required to authenticate the request and to make sure MiTM has not happened while data was travelling over the network. You have to set the hash in hash parameter during creation of payment params.  Use the following format to generate the hash:

`sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)`

> 📘 Note
> 
> For TPV transactions, use the following format to generate the hash:
> 
> `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)`
> 
> The beneficiarydetail parameter value will be at last or the last value to be appended.{"beneficiaryAccountNumber":,"ifscCode":}

Here is a sample hash logic with sample value of the parameters for your reference:

 `smsplus|1695662774012|1|Info|Abc|[test@gmail.com](mailto:test@gmail.com)|udf1|udf2|udf3|udf4|udf5||||||
 {"beneficiaryAccountNumber":"1234567890","ifscCode":"IFSC0000024"}|1b1b0`

## Step 5: Generate the Payment Parameters

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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Notes",
    "0-0": "key  \n`Mandatory`",
    "0-1": "`String` This parameter must contain your merchant key received from PayU.",
    "0-2": "Cannot be null or empty",
    "1-0": "transaction_id  \n`Mandatory`",
    "1-1": "`String` It should be unique for each transaction.",
    "1-2": "Cannot be null or empty and should be unique for each transaction. Maximum allowed length is 25 characters. It cannot contain special characters like: -\\_/",
    "2-0": "amount  \n`Mandatory`",
    "2-1": "`String` Total transaction amount.",
    "2-2": "Cannot be null or empty and should be valid double stringified example: “100.0”",
    "3-0": "product_info  \n`Mandatory`",
    "3-1": "`String` Information about product.",
    "3-2": "Cannot be null or empty",
    "4-0": "first_name  \n`Mandatory`",
    "4-1": "`String` Customer’s first name",
    "4-2": " Cannot be null or empty",
    "5-0": "email  \n`Mandatory`",
    "5-1": "`String` Customer’s email id",
    "5-2": "Cannot be null or empty",
    "6-0": "phone  \n`Mandatory`",
    "6-1": " `String` Customer’s phone number.",
    "6-2": "Should be a valid phone number",
    "7-0": "User Credential  \n`mandatory`",
    "7-1": "`String` This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. **Format**:  \n<merchantKey>:<userId>  \nHere, the UserId is any ID/email/phone number to uniquely identify the user. \\*\\*",
    "7-2": "\"merchantKey:userId\"",
    "8-0": "ios_surl  \n`Mandatory`",
    "8-1": "`String` When the transaction gets success, PayU will load this url and pass transaction response.  \nNote: This field is applicable for iOS integration",
    "8-2": "Should be a valid URL",
    "9-0": "ios_furl  \n`Mandatory`",
    "9-1": "`String` When the transaction gets fail, PayU will load this url and pass transaction response.  \nNote: This field is applicable for iOS integration",
    "9-2": " Should be a valid URL",
    "10-0": "android_surl  \n`Mandatory`",
    "10-1": " `String` When the transaction gets success, PayU will load this url and pass transaction response.  \nNote: This field is applicable for Android integration",
    "10-2": "Should be a valid URL",
    "11-0": "android_furl  \n`Mandatory`",
    "11-1": "`String` When the transaction gets fail, PayU will load this url and pass transaction response.  \nWhen the transaction gets success, PayU will load this url and pass transaction response.  \nNote: This field is applicable for Android integration",
    "11-2": "Should be a valid URL",
    "12-0": "environment  \n`Mandatory`",
    "12-1": "`String` Environment of SDK",
    "12-2": " \"0\" for Production and \"1\" for Test",
    "13-0": "url  \n`Mandatory`",
    "13-1": "`String` The post URL",
    "13-2": "",
    "14-0": "post_data  \n`Mandatory`",
    "14-1": "`String` call `getPostData` method defined in next block to generate post request",
    "14-2": "",
    "15-0": "payment_type  \n`Mandatory`",
    "15-1": "`String` Payment option using which payment is being done. Example: CC, NB, CASH etc.",
    "15-2": "",
    "16-0": "auto_approve  \n`Mandatory`",
    "16-1": "`boolean` It will auto submit the OTP without user intervention",
    "16-2": "",
    "17-0": "merchant_response_timeout  \n`Mandatory`",
    "17-1": "`integer` If the SDK does not get response from bank it will give control to Merchant app when this timeout will exceed. PayU response will be send back to Merchant.",
    "17-2": "Should be a valid positive number"
  },
  "cols": 3,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Credit / Debit Card

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

### Store Credit / Debit card

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

### Card Tokenization with PayU

For cards tokenized with the PayU platform merchant needs to pass the below parameters

```
"&ccvv=" +
PayUTestCredentials.cvv + // pass the correct CVV.
"&store_card_token=" +
PayUTestCredentials.storeCardToken + // pass the store card token
&storecard_token_type=" +
PayUTestCredentials.storecardTokenType+ // storecardTokenType value should be 0
```

### Third Party-Card Tokenization

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

## SI Payment

```
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

### Recurring Payments in NetBanking

```
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

## Step 6: Initiate Payment

Initialise and launch the SDK by calling the following code snippet:

```Text dart
payUCustomBrowserFlutterPlugin.openCB(params: <PayU Payment Params>);
```