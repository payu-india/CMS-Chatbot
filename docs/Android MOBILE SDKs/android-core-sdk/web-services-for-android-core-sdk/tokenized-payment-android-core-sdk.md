---
title: Tokenized Payment APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Tokenized Payment APIs - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
You can store and get stored card details from the vault. The tokenized payments for Android Core SDK includes the following APIs:

* [Get Tokenized Stored Cards API](get-tokenized-stored-cards-api)
* [Get Tokenized Stored Card Details API](#get-tokenized-stored-card-details-api)
* [Delete Tokenized Stored Cards API](#delete-tokenized-stored-cards-api)

## Get Tokenized Stored Cards API

The **Get Tokenized Stored Cards** API is helpful in getting all the stored cards for a particular user. For this API, you need to set the`userCredentials` in the payment params similar to the following:

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey("<pass the merchant key>");
merchantWebService.setCommand(PayuConstants.GET_TOKENISED_USER_CARD);
merchantWebService.setVar1(user_credentials); //In var1, pass the user_credential
merchantWebService.setHash("<pass the hash value>"); 
```

To integrate this API call the `getTokenizedStoredCards` method similar to the following:

```Text Java
@Override
public void onGetTokenisedCardResponse(PayuResponse payuResponse) {
        
}
```

### Get Tokenized Stored Card Details API

The **Get Tokenized Stored Card Details** API is used to get details of the stored card to make payment on another PG.

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey("<pass the merchant key>");
merchantWebService.setCommand(PayuConstants.GET_TOKENISED_CARD_DETAILS); 
merchantWebService.setVar1("<user_credentials>"); //In var1, pass the user_credential
merchantWebService.setVar2("<cardToken>"); //In var2, pass the cardToken to get the saved card details
merchantWebService.setHash("<pass the hash value>"); 
```

```Text Java
@Override
public void onTokenisedCardDetailsResponse(PayuResponse payuResponse) {
        
}
```

### Delete Tokenized Stored Cards API

The **Delete Tokenized Stored Cards** API is helpful in deleting stored cards.

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey("<pass the merchant key>");
merchantWebService.setCommand(PayuConstants.DELETE_TOKENISED_USER_CARD);
merchantWebService.setVar1("<user_credentials>"); //In var1, pass the user_credential
merchantWebService.setVar2("<cardToken>"); //In var2, pass the cardToken to delete the saved card details
merchantWebService.setHash("<pass the hash value>"); 
```

To integrate this API call the `deleteTokenizedStoredCard` method similar to the following:

```Text Java
@Override
public void onDeleteTokenisedCardResponse(PayuResponse payuResponse) {

}
```
