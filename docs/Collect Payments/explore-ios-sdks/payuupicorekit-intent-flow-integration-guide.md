---
title: PayUUPICoreKit Intent Flow Integration Guide
excerpt: >-
  This document provides step-by-step instructions for integrating the
  PayUUPICore SDK into your iOS application for Intent transactions.
deprecated: false
hidden: true
metadata:
  robots: index
---
## Integration Steps

<Accordion title="1. Add SDK Dependency" icon="download">
  <Accordion title="Using CocoaPods" icon="fa-code">
    ```
    //Add the following to your Podfile:

    use_frameworks!
    pod 'PayUIndia-UPICore'
    ```

    Then run:

    ```bash
    pod install
    ```
  </Accordion>

  <Accordion title="Using Swift Package Manager - Xcode" icon="fa-apple">
    **Steps:**

    1. Go to **File → Add Package Dependencies**
    2. Enter the repository URL: `https://github.com/payu-intrepos/payu-upi-ios-sdk`
    3. Select version **11.2.1** or latest
  </Accordion>

  <Accordion title="Using Swift Package Manager - Package.swift" icon="fa-code">
    ```swift
    .package(
        name: "PayUIndia-UPIKit",
        url: "https://github.com/payu-intrepos/payu-upi-ios-sdk",
        from: "11.2.1"
    )
    ```
  </Accordion>
</Accordion>

<Accordion title="2. Configure Supported UPI Apps" icon="fa-mobile">
  ```xml
  <!-- Add the following schemes to your Info.plist to allow the SDK to detect installed UPI apps -->

  <key>LSApplicationQueriesSchemes</key>
  <array>
      <string>tez</string>
      <string>phonepe</string>
      <string>paytm</string>
      <string>paytmmp</string>
      <string>bhim</string>
      <string>credpay</string>
      <string>mobikwik</string>
      <string>navipay</string>
      <string>super</string>
      <string>popclubapp</string>
      <string>amazonpay</string>
      <string>myairtel</string>
      <string>payzapp</string>
      <string>upi</string>
      <string>freecharge</string>
      <string>in.fampay.app</string>
      <string>kiwi</string>
      <string>jupiter</string>
      <string>omnicard</string>
      <string>slice-upi</string>
      <string>imobile</string>
      <string>icici</string>   
      <string>axismobile</string> 
      <string>yono</string>
      <string>slicepay</string>
      <string>indusmobile</string>
      <string>shriramone</string>
      <string>bobupi</string>
      <string>indusmobile</string>
      <string>whatsapp</string>
      <string>kmb</string>  
      <string>fi</string>   
      <string>idfcfirstbank</string>
  </array>
  ```

  **Note:** These schemes allow the SDK to detect installed UPI apps on the user's device. Some schemes may not be actively used but are included for compatibility and future updates.
</Accordion>

<Accordion title="3. Initialize SDK" icon="fa-gear">
  ```swift
  // Initialize the SDK before starting the payment

  PayUUPICore.shared.environment = .production // or .test
  PayUUPICore.shared.logLevel = .error // .verbose for debugging
  ```
</Accordion>

<Accordion title="4. Fetch Installed UPI Apps" icon="fa-list">
  ```swift
  // Fetch supported apps installed on the device

  let handler = PayUUPIHybridIntentHandler()
  let supportedApps = handler.getSupportedIntentApps(isForSI: <BOOL>) 
  // returns array of PayUSupportedIntentApp
  ```

  **Each app object contains:**

  * `app.name`
  * `app.scheme`

  **Display apps in your UI:**

  * Google Pay
  * PhonePe
  * Paytm
  * BHIM
  * Amazon Pay

  **After user selection:**

  ```swift
  let selectedApp = <USER_SELECTED_APP> // PayUSupportedIntentApp
  ```
</Accordion>

<Accordion title="5. Start UPI Payment" icon="fa-credit-card">
  ```swift
  func startUPIPayment(from viewController: UIViewController, selectedApp: PayUUPIApp) {
      PayUUPICore.shared.paymentCompletion = { response in
          // Handle payment response
          // Remove loader or dismiss presented screen
          self.dismiss(animated: true)
      }
      
      let handler = PayUUPIHybridIntentHandler()
      let paymentParams = createPaymentParams()
      
      handler.initiateIntentPayment(
          withApp: selectedApp,
          paymentParams: paymentParams,
          fromVC: viewController
      )
  }
  ```
</Accordion>

<Accordion title="6. Create Payment Parameters" icon="fa-code">
  ```swift
  func createPaymentParams() -> PayUPaymentParam {
      let paymentParam = PayUPaymentParam(
          key: "<MERCHANT_KEY>",
          transactionId: "<TRANSACTION_ID>",
          amount: "<AMOUNT>",
          productInfo: "<PRODUCT_INFO>",
          firstName: "<CUSTOMER_NAME>",
          email: "<CUSTOMER_EMAIL>",
          phone: "<CUSTOMER_PHONE>",
          surl: "<SUCCESS_URL>",
          furl: "<FAILURE_URL>",
          environment: .production
      )
      
      paymentParam.additionalParam[PaymentParamConstant.udf1] = "<UDF1>"
      paymentParam.additionalParam[PaymentParamConstant.udf2] = "<UDF2>"
      paymentParam.additionalParam[PaymentParamConstant.udf3] = "<UDF3>"
      paymentParam.additionalParam[PaymentParamConstant.udf4] = "<UDF4>"
      paymentParam.additionalParam[PaymentParamConstant.udf5] = "<UDF5>"
      
      paymentParam.hashes = generateHashes(for: paymentParam)
      
      return paymentParam
  }
  ```
</Accordion>

<Accordion title="7. Recurring (SI) Payment Parameters (Optional)" icon="fa-repeat">
  ```swift
  // For UPI Autopay / Subscription payments

  let siParams = PayUSIParams(
      billingAmount: "<BILLING_AMOUNT>",
      paymentStartDate: "<START_DATE>", // "dd/MM/yyyy"
      paymentEndDate: "<END_DATE>", // "dd/MM/yyyy"
      billingCycle: "<BILLING_CYCLE>", // once or daily or weekly or monthly or yearly or adhoc
      billingInterval: NSNumber(value: <BILLING_INTERVAL>)
  )

  siParams.remarks = "<REMARKS>"
  siParams.isFreeTrial = "<BOOL>"
  siParams.billingLimit = "<BILLING_LIMIT>" // "ON"
  siParams.billingRule = "<BILLING_RULE>" // "MAX"
  siParams.billingDate = "<BILLING_DATE>"

  paymentParam.siParam = siParams
  ```

  **Note:** Refer to PayU documentation for valid values of:

  * `billingCycle`
  * `billingInterval`
  * `billingLimit`
  * `billingRule`
</Accordion>

<Accordion title="8. TPV Payment Parameters (Optional)" icon="fa-bank">
  ```swift
  // For UPI TPV payments

  let beneficiary = PayUBeneficiaryParams(
      beneficiaryName: "<BENEFICIARY_NAME>",
      beneficiaryAccountNumber: "<ACCOUNT_NUMBER>",
      beneficiaryIFSC: "<IFSC_CODE>",
      beneficiaryAccountType: <ACCOUNT_TYPE>, // .savings or .current
      verficationMode: <VERIFICATION_MODE> // Optional – debitCard or netBanking or aadhaar
  )

  paymentParam.payuBeneficieryDetails = [beneficiary]
  ```

  **Note:** Refer to PayU documentation for valid values of:

  * `beneficiaryAccountType`
  * `verficationMode`
</Accordion>

<Accordion title="9. Hash Generation" icon="fa-lock">
  **⚠️ Important:** Hash must be generated on the backend using your merchant salt.

  <Accordion title="Normal Transaction Hash" icon="fa-hashtag">
    ```
    sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
    ```
  </Accordion>

  <Accordion title="SI Transaction Hash" icon="fa-repeat">
    For subscription payments, `siDetails` must be included.

    ```
    SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||siDetails|salt)
    ```

    **SI Details JSON String:**

    ```json
    "{\"billingAmount\":\"<BILLING_AMOUNT>\",\"billingCurrency\":\"<CURRENCY>\",\"billingCycle\":\"<BILLING_CYCLE>\",\"billingInterval\":\"<BILLING_INTERVAL>\",\"paymentStartDate\":\"<PAYMENT_START_DATE>\",\"paymentEndDate\":\"<PAYMENT_END_DATE>\",\"billingLimit\":\"<BILLING_LIMIT>\",\"billingRule\":\"<BILLING_RULE>\"}"
    ```
  </Accordion>

  <Accordion title="TPV Transaction Hash" icon="fa-bank">
    For TPV payments, `tpvDetails` must be included.

    ```
    sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||tpvDetails|salt)
    ```

    **TPV Details JSON String:**

    ```json
    "{\"beneficiaryAccountNumber\":\"<BENEFICIARY_ACC_NUM>\",\"ifscCode\":\"<IFSC>\"}"
    ```
  </Accordion>

  <Accordion title="TPV-SI Transaction Hash" icon="fa-key">
    For TPV-SI payments, both `tpvDetails` and `siDetails` must be included.

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||tpvDetails|siDetails|salt
    ```
  </Accordion>

  **Note:** The SI and TPV details must exactly match the values provided in the payment request, without any added spaces or line breaks.
</Accordion>

<Accordion title="10. Payment Response" icon="fa-check-circle">
  ```swift
  // Payment result is returned through:

  PayUUPICore.shared.paymentCompletion
  ```

  **Use this callback to:**

  * Handle success / failure
  * Dismiss loaders
  * Update UI
  * Verify transaction from backend
</Accordion>

## Supported Intent Apps

| APPs       | Intent    | Mandate       |
| ---------- | --------- | ------------- |
| gpay       | Supported | Supported     |
| phonepe    | Supported | Supported     |
| paytm      | Supported | Supported     |
| bhim       | Supported | Supported     |
| cred       | Supported | Not Supported |
| amazonPay  | Supported | Not Supported |
| navi       | Supported | Supported     |
| popclub    | Supported | Not Supported |
| mobikwik   | Supported | Not Supported |
| superMoney | Supported | Supported     |
| airtel     | Supported | Not Supported |
| payzapp    | Supported | Not Supported |
| freecharge | Supported | Supported     |

## Additional Resources

For Collect transactions, and for complete details on integration steps and parameter definitions, please refer to the official documentation:

**[PayU iOS UPI SDK Documentation](https://devguide.payu.in/)**
