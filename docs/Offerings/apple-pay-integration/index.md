---
title: Apple Pay Integration
excerpt: Apple Pay Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Apple Pay offers a fast, secure, and seamless payment experience across iOS and watchOS apps, as well as websites on Safari. With a simple Face ID, Touch ID, or a double-click on Apple Watch, users can instantly and securely share their payment, shipping, and contact details to complete transactions.

<Image border={false} />

## Key Features

| Feature                | Description                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- |
| One-Tap Checkout       | Quick and secure purchases with biometric authentication (Face ID/Touch ID) |
| 3D Secure Compatible   | Apple handles 3DS authentication with issuing bank                          |
| Tokenized Transactions | Uses Device Account Number (DAN) and dynamic security codes                 |
| Cross-Device Support   | Works on iPhone, iPad, Mac, and Apple Watch                                 |
| No Additional Fees     | Apple does not charge merchants processing fees                             |

***

## Supported Payment Networks

* Visa
* Mastercard
* American Express
* Diners Club

## Prerequisites

Before integrating Apple Pay, ensure the following:

| Requirement             | Description                                                |
| :---------------------- | :--------------------------------------------------------- |
| PayU Merchant Account   | Active PayU merchant account with Apple Pay enabled        |
| Apple Developer Account | Required for certificate generation                        |
| HTTPS Domain            | All domains must support HTTPS with valid SSL certificates |
| TLS Version             | TLS 1.2 or higher required                                 |
| Domain Verification     | Domains must be verified with Apple                        |

***

## Apple Supported Integrations

PayU supports two integration methods for Apple Pay:

### Seamless Integration

For merchants who want full control over the checkout experience:

| Feature          | Description                                            |
| :--------------- | :----------------------------------------------------- |
| Full UI Control  | Merchant controls the entire checkout UI               |
| Custom Branding  | Complete customization of Apple Pay button and flow    |
| Direct API Calls | Merchant's server communicates directly with PayU APIs |

### PayU Hosted Integration

For merchants using PayU's hosted checkout:

| Feature           | Description                               |
| :---------------- | :---------------------------------------- |
| Pre-built UI      | PayU provides the checkout interface      |
| Quick Integration | Minimal development effort required       |
| Managed Flow      | PayU handles Apple Pay session management |

<Callout icon="📘" theme="info">
  For more information on Apple Pay, refer to [Apple Pay Integration](doc:apple-pay-integration).
</Callout>
