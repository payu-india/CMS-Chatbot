---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Integration
  robots: index
---
The following API and SDK are used for Virtual Cards integration:

| Use case → Reference                                      | `command` / primary value               | Description                                                                                                   |
| --------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Launch Virtual Cards — **Virtual Cards Launch API**       | `POST /loyalty-points/olw/user/card/v1` | Sends an HMAC SHA-512-authorized form request and redirects the customer to the Virtual Cards OTP page.       |
| Display the Virtual Cards interface — **PayU PPI JS SDK** | `ppi.launch()`                          | Launches the Virtual Cards management interface in an iFrame on the merchant page or after a hosted redirect. |

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
