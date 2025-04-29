---
title: Credit Card/Debit Card Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Credit Card/Debit Card Integration - iOS Core SDK
  description: ''
  keywords:
    - Credit Card/Debit Card Integration for iOS Core SDK
    - ' iOS Core SDK Card Integration'
  robots: index
next:
  description: ''
---
To pay using a credit card or debit card, perform the following steps.

1. Set the following credit card parameters:

```Text Swift
paymentParamForPassing.cardNumber = "5123456789012346" //cardNumber
paymentParamForPassing.nameOnCard = "name" //Name on card
paymentParamForPassing.expYear = "2018" //Expiry year
paymentParamForPassing.expMonth = "11" //ExpiryMonth
paymentParamForPassing.cvv = "123" //CVV
paymentParamForPassing.storeCardName = "My TestCard" //If you want to save card then pass StoreCardName otherwise it will not save & make sure userCredentials are provided
```
```Text Objective-C
        self.paymentParamForPassing.cardNumber = @"5123456789012346";//cardNumber
        self.paymentParamForPassing.nameOnCard = @"name";//Name on card
        self.paymentParamForPassing.expYear = @"2018";//Expiry year
        self.paymentParamForPassing.expMonth = @"11";//ExpiryMonth
        self.paymentParamForPassing.CVV = @"123";//CVV
        self.paymentParamForPassing.storeCardName = @"My TestCard";//If you want to save card then pass StoreCardName otherwise it will not save & make sure userCredentials are provided
```

2. Get the request by using the `createRequestWithPaymentParam` method as follows:

```Text Swift
createRequest().createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_CCDC, withCompletionBlock: { request, postParam, error in
    if error == nil {
        //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
        //Something went wrong with Parameter, error contains the error Message string
    }
})
```
```Text Objective-C
        self.createRequest = [PayUCreateRequest new];
        [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_CCDC withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
        //It is good to go state. You can use request parameter in webview to open Payment Page
        }
        else{
        //Something went wrong with Parameter, error contains the error Message string
        }
    }];
```