---
title: Fetch Payment Options API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Fetch Payment Options API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Fetch Payment Option** API will get the payment options which are enabled for merchants including saved cards. Integrate this API by calling the `getPayUPaymentRelatedDetailForMobileSDK`.

- **Command Name **- payment_related_details_for_mobile_sdk
- **Var1** - userCredentials (userCredentials might be blank)

> 📘 Hash logic
> 
> The hash will be in the format of:
> 
> Sha512(Key|Command|Var1|Salt)
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

For this API, you need to set `hash` in the payment params similar to the following code block:

```Text Swift
self.paymentParamForPassing.hashes.paymentRelatedDetailsHash = "hash"
```

**Method**

```Text Swift
webServiceResponse?.getPayUPaymentRelatedDetail(forMobileSDK: paymentParamForPassing) {
    [weak self] (paymentRelatedDetails, errorMessage, extraParam) in
    completion(paymentRelatedDetails,errorMessage,extraParam)
    if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
    }

    else{
        // It is good to go & paymentRelatedDetails is having the full detail of it
    }

}
```
```text Objective-C
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

> 📘 Notes:
> 
> - `paymentRelatedDetails.availablePaymentOptionsArray` gives you all the available payment options for you.
> - paymentRelatedDetails.oneTapStoredCardArray, paymentRelatedDetails.storedCardArray, paymentRelatedDetails.netBankingArray, paymentRelatedDetails.cashCardArray, paymentRelatedDetails.EMIArray, paymentRelatedDetails.NoCostEMIArray gives available OneTapCard,StoredCard, NetBanking, CashCard, EMI and NoCostEMI

<br />

***