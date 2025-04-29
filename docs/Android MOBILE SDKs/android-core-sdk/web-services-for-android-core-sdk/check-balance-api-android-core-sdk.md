---
title: Check Balance API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Check Balance API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Check Balance** API can be used to fetch detail of the Sodexo card with the source ID.

## Step 1: Set parameters

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.CHECK_BALANCE);
merchantWebService.setVar1(sodexoSourceId); // This parameter must contain the Sodexo Source ID
merchantWebService.setHash(HashGenerationUtils.generateHashFromSDK(hashData, salt));        
```

## Step 2: Handle response

```Text Java
@Override
  public void onCheckBalanceResponse(PayuResponse payuResponse) {
    Log.d(TAG, "onCheckBalanceResponse: " + payuResponse.getRawResponse());
}
```

***

##