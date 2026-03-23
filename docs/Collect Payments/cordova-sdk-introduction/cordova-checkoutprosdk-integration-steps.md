---
title: Steps to Integrate
deprecated: false
hidden: false
metadata:
  title: Cordova Checkout Pro SDK Integration Steps
  description: >-
    This document provides instructions on including the PayUCheckoutPro Cordova
    plugin in your app project, setting up callbacks, building payment
    parameters, generating payment hashes, initiating payments, and customizing
    the integration for iOS. It also includes information on distributing your
    app on the App Store or Ad-hoc.
  keywords:
    - Cordova Checkout Pro SDK Integration Steps
    - PayU Cordova SDK integration steps
    - Mobile payment integration with PayU Cordova SDK steps
    - PayU Cordova Checkout Pro set up for Mobile
    - Cordova CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Cordova SDK Basic Integration with Checkout Pro
  robots: index
next:
  description: ''
---
The Cordova Checkout SDK integration involves the following steps:

<Callout icon="📘" theme="info">
  **Note**: You can do iOS specific customization during integration. For more information, refer to [iOS-specific Integration customization (Optional)](#ios-specific-integration-customization-optional).
</Callout>

## Step 1: SDK Integration

<Accordion title="Step 1: Include the Cordova plugin in your app project" icon="fa-code">
  The PayUCheckoutPro for Cordova plugin is offered through npm. To Include the Cordova Plugin in your app project:

  1. Include the PayUCheckoutPro Cordova Plugin in Ionic Capacitor app by running the following commands that install the dependencies in the root folder of your app:

  ```
  npm install cordova-payu-checkoutpro  
  npx cap sync //Sync the plugin added above
  ```

  For IOS deployment, run the command pod installs to Install the pod inside the following folders:

  * ios/App folder in ionic
  * platform/ios folder in Cordova.

  > Note: Ensure that your minimum deployment target is iOS 11.

  2. Include the CheckOutPro Cordova plugin in Cordova app by running the following commands that depend in the root folder of your app:

  ```
  cordova plugin add cordova-payu-checkoutpro
  cordova build 
  ```
</Accordion>

<Accordion title="Step 2: Set up Callback" icon="fa-code">
  Include the following callbacks and methods in your Cordova app to receive callbacks from the CheckOutPro SDK:

  ```js
  var responseCallBack = function (response) {
    // payment successful
    if ("generateHash" in response) {
      generateHash(response);
    } else if ("onPaymentSuccess" in response) {
      onPaymentSuccess(response);
    } else if ("onPaymentFailure" in response) {
      onPaymentFailure(response);
    } else if ("onPaymentCancel" in response) {
      onPaymentCancel(response);
    } else if ("onError" in response) {
      onError(response);
    }
  };
  //Handle Callback methods from SDK
  function generateHash(response) {
    // Pass response param to your backend server
    // Backend will generate the hash which you need to pass to SDK
    // hashResponse: is the response which you get from your server
    var merchantSalt = `<Salt>`; //Keep Salt in the backend only.
    var resultValue = response.generateHash;
    var hashString = resultValue.hashString;
    var hashName = resultValue.hashName;
    var hash = {};
    hash[hashName] = sha512(hashString + merchantSalt);
    //Convert the hash data using sh512 and pass it to SDK.
    cordova.plugins.PayUCheckoutProCordova.hashGenerated(hash);
  }

  function onPaymentSuccess(response) {
    //Handle on Payment Success Response
  }
  function onPaymentFailure(response) {
    //Handle on Payment Failure Response
  }

  function onPaymentCancel(response) {
    //Handle on Payment Cancel Response
  }

  function onError(response) {
    //Handle on Error Response
  }
  ```
</Accordion>

<Accordion title="Step 3: Build the payment parameters" icon="fa-code">
  Your app needs to send transactional information to the CheckoutPro SDK to initiate a payment. Build the transactional information using the following code snippet:

  <Accordion title="Step 3.1: Basic Integration" icon="fa-code">
    ```javascript
    function createBasicPaymentParams() {
    var txnid = new Date().getTime().toString();

    var payUPaymentParams = {
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
    isProduction: false,

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
      udf5: 'udf5'
    }
    };
    return payUPaymentParams;
    }
    ```

    > **📘 Important:**
    >
    > * The sample SURL/FURL values are for testing only. Use your own URLs before going live.
    > * The `transactionId` must be unique, ≤ 25 characters, and cannot contain special characters like `_`, `$`, `%`, `&`, etc.
    > * For more information, refer to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).

    ***
  </Accordion>

  <Accordion title="Step 3.2: For Recurring Payments (SI) - Optional" icon="fa-code">
    For Standing Instructions / subscription payments, build the `payUSIParams` object.

    ```javascript

      // SI Parameters
      var payUSIParams = {
        isFreeTrial: false,
        billingAmount: '200',
        billingCycle: 'MONTHLY', // DAILY/WEEKLY/MONTHLY/YEARLY/ADHOC/ONCE
        billingCurrency: 'INR',
        billingInterval: '1', 
        paymentStartDate: '2027-05-06', // YYYY-MM-DD
        paymentEndDate: '2028-05-10',   // YYYY-MM-DD
        remarks: 'Subscription payment',
        billingDate: '', // Optional
      };
      
      var payUPaymentParams = {
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
    | `billingInterval`  | String  | Interval between charges            | `"1"`                                                   |
    | `paymentStartDate` | String  | Start date (YYYY-MM-DD)             | `"2027-05-06"`                                          |
    | `paymentEndDate`   | String  | End date (YYYY-MM-DD)               | `"2028-05-10"`                                          |
    | `remarks`          | String  | Additional notes                    | `"Subscription"`                                        |
    | `billingCurrency`  | String  | Currency code                       | `"INR"`                                                 |
    | `billingDate`      | String  | Specific billing date (optional)    | `""`                                                    |

    For more details, refer to [PayU Standing Instructions Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).

    ***
  </Accordion>

  <Accordion title="Step 3.3: For UPI One Time Mandate Payments - Optional" icon="fa-code">
    For UPI OTM, enable pre-auth and provide mandate dates.

    ```javascript

      // OTM Parameters
      var payUSIParams = {
        isPreAuthTxn: true, // Mandatory for UPI OTM
        paymentStartDate: '2025-04-01', // YYYY-MM-DD
        paymentEndDate: '2025-04-10'    // YYYY-MM-DD
      };
      
      var payUPaymentParams = {
        // Add OTM Parameters
        payUSIParams: payUSIParams,
      };
      

    ```

    ***
  </Accordion>

  <Accordion title="Step 3.4: For Additional Charges - Optional" icon="fa-code">
    Add additional charges or percentage-based charges for specific payment methods.

    ```javascript
    var payUPaymentParams = {
    // ... other parameters

      // Fixed additional charges
      additionalCharges: 'CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55',

      // Percentage-based additional charges
      percentageAdditionalCharges: 'CC:50,AMEX:100,DINR:75,DC:25'
    };
    ```

    **Format:**

    * `PaymentMode:Amount` separated by commas
    * Payment modes: `CC` (Credit Card), `DC` (Debit Card), `NB` (Net Banking), `UPI`, `WALLET`, `EMI`, `BNPL`
    * Or use specific bank codes like `SBIB` (State Bank), `AMEX`, etc.

    For more information, refer to [Collect Additional Charges](https://docs.payu.in/docs/collect-additional-charges).

    ***
  </Accordion>

  <Accordion title="Step 3.5: For Split Payments Details - Optional" icon="fa-code">
    For split payments (aggregator model), create a JSON object and pass it as a string.

    ```javascript
      // Split payment configuration
      var splitPaymentDetails = {
        type: 'absolute', // or 'percentage'
        splitInfo: {
          'imAJ7I': { // Child Merchant Key
            aggregatorSubTxnId: '12345673443540dd33d099887766650091', // Unique per transaction
            aggregatorSubAmt: '10',
            aggregatorCharges: '0',
          },
        },
      };
      
      var payUPaymentParams = {
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

  <Accordion title="Step 3.6: SKU Details - Optional" icon="fa-code">
    Pass item-level details for cart-based transactions.

    ```javascript

      // SKU Details
      var skuDetails = {
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
      
      var payUPaymentParams = {
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

  <Accordion title="Step 3.7: Third Party Verification (TPV) Flow - Optional" icon="fa-code">
    For TPV transactions, pass beneficiary account details for verification.

    ```javascript

      // TPV Beneficiary Details
      var beneficiaryDetails = [
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
      
      var payUPaymentParams = {   
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

  <Accordion title="Step 3.8: Cross Border Flow (OPGSP) - Optional" icon="fa-code">
    For OPGSP merchants, complete address details are mandatory. UDF5 (invoice number) is also required.

    ```javascript

      // Address Details (Mandatory for OPGSP)
      var address = {
        lastName: 'LastName',
        address1: 'Address1 value',
        address2: 'Address2 value',
        city: 'Gurgaon',
        state: 'Haryana',
        country: 'India',
        zipcode: '122001',
      };
      
      // Additional Param with UDF5 (Invoice Number - Mandatory for OPGSP)
      var additionalParam = {
        udf1: 'udf1',
        udf2: 'udf2',
        udf3: 'udf3',
        udf4: 'udf4',
        udf5: 'Sample_Invoice_11', // Mandatory for OPGSP
      };
      
      var payUPaymentParams = {
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

  <Accordion title="Step 3.9: WealthTech Flow - Optional" icon="fa-code">
    For investment and mutual fund transactions.

    ```javascript
      // WealthTech Product Details
      var products = [
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
      
      var payUPaymentParams = {
        // Add WealthTech products
        products: products,
      };

    ```

    ***
  </Accordion>

  <Accordion title="Step 3.10: Enforce Offer Keys" icon="fa-code">
    Apply specific promotional offers during checkout.

    ```javascript
    var payUPaymentParams = {
      // ... other parameters
      
      // Comma-separated offer keys
      enforcementOfferKeys: ['offer_key_1', 'offer_key_2'],
    };

    // Or as a comma-separated string (if parsing on your side)
    // enforcementOfferKeys: 'HoliSale@JbBdLOBritj5,Instantoffer@Kp78nFDENX5S'
    ```

    ***
  </Accordion>

  <Accordion title="Step 3.11: Additional Parameters - Optional" icon="fa-code">
    The additional parameters that are optional that can be passed to SDK are udf parameters, static hashes, and other parameters. For more details on Static Hash generation and passing them, refer to [generate hashes](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk). The following is a list of parameters that can be passed in additional parameters:

    | Parameter                                   | Description                                                                                                                                                                         |
    | :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | PayUCheckoutProConstants.CP\_UDF1           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | PayUCheckoutProConstants.CP\_UDF2           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | PayUCheckoutProConstants.CP\_UDF3           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | PayUCheckoutProConstants.CP\_UDF4           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | PayUCheckoutProConstants.CP\_UDF5           | `String` User defined field, Merchant can store their customer id, etc.                                                                                                             |
    | Static hashes                               | `String` The static hashes is specified in this parameter. For more information, refer to [Hash Generation](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) section. |
    | PayUCheckoutProConstants.SODEX\_OSOURC\_EID | `String` Sodexo Source ID, Merchant can store it from the third field of PayU response.                                                                                             |
    | PaymentParamConstant.walletUrn              | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account.                                                                                  |
  </Accordion>

  <Accordion title="Steps 3.12: Payment Param Definitions" icon="fa-code">
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

    const createPaymentParams = () => {
      var txnid = new Date().getTime().toString();

      // ========== Basic Payment Parameters (Mandatory) ==========
      var payUPaymentParams = {
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
      var additionalParam = {
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
      var splitPaymentDetails = {
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

<Accordion title="Step 4: Set up payment hashes" icon="fa-code">
  This step describes how to pass the dynamic hashes. For detailed information, refer to [Generate Hash](doc:generate-dynamic-hash-cordova).

  The SDK will send the hash string without salt in `responseCallBacktoopenCheckoutScreen`. Use the generate hash key to get the HashMap `<HashName, HashString>` in the callback response. Pass that hashMap to the server to generate the hash. Get the Hash from the server and pass it to SDK using the `cordova.plugins.PayUCheckoutProCordova.hashGenerated`(`<HashName hash>`)

  ```js
  var responseCallBack = function (response) {
    if ("generateHash" in response) {
      generateHash(response);
    }
    "generateHash";
    ...................
  };

  function generateHash(response) {
    var merchantSalt = `<salt>`; //keep this in the backend.
    var resultValue = response.generateHash;
    var hashStringWithoutSalt = resultValue.hashString;
    var hashName = resultValue.hashName;
    var hashType = resultValue.hashType;
    var postSalt = response[resultValue.postSalt];
    var hash = `<Get Hash Backend with < hashStringWithoutSalt, hashType , postSalt >`;
    //Convert the hash data using sh512.
    //Call Call hashGenerated with HashResponse< hashName, Hash> to pass the hash from server to SDK.
    cordova.plugins.PayUCheckoutProCordova.hashGenerated(hash);
  }
  ```

  <Callout icon="📘" theme="info">
    **Notes**:

    * You need the following type of hashes to be generated at your backend: v1 Hash, v2 Hashes, MCP Lookup, and Post Salt Hash.
    * You must generate the hashes on your server. Do not generate the hashes locally in your app, as it may compromise the security of the transactions.
  </Callout>

  The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) for CheckoutPro SDK.
</Accordion>

<Accordion title="Step 5: Update AndroidManifest.xml" icon="fa-code">
  To automatically fill OTP on bank pages, SDK requires `the RECEIVE_SMS` permission. Add the following code snippet to your `AndroidManifest.xml` like below.

  ```xml
  <uses-permission android:name="android.permission.RECEIVE_SMS" />
  ```
</Accordion>

<Accordion title="iOS-specific Integration customization (Optional)" icon="fa-code">
  * **UPI Intent**: Currently, PayU supports only PhonePe, Paytm, and GooglePay through Intent. Add the following query schemes in the `info.plist`.

  ```xml
  <key>LSApplicationQueriesSchemes</key>
  <array>
    <string>phonepe</string>
    <string>paytm</string>
    <string>tez</string>
  </array>
  ```

  * **Card Scanner, Camera Permission**:

  ```xml
  <key>NSCameraUsageDescription</key>
  <string>Please mention the description to give user info</string>
  ```

  ***
</Accordion>

## Step 2. Test the Integration and Go-live

<Accordion title="Test the integration" icon="fa-code">
  After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

  > 🚧 Callout
  >
  > The UPI in-app and UPI intent flow is not available in the Test mode.

  > 👍 Testing checklist
  >
  > Things to remember while testing an integration:
  >
  > 1. To test the integration make sure that you are making a transaction call to the test endpoint.
  > 2. Use your test key and salt for the transaction requests. See [Genearate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
  > 3. Set the value of the `environment` parameters to `1`.

  ***

  <TestCardsCallout />

  You can make test payments using one of the payment methods configured at the Checkout.

  <Accordion title="Test credentials for supported payment methods" icon="fa-code">
    Following are the payment methods supported in PayU Test mode.

    <Accordion title="Test Credential for Card" icon="fa-code">
      | Card Number      | Expiry | CVV | OTP    |
      | :--------------- | :----- | :-- | :----- |
      | 5123456789012346 | 05/25  | 123 | 123456 |
    </Accordion>

    <Accordion title="Test credentials for Net Banking" icon="fa-code">
      Use the following credentials to test the Net Banking integration:

      * **user name:** payu
      * **password**: payu
      * **OTP**: 123456
    </Accordion>

    <Accordion title="Test VPA for UPI" icon="fa-code">
      You can use either of the following VPAs to test your UPI-related integration:

      * [anything@upi](anything@upi)
      * [9999999999@upi](mailto:9999999999@payu.in)

      For Testing the UPI Collect flow, Please follow the below steps:- 

      1. Once you enter the VPA click on the verify button and proceed to pay.
      2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
      3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

      [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)`<Txn_id>`

      **For Android**

      You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

      > 🚧 Ensure to remove the code from the manifest file before going live.

      ```Text xml
      <application>
      <meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
      <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
      <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
      </application>
      ```
    </Accordion>

    <Accordion title="Test cards for EMI" icon="fa-code">
      You can use the following Debit and Credit cards to test EMI integration.

      <EMITestCards />
    </Accordion>

    <Accordion title="Test Wallets" icon="fa-code">
      You can use the following wallets and their corresponding credentials to test wallet integration.

      <EMITestWallets />

      <br />
    </Accordion>
  </Accordion>
</Accordion>

<Go_Live_Checklist />

## Distributing your app (App Store / Ad-hoc)

What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayUChekoutPro, refer to [Releasing Apple App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).
