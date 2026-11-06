---
title: Server-to-Server Integration
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
PayU Server-to-Server (S2S) integration enables merchants to process payments directly from their backend application to PayU's payment gateway without redirecting customers to a PayU-hosted checkout page.

***

## 1. Why Choose S2S Integration?

* **Full Brand & Checkout Ownership:** Maintain complete control over the checkout user experience, payment forms, and checkout funnel.
* **Direct Processing Architecture:** Securely transmit payment instructions directly from your application server to PayU's payment switch.
* **Zero Redirect Overhead:** Process seamless flows for Native OTP, UPI Intent deep-linking, and Direct Authorization without landing on intermediary web pages.
* **Omnichannel Capability:** Power unified payment workflows across web, mobile apps, kiosks, and POS devices.

***

## 2. Integration Modes at a Glance

| Integration Mode        | Primary Rail         | Authentication Experience                                                             | PCI-DSS Requirement       | Ideal For                                                 |
| :---------------------- | :------------------- | :------------------------------------------------------------------------------------ | :------------------------ | :-------------------------------------------------------- |
| **Cards Classic S2S**   | Credit / Debit Cards | Base64 HTML ACS template rendered in webview/iframe or Native OTP                     | SAQ A-EP or SAQ D         | Standard e-commerce web and mobile card checkouts         |
| **Cards Decoupled S2S** | Credit / Debit Cards | Two-step authorize and capture (`auth_only=1`) or external token auth (`auth_only=2`) | SAQ A-EP or SAQ D         | Hotel bookings, ride hailing, fulfillment-delayed orders  |
| **Cards Direct Auth**   | Credit / Debit Cards | Pre-authenticated via merchant's 3DS Server / MPI                                     | SAQ D (Full Level 1)      | Large enterprises running independent 3DS servers         |
| **UPI Intent**          | UPI TPAP Apps        | Deep link invocation directly to Google Pay, PhonePe, Paytm, CRED                     | None (No cardholder data) | Mobile apps and mobile web checkouts (Highest conversion) |
| **UPI Collect**         | UPI VPA              | Push notification request to customer's UPI mobile application                        | None (No cardholder data) | Desktop web and fallback flows                            |
| **UPI Omnichannel**     | UPI / Google Pay     | Push notification via phone number or VPA to mobile device                            | None (No cardholder data) | Offline POS, kiosks, desktop checkouts                    |

***

## 3. Compliance and Security Prerequisites

* **PCI-DSS Scope:** If collecting, transmitting, or processing Debit/Credit Card numbers (`ccnum`), CVV (`ccvv`), or expiry dates on your servers, your environment must be certified PCI-DSS compliant.
* **Secure Server-side Hash Computation:** All payment request hashes must be calculated securely on your backend using your PayU Merchant `key` and secret `SALT`. Never expose your `SALT` in client-side code.
* **Dual Status Verification:** Every transaction must be validated against PayU's server-to-server webhook notifications and verified via the `verify_payment` API before updating order fulfillment state.
