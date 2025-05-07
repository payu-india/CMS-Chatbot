---
title: 1. SDK Integration Steps - iOS 3DS 2.0
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: iOS-3ds2.0SDK-Introduction
  description: ''
  robots: index
next:
  description: ''
---
The iOS 3DS SDK integration involves the following steps: 

1. [Install the SDK in your app project](https://docs.payu.in/docs/ios-3ds-20-sdk#step-1-install-the-sdk-in-your-app-project)
2. [Initialise the SDK](https://docs.payu.in/docs/ios-3ds-20-sdk#step-2-initialise-the-sdk)
   1. [Initialise](https://docs.payu.in/docs/ios-3ds-20-sdk#step-21-initialise)
   2. [UI Customisation](https://docs.payu.in/docs/ios-3ds-20-sdk#step-22-ui-customisation)
   3. [3DS Warnings](https://docs.payu.in/docs/ios-3ds-20-sdk#step-23-3ds-warnings)
3. [Device Details(PArq)](https://docs.payu.in/docs/ios-3ds-20-sdk#step-3-device-detailsparq)
4. [3DS 2.0 Challenge Initiation](https://docs.payu.in/docs/ios-3ds-20-sdk#step-4--3ds-20-challenge-initiation)
   1. [Challenge UI Handling (Optional)](https://docs.payu.in/docs/ios-3ds-20-sdk#step-41-challenge-ui-handling-optional)
   2. [Challenge Action Handing](https://docs.payu.in/docs/ios-3ds-20-sdk#step-42-challenge-action-handing)
5. [Bin Info API Details](https://docs.payu.in/docs/ios-3ds-20-sdk#step-5-bin-info-api-details)

## Step 1: Install the SDK in your app project

The 3DS2 SDK is offered via CocoaPods. To add the SDK to your app project, include the SDK framework in your pod file using the pod install command in terminal.

### CocoaPods Integration

```
//make sure to add below-mentioned line to use dynamic frameworks

use_frameworks!

// Add this to include our SDK
pod 'PayUIndia-3DS2-SDK'
```

### Swift Package Manager Integration

You can integrate 3DS2 SDK with your app or SDK using SPM with following methods:

- **Using Xcode**: Navigate to File > Add Package menu and add the following package:
- **Using Package.Swift**: Add the following line in the Package.swift dependencies:

```
.package(name: "PayUIndia-3DS2-SDK", url: "https://github.com/payu-intrepos/PayU3DS2SDK-iOS", from: "1.3.1")
```

- **Import**: Add the following imports in the class where you need to initiate a payment using 3DS2.

```
import PayU3DS2Kit
```

***

## Step 2: Initialise the SDK

### Step 2.1: Initialise

Initialise SDK before invoking any de-coupled functionality

> 📘 Remember
> 
> Initialisation of SDK is mandatory if merchant is utilising PayU 3DS 2.0 for de-couple functionality. Call initialise before every transaction.

```
    PayU3DS2.initialise(
        key: String,
        requestId: String,
        config: PayU3DS2Config,
        completion: @escaping PayU3DS2Completion
    )
```

**This method accepts four parameters**:

- **Key**: The unique merchant key. 
- **RequestId**: Unique request ID.
- **PayU3DS2Config**: It contains below properties:

```
PayU3DS2Config: It contains below properties
var config = PayU3DS2Config()

config.uiCustomisation = "set UI customisation object, refer below section of UI Customisation"
config.isProduction = "set environment where you want to test, true for production and false for sandbox"
config.fallback3DS1 = true //default value false, send true to complete payment on bank page in case of any failure
config.autoSubmit = false //Set the values as true to submit the OTP automatically without any user interaction. By default, the value is false.
config.initialiseTimeoutTimer = 5 //provide time in seconds, for waiting for merchant response
config.supportedUIMode = ArrayList<String> //to show own UI, currently accepted value = 01. Pass this if you want to create own UI and follow step 4.1 and 4.2

// Can also set progress indicator
config.setDefaultProgressLoader(showDefaultLoader: true, defaultProgressLoaderColor: "HexColor") //to show default loader instead of full page loader pass true, and to change color of progress bar pass valid hexcode

//To customise UI with your content please pass these configurations
config.enableCustomizedOtpUIFlow = true
config.enableTxnTimeoutTimer = true //pass as true to show timer for page timeout
config.merchantName = "merchant name" 
config.amount = "txn amount"

config.acsContentConfig = PayU3DS2ACSContentConfig()
config.acsContentConfig?.submitButtonTitle = "Submit Button Title"
config.acsContentConfig?.resendButtonTitle = "Resend Button Title"
config.acsContentConfig?.otpContent =  "OTP has been sent to your registered mobile number"  //you can set this value to as per your need

config.acsContentConfig?.resendInfoContent =  "OTP has been resent to your registered mobile number" //you can set this value to as per your need

config.acsContentConfig?.maxResendInfoContent =  "Limit has been exceeded to send OTP. Please retry with latest OTP or initiate a new payment" //you can set this value to as per your need


```

- **Completion**:  PayU3DS2Completion -  This is a Closure/Callback where you will receive response after Initialisation done. It contains PayU3DS2Response which will have below properties.

```
PayU3DS2Response:
status: Int = -1 //If status is 0, it implies the function was successfully executed, and you should check the result object, else there was a problem with the function's execution; you should check the error message.
errorMessage: String? // error message with details what went wrong.
result: Any? Success response with details. Please refer below class for response structure:

class PayU3DS2DeviceWarning(
    var id: String
    var message: String
    var severity: PayU3DS2DeviceSeverity 
)
PayU3DS2DeviceSeverity expected values:
 low, 
 medium, 
 high
```

***

### Step 2.2: UI Customisation

**PayU3DS2UICustomisation** - Below are the details of views that can be customised.

#### Button customisation

```
var buttonCustomisation = PayU3DS2ButtonCustomisation(
        textFontColor: String?, //HEX CODE
        textFontSize: Int,
        backgroundColor: String?,
        cornerRadius: Int,
        resendButtonTextFontColor: String? //HEX CODE
    )
Ex:
PayU3DS2ButtonCustomisation(
        textFontColor: "#ffffff",
        textFontSize: 17,
        backgroundColor: "#25272C",
        cornerRadius: 10,
        resendButtonTextFontColor: "#25272C"
    )
```

#### Label customisation

```
var labelCustomisation = PayU3DS2LabelCustomisation(
        textFontColor: String?, //HEX CODE
        textFontSize: Int,
        headingTextColor: String?, //HEX CODE
        headingTextFontSize: Int
    )
```

#### Toolbar customisation

```
var toolbarCustomisation = PayU3DS2ToolBarCustomisation(
        textFontColor: String?, //HEXCODE
        textFontSize: Int,
        backgroundColor: String?, //HEXCODE
        buttonText: String?, 
        headerText: String?
    )
```

#### TextBox Customisation:

```
var textBoxCustomisation = PayU3DS2TextBoxCustomisation(
        textFontColor: String?, //HEXCODE
        textFontSize: Int,
        borderColor: String?, //HEXCODE
        borderWidth: Int,
        cornerRadius: Int
    )
```

#### UI Customisation

```
var uiCustomisation = PayU3DS2UICustomisation(
        buttonCustomisation: PayU3DS2ButtonCustomisation?,
        labelCustomisation: PayU3DS2LabelCustomisation?,
        textBoxCustomisation: PayU3DS2TextBoxCustomisation?,
        toolbarCustomisation: PayU3DS2ToolBarCustomisation?,
        fontFamilyCustomisation: PayU3DS2FontFamilyCustomisation?
    )
```

#### Font Customisation:

```
 var fontFamilyCustomisation = PayU3DS2FontFamilyCustomisation(
            headerFontFamily: String?, // Set Font Family Name, example: "Roboto-Medium"
            subTextFontFamily: String?// Set Font Family Name, example: "Roboto-Regular"
      )
```

### Step 2.3: 3DS Warnings

The result for device security checks like rootedDevice, isDebuggable, isEmulator and is OS Supported will be provided in result of init as given in above code example for the completion callback. It is left with the requestor app to handle the warnings as per the requirement.

***

## Step 3: Device Details(PArq)

To obtain device information to initiate an authentication request, use the method below.

```
PayU3DS2.extractDeviceDetails(cardData: PayU3DS2CardData) -> PayU3DS2Response

val cardData = PayU3DS2CardData(PayU3DS2CardScheme.mastercard, "2.2.0")

PayU3DS2CardScheme expected values:
 visa,
 mastercard

The second parameter is threeDSVersion. Pass the messageVersion value received in binInfo API. 
```

**PayU3DS2Response**: Three items are in the response

```
status: If status is 0, it implies the function was successfully executed, and you should check the result object, else there was a problem with the function's execution; you should check the error message.
errorMessage: Error message with details what went wrong.
result: Success response with details. Please refer below class for response structure:

class PayU3DS2PArqResponse(
    val sdkAppID: String,
    val sdkEncData: String,
    val crv: String,
    val kty: String,
    val x: String,
    val y: String,
    val sdkTransID: String,
    val sdkReferenceNumber: String
)
```

Now these device details can be used to initiate an authentication request with us or any other aggregator.

Once the authentication request has been initiated and a response has been received, then same is used to initiate a challenge which basically means opening a UI screen to do user authentication.

## Step 4:  3DS 2.0 Challenge Initiation

Call the function below to start the challenge.

```
PayU3DS2.initiateChallenge(challengeParameter: PayU3DS2ChallengeParameter,
        completion: @escaping PayU3DS2Completion)
var challengeParameter = PayU3DS2ChallengeParameter(acsSignedContent: String,
                                                    acsRefNumber: String, 
                                                    acsTransactionID: String,
                                                    threeDSServerTransactionID: String)

```

Before invoking this method, generate the authentication request through any aggregator and pass the above defined challenge parameters to initiate challenge.

- PayU3DS2Completion: Closure consists of 1 parameter:

```
PayU3DS2Response: Three items are in the response:
status: If status is 0, it implies the function was successfully executed, and you should check the result object, else there was a problem with the function's execution; you should check the error message.
errorMessage: Error message with details what went wrong.
result: It will contain success response.

Cast response to String. If value is "Y" that means challenge is successfully executed else it is failed.
```

### Step 4.1: Challenge UI Handling (Optional)

If you have passed supportedUIMode = ["01"] parameter in config, you will receive below response in callback:

```
fun onSuccess(response: Any): It will contain success response.
fun onError(errorCode: Int, errorMessage: String): It will contain failure reason code and reason.

Cast response to HeadlessData.

class PayU3DS2HeadlessData {
    var acsRenderingType: String?
    var acsTransactionID: String?
    var challengeAddInfo: String?
    var challengeInfoHeader: String?
    var challengeInfoLabel: String?
    var challengeInfoText: String?
    var challengeInfoTextIndicator: String?
    var challengeSelectInfo: [[String: String]]?
    var expandInfoLabel: String?
    var expandInfoText: String?
    var issuerImage: PayU3DS2ImageDetails?
    var networkImage: PayU3DS2ImageDetails?
    var resendInformationLabel: String? //If it null then do not show resend button
    var submitAuthenticationLabel: String?
    var whyInfoLabel: String?
    var whyInfoText: String?
    var whitelistingInfoText: String?
    var threeDSServerTransID: String?
}

class ImageDetails(
    var mediumQualityURL: String?,
    var highQualityURL: String?,
    var extraHighQualityURL: String?
)
```

### Step 4.2: Challenge Action Handing

There are three actions that you have show to user on OTP page:

1. RESEND
2. SUBMIT
3. CANCEL

To execute these methods call below method:

```
func action(
        acsActionType: PayU3DS2ACSActionType,
        challengeInputParams: PayU3DS2ACSActionParams,
        completion: @escaping PayU3DS2Completion
    )

This method accepts 3 parameters, details are below:
1. PayU3DS2ACSActionType: action user took, accepted values are SUBMIT, RESEND, CANCEL
2. PayU3DS2ACSActionParams: It contains parameters to execute action passed. This contains 3 parameters.
 2.1 acsTransactionID //string. Value recieved in step 4.1
 2.2 acsRenderingType //string. Value recieved in step 4.1
 2.3 challengeData //string. OTP value, to be passed in case of SUBMIT action.
3. PayU3DS2Completion: Closure consists of 1 parameter:
PayU3DS2Response: Three items are in the response:
status: If status is 0, it implies the function was successfully executed, and you should check the result object, else there was a problem with the function's execution; you should check the error message.
errorMessage: Error message with details what went wrong.
result: It will contain success response.

Cast result to PayU3DS2ACSResponse.
class PayU3DS2ACSResponse(
        var message: String,
        var acsActionType: PayU3DS2ACSActionType,
        var headlessData: PayU3DS2HeadlessData
)
//message: status message.
//acsActionType: Action passed during invocation of this method
//headlessData: This bean contains data related to network and issuer image url etc. Refer section 4.1.
```

> 🚧 Call RESEND action after 10 seconds.

## Step 5: Bin Info API Details

Merchant must use the following procedure. This api will give info about whether the bin is supported on 3DS 1 or 3DS 2 and whether information can be routed through 3DS SDK. If no, then merchant can initiate a non native transaction. Merchant has to pass below parameters.

```
PayU3DS2.cardBinInfo(
        cardBinInfoRequest: PayU3DS2CardBinInfoRequest,
        delegate: PayU3DS2HashDelegate,
        completion: @escaping PayU3DS2Completion
    ) 
Please refer below code to create cardBinInfoRequest object:
val cardBinInfoRequest = PayU3DS2CardBinInfoRequest(cardDetails: "enter card number or network Token", isSI: true) //set second parameter to true if txn is for standing instructions, card details cannot be null
```

- **cardBinInfoRequest**: It contains two parameters cardDetails, isSI.
- **PayU3DS2HashDelegate**: This API need sha512 hash and this delegate will call to pass hash using generateHash functions.

In this, if messageVersion is anything that starts with 2., then it is supported on 3DS 2 else if it starts with 1., then it is supported on 3DS1. 

```
func generateHash(for param: [String: String], onCompletion: @escaping PayU3DS2HashGenerationCompletion) 
//Merchant will get map with type of hash and hash string as value of map.
      They have to sign that string using salt to create hash value and pass that in completion
 param: this contains 3 keys 
 hashName - command name
 hashString - hash string with out salt
 postSalt - needs to add after salt
 need to create hash on your server using hashString + salt + postSalt and SHA512 algo
 PayU3DS2HashGenerationCompletion: this contains hashDict parameter
 HashDict: pass a dictionary which contains hashName as key and hash as value

PayU3DS2Completion: contains PayU3DS2Response.
PayU3DS2Response: Three items are in the response:
status: If status is 0, it implies the function was successfully executed, and you should check the result object, else there was a problem with the function's execution; you should check the error message.
errorMessage: Error message with details what went wrong.
result: It will contain success response. Please refer below class for response structure:
Please refer below class for success response structure:
 class PayU3DS2BinInfoResponse(
    val issuingBank: String
    val bin: String,
    val category: String,
    val cardType: String,
    val isDomestic: String,
    val isAtmPinCard: String,
    val isSiSupported: String,
    val isOtpOnTheFly: String,
    val messageVersion: String
)
```

## Step 6:  Initiate Payment through PayU

Call the following method to initiate payment through PayU and we will return success or failure callback post transaction completion.

1. Use the following `PayU3DS2.initiatePayment` method to initiate payment:

```
 PayU3DS2.initiatePayment(
        vc: UIViewController,
        config: PayU3DS2Config,
        paymentParams: PayU3DS2PaymentParam,
        delegate: PayU3DS2Delegate
    )
```

2. You have to pass the following parameters:
   - **vc**: Parent ViewController Object
   - **config**: It contains multiple properties. 
   - **paymentParams**: Merchant to create payment param object and pass it which will contains info like: cardDeatails, SI details etc. Refer the following sample code for `paymentParams`:

```
 let paymentParam = PayU3DS2PaymentParam(
     key: "<Your Key issued by PayU>",
     transactionId: "<Transaction Id>",
     amount: "<Transaction Amount>",
     productInfo: "<Product Description>",
     firstName: "<Customer First Name>",
     email: "<Customer Email>",
     phone: "9876543210",
     surl: "<Success URL>",
     furl: "<Failure URL>"
 )
 
 let udfs = PayU3DS2UserDefines() 
 udfs.udf1 = "<User Defined Fields>"
 udfs.udf2 = "<User Defined Fields>"
 udfs.udf3 = "<User Defined Fields>"
 udfs.udf4 = "<User Defined Fields>"
 udfs.udf5 = "<User Defined Fields>"
 paymentParam.udfs = udfs

 var cardDetails =  PayU3DS2CardInfo()
 cardDetails.cardNumber = "<cardNumber>"
 cardDetails.cardName = "<cardName>"
 cardDetails.nameOnCard = "<cardholderName>"
 cardDetails.expiryMonth = "<expiryMonth>"// MM
 cardDetails.expiryYear = "<expiryYear>"// YYYY
 cardDetails.cvv = "<cvv>"
 Note: To make payment using saved card, please pass both network token and card token.
 cardDetails.networkToken = "<networkToken>"
 cardDetails.cardToken = "<cardToken>"

 paymentParam.cardinfo = cardDetails // PayU3DS2CardInfo with card details
```

3. Implement `PayU3DS2Delegate`. It contains the following methods:
   - func `onPaymentSuccess`(successResponse: Any): It will contain success response. This will be a JSON Object, parse response as per your need.
   - func `onPaymentFailure`(failureResponse: Any): It will contain failure response. This will be a JSON Object, parse response as per your need.
   - func `onPaymentCancel`(isTxnInitiated: Bool): It will tell if payment was cancelled.
   - func `onError`(errorCode: Int, errorMessage: String): It will contain failure reason code and reason.
   - func `generateHash`(for param: [String: String], onCompletion: @escaping PayU3DS2HashGenerationCompletion): Merchant will get map with type of hash and hash string as value of map.  
          They have to sign that string using salt to create hash value and pass that in completion  
     param: this contains 3 keys:
   - **hashName**: command name
   - **hashString**: hash string with out salt
   - **postSalt**: needs to add after salt

You need to create hash on your server using hashString + salt + postSalt and SHA512 algorithm.

4. Implement `PayU3DS2HashGenerationCompletion`. This contains `hashDict` parameter  
   hashDict: pass a dictionary which contains hashName as key and hash as value

## Step 7: Error Codes

|     |                                                                               |
| :-- | :---------------------------------------------------------------------------- |
| 0   | Success                                                                       |
| 1   | Fail/ Invalid params                                                          |
| 2   | Error while creating transaction to generate device details, please try again |
| 3   | Time out                                                                      |
| 4   | Challenge protocol error                                                      |
| 5   | User cancelled the transaction                                                |
| 6   | Runtime Error                                                                 |
| 12  | Action params null for headless flow                                          |
| 14  | Resend OTP limit exceeded                                                     |
| 15  | The OTP code you entered is incorrect                                         |
| 17  | Transaction failed                                                            |
| 105 | Hash cannot be nil                                                            |
| 106 | Card not supported on 3DS 2.0                                                 |
| 107 | Card scheme not supported                                                     |
| 108 | Hash incorrect                                                                |
| 109 | Invalid ACS UI Type                                                           |
| 500 | Something went wrong                                                          |
| 503 | Error while creating transaction to generate device details, please try again |