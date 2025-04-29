---
title: Get Bin Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Bin Info API – iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The** Get Bin Info** API is used to detect whether a particular BIN number is international or domestic. In addition, it is useful to determine the card’s issuing bank, the card type brand, that is, Visa, Mastercard, etc., and the card category, that is, credit card, debit card, etc. The BIN number is the first six digits of a credit or debit card. This API is also helpful in knowing whether the card BIN is eligible for Standing Instructions. For this API, you need to set the card number in the payment parameters.

The command name and var1 for this API integration are:

- Command Name - getBinInfo
- Var1 - 1
- Var5 - 1  if you want to check card supports SI and pass the isSIInfo as true.

> 📘 Hash format
> 
> The hash will be in the format of:
> 
> `Sha512(Key|Command|Var1|Salt)`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

## Integration

1. Set the following parameter in the payment params similar to the following code block:

```Text Swift
self.paymentParamForPassing.cardNumber = "5123456789012346"
self.paymentParamForPassing.isSIInfo = true
self.paymentParamForPassing.hashes.getBinInfoHash = "hash"
```
```Text Objective-C
self.paymentParamForPassing.cardNumber = @"5123456789012346";
self.paymentParamForPassing.isSIInfo = @"true";
self.paymentParamForPassing.hashes.getBinInfoHash = @"hash";
```

2. Call the GetBINInfo method to integrate with this API as described in the following code block:

```Text Swift
 webServiceResponse?.getBinInfo(paymentParamForPassing, withCompletionBlock: { result, error, json in
            completion(result, error, json)
          
     if (error){

                // Something went wrong errorMessage is having the Detail

            }else{

                // It is good to go & paymentRelatedDetails is having the full detail of it

            }

        })
```
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