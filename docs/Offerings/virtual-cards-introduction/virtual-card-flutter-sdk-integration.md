---
title: Flutter SDK Integration
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
This part of the document describes the Virtual Card integration on Flutter SDK. You can integrate Virtual card using `payu_ppi_flutter` SDK in Flutter. This section describes the procedure to integrate Virtual Card using Flutter SDK.

## Steps to Integrate

<Cards cols={3}>
  <Card title="Add Dependency" icon="fa-cube">
    Add the `payu_ppi_flutter` SDK dependency to your app's `pubspec.yaml`.
  </Card>
  <Card title="SDK Initialisation" icon="fa-code">
    Import classes, create params object, initialise `PayUPPIFlutter`, and override `PayUPPIProtocol` methods.
  </Card>
  <Card title="Hashing" icon="fa-lock">
    Generate SHA-512 hash on your backend using the hash string provided by PayU and return it to the SDK.
  </Card>
</Cards>

<Accordion title="Step 1: Add Dependency" icon="fa-cube">

Add the following dependency in your app's `pubspec.yaml`.

```plaintext
payu_ppi_flutter:^1.0.0
```

</Accordion>

<Accordion title="Step 2: SDK Initialisation" icon="fa-code">

1. Import classes from `payu_ppi_flutter` SDK in your project.

```dart
import 'package:payu_ppi_flutter/payu_ppi_flutter.dart'; 
import 'package:payu_ppi_flutter/PayUConstantKeys.dart';
```

2. Create the `params` object.

```dart
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

```dart
PayUPPIFlutter _ppi = PayUPPIFlutter(this);
_ppi.showCards(payUPPIParams: <params created with createPayUPPIParams>)
```

4. Inherit class with `PayUPPIProtocol` in which you are creating the `PayUPPIFlutter` object and override `PayUPPIProtocol` methods.

```dart
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

</Accordion>

<Accordion title="Step 3: Hashing" icon="fa-lock">

PayU will get hash string in map `"hashString"` key and hash name `"hashName"` in `generateHash`. You need to send this string to server and append salt there. After appending salt, convert string to SHA-512 hash and return back to SDK in `hashGenerated` as `Map`.

</Accordion>

## Sample app

You can download the sample app for Virtual Card integration on Flutter SDK from the following Github location:

[https://github.com/payu-intrepos/PPIManagerFlutter](https://github.com/payu-intrepos/PPIManagerFlutter)
