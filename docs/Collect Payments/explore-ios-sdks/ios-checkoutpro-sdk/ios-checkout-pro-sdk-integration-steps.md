---
title: Integration Steps
deprecated: false
hidden: false
metadata:
  title: Integration Steps - iOS Checkout Pro SDK
  description: >-
    The iOS Checkout Pro SDK integration involves following specific steps for
    integration, testing, and a go-live checklist, with additional guidance on
    generating a dynamic hash.
  keywords:
    - Integration Steps for iOS Checkout Pro SDK
    - ' iOS Checkout Pro SDK Integration Steps'
    - ' Checkout Pro SDK Integration for Mobile iOS'
  robots: index
next:
  description: ''
---
---
title: Integration Steps
deprecated: false
hidden: false
metadata:
  title: Integration Steps - iOS Checkout Pro SDK
  description: >-
    Integrate PayU CheckoutPro SDK on iOS with CocoaPods/Swift: SDK setup, payment parameters, hash, callbacks, test cards, go-live.
  robots: index
  keywords:
    - payu checkoutpro sdk ios integration steps swift
    - ios payment gateway sdk integration cocoapods payu india
    - iphone ipad payment sdk integration checkout pro payu
    - integrate payment gateway ios app swift objective c payu
    - ios upi card payment sdk integration native payu
    - mobile payment sdk ios integration test sandbox payu
    - payment gateway ios sdk hash payment callback integration
    - payu ios sdk seamless checkout integration developer guide
    - ios payment integration app store release payu sdk
    - native ios payment gateway integration india payu checkoutpro
    - payu ios checkout pro sdk cocoapods integration steps
    - payment gateway ios sdk integration steps india payu

next:
  description: ''
---
The iOS Checkout Pro SDK integration involves the following steps:

## SDK Integration

Prerequisite: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

<Accordion title="Step 1: Set up pod" icon="fa-code">
  The CheckoutPro SDK is offered through CocoaPods. To add the SDK in your app project:

  Include the SDK framework in your podfile.

  ```
  // make sure to add below-mentioned line to use dynamic frameworks
  use_frameworks!
  // Add this to include our SDK
  pod 'PayUIndia-CheckoutPro' 
  ```

  * Install dependency using the pod install command in terminal
  * Add the following imports in the class where you need to initiate a payment.

  ```swift Swift
  import PayUCheckoutProKit
  import PayUCheckoutProBaseKit
  import PayUParamsKit
  ```
  ```c
  #import <PayUCheckoutProKit/PayUCheckoutProKit.h>
  #import <PayUCheckoutProBaseKit/PayUCheckoutProBaseKit.h>
  #import <PayUBizCoreKit/PayUBizCoreKit.h>
  #import <PayUParamsKit/PayUParamsKit.h>
  ```

  * Refer to the following Test the key and salt environments:
    * **Production**: [Generate Production Merchant Key and Salt](https://onboarding.payu.in/app/account/signup)
    * **Test**: [Generate Test Merchant Key and Salt](https://uat-onepayuonboarding.payu.in/app/account/signup)

  <Accordion title="Swift Package Manager Integration" icon="fa-code">
    You can integrate PayUIndia-Checkoutpro with your app or SDK using the following methods:

    * Using Xcode: Navigate to File > Add Package menu and add the following package:
      [https://github.com/payu-intrepos/PayUCheckoutPro-iOS](https://github.com/payu-intrepos/PayUCheckoutPro-iOS)
    * Using Package.Swift: Add the following line in the Package.swift dependencies: `.package(name: "PayUCheckoutProKit", url: "https://github.com/payu-intrepos/PayUCheckoutPro-iOS", from: "7.4.0")`
  </Accordion>

  <Accordion title="CrashReporter" icon="fa-code">
    In order to receive all the crashes related to our SDKs, add the following line to your AppDelegate `didFinishLaunchingWithOptions` method:

    ```swift
    PayUCheckoutPro.start()
    ```
    ```c
    [PayUCheckoutPro start];
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 2: Build the payment parameters (mandatory step)" icon="fa-code">
  <Accordion title="Step 2.1: Basic Integration" icon="fa-code">
    PayU SDK needs certain inputs from the merchant app to authenticate and initiate a transaction.

    ```swift
    let paymentParam = PayUPaymentParam(key: <String>,
                                        transactionId: <String>,
                                        amount: <String>,
                                        productInfo: <String>,
                                        firstName: <String>,
                                        email: <String>,
                                        phone: <String>,
                                        surl: <String>,//Pass your own surl
                                        furl: <String>,//Pass your own furl
                                        environment: <Environment> /*.production or .test*/)
                                        
    paymentParam.userCredential = <String> // For saving and fetching user’s saved card
    ```
    ```c
    PayUPaymentParam *paymentParam = [[PayUPaymentParam alloc] initWithKey:<#(NSString * _Nonnull)#>
                                                             transactionId:<#(NSString * _Nonnull)#>
                                                                    amount:<#(NSString * _Nonnull)#>
                                                               productInfo:<#(NSString * _Nonnull)#>
                                                                 firstName:<#(NSString * _Nonnull)#>
                                                                     email:<#(NSString * _Nonnull)#>
                                                                     phone:<#(NSString * _Nonnull)#>
                                                                      surl:<#(NSString * _Nonnull)#>
                                                                      furl:<#(NSString * _Nonnull)#>
                                                               environment:<#(enum Environment)#> /*EnvironmentProduction or EnvironmentTest*/];

    paymentParam.userCredential = <#(NSString)#>; // For saving and fetching use saved card
    ```

    > 📘 Notes:
    >
    > * The URL used in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.
    > * Kindly refer the below to[Generate own SURL/FURL](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios)
    > * The **TransactionId** parameter cannot have a special character and not more than 25 characters.

    <Accordion title="Mandatory parameters" icon="fa-code">
      Use the following table to pass the mandatory parameters in the PayU SDK:

      <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Data Type and Validation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Key<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant Key received from PayU Dashboard</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>TransactionId<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Cannot be null or empty and should be unique for each transaction. Maximum allowed length is 25 characters. It cannot contain special characters like: - /, & , @ etc.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be unique for each transaction</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Amount<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Total transaction amount.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Product Info<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Information about Product</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>First Name<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s first name</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Email<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s Email ID</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Phone<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer’s phone number</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be of 10 digits</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When the transaction gets successful, PayU will load this URL and pass the transaction response.</p><ul><li><em>Sample URL</em>: <a href="https://cbjs.payu.in/sdk/success">https://cbjs.payu.in/sdk/success</a></li><li><em>Note</em>:- This URL is used for only Testing Purposes. Don't go live, <a href="https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios">Refer to Generate own SURL/FURL</a></li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>furl\<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> When the transaction gets fail, PayU will load this url and pass transaction response.</p><ul><li><em>Sample URL</em>: <a href="https://cbjs.payu.in/sdk/failure">https://cbjs.payu.in/sdk/failure</a></li><li><em>Note</em>:- This URL is used for only Testing Purposes. Don't go live, <a href="https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios">Refer to Generate own SURL/FURL</a></li></ul></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Cannot be null or empty</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Environment\<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>Environment of SDK</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be either</p><ul><li><em>Swift</em>:<code>production or test </code><strong>ObjectiveC</strong>: <code>EnvironmentProduction </code>or <code>EnvironmentTest</code></li></ul></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>User Credential\ <code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a unique value\ Format: \<merchantKey>:\<userId> Here, UserId is any id/email/phone number to uniquely identify the user</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>PayUSIParams\ <code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> of PayUSIParams. This contains SI Details.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Object of PayUSIParams</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>SplitPaymentDetails\ <code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>\ This parameter is required for splitting the transactions.</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>Should be a json String</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>additionalCharges</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>String\ This parameter is required if merchant want to take additional charge from user</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>should be string with PG:Amount or IBIBOCode:Amount\ Sample: CC:10,NB:20,SBIB:15</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>percentageAdditionalCharges</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>String\ This parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>should be string with PG:Amount or IBIBOCode:Amount\ Sample: CC:100,NB:50,SBIB:25</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

      If you required any value in the response then pass the below value

      ```swift
      paymentParam.additionalParam[PaymentParamConstant.udf1] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf2] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf3] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf4] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf5] = <String>
      paymentParam.additionalParam[PaymentParamConstant.walletURN] = <String>  // Required for Amul Wallet
      ```
      ```c
      paymentParam.additionalParam = [[NSDictionary alloc] initWithObjectsAndKeys:
                                          <#(NSString)#>, PaymentParamConstant.udf1,
                                          <#(NSString)#>, PaymentParamConstant.udf2,
                                          <#(NSString)#>, PaymentParamConstant.udf3,
                                          <#(NSString)#>, PaymentParamConstant.udf4,
                                          <#(NSString)#>, PaymentParamConstant.udf5,
                                          <#(NSString)#>, PaymentParamConstant.walletURN,
                                          nil];
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Step 2.2: For Recurring Payments(SI) (Optional)" icon="fa-code">
    For setting up Standing Instructions (SI) or recurring payments, you can refer to the [Recurring Payments Documentation](doc:ios-recurring-payments-si).

    Use the following sample code:

    ```swift
     let siInfo = PayUSIParams(billingAmount: <String>,
                               paymentStartDate: <Date>,
                               paymentEndDate: <Date>,
                               billingCycle: <PayUBillingCycle>,
                               billingInterval: <NSNumber>)

                siInfo.billingLimit = <PayuBillingLimit>
                siInfo.billingRule = <PayuBillingRule>
                
                paymentParam.siParam = siInfo
    ```
    ```c
    paymentParam.siParams = siParam;
    ```
  </Accordion>

  <Accordion title="Step 2.3: For UPI One Time Mandate Payments (Optional)" icon="fa-code">
    For UPI One Time Mandate (OTM) payments, use the following parameters:

    ```swift
    let siInfo = PayUSIParams(paymentStartDate: self.siStartDate,
                            paymentEndDate: self.siEndDate,
                           isPreAuthTxn: true)
                
       paymentParam.siParam = siInfo
     #isPreAuthTxn must be true for OTM transactions
    ```
    ```c
    paymentParam.siParams = siParam;
    ```
  </Accordion>

  <Accordion title="Step 2.4: For Additional Charges" icon="fa-code">
    Additional charges can be applied to transactions:

    ```swift
    paymentParam.additionalCharges = "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55"
    paymentParam.percentageAdditionalCharges = "CC:50,SBIB:100,DINR:100,DC:25,NB:50"
    ```
    ```c
    paymentParam.additionalCharges = @"CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55";
    paymentParam.percentageAdditionalCharges = @"CC:50,SBIB:100,DINR:100,DC:25,NB:50";
    ```
  </Accordion>

  <Accordion title="Step 2.5: For Split Payments details (Optional)" icon="fa-code">
    Split payments allow you to distribute the payment amount between a parent merchant and sub-merchants.

    <Accordion title="JSON request structure of splitInfo field" icon="fa-code">
      ```json
      {
        "type": "absolute",
        "splitInfo": {
          "merchant_05Apr16_126800": {
            "aggregatorSubTxnId": "aggregatorSubTxnId1",
            "aggregatorSubAmt": "50"
          },
          "merchant_05Apr16_780908": {
            "aggregatorSubTxnId": "aggregatorSubTxnId2", 
            "aggregatorSubAmt": "30"
          }
        }
      }
      ```

      Example implementation:

      ```swift
      paymentParam.splitPaymentDetails = ""
      ```
      ```c
      paymentParam.splitPaymentDetails = @"";
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Step 2.6: For SKU details (Optional)" icon="fa-code">
    `PayUSkuDetails` is used for SKU-based offers.

    **PayUSkuDetails** – contains the following property:

    * `PayUSkuDetails(skus: [PayUSku])`
    * `skus`: Array of `PayUSku`

    **PayUSku** – Swift / Objective-C model:

    ```swift
    // Swift
    PayUSku(
        skuId: String,
        skuName: String,
        skuAmount: String,
        quantity: Int,
        offerKeys: [String]? = nil
    )
    ```

    | Parameter   | Description                                                                                                 |
    | ----------- | ----------------------------------------------------------------------------------------------------------- |
    | `skuId`     | Product Id used when creating the offer on the dashboard                                                    |
    | `skuName`   | Name of product                                                                                             |
    | `skuAmount` | Amount of product                                                                                           |
    | `quantity`  | Total quantity of product                                                                                   |
    | `offerKeys` | Optional – provide offer keys only if you want to restrict the offer to these products; otherwise set `nil` |

    For more information on the SkuDetails parameters, refer to [Create SKU Based Offers for iOS Checkout Pro](https://docs.payu.in/docs/ios_checkoutpro-offers_integration).

    <br />

    After creating the `PayUSkuDetails` object, set it on `PayUPaymentParam` as shown below.

    <br />

    > **Keep in mind**\
    > If you add SKU offer details, the `amount` in `PayUPaymentParam` must equal the sum of (quantity × skuAmount) for each item.

    ```swift
    let sku1 = PayUSku(skuId: "111", skuName: "Shoes", skuAmount: "100", quantity: 1, offerKeys: nil)
    let sku2 = PayUSku(skuId: "222", skuName: "Shirt", skuAmount: "100", quantity: 1, offerKeys: nil)

    let skuDetails = PayUSkuDetails(skus: [sku1, sku2])

    // Attach SKU details to payment params
    paymentParam.skuDetail = skuDetails
    ```
    ```c
    PayUSku *sku1 = [PayUSku new];
    sku1.skuId = @"111";
    sku1.skuName = @"Shoes";
    sku1.skuAmount = @"100";
    sku1.quantity = 1;
    sku1.offerKeys = nil;

    PayUSku *sku2 = [PayUSku new];
    sku2.skuId = @"222";
    sku2.skuName = @"Shirt";
    sku2.skuAmount = @"100";
    sku2.quantity = 1;
    sku2.offerKeys = nil;

    NSArray<PayUSku *> *skus = @[sku1, sku2];

    PayUSkuDetails *skuDetails = [PayUSkuDetails new];
    skuDetails.skus = skus;

    // Attach SKU details to payment params
    paymentParam.skuDetail = skuDetails;
    ```
  </Accordion>

  <Accordion title="Step 2.7: Third Party Verification (TPV) Flow (Optional)" icon="fa-code">
    CheckoutPro SDK supports TPV (Third Party Verification) flow for both UPI and Net Banking payment methods. TPV validates that payments are made from authorized beneficiary accounts by verifying account details during the transaction.

    > **What is TPV?**\
    > TPV is a security feature that ensures payments are made only from pre-registered and verified bank accounts. It helps prevent fraudulent transactions by matching the payer's account details with pre-approved beneficiary information.

    <Accordion title="TPV for UPI Payments" icon="fa-code">
      To enable TPV for UPI payments, you need to pass beneficiary account details with IFSC code and account number. This ensures that UPI transactions are processed only from the specified bank account.

      **Required Parameters for UPI TPV:**

      * `beneficiaryIFSC`: Bank's IFSC code
      * `beneficiaryAccountNumber`: Account number from which payment should be made

      ```swift
      let beneficiary1 = PayUBeneficiaryParams(
          beneficiaryName: "",
          beneficiaryAccountNumber: "002001600674",
          beneficiaryIFSC: "HDFC0000090",
          beneficiaryAccountType: .savings
      )

      var beneficiaryList = [PayUBeneficiaryParams]()
      beneficiaryList.append(beneficiary1)

      paymentParam.payuBeneficieryDetails = beneficiaryList
      ```
      ```c
      PayUBeneficiaryParams *beneficiary1 = [[PayUBeneficiaryParams alloc]
          initWithBeneficiaryName:@""
          beneficiaryAccountNumber:@"002001600674"
          beneficiaryIFSC:@"HDFC0000090"
          beneficiaryAccountType:BeneficiaryAccountTypeSavings];

      NSMutableArray *beneficiaryList = [NSMutableArray array];
      [beneficiaryList addObject:beneficiary1];

      paymentParam.payuBeneficieryDetails = beneficiaryList;
      ```

      > **Note**\
      > For UPI payments, only IFSC and Account Number are mandatory. Account type and beneficiary name are optional.
    </Accordion>

    <Accordion title="TPV for Net Banking Payments" icon="fa-code">
      To enable TPV for Net Banking, you need to pass additional parameters including account type and beneficiary name along with IFSC and account number. This provides enhanced verification for Net Banking transactions.

      **Required Parameters for Net Banking TPV:**

      * `beneficiaryIFSC`: Bank's IFSC code
      * `beneficiaryAccountNumber`: Account number from which payment should be made
      * `beneficiaryAccountType`: Type of account (savings or current)
      * `beneficiaryName`: Account holder's name (must match bank records)

      ```swift
      let beneficiary1 = PayUBeneficiaryParams(
          beneficiaryName: "John Doe",
          beneficiaryAccountNumber: "002001600674",
          beneficiaryIFSC: "HDFC0000090",
          beneficiaryAccountType: .savings
      )

      var beneficiaryList = [PayUBeneficiaryParams]()
      beneficiaryList.append(beneficiary1)

      paymentParam.payuBeneficieryDetails = beneficiaryList
      ```
      ```c
      PayUBeneficiaryParams *beneficiary1 = [[PayUBeneficiaryParams alloc]
          initWithBeneficiaryName:@"John Doe"
          beneficiaryAccountNumber:@"002001600674"
          beneficiaryIFSC:@"HDFC0000090"
          beneficiaryAccountType:BeneficiaryAccountTypeSavings];

      NSMutableArray *beneficiaryList = [NSMutableArray array];
      [beneficiaryList addObject:beneficiary1];

      paymentParam.payuBeneficieryDetails = beneficiaryList;
      ```

      **Available Account Types:**

      * `.savings` (Swift) / `BeneficiaryAccountTypeSavings` (Objective-C) - For savings bank accounts
      * `.current` (Swift) / `BeneficiaryAccountTypeCurrent` (Objective-C) - For current/checking accounts

      > **Important**\
      > The beneficiary name must exactly match the name registered with the bank. Any mismatch will cause the transaction to fail.
    </Accordion>

    <Accordion title="TPV for Multiple Payment Methods" icon="fa-layer-group">
      To support TPV for both UPI and Net Banking in the same transaction, create separate beneficiary detail objects and add them to an array. This allows customers to choose between UPI or Net Banking while maintaining TPV verification for both methods.

      **Use Case:**\
      This is useful when you want to offer multiple payment options to the customer while enforcing TPV validation on all available methods.

      ```swift
      // Beneficiary details for UPI
      let upiBeneficiary = PayUBeneficiaryParams(
          beneficiaryName: "",
          beneficiaryAccountNumber: "1234567890",
          beneficiaryIFSC: "BANK0001234",
          beneficiaryAccountType: .savings
      )

      // Beneficiary details for Net Banking
      let netBankingBeneficiary = PayUBeneficiaryParams(
          beneficiaryName: "John Doe",
          beneficiaryAccountNumber: "9876543210",
          beneficiaryIFSC: "BANK0005678",
          beneficiaryAccountType: .savings
      )

      // Add both beneficiary details to array
      var beneficiaryList = [PayUBeneficiaryParams]()
      beneficiaryList.append(upiBeneficiary)
      beneficiaryList.append(netBankingBeneficiary)

      paymentParam.payuBeneficieryDetails = beneficiaryList
      ```
      ```c
      // Beneficiary details for UPI
      PayUBeneficiaryParams *upiBeneficiary = [[PayUBeneficiaryParams alloc]
          initWithBeneficiaryName:@""
          beneficiaryAccountNumber:@"1234567890"
          beneficiaryIFSC:@"BANK0001234"
          beneficiaryAccountType:BeneficiaryAccountTypeSavings];

      // Beneficiary details for Net Banking
      PayUBeneficiaryParams *netBankingBeneficiary = [[PayUBeneficiaryParams alloc]
          initWithBeneficiaryName:@"John Doe"
          beneficiaryAccountNumber:@"9876543210"
          beneficiaryIFSC:@"BANK0005678"
          beneficiaryAccountType:BeneficiaryAccountTypeSavings];

      // Add both beneficiary details to array
      NSMutableArray *beneficiaryList = [NSMutableArray array];
      [beneficiaryList addObject:upiBeneficiary];
      [beneficiaryList addObject:netBankingBeneficiary];

      paymentParam.payuBeneficieryDetails = beneficiaryList;
      ```

      > **Best Practice**\
      > When supporting multiple payment methods, ensure that you provide complete beneficiary details for each payment method according to their respective requirements.
    </Accordion>

    ### Required Parameters Summary

    | Parameter                | UPI        | Net Banking | Description                                                |
    | ------------------------ | ---------- | ----------- | ---------------------------------------------------------- |
    | beneficiaryIFSC          | ✓ Required | ✓ Required  | Bank IFSC code (11 characters)                             |
    | beneficiaryAccountNumber | ✓ Required | ✓ Required  | Beneficiary account number                                 |
    | beneficiaryAccountType   | ✗ Optional | ✓ Required  | Account type (savings/current) - Mandatory for Net Banking |
    | beneficiaryName          | ✗ Optional | ✓ Required  | Account holder's name - Must match bank records exactly    |

    <br />

    > **Common Issues**\
    > • **Invalid IFSC Code**: Ensure the IFSC code is valid and matches the beneficiary's bank\
    > • **Name Mismatch**: For Net Banking, beneficiary name must exactly match bank records\
    > • **Account Type Error**: Use the correct account type enum value (savings or current)
  </Accordion>

  <Accordion title="Step 2.8: Cross Border Flow (OPGSP) (Optional)" icon="fa-code">
    OPGSP (Online Payment Gateway Service Provider) flow is designed for cross-border and international transactions. It requires complete address details to be passed along with payment parameters for compliance and fraud prevention purposes.

    > **When to use OPGSP?**\
    > Use OPGSP flow when processing international payments or when your business requires complete billing address verification for risk management and regulatory compliance.

    **PayUAddressDetails** – Contains the following properties:

    ```swift
    let address = PayUAddressDetails()
    address.lastName = "Doe"
    address.address1 = "34 Saikripa-Estate, Tilak Nagar"
    address.address2 = "Near Metro Station"
    address.city = "Mumbai"
    address.state = "Maharashtra"
    address.country = "India"
    address.zipcode = "400004"

    paymentParam.address = address
    ```
    ```c
    PayUAddressDetails *address = [[PayUAddressDetails alloc] init];
    address.lastName = @"Doe";
    address.address1 = @"34 Saikripa-Estate, Tilak Nagar";
    address.address2 = @"Near Metro Station";
    address.city = @"Mumbai";
    address.state = @"Maharashtra";
    address.country = @"India";
    address.zipcode = @"400004";

    paymentParam.address = address;
    ```

    ### Address Parameters

    | Parameter | Required   | Description                                                                                                                                                                                            | Example                         |
    | --------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
    | lastName  | ✓ Required | Customer's last name                                                                                                                                                                                   | Doe                             |
    | address1  | ✓ Required | The first line of the billing address. **Note:** This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 34 Saikripa-Estate, Tilak Nagar |
    | address2  | ✓ Required | The second line of the billing address                                                                                                                                                                 | Near Metro Station              |
    | city      | ✓ Required | The city where your customer resides as part of the billing address                                                                                                                                    | Mumbai                          |
    | state     | ✓ Required | The state where your customer resides as part of the billing address                                                                                                                                   | Maharashtra                     |
    | country   | ✓ Required | The country where your customer resides                                                                                                                                                                | India                           |
    | zipcode   | ✓ Required | Billing address zip code is mandatory for the cardless EMI option. Character Limit: 20                                                                                                                 | 400004                          |

    <br />

    > **Keep in mind**\
    > All address fields are **mandatory** for OPGSP transactions. Incomplete or incorrect address information may result in transaction failure or delays in processing.

    ***

    ### **UDF5 Parameter (Invoice Number) - MANDATORY**

    When using OPGSP flow, you **must** pass the Invoice Number in the **UDF5** parameter. This is a critical requirement for cross-border transactions and helps in transaction tracking and reconciliation.

    ```swift
    paymentParam.additionalParam[PaymentParamConstant.udf5] = "INV-2024-001234"
    ```
    ```c
    paymentParam.additionalParam[PaymentParamConstantUdf5] = @"INV-2024-001234";
    ```

    | Parameter | Required   | Description                                                         | Example         |
    | --------- | ---------- | ------------------------------------------------------------------- | --------------- |
    | udf5      | ✓ Required | The invoice ID or invoice number must be collected using this field | INV-2024-001234 |

    <br />

    > **Important**\
    > • The invoice number in UDF5 should be unique for each transaction\
    > • Keep the invoice number for your records as it will be used for reconciliation\
    > • Failure to provide UDF5 will result in transaction rejection for OPGSP flow
  </Accordion>

  <Accordion title="Step 2.9: WealthTech Flow (Optional)" icon="fa-code">
    WealthTech flow enables payments for wealth management products like mutual funds, SIPs (Systematic Investment Plans), and other investment instruments. You need to pass wealth product details as an array of PayUWealthProducts objects.

    > **What is WealthTech Flow?**\
    > WealthTech flow is specifically designed for fintech and wealth management platforms that facilitate investments in mutual funds and other financial products through PayU's payment gateway.

    **PayUWealthProducts** – Contains the following properties:

    | Parameter        | Required   | Description                                | Example      |
    | ---------------- | ---------- | ------------------------------------------ | ------------ |
    | type             | ✓ Required | Product type (e.g., mutual\_fund)          | mutual\_fund |
    | amount           | ✓ Required | Investment amount                          | 50000        |
    | receipt          | ✓ Required | Receipt number for the transaction         | 77407        |
    | mfMemberID       | ✓ Required | Unique member ID for the investor          | 123445       |
    | mfUserID         | ✓ Required | User ID for the investor                   | 77407        |
    | mfPartner        | ✓ Required | Partner name (e.g., cams, karvy, franklin) | cams         |
    | mfInvestmentType | ✓ Required | Investment type (L=Lumpsum, S=SIP)         | L            |
    | folio            | Optional   | Folio number (for existing investments)    | 9104927822   |
    | scheme           | Optional   | Scheme code                                | LT           |
    | mfAMCCode        | Optional   | AMC (Asset Management Company) code        | UTB          |

    <br />

    ```swift
    let product = PayUWealthProducts(
        type: "mutual_fund",
        amount: "50000",
        receipt: "77407",
        mfMemberID: "123445",
        mfUserID: "77407",
        mfPartner: "cams",
        mfInvestmentType: "L"
    )
    product.scheme = "LT"
    product.mfAMCCode = "UTB"

    paymentParam.products = [product]
    ```
    ```c
    PayUWealthProducts *product = [[PayUWealthProducts alloc]
        initWithType:@"mutual_fund"
        amount:@"50000"
        receipt:@"77407"
        mfMemberID:@"123445"
        mfUserID:@"77407"
        mfPartner:@"cams"
        mfInvestmentType:@"L"];

    product.scheme = @"LT";
    product.mfAMCCode = @"UTB";

    paymentParam.products = @[product];
    ```

    ### Investment Type Values

    | Code | Description | Use Case                   |
    | ---- | ----------- | -------------------------- |
    | L    | Lumpsum     | One-time investment        |
    | S    | SIP         | Systematic Investment Plan |

    ### Supported RTA Partners

    | Partner Code | Partner Name        |
    | ------------ | ------------------- |
    | cams         | CAMS (Computer Age) |
    | karvy        | Karvy/Kfintech      |
    | franklin     | Franklin Templeton  |

    <br />

    > **Keep in mind**\
    > • You can pass multiple wealth products in a single transaction\
    > • Ensure the total amount in PaymentParams matches the sum of all product amounts\
    > • Partner codes must match the RTA (Registrar and Transfer Agent) handling the mutual fund\
    > • For existing investments (additional purchase), always include the folio number
  </Accordion>

  <Accordion title="Step 2.10: Enforce Offer Keys (Optional)" icon="fa-code">
    Enforce Offer Keys allows you to apply specific promotional offers to transactions. Pass an array of offer keys to enforce specific offers during checkout.

    ```swift
    paymentParam.enforcementOfferKeys = ["offer_key_1"]

    // Usage - Multiple offers
    paymentParam.enforcementOfferKeys = ["OFFER123", "OFFER456", "OFFER789"]
    ```
    ```c
    paymentParam.enforcementOfferKeys = @[@"offer_key_1"];

    // Usage - Multiple offers
    paymentParam.enforcementOfferKeys = @[@"OFFER123", @"OFFER456", @"OFFER789"];
    ```

    **Note:** You can pass multiple offer keys to enforce different promotional offers during the payment process.
  </Accordion>

  <Accordion title="Step 2.11: Additional Parameters (Optional)" icon="fa-code">
    Additional parameters are optional parameters such as UDF (User Defined Fields), static hashes, etc. More details on static hash generation and passing are mentioned in the hash generation section. The following is a list of other parameters that can be passed in additional parameters.

    ### Additional Parameters

    | Parameter                                  | Description                                                           | Example      |
    | ------------------------------------------ | --------------------------------------------------------------------- | ------------ |
    | PaymentParamConstant.udf1 (optional)       | User-defined field, Merchant can store their customer ID, etc.        | udf1         |
    | PaymentParamConstant.udf2 (optional)       | User-defined field, Merchant can store their customer ID, etc.        | udf2         |
    | PaymentParamConstant.udf3 (optional)       | User-defined field, Merchant can store their customer ID, etc.        | udf3         |
    | PaymentParamConstant.udf4 (optional)       | User-defined field, Merchant can store their customer ID, etc.        | udf4         |
    | PaymentParamConstant.udf5 (optional)       | User-defined field, Merchant can store their customer ID, etc.        | udf5         |
    | PaymentParamConstant.sourceId (mandatory)  | When we use SODEXO Card payment then it's a mandatory parameter       | 456788765678 |
    | PaymentParamConstant.walletURN (mandatory) | When we use ClosedLoop Wallet payment then it's a mandatory parameter | 67890987     |
    | PaymentParamConstant.merchantAccessKey     | Merchant access key for specific payment flows                        | YOUR\_KEY    |

    <br />

    ```swift
    // UDF Parameters
    paymentParam.additionalParam[PaymentParamConstant.udf1] = "udf1"
    paymentParam.additionalParam[PaymentParamConstant.udf2] = "udf2"
    paymentParam.additionalParam[PaymentParamConstant.udf3] = "udf3"
    paymentParam.additionalParam[PaymentParamConstant.udf4] = "udf4"
    paymentParam.additionalParam[PaymentParamConstant.udf5] = "udf5"

    // Other Parameters
    paymentParam.additionalParam[PaymentParamConstant.walletURN] = "100000"
    paymentParam.additionalParam[PaymentParamConstant.sourceId] = "src_xxx"
    paymentParam.additionalParam[PaymentParamConstant.merchantAccessKey] = "YOUR_KEY"
    ```
    ```c
    // UDF Parameters
    paymentParam.additionalParam[PaymentParamConstantUdf1] = @"udf1";
    paymentParam.additionalParam[PaymentParamConstantUdf2] = @"udf2";
    paymentParam.additionalParam[PaymentParamConstantUdf3] = @"udf3";
    paymentParam.additionalParam[PaymentParamConstantUdf4] = @"udf4";
    paymentParam.additionalParam[PaymentParamConstantUdf5] = @"udf5";

    // Other Parameters
    paymentParam.additionalParam[PaymentParamConstantWalletURN] = @"100000";
    paymentParam.additionalParam[PaymentParamConstantSourceId] = @"src_xxx";
    paymentParam.additionalParam[PaymentParamConstantMerchantAccessKey] = @"YOUR_KEY";
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Generate the hash" icon="fa-code">
  This integration requires dynamic hashes. You must get hash string in map again `HashConstant.hashString` key in `generateHash`.  You need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to SDK.

  ```swift
  /// Use this function to provide hashes
  /// - Parameters:
  ///   - param: Dictionary that contains key as HashConstant.hashName & HashConstant.hashString
  ///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  func generateHash(for param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletion) {
      // Send this string to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashStringWithoutSalt = param[HashConstant.hashString] ?? ""
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashName = param[HashConstant.hashName] ?? ""

      // Set the hash in below string which is fetched from your server
      let hashFetchedFromServer = <#T##String#>
      
      onCompletion([hashName : hashFetchedFromServer])
  }
  ```
</Accordion>

<Accordion title="Step 4: Initiate the payment" icon="fa-code">
  After setting up the payment parameters and hashes, initiate the payment:

  ```swift
  PayUCheckoutPro.open(on: self, paymentParam: paymentParam, config: <PayUCheckoutProConfig>, delegate: self)
  ```
  ```c
  [PayUCheckoutPro openOn:self paymentParam:paymentParam config:<#(PayUCheckoutProConfig * _Nullable)#> delegate:self];
  ```
</Accordion>

<Accordion title="Step 5: Handle the payment completion" icon="fa-code">
  Handle the response when the payment is completed:
  Confirm to PayUCheckoutProDelegate and use these functions to get appropriate callbacks from the SDK:

  ```swift
  /// This function is called when we successfully process the payment
  /// - Parameter response: success response
  func onPaymentSuccess(response: Any?) {
      
  }

  /// This function is called when we get failure while processing the payment
  /// - Parameter response: failure response
  func onPaymentFailure(response: Any?) {
      
  }

  /// This function is called when the user cancel’s the transaction
  /// - Parameter isTxnInitiated: tells whether payment cancelled after reaching bankPage
  func onPaymentCancel(isTxnInitiated: Bool) {
      
  }

  /// This function is called when we encounter some error while fetching payment options or there is some validation error
  /// - Parameter error: This contains error information
  func onError(_ error: Error?) {
      
  }

  /// Use this function to provide hashes
  /// - Parameters:
  ///   - param: Dictionary that contains key as HashConstant.hashName & HashConstant.hashString
  ///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  func generateHash(for param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletion) {
      // Send this string to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashStringWithoutSalt = param[HashConstant.hashString] ?? ""
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashName = param[HashConstant.hashName] ?? ""
      let postSalt = param[HashConstant.postSalt] ?? "" //// compulsory for Additional Charges and Split Payment
      // Set the hash in below string which is fetched from your server
  		//  "<create SHA -512 hash of 'hashString+salt+postSalt'>" 
      let hashFetchedFromServer = <#T##String#>
      
      onCompletion([hashName : hashFetchedFromServer])
  }
  ```
  ```c
  /// This function is called when we successfully process the payment
  /// @param response  success response
  - (void)onPaymentSuccessWithResponse:(id _Nullable)response {
      
  }

  /// This function is called when we get failure while processing the payment
  /// @param response failure response
  - (void)onPaymentFailureWithResponse:(id _Nullable)response {
      
  }

  /// This function is called when the user cancel’s the transaction
  /// @param isTxnInitiated tells whether payment cancelled after reaching bankPage
  - (void)onPaymentCancelWithIsTxnInitiated:(BOOL)isTxnInitiated {
      
  }

  /// This function is called when we encounter some error while fetching payment options or there is some validation error
  /// @param error This contains error information
  - (void)onError:(NSError * _Nullable)error {
      
  }

  /// Use this function to provide hashes
  /// @param param NSDictionary that contains key as HashConstant.hashName & HashConstant.hashString
  /// @param onCompletion Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  - (void)generateHashFor:(NSDictionary<NSString *, NSString *> * _Nonnull)param onCompletion:(void (^ _Nonnull)(NSDictionary<NSString *, NSString *> * _Nonnull))onCompletion {
      // Send below string hashStringWithoutSalt to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      NSString *hashStringWithoutSalt = [param objectForKey:HashConstant.hashString];
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      NSString * hashName = [param objectForKey:HashConstant.hashName];
      
      // Set the hash in below string which is fetched from your server
      NSString *hashFetchedFromServer = <#(NSString)#>;
      
      NSDictionary *hashResponseDict = [NSDictionary dictionaryWithObjectsAndKeys:hashFetchedFromServer, hashName, nil];
      onCompletion(hashResponseDict);
  }
  ```

  <Accordion title="UPI Intent (Optional)" icon="fa-code">
    Currently, PayU supports only PhonePe and GooglePay through Intent. Add the query schemes in the`info.plist`:

    ```xml
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
    <Callout icon="📘" theme="info">
  **Note**: These schemes allow the SDK to detect installed UPI apps on the user’s device.

Some of the listed schemes may not be actively used at the moment, but they are included to maintain compatibility and to support additional UPI apps in future updates.
</Callout>

    # Sample Responses

    > 🚧 Watch Out
    >
    > * In case of UPI intent/Collect flow, you will not receive a callback response in surl or furl. In this case, the format of PayU response received will be different from other payment options that you need to handle at your end.
    > * Consider the **mihpayid** in the PayU response as **PayU ID/ID**
  </Accordion>

  <Accordion title="Card/NB/Wallet and other transactions" icon="fa-code">
    ```json
    {
      "id": 403993715526319631,
      "mode": "CC",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "gtKFFx",
      "txnid": "iOS220530192146",
      "transaction_fee": "1.00",
      "amount": "1.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "addedon": "2022-05-30 19:22:39",
      "productinfo": "Nokia",
      "firstname": "Umang",
      "email": "umang@arya.com",
      "phone": "9876543210",
      "udf1": "udf11",
      "udf2": "udf22",
      "udf3": "udf33",
      "udf4": "udf44",
      "udf5": "udf55",
      "hash": "35e9b2f143abb2bcfbbe5e1b3fb7d95a8a2fad3b8e0fc2d737aa087b52a2f620847048e2794bfcfd06708e8095428314268a88867fffa30430275c496dc70847",
      "field1": "718984",
      "field2": "617544",
      "field3": "20220530",
      "field4": "0",
      "field5": "172989726099",
      "field6": "00",
      "field7": "AUTHPOSITIVE",
      "field8": "Approved or completed successfully",
      "field9": "No Error",
      "payment_source": "payu",
      "PG_TYPE": "CC-PG",
      "bank_ref_no": "718984",
      "ibibo_code": "MASTCC",
      "error_code": "E000",
      "Error_Message": "No Error",
      "offer_key": "CardsOfferKey@11311",
      "offer_failure_reason": "Invalid Offer Key.",
      "name_on_card": "PayUUser",
      "card_no": "512345XXXXXX2346",
      "issuing_bank": "HDFC",
      "card_type": "MAST",
      "is_seamless": 2,
      "surl": "https://payu.herokuapp.com/ios_success",
      "furl": "https://payu.herokuapp.com/ios_failure"
    }
    ```
    ```json
    {
      "id": 403993715530851078,
      "mode": "CC",
      "status": "failure",
      "unmappedstatus": "failed",
      "key": "gtKFFx",
      "txnid": "iOS240117182325",
      "transaction_fee": "1.00",
      "amount": "1.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "addedon": "2024-01-17 18:23:43",
      "productinfo": "Nokia",
      "firstname": "Umang",
      "email": "umang@arya.com",
      "phone": "9999999999",
      "udf1": "udf11",
      "udf2": "udf22",
      "udf3": "udf33",
      "udf4": "udf44",
      "udf5": "udf55",
      "hash": "0503b628ba7fe4716a7a96ac6b2c668634200419416af887766a417f3fc048200b155b04ccd3f4f5f601f5a22c3fb3af571773499605ee0446c98fe541b089f9",
      "field1": 793583808525231700,
      "field2": 833617,
      "field5": "63",
      "field6": "02",
      "field7": "AUTHNEGATIVE",
      "field9": "Bank was unable to authenticate.",
      "payment_source": "payu",
      "PG_TYPE": "CC-PG",
      "bank_ref_no": 793583808525231700,
      "ibibo_code": "CC",
      "error_code": "E308",
      "Error_Message": "Transaction Failed at bank end.",
      "card_no": "XXXXXXXXXXXX2346",
      "issuing_bank": "AXIS",
      "card_type": "MAST",
      "is_seamless": 2,
      "surl": "https://cbjs.payu.in/sdk/success",
      "furl": "https://cbjs.payu.in/sdk/failure"
    }
    ```
  </Accordion>

  <Accordion title="UPI Collect/Intent payments" icon="fa-code">
    ```json
    {
      "txnid": "iOS240117183850",
      "address1": "",
      "udf1": "udf11",
      "furl": "https://cbjs.payu.in/sdk/failure",
      "address2": "",
      "field6": "NA!NA!NA!NA",
      "lastname": "",
      "zipcode": "",
      "status": "success",
      "offer_key": null,
      "udf5": "udf55",
      "city": "",
      "udf9": "",
      "field2": "87768967657",
      "udf4": "udf44",
      "field7": "APPROVED OR COMPLETED SUCCESSFULLY|00",
      "addedon": "2024-01-17 18:39:13",
      "state": "",
      "field0": "",
      "udf6": "",
      "card_no": "",
      "discount": "0.00",
      "udf10": "",
      "hash": "44161a41207d4bc29ad802ecd6e06f0b350930fa539675bdd24ba8321e22972d2d12fee84a02af549717a5e52fd93db56be5f1c89388eaf2a2740b20491f8bac",
      "field4": "",
      "mode": "UPI",
      "bank_ref_num": "401789868507",
      "field9": "SUCCESS|Completed Using Callback",
      "offer_availed": null,
      "udf3": "udf33",
      "payment_source": "payuPureS2S",
      "key": "smsplus",
      "productinfo": "Nokia",
      "field1": "",
      "bank_ref_no": "401789868507",
      "mihpayid": 18978067105,
      "field8": "Phone Pe",
      "country": "",
      "curl": "https://cbjs.payu.in/sdk/failure",
      "bankcode": "INTENT",
      "udf2": "udf22",
      "field3": "8700908382@ybl",
      "phone": "9999999999",
      "email": "umang@arya.com",
      "net_amount_debit": 1,
      "amount": "1.00",
      "firstname": "Umang",
      "field5": "PPPL18978067105170124183913",
      "card_token": "",
      "unmappedstatus": "captured",
      "surl": "https://cbjs.payu.in/sdk/success",
      "udf8": "",
      "error": "E000",
      "error_Message": "No Error",
      "udf7": "",
      "PG_TYPE": "UPI-PG"
    }
    ```
    ```json
    {
      "address2": "",
      "field0": "",
      "field1": "",
      "udf9": "",
      "udf1": "udf11",
      "hash": "f995befdf65dacf0b71db83a94776efe9154ab9f0c5a378f4f07821fd61088a6f0a9cedbbf273df9048df64c4a4adb071701e9b2136e0b3e60f3c30e21aaa1ca",
      "txnid": "iOS220706164103",
      "field3": "",
      "mode": "UPI",
      "field5": "",
      "surl": "https://payu.herokuapp.com/ios_success",
      "udf7": "",
      "bankcode": "TEZ",
      "amount": "1.00",
      "udf5": "udf55",
      "additionalCharges": "0.59",
      "bank_ref_no": null,
      "payment_source": "payuPureS2S",
      "zipcode": "",
      "firstname": "Umang",
      "lastname": "",
      "net_amount_debit": 0,
      "productinfo": "Nokia",
      "city": "",
      "udf2": "udf22",
      "mihpayid": 15463188898,
      "email": "umang@arya.com",
      "field4": "",
      "state": "",
      "phone": "9876543210",
      "furl": "https://payu.herokuapp.com/ios_failure",
      "curl": "https://payu.herokuapp.com/ios_failure",
      "card_token": "",
      "PG_TYPE": "UPI-PG",
      "field6": "",
      "addedon": "2022-07-06 16:41:28",
      "udf6": "",
      "udf8": "",
      "bank_ref_num": null,
      "field7": "",
      "udf10": "",
      "error": "E308",
      "field2": "",
      "udf3": "udf33",
      "card_no": "",
      "field9": "P|PENDING|Completed Using Verify API",
      "field8": "INTENT",
      "unmappedstatus": "failed",
      "key": "3TnMpV",
      "udf4": "udf44",
      "country": "",
      "status": "failure",
      "address1": "",
      "error_Message": "Transaction Failed at bank end."
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 6: Custom Note Integration" icon="fa-info-circle">
  This section describes how to integrate custom notes in PayUCheckoutPro SDK.

  <Accordion title="Create a Custom Note List and Pass to SDK" icon="fa-info-circle">
    Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom\_note and custom\_note\_category need to be passed.To pass the custom note list, Create a PayUCheckoutProConfig object and set the CustomNoteDetails similar to the following code block:

    ```swift Swift
    var customNotes = [PayUCustomNote]()
    let customNote1 = PayUCustomNote()
    customNote.note = “<your note message>”
    customNote.noteCategories =  [] // Empty to show notes on L1 screen
    customNotes.append(customNote)

    let customNote2 = PayUCustomNote()
    customNote.note = “<your note message>”
    customNote.noteCategories =  [PaymentType.ccdc, PaymentType.NB, PaymentType.wallet, PaymentType.emi, PaymentType.savedCard, PaymentType.sodexo, PaymentType.upi, PaymentType.neftRtgs] 
    // pass Payment type to show notes on specific payment mode screen
    customNotes.append(customNote)

    // Initialize the PayU CheckoutPro Configuration
    let config = PayUCheckoutProConfig()

    // Assign the custom notes to the config
    config.customNotes = customNotes

    ```
  </Accordion>
</Accordion>

## Test the integration and Go-Live

<IOS_Test_the_Integration />

<IOS_Go_Live />