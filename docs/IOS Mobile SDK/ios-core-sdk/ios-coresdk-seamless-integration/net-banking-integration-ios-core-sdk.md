---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Net Banking Integration - iOS Core SDK
  description: ''
  keywords:
    - Net Banking Integration for iOS Core SDK
    - ' iOS Net Banking Integration'
  robots: index
next:
  description: ''
---
To pay using Net Banking, perform the following steps.

1. Set the Net Banking parameter as follows:

```Text Swift
paymentParamForPassing.bankCode = "AXIB" //BankCode
```
```Text Objective-C
```

2. Get the request by using the `createRequestWithPaymentParam` method as follows:

```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_NET_BANKING, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```
```Text Objective-C
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
