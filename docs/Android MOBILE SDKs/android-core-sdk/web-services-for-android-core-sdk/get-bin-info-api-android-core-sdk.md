---
title: Get BIN Info API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Get BIN Info API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Get Bin Info** API is used to get the following using the BIN number, that is, the first six digits of a credit card or debit card:

**BIN information**

* Detect whether a particular BIN number is international or domestic.
* Determine the card’s issuing bank, the card type brand, that is, Visa, Master, etc.,
* Determine the card category, that is, credit, debit, etc.

This API is used to get the card BIN details. For this API, you need to set the following parameter in the payment params similar to the following code block:

## Step 1: Create Post Request

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey); // Merchant key
merchantWebService.setCommand(PayuConstants.GET_BIN_INFO);
merchantWebService.setVar1("1")
merchantWebService.setVar2("1") //only for SI
merchantWebService.setVar5("<pass card BIN Number>") // Pass card BIN Number
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Get onBinInfoApiResponse

```Text Java
@Override
public void onBinInfoApiResponse(PayuResponse payuResponse) {
}
```
