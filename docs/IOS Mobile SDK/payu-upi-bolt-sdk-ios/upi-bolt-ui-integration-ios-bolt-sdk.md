---
title: UPI Bolt UI Integration - iOS Bolt SDK
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
## Prerequisites

- SDK Compatibility  
- Supported iOS deployment target - iOS 17 and above.

## UI Bolt Integration

Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use **PayU UPI Bolt UI SDK** for customer registration, payment, and profile management. 

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile. 

```
pod 'PayUIndia-UPIBoltUIKit', '~> 1.0.0-alpha.0'
```

The following xcframework files will be provided by PayU during onboarding.

- **NPCI** - CommonLibrary.xcframework
- **AXIS** - OlivePayLibrary.xcframework 

Add these framework in your project.

The added framework is similar to the following screenshot:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/227250da5bb54c8967c59370aac96e27be792b9224dc4a61b536efe539aa2429-bolt_added_framework.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


To integrate UPI Bolt UI on iOS SDK platform:

## Step 1: Initialization

 It is used to initialize the SDK. This method returns a object that will be used to access other methods available in `PayUUPIBoltUI`.

```swift
let config = PayUUPIBoltUIConfig(
              merchantName: "<merchantName>", // String
              merchantKey: "<merchantKey>" // String,
              phone: "<phone>", // String
              email: "<email>", // String
              refId: "<refId>", // String
              pluginTypes: ["<pluginType>"], // Array<String>
              excludedBanksIINs: ["<excludedBanksIIN>"], // Array<String>
              isProduction: <isProduction> // Bool
             )

// To initialize the SDK
val boltUI = PayUUPIBoltUI.initSDK(
            parentVC: <parentVC>, // UIViewController
            config: <config>, // PayUUPIBoltUIConfig
            delegate: <self> // Reference to delegate
          )

// To get the already initialised object
let boltUI = PayUUPIBoltUI.getInstance()

// To clear the SDK Instance
PayUUPIBoltUI.reset() 

```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Description",
    "0-0": "parentVC  \n`mandatory`",
    "0-1": "`UIViewController` Calling VC of the merchant App ",
    "1-0": "delegate  \n`mandatory`",
    "1-1": "`PayUUPIBoltUIDelegate` Delegates to receive response",
    "2-0": "config  \n`mandatory`",
    "2-1": "`PayUUPIBoltUIConfig` PayUUPIBoltUIConfig includes the below fields. ",
    "3-0": "merchantName  \n`mandatory`",
    "3-1": "`String` Merchant Name",
    "4-0": "merchantKey  \n`mandatory`",
    "4-1": "`String` PayU Merchant Key",
    "5-0": "phone  \n`mandatory`",
    "5-1": "`String` Phone number for registration",
    "6-0": "email  \n`mandatory`",
    "6-1": "`String` Customer Email Id",
    "7-0": "pluginTypes  \n`mandatory`",
    "7-1": "`Array <String>` List of Supported Plugin (Values - AXIS or HDFC)",
    "8-0": "isProduction  \n`mandatory`",
    "8-1": "`Boolean` This parameter must contain any of the following: true - Production environment, false - Test or Staging environment",
    "9-0": "excludedBanksIINs  \n`mandatory`",
    "9-1": "`Array <String>` List of Bank’s IIN to exclude",
    "10-0": "refId  \n`optional`",
    "10-1": "`String` Unique reference ID"
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 2: Check if UPI Bolt SDK is available

      The **isUPIBoltSDKAvailable** API allows you to manage UPI accounts and transaction history.

```swift
boltUI.isUPIBoltSDKAvailable(callback: PayUUPIBoltUICallBack)
```

For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

 The following fields are needed as a request for this API: 

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n`mandatory`",
    "0-1": "`PayUUPIBoltUI `Callback Ref. 6"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 3: Register and pay

The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener. 

```swift
boltUI.registerAndPay(paymentParams PayUUPIBoltPaymentParams)
```

For paymentParams, pass `PayUUPIBoltPaymentParams` instance. For more information, refer to [ Generate PayU Payment Params](#step-5-generate-payu-payment-params).

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "paymentParams  \n`mandatory`",
    "0-1": "`PayUUPIBoltPaymentParams` Ref. 5"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 4: Open UPI Management

The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

```swift
boltUI.openUPIManagement(screenType: PayUUPIBoltUIScreenType) // Screen Types enum PayUUPIBoltUIScreenType: Int {    case all    case transactionHistory    case manageUPIAccounts    case dispute    case deregisterUPI }\`
```

For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

 The following fields are needed as a request for this API: 

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "screenType  \n`mandatory`",
    "0-1": "`PayUUPIBoltUIScreenType` To enforce the management screen"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 5: Generate PayU payment params

The **PayUPaymentParams API** is used to generate PayU payment parameters.

```swift
var paymentParams = PayUUPIBoltPaymentParams(
    transactionId: "<transactionId>", // Replace with actual transaction ID
    amount: "<amount>", // Replace with actual amount
    productInfo: "<productInfo>", // Replace with actual product info
    firstName: "<firstName>", // Replace with actual first name
    surl: "<surl>", // Replace with actual success URL
    furl: "<furl>" // Replace with actual failure URL
)

paymentParams.additionalParam = ["key": "value"] // Optional to pass any additional information

let udfs = PayUUPIBoltUserDefines()
udfs.udf1 = "<udf1>" // Replace with actual value or nil
udfs.udf2 = "<udf2>" // Replace with actual value or nil
udfs.udf3 = "<udf3>" // Replace with actual value or nil
udfs.udf4 = "<udf4>" // Replace with actual value or nil
udfs.udf5 = "<udf5>" // Replace with actual value or nil
udfs.udf6 = "<udf6>" // Replace with actual value or nil

paymentParams.udfs = udfs // Optional User defined fields
```

The following fields are needed as a request:  

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "amount  \n`mandatory`",
    "0-1": "`String` Amount to make payment",
    "1-0": "transactionId  \n`mandatory`",
    "1-1": "`String`  Unique transaction ID",
    "2-0": "productInfo  \n`mandatory`",
    "2-1": "`String` Product description.",
    "3-0": "firstName  \n`mandatory`",
    "3-1": "`String`  First name of the user",
    "4-0": "furl  \n`optional`",
    "4-1": "`String` Failure callback URL",
    "5-0": "surl  \n`optional`",
    "5-1": "`String` Success callback URL ",
    "6-0": "udf1  \n`optional`",
    "6-1": "`String` User-defined fields 1",
    "7-0": "udf2  \n`optional`",
    "7-1": "`String` User-defined fields 2",
    "8-0": "udf3  \n`optional`",
    "8-1": "`String` User-defined fields 3",
    "9-0": "udf4  \n`optional`",
    "9-1": "`String` User-defined fields 4",
    "10-0": "udf5  \n`optional`",
    "10-1": "`String` User-defined fields 5",
    "11-0": "udf6  \n`optional`",
    "11-1": "`String` User-defined fields 6"
  },
  "cols": 2,
  "rows": 12,
  "align": [
    null,
    null
  ]
}
[/block]


## Step 6: Check PayU UPI Response

The **PayUUPIResponse** API is used to check the response.

| Fields  | Definition                        |
| ------- | --------------------------------- |
| code    | `Integer` Error or success code   |
| message | `String` Error or success message |
| result  | `Object` Response data            |

## Hash generation logic

The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. 

To generate and pass dynamic hashes, the merchant will receive a call from the `generateHash` method of **PayUUPIBoltUIDelegate**. The SDK calls the `generateHash` method each time it needs an individual hash.

```swift
func generateHash(for param: [String: String], 
                  onCompletion: @escaping PayUUPIBoltHashGenerationCompletion) {
    // Your implementation here
}
```

The merchant receives a dictionary containing the type of hash and the corresponding hash string as its values. The merchant needs to sign the provided hash string using their salt to create the final hash and pass it back via the completion handler. param: This dictionary contains two keys: 

- **hashName** - The name of the command. 
- **hashString** - The hash string, without the salt. PayUUPIBoltHashGenerationCompletion: This completion handler contains the hashDict parameter.
- **hashDict**: Provide a dictionary where the hashName is the key, and the generated hash is the value. To generate the hash, you need to combine the hashString with the salt on your server and apply the SHA-512 algorithm and pass it back via the completion handler

### Listener or Callback logic

The listener/callback contains 4 methods where the merchant app will get the API response and hash-related callbacks.

| Method                                                                                                         | Purpose                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| func onPayUSuccess(response: PayUUPIBoltResponse)                                                              | It will contain success response.                                              |
| func onPayUFailure(response: PayUUPIBoltResponse)                                                              | It will contain failure response                                               |
| onPayUCancel(isTxnInitiated: Bool)                                                                             | It will tell if payment was cancelled                                          |
| func generateHash(for param: \[String: String\], onCompletion: @escaping PayUUPIBoltHashGenerationCompletion): | For hash generation, refer to [Hash generation logic](#hash-generation-logic). |

## Error codes and error message list

| Codes | Message                                |
| ----- | -------------------------------------- |
| 0     | Success                                |
| 1     | Fail/ Invalid Response/ Missing params |
| 2     | User canceled the transaction          |
| 100   | Transaction timeout                    |
| 101   | Hash missing                           |
| 102   | Incorrect Hash                         |
| 103   | Handshake failed                       |
| 104   | UPI bolt not supported                 |
| 105   | Device not supported for UPI Bolt      |
| 106   | Permission missing                     |
| 107   | Sim info not available                 |
| 108   | Device binding failed                  |
| 500   | Something went wrong                   |
| 501   | No internet connection                 |