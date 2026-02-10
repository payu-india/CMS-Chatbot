---
title: Copy of Integration Steps
deprecated: false
hidden: true
metadata:
  title: Integration Steps - Android Customer Browser
  keywords:
    - Integration Steps - Android Customer Browser
    - Android Customer Browser Integration Steps
    - Integrate Android Customer Browser
    - Android Customer Browser Integration Steps
    - Custom Browser Android Integration Steps
    - Custom Browser Mobile SDK - Android Integration Steps
  robots: index
---
---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps - Android Customer Browser
  description: ''
  keywords:
    - Integration Steps - Android Customer Browser
    - Android Customer Browser Integration Steps
    - Integrate Android Customer Browser
    - ' Android Customer Browser Integration Steps'
    - ' Custom Browser Android Integration Steps'
    - Custom Browser Mobile SDK - Android Integration Steps
  robots: index
next:
  description: ''
---

The Android Customer Browser integration involves the following steps:

<Cards columns={3}>
  <Card title="1. SDK Integration" href="#sdk-integration">
    Set up build.gradle, check payment availability, and invoke CustomBrowser

    <br />
  </Card>

  <Card title="2. Test the Integration" href="#test-the-integration">
    Test the integration with test credentials before going live

    <br />
  </Card>

  <Card title="3. Go-live Checklist" href="#go-live-checklist">
    Configure production settings, verify payment method, and webhooks
  </Card>

  <br />
</Cards>

## SDK Integration

Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. PayU enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you. For more information, refer to <Anchor label="Configure Checkout Payment Methods" target="_blank" href="https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings">Configure Checkout Payment Methods</Anchor>.

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

### Step 2: Set Up build.gradle

Add the following dependency in your application’s build.gradle:

```
implementation 'in.payu:payu-custom-browser:7.16.0'
```

<Callout icon="🚧" theme="warn">
  **Watch Out**: If you are getting the following error: `Default interface methods are only supported starting with Android N (--min-api 24): Landroidx/lifecycle/DefaultLifecycleObserver;onCreate(Landroidx/lifecycle/LifecycleOwner;)V`

  Add the following compileOptions on your app's build.gradle:

  ```
  android {
   compileOptions {
          sourceCompatibility 1.8
          targetCompatibility 1.8
      }
      }
  ```
</Callout>

From version 7.4.0 onwards, it is mandatory to import UPI SDK dependency if you want to make payments through any of the following UPI options along with the changes mentioned in the Third-Party Payments Support section.

* UPI Intent
* Collect
* Google Pay
* PhonePe

```
<uses-permission android:name="android.permission.RECEIVE_SMS" />
```

<Callout icon="👍" theme="okay">
  **Tip**: Merchants are advised to add this permission in the application’s `AndroidManifest.xml` to support OTP assist. In case your application supports a minimum SDK of less than 20, do these changes in your surl/furl.
</Callout>

### Step 3: Check for Payment Availability

The `CheckForPaymentAvailability` function in CustomBrowser class. Checks for payment option type availability:

```Text Input

      Activity : activity instance
      PaymentOption : Payment Option type e.g.PaymentOption.SAMSUNGPAY,PaymentOption.PHONEPE
      PayUCustomBrowserCallback : this class provide callbacks 
      paymentOptionHash : Payment Related Details Hash
      merchantKey : PayU Merchant Key
      user_credentials : User credentials or use "default"
```

> 📘 Generate PaymentOption Hash
>
> To generate PaymentOption Hash refer to Hash Generation.
>
> Formula :-sha512(key|command|var1|salt)
>
> where
>
> key= Provide your merchant key here
> command= "payment_related_details_for_mobile_sdk" // Api Commands
> salt=  Provide your merchant salt here
> var1= Provide user credentials or use "default"
>
> For more information, refer to  [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

**Sample**

```java Java
new CustomBrowser().checkForPaymentAvailability(Activity activity, PaymentOption paymentOption, PayUCustomBrowserCallback payUCustomBrowserCallback, String paymentOptionHash, String merchantKey, String user_credentials)
```

### Step 2: Invoke CustomBrowser

To invoke CustomBrowser:

Create a basic object of CustomBrowserConfig similar to the following code snippet. For more information on configurations supported, refer to  [Android CustomBrowser Configurations](doc:android-custombrowser-configurations).

<Callout icon="📘" theme="info">
  **Post URL** can be any of the following:

  Production - [https://secure.payu.in/_payment](https://secure.payu.in/_payment)
  Staging - [https://test.payu.in/_payment](https://test.payu.in/_payment)
</Callout>

```java JAVA
CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey,txnId);
customBrowserConfig.setPayuPostData(<Post Data>);
customBrowserConfig.setPostUrl(<Post Url>);
```

1. Create an object of `PayUCustomBrowserCallback`.
2. Call method `addCustomBrowser()` similar to the following code snippet:

**Input:**

* `Activity`: activity instance.
* `CustomBrowserConfig`: configuration object of the custom browser.
* `PayUCustomBrowserCallback`: this class provides callbacks.

```java Java
Input:
    Activity : activity instance
    CustomBrowserConfig : configuration object of the custom browser
    PayUCustomBrowserCallback : this class provide callbacks
```

**Sample**

```java Java
new CustomBrowser().addCustomBrowser( Activity activity, CustomBrowserConfig customBrowserConfig, PayUCustomBrowserCallback cbPayUCustomBrowserCallback)
```

### Sample Post Request

#### Card

```java
firstname=John&ccnum=5123456789012346&device_type=1&ccvv=123&ccexpyr=2025&key=gt****&email=snooze@payu.in
&bankcode=CC&txnid=1705055037779&amount=1.0&udf5=udf5&ccexpmon=05&surl=https://cbjs.payu.in/sdk/success
 &udf3=udf3&udf4=udf4&udf1=udf1&udf2=udf2&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"},{"platform":"android","name":"coresdk","version":"7.0.1"},
{"platform":"android","name":"pgsdk","version":"2.0.5"},{"platform":"android","name":"custombrowser","version":"7.11.14"}]
&phone=99999*****&pg=CC&furl=https://cbjs.payu.in/sdk/failure&productinfo=Macbook+Pro&ccname=PayuUser
&hash=a13d39d161c4377b4e81a97bc8b8bf06835628d208b379f3a15a4e352b88d1dc6fde878ff89e5c7d0eeb36f214d996313f4672432a92244c4950224a472c669b
```

#### Net Banking

```
amount=1.0&firstname=John&udf5=udf5&device_type=1&surl=https://cbjs.payu.in/sdk/success&udf3=udf3&
udf4=udf4&udf1=udf1&udf2=udf2&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"},
{"platform":"android","name":"coresdk","version":"7.0.1"},{"platform":"android","name":"pgsdk","version":"2.0.5"},{"platform":"android","name":"custombrowser","version":"7.11.14"}]
&phone=99999*****&pg=NB&furl=https://cbjs.payu.in/sdk/failure&productinfo=Macbook+Pro&key=gt****&email=snooze@payu.in
&hash=84d0fe7da879adb22429f2f4c33334c31ed164d819356b5f8842d4c207560cc4251c76b4211a476ca029ffd5581b6f760afe97c35c635d2eaa75d379619e6145
&bankcode=SBIB&txnid=1705055218155
```

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `pg` `**mandatory**`
      </td>

      <td>
        `String` It defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page.
        For NetBanking, pg=NB.
      </td>

      <td>
        TESTPG
      </td>
    </tr>

    <tr>
      <td>
        `bankcode `**mandatory**`
      </td>

      <td>
        `String` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For the list of bank codes that can be used with the `bankcode` parameter, refer to

        [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes)

        .
        Reference: For the test Net Banking credentials, refer to

        [Test Cards, UPI ID, and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets)

        .
      </td>

      <td>
        TESTPGNB
      </td>
    </tr>
  </tbody>
</Table>

For the supported payment method, refer to [Supported Payment Methods](doc:android-coresdk-supported-payment-method).

## Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

<TestCardsCallout />

<Accordion title="Test credentials for supported payment methods" icon="fa-vial">
  Following are the payment methods supported in PayU Test mode.

  <Accordion title="Test credentials for Net Banking" icon="fa-university">
    Use the following credentials to test the Net Banking integration:

    * **user name:** payu
    * **password**: payu
    * **OTP**: 123456
  </Accordion>

  <Accordion title="Test VPA for UPI" icon="fa-mobile">
    > ❗️ Callout
    >
    > The UPI in-app and UPI intent flow is not available in the Test mode.

    You can use either of the following VPAs to test your UPI-related integration:

    * [anything@payu](anything@payu)
    * [9999999999@payu.in](mailto:9999999999@payu.in)

    For Testing the UPI Collect flow, Please follow the below steps:-

    1. Once you enter the VPA click on the verify button and proceed to pay.
    2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
    3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

    [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)\<Txn\_id>

    \**For Android*

    You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

    > 🚧 Ensure to remove the code from the manifest file before going live.

    ```xml XML
    <application>
    <meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
    <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
    <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
    </appliction>
    ```
  </Accordion>

  <Accordion title="Test cards for EMI" icon="fa-credit-card">
    You can use the following Debit and Credit cards to test Emi integration.

    |              |                                                                                                                                                                                              |
    | :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Kotak DC EMI | 1. **Card Number**: 4706-1378-0509-9594
    2. **Expiry**: any future date (mm/yy)
    3. **CVV**: 123
    4. **OTP**: 111111
    5. **Name**: Any name
    6. **Mobile Number**: 9123412345 (mandatory for EMI) |
    | AXIS DC EMI  | 1) **Card Number**: 4011-5100-0000-0007
    2) **Expiry**: any future date (mm/yy)
    3) **CVV**: 123
    4) **OTP**: 111111
    5) **Name**: Any name
    6) **Mobile Number**: 9123412345 (mandatory for EMI) |
    | HDFC CC EMI  | 1. **Card Number**: 4453-3410-65876437
    2. **Expiry**: any future date (mm/yy)
    3. **CVV**: 123
    4. **OTP**: 111111
    5. **Name**: Any name
    6. **Mobile Number**: 9123412345 (mandatory for EMI)  |
    | ICICI CC EMI | 1) **Card Number**: 4453-3410-65876437
    2) **Expiry**: any future date (mm/yy)
    3) **CVV**: 123
    4) **OTP**: 111111
    5) **Name**: Any name
    6) **Mobile Number**: 9123412345 (mandatory for EMI)  |
  </Accordion>

  <Accordion title="Test Wallets" icon="fa-wallet">
    You can use the following wallets and their corresponding credentials to test wallet integration.

    <Table align={["left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Wallet
          </th>

          <th style={{ textAlign: "left" }}>
            Mobile Number
          </th>

          <th style={{ textAlign: "left" }}>
            OTP
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            PayTM
          </td>

          <td style={{ textAlign: "left" }}>
            7777777777
          </td>

          <td style={{ textAlign: "left" }}>
            888888
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            PhonePe
          </td>

          <td style={{ textAlign: "left" }}>
            Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location:

            [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)

            Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.
          </td>

          <td style={{ textAlign: "left" }}>
            NA
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            AmazonPay
          </td>

          <td style={{ textAlign: "left" }}>
            You can test using your original Amazon account details.
          </td>

          <td style={{ textAlign: "left" }} />
        </tr>
      </tbody>
    </Table>
  </Accordion>
</Accordion>

## Go-live Checklist

Ensure these steps before you deploy the integration in a live environment.

<Accordion title="Collect Live payments" icon="fa-credit-card">
  After testing the integration end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

  > 🚧 Watch Out!
  >
  > Ensure that you are using the production merchant key and salt generated in the live mode.

  <ProductionKeyAndSaltProcedure />
</Accordion>

<Accordion title="Checklist 2: Configure setIsProduction()" icon="fa-cog">
  Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.
</Accordion>

<Accordion title="Checklist 3: Configure verify payment method" icon="fa-check-circle">
  Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.
</Accordion>

<Accordion title="Checklist 4: Configure Webhook" icon="fa-plug">
  We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).

  <br />

  During the integration, refer the [Generate Static Hash](doc:generate-static-hash-android-sdk-pro) for hash generation details.
</Accordion>