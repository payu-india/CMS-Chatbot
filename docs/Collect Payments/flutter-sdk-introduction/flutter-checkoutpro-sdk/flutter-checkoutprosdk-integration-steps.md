---
title: Flutter SDK Integration
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Flutter Check Out SDK Integration Steps
  description: ''
  keywords:
    - Flutter Checkout Pro SDK Integration Steps
    - PayU Flutter SDK integration steps
    - Mobile payment integration with PayU Flutter SDK steps
    - PayU Flutter Checkout Pro set up for Mobile
    - Flutter CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Flutter SDK Basic Integration with Checkout Pro
  robots: index
---
---
title: Flutter SDK Integration
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  title: Flutter Check Out SDK Integration Steps
  description: ''
  keywords:
    - Flutter Checkout Pro SDK Integration Steps
    - PayU Flutter SDK integration steps
    - Mobile payment integration with PayU Flutter SDK steps
    - PayU Flutter Checkout Pro set up for Mobile
    - Flutter CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Flutter SDK Basic Integration with Checkout Pro
  robots: index
---
This section describes the steps to integrate on Flutter SDK.

<Cards>
  <Card title="Step 1: SDK Integration" href="#step-1-sdk-integration" icon="fa-rocket">
    New to our platform? Follow this guide to get started.
  </Card>

  <Card title="Step 2: Test the Integration and Go-Live" href="#step-2-test-the-integration-and-go-live" icon="fa-list">
    Explore our interactive API reference.
  </Card>
</Cards>

## Step 1: SDK Integration

To integrate PayU CheckoutPro with Flutter SDK:
For IOS, refer to iOS Specific Integration and check Distributing Your App (App Store/ Ad-hoc) to deploy your application. For more information, refer to [Explore iOS SDKs](doc:explore-ios-sdks)

<Accordion title="Step 1: Include the SDK in your app project" icon="fa-code">
  The CheckoutPro SDK for Flutter is offered through Flutter `pub.dev`

  * To add the PayU Checkout Pro Flutter plugin add the following dependency in your app: `$ flutter pub add payu_checkoutpro_flutter`

  ```d Dart
  import 'package:payu_checkoutpro_flutter/payu_checkoutpro_flutter.dart'; 
  import 'package:payu_checkoutpro_flutter/PayUConstantKeys.dart'; 
   
  ```

  * **For iOS**: Install the pod using the following command inside `ios` folder: `$ pod install`

  ***
</Accordion>

<Accordion title="Step2: Initialize PayU Checkout Pro Flutter object" icon="fa-code">
  * Create PayUCheckout Pro Flutter instance.
    ```d Dart
    late PayUCheckoutProFlutter \_checkoutPro;
    ```

  Initialize the PayUCheckoutProFlutter object using the current object.

  ```d Dart
  @override 
  void initState() 
  { 
  _checkoutPro = PayUCheckoutProFlutter(this); 
  } 
  ```

  > Note: Make sure your minimum deployment target is iOS 11.
</Accordion>

<Accordion title="Step3: Setup PayU Checkout Pro protocol" icon="fa-code">
  * Implement Checkout Pro protocol methods to get hash generation callback and transaction status callback from Checkout Pro SDK: `class MyClass extends SupeprClass implements PayUCheckoutProProtocol`
  * Implement the following methods in your class to get a callback from the SDK.

  ```d Dart
  @override 
    generateHash(Map response) { 
      // Pass response param to your backend server 
      // Backend will generate the hash which you need to pass to SDK 
      // hashResponse: is the response which you get from your server 
      Map hashResponse = {}; 
      _checkoutPro.hashGenerated(hash: hashResponse); 
    } 

  @override 
    onPaymentSuccess(dynamic response) { 
  //Handle Success response 
    } 
   
    @override 
    onPaymentFailure(dynamic response) { 
  //Handle Failure response 
    } 
   
    @override 
    onPaymentCancel(Map? response) { 
  //Handle Payment cancel response 
    } 
   
    @override 
    onError(Map? response) { 
  //Handle on error response 
    } 
  ```

  ***
</Accordion>

<Accordion title="Step4: Setup payment hashes" icon="fa-code">
  This step describes how to pass the static and dynamic hashes. For detailed information, refer to [Generate Hash](doc:generate-dynamic-hash-flutter).

  <Accordion title="Pass static hashes" icon="fa-code">
    To pass static hashes during integration, use the following code snippet:

    ```dart
    var payUPaymentParams = { 

       “key”: "Merchant key", 

       ... 

       ... 

       ... 

      “additionalParam”: { 
           “payment_related_details_for_mobile_sdk”: "payment_related_details_for_mobile_sdk hash", 
      “vas_for_mobile_sdk”: "vas_for_mobile_sdk hash", 
     “payment": "Payment Hash" 
       } 
    } 
    ```
  </Accordion>

  <Accordion title="Pass dynamic hashes" icon="fa-code">
    To pass dynamic hashes, the merchant will receive a call on the generateHash method. In the method parameter, you will receive a dictionary or hashMap, then extract the value of hashString from that. Pass that value to the server to append the Salt at the end and generate the sha512 hash over it. The server gives that hash back to your app, and the app will pass that hash to PayU through a callback mechanism.

    To pass the dynamic hashes during integration, use the following code snippet:

    ```dart
    var hashName = response[PayUHashConstantsKeys.hashName]; 
    var hashStringWithoutSalt = response[PayUHashConstantsKeys.hashString]; 
    var hashType = response[PayUHashConstantsKeys.hashType]; 
    var postSalt = response[PayUHashConstantsKeys.postSalt]; 
    var hash = <Get Hash Backend with < hashString, merchantSalt , postSalt > 
    Call hashGenerated with HashResponse< hashName , Hash> 
    _checkoutPro.hashGenerated(hash: hashResponse); 
    ```

    We need the following type of hashes to be generated at your backend: V1 Hash, V2 Hashes, MCP Lookup, and Post Salt Hash.

    Use the following code snippet to generate the required hashes:

    ```dart
    if (hashType == “V2”) { 
    hash = <Get HmacSHA256Hash with (hashStringWithoutSalt, merchantSalt)> 
    } else if (hashName == “mcpLookup”) { 
    hash = <Get HmacSHA1Hash with (hashStringWithoutSalt, 	merchantSecretKey)> 
    } else if (postSalt != null) 
    { 
    //Add salt first then add post salt to create final hash 	string. 
    hash = <Get SHA512Hash with <hashStringWithoutSalt + merchantSalt + <postSalt)>> 
    } 
    else 
    { 
    hash = <Get SHA512Hash from Backend with <hashStringWithoutSalt > + <merchantSalt>> 
    } 
    ```

    <Callout icon="📘" theme="info">
      **Remember:**

      * Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
      * The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) for CheckoutPro SDK.
    </Callout>

    ***
  </Accordion>
</Accordion>

<Accordion title="Step 5: Build the payment parameters" icon="fa-code">
  To initiate a payment, your app must send transactional information to the CheckoutPro SDK.

  <Accordion title="Step 5.1: Basic Integration" icon="fa-code">
    ```dart
    static Map createPayUPaymentParams() {
      var payUPaymentParams = {
        PayUPaymentParamKey.key: PayUTestCredentials.merchantKey,
        PayUPaymentParamKey.amount: "10",
        PayUPaymentParamKey.productInfo: "Info",
        PayUPaymentParamKey.firstName: "Abc",
        PayUPaymentParamKey.email: "test@gmail.com",
        PayUPaymentParamKey.phone: "9999999999",
        // Redirect URLs
        PayUPaymentParamKey.ios_surl: PayUTestCredentials.iosSurl,
        PayUPaymentParamKey.ios_furl: PayUTestCredentials.iosFurl,
        PayUPaymentParamKey.android_surl: PayUTestCredentials.androidSurl,
        PayUPaymentParamKey.android_furl: PayUTestCredentials.androidFurl,
        // 0 => Production, 1 => Test
        PayUPaymentParamKey.environment: "1",
    		PayUPaymentParamKey.additionalParam: additionalParam,
        PayUPaymentParamKey.userCredential:
            "${PayUTestCredentials.merchantKey}:test@gmail.com",
        // Must be <= 25 chars and should not contain special characters
        PayUPaymentParamKey.transactionId:
            DateTime.now().millisecondsSinceEpoch.toString(),
      };
      return payUPaymentParams;
    }
    ```

    > 📘 Important:
    >
    > * The sample SURL/FURL values are for testing only. PayU recommends using your own SURL/FURL before going live. For more information, refer to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk).
    > * The `transactionId` must not include special characters and must not exceed 25 characters.
  </Accordion>

  <Accordion title="Step 5.2: For Recurring Payments (SI) (Optional)" icon="fa-code">
    For Standing Instructions / subscription payments, build the `siParams` map and pass it using `PayUPaymentParamKey.payUSIParams`.

    ```dart
    // Mandatory for Recurring (Subscription / Standing Instruction) transactions, optional otherwise
    var siParams = {
      PayUSIParamsKeys.isFreeTrial: true,
      PayUSIParamsKeys.billingAmount: "200", // Required
      PayUSIParamsKeys.billingInterval: "1", // Required (string works for Android + iOS)
      PayUSIParamsKeys.paymentStartDate: "2026-02-20", // Required
      PayUSIParamsKeys.paymentEndDate: "2026-03-20", // Required
      PayUSIParamsKeys.billingCycle:
          "adhoc", // Required: daily/weekly/yearly/adhoc/once/monthly
      PayUSIParamsKeys.remarks: "Test SI transaction",
      PayUSIParamsKeys.billingCurrency: "INR",
      PayUSIParamsKeys.billingLimit: "ON", // ON/BEFORE/AFTER
      PayUSIParamsKeys.billingRule: "MAX", // MAX/EXACT
    };

    // Add to payment params
    payUPaymentParams[PayUPaymentParamKey.payUSIParams] = siParams;
    ```

    For more details, refer to [PayU Standing Instructions Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters).
  </Accordion>

  <Accordion title="Step 5.3: For UPI One Time Mandate Payments (Optional)" icon="fa-code">
    For UPI OTM, enable pre-auth and provide mandate dates.

    ```dart
    var siParams = {
      PayUSIParamsKeys.isPreAuthTxn: true, // Mandatory for UPI OTM
      PayUSIParamsKeys.paymentStartDate: "2026-02-20", // Required
      PayUSIParamsKeys.paymentEndDate: "2026-03-20", // Required
    };

    payUPaymentParams[PayUPaymentParamKey.payUSIParams] = siParams;
    ```
  </Accordion>

  <Accordion title="Step 5.4: For Additional Charges (Optional)" icon="fa-code">
    ```dart
    payUPaymentParams[PayUPaymentParamKey.additionalCharges] =
        "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55";
    payUPaymentParams[PayUPaymentParamKey.percentageAdditionalCharges] =
        "CC:50,AMEX:100,DINR:75,DC:25";
    ```

    For more information, refer to [Collect Additional Charges](https://docs.payu.in/docs/collect-additional-charges).
  </Accordion>

  <Accordion title="Step 5.5: For Split Payments details (Optional)" icon="fa-code">
    For split payments, create a JSON object and pass it as an encoded string.

    ```dart
    // import 'dart:convert';
    var splitPaymentDetails = {
      "type": "absolute",
      "splitInfo": {
        "imAJ7I": { // <Pass Child Merchant Key>
          "aggregatorSubTxnId": "123456754009227766650091", // unique for each txn
          "aggregatorSubAmt": "10",
          "aggregatorCharges": "0"
        }
      }
    };

    payUPaymentParams[PayUPaymentParamKey.splitPaymentDetails] =
        json.encode(splitPaymentDetails);
    ```
  </Accordion>

  <Accordion title="Step 5.6: SKU details (Optional)" icon="fa-code">
    ```dart
    var skus = [
      {
        PayUSKUKeys.skuId: "111",
        PayUSKUKeys.skuName: "Shoes",
        PayUSKUKeys.skuAmount: "100",
        PayUSKUKeys.quantity: 1,
        PayUSKUKeys.offerKeys: null
      },
      {
        PayUSKUKeys.skuId: "222",
        PayUSKUKeys.skuName: "Shirt",
        PayUSKUKeys.skuAmount: "100",
        PayUSKUKeys.quantity: 1,
        PayUSKUKeys.offerKeys: null
      }
    ];

    payUPaymentParams[PayUPaymentParamKey.skuDetails] = {PayUSKUKeys.skus: skus};
    ```

    > 🚧 Keep in mind
    >
    > If you are passing SKU offer details, the `amount` must equal the sum of (quantity × skuAmount) across all items.
  </Accordion>

  <Accordion title="Step 5.7: Third Party Verification (TPV) Flow (Optional)" icon="fa-code">
    ```dart
    var beneficiaryDetails = [
      // For UPI
      {
        PayUBeneficiaryKeys.beneficiaryAccount: "002001600674",
        PayUBeneficiaryKeys.beneficiaryIfsc: "HDFC0000090",
      },
      // For NetBanking
      {
        PayUBeneficiaryKeys.beneficiaryName: "SACHIN Tendulkar",
        PayUBeneficiaryKeys.beneficiaryAccount: "002001600674",
        PayUBeneficiaryKeys.beneficiaryIfsc: "ICIC0000090",
        PayUBeneficiaryKeys.beneficiaryAccountType: "SAVINGS",
      },
    ];

    payUPaymentParams[PayUPaymentParamKey.beneficiaryDetails] = beneficiaryDetails;
    ```
  </Accordion>

  <Accordion title="Step 5.8: Cross Border Flow (OPGSP)" icon="fa-code">
    OPGSP flow requires complete address details. When using OPGSP, **UDF5 (invoice number)** is mandatory.

    ```dart
    // Address details (mandatory only for OPGSP merchants)
    var addressDetails = {
      PayUAddressKeys.lastName: "Rastogi",
      PayUAddressKeys.address1: "C-366/A",
      PayUAddressKeys.address2: "LIC Gali",
      PayUAddressKeys.city: "New Delhi",
      PayUAddressKeys.state: "New Delhi",
      PayUAddressKeys.country: "India",
      PayUAddressKeys.zipcode: "110096",
    };

    payUPaymentParams[PayUPaymentParamKey.address] = addressDetails;

    // Additional params (UDF5 required for OPGSP)
    var additionalParam = {
      PayUAdditionalParamKeys.udf5: "Sample_Invoice_11",
    };
    payUPaymentParams[PayUPaymentParamKey.additionalParam] = additionalParam;
    ```
  </Accordion>

  <Accordion title="Step 5.9: WealthTech Flow (Optional)" icon="fa-code">
    ```dart
    var wealthTech = [
      {
        PayUWealthTechKeys.type: "mutual_fund",
        PayUWealthTechKeys.plan: "GD",
        PayUWealthTechKeys.folio: "9104927822",
        PayUWealthTechKeys.amount: "50000",
        PayUWealthTechKeys.option: "G",
        PayUWealthTechKeys.scheme: "LT",
        PayUWealthTechKeys.receipt: "77407",
        PayUWealthTechKeys.mfMemberID: "123445",
        PayUWealthTechKeys.mfUserID: "77407",
        PayUWealthTechKeys.mfPartner: "cams",
        PayUWealthTechKeys.mfInvestmentType: "L",
        PayUWealthTechKeys.mfAMCCode: "UTB"
      }
    ];

    payUPaymentParams[PayUPaymentParamKey.products] = wealthTech;
    ```
  </Accordion>

  <Accordion title="Step 5.10: Enforce Offer Keys (Optional)" icon="fa-code">
    ```dart
    payUPaymentParams[PayUPaymentParamKey.enforcementOfferKeys] =
        "HoliSale@JbBdLOBritj5,Instantoffer@Kp78nFDENX5S";
    ```
  </Accordion>

  <Accordion title="Step 5.11: Additional parameters (Optional)" icon="fa-code">
    Additional parameters are optional parameters such as UDF (User Defined Fields), access keys, static hashes, etc. The following is a list of commonly used fields:

    | Parameter                                 | Description                                                                                        |
    | :---------------------------------------- | :------------------------------------------------------------------------------------------------- |
    | PayUAdditionalParamKeys.udf1              | `String` User defined field, Merchant can store their customer id, etc.                            |
    | PayUAdditionalParamKeys.udf2              | `String` User defined field, Merchant can store their customer id, etc.                            |
    | PayUAdditionalParamKeys.udf3              | `String` User defined field, Merchant can store their customer id, etc.                            |
    | PayUAdditionalParamKeys.udf4              | `String` User defined field, Merchant can store their customer id, etc.                            |
    | PayUAdditionalParamKeys.udf5              | `String` User-defined field, Merchant can store their customer id, etc.                            |
    | PayUAdditionalParamKeys.merchantAccessKey | `String` Merchant access key (optional)                                                            |
    | PayUAdditionalParamKeys.sourceId          | `String` Sodexo Source ID, Merchant can store it from the third field of PayU response.            |
    | PayUAdditionalParamKeys.walletUrn         | `String` Pass this parameter if closed loop wallet (clw) payment mode is enabled for your account. |

    ```dart
    var additionalParam = {
      PayUAdditionalParamKeys.udf1: "udf1",
      PayUAdditionalParamKeys.udf2: "udf2",
      PayUAdditionalParamKeys.udf3: "udf3",
      PayUAdditionalParamKeys.udf4: "udf4",
      PayUAdditionalParamKeys.udf5: "Sample_Invoice_11",
      PayUAdditionalParamKeys.merchantAccessKey:
          PayUTestCredentials.merchantAccessKey,
      PayUAdditionalParamKeys.sourceId: PayUTestCredentials.sodexoSourceId,
      PayUAdditionalParamKeys.walletUrn: "<Wallet URN>",  
    };

    payUPaymentParams[PayUPaymentParamKey.additionalParam] = additionalParam;
    ```

    For more details on Static Hash generation and passing them, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk).
  </Accordion>

  <Accordion title="Step 5.12: Payment Param Definitions" icon="fa-code">
    <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Key<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter must contain your merchant key received from PayU.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"sms\<em>\</em>"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionId<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> It should be unique for each transaction. Cannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - "\_,$,%,&, etc"</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>4567890</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Amount<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Total transaction amount.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>100.0</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>productInfo<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Information about the product.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"ProductInfo"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>firstName<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s first name.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"Firstname"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Email<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s email id.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"<a href="mailto:test@payu.in">test@payu.in</a>"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s phone number.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"9999999999"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Surl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When the transaction is successful, PayU will load this URL and pass the transaction response.</p><ul><li><em>Sample SURL for testing</em>: <a href="https://cbjs.payu.in/sdk/success">https://cbjs.payu.in/sdk/success</a></li><li><em>Note</em>:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error.</li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The Surl that you have configured</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Furl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When the transaction fails, PayU will load this URL and pass the transaction response.</p><ul><li><em>Sample FURL for testing</em>: <a href="https://cbjs.payu.in/sdk/failure">https://cbjs.payu.in/sdk/failure</a></li><li><em>Note</em>:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error.</li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>The Furl that you have configured</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>User Credential <code>mandatory </code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format: <code>&lt;merchantKey&gt;:&lt;userId&gt;</code> Here, the <code>UserId</code> is any ID/email/phone number to uniquely identify the user.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"merchantKey:userId"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>isProduction<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Set the value of this parameter as <code>true</code>When you deploy the integration in production. To test the integration set the value as <code>false</code>.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>user\_token<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> The use for this param is to allow the offer engine to apply velocity rules at a user level.-<strong>Card Based Offers (CC, DC, EMI):</strong> For card payment mode offers, if this parameter is passed then the velocity rules would be applied on this token, if not passed the same would be applied to the card number.-<strong>UPI, NB, Wallet:</strong> It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"ABC456789"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>SkuDetails <code>'madatory'</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Create list of SKU as per products added in cart and add this list in SKU details. and set sku detials to PayUPaymentParams.</p><ul><li>\<em>Note:- \</em>When we use SKU features then it's a mandatory parameter otherwise it's not required.</li></ul></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalCharges</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>String This parameter is required if merchant want to take additional charge from user</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>should be string with PG:Amount or IBIBOCode:Amount Sample : CC:10,NB:20,SBIB:15</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>percentageAdditionalCharges</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>String This parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>should be string with PG:Amount or IBIBOCode:Amount Sample : CC:100,NB:50,SBIB:25</p><p><br /></p><p>Refer to Step 5.4: For Additional Charges (Optional)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>payUSIParams <code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains SI/mandate details for recurring payments.</p><ul><li>*Mandatory for Recurring (Subscription / Standing Instruction) transactions.**</li></ul><p>For more details: <a href="https://docs.payu.in/docs/introduction-recurring-payments-integration">Recurring Payments Integration</a></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>siParams object</p><p><br /></p><p>Refer to Step 5.2: For Recurring Payments(SI) (Optional) or Step 3.3: For UPI One Time Mandate Payments (Optional)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>enableNativeOTP <code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> Enable native OTP flow for card transactions. When set to true, OTP will be handled natively within the SDK.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>true / false</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>splitPaymentDetails <code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String (JSON encoded)</code> Contains details for split payment/settlement between multiple parties.</p><ul><li>*Mandatory only for Aggregator transactions.**</li></ul><p>For more details: <a href="https://docs.payu.in/docs/split-settlments">Split Settlements</a></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>json.encode(splitPaymentDetails)</p><p><br /></p><p>Refer to Step 5.5: For split Payments details (Optional)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>enforcementOfferKeys <code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Comma-separated list of offer keys to enforce specific offers during checkout. Allows merchants to apply targeted promotional offers.</p><ul><li><em>Note</em>: Optional parameter for enforcing specific offer keys at checkout.</li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"HoliSale\@JbBdLOBritj5,Instantoffer\@Kp78nFDENX5S"</p><p><br /></p><p>Refer to Step 5.10: Enforce Offer Keys</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryDetails <code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object/List</code> Contains beneficiary account details for payment verification in TPV flow.</p><ul><li>*Mandatory only for TPV (Third Party Verification) transactions.**</li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>beneficiaryDetails object or list</p><p><br /></p><p>Refer to Step 5.7: Third Party Verification (TPV) Flow (Optional)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>address / addressDetails <code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Contains customer's complete billing address including address lines, city, state, country, and zipcode.</p><ul><li>*Mandatory only for Cross-Border Payments (OPGSP) Merchant.**</li></ul><p>For more details: <a href="https://docs.payu.in/docs/introduction-cross-border-payments-import">Cross-Border Payments (Import)</a></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>addressDetails object</p><p><br /></p><p>Refer to Step 5.8: Cross Border Flow (OPGSP)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>products <code>conditional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>List<PayUWealthProducts></code> Contains details of wealth management and investment products such as mutual funds. Each product includes information like type, amount, folio number, plan, scheme, AMC code, member ID, user ID, partner details, and investment type.</p><ul><li>*Mandatory only for WealthTech / Investment product transactions.**</li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>List of PayUWealthProducts objects</p><p><br /></p><p>Refer to Step 5.9: WealthTech Flow</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
  </Accordion>

  <Accordion title="Step 5.13:  sample (recommended)" icon="fa-code">
    ```dart
    // import 'dart:convert';

    static Map createPayUPaymentParams() {
      // Mandatory for Recurring (Subscription / Standing Instruction) transactions, optional otherwise
      var siParams = {
        PayUSIParamsKeys.isFreeTrial: true,
        PayUSIParamsKeys.billingAmount: "200", // Required
        PayUSIParamsKeys.billingInterval: "1", // Required (string works for Android + iOS)
        PayUSIParamsKeys.paymentStartDate: "2026-02-20", // Required
        PayUSIParamsKeys.paymentEndDate: "2026-03-20", // Required
        PayUSIParamsKeys.billingCycle:
            "adhoc", // daily/weekly/yearly/adhoc/once/monthly
        PayUSIParamsKeys.remarks: "Test SI transaction",
        PayUSIParamsKeys.billingCurrency: "INR",
        PayUSIParamsKeys.billingLimit: "ON", // ON/BEFORE/AFTER
        PayUSIParamsKeys.billingRule: "MAX", // MAX/EXACT
      };

      // For UPI OTM
      // var siParams = {
      //   PayUSIParamsKeys.isPreAuthTxn: true, // Mandatory for UPI OTM
      //   PayUSIParamsKeys.paymentStartDate: "2026-02-20", // Required
      //   PayUSIParamsKeys.paymentEndDate: "2026-03-20", // Required
      // };

      var additionalParam = {
        PayUAdditionalParamKeys.udf1: "udf1",
        PayUAdditionalParamKeys.udf2: "udf2",
        PayUAdditionalParamKeys.udf3: "udf3",
        PayUAdditionalParamKeys.udf4: "udf4",
        PayUAdditionalParamKeys.udf5:
            "Sample_Invoice_11", // Invoice no required for OPGSP only
        PayUAdditionalParamKeys.merchantAccessKey:
            PayUTestCredentials.merchantAccessKey,
        PayUAdditionalParamKeys.sourceId: PayUTestCredentials.sodexoSourceId,
      };

      // Mandatory only for Aggregator transactions, optional for normal payments
      var splitPaymentDetails = {
        "type": "absolute",
        "splitInfo": {
          "imAJ7I": { // <Pass Child Merchant Key>
            "aggregatorSubTxnId": "123456754009227766650091", // unique per txn
            "aggregatorSubAmt": "10",
            "aggregatorCharges": "0"
          }
        }
      };

      // SKU Details
      var skus = [
        {
          PayUSKUKeys.skuId: "111",
          PayUSKUKeys.skuName: "Shoes",
          PayUSKUKeys.skuAmount: "100",
          PayUSKUKeys.quantity: 1,
          PayUSKUKeys.offerKeys: null
        },
        {
          PayUSKUKeys.skuId: "222",
          PayUSKUKeys.skuName: "Shirt",
          PayUSKUKeys.skuAmount: "100",
          PayUSKUKeys.quantity: 1,
          PayUSKUKeys.offerKeys: null
        }
      ];

      // Mandatory only for TPV transactions, optional for normal payments
      var beneficiaryDetails = [
        // For UPI Only
        {
          PayUBeneficiaryKeys.beneficiaryAccount: "002001600674",
          PayUBeneficiaryKeys.beneficiaryIfsc: "HDFC0000090"
        },
        // For NB Only
        {
          PayUBeneficiaryKeys.beneficiaryName: "SACHIN Tendulkar",
          PayUBeneficiaryKeys.beneficiaryAccount: "002001600674",
          PayUBeneficiaryKeys.beneficiaryIfsc: "ICIC0000090",
          PayUBeneficiaryKeys.beneficiaryAccountType: "SAVINGS"
        },
      ];

      // Mandatory only for OPGSP merchants, optional for others
      var addressDetails = {
        PayUAddressKeys.lastName: "Rastogi",
        PayUAddressKeys.address1: "C-366/A",
        PayUAddressKeys.address2: "LIC Gali",
        PayUAddressKeys.city: "New Delhi",
        PayUAddressKeys.state: "New Delhi",
        PayUAddressKeys.country: "India",
        PayUAddressKeys.zipcode: "110096"
      };

      // Mandatory only for WealthTech / Investment product
      var wealthTech = [
        {
          PayUWealthTechKeys.type: "mutual_fund",
          PayUWealthTechKeys.plan: "GD",
          PayUWealthTechKeys.folio: "9104927822",
          PayUWealthTechKeys.amount: "50000",
          PayUWealthTechKeys.option: "G",
          PayUWealthTechKeys.scheme: "LT",
          PayUWealthTechKeys.receipt: "77407",
          PayUWealthTechKeys.mfMemberID: "123445",
          PayUWealthTechKeys.mfUserID: "77407",
          PayUWealthTechKeys.mfPartner: "cams",
          PayUWealthTechKeys.mfInvestmentType: "L",
          PayUWealthTechKeys.mfAMCCode: "UTB"
        }
      ];

      var payUPaymentParams = {
        PayUPaymentParamKey.key: PayUTestCredentials.merchantKey,
        PayUPaymentParamKey.amount: "10",
        PayUPaymentParamKey.productInfo: "Info",
        PayUPaymentParamKey.firstName: "Abc",
        PayUPaymentParamKey.email: "test@gmail.com",
        PayUPaymentParamKey.phone: "9999999999",
        PayUPaymentParamKey.ios_surl: PayUTestCredentials.iosSurl,
        PayUPaymentParamKey.ios_furl: PayUTestCredentials.iosFurl,
        PayUPaymentParamKey.android_surl: PayUTestCredentials.androidSurl,
        PayUPaymentParamKey.android_furl: PayUTestCredentials.androidFurl,
        PayUPaymentParamKey.environment: "1", // 0 => Production, 1 => Test
        PayUPaymentParamKey.userCredential:
            "${PayUTestCredentials.merchantKey}:test@gmail.com",
        PayUPaymentParamKey.transactionId:
            DateTime.now().millisecondsSinceEpoch.toString(),
        PayUPaymentParamKey.additionalParam: additionalParam,

        // PayUPaymentParamKey.payUSIParams: siParams,
        // PayUPaymentParamKey.enableNativeOTP: true,
        // PayUPaymentParamKey.splitPaymentDetails: json.encode(splitPaymentDetails),
        // PayUPaymentParamKey.userToken: "", // Offers token (optional)
        // PayUPaymentParamKey.skuDetails: {PayUSKUKeys.skus: skus}, 
        // PayUPaymentParamKey.enforcementOfferKeys:
        //     "HoliSale@JbBdLOBritj5,Instantoffer@Kp78nFDENX5S", 
        // PayUPaymentParamKey.additionalCharges:
        //     "CC:25,NB:15,CASH:10,EMI:5,BNPL:50,UPI:100",
        // PayUPaymentParamKey.percentageAdditionalCharges:
        //     "CC:25,NB:15,CASH:10,EMI:5,BNPL:50,UPI:100",
        // PayUPaymentParamKey.beneficiaryDetails: beneficiaryDetails, 
        // PayUPaymentParamKey.address: addressDetails,
        // PayUPaymentParamKey.products: wealthTech, 
      };

      return payUPaymentParams;
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 6: Initiate payment" icon="fa-code">
  Initialize and launch the Checkout Pro SDK by calling the following code snippet:

  ```dart
  _checkoutPro.openCheckoutScreen( 
  payUPaymentParams: < payUPaymentParams >, 
  payUCheckoutProConfig: <payUConfigParams>, 

  ); 
  ```
</Accordion>

<Accordion title="IOS specific integration" icon="fa-code">
  Flutter SDK offers a few optional customizations for IOS as mentioned below:

  Customization (Optional)

  * **For UPI Intent**

  Currently, PayU supports only PhonePe and GooglePay through Intent. Add the query schemes in the `info.plist.`

  ```xml
  <key>LSApplicationQueriesSchemes</key> 
  <array> 
  <string>phonepe</string> 
  <string>paytm</string> 
  <string>tez</string> 
  <string>credpay</string>
  <string>bhim</string.
  </array> 
  ```

  * Card Scanner, Camera Permission

  ```xml
  <key>NSCameraUsageDescription</key> 

  <string>Please mention the description to give user info</string> 
  ```

  ***
</Accordion>

<Accordion title="Distributing your app (App Store / Ad-hoc)" icon="fa-code">
  What you get by default is a fat framework that allows you to test your app seamlessly on the device and simulator. But before archiving your app, you need to remove simulator slices from the framework. For detailed information on archiving your app with PayU ChekoutPro, refer to [Releasing Apple App Store](https://docs.payu.in/docs/ios-releasing-the-app-to-the-app-store).
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
