---
title: Get EMI According to Interest API
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Get EMI According to Interest API - iOS Core SDK
  description: ''
  robots: index
---
The **Get EMI According to Interest** API helps you get details of all the available EMIs.

To integrate this API:

1. Set the amount in the payment parameter for this API as described in the following code block.

```swift Swift
self.paymentParamForPassing.amount = @"100"; self.paymentParamForPassing.hashes.EMIDetailsHash = @"hash";
```
```objectivec Objective-C
[webServiceResponse getOfferStatus:self.paymentParamForPassing withCompletionBlock:^(PayUModelOfferStatus *offerStatus, NSString *errorMessage, id extraParam) {
    if (errorMessage == nil) {
        //It is good to go & offerStatus.discount contains the discounted amount if there is any offer & offerStatus.msg contains the message why offer is not available
    }
    else{
        // Something went wrong errorMessage is having the Detail
    }
}];
```

2. Call the `getEMIAmountAccordingToInterest` method to integrate this API as described in the following code block:

```swift Swift
[webServiceResponse
getEMIAmountAccordingToInterest:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictEMIDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictEMIDetails is having the EMI detail
      }
    }];
```
```objectivec Objective-C
[webServiceResponse
getEMIAmountAccordingToInterest:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictEMIDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictEMIDetails is having the EMI detail
      }
    }];
```

***
