---
title: Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
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

- **user name:** payu
- **password**: payu
- **OTP**: 123456

### Test VPA for UPI

> ❗️ Callout
> 
> The UPI in-app and UPI intent flow is not available in the Test mode.

You can use either of the following VPAs to test your UPI-related integration:

- [anything@upi](anything@upi)
- [9999999999@upi](mailto:9999999999@upi)

For Testing the UPI Collect flow, Please follow the below steps:-

1. Once you enter the VPA click on the verify button and proceed to pay.
2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

\<https://pgsim01.payu.in/UPI-test-transaction/confirm/> `<Txn_id>`

#### For Android

You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

> 🚧 Ensure to remove the code from the manifest file before going live.

```xml
<application>
<meta-data android:name="payu_debug_mode_enabled" android:value="true" /> <!-- set the value to false for production environment -->
<meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> <!-- Comment in case of Production -->
<meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> <!-- Comment in case of Production -->
</application>
```

### Test cards for EMI

You can use the following Debit and Credit cards to test Emi integration.

|              |                                                                                                                                                                                              |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kotak DC EMI | 1. **Card Number**: 4706-1378-0509-9594 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI) |
| AXIS DC EMI  | 1. **Card Number**: 4011-5100-0000-0007 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI) |
| HDFC CC EMI  | 1. **Card Number**: 4453-3410-65876437 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)  |
| ICICI CC EMI | 1. **Card Number**: 4453-3410-65876437 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)  |

### Test wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Wallet</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Mobile Number</th>
  <th style="border: 1px solid #ddd; padding: 8px;">OTP</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PayTM</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>7777777777</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>888888</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PhonePe</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: <a href="https://developer.phonepe.com/v1/docs/setting-up-test-account">https://developer.phonepe.com/v1/docs/setting-up-test-account</a><br>Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>NA</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>AmazonPay</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>You can test using your original Amazon account details.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>