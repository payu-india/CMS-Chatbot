---
title: Cash Card Integration
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Cash Card Integration for iOS Core SDK
  description: ''
  keywords:
    - Cash Card Integration for iOS Core SDK
    - iOS Cash Card Integration
  robots: index
---
To pay using a Cash Card, perform the following steps

1. Set the cashcard parameter as follows:

```swift Swift
  paymentParamForPassing.bankCode = "AXIB" //BankCode
```
```objectivec
 self.paymentParamForPassing.bankCode = @"AXIB";//BankCode
```

2. Get the request by using the `createRequestWithPaymentParam` method for instance.

```swift Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_CASHCARD, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```
```objectivec Objective-C
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
