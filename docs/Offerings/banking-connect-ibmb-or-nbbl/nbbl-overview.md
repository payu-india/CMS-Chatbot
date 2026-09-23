---
title: NBBL Overview with Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
\=NBBL Banking Connect is PayU's implementation of NPCI Bharat BillPay Limited's standardized NetBanking framework. It keeps the trust and high-value capability of NetBanking while replacing the checkout experience built around bank-website credentials with a mobile-first, password-free flow.

## What changes for the customer

The customer selects a bank at checkout and authenticates inside that bank's app. Depending on the device and available bank flow, the customer either opens the app through an intent deep link or scans a QR code displayed on the checkout page.

The customer uses the bank app's authentication method, such as biometrics or an app MPIN. The customer does not enter NetBanking credentials on a merchant or PayU page.

If the selected bank app is not installed, or the app-first path is not enabled, the journey can fall back to the bank website NetBanking flow.

## Payment flows

### Mobile app-intent flow

1. The customer selects a bank under NetBanking.
2. PayU offers the option to pay through the selected bank app.
3. PayU opens the installed bank app through a deep link.
4. The customer authenticates in the bank app with biometrics or an app MPIN.
5. The customer confirms the debit account.
6. The customer returns to the merchant with the payment result.

### Desktop QR flow

1. The customer selects a bank under NetBanking.
2. PayU offers the available payment modes, such as QR or the bank website.
3. PayU displays a NetBanking QR code.
4. The customer scans the QR code with the bank's mobile app.
5. The customer authenticates in the bank app.
6. The customer confirms the debit account.
7. PayU displays the payment result to the customer and merchant.

### Website fallback

When the bank app is not installed or the app-first route is unavailable, the customer can continue with the familiar bank-website NetBanking journey.

## Technical flow diagrams

> **Source note:** The following Net Banking 1.0+ and Net Banking 2.0 flow diagrams are retained from the previous Devguide page. Confirm the API names and technical sequence against the current Product and Tech source before publication.

NBBL offers two payment flows to accommodate different use cases:

### Net Banking 1.0+ (Redirect Flow)

Enhanced version of traditional net banking that maintains the familiar bank website experience while adding interoperability:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Customer   │────▶│   Merchant  │────▶│     PayU     │────▶│    IBMB     │
│             │     │   / PA      │     │   Gateway    │     │  Platform   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       │  1. Select Bank   │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │  2. Txn Details   │                   │
       │                   │──────────────────▶│                   │
       │                   │                   │                   │
       │                   │                   │  3. reqTxnInit    │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │                   │                   │  4. Encrypted URL  │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │                   │  5. Redirect URL  │                   │
       │                   │◀──────────────────│                   │
       │                   │                   │                   │
       │  6. Redirect to    │                   │                   │
       │     Bank Website  │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │                   │  7. Bank decrypts │
       │                   │                   │     URL via API   │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │  8. Complete      │                   │                   │
       │     Transaction   │                   │                   │
       │     on Bank Site  │                   │                   │
       │                   │                   │                   │
```

**Key Steps:**

1. Customer selects bank and initiates payment
2. Merchant/PA sends transaction details to PayU
3. PayU sends transaction to IBMB platform via `reqTxnInit` API
4. IBMB generates bank-specific encrypted redirection URL
5. Customer is redirected to bank website
6. Bank decrypts URL via API call to IBMB
7. Customer completes transaction on bank website using existing login
8. Transaction status communicated back through the system

### Net Banking 2.0 (QR & Intent Flow)

Modern mobile-first approach using QR codes and app intents:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Customer   │     │   Merchant  │     │     PayU     │     │    IBMB     │
│  (Desktop)  │     │   / PA      │     │   Gateway    │     │  Platform   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       │  1. Select QR     │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │  2. Txn Details   │                   │
       │                   │──────────────────▶│                   │
       │                   │                   │                   │
       │                   │                   │  3. reqTxnInit    │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │                   │                   │  4. Encrypted URL │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │                   │  5. QR Code       │                   │
       │                   │◀──────────────────│                   │
       │                   │                   │                   │
       │  6. QR Displayed  │                   │                   │
       │◀──────────────────│                   │                   │
       │                   │                   │                   │
       │                   │                   │                   │
┌─────────────┐            │                   │                   │
│  Customer   │            │                   │                   │
│  (Mobile)   │            │                   │                   │
│  Bank App   │            │                   │                   │
└─────────────┘            │                   │                   │
       │                   │                   │                   │
       │  7. Scan QR       │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │                   │  8. reqFetchTxn   │
       │                   │                   │     Details       │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │  9. Select Account│                   │                   │
       │     & Authorize   │                   │                   │
       │                   │                   │                   │
       │  10. Payment      │                   │                   │
       │      Success      │                   │                   │
       │                   │                   │                   │
```

**Key Steps:**

1. Customer selects QR code payment option
2. Merchant/PA sends transaction to PayU
3. PayU sends transaction to IBMB via `reqTxnInit` API
4. IBMB generates encrypted URL (format: `nb://nbpay?param=value`)
5. PayU converts URL to QR code and displays on merchant page
6. Customer scans QR code using bank mobile app
7. Bank app sends `reqFetchTxnDetails` to IBMB to decrypt URL
8. Customer selects account and authorizes payment in bank app
9. Transaction completes within bank app
10. Merchant page shows payment confirmation

## Merchant impact

- Existing NetBanking integrations do not require changes.
- PayU can roll out the capability bank by bank or through traffic splits.
- Reconciliation and settlement processes remain unchanged according to the product brief.
- A standardized framework is intended to improve transaction visibility and dispute handling.

## Product positioning

NBBL Banking Connect is intended for merchants with high-value NetBanking use cases, including insurance, financial services, government and utilities, education-fee payments, loan and EMI repayments, SIP or investment contributions, B2B invoice settlement, and travel bookings.

## Bank rollout

The attached product brief lists HDFC Bank, ICICI Bank, Axis Bank, YES Bank, Federal Bank, and AU Small Finance Bank as currently live via NBBL. It lists SBI, IDBI Bank, Bank of Baroda, IDFC FIRST Bank, Canara Bank, Kotak Mahindra Bank, and CSB Bank as coming soon.

> **Publication note:** The source brief contains a separate supporting statement that mentions four live banks, while its detailed live-bank list contains six. This page uses the detailed list and the discrepancy is recorded in the delivery notes. Confirm the live-bank list with Product before publication.

## Related documentation

- [PayU Hosted Customer Journey - Banking Connect](./payu-hosted-customer-journey-banking-connect.md)
- [Handle NBBL Deep-Links in WebView](./handle-nbbl-deep-links-in-webview.md)
