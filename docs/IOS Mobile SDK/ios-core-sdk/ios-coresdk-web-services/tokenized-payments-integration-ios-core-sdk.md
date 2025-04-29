---
title: Tokenized Payments Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Tokenized Payments Integration - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
You can store and get stored card details from the vault.

## Get tokenized payment details

1. Get details of the stored card to make payment on another PG.

```Text Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParam.cardToken = @"<cardToken>";    
self.paymentParam.amount = @"100";  
self.paymentParam.currency = @"INR";
self.paymentParamForPassing.hashes.getTokenizedPaymentDetailHash = @"hash";
```

2. Call the `getTokenizedPaymentDetails` method to integrate this similar to the following:

```Text Objective-C
[webServiceResponse getTokenizedPaymentDetails.paymentParamForPassing withCompletionBlock:^(PayUModelTokenizedPaymentDetails *tokenizedPaymentdetails,NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```

## Get tokenised stored cards

This API is helpful in getting all the stored cards for a particular user. 

1. Set the`userCredentials` in the payment params similar to the following:

```Text Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParamForPassing.hashes.getTokenizeddStoredCardHash = @"hash";
```

2. Call the getTokenizedStoredCards method to integrate this API similar to the following:

```Text Objecitve-C
[webServiceResponse getTokenizedStoredCards:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictStoredCard,NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```

## Delete tokenised stored cards

This API is helpful in deleting stored cards.

1. Set the`userCredentials` in the payment params similar to the following:

```Text Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParam.cardToken = @"<cardToken>";    
self.paymentParam.networkToken = @"<networkToken>";  
self.paymentParam.issuerToken = @"<issuerToken>";
self.paymentParamForPassing.hashes.deleteTokenizedStoredCardHash = @"hash";
```

2. Call the `deleteTokenizedStoredCard` method to integrate this API similar to the following:

```Text Objective-C
[webServiceResponse deleteTokenizedStoredCard:self.paymentParamForPassing withCompletionBlock:^(NSString *deleteStoredCardStatus, NSString *deleteStoredCardMessage, NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```
