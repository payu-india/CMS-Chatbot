---
title: Get Transaction Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get Transaction Info API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Get Transaction Info** API is used to extract the transaction details between two given time periods. 

## Step 1: Set parameters

The API takes the input as two dates and the time (initial and final) between which the transaction details are needed. The output would consist of the status of the API (success or failed) and all the transaction details in an array format. Set startTime and endTime in the payment params as described in the following code block:

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.GET_TRANSACTION_INFO);
merchantWebService.setVar1(startDate); // The starting Time (from when the transaction details are needed
merchantWebService.setVar2(endDate); // The end Time (till when the transaction details are needed).
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Handle response

```Text Java
@Override
public void onGetTransactionApiListener(PayuResponse payuResponse) {
    Log.d(TAG, "onGetTransactionApiListener: " + payuResponse.getRawResponse());
}
```
