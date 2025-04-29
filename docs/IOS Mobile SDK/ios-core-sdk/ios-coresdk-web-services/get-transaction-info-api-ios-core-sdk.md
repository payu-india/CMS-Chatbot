---
title: Get Transaction Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Transaction Info API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The** Get Transaction Info** API is used to extract the transaction details between two given time periods. The API takes the input as two dates and the time (initial and final) between which the transaction details are needed. The output would consist of the status of the API (success or failed) and all the transaction details in an array format. 

## Integration

1. Set `startTime` and `endTime` in the payment params as described in the following code block:

```Text Objective-C
self.paymentParamForPassing.startTime = @"2014-01-12 16:00:00";
self.paymentParamForPassing.endTime = @"2014-01-12 16:00:50";
self.paymentParamForPassing.hashes.getTransactionInfoHash = @"hash";
```

1. Call the `getTransactionInfo` method to integrate with this API as described in the following code block:

```Text Objective-C
[webServiceResponse
getTransactionInfo:self.paymentParamForPassing withCompletionBlock:^(NSArray *arrOfGetTxnInfo, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // arrOfGetTxnInfo is the array of PayUModelGetTxnInfo which is having detail of transaction
      }
    }];
```