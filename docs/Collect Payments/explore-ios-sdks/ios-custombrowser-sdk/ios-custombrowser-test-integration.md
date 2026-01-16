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

<Accordion title="Test Credentials for Net Banking" icon="fa-university">
  Use the following credentials to test the Net Banking integration:

  * **user name:** payu
  * **password**: payu
  * **OTP**: 123456
</Accordion>

<Accordion title="Test VPA for UPI" icon="fa-mobile">
  You can use either of the following VPAs to test your UPI-related integration:

  * [anything@payu](anything@payu)
  * [9999999999@payu.in](mailto:9999999999@payu.in)

  > ❗️ Callout
  >
  > The UPI in-app and UPI intent flow is not available in the Test mode.
</Accordion>

<Accordion title="Test Cards for EMI" icon="fa-credit-card">
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
          1. **Card Number**: 4706-1378-0509-9594  
          2. **Expiry**: any future date (mm/yy)  
          3. **CVV**: 123  
          4. **OTP**: 111111  
          5. **Name**: Any name  
          6. **Mobile Number**: 9123412345 (mandatory for EMI)
        </td>
      </tr>

      <tr>
        <td>
          AXIS DC EMI
        </td>

        <td>
          1. **Card Number**: 4011-5100-0000-0007  
          2. **Expiry**: any future date (mm/yy)  
          3. **CVV**: 123  
          4. **OTP**: 111111  
          5. **Name**: Any name  
          6. **Mobile Number**: 9123412345 (mandatory for EMI)
        </td>
      </tr>

      <tr>
        <td>
          HDFC CC EMI
        </td>

        <td>
          1. **Card Number**: 4453-3410-65876437  
          2. **Expiry**: any future date (mm/yy)  
          3. **CVV**: 123  
          4. **OTP**: 111111  
          5. **Name**: Any name  
          6. **Mobile Number**: 9123412345 (mandatory for EMI)
        </td>
      </tr>

      <tr>
        <td>
          ICICI CC EMI
        </td>

        <td>
          1. **Card Number**: 4453-3410-65876437  
          2. **Expiry**: any future date (mm/yy)  
          3. **CVV**: 123  
          4. **OTP**: 111111  
          5. **Name**: Any name  
          6. **Mobile Number**: 9123412345 (mandatory for EMI)
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

<Accordion title="Test Wallets" icon="fa-wallet">
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
          Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)\
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
</Accordion>
