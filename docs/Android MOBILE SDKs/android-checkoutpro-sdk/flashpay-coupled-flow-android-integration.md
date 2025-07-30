---
title: FlashPay Coupled Flow Android Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
FlashPay solution primarily offers a single comprehensive SDK which is equipped to operate on 3DS protocols and additionally manages e2e authentication, including advanced biometric-based OOB authentication.

## 1. Gradle changes

Add the following dependency in your app-level gradle file:

```gradle
implementation 'in.payu:threeds-sdk:X.X.X'
```

## 2. Installation

### Payment initialization method

Call the following `initiatePayment` method to initiate payment through us and we will return success or failure callback post transaction completion. This method will internally call Authentication request (/\_payment), collect device detail, call binInfo API, present the native OTP screen and do the authorization too.

Use the `initiatePayment` method:

```kotlin
fun initiatePayment(
    activity: AppCompatActivity,
    config: PayU3DS2Config,
    paymentParams: PaymentParams,
    callback: PayU3DS2PaymentCallback
)
```

### Parameters for initiatePayment

| Parameter       | Description                                               |
| --------------- | --------------------------------------------------------- |
| `activity`      | Current activity context                                  |
| `config`        | Configuration object for customizing the FlashPay SDK     |
| `paymentParams` | Payment-related details object                            |
| `callback`      | Callback for payment success, failure, cancellation, etc. |

### 2.1 PayU3DS2Config

Define and configure details for the SDK:

> 📘 Note:
>
> For uiCustomisation object initialisation, refer to [UI customization](#ui-customization).

```kotlin
PayU3DS2Config: It contains below properties
var config = PayU3DS2Config()
config.uiCustomisation = "set UI customisation object, refer below section of UI Customisation" // 
config.isProduction = "set environment where you want to test, true for production and false for sandbox"
config.autoRead = false //Set the values as true to allow auto-read OTP and fill in the OTP field. By default, the value is false.
config.autoSubmit = false //Set the values as true to submit the OTP automatically without any user interaction. By default, the value is false.
config.setDefaultProgressLoader(true, "HexColor") //to show default loader instead of full page loader pass true, and to change color of progress bar pass valid hexcode

config.enableMFAViaBiometric = true // if set to true, then during payment via OTP, there will an option to enable biometric authentication. 
// If selected, the biometric registration process will start after payment success callback is triggered. 
```

#### Customise UI with your content

To customise UI with your content,  pass these configurations:

```
config.enableCustomizedOtpUIFlow = true
config.enableTxnTimeoutTimer = true //pass as true to show timer for page timeout
config.merchantName = "merchant name"
config.amount = "txn amount"
```

#### ACS content configurations

Customize OTP and related properties:

```kotlin
val acsContentConfig = ACSContentConfig()
acsContentConfig.otpContent = "OTP has been sent to your registered mobile number". //you can set this value to as per your need
acsContentConfig.resendButtonTitle = //you can set this value to as per your need
acsContentConfig.submitButtonTitle = //you can set this value to as per your need
acsContentConfig.resendInfoContent = //you can set this value to as per your need
acsContentConfig.maxResendInfoContent = //you can set this value to as per your need
config.acsContentConfig = acsContentConfig
```

#### Configuration properties

| Property                    | Description                                    |
| :-------------------------- | :--------------------------------------------- |
| `isProduction`              | true for production, false for sandbox         |
| `autoRead`                  | Auto-read OTP. The default value is "false".   |
| `autoSubmit`                | Auto-submit OTP. The default value is "false". |
| `enableMFAViaBiometric`     | Biometric registration after payment success   |
| `enableCustomizedOtpUIFlow` | Customized OTP UI                              |
| `enableTxnTimeoutTimer`     | Enable timeout timer for pages                 |

#### Configuration Notes

* **autoRead**: Set to `true` to allow auto-read OTP and auto-fill it in the OTP field. Defaults to `false`.
* **autoSubmit**: Set to `true` to submit OTP automatically without user interaction. Defaults to `false`.
* **setDefaultProgressLoader**: Customize via `config.setDefaultProgressLoader(true, "HexColor")`. This replaces the full-page loader with a default small loader.
* **enableMFAViaBiometric**: If set `true`, users will receive an option to enable biometric authentication during payment via OTP. The biometric registration process starts after the payment success callback.

## UI customization

### Button customization

```kotlin
var buttonCustomisation = ButtonCustomisation.Builder()
    .setBackgroundColor("colorCode") // HEX CODE
    .setCornerRadius(5) // Integer
    .setTextFontColor("colorCode") // HEX CODE
    .setTextFontSize(5) // Integer
    .setTextCaseType(ButtonTextCaseType.LOWER_CASE) // LOWER_CASE, UPPER_CASE
    .setResendTextFontColor("colorCode") // HEX CODE
    .build()
```

### Label customization

```kotlin
var labelCustomisation = LabelCustomisation.Builder()
    .setHeadingTextColor("colorCode") // HEX CODE
    .setHeadingTextFontName(FontName.ROBOTO_REGULAR)
    .setHeadingTextFontSize(10) // Integer
    .setTextColor("colorCode") // HEX CODE
    .setTextFontName(FontName.ROBOTO_REGULAR)
    .setTextFontSize(10) // Integer
    .build()
```

### Toolbar customization

```kotlin
var toolbarCustomisation = ToolbarCustomisation.Builder()
    .setBackgroundColor("colorCode") // HEX CODE
    .setButtonText("ButtonText") // String
    .setHeaderText("HeaderText") // String
    .setTextColor("colorCode") // HEX CODE
    .setTextFontSize(18) // Integer
    .setTextFontName(FontName.ROBOTO_REGULAR)
    .build()
```

### TextBox customization

```kotlin
var textBoxCustomisation = TextBoxCustomisation.Builder()
    .setTextColor("colorCode") // HEX CODE
    .setBorderColor("colorCode") // HEX CODE
    .setCornerRadius(5) // Integer
    .setTextFontSize(5) // Integer
    .setBorderWidth(5) // Integer
    .setTextFontName(FontName.ROBOTO_REGULAR)
    .build()
```

### Bottom sheet customization

```kotlin
var bottomSheetCustomisation = BottomSheetCustomisation.Builder()
    .setButtonBackgroundColor("colorCode") // HEX CODE
    .setTextFontColor("colorCode") // HEX CODE
    .setCornerRadius(5) // Integer
    .setTextFontSize(5) // Integer
    .setLabelTextFontSize(5) // Integer
    .setHeadingTextFontSize(5) // Integer
    .setTextCaseType(ButtonTextCaseType.LOWER_CASE) // LOWER_CASE, UPPER_CASE
    .setResendTextFontColor("colorCode") // HEX CODE
    .build()
```

### Font customization

```kotlin
val fontFamilyCustomisation = FontFamilyCustomisation.Builder()
    .setHeaderFontFamily("Header Font family path") // example: assets/fonts/lato-italic.ttf
    .setSubTextFontFamily("Sub text font family path") // example: assets/fonts/lato-italic.ttf
    .build()
```

### UI customization integration

```kotlin
var uiCustomisation = UICustomisation.Builder()
    .setButtonCustomisation(buttonCustomisation)
    .setToolbarCustomisation(toolbarCustomisation)
    .setTextBoxCustomisation(textBoxCustomisation)
    .setLabelCustomisation(labelCustomisation)
    .setFontFamilyCustomisation(fontFamilyCustomisation)
    .setBottomSheetCustomisation(bottomSheetCustomisation)
    .build()
```

### Font customization options

| Property            | Description                                             | Example                        |
| ------------------- | ------------------------------------------------------- | ------------------------------ |
| `HeaderFontFamily`  | Set the header font family from the specified file path | `assets/fonts/lato-italic.ttf` |
| `SubTextFontFamily` | Set subtext font family from the specified file path    | `assets/fonts/lato-italic.ttf` |

## 2.2 PaymentParams

Create and configure payment details:

```kotlin
var mPaymentParams =  PaymentParams();
        mPaymentParams.key = "<Your Key issued by PayU>"
        mPaymentParams.amount = "<Transaction Amount>"
        mPaymentParams.productInfo = "<Product Description>"
        mPaymentParams.firstName = "<Customer First Name>"
        mPaymentParams.email = "<Customer Email>"
        mPaymentParams.txnId = "<Transaction Id>"
        mPaymentParams.surl = "<Success URL>"
        mPaymentParams.furl = "<Failure URL>"
        mPaymentParams.termUrl = "<Term URL>"
        mPaymentParams.udf1 = "<User Defined Fields>"
        mPaymentParams.udf2 = "<User Defined Fields>"
        mPaymentParams.udf3 = "<User Defined Fields>"
        mPaymentParams.udf4 = "<User Defined Fields>"
        mPaymentParams.udf5 = "<User Defined Fields>"
        mPaymentParams.cardNumber = "<cardNumber>"
        mPaymentParams.cardName = "<cardName>"
        mPaymentParams.nameOnCard = "<cardholderName>"
        mPaymentParams.expiryMonth = "<expiryMonth>"// MM
        mPaymentParams.expiryYear = "<expiryYear>"// YYYY
        mPaymentParams.cvv = "<cvv>"
        mpaymentParams.storeCard = if (true) 1 else 0

```

### Required payment parameters

| Parameter     | Description             |
| ------------- | ----------------------- |
| `key`         | Your Key issued by PayU |
| `amount`      | Transaction Amount      |
| `productInfo` | Product Description     |
| `firstName`   | Customer First Name     |
| `email`       | Customer Email          |
| `txnId`       | Transaction ID          |
| `surl`        | Success URL             |
| `furl`        | Failure URL             |
| `cardNumber`  | Card Number             |
| `expiryMonth` | Expiry MM               |
| `expiryYear`  | Expiry YYYY             |
| `cvv`         | CVV                     |

To make payment using saved card, pass both network token and card token:

```
        mpaymentParams.userCredentials = "XXXX:XXXX"
        mpaymentParams.networkToken = <Network Token>
        mpaymentParams.cardToken = <Card Token>
```

> 📘 Saved Card Payments
>
> Requires both `networkToken` and `cardToken` under `mPaymentParams` for saved card-related transactions.

## 2.3 PayU3DS2PaymentCallback

Callback methods during the transaction:

```kotlin
fun onPaymentSuccess(successResponse: Any)
fun onPaymentFailure(failureResponse: Any)
fun onPaymentCancel(isTxnInitiated: Boolean)
fun onError(errorCode: Int, errorMessage: String)
fun generateHash(map: HashMap<String, String>, hashGenerationListener: PayUHashGeneratedListener)
fun mfaRegistrationstatus(status: Boolean)
```

### Callback Method Descriptions

| Method                  | Description                              |
| ----------------------- | ---------------------------------------- |
| `onPaymentSuccess`      | Called when payment is successful        |
| `onPaymentFailure`      | Called when payment fails                |
| `onPaymentCancel`       | Called when payment is cancelled         |
| `onError`               | Called when an error occurs              |
| `generateHash`          | Called to generate payment hash          |
| `mfaRegistrationstatus` | Called for biometric registration status |

### Hash Generation

Example for creating a hash in the `generateHash` callback:

```kotlin
val hashMap: HashMap<String, String> = HashMap()
hashMap[hashName] = hash // 'hashName' key and hash value
hashGenerationListener.onHashGenerated(hashMap)
```

#### Hash Generation Algorithm

1. Append your salt to `hashString`
2. Optionally append `postSalt` if provided
3. Use `SHA-512` on the final string to return the computed hash

> 📘 Hash Generation notes:
>
> * Append your `salt` to the `hashString` and use SHA-512 to generate the hash
> * If `postSalt` is provided, append it to the hashString after adding salt before hashing

### MFA registration status

It has a boolean parameter to determine the biometric registration status success/failure.

```
fun mfaRegistrationstatus(status: Boolean)
```

## Error codes

| Code | Description                          |
| ---- | ------------------------------------ |
| 0    | Success                              |
| 1    | Fail                                 |
| 3    | Challenge timeout                    |
| 4    | Challenge protocol error             |
| 5    | Challenge cancelled                  |
| 11   | Action null for headless flow        |
| 12   | Action params null for headless flow |
| 13   | Error while executing action         |
| 14   | Resend OTP limit exceeded            |
| 15   | Incorrect OTP                        |
| 16   | Transaction cancelled                |
| 17   | Transaction failed                   |
| 18   | Action Timeout                       |
| 101  | Card bin or card token was empty     |
| 102  | Merchant key null                    |
| 103  | Amount not in correct format         |
| 104  | Transaction ID null                  |
| 105  | Hash null                            |
| 106  | Card not supported on 3DS 2.0        |
| 107  | Card scheme not supported            |
| 108  | Hash incorrect                       |
| 500  | Something went wrong                 |
| 504  | Gateway timeout                      |

***

> 📘 Note:
>
> This integration guide covers the complete setup process for FlashPay Android SDK. Ensure proper implementation of all callback methods and error handling for a seamless user experience.