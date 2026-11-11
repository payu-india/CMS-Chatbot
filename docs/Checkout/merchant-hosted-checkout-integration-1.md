---
title: Merchant Hosted Checkout Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This document provides a comprehensive architectural overview of PayU’s Merchant Hosted Checkout (Custom / Seamless Checkout) solution for collecting payments online.

***

## Environment Endpoints

| Environment           | Purpose                             | Payment Initiation URL (`_payment`) | Post-Service & Verification URL                        | Merchant Portal  |
| :-------------------- | :---------------------------------- | :---------------------------------- | :----------------------------------------------------- | :--------------- |
| **Test (Sandbox)**    | Integration testing & mock payments | `<redacted URL>`                    | `<redacted URL>`                                       | `<redacted URL>` |
| **Production (Live)** | Real customer payments              | `https://secure.payu.in/_payment`   | `https://info.payu.in/merchant/postservice.php?form=2` | `<redacted URL>` |

***

## What is Merchant Hosted Checkout?

PayU’s Merchant Hosted Checkout enables merchants to deliver a completely customized checkout experience on their website or application while leveraging PayU’s secure payment processing infrastructure.

Unlike PayU Hosted Checkout (where the customer is redirected to a standard PayU-hosted payment page), Merchant Hosted Checkout allows you to collect payment details directly on your own website and transmit them securely to PayU for authorization and settlement.

### Key Benefits

* **Customizable UI/UX:** Full control over your checkout flow, styling, and branding.
* **Reduced Friction:** Seamless payment journey with minimal redirects, resulting in higher conversion rates.
* **Wide Payment Support:** Credit/Debit Cards, Net Banking, UPI (Intent S2S & Collect), Wallets, and alternate methods.

***

## Comparison: PayU Hosted vs. Merchant Hosted Checkout

| Feature                  | PayU Hosted Checkout                             | Merchant Hosted Checkout (Seamless)                      |
| :----------------------- | :----------------------------------------------- | :------------------------------------------------------- |
| **Checkout UI Location** | Hosted on PayU (`secure.payu.in`)                | Hosted entirely on Merchant's Website / App              |
| **PCI DSS Scope**        | SAQ A (Minimal compliance burden)                | SAQ A-EP (or SAQ-D if processing raw card data)          |
| **Branding Control**     | Standard customization (logo, brand colors)      | 100% control over HTML, CSS, layouts, and UX             |
| **Card Data Collection** | Collected directly on PayU domain                | Collected on Merchant UI and submitted via form POST     |
| **Redirection Behavior** | Browser redirects to PayU $\rightarrow$ Bank ACS | Browser submits form POST to PayU $\rightarrow$ Bank ACS |

***

## PCI DSS Compliance & Data Security

When using Merchant Hosted Checkout:

* If you collect card details directly on your frontend and submit them via browser form POST to PayU, you must complete the **PCI DSS Self-Assessment Questionnaire A-EP (SAQ A-EP)**.
* **Prohibition on Raw Card Storage:** In strict accordance with Reserve Bank of India (RBI) regulations, merchants must never store customer card numbers (PAN), CVVs, or expiration dates on their internal servers, databases, or application log files.
* For repeat card checkout, utilize PayU's RBI-compliant **Card-on-File (CoF) Tokenization** solution.
