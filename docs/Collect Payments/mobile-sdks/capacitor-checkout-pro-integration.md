---
title: '[Internal Review]Capacitor Checkout Pro Integration'
deprecated: false
hidden: true
icon: fad fa-air-conditioner
link:
  new_tab: false
metadata:
  robots: index
---
PayU Checkout Pro for Capacitor lets you add a complete, PayU-built checkout screen to your Capacitor (Ionic) app. Your app passes the payment details, your server generates the security hash, and the plugin handles the payment and returns the result to your app.

## Before you begin

Make sure you have:

- A PayU merchant account with your **merchant key** and **salt**. Keep the salt on your server only.
- A Capacitor app that meets the requirements below.
- A server endpoint that can generate the payment hash (see [Step 5](#step-5-generate-the-hash-on-your-server)).

### Requirements

| Platform    | Requirement          |
| ----------- | -------------------- |
| Android SDK | Version 21 and above |
| Compile SDK | Version 31 and above |

## Integration steps

1. [Install the plugin](#step-1-install-the-plugin)
2. [Import the plugin](#step-2-import-the-plugin)
3. [Create the payment parameters](#step-3-create-the-payment-parameters)
4. [Configure the checkout screen](#step-4-configure-the-checkout-screen)
5. [Generate the hash on your server](#step-5-generate-the-hash-on-your-server)
6. [Launch the checkout screen](#step-6-launch-the-checkout-screen)
7. [Handle the payment result](#step-7-handle-the-payment-result)

***

## Step 1: Install the plugin

Run the following command in your project root:

```bash
npm install @capacitor/payu-checkoutpro-capacitor
npx cap sync
```

<Callout icon="🚧" theme="warn">
  ### Android theme conflict

  If your build fails with an error like:

  `Attribute application@theme value=(@style/Theme.TestApp) from AndroidManifest.xml is also present at [in.payu:payu-checkout-pro-ui] ... value=(@style/OnePayuTheme)`

  add `tools:replace="android:theme"` to the `<application>` tag in your app's `AndroidManifest.xml`:

  ```xml
  <manifest xmlns:android="<redacted URL>"
      xmlns:tools="<redacted URL>">
      <application
          android:theme="@style/AppTheme"
          tools:replace="android:theme">
          ...
      </application>
  </manifest>
  ```
</Callout>

## Step 2: Import the plugin

Import the plugin into the TypeScript page where you start the payment:

```typescript
import { PayUCheckoutProCapacitor } from '@capacitor/payu-checkoutpro-capacitor';
```

## Step 3: Create the payment parameters

Create a `payUPaymentParams` object with the details of the current payment.

```typescript
const payUPaymentParams: any = {
  key: '<merchant_key>',
  transactionId: '<unique_txn_id>',
  amount: '100.0',
  productInfo: 'ProductInfo',
  firstName: 'Firstname',
  email: 'test@payu.in',
  phone: '9999999999',
  android_surl: 'https://cbjs.payu.in/sdk/success',
  android_furl: 'https://cbjs.payu.in/sdk/failure',
  ios_surl: 'https://cbjs.payu.in/sdk/success',
  ios_furl: 'https://cbjs.payu.in/sdk/failure',
  environment: '<environment_value>',
  userCredential: '<merchant_key>:<user_id>', // For saved cards
  userToken: '<user_token>',                 // For offers
  additionalParam: {
    payment_related_details_for_mobile_sdk: '<value>',
    merchantAccessKey: '<value>',
    vas_for_mobile_sdk: '<value>',
    walletUrn: '<value>',
    SodexoSourceId: '<value>',
    udf1: '<value>',
    udf2: '<value>',
    udf3: '<value>',
    udf4: '<value>',
    udf5: '<value>',
  },
  enableNativeOtp: true,
};
```

### Payment parameters

#### Mandatory parameters

| Parameter                   | Type   | Description                                                                                                                              | Example                              |
| :-------------------------- | :----- | :--------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| `key`                       | String | Your merchant key from PayU.                                                                                                             | `"sms***"`                           |
| `transactionId`             | String | A unique ID for this transaction. It can't be empty, can be up to 25 characters, and can't contain special characters such as `_ $ % &`. | `"4567890"`                          |
| `amount`                    | String | The total amount of the transaction.                                                                                                     | `"100.0"`                            |
| `productInfo`               | String | A short description of the product.                                                                                                      | `"ProductInfo"`                      |
| `firstName`                 | String | The customer's first name.                                                                                                               | `"Firstname"`                        |
| `email`                     | String | The customer's email address.                                                                                                            | `"test@payu.in"`                     |
| `phone`                     | String | The customer's phone number.                                                                                                             | `"9999999999"`                       |
| `android_surl` / `ios_surl` | String | The success URL. PayU loads this URL and passes the response when the payment succeeds.                                                  | `"https://cbjs.payu.in/sdk/success"` |
| `android_furl` / `ios_furl` | String | The failure URL. PayU loads this URL and passes the response when the payment fails.                                                     | `"https://cbjs.payu.in/sdk/failure"` |
| `environment`               | String | Sets whether the payment runs in test or production.                                                                                     | —                                    |

#### Optional parameters

| Parameter         | Type    | Description                                                                                                                                                                                                                                                                                              | Example                |
| :---------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| `userCredential`  | String  | Used to save cards and show a customer's saved cards. Format: `<merchantKey>:<userId>`, where `userId` is any ID, email or phone number that uniquely identifies the customer.                                                                                                                           | `"merchantKey:userId"` |
| `userToken`       | String  | Lets the offer engine apply usage limits per customer. Needed for offers on UPI, Net Banking and Wallets. For card offers (credit card, debit card, EMI), limits apply to this token if you pass it, or to the card number if you don't.                                                                 | `"ABC456789"`          |
| `additionalParam` | String  | Additional parameter fields for payment related details, VAS details, Wallet URN, Sodexo Source ID and your own customn data in user defined fields, such as an order reference. For more information, refer to [additionalParam Object Fields Description](#additionalparam-object-fields-description). | `"order_9876"`         |
| `enableNativeOtp` | Boolean | Turns on the native OTP screen.                                                                                                                                                                                                                                                                          | `true`                 |

<Callout icon="❗️" theme="error">
  ### Test URLs

  The sample success and failure URLs are for testing only. Going live with them may cause transaction errors. Replace them with your own URLs before going live.
</Callout>

### additionalParam Object Fields Description

Pass these inside the `additionalParam` object.

| Parameter                                | Type   | Description                                                                                          |
| ---------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| `payment_related_details_for_mobile_sdk` | String | Payment-related details for the mobile SDK.                                                          |
| `merchantAccessKey`                      | String | Your merchant access key.                                                                            |
| `vas_for_mobile_sdk`                     | String | Value-added services details for the mobile SDK.                                                     |
| `walletUrn`                              | String | Wallet URN, for wallet payments.                                                                     |
| `SodexoSourceId`                         | String | Sodexo source ID, for Sodexo card payments.                                                          |
| `udf1` – `udf5`                          | String | User-defined fields. Use these to pass any extra information you want returned with the transaction. |

### Recurring payments (Standing Instruction)

To set up a recurring payment, create an SI object and attach it to `payUPaymentParams` as `payUSIParams`:

```typescript
const siParamObject = {
  isFreeTrial: false,
  billingAmount: '100.00',
  billingInterval: '<billing_interval>',
  paymentStartDate: '<start_date>',
  paymentEndDate: '<end_date>',
  billingCycle: '<billing_cycle>',
  remarks: 'Monthly subscription',
  billingCurrency: 'INR',
};

payUPaymentParams.payUSIParams = siParamObject;
```

| Parameter          | Type    | Description                                                 |
| ------------------ | ------- | ----------------------------------------------------------- |
| `isFreeTrial`      | Boolean | Set to `true` if the subscription starts with a free trial. |
| `billingAmount`    | String  | Amount charged each billing cycle.                          |
| `billingInterval`  | String  | Number of billing cycles between each charge.               |
| `paymentStartDate` | String  | Date of the first recurring payment.                        |
| `paymentEndDate`   | String  | Date of the last recurring payment.                         |
| `billingCycle`     | String  | Frequency of the billing cycle.                             |
| `remarks`          | String  | Remarks for the recurring payment.                          |
| `billingCurrency`  | String  | Currency for billing, for example `INR`.                    |

## Step 4: Configure the checkout screen

Create a `payUCheckoutProConfig` object to customise the checkout screen:

```typescript
const payUCheckoutProConfig: any = {
  primaryColor: '#4c31ae',
  secondaryColor: '#ffffff',
  merchantName: 'Your Store',
  merchantLogo: this.merchantLogo,
  showExitConfirmationOnCheckoutScreen: true,
  showExitConfirmationOnPaymentScreen: true,
  cartDetails: [{ 'Order': 'Value' }],
  autoSelectOtp: true,
  // Android only
  merchantSMSPermission: true,
  showCbToolbar: true,
  enableSavedCard: true,
};
```

| Setting                                | Type    | Description                                                               |
| -------------------------------------- | ------- | ------------------------------------------------------------------------- |
| `primaryColor`                         | String  | Primary colour of the checkout screen.                                    |
| `secondaryColor`                       | String  | Secondary colour of the checkout screen.                                  |
| `merchantName`                         | String  | Your business name, shown on the checkout screen.                         |
| `merchantLogo`                         | String  | Your logo, shown on the checkout screen.                                  |
| `showExitConfirmationOnCheckoutScreen` | Boolean | Shows a confirmation when the customer tries to exit the checkout screen. |
| `showExitConfirmationOnPaymentScreen`  | Boolean | Shows a confirmation when the customer tries to exit the payment screen.  |
| `cartDetails`                          | Array   | Key–value pairs of order details shown to the customer.                   |
| `autoSelectOtp`                        | Boolean | Automatically selects the OTP option.                                     |
| `merchantSMSPermission`                | Boolean | **Android only.** Requests SMS permission for reading OTPs.               |
| `showCbToolbar`                        | Boolean | **Android only.** Shows the toolbar on the bank page.                     |
| `enableSavedCard`                      | Boolean | **Android only.** Enables saved cards. Requires `userCredential`.         |

## Step 5: Generate the hash on your server

PayU uses a hash to validate each payment request. When the plugin needs a hash, it emits a `generateHash` event with a `hashString` and a `hashName`.

1. Listen for the `generateHash` event.
2. Send `hashString` to your server.
3. On your server, append your salt to `hashString` and generate a **SHA-512** hash.
4. Return the hash to the plugin with `PayUCheckoutProCapacitor.hashGenerated()`, keyed by `hashName`.

<Callout icon="❗️" theme="error">
  ### Keep your salt on your server

  Never store your merchant salt in the app. Anyone who has your salt can create valid payment requests.
</Callout>

### App code

```typescript
import { Plugins } from '@capacitor/core';

private generateHashListener: any;

this.generateHashListener = Plugins['PayUCheckoutProCapacitor']['addListener']('generateHash', async (data: any) => {
  if (data != null) {
    try {
      const hashString: string = data.hashString;
      const hashName: string = data.hashName;

      // Ask your server to generate the hash
      const res = await fetch('<redacted URL>', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ hashString }),
      });
      const { hash: encodedHash } = await res.json();

      const hash = { [hashName]: encodedHash };
      PayUCheckoutProCapacitor.hashGenerated({ hashData: JSON.stringify(hash) });
    } catch (error) {
      console.error('Error generating hash:', error);
    }
  }
});
```

### Server code (Node.js)

```javascript
const crypto = require('crypto');
const express = require('express');
const app = express();
app.use(express.json());

const MERCHANT_SALT = process.env.PAYU_SALT; // Stored securely on the server

app.post('/payu/hash', (req, res) => {
  const { hashString } = req.body;
  const hash = crypto
    .createHash('sha512')
    .update(hashString + MERCHANT_SALT)
    .digest('hex');
  res.json({ hash });
});

app.listen(3000);
```

## Step 6: Launch the checkout screen

Combine the payment parameters and checkout configuration, then open the checkout screen:

```typescript
const payuParams = {
  payUPaymentParams,
  payUCheckoutProConfig,
};

PayUCheckoutProCapacitor.openCheckoutScreen({ params: JSON.stringify(payuParams) });
```

## Step 7: Handle the payment result

The plugin emits an event when the payment succeeds, fails, is cancelled or hits an error. Add a listener for each.

| Event              | When it fires                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| `generateHash`     | The plugin needs a hash for the request. See [Step 5](#step-5-generate-the-hash-on-your-server). |
| `onPaymentSuccess` | The payment succeeded.                                                                           |
| `onPaymentFailure` | The payment failed.                                                                              |
| `onPaymentCancel`  | The customer cancelled the payment.                                                              |
| `onError`          | An error occurred.                                                                               |

```typescript
private onPayUSuccessListener: any;
private onPayUCancelListener: any;
private onPayUFailureListener: any;
private onPayUErrorListener: any;

this.onPayUSuccessListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentSuccess', (data: any) => {
  // Payment succeeded. Confirm the status on your server before fulfilling the order.
});

this.onPayUCancelListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentCancel', (data: any) => {
  // Customer cancelled the payment.
});

this.onPayUFailureListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onPaymentFailure', (data: any) => {
  // Payment failed. Let the customer retry.
});

this.onPayUErrorListener = Plugins['PayUCheckoutProCapacitor']['addListener']('onError', (data: any) => {
  // Handle the error.
});
```

<Callout icon="📘" theme="info">
  ### Remove listeners

  Remove the listeners when the page is destroyed to avoid duplicate callbacks, for example `this.onPayUSuccessListener.remove()`.
</Callout>

***

## Test the integration

1. Set `environment` to the test value.
2. Use your test merchant key and salt.
3. Use the test success and failure URLs: `https://cbjs.payu.in/sdk/success` and `https://cbjs.payu.in/sdk/failure`.
4. Run a payment and confirm that your app receives the `generateHash` event, your server returns a valid hash, and the success, failure and cancel events fire as expected.

## Go-live checklist

- [ ] `environment` is set to the production value.
- [ ] Production merchant key is used, and the production salt is stored only on your server.
- [ ] Test success and failure URLs are replaced with your own URLs.
- [ ] Hash is generated on your server, not in the app.
- [ ] `transactionId` is unique for every payment.
- [ ] `userCredential` is passed if you use saved cards.
- [ ] `userToken` is passed if you use offers.
- [ ] All p