---
title: Eligible Bins for EMI API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Eligible Bins for EMI API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Eligible BINs for EMI** API fetches a list of eligible Bins for EMI corresponding to each Bank name along with minimum amount. 

> 📘 Hash logic
> 
> The hash logic for this API is:
> 
> `<key>|eligibleBinsForEMI|default|<salt>`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

## Step 1: Set parameters

Set the parameters similar to the following snippet:

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.ELIGIBLE_BINS_FOR_EMI);
merchantWebService.setVar1("BIN"); // This parameter needs can include either Bin or NET.
merchantWebService.setVar2(cardBin); // The first 6/8/9 digits of card number or network token.
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Handle the response

Handle the API response for eligible bins for EMI and log the raw response for debugging or informational purposes.

```Text Java
@Override
 public void onEligibleBinsForEMIApiResponse(PayuResponse payuResponse) {
    Log.d(TAG, "onEligibleBinsForEMIApiResponse: " + payuResponse.getRawResponse());
}
```