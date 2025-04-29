---
title: Stored Card Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Stored Card Integration - iOS Core SDK
  description: ''
  keywords:
    - iOS Stored Card Integration
    - ' Stored Card Integration for iOS Core SDK'
  robots: index
next:
  description: ''
---
To pay using a stored card, perform the following steps.

1. Set the stored card parameter similar to the following code snippet:

```Text Swift
let modelStoredCard = paymentRelatedDetail.storedCardArray[indexPath.row] as? PayUModelStoredCard

paymentParamForPassing.cardToken = modelStoredCard?.cardToken
paymentParamForPassing.cardBin = modelStoredCard?.cardBin
paymentParamForPassing.cvv = "123" //CVV
```
```Text Objective-C
    PayUModelStoredCard *modelStoredCard = [self.paymentRelatedDetail.storedCardArray objectAtIndex:indexPath.row];

    self.paymentParamForPassing.cardToken = modelStoredCard.cardToken;
    self.paymentParamForPassing.cardBin = modelStoredCard.cardBin;
    self.paymentParamForPassing.CVV = @"123";//CVV
```

2. Get the request by using the`createRequestWithPaymentParam` method similar to the following code snippet:

```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_STOREDCARD, withCompletionBlock: { request, postParam, error in
    if error == nil {
        //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
        //Something went wrong with Parameter, error contains the error Message string
    }
})
```
```Text Objective-C
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
