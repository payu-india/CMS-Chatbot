---
title: UPI Bolt UI SDK Integration
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
UPI Bolt UI SDK allows you to manage the checkout options on their checkout screen. You use **PayU UPI Bolt UI SDK** for customer registration, payment and profile management. This integration involves the following steps:

1. [Add permissions to Manifest file](#step-1-add-permissions-to-manifest-file)
2. [Include Bolt UI SDK and AAR Files](#step-2-include-bolt-ui-sdk-and-aar-files)
3. [Initialize the SDK](#step-3-initialize-the-sdk)
4. [Check for UPI Bolt SDK availability](#step-4-check-for-upi-bolt-sdk-availability)
5. [Register and pay](#step-5-register-and-pay)

For hash generation logic and Listener/Callback integration, the [Hash generation logic ](#hash-generation-logic)and  [Listener or Callback logic](#listener-or-callback-logic) sub-sections.

## Prerequisites

- Minimum Android SDK Version - 23 and above.
- Compile SDK Version - 31 and above.
- The following .aar (Android archive) files provided by PayU during onboarding:
  1. NPCI Secure Component
  2. AXIS Olive

## Step 1: Add permissions to Manifest file

Update the manifest file to include the following so that permissions are provided for SDK:

```
// To send SMS for device binding
<uses-permission android:name="android.permission.SEND_SMS"/>
// To check current network state
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
// To access internet for API calls 
<uses-permission android:name="android.permission.INTERNET" />
// To get sim details from devices below or equal to 29
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
// Too get sim details from devices above 29
<uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
// To provide location details for transaction
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

## Step 2: Include Bolt UI SDK and AAR Files

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your app’s `build.gradle`.

```
implementation 'in.payu:payu-upi-bolt-axis-wrapper-sdk:0.0.1' // PayU AXIS Wrapper
implementation 'in.payu:payu-upi-bolt-ui-sdk:0.0.1' // PayU Bolt SDK
```

Add the .aar files provided by PayU during onboarding. in the **libs** directory of your android module and add these in module level **build.gradle**. For the list of files, refer to[ Prerequisites](#prerequisites).

```
api(files("$projectDir/libs/SecureComponent-release-prod_05062024_9d3904ab.aar")) // NPCI .aar
api(files("$projectDir/libs/oliveupi-payu-release_PROD_02-12-2024_2.0.2.aar")) // AXIS .aar 
```

The screenshot of libs directory is similar to the following:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1af3684beef4a3b10716b5fc7de478bc9a07ff6f82ae0cec8041bbb94d8c754c-bolt_native_flow_aar_directory_structure.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "360px"
    }
  ]
}
[/block]


## Step 3: Initialize the SDK

It is used to initialize the SDK. This method returns a object that will be used to access other methods available in `PayUUPIBoltUI`.

```kotlin
val bolt = PayUUPIBoltUI.getInstance(
    activity: AppCompatActivity,
    config: PayUUPIBoltConfig,
    hashGenerationListener: PayUHashGenerationListener
)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "activity  \n` mandatory`",
    "0-1": "`AppCompatActivity` Calling activity of the merchant App",
    "1-0": "config  \n` mandatory`",
    "1-1": "`PayUUPIBoltUIConfig` Config includes the below fields.",
    "2-0": "hashGenerationListener  \n` mandatory`",
    "2-1": "`PayUHashGenerationListener` Callback listener for hash generation",
    "3-0": "merchantKey  \n` mandatory`",
    "3-1": "`String`PayU Merchant Key",
    "4-0": "phone  \n` mandatory`",
    "4-1": "`String`Phone number for registration",
    "5-0": "email  \n` mandatory`",
    "5-1": "`String`Customer Email Id",
    "6-0": "pluginType  \n` mandatory`",
    "6-1": "`String Array`List of Supported Banks (“AXIS, HDFC”)",
    "7-0": "isProd  \n` optional`",
    "7-1": "`Boolean`Prod - ture, staging - false",
    "8-0": "excludedBanksIINs  \n` optional`",
    "8-1": "`String Array`List of Bank’s IIN to exclude",
    "9-0": "requestId  \n` mandatory`",
    "9-1": "`String`Unique reference ID"
  },
  "cols": 2,
  "rows": 10,
  "align": [
    null,
    null
  ]
}
[/block]


### Response

| Response Params | Definition                                 |
| --------------- | ------------------------------------------ |
| `PayUUPIBoltUI` | PayUUPIBoltUI object for invoking SDK APIs |

> 📘 Callback:
> 
> After the SDK is initialised, use the same object to call the sdk methods.

## De-initialise PayUBolt UI SDK

`reset`: This method is used to deinitailise the bolt object. 

```
`PayUUPIBoltUI.reset()`
```

## Step 4: Check for UPI Bolt SDK availability

The **isUpiBoltEnabled** API allows you to manage UPI accounts and transaction history.

```kotlin
boltUI.isUpiBoltEnabled(callback: (PayUUPIBoltResponse) -> Unit)
```

## Step 5: Register and Pay

The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

```swift ionic
boltUI.registerAndPay(paymentParams PayUUPIBoltPaymentParams, callback: PayUUPIBoltUICallBack)

```

> 📘 Callback reference:
> 
> For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Definition",
    "0-0": "paymentParams  \n`mandatory`",
    "0-1": "**Object** This parameter includes the fields listed in the ",
    "1-0": "callback  \n`mandatory`",
    "1-1": "**PayUUPIBoltUICallBack** This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### paymentParams object

The following fields are part of `paymentParams` object:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Definition",
    "0-0": "amount  \n`mandatory`",
    "0-1": "`String` Amount to be paid",
    "1-0": "txnId  \n`mandatory`",
    "1-1": "`String`Unique transaction ID",
    "2-0": "productInfo  \n`mandatory`",
    "2-1": "`String`Product description",
    "3-0": "firstName  \n`mandatory`",
    "3-1": "`String`First name of the user",
    "4-0": "furl  \n`optional`",
    "4-1": "`String`Failure URL ",
    "5-0": "surl  \n`optional`",
    "5-1": " `String`Success URL",
    "6-0": "udf1  \n`optional`",
    "6-1": " `String`User defined field",
    "7-0": "udf2  \n`optional`",
    "7-1": "  `String`User defined field",
    "8-0": "udf3  \n`optional`",
    "8-1": "  `String`User defined field",
    "9-0": "udf4  \n`optional`",
    "9-1": "  `String`User defined field",
    "10-0": "udf5  \n`optional`",
    "10-1": "  `String`User defined field"
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


## Manage UPI accounts

The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

```kotlin
boltUI.openUPIManagement(enforceScreenType: EnforceScreenType, callback: PayUUPIBoltUICallBack)
```

> 📘 Callback reference:
> 
> For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Data Type",
    "h-2": "Optional /Mandatory",
    "h-3": "Definition",
    "0-0": "enforceScreenType",
    "0-1": "EnforceScreenType",
    "0-2": "O",
    "0-3": "`\"ALL\" or \"TRANSACTIONHISTORY\" or \"MANAGEUPIACCOUNTS\" or \"DISPUTE\" or \"DEREGISTERUPI\"`",
    "1-0": "callback  \n`mandatory`",
    "1-1": "PayUUPIBoltUICallBack",
    "1-2": "M",
    "1-3": "**PayUUPIBoltUICallBack** This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section."
  },
  "cols": 4,
  "rows": 2,
  "align": [
    null,
    null,
    null,
    null
  ]
}
[/block]


## Listener or Callback logic

Listerner/Callback contains 3 methods where the merchant app will get the API response and hash-related callbacks

| S.No. | Listener                                                                                           | Description                                                                               |
| ----- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1     | fun generateHash(map: HashMap\<String, String>, hashGenerationListener: PayUHashGeneratedListener) | For hash generation, refer to [Hash generation logic ](#hash-generation-logic)sub-section |
| 2     | fun onPayUSuccess(response: PayUUPIBoltResponse)                                                   | It will contain success response.                                                         |
| 3     | fun onPayUFailure(response: PayUUPIBoltResponse)                                                   | It will contain failure response.                                                         |

### PayUUPIResponse

| Fields       | Data Type | Definition               |
| ------------ | --------- | ------------------------ |
| responseType | Integer   | f. ResponseType section  |
| code         | Integer   | Error or success code    |
| message      | String    | Error or success message |
| result       | Object    | Response data            |

### ResponseType

| Response Type        | Response Code | Definition       |
| -------------------- | ------------- | ---------------- |
| REQUEST\_UPI\_BOLT   | 100           | UPI Bolt Status  |
| REQUEST\_TRANSACTION | 124           | Register And Pay |
| REQUEST\_MANAGE      | 125           | UPI Management   |

## Hash Generation logic

The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

For generating and passing dynamic hashes, the merchant will receive a call from the `generateHash()` method of `PayUUPIBoltUiListener`. The `generateHash() `method is called by the SDK each time it needs an individual hash.

```kotlin
fun generateHash(map: HashMap<String, String>, hashGenerationListener: PayUHashGeneratedListener): Merchant will get map with type of hash and hash string as value of map.
  
  They have to sign that string using salt to create hash value and pass that to hashGenerationListener.onHashGenerated().
      In the map you have to check for three keys to generate hash.
      1. hashString
      2. hashName
      3. postSalt
  At the end of that hashString append your salt and use SHA-512 algo on that final string to generate hash.
  Note: If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algo on that final string to generate hash.
  Once the hash is generated use hashGenerationListener parameter to pass the hash to SDK. Example code:
         val hashMap: HashMap<String, String> = HashMap()
         hashMap[hashName] = hash //hashName is the value you got in map and hash is the hash value.
         hashGenerationListener.onHashGenerated(hashMap)     

```