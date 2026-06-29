---
title: Apple Pay Integration
deprecated: false
hidden: false
metadata:
  title: Apple Pay with PayU Payments Integration
  description: >-
    Integrate Apple Pay with PayU to enable secure, seamless, one‑tap payments
    on iOS devices. Learn the complete setup process, supported flows, and
    implementation steps for merchants.
  keywords:
    - apple pay integration
    - payu apple pay
    - ios payment integration
    - apple pay documentation
    - apple pay setup
    - digital wallet integration
    - one tap payments
    - payment gateway apple pay
    - apple pay india
  robots: index
---
---
title: Apple Pay Integration
deprecated: false
hidden: false
metadata:
  title: Apple Pay with PayU Payments Integration
  description: >-
    Integrate Apple Pay with PayU to enable secure, seamless, one‑tap payments
    on iOS devices. Learn the complete setup process, supported flows, and
    implementation steps for merchants.
  keywords:
    - apple pay integration
    - payu apple pay
    - ios payment integration
    - apple pay documentation
    - apple pay setup
    - digital wallet integration
    - one tap payments
    - payment gateway apple pay
    - apple pay india
  robots: index
---
Apple Pay offers a fast, secure, and seamless payment experience across iOS and watchOS apps, as well as websites on Safari. With a simple Face ID, Touch ID, or a double-click on Apple Watch, users can instantly and securely share their payment, shipping, and contact details to complete transactions.

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. Complete domain verification and Apple Pay setup, then contact your PayU Key Account Manager to activate Apple Pay on your account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard) and [Prerequisites and Set up for Apple Pay Integration](doc:prerequisites-and-set-up-for-apple-pay-integration).

## Integration guides

The following sections describe how to integrate Apple Pay with PayU:

* [Prerequisites and Set up for Apple Pay Integration](doc:prerequisites-and-set-up-for-apple-pay-integration)
* [PayU Hosted Checkout Integration](doc:apple-pay-integration-payu-hosted-checkout)
* [Merchant Hosted Checkout Integration](doc:apple-pay-integration-merchant-hosted-checkout)
* [Merchant Hosted with Session Management Integration](doc:apple-pay-session-mgmt-integration)
* [Apple Pay UI Seamless Integration](doc:apple-pay-ui-seamless-integration)

<Accordion title="APIs mentioned without a linked reference page" icon="fa-info-circle">
  | Mention | Context | Purpose |
  | --- | --- | --- |
  | **Apple Pay Session Validation API** (`/seamless/Session`) | [Merchant Hosted with Session Management Integration](doc:apple-pay-session-mgmt-integration), [Apple Pay UI Seamless Integration](doc:apple-pay-ui-seamless-integration) | Validate the merchant session with Apple during `onvalidatemerchant`; PayU forwards the request to Apple and returns the merchant session object. Documented inline on integration pages; no `ref:` link is provided. |
</Accordion>

<Accordion title="Verification and post-payment APIs" icon="fa-check-circle">
  | Name | Purpose |
  | --- | --- |
  | [Webhooks](doc:webhooks) | Alternative server-to-server verification when callbacks fail. Available via `<Verify_Payment_Tabs />` on integration pages. |
</Accordion>

## Key Features

<Accordion title="For users" icon="fa-user">
  | Feature | Description |
  | :------------------- | :-------------------------------------------------------------------------- |
  | One-Tap Checkout | Quick and secure purchases with biometric authentication (Face ID/Touch ID) |
  | Privacy Protection | Card numbers are never stored on device or shared with merchants |
  | Cross-Device Support | Works seamlessly across iPhone, iPad, Mac, and Apple Watch |
  | No Additional Fees | Users are not charged any extra fees for using Apple Pay |
</Accordion>

<Accordion title="For merchants" icon="fa-store">
  | Feature | Description |
  | :---------------------- | :--------------------------------------------------------- |
  | Higher Conversion Rates | Simplified checkout reduces cart abandonment |
  | Enhanced Security | Tokenized transactions reduce fraud risk |
  | 3D Secure Compatible | Apple handles 3DS authentication with issuing bank |
  | No Processing Fees | Apple does not charge merchants for Apple Pay transactions |
</Accordion>

<Accordion title="How Apple Pay works" icon="fa-lock">
  1. **Card Tokenization**: When a user adds a card to Apple Pay, the card number is replaced with a Device Account Number (DAN) - a unique token specific to that device.
  2. **Secure Element Storage**: The DAN is stored in the Secure Element, a dedicated chip on Apple devices that isolates payment information from the operating system.
  3. **Dynamic Security Code**: For each transaction, Apple Pay generates a one-time dynamic security code that validates the payment.
  4. **Biometric Authentication**: Users authenticate payments using Face ID, Touch ID, or device passcode.
  5. **Network Processing**: The tokenized payment is sent through the payment network, which de-tokenizes it and processes the transaction with the issuing bank.
</Accordion>

<Accordion title="Supported payment networks" icon="fa-credit-card">
  * Visa
  * Mastercard
  * American Express
  * Diners Club
  * Discover (in supported regions)
</Accordion>

<Accordion title="Goals" icon="fa-bullseye">
  | Goal | Description |
  | :---------------------- | :------------------------------------------------- |
  | Increase Conversion | Reduce checkout friction and cart abandonment |
  | Enhance Security | Leverage tokenization and biometric authentication |
  | Improve User Experience | Provide seamless, one-tap payment experience |
  | Expand Payment Options | Offer modern digital wallet support for customers |
</Accordion>

## Apple Pay flow

<Accordion title="High-level flow" icon="fa-diagram-project">
  <Image align="center" border={true} src="https://files.readme.io/33c344fb8ffe7e074dfc5c42fb677e87a7ec484bfa94e2e4f130b8359a26d4b7-swimlanes-1161932f5e7fee435e1ca091cd7f3732.png" className="border" />

  **Technical summary**

  1. User initiates payment by tapping the Apple Pay button. Apple Pay payment sheet appears with card and shipping info.
  2. User authenticates with Face ID, Touch ID, or passcode.
  3. Merchant server requests session validation from PayU.
  4. PayU sends validation request to Apple servers.
  5. Apple returns a valid merchant session object.
  6. PayU forwards session to merchant for completion.
  7. Apple generates encrypted payment token with card data.
  8. Merchant sends token to PayU for payment processing.
  9. PayU returns transaction status to merchant.
  10. Merchant shows success/failure to customer.
</Accordion>

<Accordion title="PayU Hosted Checkout flow" icon="fa-window-maximize">
  For merchants using PayU's hosted checkout:

  1. Customer selects Apple Pay on PayU checkout page
  2. PayU displays Apple Pay payment sheet
  3. Customer authenticates and authorizes payment
  4. PayU processes the payment and returns result
  5. Customer is redirected to merchant's success/failure URL

  For step-by-step integration, refer to [PayU Hosted Checkout Integration](doc:apple-pay-integration-payu-hosted-checkout).
</Accordion>

<Accordion title="Seamless (direct API) flow" icon="fa-code">
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

  For step-by-step integration, refer to [Merchant Hosted Checkout Integration](doc:apple-pay-integration-merchant-hosted-checkout), [Merchant Hosted with Session Management Integration](doc:apple-pay-session-mgmt-integration), or [Apple Pay UI Seamless Integration](doc:apple-pay-ui-seamless-integration).
</Accordion>
## APIs used in Apple Pay integration

| API | Purpose |
| --- | --- |
| [Collect Payment API – Apple Pay (Merchant Hosted)](ref:_payment-apple-pay-merchant-hosted) | Process an Apple Pay payment token with `pg=APPLEPAY` and `bankcode=APPLEPAY` on merchant-hosted checkout. |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | Redirect customers to PayU Hosted Checkout with Apple Pay as the payment method.  |
| [Verify Payment API](ref:verify_payment_api) | Server-side reconciliation of transaction status after payment. |

