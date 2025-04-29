---
title: PayUBolt SDK Integration
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
PayUBolt SDK will provide a way to integrate in-app UPI payment in merchant app with their own UI. They can manage the checkout options on their checkout screen. Features included in this SDK are:

- **Registration** - This SDK provides APIs for device binding and registration. Merchant App can consume these APIs and build their own registration journey.
- **Payment** - This SDK provides payment and verify transaction APIs. Merchant App can consume these APIs to build payment journey as well.
- **Management** - This SDK provides account management APIs. Merchant App can check balance, set/change pin and add/delete account in their own user journeys.

This integration involves the following steps:

1. [Add permissions to Manifest file](#step-1-add-permissions-to-manifest-file)
2. [Include Bolt SDK and AAR Files](#step-2-include-bolt-sdk-and-aar-files)
3. [Initialize the SDK](#step-3-initialize-the-sdk)

 Later, you can integrate the following flows:

- [Integrate Registration Flow](https://docs.payu.in/docs/payubolt-sdk-integration-native#integrate-registration-flow)
- [Integrate Repeat Flow](#integrate-repeat-flow)
- [Integrate Payment Flow](#integrate-payment-flow)
- [Integrate Management flow](#integrate-management-flow)

For hash generation logic and Listener/Callback integration, the [Hash generation logic ](#hash-generation-logic)and o [Listener or Callback logic](#listener-or-callback-logic) sub-sections.

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

## Step 2: Include Bolt SDK and AAR Files

To include the PayU UPI Bolt SDK in your project, add the following code snippet to your app’s `build.gradle`.

```
implementation 'in.payu:payu-upi-bolt-axis-wrapper-sdk:1.0.0' // PayU AXIS Wrapper
implementation 'in.payu:payu-upi-bolt-sdk:1.0.0' // PayU Bolt SDK
```

Add the **.aar** files provided by PayU during onboarding. in the **libs** directory of your android module and add these in module level **build.gradle**. For the list of files, refer to[ Prerequisites](#prerequisites).

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
val bolt = PayUUPIBolt.getInstance(
    activity: AppCompatActivity,
    config: PayUUPIBoltConfig,
    hashGenerationListener: PayUHashGenerationListener
)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Definition",
    "0-0": "activity  \n` mandatory`",
    "0-1": "`AppCompatActivity` Calling activity of the merchant App",
    "1-0": "config  \n` mandatory`",
    "1-1": "`PayUUPIBoltUIConfig` Config includes the below fields.",
    "2-0": "hashGenerationListener  \n` mandatory`",
    "2-1": "`PayUHashGenerationListener` Callback listener for hash generation"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


The PayUUPIBoltConfig includes the following fields:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "merchantKey  \n`mandatory`",
    "0-1": "`String`PayU Merchant Key",
    "1-0": "phone  \n`mandatory`",
    "1-1": "`String`Phone number for registration",
    "2-0": "email  \n`mandatory`",
    "2-1": "`String`Customer Email Id",
    "3-0": "pluginType  \n`mandatory`",
    "3-1": "`String Array`List of Supported Banks (“AXIS, HDFC”)",
    "4-0": "isProd  \n`optional`",
    "4-1": "`Boolean`Prod - ture, staging - false",
    "5-0": "excludedBanksIINs  \n`optional`",
    "5-1": "`String Array`List of Bank’s IIN to exclude",
    "6-0": "requestId  \n`mandatory`",
    "6-1": "`String`Unique reference ID"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    null,
    null
  ]
}
[/block]


### Response

| Response Params | Definition                               |
| --------------- | ---------------------------------------- |
| `PayUUPIBolt`   | PayUUPIBolt object for invoking SDK APIs |

> 📘 Callback:
> 
> After the SDK is initialised, use the same object to call the sdk methods.

## De-initialise PayUBolt SDK

`reset`: This method is used to deinitailise the bolt object. 

```
`PayUUPIBolt.reset()`
```

## Listener or Callback logic

Listerner/Callback contains 3 methods where the merchant app will get the API response and hash-related callbacks

| S.No. | Listener                                                                                           | Description                                                                               |
| ----- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1     | fun generateHash(map: HashMap\<String, String>, hashGenerationListener: PayUHashGeneratedListener) | For hash generation, refer to [Hash generation logic ](#hash-generation-logic)sub-section |
| 2     | fun onPayUSuccess(response: PayUUPIBoltResponse)                                                   | It will contain success response.                                                         |
| 3     | fun onPayUFailure(response: PayUUPIBoltResponse)                                                   | It will contain failure response.                                                         |

### PayUUPIResponse

| Fields       | Data Type | Definition                                                              |
| ------------ | --------- | ----------------------------------------------------------------------- |
| responseType | Integer   | Refer to[ Response type](#response-type).                               |
| code         | Integer   | Error or success code. Refer to[ Response codes](#response-codes) .     |
| message      | String    | Error or success message. Refer to[ Response codes](#response-codes)  . |
| result       | Object    | Response data                                                           |

Note: If result object is null or empty. Kindly use the response from message 

### Response type

| Response Type        | Response Code | Definition       |
| -------------------- | ------------- | ---------------- |
| REQUEST\_UPI\_BOLT   | 100           | UPI Bolt Status  |
| REQUEST\_TRANSACTION | 124           | Register And Pay |
| REQUEST\_MANAGE      | 125           | UPI Management   |

### Response codes

| Codes | Message                                |
| ----- | -------------------------------------- |
| 0     | Success                                |
| 1     | Fail/ Invalid Response/ Missing params |
| 2     | User canceled the transaction          |
| 100   | Transaction timeout                    |
| 101   | Hash missing                           |
| 102   | Something went wrong                   |
| 103   | Handshake failed                       |
| 104   | UPI bolt not supported                 |
| 105   | Device not supported for UPI Bolt      |
| 106   | Permission missing                     |
| 107   | Sim info not available                 |
| 108   | Device binding failed                  |
| 109   | Initiate pay failed                    |
| 110   | Dispute already exists                 |
| 501   | No internet connection                 |

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

## Integrate Registration Flow

The following methods are used to integrate registration flow:

- [Check if UPI Bolt is enabled](#check-if-upi-bolt-is-enabled)
- [Get registered mobile number](#get-registered-mobile-number)
- [Get subscriber info](#get-subscriber-info)
- [Check device status](#check-device-status)
- [Initiate SDK](#initiate-sdk)
- [Fetch bank list](#fetch-bank-list)
- [Fetch accounts of a selected bank](#fetch-accounts-of-a-selected-bank)
- [Set VPA](#set-vpa)
- [Set PIN](#set-pin)

### Check if UPI Bolt is enabled

Use the `isUpiBoltEnabled` method to check whether the UPI bolt is enabled for the merchant or not enabled.

```
bolt.core.isUpiBoltEnabled(callback: PayUUPIBoltCallBack)
```

The following parameters are needed as a request for this API:

| Paramater             | Definition                                                  |
| --------------------- | ----------------------------------------------------------- |
| callback`  mandatory` | `PayUUPIBoltCallback` Ref. Listener/Callback logic section. |

**Response**: Response type : REQUEST_UPI_BOLT. For more information, refer to[ Response type](#response-type).

### Get registered mobile number

Use the `getRegisteredMobile` method to get already registered mobile number. 

```
 bolt.core.getRegisteredMobile(): String
```

The following parameters are needed as a request for this API:

| Paramater | Definition               |
| --------- | ------------------------ |
| Mobile    | Registered Mobile Number |

### Get subscriber info

Use the `getSubscriberInfo` method to get SIM info from device. 

```swift ionic
bolt.core.getSubscriberInfo(mobile: String, callback: PayUUPIBoltCallBack)
```

> 📘 Callback reference:
> 
> For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.

The following parameters are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Definition",
    "0-0": "mobile  \n`mandatory`",
    "0-1": "`String` Mobile number to be used for registration.",
    "1-0": "callback  \n`mandatory`",
    "1-1": "`PayUUPIBoltUICallBack `This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


The response is `PayUSimInfo `array list that contains the following fields:

| Field         | Definition                  |
| ------------- | --------------------------- |
| mobileNumber  | `String` Mobile number      |
| slotIndex     | `String` SIM slot index     |
| subscriberId  | `String`SIM subscription id |
| carrierName   | `String`Name of carrier     |

### Check device status

Use the **checkDeviceStatus** method to check the device binding status.

```kotlin
bolt.core.checkDeviceStatus(mobile: String, subscriptionId: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "mobile  \n`mandatory`",
    "0-1": "`String `Mobile number to be used for registration",
    "1-0": "subscriptionId  \n`mandatory`",
    "1-1": "`String `SubscriptionId of Mobile Number",
    "2-0": "callback  \n`mandatory`",
    "2-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is CHECK_DEVICE_STATUS.

### Initiate SDK

Use the `initiateSDK` method to start device binding and triggering SMS.

```
bolt.core.initiateSDK(subscriptionId: String, phone: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

| Fields         | Definition                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| subscriptionId | `String `SubscriptionId of Mobile Number                                                              |
| mobile         | `String `Mobile number to be used for registration                                                    |
| callback       | `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section. |

**Response**: Response type is REQUEST_SDK_HANDSHAKE

### Fetch bank list

Use the `fetchBankList` method to fetch a list of all banks.

```
bolt.core.fetchBankList(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n`mandatory`",
    "0-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_LIST_BANKS

The response is `PayUBankData `array list that contains the following fields:

| Field    | Definition                                      |
| -------- | ----------------------------------------------- |
| name     | `String` Name of bank                           |
| iin      | `String`Issuer identification number of bank    |
| ifsc     | `String`IFSC code                               |
| logo     | `String`Bank logo url                           |
| bankCode | `String`Unique identification code for the bank |

### Fetch accounts of a selected bank

Use the `fetchAccountsWithIin` method to fetch accounts of selected bank.

```
bolt.core.fetchAccountsWithIin(iin: String, bankName: String, bankCode: String?, vpa: String?, requestType: String?, isCCTxnEnabled: Boolean, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Definition ",
    "0-0": "iin`\nmandatory`",
    "0-1": "`String`Issuer identification number of bank",
    "1-0": "bankname `\nmandatory`",
    "1-1": "`String` Name of bank",
    "2-0": "bankCode  \n`optional`",
    "2-1": "`String`Unique identification code for the bank",
    "3-0": "vpa`\noptional`",
    "3-1": "`String`UPI handle",
    "4-0": "requestType`\noptional`",
    "4-1": "`String`Only applicable for HDFC and contain any of the following:  \n  \n- **A**: Add account\n- **R** : New registration",
    "5-0": "isCCTxnEnabled`\nmandatory`",
    "5-1": "`String`The default value is false. Set it true if bank is CC.",
    "6-0": "callback `\nmandatory`",
    "6-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section."
  },
  "cols": 2,
  "rows": 7,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_FETCH_ACCOUNT_V3

The response is `PayUCustomerBankAccounts `array list that contains the following fields:

| Field        | Definition                                                                                                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| bankName     | `String` Name of bank                                                                                                               |
| bankCode     | `String`Unique identification code for the bank                                                                                     |
| bankAccounts | Refer to [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters) |

### Set VPA

Use the `setVpa `method to update the vpa of the registered account.

```
bolt.core.setVpa(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "accountDetail  \n` mandatory`",
    "0-1": "`PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_SAVE_VPA_V3

### Set PIN

Use the `setPin `method  to set PIN for new account..

```
bolt.core.setPin(accountDetail: PayUAccountDetail, cardNo: String, exp: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "accountDetail  \n` mandatory`",
    "0-1": "`PayUAccountDetail` Refer to PayU Account Detail section",
    "1-0": "cardNo  \n` mandatory`",
    "1-1": "`String `Last 6 digit of user’s card number",
    "2-0": "exp  \n` mandatory`",
    "2-1": "`String` Month and Expiry of user’s card number (format:  MM/YYYY)",
    "3-0": "callback  \n` mandatory`",
    "3-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_ACCOUNT_MOBILE_REG

## Integrate Repeat Flow

### Fetch linked accounts

Use the `fetchLinkedAccounts` method to fetch registered account with the device.

```
bolt.core.fetchLinkedAccounts(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n`mandatory`",
    "0-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_ALL_ACCOUNTS_V3

The response is `PayUCustomerBankAccounts `array list that contains the following fields:

| Field        | Definition                                                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bankName     | `String` Name of bank                                                                                                                                    |
| bankCode     | `String`Unique identification code for the bank                                                                                                          |
| bankAccounts | `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters) |

## Integrate Payment Flow

The following methods can be used to integrate payment flow:

- [Initiate payment](#initiate-payment)
- [Check transaction status](#check-transaction-status)
- [Cancel transaction](#cancel-transaction)

### Initiate payment

Use the `pay` method to  initiate payment..

```
bolt.core.pay(paymentParams: PayUUPIBoltPaymentParams, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "paymentParams  \n`mandatory`",
    "0-1": "`PayUAccountDetail` Refer to",
    "1-0": "callback  \n`mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


#### paymentParams field description

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "amount  \n`mandatory`",
    "0-1": "`String` Total transaction amount.",
    "0-2": "100.0",
    "1-0": "txnId  \n`mandatory`",
    "1-1": "`String` It should be unique for each transaction.  \nCannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - \"\\_,$,%,&, etc\"",
    "1-2": "4567890",
    "2-0": "productInfo  \n`mandatory`",
    "2-1": "`String` Information about the product.",
    "2-2": "\"ProductInfo\"",
    "3-0": "firstName  \n`mandatory`",
    "3-1": "`String` Customer’s first name.",
    "3-2": "\"Firstname\"",
    "4-0": "accountDetail  \n`mandatory`",
    "4-1": "`PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters) ",
    "4-2": "",
    "5-0": "udf1`\noptional`",
    "5-1": "`String` User defined field",
    "5-2": "",
    "6-0": "udf2`\noptional`",
    "6-1": "`String` User defined field",
    "6-2": "",
    "7-0": "udf3`\noptional`",
    "7-1": "`String` User defined field",
    "7-2": "",
    "8-0": "udf4`\noptional`",
    "8-1": "`String` User defined field",
    "8-2": "",
    "9-0": "udf5`\noptional`",
    "9-1": "`Numeric` User defined field",
    "9-2": ""
  },
  "cols": 3,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Response**: Response type is REQUEST_PAY

### Check transaction status

Use the `checkTransactionStatus` method to check the transaction status.

```
bolt.core.checkTransactionStatus(txnId: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "txnId  \n` mandatory`",
    "0-1": "`String` Transaction ID used for payment",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_CHECK_PAYMENT_STATUS

| Field   | Definition                                                  |
| ------- | ----------------------------------------------------------- |
| result  | `JSON` JSON key “status” contains transaction status value. |

### Cancel transaction

Use the `cancelTransaction` method to cancel the current transaction.

```
bolt.core.cancelTransaction(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n` mandatory`",
    "0-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_CANCEL_TRANSACTION

## Integrate Management flow

The following methods can be used to integrate management flow:

- [Fetch transaction history](#fetch-transaction-history)
- [Check balance](#check-balance)
- [Remove account](#remove-account)
- [Change mPIN](#change-mpin)
- [Fetch VPA profile](#fetch-vpa-profile)
- [Save VPA](#save-vpa)
- [Delete VPA](#delete-vpa)
- [Raise query or dispute](#raise-query-or-dispute)
- [Fetch query list](#fetch-query-list)
- [Deregister](#deregister)
- [Check required permissions](#check-required-permissions)
- [Check clear cache](#check-clear-cache)
- [Clear data](#clear-data)

### Fetch transaction history

Use the `fetchTransactionHistory` method to fetch the transaction history.

```
bolt.core.fetchTransactionHistory(fromDate: String, toDate: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "fromDate  \n` mandatory`",
    "0-1": "Transaction start date from which transaction history is required",
    "1-0": "toDate  \n` mandatory`",
    "1-1": "Transaction end date until which transaction history is required",
    "2-0": "callback  \n` mandatory`",
    "2-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_TRANSACTION_HISTORY_V3

The response is `PayUTransactionHistory `array list.

### Check balance

Use the `checkBalance` method to check registered account balance.

```
bolt.core.checkBalance(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "accountDetail  \n` mandatory`",
    "0-1": "`PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_BALANCE

| Field   | Definition               |
| ------- | ------------------------ |
| Balance | `String` Account balance |

### Remove account

Use the `removeAccount` method to remove registered account from your device.

```
bolt.core.removeAccount(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "accountDetail  \n` mandatory`",
    "0-1": "`PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_ACCOUNT_REMOVE_V3

### Change mPIN

Use the `changeMpin` method to change the mobile PIN of the registered account.

```
bolt.core.changeMpin(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "accountDetail  \n` mandatory`",
    "0-1": "`PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_CHANGE_MPIN

### Fetch VPA profile

Use the `fetchVpaProfile` method to fetch the VPA profile.

```
bolt.core.fetchVpaProfile(vpa: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "vpa  \n` mandatory`",
    "0-1": "`String` VPA or UPI handle",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_PROFilE_VPA_V3

### Save VPA

Use the `saveVpa` method to save a VPA profile.

```
bolt.core.saveVpa(vpa: String, name: String, nickName: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "vpa  \n` mandatory`",
    "0-1": "`String` VPA or UPI handle",
    "1-0": "name  \n` mandatory`",
    "1-1": "`String` Name of customer",
    "2-0": "nickName  \n` mandatory`",
    "2-1": "`String` Nickname for saving VPA",
    "3-0": "callback  \n` mandatory`",
    "3-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_SAVE_VPA_V3

### Delete VPA

Use the `deleteVpa` method to delete a VPA profile.

```
bolt.core.deleteVpa(vpa: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "vpa  \n` mandatory`",
    "0-1": "`String` VPA or UPI handle",
    "1-0": "callback  \n` mandatory`",
    "1-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_VPA_REMOVE_V3

### Raise query or dispute

Use the `raiseQuery` method to raise query/ dispute for the transaction.

```
bolt.core.raiseQuery(txnId: String, txnRefId: String, amount: Double, query: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "txnId  \n`mandatory`",
    "0-1": "`String` Transaction ID and it should be unique for each transaction.",
    "1-0": "txnRefId  \n`mandatory`",
    "1-1": "`String`Transaction Ref Id",
    "2-0": "amount  \n`mandatory`",
    "2-1": "`String` Total transaction amount.",
    "3-0": "query`\nmandatory`",
    "3-1": "`String` Query or dispute description",
    "4-0": "callback`\nmandatory`",
    "4-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_RAISE_QUERY_V3

### Fetch query list

Use the `fetchQueryList` method to fetch the query list.

```
bolt.core.fetchQueryList(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n` mandatory`",
    "0-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_LIST_QUERIES_V3

| Response Parameter                 | Definition                                   |
| ---------------------------------- | -------------------------------------------- |
| ArrayList\<PayUTransactionHistory> | `ArrayList` List of PayU transaction history |

### Deregister

Use the `deregister` method to deregister your device from UPI.

```
bolt.core.deregister(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Definition",
    "0-0": "callback  \n` mandatory`",
    "0-1": "`PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


**Response**: Response type is REQUEST_GET_CUSTOMER_DEREGISTER_V3

### Check required permissions

Use the `hasPermissions `method to check if all required permissions are granted.

### Check clear cache

Use the `clearCache `method to clear all ongoing callbacks.

### Clear data

Use the `clearData` method clears user data saved on device. It also clears the device binding.

## PayU Account Detail Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Definition ",
    "0-0": "name  \n`optional`",
    "0-1": "Account Name",
    "1-0": "accRefNumber  \n`mandatory`",
    "1-1": "Account Reference Number",
    "2-0": "ifsc  \n`optional`",
    "2-1": "IFSC Code",
    "3-0": "maskedAccnumber  \n`optional`",
    "3-1": "Masked Account Numner",
    "4-0": "type  \n`optional`",
    "4-1": "Account Type",
    "5-0": "vpa  \n`optional`",
    "5-1": "\\-",
    "6-0": "iin  \n`optional`",
    "6-1": "Account IIN",
    "7-0": "mmid  \n`optional`",
    "7-1": "\\-",
    "8-0": "aeba  \n`optional`",
    "8-1": "\\-",
    "9-0": "mbeba  \n`optional`",
    "9-1": "\\-",
    "10-0": "dLength  \n`optional`",
    "10-1": "\\-",
    "11-0": "dType  \n`optional`",
    "11-1": "\\-",
    "12-0": "balance  \n`optional`",
    "12-1": "\\-",
    "13-0": "balTime  \n`optional`",
    "13-1": "\\-",
    "14-0": "status  \n`optional`",
    "14-1": "\\-",
    "15-0": "bankCode  \n`optional`",
    "15-1": "Bank Code",
    "16-0": "formatType  \n`optional`",
    "16-1": "\\-",
    "17-0": "atmdLength  \n`optional`",
    "17-1": "\\-",
    "18-0": "bankName  \n`optional`",
    "18-1": "Bank Name",
    "19-0": "otpdType  \n`optional`",
    "19-1": "\\-",
    "20-0": "otpdLength  \n`optional`",
    "20-1": "\\-",
    "21-0": "bankId  \n`optional`",
    "21-1": "Bank ID"
  },
  "cols": 2,
  "rows": 22,
  "align": [
    null,
    null
  ]
}
[/block]