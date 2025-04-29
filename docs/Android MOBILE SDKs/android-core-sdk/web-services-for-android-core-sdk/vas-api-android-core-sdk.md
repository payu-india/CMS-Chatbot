---
title: VAS API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to get the list of down Net Banking and card BIN that is down.

> 📘 Note :
> 
> You can check if a particular NetBanking service is down or not by just passing the bankCode or card-bin (first 6 digits of card number) and in payuResponse, the response will be fetched, for instance.

## Step 1: Call ValueAddedServiceTask

 Integrate this API by calling the `ValueAddedServiceTask` method:

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.VAS_FOR_MOBILE_SDK);
merchantWebService.setVar1(PayuConstants.DEFAULT);
merchantWebService.setVar2(PayuConstants.DEFAULT);
merchantWebService.setVar3(PayuConstants.DEFAULT);
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

## Step 2: Get onValueAddedServiceApiResponse

After you execute `ValueAddedServiceTask`, the `onValueAddedServiceApiResponse` callback method is called:

```Text Java
  @Override
    public void onValueAddedServiceApiResponse(PayuResponse payuResponse) {
        if (mPayuResponse != null) {
           // It means given NetBanking code or cardnumber is not down i.e. it is in good to go condition
            } else {
           // It means given NetBanking code or cardnumber is down and you can display the responseMessage if you want or you can customize it
            }
        }
    }
```