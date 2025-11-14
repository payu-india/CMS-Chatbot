---
title: FlashPay Coupled Flow Android Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
FlashPay solution primarily offers a single comprehensive SDK which is equipped to operate on 3DS protocols and additionally manages e2e authentication, including advanced biometric-based OOB authentication.

## 1. Gradle changes

<br />

9PayU SDK offers the following methods to integrate with 3DS 2.0:

* **SDK Integration**: Min SDK Version is v21 Compile SDK Version is v31 or later
* **Maven Dependency URL** Use the following code snippet in your app’s build.gradle file:

Add the following dependency in your app-level gradle file:

```groovy
implementation 'in.payu:threeds-sdk:1.1.2-SNAPSHOT'
```

* Use our SDK for a complete transaction:
  * Collecting device details
  * Invoking an authentication request through our 3DS Server
  * Invoking challenge
  * Completing authorization through PayU
  * Use our SDK for collecting device details and to render challenge screens.

## 2. Installation

### Payment initialisation method

Call the following `initiatePayment` method to initiate payment through us and we will return success or failure callback post transaction completion. This method will internally call Authentication request (/_payment), collect device detail, call binInfo API, present the native OTP screen and do the authorization too.

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

| Parameter       | Description                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `activity`      | This parameter contains the AppCompatActivity reference.                                                                                         |
| `config`        | Configuration object for customizing the FlashPay SDK                                                                                            |
| `paymentParams` | Payment-related details object. Merchants have to create the payment param object and pass it which will contain info such as cardDeatails, etc. |
| `callback`      | Callback for payment success, failure, cancellation, etc.                                                                                        |

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
config.authenticateOnly = true //Pass this as true if you want to authenticate only using PayU. By default we will authorize.
```

#### Customise UI with your content

To customise UI with your content,  pass these configurations:

```kotlin
config.enableCustomizedOtpUIFlow = true //To customise UI with your content please pass as true
config.enableTxnTimeoutTimer = true //pass as true to show timer for page timeout
config.merchantName = "merchant name" // pass merchant name with customised OTP Flow
config.amount = "txn amount" // pass transaction amount with customised OTP Flow
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

| Property                    | Description                                                                                                                                                                                    |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isProduction`              | `Boolean` Set environment where you want to test: `true` for the Production environment `false` for the Test environment                                                                       |
| `autoRead`                  | `Boolean` Set the values as `true` to allow auto-read OTP and fill in the OTP field. By default, the value is `false`.                                                                         |
| `autoSubmit`                | `Boolean` Set the values as `true` to submit the OTP automatically without any user interaction. By default, the value is `false`.                                                             |
| `enableMFAViaBiometric`     | `Boolean` If set `true`, users will receive an option to enable biometric authentication during payment via OTP. The biometric registration process starts after the payment success callback. |
| `enableCustomizedOtpUIFlow` | `Boolean` To customise UI with your content please pass as true                                                                                                                                |
| `enableTxnTimeoutTimer`     | `Boolean` pass as true to show timer for page timeout                                                                                                                                          |

#### Configuration Notes

* **setDefaultProgressLoader**: Customize via `config.setDefaultProgressLoader(true, "HexColor")`. This replaces the full-page loader with a default small loader.

## UI Customization

### Button Customization

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

### Toolbar Customization

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

### TextBox Customization

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

### Bottom Sheet Customization

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

### Font Customization

```kotlin
val fontFamilyCustomisation = FontFamilyCustomisation.Builder()
    .setHeaderFontFamily("Header Font family path") // example: assets/fonts/lato-italic.ttf
    .setSubTextFontFamily("Sub text font family path") // example: assets/fonts/lato-italic.ttf
    .build()
```

### UI Customization integration

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
        mPaymentParams.udf1 = "<User Defined Fields>"
        mPaymentParams.udf2 = "<User Defined Fields>"
        mPaymentParams.udf3 = "<User Defined Fields>"
        mPaymentParams.udf4 = "<User Defined Fields>"
        mPaymentParams.udf5 = "<User Defined Fields>"
        mPaymentParams.cardNumber = "<cardNumber>"
        mPaymentParams.nameOnCard = "<cardholderName>"
        mPaymentParams.expiryMonth = "<expiryMonth>"// MM
        mPaymentParams.expiryYear = "<expiryYear>"// YYYY
        mPaymentParams.cvv = "<cvv>"
        mPaymentParams.partnerWebhookSuccess = "<Webhook Success  URL>"
        mPaymentParams.partnerWebhookFailure = "<Webhook Failure  URL>"

```

### Required payment parameters

<Table align={[null,null,"left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key `mandatory`
      </td>

      <td>
        `String` This parameter must contain your merchant key received from PayU.
      </td>

      <td>
        "sms***"
      </td>
    </tr>

    <tr>
      <td>
        amount`mandatory`
      </td>

      <td>
        `String` Total transaction amount.
      </td>

      <td>
        100.0

        <br />
      </td>
    </tr>

    <tr>
      <td>
        productInfo`mandatory`
      </td>

      <td>
        `String`  Information about the product.
      </td>

      <td>
        "ProductInfo"

        <br />
      </td>
    </tr>

    <tr>
      <td>
        firstName `mandatory`
      </td>

      <td>
        `String` Customer's First Name
      </td>

      <td>
        "Firstname"

        <br />
      </td>
    </tr>

    <tr>
      <td>
        email`mandatory`
      </td>

      <td>
        `String` Customer's Email ID
      </td>

      <td>
        "[test@payu.in](mailto:test@payu.in)"
      </td>
    </tr>

    <tr>
      <td>
        txnId`mandatory`
      </td>

      <td>
        `String`  It should be unique for each transaction. Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "_,$,%,&, etc"
      </td>

      <td>
        4567890
      </td>
    </tr>

    <tr>
      <td>
        surl `mandatory`
      </td>

      <td>
        `String`  When the transaction is successful, PayU will load this URL and pass the transaction response.

        Sample SURL for testing*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
        Note*:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error.
      </td>

      <td>
        The Surl that you have configured

        <br />
      </td>
    </tr>

    <tr>
      <td>
        furl `mandatory`
      </td>

      <td>
        `String` When the transaction fails, PayU will load this URL and pass the transaction response.

        Sample FURL for testing*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
        Note*:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error.
      </td>

      <td>
        The Furl that you have configured

        <br />
      </td>
    </tr>

    <tr>
      <td>
        cardNumber
      </td>

      <td>
        `String` Card Number
      </td>

      <td>
        4080546540192009
      </td>
    </tr>

    <tr>
      <td>
        expiryMonth
      </td>

      <td>
        `String` Expiry MM
      </td>

      <td>
        12
      </td>
    </tr>

    <tr>
      <td>
        expiryYear
      </td>

      <td>
        `String` Expiry YYYY
      </td>

      <td>
        2025
      </td>
    </tr>

    <tr>
      <td>
        cvv
      </td>

      <td>
        `String` CVV
      </td>

      <td>
        123
      </td>
    </tr>

    <tr>
      <td>
        udf1 `optional`
      </td>

      <td>
        `String` User-defined field, Merchant can store their customer ID, etc.
      </td>

      <td>
        udf1
      </td>
    </tr>

    <tr>
      <td>
        udf2`optional`
      </td>

      <td>
        `String` User-defined field, Merchant can store their customer ID, etc.
      </td>

      <td>
        udf2
      </td>
    </tr>

    <tr>
      <td>
        udf3`optional`
      </td>

      <td>
        `String` User-defined field, Merchant can store their customer ID, etc.
      </td>

      <td>
        udf3
      </td>
    </tr>

    <tr>
      <td>
        udf4`optional`
      </td>

      <td>
        `String` User-defined field, Merchant can store their customer ID, etc.
      </td>

      <td>
        udf4
      </td>
    </tr>

    <tr>
      <td>
        udf5`optional`
      </td>

      <td>
        `String` User-defined field, Merchant can store their customer ID, etc.
      </td>

      <td>
        udf5
      </td>
    </tr>

    <tr>
      <td>
        partnerWebhookSuccess `optional`
      </td>

      <td>
        `String`When the transaction is successful, PayU will send webhook response in this URL and pass the transaction response.  [https://docs.payu.in/docs/webhooks#/](https://docs.payu.in/docs/webhooks#/)
      </td>

      <td>
        The success URL that you have configured
      </td>
    </tr>

    <tr>
      <td>
        partnerWebhookFailure `optional`
      </td>

      <td>
        `String` When the transaction is failed,  PayU will send webhook response in this URL and pass the transaction response. [https://docs.payu.in/docs/webhooks#/](https://docs.payu.in/docs/webhooks#/)
      </td>

      <td>
        The Failure URL that you have configured
      </td>
    </tr>
  </tbody>
</Table>

**Store Card**

To store the card, pass both userCredentials and storeCard

```kotlin Kotlin
     mpaymentParams.userCredentials = "XXXX:XXXX"
     mpaymentParams.storeCard = 1 or 0 

```

To make payment using stored card, pass userCredentials, network token and card token:

```kotlin
      mpaymentParams.userCredentials = "XXXX:XXXX"
      mpaymentParams.networkToken = <Network Token>
      mpaymentParams.cardToken = <Card Token>
```

> 📘 Saved Card Payments
>
> Requires both `networkToken` and `cardToken` under `mPaymentParams` for saved card-related transactions.

<br />

| Parameters      | Description                                                                                                                                                                                                                                                                                                                          | Example  |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| userCredentials | `String` It contains the merchant ID and a unique customer identifier. In this example, the user credentials that you submitted with the var1 parameter using the save_user_cards API. The format of the value is  _merchant key:user ID_                                                                                            | a:b      |
| storeCard       | `integer`  This is an existing field, where the card token flag is passed by merchant. The values for this field can be:                                                                                                                                                                                                             | 1        |
| networkToken    | `String` A network token is a tokenized representation of a card provided by the card network (e.g., Visa, Mastercard). It is used for processing payments at the network level and is required for certain API processes like binInfo API 1. Network tokens are typically used when a non-DI (Direct Integration) payment gateway . | abcdefgh |
| cardToken       | `String` A card token is a merchant-specific tokenized representation of a card. It is often used to store card information securely without exposing sensitive details. Merchants can store these tokens themselves or with a payment service provider like PayU.                                                                   | abcdefgh |

<br />

**EMI**
To process payments using EMI (Equated Monthly Installments), you need to specify the card details along with the bank code for EMI and set the payment gateway (PG) to "EMI".  Refer to [EMI Codes](https://docs.payu.in/docs/emi-codes)

```kotlin Kotlin
mPaymentParams.setBankCode("EMI03")                 // Bank code for EMI (e.g., EMI03)
mPaymentParams.setPg("EMI")                         // Set payment gateway to EMI
```

<br />

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

| Method                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onPaymentSuccess`      | Called when payment is successful. It will contain a success response. This will be a JSON Object, parse response as per your need.                                                                                                                                                                                                                                                                                                                                                 |
| `onPaymentFailure`      | Called when payment fails. t will contain a failure response. This will be a JSON Object, parse response as per your need                                                                                                                                                                                                                                                                                                                                                           |
| `onPaymentCancel`       | Called when payment is cancelled                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `onError`               | Called when an error occurs. It will contain failure reason code and reason.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `generateHash`          | Called to generate payment hash. Merchant will get a map with the type of hash and hash string as the value of the map.                                                                Refer to the <Anchor label="[hash-generation](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk)" target="_blank" href="https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk">[hash-generation](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk)</Anchor> |
| `mfaRegistrationstatus` | Called for biometric registration status (Registration/ De-registration)                                                                                                                                                                                                                                                                                                                                                                                                            |

### Hash Generation

You will receive a call on the generateHash method of PayU3DS2PaymentCallback.

In the method parameter, you will receive a dictionary or hashMap, and extract the value of hashString from that. Pass that value to the server, and now the server will append salt at the end and generate sha512 hash over it. The server will give that hash back to your app, and the app will provide that hash to PayU through a callback mechanism.

In the map, you have to check for the following keys to generate a hash:

* hashString
* hashName
* postSalt

  At the end of that hashString, append your salt and use the SHA-512 algorithm on that final string to generate a hash.

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

> 📘 Callout
>
> * If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algorithm on that final string to generate hash.
> * There is no need to know the formula for dynamic hashes because PayU SDK gives you the string containing all the required parameters. Your server has to append salt at the end and generate sha512 hash over it.

### MFA registration status

It has a boolean parameter to determine the biometric registration status success/failure.

```kotlin
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