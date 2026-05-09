---
title: FlashPay Coupled Flow iOS 3DS 2.0 SDK Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU's FlashPay SDK solution provides a robust biometric authentication solution for card transactions. FlashPay is a secure and efficient SDK that facilitates device biometric authentication for card transactions while being compliant with RBI guidelines for multi-factor authentication (MFA). The solution operates on existing 3DS protocols and includes advanced biometric-based out-of-band authentication (OOB).

This section outlines the technical specifications and integration requirements for implementing the PayU FlashPay SDK into merchant mobile applications. The document covers the following key integration touchpoints:

* Customer eligibility for FlashPay
* Customer registration flow
* Transaction authentication flow

The scenarios outlined are designed to work seamlessly with PayU or other Payment Aggregators (PA).

## Benefits

FlashPay offers significant advantages for both merchants and customers:

1. **Enhanced Performance**: Split-second biometric card payments with 4x reduced transaction latency
2. **Improved Success Rates**: 1.5-2% higher authentication success rates compared to traditional methods
3. **Enhanced Security**: Continuous monitoring and lifecycle management for secure transactions
4. **Seamless Fallback**: Automatic fallback to OTP-based authentication in case of biometric failures
5. **Minimal Integration**: Operates on existing 3DS infrastructure with minimal changes required
6. **Universal Support**: Compatible with all major card networks and supports various card types including:
   * Guest checkout
   * Alternative IDs
   * Network tokens
   * Issuer tokens
   * Tokenized cards

## SDK Integration

To integrate the FlashPay SDK into your mobile application, refer to the comprehensive integration documentation titled **"FlashPay_3DS SDK"** which contains detailed implementation steps, callback mechanisms, and communication protocols.

* Supported Operating Systems

| Platform | Version        | Device Support                           |
| -------- | -------------- | ---------------------------------------- |
| Android  | 6.0 and above  | Smartphones only (tablets not supported) |
| iOS      | 12.0 and above | iPhones only (iPads not supported)       |

* Customer Eligibility for FlashPay

Issuing banks provide a list of Bank Identification Numbers (BINs) that are eligible for the FlashPay Biometric MFA Solution. Merchants can use the BIN Info API to verify card eligibility in real-time.

### Key Pointers for Consideration

1. **Real-time Management**: Merchants can dynamically manage customer UX based on API responses
2. **Universal Application**: Can be used for both guest checkout scenarios and saved card transactions
3. **Mandatory Invocation**: API must be called every time card details are entered or selected
4. **Scalable Configuration**: System is configurable to automatically include BIN data for newly onboarded banks

## Customer Journey

This section details the step-by-step process for registering a customer's card for FlashPay biometric authentication during an inline transaction.

### Registration Workflow

The technical Implementation steps involves:

1. Checkout page is displayed with payment modes

<Image align="center" border={true} width="250px" src="https://files.readme.io/1ecd2143e141c7f95dc6af8af4917ec539f75c5cb2eda5101080c353753afe00-Flashpay_SDK_registration_flow_checkout_page.png" className="border" />

2. Customer selects eligible card for authentication.

<Image align="center" border={true} width="250px" src="https://files.readme.io/9a195225492306df95631d21b8db1b0fda12caba0d5dfb140344e213553bc45f-Flashpay_SDK_registration_flow_eligible_card_selection.png" className="border" />

3. Enters OTP for transaction authentication & opts to enroll for biometric authentication. Customer must select the **Set up your Face ID or Fingerprint for quick and secure payments** check box.

<Image align="center" border={true} width="250px" src="https://files.readme.io/dc14398d54d33890cde207fabccaa07f7ac400caf73508d00c18cc6a7120f4fb-Flashpay_SDK_registration_flow_otp-input.png" className="border" />

<Callout icon="📘" theme="info">
  **Note**: If the customer has not selected the **Set up your Face ID or Fingerprint for quick and secure payments** check box,  FlashPay SDK initiates biometric enrollment:

  <Image align="center" width="250px" src="https://files.readme.io/955ec58c28e9428b15f1acd6a8eb0b8bc1011df6ad6a910b635b8a35485e0a34-Flashpay_SDK_registraction_flow_biometric.png" />
</Callout>

5. Biometric credential is registered

<Image align="center" border={true} width="250px" src="https://files.readme.io/cb10d627d74c852966eb74f9d110a290c0013e4711eac08994b6c39e9aca7aef-Flashpay_SDK_registraction_flow_faceid.png" className="border" />

6. Mobile verification is done

<Image align="center" border={true} width="250px" src="https://files.readme.io/7023dd572c886b5280cb4bde0e23d65bb55df2656d5ecdab96827ae9e93ce66e-Flashpay_SDK_registration_flow_device_setting_up.png" className="border" />

7. FlashPay registration is complete

<Image align="center" border={true} width="250px" src="https://files.readme.io/afde344f38ca6e0ef3cbefdc4201b95335c84ee044948a57d2f292ee0369d072-Flashpay_SDK_registration_flow_device_success.png" className="border" />

### Key Registration Considerations

1. **Universal Application**: Registration process applies to both guest checkout and saved card scenarios
2. **Consent-Based Enrollment**: Biometric enrollment occurs post-OTP validation with explicit customer consent
3. **Status Management**: Enrollment status must be stored and managed by merchant in customer records
4. **Seamless Integration**: Process integrates seamlessly with existing transaction workflows

### Transaction Authentication Workflow

Customers who have successfully registered their cards with FlashPay can authenticate subsequent transactions using biometric authentication directly within the merchant application.

The technical implementation steps involves:

1. Customer selects enrolled card for authentication.

<Image align="center" border={true} width="250px" src="https://files.readme.io/9a195225492306df95631d21b8db1b0fda12caba0d5dfb140344e213553bc45f-Flashpay_SDK_registration_flow_eligible_card_selection.png" className="border" />

2. Authentication screen with auto-fallback capability

<Image align="center" border={true} width="250px" src="https://files.readme.io/f70f570575b4fccce24a8d3ab58c642d7ea98def1979668d63b35395c7475250-Flashpay_SDK_registration_flow_educate_about_biometrtic.png" className="border" />

3. Customer validation & biometric capture

<Image align="center" border={true} width="250px" src="https://files.readme.io/cb10d627d74c852966eb74f9d110a290c0013e4711eac08994b6c39e9aca7aef-Flashpay_SDK_registraction_flow_faceid.png" className="border" />

4. Transaction is complete.

<Image align="center" border={true} width="250px" src="https://files.readme.io/5c44d95ed40b62fd80467b939341bc1531f1311dc2ee5a99968c58d20f326aad-Flashpay_SDK_registration_flow_transaction_success.png" className="border" />

### Key Authentication Considerations

1. **Comprehensive Support**: Supports both guest checkout and saved card scenarios
2. **Robust Fallback**: Automatic fallback to OTP authentication when biometric validation is unavailable
3. **Multiple Communication Channels**: Validation statuses available via both SDK callbacks and webhooks
4. **Seamless Experience**: Authentication occurs entirely within merchant application environment

### Merchant Integration with Payment Aggregator APIs

The following APIs are required for complete Payment Aggregator integration:

1. **Get BIN Info API**: Fetch BIN eligibility status for FlashPay authentication
2. **Payment API**: Initiate authentication request with payment aggregator
3. **AuthN Callback**: Receive authentication status via webhook mechanism
4. **AuthN Data API**: Retrieve detailed authentication results from payment aggregator
5. **AuthZ API**: Process customer account debit following successful authentication

## Integration

With 3DS SDK, merchants will be able to provide a native experience rather than redirecting customer to a bank page. The UI is standardized according to EMVCO guidelines and offers customization. With 3DS 2.0, a native experience can only be provided in an app through a 3DS SDK.

### How it works?

1. SDK collects device details.
2. Post collecting device details, an authentication request has to be generated by passing device details.
3. Issuer ACS identifies to do a frictionless/ non frictionless flow and responds back with the details.
4. Basis of the details received, SDK initiates a request for non frictionless flow with ACS/ bank to complete the authentication. SDK renders the UI in a native format and asks the user to input the authentication mechanism and complete the authentication journey.
5. SDK relays back the response of authentication to merchant and then merchant has to be proceed for authorization of the transaction.

### Supported Flows

PayU 3DS SDK offers two types of solutions for transaction processing:

**Decoupled Flow:**

* Device detail collection and custom UI rendering
* Merchant handles authentication request generation
* Full control over frictionless/non-frictionless flows

**Complete Transaction Flow:**

* End-to-end payment processing through PayU
* Simplified integration with built-in authentication handling

### Step 1. Install the SDK in your app project (mandatory)

<Callout icon="📘" theme="info">
  Minimum supported iOS version :  iOS 13
</Callout>

#### CocoaPods Integration

1. Add the following line to use dynamic frameworks in your Podfile.

```ruby
use_frameworks!
```

2. Install the dependencies using the command:

```bash
pod 'PayUIndia-3DS2-SDK', '3.0.0.alpha.1'
pod install
```

#### Swift Package Manager Integration

**Using Xcode:**

1. Navigate to **File > Add Package** in Xcode
2. Add the following URL:
   ```
   https://github.com/payu-intrepos/PayU3DS2SDK-iOS
   ```

**Using Package.swift:**

1. Add the following line in the `Package.swift` dependencies:

```swift
.package(name: "PayUIndia-3DS2-SDK", url: "https://github.com/payu-intrepos/PayU3DS2SDK-iOS", from: "3.0.0.alpha.1")
```

#### Import Statement

Add the following import in the class where you need to initiate a payment:

```swift
import PayU3DS2Kit
```

### Step 2: Configure SDK

Configure the SDK using the `PayU3DS2Config` object with the following properties:

```swift
var config = PayU3DS2Config()
config.uiCustomisation = "set UI customisation object, refer below section of UI Customisation"
config.isProduction = "set environment where you want to test, true for production and false for sandbox"
config.fallback3DS1 = true //default value false, send true to complete payment on bank page in case of any failure
config.autoSubmit = false //Set the values as true to submit the OTP automatically without any user interaction. By default, the value is false.
config.initialiseTimeoutTimer = 5 //provide time in seconds, for waiting for merchant response
config.supportedUIMode = ArrayList<String> //to show own UI, currently accepted value = 01. Pass this if you want to create own UI and follow step 4.1 and 4.2
config.enableMFAViaBiometric = true // if set to true, then during payment via OTP, there will an option to enable biometric authentication. 
// If selected, the biometric registration process will start after payment success callback is triggered.
// Can also set progress indicator
config.setDefaultProgressLoader(showDefaultLoader: true, defaultProgressLoaderColor: "HexColor") //to show default loader instead of full page loader pass true, and to change color of progress bar pass valid hexcode
//To customise UI with your content please pass these configurations
config.enableCustomizedOtpUIFlow = true
config.enableTxnTimeoutTimer = true //pass as true to show timer for page timeout
config.merchantName = "merchant name" 
config.amount = "txn amount"
config.enableTxnTimeoutTimer = true
config.acsContentConfig = PayU3DS2ACSContentConfig()
config.acsContentConfig?.submitButtonTitle = "Submit Button Title"
config.acsContentConfig?.resendButtonTitle = "Resend Button Title"
config.acsContentConfig?.otpContent = "OTP has been sent to your registered mobile number". //you can set this value to as per your need
config.acsContentConfig?.resendInfoContent = "Submit Button Title"
config.acsContentConfig?.maxResendInfoContent = "Max Retry Content"
```

#### Configuration properties

| Property                    | Description                                                                    |
| --------------------------- | ------------------------------------------------------------------------------ |
| `isProduction`              | Set environment (true for production, false for sandbox).                      |
| `fallback3DS1`              | Complete payment on bank page in case of failure. By default, value is "false" |
| `autoSubmit`                | Submit OTP automatically. By default, value is "false"                         |
| `initialiseTimeoutTimer`    | Timeout in seconds for merchant response. By default, value is "5"             |
| `enableMFAViaBiometric`     | Enable biometric authentication for OTP flow                                   |
| `enableCustomizedOtpUIFlow` | Enable customized OTP UI flow                                                  |
| `enableTxnTimeoutTimer`     | Enable transaction timeout timer                                               |

### Step 3: UI customization

#### Button customization

```swift
var buttonCustomisation = PayU3DS2ButtonCustomisation(
    textFontColor: "#ffffff",
    textFontSize: 17,
    backgroundColor: "#25272C",
    cornerRadius: 10,
    resendButtonTextFontColor: "#25272C"
)
```

#### Label customization

```swift
var labelCustomisation = PayU3DS2LabelCustomisation(
    textFontColor: "#000000",
    textFontSize: 14,
    headingTextColor: "#000000",
    headingTextFontSize: 16
)
```

#### Toolbar customization

```swift
var toolbarCustomisation = PayU3DS2ToolBarCustomisation(
    textFontColor: "#ffffff",
    textFontSize: 18,
    backgroundColor: "#25272C",
    buttonText: "Pay Now",
    headerText: "Secure Payment"
)
```

#### TextBox customization

```swift
var textBoxCustomisation = PayU3DS2TextBoxCustomisation(
    textFontColor: "#000000",
    textFontSize: 16,
    borderColor: "#CCCCCC",
    borderWidth: 1,
    cornerRadius: 8
)
```

#### Font Family Customization

```swift
var fontFamilyCustomisation = PayU3DS2FontFamilyCustomisation(
    headerFontFamily: "Roboto-Medium",
    subTextFontFamily: "Roboto-Regular"
)
```

#### UI Customization integration

```
var uiCustomisation = PayU3DS2UICustomisation(
        buttonCustomisation: buttonCustomisation,
        labelCustomisation: labelCustomisation,
        textBoxCustomisation: textBoxCustomisation,
        toolbarCustomisation: toolbarCustomisation,
        fontFamilyCustomisation: fontFamilyCustomisation,
        textCustomisation: textCustomisation
    )
config.uiCustomisation = uiCustomisation
```

> 🚧 3DS Warnings:
>
> The result for device security checks like rootedDevice, isDebuggable, isEmulator and is OS Supported will be provided in result of init as given in above sample code. It is upto requestor app to handle the warnings as per the requirement.

### Step 4: SDK Initialisation

Call below method to initiate payment through us and we will return success or failure callback post transaction completion.

### Payment Initiation Method

```swift
PayU3DS2.initiatePayment(
    vc: UIViewController,
    config: PayU3DS2Config,
    paymentParams: PayU3DS2PaymentParam,
    delegate: PayU3DS2Delegate
)
```

#### Payment parameters setup

> 📘 Notes:
>
> * **vc**: Parent ViewController Object
> * **config**: It contains multiple properties. For more information, refer to [Step 3: UI customization](#step-3-ui-customization).
> * **paymentParams**: You have to create payment parameter object and pass it which will contains info like: cardDeatails, SI details etc.

**PayU3DS2PaymentParam**

```swift
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
udfs.udf1 = "<User Defined Field>"
paymentParam.udfs = udfs

var cardDetails = PayU3DS2CardInfo()
cardDetails.cardNumber = "<Card Number>"
cardDetails.cardName = "<Card Name>"
cardDetails.nameOnCard = "John Doe"
cardDetails.expiryMonth = "01"
cardDetails.expiryYear = "2025"
cardDetails.cvv = "123"
paymentParam.userCredential = "<XXXX:XXXX>"

// For Stored Card with PayU Token
cardDetails.cardToken = "<Card Token>"

Note: To make payment using another payment aggregator vault saved card.
cardDetails.networkToken = "<networkToken>"
paymentParam.additionalParam = ["last4Digits" : "6702", "tavv": "/wAAAAAARebB4YIAmbHTgmoAAAA=","trid" : "40020003934", "tokenRefNo": "2b7f916e790ff9d551cf145fbc9bee0b"]
paymentParam.cardTokenTpe = "1" //if passing networkToken otherwise value = 0 if you will pass cardToken
paymentParam.partnerWebhookSuccess = "<url>"
paymentParam.partnerWebhookFailure = "<url>"
paymentParam.isPreAuthTxn = true //Optional - Set this as true for pre auth transactions
paymentParam.cardinfo = cardDetails
```

**SI Payments**:

```
let siInfo = PayU3DS2SIParams(
        billingAmount: String?, // Set billing amount in String
        paymentStartDate: Date?, // Set start date of SI
        paymentEndDate: Date?,  // Set end date of SI
        billingCycle: PayU3DS2BillingCycle, // Set billing cycle of SI
        billingInterval: Int, // Set billing interval of SI
        isFreeTrial: Bool, // Set free trail of SI, the default is false
        remarks: String?, // Set remarks of SI
        billingLimit: String?, // Set remarks of SI
        billingRule: String?, // Set remarks of SI
)

paymentParam.siParam = siInfo
```

**PayU3DS2BillingCycle**

```
enum PayU3DS2BillingCycle {
    case once
    case daily
    case weekly
    case monthly
    case yearly
    case adhoc
}

```

**EMI Transaction:** EMI To process payments using EMI (Equated Monthly Installments), you need to specify the card details along with the bank code for EMI and set the payment gateway (PG) to "EMI". Refer to <Anchor label="EMI Codes" target="_blank" href="https://docs.payu.in/docs/emi-codes">EMI Codes</Anchor>

```
paymentParam.pgCode = "PG_Code" // Set payment gateway to EMI
paymentParam.bankCode = "<Bank Code>" // Bank code for EMI (e.g., EMI03)

```

#### Request parameters

> 📘 All the parameters are mandatory

| Parameter                 | Description                                                             |
| :------------------------ | :---------------------------------------------------------------------- |
| key `mandatory`           | Merchant key issued by PayU                                             |
| transactionId `mandatory` | Unique transaction identifier                                           |
| amount `mandatory`        | Transaction amount                                                      |
| productInfo `mandatory`   | Product description                                                     |
| firstName `mandatory`     | Customer first name                                                     |
| email `mandatory`         | Customer email                                                          |
| phone `mandatory`         | Customer phone number                                                   |
| surl `mandatory`          | Success URL                                                             |
| furl  `mandatory`         | Failure URL                                                             |
| udfs.udf1 `optional`      | `String` User-defined field, Merchant can store their customer ID, etc. |
| udfs.udf2`optional`       | `String` User-defined field, Merchant can store their customer ID, etc. |
| udfs.udf3`optional`       | `String` User-defined field, Merchant can store their customer ID, etc. |
| udfs.udf4`optional`       | `String` User-defined field, Merchant can store their customer ID, etc. |
| udfs.udf5`optional`       | `String` User-defined field, Merchant can store their customer ID, etc. |

### Card Information

> 📘 All the parameters are mandatory

| Parameter      | Description                                                                                                                                                                                                                                                                                                                 |    |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :- |
| `cardNumber`   | Card number                                                                                                                                                                                                                                                                                                                 |    |
| `cardName`     | Card name                                                                                                                                                                                                                                                                                                                   |    |
| `nameOnCard`   | Name on card                                                                                                                                                                                                                                                                                                                |    |
| `expiryMonth`  | Expiry month                                                                                                                                                                                                                                                                                                                |    |
| `expiryYear`   | Expiry year                                                                                                                                                                                                                                                                                                                 |    |
| `cvv`          | Card CVV                                                                                                                                                                                                                                                                                                                    |    |
| userCredential | The merchant ID and a unique customer identifier.                                                                                                                                                                                                                                                                           |    |
| cardToken      | A card token is a merchant-specific tokenized representation of a card. It is often used to store card information securely without exposing sensitive details. Merchants can store these tokens themselves or with a payment service provider like PayU.                                                                   |    |
| networkToken   | A network token is a tokenized representation of a card provided by the card network (e.g., Visa, Mastercard). It is used for processing payments at the network level and is required for certain API processes like binInfo API 1. Network tokens are typically used when a non-DI (Direct Integration) payment gateway . |    |
| cardTokenType  | Pass 1 if networkToken is passed                                                                                                                                                                                                                                                                                            |    |

<br />

### Delegate methods implementation

Implement the following delegate methods in your `PayU3DS2Delegate`:

* Payment success

```swift
func onPaymentSuccess(successResponse: Any?)
```

* Payment failure

```swift
func onPaymentFailure(failureResponse: Any?)
```

* Payment cancellation

```swift
func onPaymentCancel(isTxnInitiated: Bool)
```

* Error response

```swift
func onError(errorCode: Int, errorMessage: String)
```

* Hash generation

```swift
func generateHash(for param: [String: String], onCompletion: @escaping PayU3DS2HashGenerationCompletion)
```

* MFA registration status

```swift
func mfaRegistrationstatus(response: Any?) // Downcast response to type PayU3DS2MFAResponse

class PayU3DS2MFAResponse {
    var type: PayU3DS2MFARequestType // Request Type registration or deregistration
    var status: PayU3DS2MFAStatus // Request Status initiated, success, or error
    var timeout: Int // Txn Timeout in seconds
}

enum PayU3DS2MFARequestType {
    case registration
    case deregistration
}

enum PayU3DS2MFAStatus {
    case initiated
    case success
    case error
}

```

### Callback Method Descriptions

| Method                  | Description                                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `onPaymentSuccess`      | Called when payment is successful. It will contain a success response. This will be a JSON Object, parse response as per your need.                                                                                                                                                                                                               |
| `onPaymentFailure`      | Called when payment fails. It will contain a failure response. This will be a JSON Object, parse response as per your need                                                                                                                                                                                                                        |
| `onPaymentCancel`       | Called when payment is cancelled                                                                                                                                                                                                                                                                                                                  |
| `onError`               | Called when an error occurs. It will contain failure reason code and reason.                                                                                                                                                                                                                                                                      |
| `generateHash`          | Called to generate payment hash. Merchant will get a map with the type of hash and hash string as the value of the map.                                                                Refer to the <Anchor label="hash-generation" target="_blank" href="https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk">hash-generation</Anchor> |
| `mfaRegistrationstatus` | Called for biometric registration status (Registration/ De-registration)                                                                                                                                                                                                                                                                          |

### Error codes

| Code | Description                             |
| ---- | --------------------------------------- |
| 0    | Success                                 |
| 1    | Fail/Invalid params                     |
| 2    | Error while creating transaction        |
| 3    | Timeout                                 |
| 4    | Challenge protocol error                |
| 5    | User canceled the transaction           |
| 6    | Runtime Error                           |
| 12   | Action params missing for headless flow |
| 14   | Resend OTP limit exceeded               |
| 15   | Incorrect OTP code                      |
| 17   | Transaction failed                      |
| 105  | Hash cannot be nil                      |
| 106  | Card not supported on 3DS 2.0           |
| 107  | Card scheme not supported               |
| 108  | Invalid hash                            |
| 109  | Invalid ACS UI Type                     |
| 500  | Something went wrong                    |
| 503  | Error while creating transaction        |
| 31   | User opted for OTP authentication       |
| 32   | Device deregistered                     |
| 33   | RBA transaction error                   |
| 34   | RBA Registration failed                 |
