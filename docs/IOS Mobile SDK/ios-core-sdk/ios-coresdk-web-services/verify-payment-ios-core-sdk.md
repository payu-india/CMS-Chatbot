---
title: Verify Payment API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Verify Payment API – iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The Verify Payment API is used to reconcile the transaction with PayU. When PayU posts back the final response to you (merchant), PayU provides a list of parameters (including the status of the transaction). For example, success, failure, etc. On a few occasions, the transaction response is initiated from our end, but it does not reach you due to network issues or user activity (like refreshing the browser, etc.).

The command name and var1 for this API integration are:

* Command Name - verify\_payment
* Var1 - txnId

> 📘 Note:
>
> PayU strongly recommends that this API is used to reconcile with PayU’s database once you receive the response. This will protect you from any tampering by the user and help in ensuring safe and secure transaction experience.

> 📘 Hash logic
>
> The hash will be in the format of: 
>
> `Sha512(Key|Command|Var1|Salt)`
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

## Integration

1. Set `transactionID` inside your payment parameters for instance:

```Text Swift
self.paymentParamForPassing.transactionID = "tnxID";
self.paymentParamForPassing.hashes.verifyTransactionHash = "hash";
```
```Text Objective-C
self.paymentParamForPassing.transactionID = @"tnxID1|txnID2|txnID3";
self.paymentParamForPassing.hashes.verifyTransactionHash = @"hash";
```

> Note: You can send multiple txnIDs (transaction IDs) using the pipe symbol(|) as a separator.

2. Call the `verifyPayment()` method to integrate this API as described in the following code block:

```Text Swift
webServiceResponse?.verifyPayment(paymentParamForPassing, withCompletionBlock: { result, error, json in
            completion(result,error,json)
          if (error){

                // Something went wrong errorMessage is having the Detail

            }else{

                // It is good to go & paymentRelatedDetails is having the full detail of it

            }
        })
```
```Text Objective-C
[webServiceResponse
verifyPayment:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictVerifyPayment, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictVerifyPayment is having the verifyPayment detail
      }
    }];
```

***
