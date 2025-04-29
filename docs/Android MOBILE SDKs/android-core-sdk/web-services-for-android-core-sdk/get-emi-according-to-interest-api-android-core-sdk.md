---
title: Get EMI According to Interest API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get EMI According to Interest API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
**Get EMI According to Interest** API is used to get information to get details related to EMI such as EMI amount, tenure in month, interest rate, etc.

> 📘 Hash logic
> 
> The hash logic for this API is:
> 
> `<key>|vas_for_mobile_sdk|<amount>|<salt>`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

## 

## Step 1: Set parameters

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.API_GET_EMI_AMOUNT_ACCORDING_INTEREST);
merchantWebService.setVar1(amount); // The amount that must be converted to EMI.
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Handle response

```Text Java
@Override
public void onGetEmiAmountAccordingToInterestApiResponse(PayuResponse payuResponse) {
    Log.d(TAG, "onGetEmiAmountAccordingToInterestApiResponse: " + payuResponse.getRawResponse());
}
```