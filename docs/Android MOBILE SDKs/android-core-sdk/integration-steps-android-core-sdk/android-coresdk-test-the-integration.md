---
title: 2. Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: Test the Android Custom Browser SDK Integration
  description: >-
    After integrating payment methods, you must test before going live. Test
    credentials are provided for cards, net banking, UPI, EMI, and wallets to
    ensure successful testing
  keywords:
    - Android Custom Browser SDK Integration Testing
    - PayU Android SDK Integration Testing
    - Test Mobile payment integration with PayU Android SDK
    - PayU Android Custom Browser for Mobile Integration Test
  robots: index
next:
  description: ''
---
After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

<TestCardsCallout />

## Test credentials for supported payment methods

Following are the payment methods supported in PayU Test mode.

### Test Credential for Card

| Card Number      | Expiry | CVV | OTP    |
| :--------------- | :----- | :-- | :----- |
| 5123456789012346 | 05/25  | 123 | 123456 |

### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

* **user name:** payu
* **password**: payu
* **OTP**: 123456

### Test VPA for UPI

> ❗️ Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

You can use either of the following VPAs to test your UPI-related integration:

* [anything@payu](anything@payu)
* [9999999999@payu.in](mailto:9999999999@payu.in)

For Testing the UPI Collect flow, Please follow the below steps:-

1. Once you enter the VPA click on the verify button and proceed to pay.
2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.\
   [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)\<Txn\_id>

**For Android**

You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

> 🚧 Ensure to remove the code from the manifest file before going live.

```Text XML
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
</appliction>
```

### Test cards for EMI

You can use the following Debit and Credit cards to test EMI integration.

<EMITestCards />

### Test Wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

<EMITestWallets />