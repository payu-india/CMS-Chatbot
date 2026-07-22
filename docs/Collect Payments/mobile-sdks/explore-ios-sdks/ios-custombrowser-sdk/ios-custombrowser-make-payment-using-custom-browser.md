---
title: Make Payment Using Custom Browser
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
To make payment using CustomBrowser in iOS:

* Initiate Payment
* Handle Payment Response

## Step 1: Initiate payment

You just need to pass a few parameters to initialize `PUCBWebVC` controller which will initiate the payment process.

* **postParam**: A string containing payment-related information. For more information on how to create it, refer to [SDK Wiki​](https://github.com/payu-intrepos/Documentations/wiki/).
* **URL**: This is the first URL loaded in the webView. postParam will be posted here. For example, in the case of PayU (production server), it will be:
  [https://secure.payu.in/\_payment](https://secure.payu.in/_payment)
* **merchantKey**: This is the key provided to you by PayU. This is required to provide tech support to merchants for live transactions.

```objectivec Objective-C
NSError *err = nil;
PUCBWebVC * webVC = [[PUCBWebVC alloc] initWithNSURLRequest:request                                               merchantKey:self.paymentParamForPassing.key
                                                      error:&err];
webVC.cbWebVCDelegate = self;
​
if (!err) {
    [self.navigationController pushViewController:webVC animated:true];
}
```

## Step 2: Handle payment response

To get the response of payment (success, failure, or error), you need to conform to the `PUCBWebVCDelegate `protocol. The class in which you create the `PUCBWebVC` object will generally be the delegate. The following methods need to be implemented for response handling:

```objectivec Objective-C
// Following methods give the response from your server's Success URL/ Failure URL. These are recommended to receive the response in your app after the transaction. 
// First parameter contains PayU's response. The second parameter contains response that your server has posted 
// to your app
- (void)PayUSuccessResponse:(id) payUResponse SURLResponse:(id) surlResponse;
- (void)PayUFailureResponse:(id) payUResponse FURLResponse:(id) furlResponse;

// Following methods give response from PayU to your app. The above methods are preferred over these methods 
// to mitigate data tampering risk. 
- (void)PayUSuccessResponse:(id)response; 
- (void)PayUFailureResponse:(id)response;

// General callbacks in case of ongoing transaction getting issues
- (void)PayUConnectionError:(NSDictionary *)notification;
- (void)PayUTransactionCancel;
- (void)shouldDismissVCOnBackPress; // This is an optional method which gets invoked if user presses back button. If you override it,
```
