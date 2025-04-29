---
title: Check Pluxee Card Balance API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Check Pluxee Card Balance API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Check Pluxee Card Balance** API can be used to fetch detail of the Sodexo card with the source ID.

1. Set the sodexoSourceId and checkBalanceApiHash parameter for instance:

```Text Objective-C
self.paymentParamForPassing.sodexoSourceId = @"<Sodexo source id>;
self.paymentParamForPassing.hashes.checkBalanceApiHash =  @"hash";
```

2. Call the `fetchSodexoCardDetails` method to integrate with this API similar to the following code block:

```Text Objective-C
[webServiceResponse
fetchSodexoCardDetails.paymentParamForPassing withCompletionBlock:^(PayUModelSodexoCardDetail *sodexoCardDetail, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // sodexoCardDetail object is having the required detail
      }
    }];
```

***
