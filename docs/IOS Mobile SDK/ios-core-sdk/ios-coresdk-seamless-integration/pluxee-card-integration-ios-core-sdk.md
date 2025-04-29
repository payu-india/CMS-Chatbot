---
title: Pluxee Card Integration - iOS Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: TwidPay BNPL Integration - iOS Core SDK
  description: ''
  keywords:
    - iOS TwidPay BNPL Integration
    - ' TwidPay BNPL Integration for iOS Core SDK'
  robots: index
next:
  description: ''
---
To pay using Pluxee card:

1. Create the post data with the`PAYMENT_PG_SODEXO `:

```Text Objective-C
    self.paymentParamForPassing.cardNumber = @"<Sodexo card number>";//cardNumber
    self.paymentParamForPassing.nameOnCard = @"name";//Name on card
    self.paymentParamForPassing.expYear = @"2018";//Expiry year
    self.paymentParamForPassing.expMonth = @"11";//ExpiryMonth
    self.paymentParamForPassing.CVV = @"123";//CVV
    self.paymentParamForPassing.shouldSaveCard = YES;//If you want to save card then pass it otherwise it will not save 
```
```Text Swift
self.paymentParamForPassing.cardNumber = "<Sodexo card number>";//cardNumber
self.paymentParamForPassing.nameOnCard = "name";//Name on card
self.paymentParamForPassing.expYear = "2018";//Expiry year
self.paymentParamForPassing.expMonth = "11";//ExpiryMonth
self.paymentParamForPassing.CVV = "123";//CVV
self.paymentParamForPassing.shouldSaveCard = true;//If you want to save card then pass it otherwise it will not save 
```

2. Get the request by using the`createRequestWithPaymentParam` method similar to the following code snippet:

```Text Objective-C
        self.createRequest = [PayUCreateRequest new];
        [self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_SODEXO withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
        if (error == nil) {
        //It is good to go state. You can use request parameter in webview to open Payment Page
        }
        else{
        //Something went wrong with Parameter, error contains the error Message string
        }
    }];
```
```Text Swift
createRequest().createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_SODEXO, withCompletionBlock: { request, postParam, error in
    if error == nil {
        //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
        //Something went wrong with Parameter, error contains the error Message string
    }
})
```

The successful or failed payment response is sent by PayU.

3. Get the Sodexo source id in the field3 param of PayuResponse, which can be used to show and get stored Sodexo card details and also can be used for initiating payment.

```Text Objective-C
    self.paymentParamForPassing.sodexoSourceId = @"<Sodexo source id>";
    
```
```Text Swift
    self.paymentParamForPassing.sodexoSourceId = "<Sodexo source id>"
```
