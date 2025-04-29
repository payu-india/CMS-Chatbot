---
title: Check Is Domestic API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Check Is Domestic API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Check is Domestic **API is used to get the following using the BIN number, that is, the first six digits of a credit card or debit card:

- BIN information
- Detect whether a particular BIN number is international or domestic.
- Determine the card’s issuing bank, the card type brand, that is, Visa, Master, etc.,
- Determine the card category, that is, credit, debit, etc.

The command name and var1 will be:

- Command Name - check_isDomestic
- Var1 - Card Number(Like. "5123456789012346")

> 📘 Hash logic
> 
> The hash will be in the format of: 
> 
> `Sha512(Key|Command|Var1|Salt)`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

## Integration

1. Set `cardNumber` in the payment params similar to the following code block:

```Text Swift
self.paymentParamForPassing.cardNumber = "5123456789012346";
self.paymentParamForPassing.hashes.checkIsDomesticHash = "hash";
```
```Text Objective-C
self.paymentParamForPassing.cardNumber = @"5123456789012346";
self.paymentParamForPassing.hashes.checkIsDomesticHash = @"hash";
```

2. Call the checkIsDomestic method to integrate this API as described in the following code block:

```Text Swift
   webServiceResponse?.checkIsDomestic(paymentParamForPassing, withCompletionBlock: { result, error, json in 
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
verifyPayment:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictVerifyPayment, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictVerifyPayment is having the verifyPayment detail
      }
    }];
```