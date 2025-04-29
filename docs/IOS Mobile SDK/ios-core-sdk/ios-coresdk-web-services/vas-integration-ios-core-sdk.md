---
title: VAS Integration API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: VAS Integration API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **VAS Integration **API is used to get the list of down Net Banking and down card BIN. Integrate this API by calling the `callVASForMobileSDKWithPaymentParam`. The command name and var1 for this API integration are:

- Command Name - vas_for_mobile_sdk
- Var1 - default

> 📘 Hash format
> 
> The hash will be in the format of: 
> 
> `Sha512(Key|Command|Var1|Salt)`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

For this API, you need to set `hash` in the payment params similar to the following code block

```Text Swift
self.paymentParamForPassing.hashes.vasForMobileSDKHash = "hash"
```

## Integrate

```Text Swift
webServiceResponse?.callVASForMobileSDK(withPaymentParam: paymentParamForPassing, withCompletionBlock: { result, error, json in

            completion(result,error,json)

       if (errorMessage) {
                  // Something went wrong errorMessage is having the Detail
            } else {
                 // It is good to go & paymentRelatedDetails is having the full detail of it
            }
        })
```
```Text Objective-C
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

> 📘 **Note**:
> 
> You can check if a particular NetBanking service is down or not by just passing the bankCode or card-bin (first 6 digits of card number) and in completionBlock, the response will be fetched, for instance.
> 
> ```Text Objective-C
> [webServiceResponse getVASStatusForCardBinOrBankCode:@"AXIB" withCompletionBlock:^(id ResponseMessage, NSString *errorMessage, id extraParam) {
>     	if (errorMessage == nil) {
>         		if (ResponseMessage == nil) {
> 			        // It means given NetBanking code or cardnumber is not down i.e. it is in good to go condition
>         		}else{
>             		NSString * responseMessage = [NSString new];
>             		responseMessage = (NSString *) ResponseMessage;
> 			        // It means given NetBanking code or cardnumber is down and you can display the responseMessage if you want or you can customize it
>         		}
>     	}else{
> 		    // Something went wrong errorMessage is having the Detail
>     	}
> 	}];
> ```

***