---
title: Merchant Hosted Customer Journey - Banking Connect
deprecated: false
hidden: true
metadata:
  robots: index
---
NBBL Banking Connect is PayU's implementation of NPCI Bharat BillPay Limited's standardized NetBanking framework. It keeps the trust and high-value capability of NetBanking while replacing the checkout experience built around bank-website credentials with a mobile-first, password-free flow.

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

### Net Banking

Modern mobile-first approach using QR codes and app intents:

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

## Related documentation

- [PayU Hosted Customer Journey - Banking Connect](doc:payu-hosted-customer-journey-banking-connect)
- [Handle NBBL Deep-Links in WebView](doc:handle-nbbl-deep-links-in-webview)
