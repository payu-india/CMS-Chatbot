---
title: 2. Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: iOS Checkout Pro SDK Test Integration
  description: >-
    After integrating payment methods, you must test before going live. Test
    credentials are provided for Net Banking, UPI, EMI cards, and wallets like
    PayTM and AmazonPay.
  keywords:
    - IOS Checkout Pro SDK Integration Testing
    - PayU IOS SDK Integration Testing
    - Test Mobile payment integration with PayU IOS SDK
    - PayU IOS Checkout Pro for Mobile Integration Test
    - IOS CheckoutPro SDK Integration Testing
    - PayU Hosted Checkout SDK for Mobile Integration Testing
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

### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

* **user name:** payu
* **password**: payu
* **OTP**: 123456

### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

* [anything@payu](anything@payu)
* [9999999999@payu.in](mailto:9999999999@payu.in)

> ❗️ Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

### Test cards for EMI

You can use the following Debit and Credit cards to test EMI integration.

<EMITestCards />

<br />

### Test wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Wallet
      </th>

      <th>
        Mobile Number
      </th>

      <th>
        OTP
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        PayTM
      </td>

      <td>
        7777777777
      </td>

      <td>
        888888
      </td>
    </tr>

    <tr>
      <td>
        PhonePe
      </td>

      <td>
        Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)
        Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.
      </td>

      <td>
        NA
      </td>
    </tr>

    <tr>
      <td>
        AmazonPay
      </td>

      <td>
        You can test using your original Amazon account details.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>