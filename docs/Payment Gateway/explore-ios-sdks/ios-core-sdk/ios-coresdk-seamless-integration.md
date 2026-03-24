---
title: Seamless Integration
excerpt: Build a seamless integration to create your own UI for payment flow.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Accordion title="Prerequisites" icon="fa-code">
  > ❗️ Before you begin
  >
  > * To download iOS SDK through CocoaPod, refer to CocoaPods Integration.
  > * Run the sample app:
  >   i. Download latest SDK version and unzip it.
  >   ii. Unzip Release-Universal, now drag and drop the content of unzipped file into Sample App

  <Accordion title="Step 1: Initial set up" icon="fa-code">
    To perform the initial setup:

    1. Download the latest SDK version from the following location and unzip it: [https://github.com/payu-intrepos/iOS-SDK/releases](https://github.com/payu-intrepos/iOS-SDK/releases)
    2. Unzip Release-Universal, drag and drop the content of the unzipped file into Sample App.

    ```swift Swift
    import PayUBizCoreKit
    ```
    ```swift Objective-C
    #import <PayUBizCoreKit/PayUBizCoreKit.h>
    ```

    > **Note**: While working with the Swift project add the above code in Bridging-Header.h file.

    3. Get all the required parameters.
    4. Create an object of PayUModelPaymentParams and set all the parameters in it.

    ```swift Swift
    let paymentParamForPassing = PayUModelPaymentParams()
    paymentParamForPassing.key = "0MQaQP"
    paymentParamForPassing.transactionID = "Ywism0Q9XC88qvy"
    paymentParamForPassing.amount = "10.0"
    paymentParamForPassing.productInfo = "Nokia"
    paymentParamForPassing.firstName = "Ram"
    paymentParamForPassing.email = "email@testsdk1.com"
    paymentParamForPassing.userCredentials = "ra:ra"
    paymentParamForPassing.phoneNumber = "1111111111"
    paymentParamForPassing.surl = "https://payu.herokuapp.com/ios_success"
    paymentParamForPassing.furl = "https://payu.herokuapp.com/ios_failure"
    paymentParamForPassing.udf1 = "u1"
    paymentParamForPassing.udf2 = "u2"
    paymentParamForPassing.udf3 = "u3"
    paymentParamForPassing.udf4 = "u4"
    paymentParamForPassing.udf5 = "u5"
    paymentParamForPassing.environment = ENVIRONMENT_PRODUCTION
    paymentParamForPassing.offerKey = "offertest@1411"
    ```
    ```objectivec Objective-C
      @property (strong, nonatomic) PayUModelPaymentParams *paymentParamForPassing;
      self.paymentParamForPassing = [PayUModelPaymentParams new];
      self.paymentParamForPassing.key = @"0MQaQP";
      self.paymentParamForPassing.transactionID = @"Ywism0Q9XC88qvy";
      self.paymentParamForPassing.amount = @"10.0";
      self.paymentParamForPassing.productInfo = @"Nokia";
      self.paymentParamForPassing.firstName = @"Ram";
      self.paymentParamForPassing.email = @"email@testsdk1.com";
      self.paymentParamForPassing.userCredentials = @"ra:ra";
      self.paymentParamForPassing.phoneNumber = @"1111111111";
      self.paymentParamForPassing.SURL = @"https://cbjs.payu.in/sdk/success";
      self.paymentParamForPassing.FURL = @"https://cbjs.payu.in/sdk/failure";
      self.paymentParamForPassing.udf1 = @"u1";
      self.paymentParamForPassing.udf2 = @"u2";
      self.paymentParamForPassing.udf3 = @"u3";
      self.paymentParamForPassing.udf4 = @"u4";
      self.paymentParamForPassing.udf5 = @"u5";
      self.paymentParamForPassing.environment= ENVIRONMENT_PRODUCTION;
      self.paymentParamForPassing.offerKey = @"offertest@1411";
    //You don't need to set udf1-5 in case you are not using them email and firstname can be empty strings "" if you don't want to use them For store user card feature you need to set userCredentials
    ```

    > **Note**: You don't need to set the udf1 – udf5 parameters. In case you are not using them, the email and firstname parameters can be empty strings ("").

    5. Set `paymentParamForPassing.userCredentials` to store the user card:

    ```swift Swift
    paymentParamForPassing.userCredentials = "ra:ra"
    ```
    ```objectivec Objective-c
      self.paymentParamForPassing.userCredentials = @"ra:ra"
    ```

    6. Set `offerKey` for offers:

    ```swift Swift
    paymentParamForPassing.offerKey = "offertest@1411"
    ```
    ```objectivec Objective-C
      self.paymentParamForPassing.offerKey = @"offertest@1411"
    ```

    7. Set default param (like phone and others) for any other payment:

    ```swift Swift
    paymentParamForPassing.phoneNumber = "1111111111"
    ```
    ```objectivec Objective-C
    self.paymentParamForPassing.phoneNumber = @"1111111111";
    ```

    8. Get the required hashes by using your own server. Set the hashes as follows:

    ```swift Swift
    paymentParamForPassing.hashes.paymentHash = "ade84bf6dd9da35d0aab50a5bf61d6272ab0fc488b361b65c66745054aacf1900e3c60b5022d2114bae7360174ebcb3cd7185a5d472e5c99701e5e7e1eccec34"
    paymentParamForPassing.hashes.paymentRelatedDetailsHash = "915299224c80eff0eb2407b945a5087556292f58baca25fd05a0bceb6826aa9eb531810001dd4b4677dd928dd60d39eecf843b2189f213f9bb82c5a9483e3aac"
    paymentParamForPassing.hashes.vasForMobileSDKHash = "5c0314c2781876f7e0a53676b0d08e1457dafe904d2d15d948626b57409538d51093eef4f15c792b1b9651be7b5659efdd45926e43a1145d68cea094687011ca"
    paymentParamForPassing.hashes.deleteUserCardHash = "03e10e892005755f91061121036fb1b10f46202b4138d182f153c5de5c7fd44930ed94b32fac230e59bac1e4ca123aca3297e4b9d25024bf13237db9721fec1a"
    paymentParamForPassing.hashes.offerHash = "1e99fdb59bd91c1a85624104c0fcfae34d7fcb850dd17a0b75e7efe49857d15fdefc47dd0d86ca34cbc3a8b580839aea6341a573e4e60dc1ddcf7ecc32bf9cae"
    ```
    ```objectivec Objective-C
      self.paymentParamForPassing.hashes.paymentHash = @"ade84bf6dd9da35d0aab50a5bf61d6272ab0fc488b361b65c66745054aacf1900e3c60b5022d2114bae7360174ebcb3cd7185a5d472e5c99701e5e7e1eccec34";
      self.paymentParamForPassing.hashes.paymentRelatedDetailsHash = @"915299224c80eff0eb2407b945a5087556292f58baca25fd05a0bceb6826aa9eb531810001dd4b4677dd928dd60d39eecf843b2189f213f9bb82c5a9483e3aac";
      self.paymentParamForPassing.hashes.VASForMobileSDKHash = @"5c0314c2781876f7e0a53676b0d08e1457dafe904d2d15d948626b57409538d51093eef4f15c792b1b9651be7b5659efdd45926e43a1145d68cea094687011ca";
      self.paymentParamForPassing.hashes.deleteUserCardHash = @"03e10e892005755f91061121036fb1b10f46202b4138d182f153c5de5c7fd44930ed94b32fac230e59bac1e4ca123aca3297e4b9d25024bf13237db9721fec1a";
      self.paymentParamForPassing.hashes.offerHash = @"1e99fdb59bd91c1a85624104c0fcfae34d7fcb850dd17a0b75e7efe49857d15fdefc47dd0d86ca34cbc3a8b580839aea6341a573e4e60dc1ddcf7ecc32bf9cae";
    ```

    ***
  </Accordion>

  <Accordion title="Step 2: Generate URL request for payment" icon="fa-code">
    To generate an URL request (and post parameters), you need to create an object as `createRequest `of the PayUCreateRequest class as shown in the following code block:

    ```swift Swift
    let createRequest = PayUCreateRequest()
    ```
    ```objectivec Objective-C
    @property (nonatomic, strong) PayUCreateRequest *createRequest;
    ```

    The callbacks give your URLRequest as well as post parameters (NSString format). You can use these post parameters to initialize the Custom Browser Instance.

    The following payment types are supported by SDK, and additional parameters are supported. The additional parameters that can be configured in the createRequest object created earlier are described in the following sections:
  </Accordion>
</Accordion>

<Accordion title="Credit Card/Debit Card Integration" icon="fa-code">
  To pay using a credit card or debit card, perform the following steps.

  1. Set the following credit card parameters:

  ```swift Swift
  paymentParamForPassing.cardNumber = "5123456789012346" //cardNumber
  paymentParamForPassing.nameOnCard = "name" //Name on card
  paymentParamForPassing.expYear = "2018" //Expiry year
  paymentParamForPassing.expMonth = "11" //ExpiryMonth
  paymentParamForPassing.cvv = "123" //CVV
  paymentParamForPassing.storeCardName = "My TestCard" //If you want to save card then pass StoreCardName otherwise it will not save & make sure userCredentials are provided
  ```
  ```objectivec Objective-C
          self.paymentParamForPassing.cardNumber = @"5123456789012346";//cardNumber
          self.paymentParamForPassing.nameOnCard = @"name";//Name on card
          self.paymentParamForPassing.expYear = @"2018";//Expiry year
          self.paymentParamForPassing.expMonth = @"11";//ExpiryMonth
          self.paymentParamForPassing.CVV = @"123";//CVV
          self.paymentParamForPassing.storeCardName = @"My TestCard";//If you want to save card then pass StoreCardName otherwise it will not save & make sure userCredentials are provided
  ```

  2. Get the request by using the `createRequestWithPaymentParam` method as follows:

  ```swift Swift
  createRequest().createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_CCDC, withCompletionBlock: { request, postParam, error in
      if error == nil {
          //It is good to go state. You can use request parameter in webview to open Payment Page
      } else {
          //Something went wrong with Parameter, error contains the error Message string
      }
  })
  ```
  ```objectivec Objective-C
          self.createRequest = [PayUCreateRequest new];
          [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_CCDC withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
          if (error == nil) {
          //It is good to go state. You can use request parameter in webview to open Payment Page
          }
          else{
          //Something went wrong with Parameter, error contains the error Message string
          }
      }];
  ```

  <br />
</Accordion>

<Accordion title="Stored Card Integration" icon="fa-code">
  To pay using a stored card, perform the following steps.

  1. Set the stored card parameter similar to the following code snippet:

  ```swift Swift
  let modelStoredCard = paymentRelatedDetail.storedCardArray[indexPath.row] as? PayUModelStoredCard

  paymentParamForPassing.cardToken = modelStoredCard?.cardToken
  paymentParamForPassing.cardBin = modelStoredCard?.cardBin
  paymentParamForPassing.cvv = "123" //CVV
  ```
  ```objectivec Objective-C
      PayUModelStoredCard *modelStoredCard = [self.paymentRelatedDetail.storedCardArray objectAtIndex:indexPath.row];

      self.paymentParamForPassing.cardToken = modelStoredCard.cardToken;
      self.paymentParamForPassing.cardBin = modelStoredCard.cardBin;
      self.paymentParamForPassing.CVV = @"123";//CVV
  ```

  2. Get the request by using the`createRequestWithPaymentParam` method similar to the following code snippet:

  ```swift Swift
  createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_STOREDCARD, withCompletionBlock: { request, postParam, error in
      if error == nil {
          //It is good to go state. You can use request parameter in webview to open Payment Page
      } else {
          //Something went wrong with Parameter, error contains the error Message string
      }
  })
  ```
  ```objectivec Objective-C
     self.createRequest = [PayUCreateRequest new];
      [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_STOREDCARD withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
      if (error == nil) {
      //It is good to go state. You can use request parameter in webview to open Payment Page
      }
      else{
      //Something went wrong with Parameter, error contains the error Message string
      }
  }];
  ```
</Accordion>

<Accordion title="Tokenized Card Payments" icon="fa-code">
  To pay using a stored card, perform the following steps.

  1. Set the stored card parameter similar to the following code snippet:

  ```swift Swift
  let modelStoredCard = paymentRelatedDetail.storedCardArray[indexPath.row] as? PayUModelStoredCard

  paymentParamForPassing.cardToken = modelStoredCard?.cardToken
  paymentParamForPassing.cardBin = modelStoredCard?.cardBin
  paymentParamForPassing.cvv = "123" //CVV
  ```
  ```objectivec Objective-C
      PayUModelStoredCard *modelStoredCard = [self.paymentRelatedDetail.storedCardArray objectAtIndex:indexPath.row];

      self.paymentParamForPassing.cardToken = modelStoredCard.cardToken;
      self.paymentParamForPassing.cardBin = modelStoredCard.cardBin;
      self.paymentParamForPassing.CVV = @"123";//CVV
  ```

  2. Get the request by using the`createRequestWithPaymentParam` method similar to the following code snippet:

  ```swift Swift
  createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_STOREDCARD, withCompletionBlock: { request, postParam, error in
      if error == nil {
          //It is good to go state. You can use request parameter in webview to open Payment Page
      } else {
          //Something went wrong with Parameter, error contains the error Message string
      }
  })
  ```
  ```objectivec Objective-C
     self.createRequest = [PayUCreateRequest new];
      [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_STOREDCARD withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
      if (error == nil) {
      //It is good to go state. You can use request parameter in webview to open Payment Page
      }
      else{
      //Something went wrong with Parameter, error contains the error Message string
      }
  }];
  ```
</Accordion>

<Accordion title="Net Banking Integration" icon="fa-code">
  To pay using Net Banking, perform the following steps.

  1. Set the Net Banking parameter as follows:

  ```swift Swift
  paymentParamForPassing.bankCode = "AXIB" //BankCode
  ```
  ```objectivec Objective-C
  ```

  2. Get the request by using the `createRequestWithPaymentParam` method as follows:

  ```swift Swift
  createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_NET_BANKING, withCompletionBlock: { request, postParam, error in
  if error == nil {
  //It is good to go state. You can use request parameter in webview to open Payment Page
  } else {
  //Something went wrong with Parameter, error contains the error Message string
  }
  })
  ```
  ```objectivec Objective-C
      self.createRequest = [PayUCreateRequest new];
      [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_NET_BANKING withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
      if (error == nil) {
      //It is good to go state. You can use request parameter in webview to open Payment Page
      }
      else{
      //Something went wrong with Parameter, error contains the error Message string
      }
  }];
  ```

  <br />
</Accordion>

<Accordion title="Cash Card Integration" icon="fa-code">
  To pay using a Cash Card, perform the following steps

  1. Set the cashcard parameter as follows:

  ```swift Swift
    paymentParamForPassing.bankCode = "AXIB" //BankCode
  ```
  ```objectivec
   self.paymentParamForPassing.bankCode = @"AXIB";//BankCode
  ```

  2. Get the request by using the `createRequestWithPaymentParam` method for instance.

  ```swift Swift
  createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_CASHCARD, withCompletionBlock: { request, postParam, error in
  if error == nil {
  //It is good to go state. You can use request parameter in webview to open Payment Page
  } else {
  //Something went wrong with Parameter, error contains the error Message string
  }
  })
  ```
  ```objectivec Objective-C
      self.createRequest = [PayUCreateRequest new];
      [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing
       forPaymentType:PAYMENT_PG_CASHCARD withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
         if (error == nil) {
            //It is good to go state. You can use request parameter in webview to open Payment Page
         }
         else{
           //Something went wrong with Parameter, error contains the error Message string
         }
      }];
  ```
</Accordion>

<Accordion title="EMI Payment" icon="fa-code">
  The section describes the following methods to collect payments with EMI:

  * [EMI](#emi)
  * [Cardless EMI](#cardless-emi)
  * [Subvention EMI](#subvention-emi)

  <Accordion title="EMI" icon="fa-code">
    To pay using EMI, perform the following steps.

    1. Set the EMI parameter for instance:

    ```swift Swift
    paymentParamForPassing.bankCode = "EMI03" //BankCode
    paymentParamForPassing.expiryYear = "2019"
    paymentParamForPassing.expiryMonth = "12"
    paymentParamForPassing.nameOnCard = "test"
    paymentParamForPassing.cardNumber = "5123456789012346"
    paymentParamForPassing.cvv = "123"
    ```
    ```objectivec Objective-C
        self.paymentParamForPassing.bankCode = @"EMI03";//BankCode
        self.paymentParamForPassing.expiryYear = @"2019";
        self.paymentParamForPassing.expiryMonth = @"12";
        self.paymentParamForPassing.nameOnCard = @"test";
        self.paymentParamForPassing.cardNumber = @"5123456789012346";
        self.paymentParamForPassing.CVV = @"123";
    ```

    2. Get the request by using the `createRequestWithPaymentParam` method for instance.

    ```swift Swift
    createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_EMI, withCompletionBlock: { request, postParam, error in
    if error == nil {
    //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
    //Something went wrong with Parameter, error contains the error Message string
    }
    })
    ```objectivec Objective-C
    self.createRequest = [PayUCreateRequest new];
    [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_EMI withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
                //It is good to go state. You can use request parameter in webview to open Payment Page
        }
        else{
         //Something went wrong with Parameter, error contains the error Message string

        }
    }];
    ```
  </Accordion>

  <Accordion title="Cardless EMI" icon="fa-code">
    To Pay using CardlessEMI, you need to set a parameter similar to the following code snippet:

    ```swift Swift
    paymentParamForPassing.bankCode = "ZESTMON" //BankID
    paymentParamForPassing.isCardlessEMI = true
    paymentParamForPassing.phoneNumber = "99999999"
    ```
    ```objectivec Objective-C
        self.paymentParamForPassing.bankCode = @"ZESTMON";//BankID
        self.paymentParamForPassing.isCardlessEMI = true;
        self.paymentParamForPassing.phoneNumber = @"9999999999";
        
    ```
  </Accordion>

  <Accordion title="Subvention EMI" icon="fa-code">
    To pay using Subvention EMI, perform the following steps.

    1. Set the value of the `subventionAmount` parameter of `paymentParams`:

    ```swift Swift
    paymentParamForPassing.bankCode = "EMI03" //BankCode
    paymentParamForPassing.expiryYear = "2019"
    paymentParamForPassing.expiryMonth = "12"
    paymentParamForPassing.nameOnCard = "test"
    paymentParamForPassing.cardNumber = "5123456789012346"
    paymentParamForPassing.cvv = "123"
    paymentParamForPassing.subventionAmount = "3000"
    ```
    ```objectivec Objective-C
        self.paymentParamForPassing.bankCode = @"EMI03";//BankCode
        self.paymentParamForPassing.expiryYear = @"2019";
        self.paymentParamForPassing.expiryMonth = @"12";
        self.paymentParamForPassing.nameOnCard = @"test";
        self.paymentParamForPassing.cardNumber = @"5123456789012346";
        self.paymentParamForPassing.CVV = @"123";

        self.paymentParamForPassing.subventionAmount = @"3000";
    ```

    2. Get the request by using the`createRequestWithPaymentParam` method as follows:

    ```swift Swift
    createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_EMI, withCompletionBlock: { request, postParam, error in
        if error == nil {
            //It is good to go state. You can use request parameter in webview to open Payment Page
        } else {
            //Something went wrong with Parameter, error contains the error Message string
        }
    })
    ```
    ```objectivec Objective-C
    Get the request by using createRequestWithPaymentParam method as follows:
    ```

    <Callout icon="📘" theme="info">
      **Hashing algorithm of a subvention transaction**: If subventionAmount is passed, the hash formula for payment hash will be similar to the following algorithm: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|SubventionAmount)`
    </Callout>
  </Accordion>

  <Accordion title="Fetch a List of No-Cost EMI-supporting banks" icon="fa-code">
    Pass the value for the subventionEligibility parameter as "all" in the Fetch Payment Option WebService. For more information refer to Web Services for Core.
  </Accordion>
</Accordion>

<Accordion title="LazyPay BNPL Integration" icon="fa-code">
  To pay using LazyPay (BNPL), perform the following steps.

  1. Set the Notify URL to the HTTPS Callback URL of the merchant where notification of transaction status will be sent on completion of a transaction.

  ```swift Swift
  paymentParamForPassing.notifyURL = "https://notifyURL.com"
  ```
  ```objectivec Objective-C
  self.paymentParamForPassing.notifyURL= @"https://notifyURL.com";
  ```

  2. Get the request by using the`createRequestWithPaymentParam` method as follows:

  ```swift Swift
  reateRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_LAZYPAY, withCompletionBlock: { request, postParam, error in
  if error == nil {
  //It is good to go. You can use request parameter in webview to open Payment Page
  } else {
  //Something went wrong with Parameter, error contains the error Message string
  }
  })
  ```
  ```objectivec Objective-C
      self.createRequest = [PayUCreateRequest new];

      [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_LAZYPAY withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
          //It is good to go. You can use request parameter in webview to open Payment Page
        }
        else{
          //Something went wrong with Parameter, error contains the error Message string
        }
      }];
  ```
</Accordion>

<Accordion title="TWID Pay BNPL Integration" icon="fa-code">
  To pay using TWID Pay:

  1. Create the post data with `CASH_CARD_TWID`:

  ```swift Swift
  paymentParamForPassing.bankCode = CASH_CARD_TWID //BankCode
  ```
  ```objectivec Objective-C
  self.paymentParamForPassing.bankCode = CASH_CARD_TWID;//BankCode
  ```

  2. Get the Twid customer hash in the `field5` param of PayuResponse, which can be used in the next transactions to skip authentication.

  ```swift Swift
  paymentParamForPassing.twidCustomerHash = "Twid customer hash"
  ```
  ```objectivec Objective-C
      self.paymentParamForPassing.twidCustomerHash = @"Twid customer hash";
    
  ```
</Accordion>

<Accordion title="Pluxee Card Integration" icon="fa-code">
  To pay using Pluxee card:

  1. Create the post data with the`PAYMENT_PG_SODEXO `:

  ```swift Swift
  self.paymentParamForPassing.cardNumber = "<Sodexo card number>";//cardNumber
  self.paymentParamForPassing.nameOnCard = "name";//Name on card
  self.paymentParamForPassing.expYear = "2018";//Expiry year
  self.paymentParamForPassing.expMonth = "11";//ExpiryMonth
  self.paymentParamForPassing.CVV = "123";//CVV
  self.paymentParamForPassing.shouldSaveCard = true;//If you want to save card then pass it otherwise it will not save 
  ```
  ```objectivec Objective-C
      self.paymentParamForPassing.cardNumber = @"<Sodexo card number>";//cardNumber
      self.paymentParamForPassing.nameOnCard = @"name";//Name on card
      self.paymentParamForPassing.expYear = @"2018";//Expiry year
      self.paymentParamForPassing.expMonth = @"11";//ExpiryMonth
      self.paymentParamForPassing.CVV = @"123";//CVV
      self.paymentParamForPassing.shouldSaveCard = YES;//If you want to save card then pass it otherwise it will not save 
  ```

  2. Get the request by using the`createRequestWithPaymentParam` method similar to the following code snippet:

  ```swift Swift
  createRequest().createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_SODEXO, withCompletionBlock: { request, postParam, error in
      if error == nil {
          //It is good to go state. You can use request parameter in webview to open Payment Page
      } else {
          //Something went wrong with Parameter, error contains the error Message string
      }
  })
  ```
  ```objectivec Objective-C
          self.createRequest = [PayUCreateRequest new];
          [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_SODEXO withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
          if (error == nil) {
          //It is good to go state. You can use request parameter in webview to open Payment Page
          }
          else{
          //Something went wrong with Parameter, error contains the error Message string
          }
      }];
  ```

  The successful or failed payment response is sent by PayU.

  3. Get the Sodexo source id in the field3 param of PayuResponse, which can be used to show and get stored Sodexo card details and also can be used for initiating payment.

  ```swift Swift
      self.paymentParamForPassing.sodexoSourceId = "<Sodexo source id>"
  ```
  ```c Objective-C
      self.paymentParamForPassing.sodexoSourceId = @"<Sodexo source id>";
      
  ```

  <br />
</Accordion>

## Test the integration and Go-Live

<IOS_Test_the_Integration />

<IOS_Go_Live />
