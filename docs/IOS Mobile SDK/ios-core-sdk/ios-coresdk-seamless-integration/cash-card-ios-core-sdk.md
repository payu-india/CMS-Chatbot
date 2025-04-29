---
title: Cash Card Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Cash Card Integration for iOS Core SDK
  description: ''
  keywords:
    - Cash Card Integration for iOS Core SDK
    - iOS Cash Card Integration
  robots: index
next:
  description: ''
---
To pay using a Cash Card, perform the following steps

1. Set the cashcard parameter as follows:

```Text Swift
  paymentParamForPassing.bankCode = "AXIB" //BankCode
```

```Text Objective-C
 self.paymentParamForPassing.bankCode = @"AXIB";//BankCode
```

2. Get the request by using the `createRequestWithPaymentParam` method for instance.

```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_CASHCARD, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```
```Text Objective-C
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