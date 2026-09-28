---
title: Merchant Hosted Customer Journey - Banking Connect
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
NBBL Banking Connect is PayU's implementation of NPCI Bharat BillPay Limited's standardized NetBanking framework. It keeps the trust and high-value capability of NetBanking while replacing the checkout experience built around bank-website credentials with a mobile-first, password-free flow.

## What changes for the customer

The customer selects a bank at checkout and authenticates inside that bank's app. Depending on the device and available bank flow, the customer either opens the app through an intent deep link or scans a QR code displayed on the checkout page.

The customer uses the bank app's authentication method, such as biometrics or an app MPIN. The customer does not enter NetBanking credentials on a merchant or PayU page.

If the selected bank app is not installed, or the app-first path is not enabled, the journey can fall back to the bank website NetBanking flow.

## Payment flows

### Desktop QR flow

1. The customer selects a bank under NetBanking.
2. PayU offers the available payment modes, such as QR or the bank website.
3. PayU displays a NetBanking QR code.
4. The customer scans the QR code with the bank's mobile app.
5. The customer authenticates in the bank app.
6. The customer confirms the debit account.
7. PayU displays the payment result to the customer and merchant.

![](https://files.readme.io/654ab97c2c1e813d651d2852842a01d9d83556e3135ebb6e8a1581ff5122ed48-Seamless_web_checkout_flow.png)

<br />

### Mobile app-intent flow

1. The customer selects a bank under NetBanking.
2. PayU offers the option to pay through the selected bank app.
3. PayU opens the installed bank app through a deep link.
4. The customer authenticates in the bank app with biometrics or an app MPIN.
5. The customer confirms the debit account.
6. The customer returns to the merchant with the payment result.

#### iOS Device Customer Journey


<Image src="https://files.readme.io/59b07a2e46f06543352360d8838b2c0592f0ff84d677e662accc8f6c7f2550e4-Seamless_iOS_payment_flow_final.png" width="400px" border={true} framed={true} />


#### Android Device Customer Journey


<Image src="https://files.readme.io/9b6c32b4942c08f21c5e01992d4cdad7bcdb5ee58edf8e39a9e47dfec5e81c83-Seamless_Android_payment_flow_final.png" border={true} />


<br />

###

### Website fallback

When the bank app is not installed or the app-first route is unavailable, the customer can continue with the familiar bank-website NetBanking journey.

### Merchant Changes

- No integration changes required to enable the desktop based flow. Existing flow will work as is.
- To enable intent flow in mobile webview; please refer the document - Handle NBBL Deep-Links in WebView

## Related documentation

- [PayU Hosted Customer Journey - Banking Connect](doc:payu-hosted-customer-journey-banking-connect)
- [Handle NBBL Deep-Links in WebView](doc:handle-nbbl-deep-links-in-webview)
