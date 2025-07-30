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

```kotlin
var config = PayU3DS2Config()
config.uiCustomisation = "set UI customisation object, refer below section of UI Customisation"
config.isProduction = true // true for production, false for sandbox
config.autoRead = false // Auto-read OTP, default is false.
config.autoSubmit = false // Auto-submit OTP, default is false.
config.setDefaultProgressLoader(true, "HexColor") // Custom or default progress loader
config.enableMFAViaBiometric = true // Biometric registration after payment success
config.enableCustomizedOtpUIFlow = true // Customized OTP UI
config.enableTxnTimeoutTimer = true // Enable timeout timer for pages
config.merchantName = "<merchant name>"
config.amount = "<txn amount>"
```

#### ACS content configurations

Customize OTP and related properties:

```kotlin
val acsContentConfig = ACSContentConfig()
acsContentConfig.otpContent = "OTP has been sent to your registered mobile number"
acsContentConfig.resendButtonTitle = "Resend OTP"
acsContentConfig.submitButtonTitle = "Submit"
acsContentConfig.resendInfoContent = "You can resend OTP after X seconds"
acsContentConfig.maxResendInfoContent = "Max resend attempts reached"
config.acsContentConfig = acsContentConfig
```

#### Configuration properties

<Table>
  <thead>
    <tr>
      <th>
        Property
      </th>

      <th>
        Description
      </th>

      <th>
        Default
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `isProduction`
      </td>

      <td>
        true for production, false for sandbox
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        `autoRead`
      </td>

      <td>
        Auto-read OTP
      </td>

      <td>
        false
      </td>
    </tr>

    <tr>
      <td>
        `autoSubmit`
      </td>

      <td>
        Auto-submit OTP
      </td>

      <td>
        false
      </td>
    </tr>

    <tr>
      <td>
        `enableMFAViaBiometric`
      </td>

      <td>
        Biometric registration after payment success
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        `enableCustomizedOtpUIFlow`
      </td>

      <td>
        Customized OTP UI
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        `enableTxnTimeoutTimer`
      </td>

      <td>
        Enable timeout timer for pages
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

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
var mPaymentParams = PaymentParams()
mPaymentParams.key = "<Your Key issued by PayU>"
mPaymentParams.amount = "<Transaction Amount>"
mPaymentParams.productInfo = "<Product Description>"
mPaymentParams.firstName = "<Customer First Name>"
mPaymentParams.email = "<Customer Email>"
mPaymentParams.txnId = "<Transaction Id>"
mPaymentParams.surl = "<Success URL>"
mPaymentParams.furl = "<Failure URL>"
mPaymentParams.userCredentials = "XXXX:XXXX"
mPaymentParams.cardNumber = "<Card Number>"
mPaymentParams.expiryMonth = "<Expiry MM>"
mPaymentParams.expiryYear = "<Expiry YYYY>"
mPaymentParams.cvv = "<CVV>"
mPaymentParams.storeCard = if (true) 1 else 0
```

### Payment parameters

> 📘 All parameters mandatory

| Parameter     | Description             |
| ------------- | ----------------------- |
| `key`         | Your Key issued by PayU |
| `amount`      | Transaction Amount      |
| `productInfo` | Product Description     |
| `firstName`   | Customer First Name     |
| `email`       | Customer Email          |
| `txnId`       | Transaction Id          |
| `surl`        | Success URL             |
| `furl`        | Failure URL             |
| `cardNumber`  | Card Number             |
| `expiryMonth` | Expiry MM               |
| `expiryYear`  | Expiry YYYY             |
| `cvv`         | CVV                     |

<Cards columns={4}>
  <Card title="First Card" href="https://readme.com" icon="fa-home" target="_blank">
    Neque porro quisquam est qui dolorem ipsum quia
  </Card>

  <Card title="Second Card" icon="fa-user">
    *Lorem ipsum dolor sit amet, consectetur adipiscing elit*
  </Card>

  <Card title="Third Card" icon="fa-star">
    > Ut enim ad minim veniam, quis nostrud ullamco
  </Card>

  <Card title="Fourth Card" icon="fa-question">
    **Excepteur sint occaecat cupidatat non proident**
  </Card>
</Cards>

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

### Hash Generation Notes

* Append your `salt` to the `hashString` and use SHA-512 to generate the hash
* If `postSalt` is provided, append it to the hashString after adding salt before hashing

### Biometric Registration

* **Biometric Registration Status**: Biometric registration (MFA) success/failure can be determined via a callback

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