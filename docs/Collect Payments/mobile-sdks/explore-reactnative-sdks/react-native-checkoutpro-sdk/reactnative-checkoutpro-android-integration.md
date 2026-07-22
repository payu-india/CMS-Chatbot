---
title: Android Integration
deprecated: false
hidden: false
metadata:
  title: React Native Checkout Pro SDK for Android Integration
  description: >-
    This document provides a step-by-step guide on integrating React Native
    Checkout Pro mobile SDK for Android, including setting up payment hashes,
    building payment parameters, initiating payments, handling payment
    completion, and customization options.
  keywords:
    - React Native with Android Checkout Pro SDK Integration Steps
    - PayU React Native with Android SDK integration steps
    - Mobile payment integration with PayU React Native with Android SDK steps
    - PayU React Native with Android Checkout Pro set up for Mobile
    - React Native with Android CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile React Native with Android SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
---
title: Android Integration
deprecated: false
hidden: false
metadata:
  title: React Native Checkout Pro SDK for Android Integration
  description: >-
    PayU CheckoutPro React Native on Android: native module linking, Gradle config, hash, payment flow, and Android-specific setup.
  robots: index
  keywords:
    - payu react native checkoutpro android integration steps
    - react native payment gateway sdk android integration payu
    - integrate checkoutpro react native android app payu india
    - react native android payment sdk integration guide payu
    - mobile payment sdk react native android checkoutpro payu
    - payu react native checkout pro android gradle integration
    - payment gateway react native android sdk integration payu
    - react native checkoutpro android hash callback integration
    - payu react native android test sandbox integration guide
    - react native in app payment android sdk payu checkoutpro
    - android react native payment gateway integration india payu
    - react native checkoutpro android ios integration payu sdk

next:
  description: ''
---
This section describes how to integrate React Native with Android Checkout Pro SDK.

## 🔴 IMPORTANT NOTICE - React Native 0.82.0+ Users

<Callout icon="❗️" theme="error">
  **Breaking Change for React Native 0.82.0 and Above**

  If you are using **React Native version 0.82.0 or above**, or planning to upgrade your SDK, you **MUST** use the new `makeHttpRequest` method for hash generation.

  The traditional `fetch` or other HTTP methods will **NOT work** with React Native 0.82.0+.
</Callout>

<Accordion title="New Hash Generation Method (React Native >= 0.82.0)" icon="fa-exclamation-triangle">
  For React Native version **0.82.0 and above**, you must use the `PayUBizSdk.makeHttpRequest` method inside the `generateHash` callback:

  ```javascript React Native
  generateHash = async (e) => {
      var hashStringWithoutSalt = e.hashString;
      var hashName = e.hashName;
      var postSalt = e.postSalt;  // Compulsory for Additional Charges and Split Payment
      
      try {
          // Prepare request body
          const rawBody = JSON.stringify({
              hashString: hashStringWithoutSalt,
              postSalt: postSalt
          });
          
          // Prepare headers
          const headers = {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer YOUR_API_TOKEN'  // If required
          };
          
          // NEW METHOD - Use PayUBizSdk.makeHttpRequest
          var response = await PayUBizSdk.makeHttpRequest(
              "https://yourserver.com/generate-hash",  // API URL
              "POST",                                    // Method Type
              rawBody,                                   // Body
              headers                                    // Headers
          );
          
          console.log('Raw Response:', response);
          
          // Parse the JSON response
          const parsedResponse = typeof response === 'string' 
              ? JSON.parse(response) 
              : response;
          
          var hashValue = parsedResponse.hash;
          var result = { [hashName]: hashValue };
          
          // Return hash to SDK
          PayUBizSdk.hashGenerated(result);
          
      } catch (error) {
          console.error('Hash generation error:', error);
      }
  };
  ```

  <Callout icon="📘" theme="info">
    **For React Native versions below 0.82.0**, you can continue using the standard `fetch` approach. See detailed implementation in Step 5 below.
  </Callout>
</Accordion>

<Callout icon="👍" theme="success">
  **Why This Change?**

  * Required for compatibility with React Native 0.82.0+
  * Ensures network requests work correctly in newer React Native versions
</Callout>

***

## SDK Integration

To integrate with the CheckoutPro mobile SDK for Android:

<Accordion title="Step 1: Include the SDK in your app project" icon="fa-code">
  The CheckoutPro SDK is offered through npm.

  Add the following entries to include CheckoutPro SDK in your app:

  <Accordion title="Install the SDK" icon="fa-code">
    ```
    npm install payu-non-seam-less-react --save
    react-native link payu-non-seam-less-react
    ```
  </Accordion>

  <Accordion title="Import the SDK in your payment component" icon="fa-code">
    Add the following imports in the class where you need to initiate a payment:

    ```Text React
    import PayUBizSdk from 'payu-non-seam-less-react';
    ```
  </Accordion>

  <Accordion title="Update Root build.gradle" icon="fa-code">
    Add the repository details for SDK dependencies under `allprojects` in `android/build.gradle`::

    ```
    allprojects {
      repositories {
        maven {
        url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android"
        }
      }
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 2: Build the payment parameters" icon="fa-code">
  To initiate a payment, your app needs to send transactional information to the Checkout Pro SDK.

  <Accordion title="Step 2.1: Basic Integration" icon="fa-code">
    ```javascript
    import {NativeModules} from 'react-native';
    const {PayUBizSdk} = NativeModules;

    const createBasicPaymentParams = () => {
      const txnid = new Date().getTime().toString();
      
      const payUPaymentParams = {
        key: 'YOUR_MERCHANT_KEY',
        transactionId: txnid,
        amount: '10',
        productInfo: 'Macbook Pro',
        firstName: 'Abc',
        email: 'test@gmail.com',
        phone: '9999999999',
        // Redirect URLs
        android_surl: 'https://cbjs.payu.in/sdk/success',
        android_furl: 'https://cbjs.payu.in/sdk/failure',
        ios_surl: 'https://cbjs.payu.in/sdk/success',
        ios_furl: 'https://cbjs.payu.in/sdk/failure',
        // Environment: '0' => Production, '1' => Test
        environment: '1',
        // User credentials for saved cards
        userCredential: 'YOUR_MERCHANT_KEY:user@email.com',
        // User token for offer engine
        userToken: 'userId:userName',
        // Additional parameters
        additionalParam: {
          udf1: 'udf1',
          udf2: 'udf2',
          udf3: 'udf3',
          udf4: 'udf4',
          udf5: 'udf5',
					sourceId: "<sourceId>",
          walletUrn: "<walletUrn>"
        },
      };
      return payUPaymentParams;
    };
    ```

    > **📘 Important:**
    >
    > * The sample SURL/FURL values are for testing only. Use your own URLs before going live.
    > * The `transactionId` must be unique, ≤ 25 characters, and cannot contain special characters like `_`, `$`, `%`, `&`, etc.
    > * For more information, refer to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).

    ***
  </Accordion>

  <Accordion title="Step 2.2: For Recurring Payments (SI) - Optional" icon="fa-code">
    For Standing Instructions / subscription payments, build the `payUSIParams` object.

    ```javascript

      // SI Parameters
      const payUSIParams = {
        isFreeTrial: false,
        billingAmount: '3000',
        billingCycle: 'MONTHLY', // DAILY/WEEKLY/MONTHLY/YEARLY/ADHOC/ONCE
        billingCurrency: 'INR',
        billingInterval: '10',
        paymentStartDate: '2027-05-06', // YYYY-MM-DD
        paymentEndDate: '2028-05-10',   // YYYY-MM-DD
        remarks: 'Subscription payment',
        billingDate: '', // Optional
      };
      
      const payUPaymentParams = {
        // Add SI Parameters
        payUSIParams: payUSIParams,
      };

    ```

    **SI Parameters Reference:**

    | Parameter          | Type    | Description                         | Example                                                 |
    | ------------------ | ------- | ----------------------------------- | ------------------------------------------------------- |
    | `isFreeTrial`      | Boolean | Whether this is a free trial period | `true` / `false`                                        |
    | `billingAmount`    | String  | Amount to be charged                | `"3000"`                                                |
    | `billingCycle`     | String  | Billing frequency                   | `MONTHLY`, `DAILY`, `WEEKLY`, `YEARLY`, `ADHOC`, `ONCE` |
    | `billingInterval`  | String  | Interval between charges            | `"10"`                                                  |
    | `paymentStartDate` | String  | Start date (YYYY-MM-DD)             | `"2027-05-06"`                                          |
    | `paymentEndDate`   | String  | End date (YYYY-MM-DD)               | `"2028-05-10"`                                          |
    | `remarks`          | String  | Additional notes                    | `"Subscription"`                                        |
    | `billingCurrency`  | String  | Currency code                       | `"INR"`                                                 |
    | `billingDate`      | String  | Specific billing date (optional)    | `""`                                                    |

    For more details, refer to [PayU Standing Instructions Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).

    ***
  </Accordion>

  <Accordion title="Step 2.3: For UPI One Time Mandate Payments - Optional" icon="fa-code">
    For UPI OTM, enable pre-auth and provide mandate dates.

    ```javascript

      // OTM Parameters
      const payUSIParams = {
        isPreAuthTxn: true, // Mandatory for UPI OTM
        paymentStartDate: '2025-04-01', // YYYY-MM-DD
        paymentEndDate: '2025-04-10',   // YYYY-MM-DD
      };
      
      const payUPaymentParams = {
        // Add OTM Parameters
        payUSIParams: payUSIParams,
      };
      

    ```

    ***
  </Accordion>

  <Accordion title="Step 2.4: For Additional Charges - Optional" icon="fa-code">
    Add additional charges or percentage-based charges for specific payment methods.

    ```javascript
    const payUPaymentParams = {
      // ... other parameters
      
      // Fixed additional charges
      additionalCharges: 'CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55',
      
      // Percentage-based additional charges
      percentageAdditionalCharges: 'CC:50,AMEX:100,DINR:75,DC:25',
    };
    ```

    **Format:**

    * `PaymentMode:Amount` separated by commas
    * Payment modes: `CC` (Credit Card), `DC` (Debit Card), `NB` (Net Banking), `UPI`, `WALLET`, `EMI`, `BNPL`
    * Or use specific bank codes like `SBIB` (State Bank), `AMEX`, etc.

    For more information, refer to [Collect Additional Charges](https://docs.payu.in/docs/collect-additional-charges).

    ***
  </Accordion>

  <Accordion title="Step 2.5: For Split Payments Details - Optional" icon="fa-code">
    For split payments (aggregator model), create a JSON object and pass it as a string.

    ```javascript
      // Split payment configuration
      const splitPaymentDetails = {
        type: 'absolute', // or 'percentage'
        splitInfo: {
          'imAJ7I': { // Child Merchant Key
            aggregatorSubTxnId: '12345673443540dd33d099887766650091', // Unique per transaction
            aggregatorSubAmt: '10',
            aggregatorCharges: '0',
          },
        },
      };
      
      const payUPaymentParams = {
        // Add split payment details as JSON string
        splitPaymentDetails: JSON.stringify(splitPaymentDetails),
      };
      
    ```

    **Important:**

    * `aggregatorSubTxnId` must be unique for each transaction
    * `type` can be `'absolute'` or `'percentage'`
    * Multiple child merchants can be added to `splitInfo`

    ***
  </Accordion>

  <Accordion title="Step 2.6: SKU Details - Optional" icon="fa-code">
    Pass item-level details for cart-based transactions.

    ```javascript

      // SKU Details
      const skuDetails = {
        skus: [
          {
            skuId: '111',
            skuName: 'Shoes',
            skuAmount: '100',
            quantity: 1,
            offerKeys: null,
          },
          {
            skuId: '222',
            skuName: 'Shirt',
            skuAmount: '100',
            quantity: 1,
            offerKeys: null,
          },
        ],
      };
      
      const payUPaymentParams = {
        // Add SKU details
        skuDetails: skuDetails,
      };
      

    ```

    > **🚧 Keep in mind:**
    >
    > * The total `amount` must equal the sum of `(quantity × skuAmount)` for all items
    > * If passing SKU-specific offers, use the `offerKeys` field

    ***
  </Accordion>

  <Accordion title="Step 2.7: Third Party Verification (TPV) Flow - Optional" icon="fa-code">
    For TPV transactions, pass beneficiary account details for verification.

    ```javascript

      // TPV Beneficiary Details
      const beneficiaryDetails = [
        // For UPI
        {
          beneficiaryAccount: '002001600674',
          beneficiaryIfsc: 'HDFC0000090',
        },
        // For Net Banking
        {
          beneficiaryName: 'SACHIN Tendulkar',
          beneficiaryAccount: '002001600674',
          beneficiaryIfsc: 'ICIC0000090',
          beneficiaryAccountType: 'SAVINGS',
        },
      ];
      
      const payUPaymentParams = {   
        // Add TPV beneficiary details
        beneficiaryDetails: beneficiaryDetails,
      };

    ```

    **TPV Parameters:**

    | Parameter                | Required For | Description                |
    | ------------------------ | ------------ | -------------------------- |
    | `beneficiaryAccount`     | All          | Beneficiary account number |
    | `beneficiaryIfsc`        | All          | Bank IFSC code             |
    | `beneficiaryName`        | Net Banking  | Account holder name        |
    | `beneficiaryAccountType` | Net Banking  | `SAVINGS` or `CURRENT`     |

    ***
  </Accordion>

  <Accordion title="Step 2.8: Cross Border Flow (OPGSP) - Optional" icon="fa-code">
    For OPGSP merchants, complete address details are mandatory. UDF5 (invoice number) is also required.

    ```javascript

      // Address Details (Mandatory for OPGSP)
      const address = {
        lastName: 'LastName',
        address1: 'Address1 value',
        address2: 'Address2 value',
        city: 'Gurgaon',
        state: 'Haryana',
        country: 'India',
        zipcode: '122001',
      };
      
      // Additional Param with UDF5 (Invoice Number - Mandatory for OPGSP)
      const additionalParam = {
        udf1: 'udf1',
        udf2: 'udf2',
        udf3: 'udf3',
        udf4: 'udf4',
        udf5: 'Sample_Invoice_11', // Mandatory for OPGSP
      };
      
      const payUPaymentParams = {
        // Add address details
        address: address,
        // Add additional params with UDF5, pass invoice number
        additionalParam: additionalParam,
      };

    ```

    > **Important:** For OPGSP merchants, both `address` and `udf5` (invoice number) are mandatory.

    For more details: [Cross-Border Payments (Import)](https://docs.payu.in/docs/introduction-cross-border-payments-import)

    ***
  </Accordion>

  <Accordion title="Step 2.9: WealthTech Flow - Optional" icon="fa-code">
    For investment and mutual fund transactions.

    ```javascript
      // WealthTech Product Details
      const products = [
        {
          type: 'mutual_fund',
          plan: 'GD',
          folio: '9104927822',
          amount: '50000',
          option: 'G',
          scheme: 'LT',
          receipt: '77407',
          mfMemberID: '123445',
          mfUserID: '77407',
          mfPartner: 'cams',
          mfInvestmentType: 'L',
          mfAMCCode: 'UTB',
        },
      ];
      
      const payUPaymentParams = {
        // Add WealthTech products
        products: products,
      };

    ```

    ***
  </Accordion>

  <Accordion title="Step 2.10: Enforce Offer Keys" icon="fa-code">
    Apply specific promotional offers during checkout.

    ```javascript
    const payUPaymentParams = {
      // ... other parameters
      
      // Comma-separated offer keys
      enforcementOfferKeys: ['offer_key_1', 'offer_key_2'],
    };

    // Or as a comma-separated string (if parsing on your side)
    // enforcementOfferKeys: 'HoliSale@JbBdLOBritj5,Instantoffer@Kp78nFDENX5S'
    ```

    ***
  </Accordion>

  <Accordion title="Step 2.11: Additional Parameters - Optional" icon="fa-code">
    The additional parameters that are optional that can be passed to SDK are udf parameters, static hashes, and other parameters. For more details on Static Hash generation and passing them, refer to [generate hashes](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk). The following is a list of parameters that can be passed in additional parameters:

    | Parameter                                   | Description                                                                                                                                                                         |
    | :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | udf1           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | udf2           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | udf3           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | udf4           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | udf5           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | sourceId | `String` Sodexo Source ID, Merchant can store it from the third field of PayU response.                                                                                             |
    | walletUrn              | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account.                                                                                  |
  </Accordion>

  <Accordion title="Steps 2.12: Payment Param Definitions" icon="fa-code">
    <Table align={["left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Parameter
          </th>

          <th style={{ textAlign: "left" }}>
            Description
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            Key
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` This parameter must contain your merchant key received from PayU.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            transactionId
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` It should be unique for each transaction.
            Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "\_,$,%,&, etc"
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Amount
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Total transaction amount.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            productInfo
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Information about the product.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            firstName
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer's first name
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Email
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer's email id
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Phone
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Customer's phone number. **Max character limit** : 10 Digits
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ios\_surl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for iOS integration
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            ios\_furl
            mandatory
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction fails, PayU will load this URL and pass the transaction response.

            * *Note*\*: This field is applicable for iOS integration
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            android\_surl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction gets successful, PayU will load this URL and pass the transaction response.
            `Note`: This field is applicable for Android integration

            * *Sample URL*\*: [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            android\_furl
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` When the transaction gets fail, PayU will load this url and pass transaction response.
            When the transaction gets success, PayU will load this url and pass transaction response.
            `Note`: This field is applicable for Android integration

            * *Sample URL*\*: [https://cbjs.payu.in/sdk/failure](https://cbjs.payu.in/sdk/failure)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Environment
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Environment of SDK
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            User Credential
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            * *String*\* This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:
              `<merchantKey>:<userId>  `
              Here,
              UserId is any id/email/phone number to uniquely identify the user.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            user\_token
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            String The use for this param is to allow the offer engine to apply velocity rules at a user level.

            -\*\*Card Based Offers (CC, DC, EMI):\*\*For card payment mode offers, if this parameter is passed then the velocity rules would be applied on this token, if not passed the same would be applied to the card number.

            -**NB, Wallet:** It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
            Note:- When we use Offer features then it's a mandatory parameter otherwise it's not required.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            additionalCharges
          </td>

          <td style={{ textAlign: "left" }}>
            String
            This parameter is required if merchant want to take additional charge from user,	should be string with PG:Amount or IBIBOCode:Amount
            Sample : CC:10,NB:20,SBIB:15
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            percentageAdditionalCharges
          </td>

          <td style={{ textAlign: "left" }}>
            String
            This parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable,
            should be string with PG:Amount or IBIBOCode:Amount
            Sample : CC:100,NB:50,SBIB:25
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            SkuDetails
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            Create list of SKU as per products added in cart and add this list in SKU details. and set sku detials to PayUPaymentParams.

            * \*Note:- \*\*When we use SKU features then it's a mandatory parameter otherwise it's not required.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            payUSIParams
            `conditional`
          </td>

          <td style={{ textAlign: "left" }}>
            `Object` Contains SI/mandate details for recurring payments.

            **Mandatory for Recurring (Subscription / Standing Instruction) transactions.**

            For more details: [Recurring Payments Integration](https://docs.payu.in/docs/introduction-recurring-payments-integration)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            enableNativeOTP
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `Boolean` Enable native OTP flow for card transactions. When set to true, OTP will be handled natively within the SDK.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            splitPaymentDetails
            `conditional`
          </td>

          <td style={{ textAlign: "left" }}>
            `String (JSON encoded)` Contains details for split payment/settlement between multiple parties.

            **Mandatory only for Aggregator transactions.**

            For more details: [Split Settlements](https://docs.payu.in/docs/split-settlments)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            enforcementOfferKeys
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `String` Comma-separated list of offer keys to enforce specific offers during checkout. Allows merchants to apply targeted promotional offers.

            * *Note*: Optional parameter for enforcing specific offer keys at checkout.
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            beneficiaryDetails
            `conditional`
          </td>

          <td style={{ textAlign: "left" }}>
            `Object/List` Contains beneficiary account details for payment verification in TPV flow.
            **Mandatory only for TPV (Third Party Verification) transactions.**
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            address / addressDetails
            `conditional`
          </td>

          <td style={{ textAlign: "left" }}>
            `Object` Contains customer's complete billing address including address lines, city, state, country, and zipcode.
            **Mandatory only for Cross-Border Payments (OPGSP) Merchant.**

            For more details: [Cross-Border Payments (Import)](https://docs.payu.in/docs/introduction-cross-border-payments-import)
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            products
            `conditional`
          </td>

          <td style={{ textAlign: "left" }}>
            `List<PayUWealthProducts>` Contains details of wealth management and investment products such as mutual funds. Each product includes information like type, amount, folio number, plan, scheme, AMC code, member ID, user ID, partner details, and investment type.

            **Mandatory only for WealthTech / Investment product transactions.**
          </td>
        </tr>
      </tbody>
    </Table>

    > 📘 Note:
    >
    > The sample URLs mentioned in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.

    For details on Standing Instructions parameters, refer to [PayU Standing Instruction Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).
  </Accordion>

  <Accordion title="Step 2.13: Complete Sample (Recommended)" icon="fa-code">
    The payment parameters and additional parameters can be passed using the following code snippet:

    ```javascript
    import React from 'react';
    import {NativeModules, Alert} from 'react-native';
    import CryptoJS from 'crypto-js';

    const {PayUBizSdk} = NativeModules;

    const createPaymentParams = () => {
      const txnid = new Date().getTime().toString();

      // ========== Basic Payment Parameters (Mandatory) ==========
      const payUPaymentParams = {
        key: 'YOUR_MERCHANT_KEY',
        transactionId: txnid,
        amount: '10',
        productInfo: 'Product Info',
        firstName: 'Abc',
        email: 'test@gmail.com',
        phone: '9999999999',
        android_surl: 'https://cbjs.payu.in/sdk/success',
        android_furl: 'https://cbjs.payu.in/sdk/failure',
        ios_surl: 'https://cbjs.payu.in/sdk/success',
        ios_furl: 'https://cbjs.payu.in/sdk/failure',
        environment: '1', // '0' => Production, '1' => Test
        userCredential: 'YOUR_MERCHANT_KEY:test@gmail.com',
        userToken: 'userId:userName',
      };

      // ========== Additional Parameters ==========
      const additionalParam = {
        udf1: 'udf1',
        udf2: 'udf2',
        udf3: 'udf3',
        udf4: 'udf4',
        udf5: 'udf5',
        walletUrn: '100000',
        sourceId: 'src_dfcbd083-f38d-4d0d-9fac-80d7d1bb8f2d',
      };
      payUPaymentParams.additionalParam = additionalParam;

      // ========== Standing Instruction (SI) - Optional ==========
      payUPaymentParams.payUSIParams = {
        isFreeTrial: false,
        billingAmount: '3000',
        billingCycle: 'MONTHLY', // DAILY/WEEKLY/MONTHLY/YEARLY/ADHOC/ONCE
        billingCurrency: 'INR',
        billingInterval: '10',
        paymentStartDate: '2027-05-06', // YYYY-MM-DD
        paymentEndDate: '2028-05-10',   // YYYY-MM-DD
        remarks: 'Subscription payment',
        billingDate: '',
      };

      // ========== One Time Mandate (OTM) - Optional ==========
      payUPaymentParams.payUSIParams = {
        isPreAuthTxn: true,
        paymentStartDate: '2025-04-01', // YYYY-MM-DD
        paymentEndDate: '2025-04-10',   // YYYY-MM-DD
      };

      // ========== SKU Details - Optional ==========
      payUPaymentParams.skuDetails = {
        skus: [
          {
            skuId: '111',
            skuName: 'Shoes',
            skuAmount: '100',
            quantity: 1,
            offerKeys: null,
          },
          {
            skuId: '222',
            skuName: 'Shirt',
            skuAmount: '100',
            quantity: 1,
            offerKeys: null,
          },
        ],
      };

      // ========== TPV (Third Party Verification) - Optional ==========
      payUPaymentParams.beneficiaryDetails = [
        // For UPI
        {
          beneficiaryAccount: '002001600674',
          beneficiaryIfsc: 'HDFC0000090',
        },
        // For Net Banking
        {
          beneficiaryName: 'SACHIN Tendulkar',
          beneficiaryAccount: '002001600674',
          beneficiaryIfsc: 'ICIC0000090',
          beneficiaryAccountType: 'SAVINGS',
        },
      ];

      // ========== OPGSP (Cross Border) - Optional ==========
      // Note: For OPGSP, udf5 (invoice number) is also mandatory
      payUPaymentParams.address = {
        lastName: 'LastName',
        address1: 'Address1 value',
        address2: 'Address2 value',
        city: 'Gurgaon',
        state: 'Haryana',
        country: 'India',
        zipcode: '122001',
      };
      additionalParam.udf5 = 'Sample_Invoice_11'; // Mandatory for OPGSP

      // ========== WealthTech - Optional ==========
      payUPaymentParams.products = [
        {
          type: 'mutual_fund',
          plan: 'GD',
          folio: '9104927822',
          amount: '50000',
          option: 'G',
          scheme: 'LT',
          receipt: '77407',
          mfMemberID: '123445',
          mfUserID: '77407',
          mfPartner: 'cams',
          mfInvestmentType: 'L',
          mfAMCCode: 'UTB',
        },
      ];

      // ========== Split Payment - Optional ==========
      const splitPaymentDetails = {
        type: 'absolute', // or 'percentage'
        splitInfo: {
          imAJ7I: { // Child Merchant Key
            aggregatorSubTxnId: '12345673443540dd33d099887766650091', // Unique per transaction
            aggregatorSubAmt: '10',
            aggregatorCharges: '0',
          },
        },
      };
      payUPaymentParams.splitPaymentDetails = JSON.stringify(splitPaymentDetails);

      // ========== Additional Charges - Optional ==========
      payUPaymentParams.additionalCharges = 'CC:12,AMEX:19,SBIB:98,DC:25,NB:55';
      payUPaymentParams.percentageAdditionalCharges = 'CC:50,AMEX:100,DC:25';

      // ========== Offer Keys - Optional ==========
      payUPaymentParams.enforcementOfferKeys = ['offer_key_1', 'offer_key_2'];

      // ========== Enable Native OTP - Optional ==========
      payUPaymentParams.enableNativeOTP = true;

      return payUPaymentParams;
    };
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Initiate the payment" icon="fa-code">
  Initialize and launch the Checkout Pro SDK by calling the following code snippet:

  ```javascript React.js
  var paymentObject = {
  payUPaymentParams: payUPaymentParams,
  // payUCheckoutProConfig is optional
  // Detail can be found in latter section
  payUCheckoutProConfig: payUCheckoutProConfig
  }
  PayUBizSdk.openCheckoutScreen(paymentObject);
  ```

  ***
</Accordion>

<Accordion title="Step 4: Handle Payment Completion (Callbacks)" icon="fa-code">
  To get the callbacks for payment-related statuses, create a NativeEventEmitter object and subscribe to the following events.

  ```javascript React.js
  import { NativeEventEmitter } from 'react-native';

  //Register event emitters here.
  componentDidMount() {
  const eventEmitter = new NativeEventEmitter(PayUBizSdk);
  this.paymentSuccess = eventEmitter.addListener('onPaymentSuccess', this.onPaymentSuccess);
  this.paymentFailure = eventEmitter.addListener('onPaymentFailure', this.onPaymentFailure);
  this.paymentCancel = eventEmitter.addListener('onPaymentCancel', this.onPaymentCancel);
  this.error = eventEmitter.addListener('onError', this.onError);
  this.generateHash = eventEmitter.addListener('generateHash', this.generateHash);
  }
  onPaymentSuccess = (e) => {
  console.log(e.merchantResponse);
  console.log(e.payuResponse);
  }
  onPaymentFailure = (e) => {
  console.log(e.merchantResponse);
  console.log(e.payuResponse);
  }
  onPaymentCancel = (e) => {
  console.log('onPaymentCancel isTxnInitiated -' + e);
  }
  onError = (e) => {
  console.log(e);
  }
  generateHash = (e) => {
  console.log(e.hashName);
  console.log(e.hashString);
  var hashStringWithoutSalt = e.hashString;
  var hashName = e.hashName;
  var postSalt = e.postSalt; // compulsory for Additional Charges and Split Payment
  // Pass hashStringWithoutSalt to server
  // Server will append salt at the end and generate sha512 hash over it
  //  "<create SHA -512 hash of 'hashString+salt+postSalt'>"
  var hashValue = "<Set hash here which is fetched from server>";
  var result = { [hashName]: hashValue };
  PayUBizSdk.hashGenerated(result);
  }
  //Do remember to unregister eventEmitters here
  componentWillUnmount() {
  this.paymentSuccess.remove();
  this.paymentFailure.remove();
  this.paymentCancel.remove();
  this.error.remove();
  this.generateHash.remove();
  }
  ```

  ***

  ***
</Accordion>

<Accordion title="Step 5: Generate Hash (Dynamic Hash Generation)" icon="fa-code">
  This step describes how to pass the dynamic hashes. For detailed information, refer to [Hash Generation](doc:generate-dynamic-hash-react).

  <Accordion title="Passing dynamic hashes" icon="fa-code">
    To pass dynamic hashes, the merchant will receive a call on the generateHash method. In the method parameter, you will receive a dictionary or hashMap, then extract the value of hashString from that. Pass that value to the server to append the Salt at the end and generate the sha512 hash over it. The server gives that hash back to your app, and the app will pass that hash to PayU through a callback mechanism. For passing dynamic hashes during integration, use the following code snippet:

    ```javascript React.js
    generateHash = (e) => {
        console.log(e.hashName);
        console.log(e.hashString);
        var hashStringWithoutSalt = e.hashString;
        var hashName = e.hashName;
    	  var postSalt = e.postSalt; // compulsory for Additional Charges and Split Payment
    // Pass hashStringWithoutSalt to server
    // Server will append salt at the end and generate sha512 hash over it
    //  "<create SHA -512 hash of 'hashString+salt+postSalt'>"
        var hashValue = "<Set hash here which is fetched from server>";
        var result = { [hashName]: hashValue };
        PayUBizSdk.hashGenerated(result);
    }
    ```

    ***
  </Accordion>
</Accordion>

<Callout icon="📘" theme="info">
  **Notes:**

  * Always generate hashes on your backend.
  * URLs like [https://cbjs.payu.in/sdk/success](https://cbjs.payu.in/sdk/success) are placeholders; replace with your backend URLs post-testing.
  * Split payment and SI (Standing Instruction) are optional features—only use them if needed.
</Callout>

## Test the Integration and Go-Live

<Accordion title="Test the Integration" icon="fa-gear">
  <ReactNative_Test_the_Integration />
</Accordion>

<Accordion title="Go-live Checklist" icon="fa-gear">
  <ReactNative_Go_Live />
</Accordion>