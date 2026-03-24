---
title: Web Services for Core SDK
excerpt: This page describes how to make api calls from SDK.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section provides a reference for the following Web Service APIs for Android Core SDK.

## Prerequisite steps

<Accordion title="Step 1: Initialise web service" icon="fa-code">
  Create an object of MerchantWebService with any of the supported API commands.

  ```java JAVA
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey); // Merchant key
  merchantWebService.setCommand(<Api Commands>); // Pass the command name
  merchantWebService.setVar1(<Pass var 1 value>) // Pass the var1 calue
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```

  For more information on Web Service hash generation, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

  <Callout icon="📘" theme="info">
    **Generate Hash for MerchantWebService**: To generate Hash refer to Hash Generation, use the following algorithm:

    `sha512(key|command|var1|salt)`

    where

    key= "Your Key"

    command= \<"Api Commands"> // Pass Command Name

    var1= \<"default"> // Pass the var1 value

    salt= "Your SALT"
  </Callout>
</Accordion>

<Accordion title="Step 2: Create Merchant web service PostData" icon="fa-code">
  ```java JAVA
  PostData postData = new MerchantWebServicePostParams(merchantWebService).getMerchantWebServicePostParams();
  if (postData.getCode() == PayuErrors.NO_ERROR) {
  payuConfig.setData(postData.getResult());
  }
  ```

  <Callout icon="📘" theme="info">
    **Troubleshoot Postdata code errors**: If the PostData code snippet (above) is returning errors, check the data point set in merchantWebService.
  </Callout>
</Accordion>

<Accordion title="Commands" icon="fa-code">
  | Commands                                 | Description                                                           | Task                                                                                                                                            | Listener                                   |
  | ---------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
  | `PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK` | To get all enabled payment options                                    | `GetPaymentRelatedDetailsTask payuTask = GetPaymentRelatedDetailsTask(this); payuTask.execute(payuConfig);`                                     | PaymentRelatedDetailsListener              |
  | `VAS_FOR_MOBILE_SDK`                     | To get the health status of payment options                           | `ValueAddedServiceTask payuTask = ValueAddedServiceTask(this); payuTask.execute(payuConfig);`                                                   | ValueAddedServiceApiListener               |
  | `GET_BIN_INFO`                           | Get Bin information on CC/DC                                          | `BinInfoTask binInfoTask = new BinInfoTask(this); binInfoTask.execute(payuConfig);`                                                             | GetCardInformationApiListener              |
  | `CHECK_IS_DOMESTIC`                      | Get Card information on CC/DC                                         | `GetCardInformationTask payuTask = GetCardInformationTask(this); payuTask.execute(payuConfig);`                                                 |                                            |
  | `GET_TRANSACTION_INFO`                   | Getting Transaction information                                       | `GetTransactionInfoTask payuTask = GetTransactionInfoTask(this); payuTask.execute(payuConfig);`                                                 | GetTransactionInfoApiListener              |
  | `VERIFY_PAYMENT`                         | Verify Payment Status                                                 | `VerifyPaymentTask payuTask = VerifyPaymentTask(this); payuTask.execute(payuConfig);`                                                           | VerifyPaymentApiListener                   |
  | `CHECK_OFFER_DETAILS`                    | To get the offer details.                                             | `CheckOfferDetailsTask payuTask = CheckOfferDetailsTask(this); payuTask.execute(payuConfig);`                                                   | CheckOfferDetailsApiListener               |
  | `API_GET_EMI_AMOUNT_ACCORDING_INTEREST`  | To get the EMI amount according to interest.                          | `GetEmiAmountAccordingToInterestTask payuTask = GetEmiAmountAccordingToInterestTask(this); payuTask.execute(payuConfig);`                       | GetEmiAmountAccordingToInterestApiListener |
  | `CHECK_OFFER_STATUS`                     | To check the status of the offer                                      | `GetOfferStatusTask payuTask = GetOfferStatusTask(this); payuTask.execute(payuConfig);`                                                         | GetOfferStatusApiListener                  |
  | `ELIGIBLE_BINS_FOR_EMI`                  | To check if the bin is eligible for EMI                               | `EligibleBinsForEMITask payuTask = EligibleBinsForEMITask(this); payuTask.execute(payuConfig);`                                                 | EligibleBinsForEMIApiListener              |
  | `GET_CHECKOUT_DETAILS`                   | To get info about additional charges, bank down, tax info, and offers | `GetCheckoutDetailsTask getCheckoutDetailsTask = GetCheckoutDetailsTask(this); getCheckoutDetailsTask.execute(payuConfig);`                     | CheckoutDetailsListener                    |
  | `GET_PAYMENT_INSTRUMENT`                 | To get stored cards of the user                                       | `GetTokenisedCardTask getTokenisedCardTask = GetTokenisedCardTask(this); getTokenisedCardTask.execute(payuConfig);`                             | GetTokenisedCardApiListener                |
  | `DELETE_PAYMENT_INSTRUMENT`              | To delete the stored card of the user                                 | `DeleteTokenisedCardTask deleteTokenisedCardTask = DeleteTokenisedCardTask(this); deleteTokenisedCardTask.execute(payuConfig);`                 | DeleteTokenisedCardApiListener             |
  | `GET_PAYMENT_DETAILS`                    | To get details of the stored card to make payment on another PG       | `GetTokenisedCardDetailsTask getTokenisedCardDetailsTask = GetTokenisedCardDetailsTask(this); getTokenisedCardDetailsTask.execute(payuConfig);` | GetTokenisedCardDetailsApiListener         |
  | `CHECK_BALANCE`                          | To get info about Sodexo saved Card                                   | `CheckBalanceTask checkBalanceTask= CheckBalanceTask(this); checkBalanceTask.execute(payuConfig);`                                              | CheckBalanceListener                       |
</Accordion>

## Enable Payment Options

This API is used enable multiple payment options on your checkout page.

<Callout icon="📘" theme="info">
  **Hash logic**: The hash logic for this API is:

  `<key>|payment_related_details_for_mobile_sdk|<userCredential>|<salt>`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
</Callout>

<Accordion title="Step 1: Execute GetPaymentRelatedDetailsTask" icon="fa-code">
  This class is used to get payment-related details. It takes an instance of a class that implements the `PaymentRelatedDetailsListener` interface as input.

  ```node Node
  GetPaymentRelatedDetailsTask paymentRelatedDetailsForMobileSdkTask = new GetPaymentRelatedDetailsTask(this);
  ```

  The `PaymentRelatedDetailsListener` interface has an abstract method called `onPaymentRelatedDetailsResponse()`. This method is called when the payment-related details are received.
</Accordion>

<Accordion title="Step 2: Get Response using onPaymentRelatedDetailsResponse()" icon="fa-code">
  Get response to determine the availability of various payment options (UPI, Google Pay, PhonePe, LazyPay, and Generic Intent) similar to the following code snippet:

  ```node Node
  @Override
  public void onPaymentRelatedDetailsResponse(PayuResponse payuResponse) {
  mPayuResponse = payuResponse;
  // Check if UPI as payment option available.
  if(payuResponse.isUpiAvailable()){
  // To check if UPI as payment option is available
  }
  if(payuResponse.isGoogleTezAvailable()){
  // To check if Google Pay as payment option is available
  }
  if(payuResponse.isPhonePeIntentAvailable()){
  // To check if Phonepe as payment option is available
  }
  if(payuResponse.isLazyPayAvailable()){
  // To check if LazyPay as payment option is available
  }
  if(payuResponse.isGenericIntentAvailable()){
  // To check if Generic Intent as payment option is available
  }
  //For SI Payments
  if(payuResponse.isNBAvailableFoSI){
  //Fetch SI NB List from payuResponse.getSiBankList() method
  }
  }
  ```

  This method is called when the payment-related details are received. This method takes a `PayuResponse` object as input. The `PayuResponse` object contains the payment-related details.

  The `onPaymentRelatedDetailsResponse()` method can be used to check if the following payment options are available:

  * UPI
  * Google Pay
  * PhonePe Intent
  * LazyPay
  * Generic Intent
  * The `onPaymentRelatedDetailsResponse()` method can also be used to fetch the list of SI banks if SI payments are enabled.
</Accordion>

## Get Checkout Details API

The **Get Check Out Details** API provides information on the bank down status, tax info, and offers enabled on a merchant key. You can call this API is similar to other Web Services. The only difference is that it requires a JSON in var1 as in the following code block:

```json JSON
{
   "requestId":"1614595430980",
   "transactionDetails":{
      "amount":5000
   },
    "customerDetails": {
      // optional
      "mobile": "9999999999" // optional
    },
   "useCase":{
      "getAdditionalCharges":true,
      "getTaxSpecification":true,
      "checkDownStatus":true,
      "getExtendedPaymentDetails":true,
      "getOfferDetails":true
   }
}
```

Where the `requestId` is a unique random number passed in the request.

<Accordion title="Step 1: Create the var1" icon="fa-code">
  Mobile SDK has a Utility class to create a JSON, as explained above. The implementation is similar to the following code snippet:

  ```Text JAVA
    Usecase.Builder usecase = new Usecase.Builder()
    .setCheckCustomerEligibility(true)
    .shouldCheckDownStatus(true) // set it to true to fetch bank down status for each payment option 
    .shouldGetAdditionalCharges(true) // set it to true to fetch additional charges applicable on each payment option
    .shouldGetOfferDetails(true) // set it to true to fetch offers enabled on merchant key 
    .shouldGetExtendedPaymentDetails(true) // set it to true to get extended payment details
    .shouldGetTaxSpecification(true) // set it to true to fetch tax info applicable on each payment mode 
    .build();
    
    GetTransactionDetails.Builder transactionDetails = new GetTransactionDetails.Builder()
    .setAmount(1000.0)//transaction amount in double
    .build();
    
    //Passing Customer Details is optional and can be used 
    //to check EMI eligibility based on mobile number
    CustomerDetails.Builder customerDetails = new CustomerDetails.Builder()
    .setMobile("9999999999") //pass the mobile number if want to get eligibility status in payment option
    .build();
    
    String var1 = new GetCheckoutDetailsRequest.Builder()
              .setUsecase(usecase)
              .setCustomerDetails(customerDetails)
              .setTransactionDetails(transactionDetails)
              .build().prepareJSON();
  ```

  After getting var1, pass that in Merchant Web Service with the command as PayuConstants.GET\_CHECKOUT\_DETAILS.
</Accordion>

<Accordion title="Step 2: Get API response" icon="fa-code">
  PayuResponse is received in the `onCheckoutDetailsResponse()` callback method of `CheckoutDetailsListener` as mentioned in the API Commands Supported table.
</Accordion>

<Accordion title="Get additional charges, bank down status, and offers" icon="fa-code">
  Additional Charges are returned in the PaymentDetails object for each payment option. The following example code snippet is for fetching Additional Charges for Net Banking:

  ```java Java
  //if netbanking is available on merchant key
  if(payuResponse.isNetBanksAvailable()){
  ArrayList<PaymentDetails> netbanks = payuResponse.getNetbanks();
  }
  ```

  * Additional Charge is available inside each `PaymentDetails` object and can be accessed using the `paymentDetails.getAdditionalCharge()` method
  * Similarly, bank health is available inside each `PaymentDetails` object and can be accessed using the `paymentDetails.isBankDown()` method.
  * For Offers, An `ArrayList<PayuOffer>` is available inside each `PaymentDetails` object. To get the offers list, use the `paymentDetails.getOfferDetailsList()`.
</Accordion>

<Accordion title="Get tax info" icon="fa-code">
  Tax is not applied on individual Net Banking or card schemes but instead applied at the payment mode level for all CC(Credit Card), DC(Debit Card), NB(Net Banking), Wallets, etc. So, to fetch the Tax Specification, use the following code block:

  ```java Java
  if(payuResponse.isTaxSpecificationAvailable())
  TaxSpecification taxSpecification = payuResponse.getTaxSpecification();

  taxSpecification.getCcTaxValue() //tax applicable on CC transactions
  taxSpecification.getDcTaxValue() //tax applicable on DC transactions
  taxSpecification.getNbTaxValue() //tax applicable on NB transactions
  taxSpecification.getCashTaxValue() //tax applicable on Wallet transactions
  ...
  ```
</Accordion>

## Lookup API

The **Lookup** API is used when integrating Multi-Currency Payments on Android Core SDK.

<Accordion title="Step 1: Create request" icon="fa-code">
  The Lookup API needs a JSON request. Product type needs to be passed either as DCC or MCP. DCC means Direct Currency Conversion, that is, it returns the conversion prices for card currency only. To get all enabled currencies on Merchant Access Key and their conversion prices, use product type as MCP. For DCC, cardBin is mandatory, but cardBin is not required for MCP.
  The following example is a request for DCC as the product type:

  ```json JSON
  {
     "merchantAccessKey":"E5ABOXOWAAZNXB6JEF5Z",
     "baseAmount":{
        "value":10000.00,
        "currency":"INR"
     },
     "cardBin":"513382",
     "merchantOrderId":"OBE-JU89-13151-110",
     "productType":"DCC",
     "signature":"be5a56667354d9e2ea5ea1c6af78b0afc1894eb2"
  }
  ```

  To create the Lookup API request as above, use the LookupApiRequestBuilder class similar to the following code block:

  ```Text JAVA
  String postData = new LookupRequest.LookupApiRequestBuilder()
                  .setAmount("10000.00")
                  .setCardBin("513382")
                  .setCurrency("INR")
                  .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                  .setMerchantOrderId("OBE-JU89-13151-110")
                  .setProductType(LookupRequest.ProductType.DCC)
                  .setSignature(hash)
                  .build().prepareJSON();
  ```
  ```Text Kotlin
   val postData = LookupRequest.LookupApiRequestBuilder()
                  .setAmount("10000.00")
                  .setCardBin("513382")
                  .setCurrency("INR")
                  .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                  .setMerchantOrderId("OBE-JU89-13151-110")
                  .setProductType(LookupRequest.ProductType.DCC)
                  .setSignature(hash)
                  .build().prepareJSON()
  ```

  The following example request is for MCP as the product type.

  ```Text JSON
  {
     "merchantAccessKey":"E5ABOXOWAAZNXB6JEF5Z",
     "baseAmount":{
        "value":10000.00,
        "currency":"INR"
     },
     "merchantOrderId":"OBE-JU89-13151-110",
     "productType":"MCP",
     "signature":"be5a56667354d9e2ea5ea1c6af78b0afc1894eb2"
  }
  ```

  To create the Lookup API request for MCP, use the LookupApiRequestBuilder class similar to the following code block:

  ```Text JAVA
  String postData = new LookupRequest.LookupApiRequestBuilder()
                  .setAmount("10000.00")
                  .setCurrency("INR")
                  .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                  .setMerchantOrderId("OBE-JU89-13151-110")
                  .setProductType(LookupRequest.ProductType.MCP)
                  .setSignature(hash)
                  .build().prepareJSON();
  ```
  ```Text Kotlin
   val postData = LookupRequest.LookupApiRequestBuilder()
                  .setAmount("10000.00")
                  .setCurrency("INR")
                  .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                  .setMerchantOrderId("OBE-JU89-13151-110")
                  .setProductType(LookupRequest.ProductType.MCP)
                  .setSignature(hash)
                  .build().prepareJSON()
  ```

  | Parameter Name      | Description                                                                                                           |
  | :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
  | Amount              | Transaction Amount                                                                                                    |
  | Card Bin            | First 6 digits of card number                                                                                         |
  | Currency            | Base Currency of Transaction                                                                                          |
  | Merchant Access Key | Merchant Access Key provided by PayU                                                                                  |
  | Merchant OrderId    | A unique request id for Lookup API request                                                                            |
  | Product Type        | Use MCP to get all enabled currency on Merchant Access Key or DCC to get direct currency conversion for card currency |
  | Signature           | Hmac SHA1 hash created with formula explained below                                                                   |

  To calculate signature, create the `HmacSHA1` hash of the following data:

  ```
  Signature =HMAC-SHA1(data, key);
  Data = baseCurrency+merchantOrderId+baseAmount
  Key = Secret Key shared with the merchant at the time of on-boarding
  Example data,
  baseCurrency = "INR"
  merchantOrderId = "OBE-JU89-13151-110"
  baseAmount = "10000.00"
  hashString = INROBE-JU89-13151-11010000.00
  ```
</Accordion>

<Accordion title="Step 2: Call LookupTask" icon="fa-code">
  Here, this is an object of a class that implements `LookupApiListener`. The following is a signature of LookupApiListener:

  ```java Java
  public interface LookupApiListener {
      void onLookupApiResponse(PayuResponse payuResponse);
  }
  ```
  ```kotlin Kotlin
  interface LookupApiListener {
      fun onLookupApiResponse(payuResponse: PayuResponse?)   
  }
  ```
</Accordion>

<Accordion title="Step 3: Get LookUp API response" icon="fa-code">
  After you execute LookupTask, the `onLookupApiResponse` callback method is called:

  ```java Java
  @Override
  public void onLookupApiResponse(PayuResponse payuResponse){    
      
      //Fetch lookup Details using below code
      LookupDetails lookupDetails = payuResponse.getLookupDetails();     
      }
  ```
  ```kotlin Kotlin
  override fun onLookupApiResponse(payuResponse: PayuResponse?){    
      
      //Fetch lookup Details using below code
      val lookupDetails = payuResponse.lookupDetails
      }
  ```
</Accordion>

## VAS API

The VAS API is used to get the list of down Net Banking and card BIN that is down.

<Callout icon="📘" theme="info">
  **Note** : You can check if a particular NetBanking service is down or not by just passing the bankCode or card-bin (first 6 digits of card number) and in payuResponse, the response will be fetched, for instance.
</Callout>

<Accordion title="Step 1: Call ValueAddedServiceTask" icon="fa-code">
  Integrate this API by calling the `ValueAddedServiceTask` method:

  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey);
  merchantWebService.setCommand(PayuConstants.VAS_FOR_MOBILE_SDK);
  merchantWebService.setVar1(PayuConstants.DEFAULT);
  merchantWebService.setVar2(PayuConstants.DEFAULT);
  merchantWebService.setVar3(PayuConstants.DEFAULT);
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Get onValueAddedServiceApiResponse" icon="fa-code">
  After you execute `ValueAddedServiceTask`, the `onValueAddedServiceApiResponse` callback method is called:

  ```java Java
    @Override
      public void onValueAddedServiceApiResponse(PayuResponse payuResponse) {
          if (mPayuResponse != null) {
             // It means given NetBanking code or cardnumber is not down i.e. it is in good to go condition
              } else {
             // It means given NetBanking code or cardnumber is down and you can display the responseMessage if you want or you can customize it
              }
          }
      }
  ```
</Accordion>

## Eligible Bins for EMI API

The **Eligible BINs for EMI** API fetches a list of eligible Bins for EMI corresponding to each Bank name along with minimum amount. 

<Callout icon="📘" theme="info">
  **Hash logic**: The hash logic for this API is:

  `<key>|eligibleBinsForEMI|default|<salt>`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
</Callout>

<Accordion title="Step 1: Set parameters" icon="fa-code">
  Set the parameters similar to the following snippet:

  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey);
  merchantWebService.setCommand(PayuConstants.ELIGIBLE_BINS_FOR_EMI);
  merchantWebService.setVar1("BIN"); // This parameter needs can include either Bin or NET.
  merchantWebService.setVar2(cardBin); // The first 6/8/9 digits of card number or network token.
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Handle the response" icon="fa-code">
  Handle the API response for eligible bins for EMI and log the raw response for debugging or informational purposes.

  ```java Java
  @Override
   public void onEligibleBinsForEMIApiResponse(PayuResponse payuResponse) {
      Log.d(TAG, "onEligibleBinsForEMIApiResponse: " + payuResponse.getRawResponse());
  }
  ```
</Accordion>

## Get EMI According to Interest API

**Get EMI According to Interest** API is used to get information to get details related to EMI such as EMI amount, tenure in month, interest rate, etc.

<Callout icon="📘" theme="info">
  **Hash logic**: The hash logic for this API is:

  `<key>|vas_for_mobile_sdk|<amount>|<salt>`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
</Callout>

<Accordion title="Step 1: Set parameters" icon="fa-code">
  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey);
  merchantWebService.setCommand(PayuConstants.API_GET_EMI_AMOUNT_ACCORDING_INTEREST);
  merchantWebService.setVar1(amount); // The amount that must be converted to EMI.
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Handle response" icon="fa-code">
  ```java Java
  @Override
  public void onGetEmiAmountAccordingToInterestApiResponse(PayuResponse payuResponse) {
      Log.d(TAG, "onGetEmiAmountAccordingToInterestApiResponse: " + payuResponse.getRawResponse());
  }
  ```
</Accordion>

## Get Transaction Info API

The **Get Transaction Info** API is used to extract the transaction details between two given time periods.

<Accordion title="Step 1: Set parameters" icon="fa-code">
  The API takes the input as two dates and the time (initial and final) between which the transaction details are needed. The output would consist of the status of the API (success or failed) and all the transaction details in an array format. Set startTime and endTime in the payment params as described in the following code block:

  ```Text Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey);
  merchantWebService.setCommand(PayuConstants.GET_TRANSACTION_INFO);
  merchantWebService.setVar1(startDate); // The starting Time (from when the transaction details are needed
  merchantWebService.setVar2(endDate); // The end Time (till when the transaction details are needed).
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Handle response" icon="fa-code">
  ```Text Java
  @Override
  public void onGetTransactionApiListener(PayuResponse payuResponse) {
      Log.d(TAG, "onGetTransactionApiListener: " + payuResponse.getRawResponse());
  }
  ```
</Accordion>

## Verify Payment API


The Android SDK provides a wrapper for the Verify Payment API that allows your mobile application to reconcile transactions with PayU's database securely. This integration is essential for Android developers implementing PayU payment functionality in their apps.

### Why Use Verify Payment in Your Android App

When implementing payments in your Android application, transaction responses may occasionally fail to reach your app due to network issues or user interactions (like app switching or device issues). The Verify Payment feature ensures your app can confirm transaction statuses directly with PayU's servers, preventing discrepancies in payment records.

<Callout icon="📘" theme="info">
  **Android Developer Note:**: Implementing this verification step in your Android payment flow protects your application from potential payment status tampering and ensures a reliable payment experience for your users.
</Callout>

### Android Implementation

<Accordion title="Step 1: Configure the Verify Payment Request" icon="fa-code">
  In your Android payment handling class, implement the Verify Payment API using the MerchantWebService provided by the PayU Android SDK:

  ```java
  // Import the required PayU Android SDK classes
  import com.payu.india.Model.PayuResponse;
  import com.payu.india.Payu.PayuConstants;
  import com.payu.india.Payu.PayuMerchantWebService;

  // In your payment verification method
  private void verifyTransactionStatus(String transactionId) {
      MerchantWebService merchantWebService = new MerchantWebService();
      
      // Set your merchant credentials and API parameters
      merchantWebService.setKey(merchantKey);
      merchantWebService.setCommand(PayuConstants.VERIFY_PAYMENT);
      
      // Set the transaction ID to verify
      // For multiple transactions, use pipe symbol (|) as separator: "txnId1|txnId2|txnId3"
      merchantWebService.setVar1(transactionId);
      
      // Generate and set the hash for secure communication
      String hashString = merchantKey + "|" + PayuConstants.VERIFY_PAYMENT + "|" + transactionId + "|" + salt;
      String hash = calculateHash(hashString);
      merchantWebService.setHash(hash);
      
      // Execute the verification request
      merchantWebService.postWebServiceRequest(this);
  }
  ```
</Accordion>

<Accordion title="Step 2: Implement the Response Handler" icon="fa-code">
  Add the response handler in your Activity or Fragment that implements PayuResponseListener:

  ```java
  @Override
  public void onVerifyPaymentResponse(PayuResponse payuResponse) {
      if (payuResponse != null) {
          // Log the complete response for debugging
          Log.d(TAG, "Payment Verification Response: " + payuResponse.getRawResponse());
          
          // Process the verification result
          if (payuResponse.isResponseAvailable() && payuResponse.getResponseStatus().equals(PayuConstants.SUCCESS)) {
              // Transaction verified successfully
              // Update your app's UI or database based on the verified status
              String transactionStatus = payuResponse.getResult();
              updateTransactionStatus(transactionStatus);
          } else {
              // Verification failed - handle accordingly
              handleVerificationFailure(payuResponse.getErrorMessage());
          }
      }
  }
  ```
</Accordion>

<Accordion title="Best Practices for Android Implementation" icon="fa-code">
  1. **Always verify after receiving payment notifications** - Implement the verification call in your app's payment completion handler
  2. **Handle timeouts appropriately** - Set reasonable timeouts for verification requests to avoid blocking your app's UI
  3. **Implement proper error handling** - Create user-friendly error messages for different verification failure scenarios
  4. **Store verification results** - Cache verification results locally to reduce unnecessary API calls
  5. **Background processing** - Consider using WorkManager for verification to ensure it completes even if the app is closed
</Accordion>

<Accordion title="Troubleshooting Android Integration" icon="fa-code">
  <Accordion title="Common Issues:" icon="fa-code">
    * **Hash calculation errors**: Ensure your hash generation uses the correct format and encoding
    * **Network connectivity**: Implement proper retry logic for intermittent network failures
    * **Transaction ID format**: Verify that transaction IDs are correctly formatted when sending multiple IDs

    For additional support with Android SDK integration, refer to the complete PayU Android SDK documentation or contact PayU mobile developer support.
  </Accordion>
</Accordion>

## Get BIN Info API

The **Get Bin Info** API is used to get the following using the BIN number, that is, the first six digits of a credit card or debit card:

**BIN information**

* Detect whether a particular BIN number is international or domestic.
* Determine the card’s issuing bank, the card type brand, that is, Visa, Master, etc.,
* Determine the card category, that is, credit, debit, etc.

This API is used to get the card BIN details. For this API, you need to set the following parameter in the payment params similar to the following code block:

<Accordion title="Step 1: Create Post Request" icon="fa-code">
  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey); // Merchant key
  merchantWebService.setCommand(PayuConstants.GET_BIN_INFO);
  merchantWebService.setVar1("1")
  merchantWebService.setVar2("1") //only for SI
  merchantWebService.setVar5("<pass card BIN Number>") // Pass card BIN Number
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Get onBinInfoApiResponse" icon="fa-code">
  ```java Java
  @Override
  public void onBinInfoApiResponse(PayuResponse payuResponse) {
  }
  ```
</Accordion>

## Get Card Information API

The **Get Card Information** (Check is Domestic) API is used to get if the card (passed in cardBin info API) is domestic or international. This API returns the following parameters:

* card_type
* category
* issuing_bank
* is_atmpin_card

For this API, you need to set the following parameter in the payment params similar to the following code block:

<Accordion title="Step 1: Create Post Request" icon="fa-code">
  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey); // Merchant key
  merchantWebService.setCommand(PayuConstants.CHECK_IS_DOMESTIC);
  merchantWebService.setVar1("<pass the card Bin number>")
  merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
  ```
</Accordion>

<Accordion title="Step 2: Get onGetCardInformationResponse" icon="fa-code">
  ```java Java
  @Override
  public void onGetCardInformationResponse(PayuResponse payuResponse) {
     Log.d(TAG, "onGetCardInformationResponse: " + payuResponse.getRawResponse());
  }
  ```
</Accordion>

<Accordion title="Offer APIs" icon="fa-code">
  The following APIs used for offers with Android Core SDK:

  * [Fetch Offer Details](#fetch-offer-details)
  * [Validate Offer Details](#validate-offer-details)
</Accordion>

<Accordion title="Fetch Offer Details" icon="fa-code">
  Use this API to fetch the offer list available for the merchant.

  To integrate this API call the fetchOfferDetails pass the requestData as parameters as shown in the code snippet below:

  ```java Java
  payuConfig = new PayuConfig();
  payuConfig.setEnvironment(PayuConstants.STAGING_ENV);

  V2ApiTask v2ApiTask = new V2ApiTask(merchantKey, payuConfig);
  FetchOfferApiRequest fetchOfferApiRequest = new FetchOfferApiRequest.Builder().setAmount(100.00).setUserToken("56789067890").build();
  v2ApiTask.getOffers(fetchOfferApiRequest, new HashGenerationListener() {
      @Override
      public void generateSignature(HashMap<String, String> hashMap, HashCompletionListener hashCompletionListener) {
          String hashName = hashMap.get(PayuConstants.CP_HASH_NAME);
          String hashData = hashMap.get(PayuConstants.CP_HASH_STRING);
          Log.d(TAG, "generateSignature: " + hashName);
          Log.d(TAG, "generateSignature: " + hashData);
          String hash = HashGenerationUtils.generateHashFromSDK(hashData, salt);
          HashMap hashMap1 = new HashMap();
          hashMap1.put(hashName, hash);
          hashCompletionListener.onSignatureGenerated(hashMap1);  // If you are passing wrong Hash then you will get null response
      }
  }, new FetchOfferDetailsListener() {
      @Override
      public void onFetchOfferDetailsResponse(PayuResponse payuResponse) {
          Log.d(TAG, "onFetchOfferDetailsResponse: " + payuResponse.getRawResponse());
      }
  });
  ```
</Accordion>

<Accordion title="Validate Offer API" icon="fa-code">
  Use this API to validate the offer for the merchants.

  To integrate this API call the method  validateOfferDetails and pass the requestData as parameters as shown in the code snippet below:

  ```java Java
  List<String> offerKey = new ArrayList<>();
  offerKey.add("<pass the offer key>");

  PaymentDetailsForOffer paymentDetailsForOffer = new PaymentDetailsForOffer.Builder().setPaymentCode("CC").setCardNumber("5123456789012346").setCategory("CREDITCARD").build();

  UserDetailsForOffer userDetailsForOffer = new UserDetailsForOffer.Builder().setUserToken("56789067890").build();

  payuConfig = new PayuConfig();
  payuConfig.setEnvironment(PayuConstants.STAGING_ENV);

  V2ApiTask v2ApiTask = new V2ApiTask(merchantKey, payuConfig);
  ValidateOfferRequest validateOfferRequest = new ValidateOfferRequest.Builder().setAmount("100.00").setOfferKey(offerKey).setPaymentDetails(paymentDetailsForOffer).setuserDetails(userDetailsForOffer).setAutoApply(false).build();
  v2ApiTask.validateOffers(validateOfferRequest, new HashGenerationListener() {
      @Override
      public void generateSignature(HashMap<String, String> hashMap, HashCompletionListener hashCompletionListener) {
          String hashName = hashMap.get(PayuConstants.CP_HASH_NAME);
          String hashData = hashMap.get(PayuConstants.CP_HASH_STRING);
          Log.d(TAG, "generateSignature: " + hashName);
          Log.d(TAG, "generateSignature: " + hashData);
          String hash = HashGenerationUtils.generateHashFromSDK(hashData, salt);
          HashMap hashMap1 = new HashMap();
          hashMap1.put(hashName, hash);
          hashCompletionListener.onSignatureGenerated(hashMap1);  // If you are passing wrong Hash then you will get null response
      }
  }, new ValidateOfferApiListener() {
      @Override
      public void onValiDateOfferResponse(PayuResponse payuResponse) {
          Log.d(TAG, "onValiDateOfferResponse: " + payuResponse.getRawResponse());
      }
  });
  ```
</Accordion>

## Check Balance API

The **Check Balance** API can be used to fetch detail of the Sodexo card with the source ID.

<Accordion title="Step 1: Set parameters" icon="fa-code">
  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey(merchantKey);
  merchantWebService.setCommand(PayuConstants.CHECK_BALANCE);
  merchantWebService.setVar1(sodexoSourceId); // This parameter must contain the Sodexo Source ID
  merchantWebService.setHash(HashGenerationUtils.generateHashFromSDK(hashData, salt));        
  ```
</Accordion>

<Accordion title="Step 2: Handle response" icon="fa-code">
  ```java Java
  @Override
    public void onCheckBalanceResponse(PayuResponse payuResponse) {
      Log.d(TAG, "onCheckBalanceResponse: " + payuResponse.getRawResponse());
  }
  ```

  ***
</Accordion>

## Tokenized Payment APIs

You can store and get stored card details from the vault. The tokenized payments for Android Core SDK includes the following APIs:

* [Get Tokenized Stored Cards API](#get-tokenized-stored-cards-api)
* [Get Tokenized Stored Card Details API](#get-tokenized-stored-card-details-api)
* [Delete Tokenized Stored Cards API](#delete-tokenized-stored-cards-api)

<Accordion title="Get Tokenized Stored Cards API" icon="fa-code">
  The **Get Tokenized Stored Cards** API is helpful in getting all the stored cards for a particular user. For this API, you need to set the`userCredentials` in the payment params similar to the following:

  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey("<pass the merchant key>");
  merchantWebService.setCommand(PayuConstants.GET_TOKENISED_USER_CARD);
  merchantWebService.setVar1(user_credentials); //In var1, pass the user_credential
  merchantWebService.setHash("<pass the hash value>"); 
  ```

  To integrate this API call the `getTokenizedStoredCards` method similar to the following:

  ```Text Java
  @Override
  public void onGetTokenisedCardResponse(PayuResponse payuResponse) {
          
  }
  ```
</Accordion>

<Accordion title="Get Tokenized Stored Card Details API" icon="fa-code">
  The **Get Tokenized Stored Card Details** API is used to get details of the stored card to make payment on another PG.

  ```Text Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey("<pass the merchant key>");
  merchantWebService.setCommand(PayuConstants.GET_TOKENISED_CARD_DETAILS); 
  merchantWebService.setVar1("<user_credentials>"); //In var1, pass the user_credential
  merchantWebService.setVar2("<cardToken>"); //In var2, pass the cardToken to get the saved card details
  merchantWebService.setHash("<pass the hash value>"); 
  ```

  ```Text Java
  @Override
  public void onTokenisedCardDetailsResponse(PayuResponse payuResponse) {
          
  }
  ```
</Accordion>

<Accordion title="Delete Tokenized Stored Cards API" icon="fa-code">
  The **Delete Tokenized Stored Cards** API is helpful in deleting stored cards.

  ```java Java
  MerchantWebService merchantWebService = new MerchantWebService();
  merchantWebService.setKey("<pass the merchant key>");
  merchantWebService.setCommand(PayuConstants.DELETE_TOKENISED_USER_CARD);
  merchantWebService.setVar1("<user_credentials>"); //In var1, pass the user_credential
  merchantWebService.setVar2("<cardToken>"); //In var2, pass the cardToken to delete the saved card details
  merchantWebService.setHash("<pass the hash value>"); 
  ```

  To integrate this API call the `deleteTokenizedStoredCard` method similar to the following:

  ```java Java
  @Override
  public void onDeleteTokenisedCardResponse(PayuResponse payuResponse) {

  }
  ```
</Accordion>
