---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps - Android Core SDK
  description: ''
  keywords:
    - Integration Steps - Android Core SDK
    - ' Android Core SDK Integration Steps'
    - ' Integrate Android Core SDK'
    - Android Core SDK Integration
  robots: index
next:
  description: ''
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. PayU enable Cards, UPI, and other payment methods by default, and it is recommended that you enable other payment methods that are relevant to you.

### Steps to integrate

<Cards columns={3}>
  <Card title="Step 1: Create a PayU account" href="#step-1-create-a-payu-account">
    Register for a merchant account on the PayU Dashboard and enable the payment methods you want to offer.
  </Card>
  <Card title="Step 2: Include the SDK in your app build.gradle" href="#step-2-include-the-sdk-in-your-app-buildgradle">
    Add the PayU Core SDK Maven Central dependency (`in.payu:payu-sdk`) to your app’s `build.gradle`.
  </Card>
  <Card title="Step 3: Build the Payment Parameters" href="#step-3-build-the-payment-parameters">
    Create a `PaymentParams` object with key, txnId, amount, surl, furl, udf fields, and other transaction details.
  </Card>
  <Card title="Step 4: Hash generation" href="#step-4-hash-generation">
    Generate payment hashes on your server and populate `PayuHashes` before launching the SDK UI.
  </Card>
  <Card title="Step 5: Generate request for payment" href="#step-5-generate-request-for-payment">
    Set payment-mode-specific fields (card, UPI, net banking, EMI, etc.) and build the request with `PaymentPostParams`.
  </Card>
  <Card title="Test the Integration and Go-Live" href="#test-the-integration-and-go-live">
    Run sandbox test transactions, then switch to production keys and complete the go-live checklist.
  </Card>
</Cards>

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Step 2: Include the SDK in your app build.gradle

<Callout icon="❗️" theme="error">
  ### Move to Maven Central

  PayU has moved to Maven Central, Please update your existing dependency using the following configuration:

  ```Text build.gradle
  api 'in.payu:payu-sdk:7.12.3'
  ```
</Callout>

## Step 3: Build the Payment Parameters

Create an object of PaymentParams, put all the obtained parameters in it by using its default set methods and setHash to paymentHash.

<Accordion title="PaymentParams object" icon="fa-code">
  ```java
  PaymentParams mPaymentParams = new PaymentParams();
  mPaymentParams.setKey(merchantKey);
  mPaymentParams.setTxnId("" + System.currentTimeMillis());
  mPaymentParams.setAmount(amount);
  mPaymentParams.setProductInfo("product_info");
  mPaymentParams.setFirstName("TEST");
  mPaymentParams.setEmail("xyz@gmail.com");
  mPaymentParams.setPhone(phoneNumber);
  mPaymentParams.setUserCredentials(userCredentials);
  mPaymentParams.setSurl("https://cbjs.payu.in/sdk/success");
  mPaymentParams.setFurl("https://cbjs.payu.in/sdk/failure");
  mPaymentParams.setNotifyURL(mPaymentParams.getSurl());  //for lazy pay
  mPaymentParams.setUdf1("udf1");
  mPaymentParams.setUdf2("udf2");
  mPaymentParams.setUdf3("udf3");
  mPaymentParams.setUdf4("udf4");
  mPaymentParams.setUdf5("udf5");
  mPaymentParams.setOfferKey("YONOYSF@6445");
  mPaymentParams.setHash("<pass the payment Hash>");

  ```
</Accordion>

> - Transaction ID should be kept unique for each transaction and not more than 25 characters.
> - udf1 to udf5 are options params where you can pass additional information related to transaction. If you don't want to use it, then send them as empty string like, udf1=""
> - Email and First name can be empty strings "" if you don't want to use them
> - For store user card feature
>   /\*_These are used for store card feature. If you are not using it then user\_credentials = "default"_ user _credentials takes of the form like user\_credentials = "merchant\_key : user\_id"_ here merchant _key = your merchant key,_ user\_id = unique id related to user like, email, phone number, etc.\_/
> - For SURL ,Success url is where the transaction response is posted by PayU on successful transaction.PayU recommends you to design or use your own surl and furl after testing is completed. See Handling SURL and FURL.
> - For FURL, Failure url is where the transaction response is posted by PayU on failed transaction. PayU recommends you to design or use your own surl and furl after testing is completed. See Handling SURL and FURL.
> - For offers `mPaymentParams.setOfferKey`("your\_offer\_key")
> - For any other payment default param (like phone and others) mPaymentParams.setPhone("your\_number")

## Step 4: Hash generation

<Callout icon="📘" theme="info">
  ### Generate Hash from Server

  It is recommended to generate hash from server only. Keep your key and salt in server side hash generation code. For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
</Callout>

The following approach for generating hash is not recommended. However, this approach can be used to test in PRODUCTION\_ENV

- if your server-side hash generation code is not completely setup. While going live, this approach for hash generation
- should not be used.

<Accordion title="Hash generation code" icon="fa-code">
  ```java
  /******************************
   * Client hash generation
   ***********************************/
  // Do not use this, you may use this only for testing.
  // lets generate hashes.
  // This should be done from server side..
  // Do not keep salt anywhere in app.
  ```

Create an object of class `PayuHashes` and set the corresponding hashes using the default set methods provided

```
    public void generateHashFromSDK(PaymentParams mPaymentParams, String salt) {
        PayuHashes payuHashes = new PayuHashes();
        PostData postData = new PostData();
//        if(mPaymentParams.getBeneficiaryAccountNumber()== null){
        // payment Hash;
        checksum = null;
        checksum = new PayUChecksum();
        checksum.setAmount(mPaymentParams.getAmount());
        checksum.setKey(mPaymentParams.getKey());
        checksum.setTxnid(mPaymentParams.getTxnId());
        checksum.setEmail(mPaymentParams.getEmail());
        checksum.setSalt(salt);
        checksum.setProductinfo(mPaymentParams.getProductInfo());
        checksum.setFirstname(mPaymentParams.getFirstName());
        checksum.setUdf1(mPaymentParams.getUdf1());
        checksum.setUdf2(mPaymentParams.getUdf2());
        checksum.setUdf3(mPaymentParams.getUdf3());
        checksum.setUdf4(mPaymentParams.getUdf4());
        checksum.setUdf5(mPaymentParams.getUdf5());
        StringBuilder beneficiarydetail = new StringBuilder();
        beneficiarydetail.append("{"+"\""+PayuConstants.BENEFICIARY_ACCOUNT_NUMBER+"\""+":"+"\""+mPaymentParams.getBeneficiaryAccountNumber()+"\"");
        beneficiarydetail.append(","+"\""+PayuConstants.IFSC_CODE+"\""+":"+"\""+mPaymentParams.getIfscCode()+"\"");
        beneficiarydetail.append("}");
      
        postData = checksum.getHash();
        if (postData.getCode() == PayuErrors.NO_ERROR) {
            payuHashes.setPaymentHash(postData.getResult());
        }

        if (mPaymentParams.getSubventionAmount() != null && !mPaymentParams.getSubventionAmount().isEmpty()){
            subventionHash = calculateHash(""+mPaymentParams.getKey()+"|"+mPaymentParams.getTxnId()+"|"+mPaymentParams.getAmount()+"|"+mPaymentParams.getProductInfo()+"|"+mPaymentParams.getFirstName()+"|"+mPaymentParams.getEmail()+"|"+mPaymentParams.getUdf1()+"|"+mPaymentParams.getUdf2()+"|"+mPaymentParams.getUdf3()+"|"+mPaymentParams.getUdf4()+"|"+mPaymentParams.getUdf5()+"||||||"+salt+"|"+mPaymentParams.getSubventionAmount());
        }
        if (mPaymentParams.getSiParams()!=null){
            siHash = calculateHash(""+mPaymentParams.getKey()+"|"+mPaymentParams.getTxnId()+"|"+mPaymentParams.getAmount()+"|"+mPaymentParams.getProductInfo()+"|"+mPaymentParams.getFirstName()+"|"+mPaymentParams.getEmail()+"|"+mPaymentParams.getUdf1()+"|"+mPaymentParams.getUdf2()+"|"+mPaymentParams.getUdf3()+"|"+mPaymentParams.getUdf4()+"|"+mPaymentParams.getUdf5()+"||||||"+prepareSiDetails()+"|"+salt);
        }
        if (beneficiarydetail!=null && beneficiarydetail.length()!=0 ){
            tpvHash  = calculateHash(""+mPaymentParams.getKey()+"|"+mPaymentParams.getTxnId()+"|"+mPaymentParams.getAmount()+"|"+mPaymentParams.getProductInfo()+"|"+mPaymentParams.getFirstName()+"|"+mPaymentParams.getEmail()+"|"+mPaymentParams.getUdf1()+"|"+mPaymentParams.getUdf2()+"|"+mPaymentParams.getUdf3()+"|"+mPaymentParams.getUdf4()+"|"+mPaymentParams.getUdf5()+"||||||"+beneficiarydetail.toString()+"|"+salt);

        }
        /*}

        else {
            String hashString = merchantKey + "|" + mPaymentParams.getTxnId() + "|" + mPaymentParams.getAmount() + "|" + mPaymentParams.getProductInfo() + "|" + mPaymentParams.getFirstName() + "|" + mPaymentParams.getEmail() + "|" + mPaymentParams.getUdf1() + "|" + mPaymentParams.getUdf2() + "|" + mPaymentParams.getUdf3() + "|" + mPaymentParams.getUdf4() + "|" + mPaymentParams.getUdf5() + "||||||{\"beneficiaryAccountNumber\":\"" +mPaymentParams.getBeneficiaryAccountNumber()+ "\"}|" + salt;

            paymentHash1 = calculateHash(hashString);
            payuHashes.setPaymentHash(paymentHash1);



        }*/

        // checksum for payment related details
        // var1 should be either user credentials or default
        String var1 = mPaymentParams.getUserCredentials() == null ? PayuConstants.DEFAULT : mPaymentParams.getUserCredentials();
        String key = mPaymentParams.getKey();

        if ((postData = calculateHash(key, PayuConstants.PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK, var1, salt)) != null && postData.getCode() == PayuErrors.NO_ERROR) // Assign post data first then check for success
            payuHashes.setPaymentRelatedDetailsForMobileSdkHash(postData.getResult());
        //vas
        if ((postData = calculateHash(key, PayuConstants.VAS_FOR_MOBILE_SDK, PayuConstants.DEFAULT, salt)) != null && postData.getCode() == PayuErrors.NO_ERROR)
            payuHashes.setVasForMobileSdkHash(postData.getResult());

        // getIbibocodes
        if ((postData = calculateHash(key, PayuConstants.GET_MERCHANT_IBIBO_CODES, PayuConstants.DEFAULT, salt)) != null && postData.getCode() == PayuErrors.NO_ERROR)
            payuHashes.setMerchantIbiboCodesHash(postData.getResult());

        if (!var1.contentEquals(PayuConstants.DEFAULT)) {
            // get user card
            if ((postData = calculateHash(key, PayuConstants.GET_TOKENISED_USER_CARD, var1, salt)) != null && postData.getCode() == PayuErrors.NO_ERROR) // todo rename storedc ard
                payuHashes.setStoredCardsHash(postData.getResult());
           // delete user card
            if ((postData = calculateHash(key, PayuConstants.DELETE_TOKENISED_USER_CARD, var1, salt)) != null && postData.getCode() == PayuErrors.NO_ERROR)
                payuHashes.setDeleteCardHash(postData.getResult());
        }

        // we have generated all the hases now lest launch sdk's ui
        launchSdkUI(payuHashes);
    }

```

```
PayuHashes payuHashes = new PayuHashes();
payuHashes.setPaymentRelatedDetailsForMobileSdkHash();
payuHashes.setVasForMobileSdkHash();
payuHashes.setMerchantIbiboCodesHash();
payuHashes.setStoredCardsHash();
payuHashes.setDeleteCardHash();
payuHashes.setPaymentHash();
mPaymentParams.setHash(payuHashes.getPaymentHash());
```

</Accordion>

## Step 5: Generate request for payment

<Accordion title="Credit / Debit Card" icon="fa-code">
  To pay using a credit card or debit card, perform the following steps.

  1. Set the following credit card parameters:

  ```Text Java
  mPaymentParams.setCardNumber(cardNumber);
  mPaymentParams.setCardName(cardName);
  mPaymentParams.setNameOnCard(cardholderName);
  mPaymentParams.setExpiryMonth(expiryMonth);// MM
  mPaymentParams.setExpiryYear(expiryYear);// YYYY
  mPaymentParams.setCvv(cvv);
  ```

  2. Get the request by using the `createRequestWithPaymentParam` method as follows:

  ```java
   try {
           mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CC).getPaymentPostParams();
        } catch (Exception e) {
              e.printStackTrace();
       }
  ```
</Accordion>

<Accordion title="Store Credit / Debit card" icon="fa-code">
  To Pay using StoredCard, perform the following steps.

  1. Set the StoredCard parameter similar to the following code snippet:

  ```java
  mPaymentParams.setCardNumber(cardNumber);
  mPaymentParams.setCardName(cardName);
  mPaymentParams.setNameOnCard(cardholderName);
  mPaymentParams.setExpiryMonth(expiryMonth);// MM
  mPaymentParams.setExpiryYear(expiryYear);// YYYY
  mPaymentParams.setCvv(cvv);
   
  mPaymentParam.setUserCredentials(userCredentials);
  mPaymentParam.setStoreCard(1);
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
   try {
           mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CC).getPaymentPostParams();
        } catch (Exception e) {
              e.printStackTrace();
       }
  ```
</Accordion>

<Accordion title="Tokenization" icon="fa-code">
  <Accordion title="Card Tokenization with PayU" icon="fa-code">
    1. For Cards tokenized with PayU platform merchant needs to pass the below parameters.

    ```javsa
    mPaymentParams.setCvv(cvv); // pass the correct cvv
    mPaymentParam.setCardToken(cardtoken); // pass the store card token
    mPaymentParams.setCardTokenType(0); //it should be passed as 0
    ```

    2. After setting the above parameters, you can get the request by using the`createRequestWithPaymentParam`.
  </Accordion>

  <Accordion title="Third Party-Card Tokenization" icon="fa-code">
    1. For cards tokenized outside the PayU platform merchant needs to pass the below parameters.

    ```java
    mPaymentParams.setCardTokenType(1); //it should be passed as 1
    TokenizedCardAdditionalParam additionalParam = new TokenizedCardAdditionalParam();
    additionalParam.setLast4Digits("1234"); //last 4 digits of card
    additionalParam.setTavv("1234"); //tavv -> will be given by tokenisation partner
    additionalParam.setTrid("1234"); //trid -> will be given by tokenisation partner
    additionalParam.setTokenRefNo("1234"); //tokenRefNo -> will be given by tokenisation partner
    mPaymentParams.setTokenizedCardAdditionalParam(additionalParam);
    ```

    2. After setting the above parameters, you can get the request by using the`createRequestWithPaymentParam`.
  </Accordion>
</Accordion>

<Accordion title="Net Banking" icon="fa-code">
  To pay using NetBanking, perform the following steps.

  1. Set the NetBanking parameter as follows:

  ```java
  mPaymentParams.setBankCode(bankCode);
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
  try {
              mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.NB).getPaymentPostParams();
          } catch (Exception e) {
              e.printStackTrace();
          }
  ```
</Accordion>

<Accordion title="Recurring Payments in NetBanking" icon="fa-code">
  For recurring payments in Net Banking, you need to collect the following details:

  ```java
  BeneficiaryDetails beneficiaryDetails = new BeneficiaryDetails();
  beneficiaryDetails.setBeneficiaryName("John Doe");
  beneficiaryDetails.setBeneficiaryAccountNumber("51234567890");
  beneficiaryDetails.setBeneficiaryAccountType(BeneficiaryAccountType.SAVINGS);
  beneficiaryDetails.setBeneficiaryIfsc("ICIC0006621")
  SIParams siParams = new SIParams();
  siParams.setBeneficiarydetail(beneficiaryDetails);
  ```
</Accordion>

<Accordion title="Beneficiary Details Parameters Definition" icon="fa-code">
  | Parameter                  | Description                                                                                                          |
  | :------------------------- | :------------------------------------------------------------------------------------------------------------------- |
  | Beneficiary Name           | `String` Account Holder Beneficiary name.                                                                            |
  | Beneficiary Account Number | `String` Account number of Beneficiary.                                                                              |
  | Beneficiary Account Type   | `Enum of BeneficiaryAccountType` Accepted values are BeneficiaryAccountType.SAVINGS, BeneficiaryAccountType.CURRENT. |
  | Beneficiary IFSC           | `String` Valid IFSC.                                                                                                 |
</Accordion>

<Accordion title="EMI" icon="fa-code">
  To pay using EMI, perform the following steps.

  1. Set the EMI parameter for instance:

  ```java
  mPaymentParams.setCardNumber(“5123456789012346”); 
  mPaymentParams.setNameOnCard(“test”); 
  mPaymentParams.setExpiryMonth(“06”); 
  mPaymentParams.setExpiryYear(“2023”); 
  mPaymentParams.setCvv(“123”); 
  mPaymentParams.setBankCode(“EMI03”); 
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
  try {
       mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.EMI).getPaymentPostParams();
      } catch (Exception e) {
        e.printStackTrace();
     }
  ```
</Accordion>

<Accordion title="Cardless EMI" icon="fa-code">
  For doing CardLess EMI transactions, `setCardLess `must be set to true along with setting the bank code in the payment parameters similar to the following code snippet:

  ```java
  mPaymentParams.setBankCode("ZESTMON"); //For Zestmoney CardLess EMI
  ```

  For the Zestmoney CardLess EMI transactions, the phone number must also be set in payment parameters similar to the following code snippet:

  ```java
  mPaymentParams.setPhone("9000000000");
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
  try {
       mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.EMI).getPaymentPostParams();
      } catch (Exception e) {
        e.printStackTrace();
     }
  ```
</Accordion>

<Accordion title="No-Cost EMI" icon="fa-code">
  For posting No-Cost EMI transactions, the subvention amount needs to be sent along with the above EMI parameters similar to the following code snippet:

  ```java
  mPaymentParams.setCardNumber(“5123456789012346”); 
  mPaymentParams.setNameOnCard(“test”); 
  mPaymentParams.setExpiryMonth(“06”); 
  mPaymentParams.setExpiryYear(“2023”); 
  mPaymentParams.setCvv(“123”); 
  mPaymentParams.setBankCode(“EMI03”); 
  mPaymentParams.setSubventionAmount(“4000”);
  ```

  > 📘 Hash Formula
  >
  > If the subvention amount is passed, the hash formula for payment hash will be similar to the following
  >
  > sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|SubventionAmount)

  <Accordion title="Fetch a List of No-Cost EMI-supporting banks" icon="fa-code">
    To get a list of No-Cost EMI supporting banks, pass var2 as “all” in the Merchant Web Service for GetPaymentRelatedDetailsTask. For more information refer to [Web Services for Core](doc:ios-coresdk-web-services).
  </Accordion>
</Accordion>

<Accordion title="Cash card" icon="fa-code">
  To pay using a CashCard, perform the following steps

  1. Set the cashcard parameter as follows:

  ```java
  mPaymentParams.setBankCode(bankCode);
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
   try {
              mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CASH).getPaymentPostParams();
          } catch (Exception e) {
              e.printStackTrace();
          }
  ```
</Accordion>

<Accordion title="UPI" icon="fa-code">
  To pay using a UPI, perform the following steps

  1. Set the VPA parameter as follows:

  ```java
  mPaymentParams.setVpa(virtualPaymentAddress);
  ```

  You need to validate the following for the virtual payment address (VPA):

  * VPA length should be less than or equal to 50 characters
  * Regex for VPA: value.match(/^(\[A-Za-z0-9.])+@\[A-Za-z0-9]+$/)

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
  try {
       mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.UPI).getPaymentPostParams();
     } catch (Exception e) {
       e.printStackTrace();
   }
  ```
</Accordion>

<Accordion title="LazyPay" icon="fa-code">
  To pay using LazyPay, perform the following steps.

  1. Notify(callback) the URL of the merchant where notification of transaction status will be sent on completion of the transaction. It should be HTTPS.

  ```java
  mPaymentParams.setNotifyURL(<Merchant Callback Url>);
  ```

  2. Get the request by using the `PaymentPostParams` method as follows:

  ```java
  try{
      mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.LAZYPAY).getPaymentPostParams();
       }
      catch (Exception e){
        e.printStackTrace(); 
  }
  ```
</Accordion>

<Accordion title="TwidPay" icon="fa-code">
  1. To Pay using TwidPay, create the post data with PayuConstants.PAY\_BY\_REWARDS.

```java
 try {
           mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.PAY_BY_REWARDS).getPaymentPostParams();
        }        } catch (Exception e) {
            e.printStackTrace();

```

2\. After a successful payment, you will get the Twid customer hash in field5 params of PayuResponse, which would use for the next transaction to skip authentication.

```java
mPaymentParams.setTwidCustomerHash("Twid customer hash");
```

</Accordion>

<Accordion title="Sodexo" icon="fa-code">
  1. To pay using Sodexo, create the post data with PAYMENT\_PG\_SODEXO:

  ```java
  mPaymentParams.setCardNumber(cardNumber);
  mPaymentParams.setCardName(cardName);
  mPaymentParams.setNameOnCard(cardholderName);
  mPaymentParams.setExpiryMonth(expiryMonth);// MM
  mPaymentParams.setExpiryYear(expiryYear);// YYYY  
  mPaymentParams.setCvv(cvv);
  ```

  2. After setting the above parameters, you can get the request by using the`PaymentPostParams` method similar to the following code snippet:

  ```java
    try {
              mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.SODEXO).getPaymentPostParams();
          } catch (Exception e) {
              e.printStackTrace();
          }
  ```

  After a successful payment, you would get the Sodexo source ID in the field3 param of PayU response, which can be used to show and get stored Sodexo card details and also can be used for initiating payment.

  ```java
  mPaymentParams.setsodexoSourceId("srcid123");
  ```
</Accordion>

## Test the Integration and Go-Live

<Accordion title="Test the Integration" icon="fa-code">
  After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

  You can make test payments using one of the payment methods configured at the Checkout.

  <UPIIntentCallout />

  <TestingChecklist />

  ***

  <TestCardsCallout />

  <Accordion title="Test credentials for supported payment methods" icon="fa-code">
    Following are the payment methods supported in PayU Test mode.
  </Accordion>

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
    > ❗️ Callout
    >
    > The UPI in-app and UPI intent flow is not available in the Test mode.

    You can use either of the following VPAs to test your UPI-related integration:

    * [anything@payu](anything@payu)
    * [9999999999@payu.in](mailto:9999999999@payu.in)

    For Testing the UPI Collect flow, Please follow the below steps:-

    1. Once you enter the VPA click on the verify button and proceed to pay.
    2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
    3. The below link opens in the browser Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.
       [https://pgsim01.payu.in/UPI-test-transaction/confirm/](https://pgsim01.payu.in/UPI-test-transaction/confirm/)\<Txn\_id>

    **For Android**

    You can add the below metadata under the application tag in the manifest file to test the UPI Collect flow on test env:-

    <Callout icon="🚧" theme="warn">
      **Remove code from manifest**: Ensure to remove the code from the manifest file before going live.
    </Callout>

    ```XML
    <application>
    <meta-data android:name="payu_debug_mode_enabled" android:value="true" /> // set the value to false for production environment
    <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" /> //Comment in case of Production-->
    <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/> //Comment in case of Production-->
    </appliction>
    ```

    <Accordion title="Test cards for EMI" icon="fa-code">
      You can use the following Debit and Credit cards to test EMI integration.

      <EMITestCards />
    </Accordion>

    <Accordion title="Test Wallets" icon="fa-code">
      You can use the following wallets and their corresponding credentials to test wallet integration.

      <EMITestWallets />
    </Accordion>
  </Accordion>
</Accordion>

<Go_Live_Checklist />

<br />
