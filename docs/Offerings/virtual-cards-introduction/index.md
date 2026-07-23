---
title: Virtual Cards
deprecated: false
hidden: false
icon: far fa-credit-card
metadata:
  robots: index
---
Virtual Cards are digital-only payment instruments (typically Visa, Mastercard, or RuPay) that function like physical debit or credit cards but exist only within a mobile app or web interface. They are primarily used to enable secure online transactions for digital wallets or Prepaid Payment Instruments (PPI).

PayU provides GPR (General Purpose Reloadable) cards as a solution for PayU partners. This offering includes Min-KYC, Full-KYC, Card Management, and Limit Management. To achieve PCI DSS compliance, merchants can use the PayU Card Management SDK on web and mobile platforms.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable Virtual Cards (GPR cards) and obtain your `walletIdentifier`. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Integration guides

The following sections describe how to integrate Virtual Cards with PayU:

- [Web Integration](doc:web-integration-virtual-cards)
  - [PayU Hosted Checkout Integration](doc:payu-hosted-virtual-cards-api-integration)
  - [iFrame Integration](doc:iframe-virtual-cards-api-integration)
- [Android SDK Integration](doc:virtual-card-integration-in-android)
- [iOS SDK Integration](doc:virtual-card-integration-in-ios)
- [Flutter SDK Integration](doc:virtual-card-flutter-sdk-integration)
- [React Native SDK Integration](doc:virtual-card-reactnative-sdk-integration)

## Key features

<Accordion title="GPR card capabilities" icon="fa-credit-card">
  PayU GPR cards for partners include:

  * **Min-KYC** — Lightweight customer verification to issue a virtual card.
  * **Full-KYC** — Complete KYC for higher limits and compliance.
  * **Card Management** — View, block, or manage virtual card details within the PayU-hosted or SDK UI.
  * **Limit Management** — Configure and enforce spending limits on issued cards.
</Accordion>

<Accordion title="Benefits for merchants" icon="fa-store">
  * **PCI DSS compliance** — Card data is handled by PayU PPI SDKs and hosted pages, reducing merchant PCI scope.
  * **Multi-platform support** — Integrate on web (PayU Hosted or iFrame) and native mobile SDKs.
  * **Wallet and PPI enablement** — Offer card-like payment experiences for closed-loop wallets and prepaid instruments.
  * **Branded experience** — Embed card management within your app or website using iFrame or native SDK UI.
</Accordion>

<Accordion title="Benefits for customers" icon="fa-user">
  * **Digital-first cards** — Use Visa, Mastercard, or RuPay virtual cards without a physical card.
  * **Secure online payments** — Complete OTP verification on PayU-hosted pages or within the merchant app via SDK.
  * **In-app card management** — View and manage card details without leaving the merchant experience.
</Accordion>

<Accordion title="Customer journey" icon="fa-route">
  **Web – PayU Hosted**

  1. Merchant constructs the request JSON and HMAC authorization header on the server.
  2. Merchant FORM-POSTs to the Virtual Cards Launch API.
  3. Customer is redirected to the PayU Virtual Cards OTP page.
  4. Customer completes OTP verification and card management.
  5. Customer is returned to the merchant `redirectUrl`.

  **Web – iFrame**

  1. Merchant loads the PayU PPI JS SDK and constructs request objects on the server.
  2. Customer clicks the card button; merchant calls `ppi.launch()` with request data and handlers.
  3. PayU renders the card UI in an iFrame on the merchant page.
  4. Customer completes the flow; `onCancel()` or `catchException()` handlers capture the outcome.

  **Mobile SDK**

  1. Merchant initialises the platform PPI SDK with `merchantKey`, `mobileNumber`, `walletIdentifier`, `walletUrn`, and `referenceId`.
  2. Merchant calls `showCards()` to present the native Virtual Cards UI.
  3. SDK requests a dynamic hash from the merchant server via `generateHash`.
  4. Merchant server returns SHA-512 hash; customer completes card management in the native UI.
</Accordion>

<Accordion title="Integration best practices" icon="fa-lightbulb">
  * Generate all hashes on your server — never expose merchant salt in client-side code.
  * Ensure the `Date` header and JSON request string used in the hash match exactly in the POST request (web integrations).
  * Use UAT SDK and API endpoints during testing before switching to production URLs.
  * Handle `onCancel()` and `catchException()` / `onError()` callbacks to manage user abandonment and errors gracefully.
  * Obtain `walletIdentifier` and customer `walletUrn` from your PayU Key Account Manager during onboarding.
</Accordion>

<br />
