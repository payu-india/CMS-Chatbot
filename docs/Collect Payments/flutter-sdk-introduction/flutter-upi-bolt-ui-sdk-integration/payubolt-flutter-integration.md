---
title: Flutter UPI Bolt Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Bolt SDK enables seamless in-app UPI payments in merchant applications. The SDK provides comprehensive functionality for:

* **Registration**: APIs for device binding and user registration
* **Payment**: APIs for payment initiation and transaction verification
* **Management**: APIs for account management including balance checking, MPIN management, and account operations

## Prerequisites

### Platform Requirements

* **iOS**: iOS 17 or above
* **Android**: Latest Android SDK with appropriate dependencies

### Dependencies

#### iOS Dependencies

Required frameworks:

* `CommonLibrary.xcframework` (mandatory)
* `OlivePayLibrary.xcframework` (optional, for AXIS bank integration)

#### Android Dependencies

To integrate the PayUBolt SDK with your Android project, you need to add these essential dependencies to your build configuration. These dependencies provide core UPI functionality and secure component handling for transaction processing.

Required dependencies in `build.gradle`:

```gradle
implementation 'in.payu:payu-upi-bolt-core-sdk:0.0.1-dev4'
implementation(files('libs/SecureComponent-release-prod_05062024_9d3904ab.aar'))
```

## Installation and Setup

### Flutter Package Installation

To get started with PayUBolt in your Flutter application, add the official package dependency. This command will download and configure the PayUBolt Flutter wrapper for seamless integration with your project.

Add the PayUBolt Flutter package to your project:

```bash
flutter pub add payu_upi_bolt_flutter 1.0.0.alpha
```

### iOS Setup

1. Add required `.xcframework` files to your Xcode project
2. Update Framework Search Paths in Xcode project settings
3. Include `CommonLibrary.xcframework` in the Frameworks section
4. Optionally add `OlivePayLibrary.xcframework` for AXIS bank support

### Android Setup

1. Place the `.aar` file in the `libs` folder of your Android project
2. Add dependencies to `build.gradle` file
3. Include `SecureComponent-release-prod.aar` for secure operations

## SDK Initialization

### Basic Initialization

The SDK initialization is the first step to enable UPI payments in your application. This configuration object contains all necessary merchant details and platform settings required for the SDK to communicate with PayU's payment infrastructure.

```dart
import 'package:payu_upi_bolt_flutter/payu_upi_bolt_flutter.dart';

late PayUUPIBoltFlutter payUUpiFlutter;

var config = {
  'merchantName': "<merchantName>",
  'merchantKey': "<merchantKey>", 
  'phone': "<phone>",
  'email': "<email>",
  'refId': "<refId>",
  'pluginTypes': ["<pluginType>"],
  'clientId': ["clientId"],
  'issuingBanks': ["<issuingBanks>"],
  'excludedBanksIINs': ["<excludedBanksIIN>"],
  'isProduction': <isProduction>
};

payUUpiFlutter.initSDK(params: config);
```

### Reset SDK

Use this method to reset the SDK to its initial state, clearing all cached data and session information. This is particularly useful when switching between different merchant configurations or during testing scenarios.

```dart
payUUpiFlutter.reset();
```

### Clear SDK Cache

This method clears specific cached data while maintaining the SDK's initialized state. The PG parameter specifies which payment gateway's cached information should be cleared.

```dart
payUUpiFlutter.clearCache(params: {
  'pg': '<PG_VALUE>' // Mandatory parameter
});
```

## Hash Generation

### Implementation

Hash generation is a critical security component that validates transaction authenticity between your application and PayU servers. This custom implementation creates SHA-512 hashes using your merchant salt and transaction parameters to ensure secure payment processing.

```dart
@override
String generateHash(Map response) {
  let commandName = (param[PayUUPIBoltHashConstants.hashName] ?? "");
  let hashStringWithoutSalt = (param[PayUUPIBoltHashConstants.hashString] ?? "");
  let postSalt = param[PayUUPIBoltHashConstants.postSalt];
  
  var hashValue = "";
  
  if (let postSalt = postSalt) {
    let hashString = hashStringWithoutSalt + salt + postSalt;
    hashValue = "<SHA-512 hash of hashString>";
  } else {
    let hashString = hashStringWithoutSalt + salt;
    hashValue = "<SHA-512 hash of hashString>";
  }
  
  var hashResponse = { commandName: hashValue };
  payUUpiFlutter.hashGenerated(params: hashResponse);
  
  return hashValue;
}
```

### Hash Components

* **hashString**: Base string for hash generation
* **hashName**: Command name identifier
* **postSalt**: Optional additional salt value
* **salt**: Merchant-specific salt value

## API Methods

### Registration Flow

#### Check UPI Bolt Status

Verify if UPI Bolt feature is enabled for the current device and merchant configuration. This is typically the first API call to determine payment capability availability.

```dart
final response = await payUUpiFlutter.isUpiBoltEnabled();
```

#### Get Registered Mobile

Retrieve the mobile number currently registered with the UPI Bolt service for this device. This helps identify the primary account holder for payment operations.

```dart
final response = await payUUpiFlutter.getRegisteredMobile();
```

#### Check Device Status

Validate the current device's registration status with the UPI Bolt service. This API confirms whether the device can process payments or requires re-registration.

```dart
final response = await payUUpiFlutter.checkDeviceStatus();
```

#### Fetch Bank List

Retrieve the list of supported banks available for UPI Bolt transactions. This information helps users select their preferred bank for payment processing.

```dart
final response = await payUUpiFlutter.fetchBankList();
```

#### Set VPA and MPIN

Configure the Virtual Payment Address (VPA) and Mobile PIN (MPIN) for secure UPI transactions. This registration step is required before initiating any payment operations.

```dart
final response = await payUUpiFlutter.setVPA(params: {
  'vpa': '<user_vpa>',
  'mpin': '<user_mpin>'
});
```

### Payment Flow

#### Payment Initiation

Initiate a UPI payment transaction with the specified amount and payment details. This is the primary method for processing payments through the UPI Bolt SDK.

```dart
final response = await payUUpiFlutter.pay(params: {
  'txnId': '<transaction_id>',
  'amount': '<amount>',
  'productInfo': '<product_info>',
  'firstName': '<first_name>',
  'email': '<email>',
  'phone': '<phone>',
  'surl': '<success_url>',
  'furl': '<failure_url>',
  'hash': '<generated_hash>'
});
```

#### Transaction Status Check

Check the current status of a previously initiated transaction. Use this method to verify payment completion and handle transaction state management.

```dart
final response = await payUUpiFlutter.checkTxnStatus(params: {
  'txnId': '<transaction_id>'
});
```

#### Cancel Transaction

Cancel an ongoing transaction that hasn't been completed. This method is useful for handling user-initiated cancellations or timeout scenarios.

```dart
final response = await payUUpiFlutter.cancelTxn(params: {
  'txnId': '<transaction_id>'
});
```

### Account Management

#### Fetch Linked Accounts

Retrieve all bank accounts linked to the current UPI registration. This information helps users select their preferred payment source for transactions.

```dart
final response = await payUUpiFlutter.fetchAccountsWithIIN(params: {
  'iin': '<bank_iin>'
});
```

#### Check Account Balance

Fetch the current balance for a specific linked bank account. This feature helps users verify available funds before initiating payment transactions.

```dart
final response = await payUUpiFlutter.fetchAccountBalance(params: {
  'accountNumber': '<account_number>'
});
```

#### Remove Account

Remove a linked bank account from the UPI Bolt registration. This security feature allows users to manage their linked payment methods.

```dart
final response = await payUUpiFlutter.removeAccount(params: {
  'accountNumber': '<account_number>'
});
```

#### Change MPIN

Update the Mobile PIN used for transaction authentication. This security feature allows users to regularly update their payment credentials.

```dart
final response = await payUUpiFlutter.changeMPIN(params: {
  'oldMpin': '<old_mpin>',
  'newMpin': '<new_mpin>'
});
```

#### Raise Query

Submit a customer service query or complaint regarding UPI Bolt services. This method provides a direct communication channel for issue resolution.

```dart
final response = await payUUpiFlutter.raiseQuery(params: {
  'queryType': '<query_type>',
  'description': '<query_description>'
});
```

#### Fetch Query Status

Check the status and response for a previously submitted query. Use this method to track the resolution progress of customer service requests.

```dart
final response = await payUUpiFlutter.fetchQuery(params: {
  'queryId': '<query_id>'
});
```

#### Device Deregistration

Completely deregister the current device from UPI Bolt services. This security measure should be used when the device is no longer authorized for payment operations.

```dart
final response = await payUUpiFlutter.deRegister();
```

## Retry Callback Implementation

### Handle Retry Scenarios

Implement this callback to manage payment retry scenarios when transactions fail due to temporary issues. The callback provides error details and allows you to present retry options to users for improved payment success rates.

```dart
@override
void onPayUHandleRetry(Map response) {
  // Display error UI based on errorCode and errorMessage
  print('Error Code: \${response['errorCode']}');
  print('Error Message: \${response['errorMessage']}');
  
  // Show retry dialog to user and get decision
  // Pass user decision back to SDK
  payUUpiFlutter.retryHandled(params: true); // or false based on user choice
}
```

## Response Structures

### Standard Response Format

All API responses from the PayUBolt SDK follow a consistent structure that includes result data, status codes, reference information, and descriptive messages. This standardized format simplifies response handling and error management across all SDK methods.

```json
{
  "result": { /* Response data if successful */ },
  "code": 0,
  "referenceId": "TXN123456", 
  "message": "Success"
}
```

### Account Response Structure

API responses for account-related operations include comprehensive account details, linked bank information, and current status. This structure provides all necessary information for account management features.

```json
{
  "result": {
    "accounts": [
      {
        "accountNumber": "1234567890",
        "bankName": "SBI",
        "iin": "508534",
        "isDefault": true
      }
    ]
  },
  "code": 0,
  "referenceId": "ACC123456",
  "message": "Accounts fetched successfully"
}
```

### Payment Response Structure

Payment API responses contain transaction details, payment status, and reference information required for transaction tracking and reconciliation. This comprehensive structure supports both successful and failed transaction scenarios.

```json
{
  "result": {
    "txnId": "TXN123456",
    "amount": "100.00",
    "status": "SUCCESS",
    "bankReferenceNumber": "BRN123456",
    "paymentMethod": "UPI"
  },
  "code": 0,
  "referenceId": "PAY123456",
  "message": "Payment completed successfully"
}
```

## Error Codes

The following error codes help identify and troubleshoot issues during SDK operations. Each code corresponds to specific failure scenarios and provides guidance for appropriate error handling and user communication.

| Error Code | Description                     |
| ---------- | ------------------------------- |
| 1000       | Invalid parameters              |
| 1001       | Network error                   |
| 1002       | Authentication failed           |
| 1003       | Transaction declined            |
| 1004       | Insufficient balance            |
| 1005       | Invalid MPIN                    |
| 1006       | Device not registered           |
| 1007       | Service temporarily unavailable |

## Configuration Parameters

### Mandatory Parameters

These essential parameters must be provided during SDK initialization and API calls. Each parameter serves a specific purpose in merchant identification and transaction processing.

* **merchantName**: Your registered merchant name with PayU
* **merchantKey**: Unique merchant identifier provided by PayU
* **phone**: Merchant contact phone number
* **email**: Merchant contact email address
* **refId**: Unique reference identifier for tracking
* **isProduction**: Boolean flag indicating production/test environment

### Optional Parameters

These parameters provide additional customization and filtering options for enhanced control over payment processing and user experience.

* **pluginTypes**: Array of supported payment plugin types
* **clientId**: Client-specific identifier for tracking
* **issuingBanks**: Array of preferred issuing bank codes
* **excludedBanksIINs**: Array of bank IINs to exclude from options

## Additional Methods

### Registration Status Check

Verify the current registration status to determine if the device and user account are properly configured for UPI Bolt transactions. This diagnostic method helps troubleshoot setup issues and guide users through required registration steps.

```dart
final response = await payUUpiFlutter.checkRegistrationStatus();
```

<br />