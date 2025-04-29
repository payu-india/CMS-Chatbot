---
title: EMI Payment Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: EMI Payment Integration - iOS Core SDK
  description: ''
  keywords:
    - EMI Payment Integration for iOS Core SDK
    - ' iOS EMI Payment Integration'
  robots: index
next:
  description: ''
---
The section describes the following methods to collect payments with EMI:

* [EMI](#emi)
* [Cardless EMI](#cardless-emi)
* [Subvention EMI](#subvention-emi)

## EMI

To pay using EMI, perform the following steps.

1. Set the EMI parameter for instance:

```Text Objective-C
    self.paymentParamForPassing.bankCode = @"EMI03";//BankCode
    self.paymentParamForPassing.expiryYear = @"2019";
    self.paymentParamForPassing.expiryMonth = @"12";
    self.paymentParamForPassing.nameOnCard = @"test";
    self.paymentParamForPassing.cardNumber = @"5123456789012346";
    self.paymentParamForPassing.CVV = @"123";
```
```Text Swift
paymentParamForPassing.bankCode = "EMI03" //BankCode
paymentParamForPassing.expiryYear = "2019"
paymentParamForPassing.expiryMonth = "12"
paymentParamForPassing.nameOnCard = "test"
paymentParamForPassing.cardNumber = "5123456789012346"
paymentParamForPassing.cvv = "123"
```

2. Get the request by using the `createRequestWithPaymentParam` method for instance.

```Text Objective-C
self.createRequest = [PayUCreateRequest new];
[self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_EMI withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
    if (error == nil) {
            //It is good to go state. You can use request parameter in webview to open Payment Page
    }
    else{
     //Something went wrong with Parameter, error contains the error Message string

    }
}];
```
```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_EMI, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```

## Cardless EMI

To Pay using CardlessEMI, you need to set a parameter similar to the following code snippet:

```Text Objective-C
    self.paymentParamForPassing.bankCode = @"ZESTMON";//BankID
    self.paymentParamForPassing.isCardlessEMI = true;
    self.paymentParamForPassing.phoneNumber = @"9999999999";
    
```
```Text Swift
paymentParamForPassing.bankCode = "ZESTMON" //BankID
paymentParamForPassing.isCardlessEMI = true
paymentParamForPassing.phoneNumber = "99999999"
```

## Subvention EMI

To pay using Subvention EMI, perform the following steps.

1. Set the value of the `subventionAmount` parameter of `paymentParams`:

```Text Objective-C
    self.paymentParamForPassing.bankCode = @"EMI03";//BankCode
    self.paymentParamForPassing.expiryYear = @"2019";
    self.paymentParamForPassing.expiryMonth = @"12";
    self.paymentParamForPassing.nameOnCard = @"test";
    self.paymentParamForPassing.cardNumber = @"5123456789012346";
    self.paymentParamForPassing.CVV = @"123";

    self.paymentParamForPassing.subventionAmount = @"3000";
```
```Text Swift
paymentParamForPassing.bankCode = "EMI03" //BankCode
paymentParamForPassing.expiryYear = "2019"
paymentParamForPassing.expiryMonth = "12"
paymentParamForPassing.nameOnCard = "test"
paymentParamForPassing.cardNumber = "5123456789012346"
paymentParamForPassing.cvv = "123"
paymentParamForPassing.subventionAmount = "3000"
```

2. Get the request by using the`createRequestWithPaymentParam` method as follows:

```Text Objective-C
Get the request by using createRequestWithPaymentParam method as follows:
```
```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_EMI, withCompletionBlock: { request, postParam, error in
    if error == nil {
        //It is good to go state. You can use request parameter in webview to open Payment Page
    } else {
        //Something went wrong with Parameter, error contains the error Message string
    }
})
```

> 📘 Hashing format of a subvention transaction
>
> If subventionAmount is passed, the hash formula for payment hash will be similar to the following format: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|SubventionAmount)`

## Fetch a List of No-Cost EMI-supporting banks

Pass the value for the subventionEligibility parameter as “all” in the Fetch Payment Option WebService. For more information refer to Web Services for Core.
