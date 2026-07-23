---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Integration
  robots: index
---
| API                                                                    | Purpose                                                                                                                                                                                                 |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Virtual Cards Launch API** (`POST /loyalty-points/olw/user/card/v1`) | FORM-POST request with HMAC SHA-512 authorization (`referenceId`, `redirectUrl`, `mobileNumber`, `walletUrn`, `walletIdentifier`) to redirect customers to the Virtual Cards OTP page.                  |
| **PayU PPI JS SDK** (`ppi.launch()`)                                   | Launch the Virtual Cards management UI in an iFrame on the merchant page or after a hosted redirect. Requires `https://jssdk.payu.in/ppi/ppi.min.js` (UAT: `https://jssdk-uat.payu.in/ppi/ppi.min.js`). |

<Accordion title="SDK integration" icon="fa-mobile-screen">
  Mobile integrations use platform-specific PayU PPI SDKs with server-side dynamic hash generation.

  | Platform | SDK / package | Integration guide |
  | --- | --- | --- |
  | Android | `in.payu:payu-ppi-sdk` — `OnePayUJSParams`, `showCards()` | [Android SDK Integration](doc:virtual-card-integration-in-android) |
  | iOS | `PayUIndia-PPI-SDK` — `OnePayUJSKit`, `showCards()` | [iOS SDK Integration](doc:virtual-card-integration-in-ios) |
  | Flutter | `payu_ppi_flutter` | [Flutter SDK Integration](doc:virtual-card-flutter-sdk-integration) |
  | React Native | `payu-ppi-react` | [React Native SDK Integration](doc:virtual-card-reactnative-sdk-integration) |
</Accordion>

<br />