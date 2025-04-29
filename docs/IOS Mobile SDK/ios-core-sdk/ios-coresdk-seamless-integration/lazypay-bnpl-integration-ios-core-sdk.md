---
title: LazyPay BNPL Integration - iOS Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: LazyPay BNPL Integration - iOS Core SDK
  description: ''
  keywords:
    - LazyPay BNPL Integration for iOS Core SDK
    - iOS LazyPay BNPL Integration
  robots: index
next:
  description: ''
---
To pay using LazyPay (BNPL), perform the following steps.

1. Set the Notify URL to the HTTPS Callback URL of the merchant where notification of transaction status will be sent on completion of a transaction. 

```Text Objective-C
self.paymentParamForPassing.notifyURL= @"https://notifyURL.com";
```
```Text Swift
paymentParamForPassing.notifyURL = "https://notifyURL.com"
```

2. Get the request by using the`createRequestWithPaymentParam` method as follows:

```Text Objective-C
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
```Text Swift
reateRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_LAZYPAY, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```