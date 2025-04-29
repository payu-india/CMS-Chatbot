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
This section provides a reference for the following Web Service APIs for Android Core SDK. Before you integrate these APIs, you must follow [Step 1](#step-1-initialise-merchant-web-service) and [Step 2](#step-2-create-merchant-web-service-postdata) of this section.

* [Enable Payment Options](https://docs.payu.in/docs/android-coresdk-enable-payment-options)
* [Get Checkout Details API](https://docs.payu.in/docs/android-coresdk-get-checkout-details)
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

## Step 1: Initialise web service

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
