---
title: 1. SDK Integration
excerpt: Build a custom payment flow integration for your Android app
deprecated: false
hidden: false
metadata:
  title: Integrate Android Android Core SDK
  description: >-
    This document provides a step-by-step guide on integrating Android Core SDK
    to enable payment methods into your app, including creating a PayU account,
    including the SDK in your app build.gradle, building payment parameters,
    generating hashes, and generating requests for various payment methods such
    as credit/debit cards, net banking, EMI, UPI, LazyPay, TwidPay, Sodexo, and
    more.
  keywords:
    - Android Core SDK Integration Steps
    - PayU Android SDK integration steps
    - Mobile payment integration with PayU Android SDK steps
    - PayU Android Core set up for Mobile
    - Android CheckoutPro SDK integration steps
    - Mobile Android SDK Basic Integration with Core
  robots: index
next:
  description: ''
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. PayU enable Cards, UPI, and other payment methods by default, and it is recommend edthat you enable other payment methods that are relevant to you.

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

***

## Step 2: Include the SDK in your app build.gradle

> ❗️ Move to Maven Central
>
> PayU has moved to Maven Central, Please update your existing dependency using the following configuration:
>
> ```Text build.gradle
> api 'in.payu:payu-sdk:7.8.0'
> ```

## Step 3: Build the Payment Parameters

Create an object of PaymentParams, put all the obtained parameters in it by using its default set methods and setHash to paymentHash.

```Text Java
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
```Text Kotlin
```

> * Transaction ID should be kept unique for each transaction and not more than 25 characters.
> * udf1 to udf5 are options params where you can pass additional information related to transaction. If you don't want to use it, then send them as empty string like, udf1=""
> * Email and First name can be empty strings "" if you don't want to use them
> * For store user card feature\
>   /\**These are used for store card feature. If you are not using it then user\_credentials = "default"* user *credentials takes of the form like user\_credentials = "merchant\_key : user\_id"* here merchant *key = your merchant key,* user\_id = unique id related to user like, email, phone number, etc.\_/
> * For SURL ,Success url is where the transaction response is posted by PayU on successful transaction.PayU recommends you to design or use your own surl and furl after testing is completed. See Handling SURL and FURL.
> * For FURL, Failure url is where the transaction response is posted by PayU on failed transaction. PayU recommends you to design or use your own surl and furl after testing is completed. See Handling SURL and FURL.
> * For offers `mPaymentParams.setOfferKey`("your\_offer\_key")
> * For any other payment default param (like phone and others) mPaymentParams.setPhone("your\_number")

## Step 4: Hash generation

> 📘 Generate Hash from Server
>
> It is recommended to generate hash from server only. Keep your key and salt in server side hash generation code. For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

The following approach for generating hash is not recommended. However, this approach can be used to test in PRODUCTION\_ENV

* if your server-side hash generation code is not completely setup. While going live, this approach for hash generation
* should not be used.

```
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

        // checksum for payemnt related details
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

## Step 5: Generate request for payment

### Credit / Debit Card

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

```Text Java
 try {
         mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CC).getPaymentPostParams();
      } catch (Exception e) {
            e.printStackTrace();
     }
```

### Store Credit / Debit card

To Pay using StoredCard, perform the following steps.

1. Set the StoredCard parameter similar to the following code snippet:

```Text Java
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

```Text Java
 try {
         mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CC).getPaymentPostParams();
      } catch (Exception e) {
            e.printStackTrace();
     }
```

### Tokenization

#### Card Tokenization with PayU

1. For Cards tokenized with PayU platform merchant needs to pass the below parameters.

```Text Java
mPaymentParams.setCvv(cvv); // pass the correct cvv
mPaymentParam.setCardToken(cardtoken); // pass the store card token
mPaymentParams.setCardTokenType(0); //it should be passed as 0
```

2. After setting the above parameters, you can get the request by using the`createRequestWithPaymentParam`.

#### Third Party-Card Tokenization

1. For cards tokenized outside the PayU platform merchant needs to pass the below parameters.

```Text Java
mPaymentParams.setCardTokenType(1); //it should be passed as 1
TokenizedCardAdditionalParam additionalParam = new TokenizedCardAdditionalParam();
additionalParam.setLast4Digits("1234"); //last 4 digits of card
additionalParam.setTavv("1234"); //tavv -> will be given by tokenisation partner
additionalParam.setTrid("1234"); //trid -> will be given by tokenisation partner
additionalParam.setTokenRefNo("1234"); //tokenRefNo -> will be given by tokenisation partner
mPaymentParams.setTokenizedCardAdditionalParam(additionalParam);
```

2. After setting the above parameters, you can get the request by using the`createRequestWithPaymentParam`.

### Net Banking

To pay using NetBanking, perform the following steps.

1. Set the NetBanking parameter as follows:

```Text Java
mPaymentParams.setBankCode(bankCode);
```

2. Get the request by using the `PaymentPostParams` method as follows:

```Text Java
try {
            mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.NB).getPaymentPostParams();
        } catch (Exception e) {
            e.printStackTrace();
        }
```

### Recurring Payments in NetBanking

For recurring payments in Net Banking, you need to collect the following details:

```Text Java
BeneficiaryDetails beneficiaryDetails = new BeneficiaryDetails();
beneficiaryDetails.setBeneficiaryName("John Doe");
beneficiaryDetails.setBeneficiaryAccountNumber("51234567890");
beneficiaryDetails.setBeneficiaryAccountType(BeneficiaryAccountType.SAVINGS);
beneficiaryDetails.setBeneficiaryIfsc("ICIC0006621")
SIParams siParams = new SIParams();
siParams.setBeneficiarydetail(beneficiaryDetails);
```

### Beneficiary Details Parameters Definition

| Parameter                  | Description                                                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Beneficiary Name           | `String` Account Holder Beneficiary name.                                                                            |
| Beneficiary Account Number | `String` Account number of Beneficiary.                                                                              |
| Beneficiary Account Type   | `Enum of BeneficiaryAccountType` Accepted values are BeneficiaryAccountType.SAVINGS, BeneficiaryAccountType.CURRENT. |
| Beneficiary IFSC           | `String` Valid IFSC.                                                                                                 |

### EMI

To pay using EMI, perform the following steps.

1. Set the EMI parameter for instance:

```Text Java
mPaymentParams.setCardNumber(“5123456789012346”); 
mPaymentParams.setNameOnCard(“test”); 
mPaymentParams.setExpiryMonth(“06”); 
mPaymentParams.setExpiryYear(“2023”); 
mPaymentParams.setCvv(“123”); 
mPaymentParams.setBankCode(“EMI03”); 
```

2. Get the request by using the `PaymentPostParams` method as follows:

```
try {
     mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.EMI).getPaymentPostParams();
    } catch (Exception e) {
      e.printStackTrace();
   }
```

### Cardless EMI

For doing CardLess EMI transactions, `setCardLess `must be set to true along with setting the bank code in the payment parameters similar to the following code snippet:

```Text Java
mPaymentParams.setBankCode("ZESTMON"); //For Zestmoney CardLess EMI
```

For the Zestmoney CardLess EMI transactions, the phone number must also be set in payment parameters similar to the following code snippet:

```Text Java
mPaymentParams.setPhone("9000000000");
```

2. Get the request by using the `PaymentPostParams` method as follows:

```
try {
     mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.EMI).getPaymentPostParams();
    } catch (Exception e) {
      e.printStackTrace();
   }
```

### No-Cost EMI

For posting No-Cost EMI transactions, the subvention amount needs to be sent along with the above EMI parameters similar to the following code snippet:

```Text Java
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

#### Fetch a List of No-Cost EMI-supporting banks

To get a list of No-Cost EMI supporting banks, pass var2 as “all” in the Merchant Web Service for GetPaymentRelatedDetailsTask. For more information refer to [Web Services for Core](doc:ios-coresdk-web-services).

### Cash card

To pay using a CashCard, perform the following steps

1. Set the cashcard parameter as follows:

```Text Java
mPaymentParams.setBankCode(bankCode);
```

2. Get the request by using the `PaymentPostParams` method as follows:

```Text Java
 try {
            mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.CASH).getPaymentPostParams();
        } catch (Exception e) {
            e.printStackTrace();
        }
```

### UPI

To pay using a UPI, perform the following steps

1. Set the VPA parameter as follows:

```Text Java
mPaymentParams.setVpa(virtualPaymentAddress);
```

You need to validate the following for the virtual payment address (VPA):

* VPA length should be less than or equal to 50 characters
* Regex for VPA: value.match(/^(\[A-Za-z0-9.])+@\[A-Za-z0-9]+$/)

2. Get the request by using the `PaymentPostParams` method as follows:

```
try {
     mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.UPI).getPaymentPostParams();
   } catch (Exception e) {
     e.printStackTrace();
 }
```

### LazyPay

To pay using LazyPay, perform the following steps.

1. Notify(callback) the URL of the merchant where notification of transaction status will be sent on completion of the transaction. It should be HTTPS.

```Text Java
mPaymentParams.setNotifyURL(<Merchant Callback Url>);
```

2. Get the request by using the `PaymentPostParams` method as follows:

```Text Java
try{
    mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.LAZYPAY).getPaymentPostParams();
     }
    catch (Exception e){
      e.printStackTrace(); 
}
```

### TwidPay

1. To Pay using TwidPay, create the post data with PayuConstants.PAY\_BY\_REWARDS.

```
 try {
           mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.PAY_BY_REWARDS).getPaymentPostParams();
        }        } catch (Exception e) {
            e.printStackTrace();

```

2. After a successful payment, you will get the Twid customer hash in field5 params of PayuResponse, which would use for the next transaction to skip authentication.

```Text Java
mPaymentParams.setTwidCustomerHash("Twid customer hash");
```

### Sodexo

1. To pay using Sodexo, create the post data with PAYMENT\_PG\_SODEXO:

```Text Java
mPaymentParams.setCardNumber(cardNumber);
mPaymentParams.setCardName(cardName);
mPaymentParams.setNameOnCard(cardholderName);
mPaymentParams.setExpiryMonth(expiryMonth);// MM
mPaymentParams.setExpiryYear(expiryYear);// YYYY  
mPaymentParams.setCvv(cvv);
```

2. After setting the above parameters, you can get the request by using the`PaymentPostParams` method similar to the following code snippet:

```
  try {
            mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.SODEXO).getPaymentPostParams();
        } catch (Exception e) {
            e.printStackTrace();
        }
```

After a successful payment, you would get the Sodexo source ID in the field3 param of PayU response, which can be used to show and get stored Sodexo card details and also can be used for initiating payment.

```Text Java
mPaymentParams.setsodexoSourceId("srcid123");
```