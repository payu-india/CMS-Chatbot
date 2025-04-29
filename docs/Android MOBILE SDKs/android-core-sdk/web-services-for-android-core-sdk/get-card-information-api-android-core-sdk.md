---
title: Get Card Information API
excerpt: Check isDomestic
deprecated: false
hidden: false
metadata:
  title: Get Card Information API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Get Card Information** (Check is Domestic) API is used to get if the card (passed in cardBin info API) is domestic or international. This API returns the following parameters:

* card\_type
* category
* issuing\_bank
* is\_atmpin\_card

For this API, you need to set the following parameter in the payment params similar to the following code block:

## Step 1: Create Post Request

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey); // Merchant key
merchantWebService.setCommand(PayuConstants.CHECK_IS_DOMESTIC);
merchantWebService.setVar1("<pass the card Bin number>")
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Get onGetCardInformationResponse

```Text Java
@Override
public void onGetCardInformationResponse(PayuResponse payuResponse) {
   Log.d(TAG, "onGetCardInformationResponse: " + payuResponse.getRawResponse());
}
```
