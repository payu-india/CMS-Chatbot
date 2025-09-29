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
### Step 1: Initialise web service

Create an object of MerchantWebService with any of the supported API commands.

```Text JAVA
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey); // Merchant key
merchantWebService.setCommand(<Api Commands>); // Pass the command name
merchantWebService.setVar1(<Pass var 1 value>) // Pass the var1 calue
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

For more information on Web Service hash generation, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

> 📘 Generate Hash for MerchantWebService
>
> To generate Hash refer to Hash Generation.
>
> **Formula** :-sha512(key|command|var1|salt)
>
> where
>
> key= "Your Key"
>
> command= \<"Api Commands"> // Pass Command Name
>
> var1= \<"default"> // Pass the var1 value
>
> salt= "Your SALT"

## Step 2: Create Merchant web service PostData

```Text JAVA
PostData postData = new MerchantWebServicePostParams(merchantWebService).getMerchantWebServicePostParams();
if (postData.getCode() == PayuErrors.NO_ERROR) {
payuConfig.setData(postData.getResult());
}
```

> 📘 Troubleshoot Postdata code errors
>
> If the PostData code snippet (above) is returning errors, check the data point set in merchantWebService.

## Commands

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


## Enable Payment Options

This API is used enable multiple payment options on your checkout page.

<Callout icon="📘" theme="info">
  **Hash logic**: The hash logic for this API is:

  `<key>|payment_related_details_for_mobile_sdk|<userCredential>|<salt>`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).
</Callout>

### Step 1: Execute GetPaymentRelatedDetailsTask

This class is used to get payment-related details. It takes an instance of a class that implements the `PaymentRelatedDetailsListener` interface as input.

```node Node
GetPaymentRelatedDetailsTask paymentRelatedDetailsForMobileSdkTask = new GetPaymentRelatedDetailsTask(this);
```

The `PaymentRelatedDetailsListener` interface has an abstract method called `onPaymentRelatedDetailsResponse()`. This method is called when the payment-related details are received.

### Step 2: Get Response using onPaymentRelatedDetailsResponse()

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

## Get Checkout Details API

<br />

* [Lookup API](https://docs.payu.in/docs/lookup-api-web-service-android-core-sdk)
* [VAS API](https://docs.payu.in/docs/vas-api-android-core-sdk)
* [Eligible Bins for EMI API](https://docs.payu.in/docs/eligible-bins-for-emi-api-android-core-sdk)
* [Get EMI According to Interest API](https://docs.payu.in/docs/get-emi-according-to-interest-api-android-core-sdk)
* [Get Transaction Info API](https://docs.payu.in/docs/get-transaction-info-api-android-core-sdk)
* [Verify Payment API](https://docs.payu.in/docs/verify-payment-api-android-core-sdk)
* [Get BIN Info API](https://docs.payu.in/docs/get-bin-info-api-android-core-sdk)
* [Get Card Information API](https://docs.payu.in/docs/get-card-information-api-android-core-sdk)
* [Offer APIs](https://docs.payu.in/docs/offer-apis-android-core-sdk)
* [Check Balance API](https://docs.payu.in/docs/check-balance-api-android-core-sdk)
* [Tokenized Payment APIs](https://docs.payu.in/docs/tokenized-payment-android-core-sdk)

***

