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

#### iOS Device Customer Journey


<Image src="https://files.readme.io/455332377a6b2b3672bee27ea371361c76903d85a9ca1d068e732a5164683953-seamless-ios-flow_1.png" border={true} />


#### Android Device Customer Journey

![](https://files.readme.io/6d943cfba74fb655577dbcc16aa12049bf215b9c03f74b59bf7b056df1abcbf0-Android_seamless_payment_flow.png)

<br />

### Desktop QR flow

1. The customer selects a bank under NetBanking.
2. PayU offers the available payment modes, such as QR or the bank website.
3. PayU displays a NetBanking QR code.
4. The customer scans the QR code with the bank's mobile app.
5. The customer authenticates in the bank app.
6. The customer confirms the debit account.
7. PayU displays the payment result to the customer and merchant.

![](https://files.readme.io/ed9e856425b3019f34ec74c1a3f7fcd1fc45f71f2aabc678a60ef0f7352c3c6a-Seamless_web_checkout_flow.png)

<br />

### Website fallback

When the bank app is not installed or the app-first route is unavailable, the customer can continue with the familiar bank-website NetBanking journey.

## Related documentation

- [PayU Hosted Customer Journey - Banking Connect](doc:payu-hosted-customer-journey-banking-connect)
- [Handle NBBL Deep-Links in WebView](doc:handle-nbbl-deep-links-in-webview)
