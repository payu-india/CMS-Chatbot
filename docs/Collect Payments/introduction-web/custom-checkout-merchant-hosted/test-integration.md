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
---
title: Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Test PayU merchant-hosted checkout: sandbox credentials, test cards/UPI/wallets, verify transactions, hash checks, and pre-production checklist.
  keywords:
    - payu merchant hosted checkout test integration sandbox
    - test payment integration custom checkout payu web india
    - payment gateway test credentials merchant hosted payu guide
    - payu test cards upi wallets merchant hosted integration web
    - website payment test integration payu custom checkout sandbox
    - merchant hosted checkout test transaction payu integration steps
    - payu collect payments test integration merchant hosted web guide
    - test payment integration sandbox go live checklist payu web
    - payu custom checkout test environment integration developer
    - payment gateway test mode merchant hosted integration payu india
    - payu merchant hosted integration testing before production go live
    - test payu payment api merchant hosted checkout website integration
  robots: index

next:
  description: ''
---
After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<Callout icon="🚧" theme="warn">
  **Use only Test Key and Salt:** You must only use the Test merchant Key and Test Salt to carry out a test transaction.
</Callout>

***

<TestKeyAndSaltProcedure />

## Configure setIsProduction()

Set the value of the `setIsProduction()` to false in the payment integration code. This enables the integration to accept live payments.

***

## Test credentials

Following are the payment methods supported in PayU Test mode.

### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

* **user name:** payu
* **password**: payu
* **OTP**: 123456

### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

* anything@payu
* [9999999999@payu.in](mailto:9999999999@payu.in)

> ❗️ Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

### Test cards for EMI

You can use the following Debit and Credit cards to test Emi integration.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Kotak DC EMI
      </td>

      <td>
        1. **Card Number**: 4706-1378-0509-9594 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        AXIS DC EMI
      </td>

      <td>
        1. **Card Number**: 4011-5100-0000-0007 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        HDFC CC EMI
      </td>

      <td>
        1. **Card Number**: 4453-3410-65876437 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        ICICI CC EMI
      </td>

      <td>
        1. **Card Number**: 4453-3410-65876437 2. **Expiry**: any future date (mm/yy) 3. **CVV**: 123 4. **OTP**: 111111 5. **Name**: Any name 6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>
  </tbody>
</Table>

### Test Wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

{/* block:parameters */}

| Wallet    | Mobile Number                                                                                                                                                                                                                                                                                                                                                        | OTP    |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| PayTM     | 7777777777                                                                                                                                                                                                                                                                                                                                                           | 888888 |
| PhonePe   | Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: \<[https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)>  <br />Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs. | NA     |
| AmazonPay | You can test using your original Amazon account details.                                                                                                                                                                                                                                                                                                             |        |

{/* /block */}