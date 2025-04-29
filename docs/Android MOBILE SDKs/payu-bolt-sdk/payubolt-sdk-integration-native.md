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

* **Registration** - This SDK provides APIs for device binding and registration. Merchant App can consume these APIs and build their own registration journey.
* **Payment** - This SDK provides payment and verify transaction APIs. Merchant App can consume these APIs to build payment journey as well.
* **Management** - This SDK provides account management APIs. Merchant App can check balance, set/change pin and add/delete account in their own user journeys.

This integration involves the following steps:

1. [Add permissions to Manifest file](#step-1-add-permissions-to-manifest-file)
2. [Include Bolt SDK and AAR Files](#step-2-include-bolt-sdk-and-aar-files)
3. [Initialize the SDK](#step-3-initialize-the-sdk)

 Later, you can integrate the following flows:

* [Integrate Registration Flow](https://docs.payu.in/docs/payubolt-sdk-integration-native#integrate-registration-flow)
* [Integrate Repeat Flow](#integrate-repeat-flow)
* [Integrate Payment Flow](#integrate-payment-flow)
* [Integrate Management flow](#integrate-management-flow)

For hash generation logic and Listener/Callback integration, the [Hash generation logic ](#hash-generation-logic)and o [Listener or Callback logic](#listener-or-callback-logic) sub-sections.

## Prerequisites

* Minimum Android SDK Version - 23 and above.
* Compile SDK Version - 31 and above.
* The following .aar (Android archive) files provided by PayU during onboarding:
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

<Image align="center" width="360px" src="https://files.readme.io/1af3684beef4a3b10716b5fc7de478bc9a07ff6f82ae0cec8041bbb94d8c754c-bolt_native_flow_aar_directory_structure.png" />

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

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        activity
        ` mandatory`
      </td>

      <td>
        `AppCompatActivity` Calling activity of the merchant App
      </td>
    </tr>

    <tr>
      <td>
        config\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltUIConfig` Config includes the below fields.
      </td>
    </tr>

    <tr>
      <td>
        hashGenerationListener\
        ` mandatory`
      </td>

      <td>
        `PayUHashGenerationListener` Callback listener for hash generation
      </td>
    </tr>
  </tbody>
</Table>

The PayUUPIBoltConfig includes the following fields:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchantKey
        `mandatory`
      </td>

      <td>
        `String`PayU Merchant Key
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `mandatory`
      </td>

      <td>
        `String`Phone number for registration
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        `String`Customer Email Id
      </td>
    </tr>

    <tr>
      <td>
        pluginType\
        `mandatory`
      </td>

      <td>
        `String Array`List of Supported Banks (“AXIS, HDFC”)
      </td>
    </tr>

    <tr>
      <td>
        isProd\
        `optional`
      </td>

      <td>
        `Boolean`Prod - ture, staging - false
      </td>
    </tr>

    <tr>
      <td>
        excludedBanksIINs\
        `optional`
      </td>

      <td>
        `String Array`List of Bank’s IIN to exclude
      </td>
    </tr>

    <tr>
      <td>
        requestId\
        `mandatory`
      </td>

      <td>
        `String`Unique reference ID
      </td>
    </tr>
  </tbody>
</Table>

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

* [Check if UPI Bolt is enabled](#check-if-upi-bolt-is-enabled)
* [Get registered mobile number](#get-registered-mobile-number)
* [Get subscriber info](#get-subscriber-info)
* [Check device status](#check-device-status)
* [Initiate SDK](#initiate-sdk)
* [Fetch bank list](#fetch-bank-list)
* [Fetch accounts of a selected bank](#fetch-accounts-of-a-selected-bank)
* [Set VPA](#set-vpa)
* [Set PIN](#set-pin)

### Check if UPI Bolt is enabled

Use the `isUpiBoltEnabled` method to check whether the UPI bolt is enabled for the merchant or not enabled.

```
bolt.core.isUpiBoltEnabled(callback: PayUUPIBoltCallBack)
```

The following parameters are needed as a request for this API:

| Paramater             | Definition                                                  |
| --------------------- | ----------------------------------------------------------- |
| callback`  mandatory` | `PayUUPIBoltCallback` Ref. Listener/Callback logic section. |

**Response**: Response type : REQUEST\_UPI\_BOLT. For more information, refer to[ Response type](#response-type).

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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mobile
        `mandatory`
      </td>

      <td>
        `String` Mobile number to be used for registration.
      </td>
    </tr>

    <tr>
      <td>
        callback\
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltUICallBack `This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

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

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        mobile
        `mandatory`
      </td>

      <td>
        `String `Mobile number to be used for registration
      </td>
    </tr>

    <tr>
      <td>
        subscriptionId\
        `mandatory`
      </td>

      <td>
        `String `SubscriptionId of Mobile Number
      </td>
    </tr>

    <tr>
      <td>
        callback\
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is CHECK\_DEVICE\_STATUS.

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

**Response**: Response type is REQUEST\_SDK\_HANDSHAKE

### Fetch bank list

Use the `fetchBankList` method to fetch a list of all banks.

```
bolt.core.fetchBankList(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_LIST\_BANKS

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

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Definition 
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        iin```

        mandatory
        ```
      </td>

      <td>
        `String`Issuer identification number of bank
      </td>
    </tr>

    <tr>
      <td>
        bankname ```

        mandatory
        ```
      </td>

      <td>
        `String` Name of bank
      </td>
    </tr>

    <tr>
      <td>
        bankCode\
        `optional`
      </td>

      <td>
        `String`Unique identification code for the bank
      </td>
    </tr>

    <tr>
      <td>
        vpa```

        optional
        ```
      </td>

      <td>
        `String`UPI handle
      </td>
    </tr>

    <tr>
      <td>
        requestType```

        optional
        ```
      </td>

      <td>
        `String`Only applicable for HDFC and contain any of the following:  

        * **A**: Add account
        * **R** : New registration
      </td>
    </tr>

    <tr>
      <td>
        isCCTxnEnabled```

        mandatory
        ```
      </td>

      <td>
        `String`The default value is false. Set it true if bank is CC.
      </td>
    </tr>

    <tr>
      <td>
        callback ```

        mandatory
        ```
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_FETCH\_ACCOUNT\_V3

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

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountDetail
        ` mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_SAVE\_VPA\_V3

### Set PIN

Use the `setPin `method  to set PIN for new account..

```
bolt.core.setPin(accountDetail: PayUAccountDetail, cardNo: String, exp: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountDetail
        ` mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to PayU Account Detail section
      </td>
    </tr>

    <tr>
      <td>
        cardNo\
        ` mandatory`
      </td>

      <td>
        `String `Last 6 digit of user’s card number
      </td>
    </tr>

    <tr>
      <td>
        exp\
        ` mandatory`
      </td>

      <td>
        `String` Month and Expiry of user’s card number (format:  MM/YYYY)
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_ACCOUNT\_MOBILE\_REG

## Integrate Repeat Flow

### Fetch linked accounts

Use the `fetchLinkedAccounts` method to fetch registered account with the device.

```
bolt.core.fetchLinkedAccounts(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_ALL\_ACCOUNTS\_V3

The response is `PayUCustomerBankAccounts `array list that contains the following fields:

| Field        | Definition                                                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bankName     | `String` Name of bank                                                                                                                                    |
| bankCode     | `String`Unique identification code for the bank                                                                                                          |
| bankAccounts | `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters) |

## Integrate Payment Flow

The following methods can be used to integrate payment flow:

* [Initiate payment](#initiate-payment)
* [Check transaction status](#check-transaction-status)
* [Cancel transaction](#cancel-transaction)

### Initiate payment

Use the `pay` method to  initiate payment..

```
bolt.core.pay(paymentParams: PayUUPIBoltPaymentParams, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        paymentParams
        `mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to
      </td>
    </tr>

    <tr>
      <td>
        callback\
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

#### paymentParams field description

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
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `String` Total transaction amount.
      </td>

      <td>
        100.0
      </td>
    </tr>

    <tr>
      <td>
        txnId\
        `mandatory`
      </td>

      <td>
        `String` It should be unique for each transaction.\
        Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "\_,$,%,&, etc"
      </td>

      <td>
        4567890
      </td>
    </tr>

    <tr>
      <td>
        productInfo\
        `mandatory`
      </td>

      <td>
        `String` Information about the product.
      </td>

      <td>
        "ProductInfo"
      </td>
    </tr>

    <tr>
      <td>
        firstName\
        `mandatory`
      </td>

      <td>
        `String` Customer’s first name.
      </td>

      <td>
        "Firstname"
      </td>
    </tr>

    <tr>
      <td>
        accountDetail\
        `mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters) 
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1```

        optional
        ```
      </td>

      <td>
        `String` User defined field
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf2```

        optional
        ```
      </td>

      <td>
        `String` User defined field
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf3```

        optional
        ```
      </td>

      <td>
        `String` User defined field
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4```

        optional
        ```
      </td>

      <td>
        `String` User defined field
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf5```

        optional
        ```
      </td>

      <td>
        `Numeric` User defined field
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_PAY

### Check transaction status

Use the `checkTransactionStatus` method to check the transaction status.

```
bolt.core.checkTransactionStatus(txnId: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        txnId
        ` mandatory`
      </td>

      <td>
        `String` Transaction ID used for payment
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_CHECK\_PAYMENT\_STATUS

| Field   | Definition                                                  |
| ------- | ----------------------------------------------------------- |
| result  | `JSON` JSON key “status” contains transaction status value. |

### Cancel transaction

Use the `cancelTransaction` method to cancel the current transaction.

```
bolt.core.cancelTransaction(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_CANCEL\_TRANSACTION

## Integrate Management flow

The following methods can be used to integrate management flow:

* [Fetch transaction history](#fetch-transaction-history)
* [Check balance](#check-balance)
* [Remove account](#remove-account)
* [Change mPIN](#change-mpin)
* [Fetch VPA profile](#fetch-vpa-profile)
* [Save VPA](#save-vpa)
* [Delete VPA](#delete-vpa)
* [Raise query or dispute](#raise-query-or-dispute)
* [Fetch query list](#fetch-query-list)
* [Deregister](#deregister)
* [Check required permissions](#check-required-permissions)
* [Check clear cache](#check-clear-cache)
* [Clear data](#clear-data)

### Fetch transaction history

Use the `fetchTransactionHistory` method to fetch the transaction history.

```
bolt.core.fetchTransactionHistory(fromDate: String, toDate: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        fromDate
        ` mandatory`
      </td>

      <td>
        Transaction start date from which transaction history is required
      </td>
    </tr>

    <tr>
      <td>
        toDate\
        ` mandatory`
      </td>

      <td>
        Transaction end date until which transaction history is required
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_TRANSACTION\_HISTORY\_V3

The response is `PayUTransactionHistory `array list.

### Check balance

Use the `checkBalance` method to check registered account balance.

```
bolt.core.checkBalance(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountDetail
        ` mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_BALANCE

| Field   | Definition               |
| ------- | ------------------------ |
| Balance | `String` Account balance |

### Remove account

Use the `removeAccount` method to remove registered account from your device.

```
bolt.core.removeAccount(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountDetail
        ` mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_ACCOUNT\_REMOVE\_V3

### Change mPIN

Use the `changeMpin` method to change the mobile PIN of the registered account.

```
bolt.core.changeMpin(accountDetail: PayUAccountDetail, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountDetail
        ` mandatory`
      </td>

      <td>
        `PayUAccountDetail` Refer to  [PayU Account Detail Parameters](https://docs.payu.in/docs/payubolt-sdk-integration-native#payu-account-detail-parameters)
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_CHANGE\_MPIN

### Fetch VPA profile

Use the `fetchVpaProfile` method to fetch the VPA profile.

```
bolt.core.fetchVpaProfile(vpa: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        vpa
        ` mandatory`
      </td>

      <td>
        `String` VPA or UPI handle
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_PROFilE\_VPA\_V3

### Save VPA

Use the `saveVpa` method to save a VPA profile.

```
bolt.core.saveVpa(vpa: String, name: String, nickName: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        vpa
        ` mandatory`
      </td>

      <td>
        `String` VPA or UPI handle
      </td>
    </tr>

    <tr>
      <td>
        name\
        ` mandatory`
      </td>

      <td>
        `String` Name of customer
      </td>
    </tr>

    <tr>
      <td>
        nickName\
        ` mandatory`
      </td>

      <td>
        `String` Nickname for saving VPA
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_SAVE\_VPA\_V3

### Delete VPA

Use the `deleteVpa` method to delete a VPA profile.

```
bolt.core.deleteVpa(vpa: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        vpa
        ` mandatory`
      </td>

      <td>
        `String` VPA or UPI handle
      </td>
    </tr>

    <tr>
      <td>
        callback\
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_VPA\_REMOVE\_V3

### Raise query or dispute

Use the `raiseQuery` method to raise query/ dispute for the transaction.

```
bolt.core.raiseQuery(txnId: String, txnRefId: String, amount: Double, query: String, callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        txnId
        `mandatory`
      </td>

      <td>
        `String` Transaction ID and it should be unique for each transaction.
      </td>
    </tr>

    <tr>
      <td>
        txnRefId\
        `mandatory`
      </td>

      <td>
        `String`Transaction Ref Id
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
    </tr>

    <tr>
      <td>
        query```

        mandatory
        ```
      </td>

      <td>
        `String` Query or dispute description
      </td>
    </tr>

    <tr>
      <td>
        callback```

        mandatory
        ```
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_RAISE\_QUERY\_V3

### Fetch query list

Use the `fetchQueryList` method to fetch the query list.

```
bolt.core.fetchQueryList(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_LIST\_QUERIES\_V3

| Response Parameter                 | Definition                                   |
| ---------------------------------- | -------------------------------------------- |
| ArrayList\<PayUTransactionHistory> | `ArrayList` List of PayU transaction history |

### Deregister

Use the `deregister` method to deregister your device from UPI.

```
bolt.core.deregister(callback: PayUUPIBoltCallBack)
```

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        ` mandatory`
      </td>

      <td>
        `PayUUPIBoltCallBack`Refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

**Response**: Response type is REQUEST\_GET\_CUSTOMER\_DEREGISTER\_V3

### Check required permissions

Use the `hasPermissions `method to check if all required permissions are granted.

### Check clear cache

Use the `clearCache `method to clear all ongoing callbacks.

### Clear data

Use the `clearData` method clears user data saved on device. It also clears the device binding.

## PayU Account Detail Parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Definition 
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        name
        `optional`
      </td>

      <td>
        Account Name
      </td>
    </tr>

    <tr>
      <td>
        accRefNumber\
        `mandatory`
      </td>

      <td>
        Account Reference Number
      </td>
    </tr>

    <tr>
      <td>
        ifsc\
        `optional`
      </td>

      <td>
        IFSC Code
      </td>
    </tr>

    <tr>
      <td>
        maskedAccnumber\
        `optional`
      </td>

      <td>
        Masked Account Numner
      </td>
    </tr>

    <tr>
      <td>
        type\
        `optional`
      </td>

      <td>
        Account Type
      </td>
    </tr>

    <tr>
      <td>
        vpa\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        iin\
        `optional`
      </td>

      <td>
        Account IIN
      </td>
    </tr>

    <tr>
      <td>
        mmid\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        aeba\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        mbeba\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        dLength\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        dType\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        balance\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        balTime\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        status\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        bankCode\
        `optional`
      </td>

      <td>
        Bank Code
      </td>
    </tr>

    <tr>
      <td>
        formatType\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        atmdLength\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        bankName\
        `optional`
      </td>

      <td>
        Bank Name
      </td>
    </tr>

    <tr>
      <td>
        otpdType\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        otpdLength\
        `optional`
      </td>

      <td>
        \-
      </td>
    </tr>

    <tr>
      <td>
        bankId\
        `optional`
      </td>

      <td>
        Bank ID
      </td>
    </tr>
  </tbody>
</Table>
