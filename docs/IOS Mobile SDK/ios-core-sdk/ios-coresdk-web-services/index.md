---
title: Web Services for iOS Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This part of the document includes the following APIs for iOS Core SDK. Before you use the following APIs, initialise  the web service as described in [Initialise web service](#initialise-web-service).

* [Fetch Payment Options](https://docs.payu.in/docs/fetch-payment-options-ios-core-sdk)
* [VAS Integration](https://docs.payu.in/docs/vas-integration-ios-core-sdk)
* [Offer APIs](https://docs.payu.in/docs/offer-apis-ios-core-sdk)
* [Get EMI According to Interest API](https://docs.payu.in/docs/get-emi-according-to-interest-api-ios-core-sdk)
* [Verify Payment API](https://docs.payu.in/docs/verify-payment-ios-core-sdk)
* [Check Is Domestic API](https://docs.payu.in/docs/check-is-domestic-api-ios-core-sdk)
* [Get Transaction Info API](https://docs.payu.in/docs/get-transaction-info-api-ios-core-sdk)
* [Get Bin Info API](https://docs.payu.in/docs/get-bin-info-api-ios-core-sdk)
* [Get Checkout Details API](https://docs.payu.in/docs/get-checkout-details-api-ios-core-sdk)
* [Lookup API](https://docs.payu.in/docs/lookup-api-ios-core-sdk)
* [Check Pluxee Card Balance](https://docs.payu.in/docs/check-pluxee-card-balance-ios-core-sdk)
* [Tokenized Payments Integration](https://docs.payu.in/docs/tokenized-payments-integration-ios-core-sdk)

## Initialise web service

1. Create an object of the `PayUWebServiceResponse` class and call the respective methods. You will get the result in the completion handler of the method.

```Text Swift
 let webServiceResponse = PayUWebServiceResponse()
```
```Text Objective-C
PayUWebServiceResponse *webServiceResponse = [PayUWebServiceResponse new];
```

> 📘 Note:
>
> If there is an error in the parameters passed by the merchant, it will give the errorMessage string. Else, you will get the parsed object.

2. Handle the response

```
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

<br />

<br />

<br />

***
