---
title: Capacitor Mobile SDK
deprecated: false
hidden: true
icon: fad fa-air-conditioner
metadata:
  robots: index
---
PayU provides two primary SDK integrations for Capacitor apps depending on your payment flow and UI customization requirements:* **Checkout Pro SDK**: A complete, ready-to-use native checkout experience that supports all major payment modes (Credit/Debit Cards, Net Banking, UPI, Wallets, EMI). It requires minimal integration effort, comes with customizable branding, and handles the complete payment lifecycle, including OTP auto-fill, Recurring Payments (SI), and SKU-based offers.
* **UPI Bolt SDK**: A dedicated, in-app UPI payment solution that provides a 1-click checkout experience without redirecting users to third-party UPI apps. It includes customer onboarding, device/SIM binding, bank account selection, MPIN setup, real-time balance inquiries, and profile management directly within your app.

---

## Choose Your Integration

The ideal SDK depends on your supported payment methods, user experience requirements, and available engineering resources:

* **Choose Checkout Pro SDK** if you want an out-of-the-box, comprehensive payment suite that supports cards, net banking, wallets, and UPI with minimal setup.
* **Choose UPI Bolt SDK** if your checkout primarily focuses on UPI and you want to maximize conversions by eliminating app switching with an embedded, 1-click in-app payment and registration flow.

### SDK Comparison

| Feature / Attribute | Checkout Pro SDK | UPI Bolt SDK |
| :--- | :--- | :--- |
| **Primary Use Case** | Full-suite, multi-instrument checkout | In-app, 1-click UPI checkout |
| **Supported Payment Modes** | Cards, Net Banking, UPI, Wallets, EMI | UPI (Direct bank-to-bank) |
| **User Interface** | Pre-built, customizable native UI | In-app native UI & custom journeys |
| **Third-Party Redirection** | Redirects to bank/wallet/UPI app where applicable | **Zero redirection** (Fully in-app) |
| **Key Differentiator** | Multi-payment mode support, auto-OTP, Recurring Payments (SI), SKU offers | 5–6% boost in success rates, embedded account linking & MPIN flow |
| **Integration Effort** | Low | Low to Medium |
| **Target Audience** | E-commerce, D2C, Marketplaces, Utilities | High-frequency UPI apps, quick commerce, subscriptions |

---

## Key Benefits

* **Native Cross-Platform Performance**: Built for hybrid applications (Capacitor / Ionic / Angular), delivering native Android and iOS speed and stability.
* **Higher Conversion Rates**: Eliminates unnecessary redirects and drop-offs with seamless native screens and OTP handling.
* **Server-Side Security**: All sensitive signing and hash generation (`SHA-512`) are handled securely server-to-server, protecting merchant keys and salts from client-side exposure.
* **Event-Driven Architecture**: Rich event callbacks (`onPaymentSuccess`, `onPaymentFailure`, `onPaymentCancel`, `onError`) provide granular control over the transaction lifecycle.

---

## Technical Specifications & Compatibility

| Platform / Framework | Checkout Pro SDK | UPI Bolt SDK |
| :--- | :--- | :--- |
| **npm Package** | `payu-checkoutpro-capacitor` | `payu-upi-bolt-ui-capacitor` |
| **Import Module** | `capacitor-payu-checkoutpro` | `PayUBoltUI` |
| **Android Requirement** | Min SDK 21+, Compile SDK 31+ | Min SDK 21+, Compile SDK 31+ |
| **iOS Requirement** | iOS 11.0 or higher | iOS 12.0 or higher |
| **Supported Frameworks** | Capacitor, Ionic (Angular, React, Vue) | Ionic, Capacitor, Angular |

---

## Integration Guides

Get started with detailed, step-by-step documentation, configuration parameter references, code snippets, and callback response samples:

<Cards columns={2}>
  <Card title="Capacitor Checkout Pro Integration" href="/docs/capacitor-checkout-pro-integration" icon="fa-credit-card">
    Integrate PayU's full-suite native checkout screen supporting Cards, Net Banking, UPI, Wallets, Recurring Payments (SI), and Offers.
  </Card>
  <Card title="UPI Bolt SDK Integration" href="/docs/upi-bolt-capacitor-ionic-angular-sdk-integration" icon="fa-bolt">
    Implement 1-click in-app UPI payments, user SIM binding, bank account linking, MPIN journeys, and balance check.
  </Card>
</Cards>
