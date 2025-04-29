---
title: Get Checkout Details API
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
The **Get Checkout Details** API provides information on `additionalCharges`, `bankDownStatus`, `taxSpecification`, `offerDetails`, `customerEligibility`, `merchantDetails`, `extendedPaymentDetails`, and pg id information for payment options on a merchant key. 

To integrate this API:

1. Call this API is similar to other Web Services, the only difference is that it requires a JSON in var1. Check the following code block for more details. Here, requestId is a unique random number passed in the request.

```Text JSON Response
{
        "useCase":{
            "getExtendedPaymentDetails":true,
            "getTaxSpecification":true,
            "checkDownStatus":true,
            "getAdditionalCharges":true,
            "getOfferDetails":true,
            "getPgIdForEachOption":true,
            "checkCustomerEligibility":true,
            "getMerchantDetails":true,
            "getPaymentDetailsWithExtraFields":true
        },
        "filters":{
            "paymentOptions":{
                "emi":{
                    "dc":"HDFC",
                    "cardless":"ZESTMON"
                },
                "bnpl":"MOBIZIP"
            }
        },
        "requestId":"iOS230113135103",
        "customerDetails":{
            "mobile":"9876543210"
        },
        "transactionDetails":{
            "amount":"1"
        }
    }
```

2. Set `amount`, `additionalCharges`, `checkDownStatus`, `checkTaxSpecification`, `checkOfferDetails`, `checkCustomerEligibility`, `getMerchantDetails`, `getExtendedPaymentDetails` and `getPgIdForEachOption` in the payment parameters, for instance:

```Text Objective-C
self.paymentParamForPassing.getExtendedPaymentDetails = true; 
self.paymentParamForPassing.checkTaxSpecification = true;      
self.paymentParamForPassing.checkDownStatus = true;   self.paymentParamForPassing.checkAdditionalCharges = true;      
self.paymentParamForPassing.checkOfferDetails = true;   self.paymentParamForPassing.getPgIdForEachOption = true;     self.paymentParamForPassing.checkCustomerEligibility = true;   
self.paymentParamForPassing.getMerchantDetails = true;          self.paymentParamForPassing.getPaymentDetailsWithExtraFields = true;     
self.paymentParamForPassing.amount = @"<Amount>";   self.paymentParamForPassing.hashes.getCheckoutDetailsHash = @"hash";         PayUModelGetCheckoutAPIFilters *getCheckoutAPIFilters = [PayUModelGetCheckoutAPIFilters new];         getCheckoutAPIFilters.dcEMIBankCode = @"<BankCode>";         getCheckoutAPIFilters.cardlessEMIBankCode = @"<BankCode>";         getCheckoutAPIFilters.bnplBankCode = @"<BankCode>";        self.paymentParamForPassing.getCheckoutAPIFilters = getCheckoutAPIFilters;
```

3. Call the `getCheckoutDetail` to integrate this API:

```Text Objective-C
[webServiceResponse
getCheckoutDetail:self.paymentParamForPassing withCompletionBlock:^(NSArray *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // paymentRelatedDetails object is having the required detail
      }
    }];
```
