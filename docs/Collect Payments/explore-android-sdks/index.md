---
title: Android Mobile SDKs
excerpt: >-
  Explore the Android SDKs offered by PayU to find the best fit for your use
  case.
deprecated: false
hidden: false
metadata:
  title: PayU Android SDK
  description: >-
    PayU offers various Android SDKs for integrating payment interfaces into
    your app, including Checkout Pro SDK for a ready-to-use UI, Core SDK for
    more customization, UPI SDK for UPI payments, OlaMoney SDK for OlaMoney
    payments, PhonePe SDK for PhonePe payments, Native OTP Assist SDK for
    capturing OTP, and 3DS 2.0 SDK for additional transaction data and fraud
    protection. The best SDK for you depends on your specific needs and
    requirements.
  keywords:
    - PayU Mobile SDK
    - ' Payment Gateway for Android Mobile'
    - ' PayU India Android SDK'
    - PayU Android SDK
    - ' PayU Android SDK integration'
    - ' Android payment SDK'
    - ' Mobile payment Android SDK'
  robots: index
next:
  description: ''
---
PayU offers various Android SDKs that each serve a unique use case. Here is a brief overview of the most popular SDKs:

* **Checkout Pro SDK**: The Checkout Pro SDK is a complete, ready-to-use native checkout UI that allows you to integrate a payment interface with minimal effort and get started quickly. The SDK includes a variety of features, such as support for multiple payment methods, a secure payment gateway, and a user-friendly interface.

* **Core SDK**: The Core SDK allows you to integrate the PayU payment gateway into your own payment interface. This gives you more control over the look and feel of the payment interface, as well as the ability to add custom features and functionality.

* **UPI SDK**: The UPI SDK allows you to integrate Unified Payments Interface (UPI) payments into your Android app. UPI is a popular payment method in India that allows users to make payments directly from their bank accounts.

* **PhonePe SDK**: PhonePay SDK offers in app experience to start collecting payments through instruments saved on phone. Supports UPI, card and wallet payments along with UPI PIN authentication.

* **Gpay SDK**: Gpay SDK offers in app experience to start collecting payments through instruments saved on gpay and phone. Supports UPI, card and wallet payments along with UPI PIN authentication.

* **OlaMoney SDK**: The OlaMoney SDK allows you to integrate OlaMoney payments into your Android app. OlaMoney is a digital wallet that allows users to make payments for goods and services online and offline.

* **Native OTP Assist SDK**: The Native OTP Assist SDK allows you to capture OTP (One-Time Password) directly from your Android app without redirecting the user to the bank's 3D secure page. This can help to improve the checkout experience and reduce the chances of abandonment.

* **3DS 2.0 SDK**: The 3DS 2.0 SDK probides you the ability to collect additional transaction data such as device location, user's location, and merchant's transaction history. It allows you to protect you and your customers from the threat of payment fraud.

## Choose your integration

<Callout icon="✅" theme="okay">
  The best SDK for you will depend on your specific needs and requirements.
</Callout>

If you need a quick and easy way to integrate a payment interface into your app, then the Checkout Pro SDK is a good option. If you need more control over the look and feel of the payment interface, then the Core SDK is a good choice. And if you need to accept payments through UPI, OlaMoney, PhonePe, or Native OTP Assist, then the respective SDKs are a good fit.

Here is a comparison table that summarizes the key features of the different SDKs:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        SDK
      </th>

      <th>
        Features
      </th>

      <th>
        Use Case
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Android CheckoutPro SDK](doc:android-checkoutpro-sdk)
      </td>

      <td>
        Complete ready-to-use native checkout UI allows you to get started quickly with minimal effort. This SDK is a great choice for small and medium sized businesses that operates on limited tech resource.
      </td>

      <td>
        | **Low Effort Integration**, | **Non-Seamless Checkout** | **Limited Tech** | **Resource** |
      </td>
    </tr>

    <tr>
      <td>
        [Android Core SDK](doc:android-core-sdk)
      </td>

      <td>
        Create your own UI for the payment flow by leveraging various methods exposed in the Core SDK. This SDK is more suitable for larger enterprises that can allocate dedicated engineering resource to develop customised payment flow.
      </td>

      <td>
        | **Seamless Checkout** | **Medium Effort** |  **Enterprise Businesses** |
      </td>
    </tr>

    <tr>
      <td>
        [Android UPI SDK](doc:android-upi-sdk)
      </td>

      <td>
        This SDK best suited for creating a custom payment UI for UPI only checkout.
      </td>

      <td>
        * _Low Effort Integration_*|
          **UPI Checkout**
      </td>
    </tr>

    <tr>
      <td>
        [PhonePe SDK](https://docs.payu.in/docs/android-phonepe-sdk)
      </td>

      <td>
        Allows you to integrate PhonePe payments into your Android app.
      </td>

      <td>
        **Low Effort Integration** | **PhonePe InApp Support**
      </td>
    </tr>

    <tr>
      <td>
        [Google Pay SDK](doc:android-google-pay-sdk)
      </td>

      <td>
        Allows you to integrate Gpay payments into your Android app.
      </td>

      <td>
        **Low Effort Integration** | **Gpay InApp Support**
      </td>
    </tr>

    <tr>
      <td>
        [Android Ola Money SDK](doc:ola-money-sdk)
      </td>

      <td>
        Allows you to integrate OlaMoney payments into your Android app.
      </td>

      <td>
        **Low Effort Integration**|**OlaMoney Checkout**
      </td>
    </tr>

    <tr>
      <td>
        [Android Native OTP Assist SDK](doc:native-otp-assist-sdk)
      </td>

      <td>
        Allows you to capture OTP (One Time Password) directly from your Android app without redirecting the user to the bank's 3D secure page.
      </td>

      <td>
        **Native OTP Support**| **Low Effort Integration**
      </td>
    </tr>

    <tr>
      <td>
        [Android 3DS 2.0 SDK](https://docs.payu.in/docs/android-3ds20-sdk)
      </td>

      <td>
        Power native experience on the new 3DS 2.0 protocol for card transactions.
      </td>

      <td>
        **3DS 2.0 Support**| **Low Effort Integration**
      </td>
    </tr>
  </tbody>
</Table>

## Size of SDK

| SDK Name                                                             | Latest SDK Version | SDK Size |
| :------------------------------------------------------------------- | :----------------- | :------- |
| [CheckoutPro SDK](https://docs.payu.in/docs/android-checkoutpro-sdk) | 3.3.7              | 293KB    |
| [Core PG SDK](https://docs.payu.in/docs/android-core-sdk)            | 7.12.3             | 163KB    |
| [CustomBrowser SDK](https://docs.payu.in/docs/custom-browser-sdk)    | 7.16.6             | 386KB    |
| [UPI SDK](doc:android-upi-sdk)                                       | 1.8.15             | 163KB    |
| [PhonePe SDK](https://docs.payu.in/docs/android-phonepe-sdk)         | 1.8.9              | 68KB     |
| [Google Pay SDK](doc:android-google-pay-sdk)                         | 4.0.2              | 94KB     |
| [OlaMoney SDK](https://docs.payu.in/docs/ola-money-sdk)              | 1.3.14             | 47KB     |
| [Native OTP SDK](https://docs.payu.in/docs/native-otp-assist-sdk)    | 1.6.5              | 194Kb    |
| [3DS 2.0 SDK](https://docs.payu.in/docs/android-3ds20-sdk)           | 2.0.2              | 80KB     |

<br />
