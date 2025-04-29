---
title: Virtual Card Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Virtual Card Integration - Flutter SDK
  description: ''
  robots: index
next:
  description: ''
---
You can integrate Virtual card using `payu_ppi_flutter` SDK in Flutter. This section describes the procedure to integrate Virtual Card using Flutter SDK. 

### Step 1: Add Dependency

Add the following dependency in your app’s `pubspec.yaml` .

```plaintext
payu_ppi_flutter:^1.0.0
```

### Step 2: SDK Initialisation

1. Import classes from `payu_ppi_flutter` SDK in your project.

```plaintext DART
import 'package:payu_ppi_flutter/payu_ppi_flutter.dart'; 
import 'package:payu_ppi_flutter/PayUConstantKeys.dart';`
```

2. Create the`params` object

```plaintext DART
static Map createPayUPPIParams() {
  var payUParams = {
    PayUPPIParamKey.merchantKey: "<String - Merchant Key>",
    PayUPPIParamKey.referenceId: "<String - Any unique reference id>",
    PayUPPIParamKey.walletUrn: "<String - User wallet urn linked with above mobile number>",
    PayUPPIParamKey.environment: "<Environment in which you want to run 0 - Prod, 1 - Test>",
    PayUPPIParamKey.walletIdentifier: "<String - Merchant wallet identifier>",
    PayUPPIParamKey.mobileNumber: "<String - User Mobile number>"
  };
  return payUParams;
}
```

3. Create the `PayUPPIFlutter` object and call `showCards` function.

```Text DART
 PayUPPIFlutter _ppi = PayUPPIFlutter(this);
  _ppi.showCards(payUPPIParams: <params created with createPayUPPIParams>)
```

4. Inherit class with `PayUPPIProtocol` in which  you are creating the`PayUPPIFlutter` object and override `PayUPPIProtocol` methods.

```plaintext DART
@override
  generateHash(Map response) {
    var hashName = response[PayUHashConstantsKeys.hashName];
    var hashStringWithoutSalt = response[PayUHashConstantsKeys.hashString];
    // Pass response param to your backend server
    // Backend will generate the hash and will callback to
    var hash = <generateHash on backend>;
    Map hashResponse = {hashName: hash};
    _ppi.hashGenerated(hash: hashResponse);
  }

  @override
  onCancel() {
    // This function is called when user presses the back button on Card and OTP Page
  }

  @override
  onError(Map? response) {
    // This function is called when any error occurs
  }
```

### Step 3: Hashing

PayU will get hash string in map "hashString" key and hash name "hashName" in generateHash.  You need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to sdk in `hashGenerated`  as  `Map`.
