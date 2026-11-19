---
title: How Merchant Hosted Checkout Works
excerpt: >-
  Understand the _payment API architecture, the form POST flow, PCI-DSS scope,  
  and how Merchant Hosted Checkout differs from PayU's other checkout products.
deprecated: false
hidden: true
metadata:
  robots: index
---
Merchant Hosted Checkout is a direct form POST integration. Your website builds the payment UI, your backend generates the hash, and your server POSTs directly to PayU's `_payment` endpoint. PayU handles payment processing and authentication, then redirects the customer back to your callback URL.

***

## Architecture Overview

```
Customer Browser         Your Website / Backend         PayU
─────────────────────────────────────────────────────────────
1. Fills payment form  ──► Collect payment fields
                           Generate SHA-512 hash  ──────────►
                           POST to _payment endpoint ────────►
                                                    Process payment
                                                    Handle bank auth ◄── Bank 3DS
                           surl/furl callback  ◄────────────
2. Lands on your       ◄── Verify hash + call
   success/failure page     Verify Payment API
```

Your website and backend handle everything before and after PayU. PayU handles only the payment processing, bank authentication, and the redirect back to your `surl` or `furl`.

***

## PCI-DSS Scope

PCI-DSS (Payment Card Industry Data Security Standard) scope is one of the most important architectural considerations for Merchant Hosted Checkout card integrations.

<br />

### **Why are You in Scope?**&#x20;

Your website collects raw card numbers and CVV directly from the customer in your own HTML form. Because cardholder data passes through your browser and backend, your infrastructure is in PCI-DSS scope.

<br />

### **What This Means in Practice?**

- HTTPS is required on all pages of your checkout — not just the payment page
- CVV must never be stored — not in databases, logs, or caches
- Card numbers must not be stored without tokenization
- Your servers must meet PCI-DSS requirements or use a compliant hosting provider
- You must complete the [PCI-DSS SAQ A-EP](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf) assessment

<br />

### **PCI Scope for Other Payment Methods:**

<br />

Wallets, UPI, and Net Banking integrations do not involve raw card data — your PCI-DSS obligations for those methods are significantly reduced.

<Callout icon="ℹ️" theme="info">
  ### **Tips:**

  If reducing PCI-DSS scope is a priority, consider [Checkout Plus](../checkout-plus-integration) — card data is collected in PayU's Bolt-hosted fields, keeping your servers out of PCI scope.
</Callout>

***

## Merchant Hosted Checkout vs Other Checkout Products

| Feature                   | PayU Hosted Checkout             | Checkout Plus (Bolt SDK)              | Merchant Hosted Checkout            |
| ------------------------- | -------------------------------- | ------------------------------------- | ----------------------------------- |
| Payment UI                | Hosted by PayU                   | PayU modal on your site               | Built entirely by you               |
| PayU branding visible     | Yes                              | Partial (modal)                       | No                                  |
| Redirect to PayU page     | Yes                              | No                                    | No (except bank auth)               |
| PCI-DSS scope for cards   | Low — PayU collects card data    | Low — PayU's Bolt fields collect data | High — your form collects card data |
| Integration complexity    | Low                              | Medium                                | High                                |
| Per-method setup required | No                               | No                                    | Yes                                 |
| Full brand control        | No                               | Partial                               | Yes                                 |
| Mobile WebView support    | Yes                              | Yes (with workaround)                 | Yes                                 |
| Suitable for              | Low-integration-effort merchants | Brand-conscious web merchants         | Enterprise / high-customization     |

***

## BIN Validation (Cards)

For card integrations, you can optionally call the `getBinInfo` API before submitting the payment. This returns card type (credit/debit), issuing bank, card network, and EMI eligibility for the BIN (first 6 digits of the card number).

<br />

This is used to:

- Display the correct card network logo
- Show EMI options for eligible cards
- Confirm accepted card types before the customer submits

See [Build Integration — Cards](./integration-guide/build-integration/cards) for the full BIN validation flow.

***

## Callback URLs

PayU POSTs the payment response to your `surl` (success URL) or `furl` (failure URL). Both URLs must:

- Be publicly reachable over HTTPS in production
- Accept POST requests
- Return a 200 HTTP status after processing

<Callout icon="far fa-circle-info" theme="info">
  ### **Tips:**

  Implement a webhook handler as a fallback. If the customer closes the browser before the redirect completes, your `surl`/`furl` may not receive the callback. Configure PayU webhooks in the Dashboard to receive server-to-server notifications as a backup.
</Callout>

***

## Key Concepts

| Concept      | Definition                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `_payment`   | PayU's payment processing endpoint. All MHC payments POST here.                                             |
| `pg`         | Payment gateway parameter. Specifies the payment method type (`CC`, `NB`, `UPI`, `CASH`, `PAYPAL`, `MC`).   |
| `bankcode`   | Bank or provider code within a payment method type.                                                         |
| `hash`       | SHA-512 signature computed from transaction parameters. Required on all requests.                           |
| `txnid`      | Your unique transaction identifier. Must be unique per transaction.                                         |
| `surl`       | Success URL — PayU redirects here after a successful payment.                                               |
| `furl`       | Failure URL — PayU redirects here after a failed or cancelled payment.                                      |
| `mihpayid`   | PayU's unique transaction reference, returned in the callback. Use this for refunds and support queries.    |
| Reverse hash | Hash computed from the callback response to verify PayU sent it. Formula is reversed from the request hash. |
| BIN          | First 6 digits of a card number. Used to identify card type, network, and issuing bank.                     |
