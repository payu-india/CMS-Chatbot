---
title: Apple Pay Integration
excerpt: Apple Pay Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
Apple Pay offers a fast, secure, and seamless payment experience across iOS and watchOS apps, as well as websites on Safari. With a simple Face ID, Touch ID, or a double-click on Apple Watch, users can instantly and securely share their payment, shipping, and contact details to complete transactions.

### Key Features for Users

| Feature              | Description                                                                 |
| :------------------- | :-------------------------------------------------------------------------- |
| One-Tap Checkout     | Quick and secure purchases with biometric authentication (Face ID/Touch ID) |
| Privacy Protection   | Card numbers are never stored on device or shared with merchants            |
| Cross-Device Support | Works seamlessly across iPhone, iPad, Mac, and Apple Watch                  |
| No Additional Fees   | Users are not charged any extra fees for using Apple Pay                    |

### Key Features for Merchants

| Feature                 | Description                                                |
| :---------------------- | :--------------------------------------------------------- |
| Higher Conversion Rates | Simplified checkout reduces cart abandonment               |
| Enhanced Security       | Tokenized transactions reduce fraud risk                   |
| 3D Secure Compatible    | Apple handles 3DS authentication with issuing bank         |
| No Processing Fees      | Apple does not charge merchants for Apple Pay transactions |

### How Does Apple Pay Work?

1. **Card Tokenization**: When a user adds a card to Apple Pay, the card number is replaced with a Device Account Number (DAN) - a unique token specific to that device.

2. **Secure Element Storage**: The DAN is stored in the Secure Element, a dedicated chip on Apple devices that isolates payment information from the operating system.

3. **Dynamic Security Code**: For each transaction, Apple Pay generates a one-time dynamic security code that validates the payment.

4. **Biometric Authentication**: Users authenticate payments using Face ID, Touch ID, or device passcode.

5. **Network Processing**: The tokenized payment is sent through the payment network, which de-tokenizes it and processes the transaction with the issuing bank.

### Supported Payment Networks

* Visa
* Mastercard
* American Express
* Diners Club
* Discover (in supported regions)

### Goals

| Goal                    | Description                                        |
| :---------------------- | :------------------------------------------------- |
| Increase Conversion     | Reduce checkout friction and cart abandonment      |
| Enhance Security        | Leverage tokenization and biometric authentication |
| Improve User Experience | Provide seamless, one-tap payment experience       |
| Expand Payment Options  | Offer modern digital wallet support for customers  |

***

## Apple Pay Flow

### High-Level Flow

<Image align="center" border={true} src="https://files.readme.io/33c344fb8ffe7e074dfc5c42fb677e87a7ec484bfa94e2e4f130b8359a26d4b7-swimlanes-1161932f5e7fee435e1ca091cd7f3732.png" className="border" />

### Technical Summary

1. User initiates payment by tapping the Apple Pay button.
   Apple Pay payment sheet appears with card and shipping info.

2. User authenticates with Face ID, Touch ID, or passcode.

3. Merchant server requests session validation from PayU.

4. PayU sends validation request to Apple servers.

5. Apple returns a valid merchant session object.

6. PayU forwards session to merchant for completion.

7. Apple generates encrypted payment token with card data.

8. Merchant sends token to PayU for payment processing.

9. PayU returns transaction status to merchant.

10. Merchant shows success/failure to customer.

### Flow for Non-Seamless / Selective Seamless Merchants

For merchants using PayU's hosted checkout:

1. Customer selects Apple Pay on PayU checkout page
2. PayU displays Apple Pay payment sheet
3. Customer authenticates and authorizes payment
4. PayU processes the payment and returns result
5. Customer is redirected to merchant's success/failure URL

### Flow for Seamless Merchants (Direct API)

For merchants with direct API integration:

1. Merchant displays Apple Pay button on their checkout page
2. Customer taps Apple Pay button
3. Merchant creates ApplePaySession and handles `onvalidatemerchant` event
4. Merchant server calls PayU API for merchant validation
5. PayU validates with Apple and returns session
6. Merchant completes merchant validation with session
7. Customer authenticates payment
8. Merchant receives payment token in `onpaymentauthorized` event
9. Merchant sends token to PayU `_payment` API with `pg=APPLEPAY`
10. PayU processes payment and returns response
11. Merchant completes payment and shows result
