---
title: '[REVIEW]PayU Hosted Customer Journey - Banking Connect'
deprecated: false
hidden: true
metadata:
  robots: index
---
This page describes the customer journey for NBBL Banking Connect in PayU Hosted Checkout on mobile and desktop.

> **Enable Banking Connect:** Contact your PayU Key Account Manager or [PayU Support](https://help.payu.in) to enable Banking Connect for a merchant.
>
> **WebView integrations:** If you load the PayU payment page in an Android or iOS WebView, follow [Handle NBBL Deep-Links in WebView](./handle-nbbl-deep-links-in-webview.md).

## Mobile: app-intent flow

The app-intent flow sends the customer from PayU Hosted Checkout to the installed bank app.

### Steps

1. The customer selects a bank under NetBanking.
2. PayU displays the option to pay through the selected bank app.
3. The customer selects the bank-app option.
4. PayU opens the bank app through a deep link.
5. The customer authenticates with the bank app's biometric or MPIN flow.
6. The customer confirms the debit account.
7. The customer returns to the merchant with the payment result.

### Example interface states

![Select bank and payment mode](../figma-crops/01-payment-mode.png)

![Processing payment in the bank app](../figma-crops/02-processing-payment.png)

![Bank app approval](../figma-crops/03-approve-payment.png)

![Payment success](../figma-crops/04-payment-success.png)

## Desktop: QR flow

The QR flow lets a customer start on a desktop checkout and complete authentication in the bank's mobile app.

### Steps

1. The customer selects a bank under NetBanking.
2. PayU presents the available modes, such as QR or the bank website.
3. PayU generates and displays a NetBanking QR code.
4. The customer scans the QR code with the bank's mobile app.
5. The customer authenticates in the app.
6. The customer confirms the debit account.
7. The customer returns to the merchant page after the payment result is available.

### Example interface states

![Scan a QR or UPI QR](../figma-crops/05-qr-scanner.png)

![Select an installed bank app](../figma-crops/06-select-installed-bank-app.png)

![Payment completed in the bank app](../figma-crops/07-bank-app-success.png)

## Website fallback

If the selected bank app is not installed, or the app-first flow is unavailable, the customer can continue with the bank website option. This preserves a way to pay without requiring the customer to install a banking app.

![Payment processing fallback](../figma-crops/08-processing-fallback.png)

## Payment states

PayU Hosted Checkout can show the relevant result after the bank flow returns:

- **Payment successful:** The payment is complete and the customer is taken back to the merchant.
- **Payment cancelled:** The customer cancels the payment and is returned to the merchant.
- **Transaction timed out:** The payment does not complete within the available time and the customer is returned to the merchant.
- **Processing:** The customer is instructed to complete the payment in the bank app. If the customer is not redirected automatically, the interface can provide an action to open the bank app.

![Payment cancelled](../figma-crops/09-payment-cancelled.png)

![Transaction timed out](../figma-crops/10-payment-timeout.png)

![Open the bank app when not redirected](../figma-crops/11-open-bank-app.png)

![Continue paying or cancel](../figma-crops/12-exit-confirmation.png)

## Customer security

Authentication takes place in the customer's bank app. The product brief states that the customer does not enter NetBanking credentials on a merchant or PayU page.

Do not ask customers to share their bank-app MPIN, biometric information, or NetBanking password with the merchant or PayU.

## Merchant impact

The product brief states that merchants do not need to change their existing NetBanking integration. PayU can enable the capability in a phased bank-by-bank rollout or through traffic splits. Existing reconciliation and settlement processes remain unchanged according to the brief.
