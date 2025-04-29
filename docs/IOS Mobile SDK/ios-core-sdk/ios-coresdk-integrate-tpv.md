---
title: Integrate TPV
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
> ❗️ Callout
> 
> For TPV transactions, you need to have a different merchantID. Contact your key account manager for the same.

To integrate TPV with the BizSDK framework:

- Calculate Hash
- Make Payment
- Handle Response

## Step 1: Calculate hash

For TPV transactions, the hash calculation formula is different from the result type of payment:

> 📘 Note:
> 
> For multiple account numbers, account numbers should be pipe separated, and max four account numbers are allowed.

```
Hash Formula:
// For single account number
beneficiarydetail = "{'beneficiaryAccountNumber':'123456789'}"
// For multiple account number
beneficiarydetail = "{'beneficiaryAccountNumber':'123456789|54321234|98765673|34767988'}"
// Hash calculation
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

> 📘 Reference:
> 
> For more information on Static Hashing, refer to [Generate Static Hash](doc:generate-static-hash-ios).

## Step 2: Make payment

To get a request, create an object of the class \`PayUCreateRequest\`\` as below. The callbacks give you NSURLRequest as well as post parameters (in String). You can use these post parameters to initialize Custom Browser Instance.

```Text Objective-C
@property (nonatomic, strong) PayUCreateRequest *createRequest;
```
```Text Swift
let createRequest = PayUCreateRequest()
```

### Net Banking

To pay using NetBanking, you need to configure the Net Banking parameters, for instance:

```Text Objective-C
self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789";
self.paymentParamForPassing.bankCode = @"AXNBTPV"; //BankCode
```
```Text Swift
paymentParamForPassing.beneficiaryAccountNumbers = "123456789"
paymentParamForPassing.bankCode = "AXNBTPV" //BankCode
```

After setting the above parameters, you can get the request by using the createRequestWithPaymentParam method similar to the following code snippet:

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
```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_NET_BANKING, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```

### UPI

To pay using UPI, you need to configure the UPI parameters, for instance:

```Text Objective-C
// For single account number
self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789";
// For multiple account number
self.paymentParamForPassing.beneficiaryAccountNumbers = @"123456789|54321234|98765673|34767988";
// Set BankCode
self.paymentParamForPassing.bankCode = @"UPITPV"; // UPITPV or TEZTPV
// Set VPA
self.paymentParamForPassing.vpa = @"umang@axis";
```
```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_UPI, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```

After configuring the above parameters, you can get the request by using the `createRequestWithPaymentParam `method, for instance.

```Text Objective-C
self.createRequest = [PayUCreateRequest new];
[self.createRequest createRequestWithPaymentParam:self.paymentParamForPassing forPaymentType:PAYMENT_PG_UPI withCompletionBlock:^(NSMutableURLRequest *request, NSString *postParam, NSString *error) {
    if (error == nil) {
        //It is good to go state. You can use request parameter in webview to open Payment Page
    }
    else{
        //Something went wrong with Parameter, error contains the error Message string
    }
}];
```
```Text Swift
createRequest.createRequest(withPaymentParam: paymentParamForPassing, forPaymentType: PAYMENT_PG_UPI, withCompletionBlock: { request, postParam, error in
if error == nil {
//It is good to go state. You can use request parameter in webview to open Payment Page
} else {
//Something went wrong with Parameter, error contains the error Message string
}
})
```

## Step 3: Handle response

The procedure for response handling is similar to how you handle other payment options.