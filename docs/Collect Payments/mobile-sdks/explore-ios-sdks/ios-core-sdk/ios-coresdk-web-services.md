---
title: Web Services for iOS Core SDK
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
This part of the document includes the following APIs for iOS Core SDK. Before you use the following APIs, initialise  the web service as described in [Initialise web service](#initialise-web-service).

<Accordion title="Prerequisite - Initialise web service" icon="fa-code">
1. Create an object of the `PayUWebServiceResponse` class and call the respective methods. You will get the result in the completion handler of the method.

```swift Swift
 let webServiceResponse = PayUWebServiceResponse()
```
```objectivec Objective-C
PayUWebServiceResponse *webServiceResponse = [PayUWebServiceResponse new];
```

<Callout icon="📘" theme="info">
  **Note**: If there is an error in the parameters passed by the merchant, it will give the errorMessage string. Else, you will get the parsed object.
</Callout>

2. Handle the response

```
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

<br />
</Accordion>

<Accordion title="Fetch Payment Options API" icon="fa-code">
The **Fetch Payment Option** API will get the payment options which are enabled for merchants including saved cards. Integrate this API by calling the `getPayUPaymentRelatedDetailForMobileSDK`.

* **Command Name** - payment_related_details_for_mobile_sdk
* **Var1** - userCredentials (userCredentials might be blank)

<Callout icon="📘" theme="info">
  **Hash logic**: The hash will be in the format of:

  `SHA512(Key|Command|Var1|Salt)`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Callout>

For this API, you need to set `hash` in the payment params similar to the following code block:

```swift Swift
self.paymentParamForPassing.hashes.paymentRelatedDetailsHash = "hash"
```

**Method**

```swift Swift
webServiceResponse?.getPayUPaymentRelatedDetail(forMobileSDK: paymentParamForPassing) {
    [weak self] (paymentRelatedDetails, errorMessage, extraParam) in
    completion(paymentRelatedDetails,errorMessage,extraParam)
    if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
    }

    else{
        // It is good to go & paymentRelatedDetails is having the full detail of it
    }

}
```
```objectivec Objective-C
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

> 📘 Notes:
>
> * `paymentRelatedDetails.availablePaymentOptionsArray` gives you all the available payment options for you.
> * paymentRelatedDetails.oneTapStoredCardArray, paymentRelatedDetails.storedCardArray, paymentRelatedDetails.netBankingArray, paymentRelatedDetails.cashCardArray, paymentRelatedDetails.EMIArray, paymentRelatedDetails.NoCostEMIArray gives available OneTapCard,StoredCard, NetBanking, CashCard, EMI and NoCostEMI

<br />
</Accordion>

<Accordion title="VAS Integration API" icon="fa-code">
The **VAS Integration** API is used to get the list of down Net Banking and down card BIN. Integrate this API by calling the `callVASForMobileSDKWithPaymentParam`. The command name and var1 for this API integration are:

* Command Name - vas_for_mobile_sdk
* Var1 - default

<Callout icon="📘" theme="info">
  **Hash format**: The hash will be in the format of:

  `Sha512(Key|Command|Var1|Salt)`

  For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Callout>

For this API, you need to set `hash` in the payment params similar to the following code block

```swift Swift
self.paymentParamForPassing.hashes.vasForMobileSDKHash = "hash"
```
</Accordion>

<Accordion title="Integrate" icon="fa-code">
```swift Swift
webServiceResponse?.callVASForMobileSDK(withPaymentParam: paymentParamForPassing, withCompletionBlock: { result, error, json in

            completion(result,error,json)

       if (errorMessage) {
                  // Something went wrong errorMessage is having the Detail
            } else {
                 // It is good to go & paymentRelatedDetails is having the full detail of it
            }
        })
```
```objectivec Objective-C
[webServiceResponse getPayUPaymentRelatedDetailForMobileSDK:self.paymentParamForPassing withCompletionBlock:^(PayUModelPaymentRelatedDetail *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
​
if (errorMessage) {
    // Something went wrong errorMessage is having the Detail
}else{
    // It is good to go & paymentRelatedDetails is having the full detail of it
}
}];
```

> 📘 **Note**:
>
> You can check if a particular NetBanking service is down or not by just passing the bankCode or card-bin (first 6 digits of card number) and in completionBlock, the response will be fetched, for instance.
>
> ```objectivec Objective-C
> [webServiceResponse getVASStatusForCardBinOrBankCode:@"AXIB" withCompletionBlock:^(id ResponseMessage, NSString *errorMessage, id extraParam) {
>     	if (errorMessage == nil) {
>         		if (ResponseMessage == nil) {
> 			        // It means given NetBanking code or cardnumber is not down i.e. it is in good to go condition
>         		}else{
>             		NSString * responseMessage = [NSString new];
>             		responseMessage = (NSString *) ResponseMessage;
> 			        // It means given NetBanking code or cardnumber is down and you can display the responseMessage if you want or you can customize it
>         		}
>     	}else{
> 		    // Something went wrong errorMessage is having the Detail
>     	}
> 	}];
> ```
</Accordion>

<Accordion title="Offer APIs" icon="fa-code">
This section includes the offer APIs for iOS Core SDK:

* [Fetch Offer Details API](#fetch-offer-details-api)
* [Validate Offer Details API](#validate-offer-details-api)
</Accordion>

<Accordion title="Fetch Offer Details API" icon="fa-code">
Use the **Fetch Offer Details** API to fetch all the offer list available for the merchant.

> 📘 Hash Generation Logic
>
> In `completionBlockForHashGeneration`, you will get hash string without salt so you need to append the salt at the end of this hash string and convert using sha512 and pass that value in hash completion as passing below in the code.
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).

<Accordion title="Integration" icon="fa-code">
1. Set amount and userToken inside your payment parameters for instance

```swift Swift
        paymentParamForPassing.amount = "amount"
        paymentParamForPassing.offerParams = PayUModelOfferParams()
        paymentParamForPassing.offerParams?.userToken = "Any default Value"
```

2. Call the `getAllOfferDetails()` method to integrate this API as described in the following code block

```swift Swift
 webServiceResponse?.getAllOfferDetails(paymentParamForPassing, completionBlockForHashGeneration: { json, hashcompletion in
                if let hashDict = json as? [String: String] {
                let hashName = hashDict["hashName"] ?? ""
                let hashStringWithoutSalt = hashDict["hashString"] ?? ""
                    let hashWithSalt = hashStringWithoutSalt.appending(kSalt)
                    let hash = hashWithSalt.sha512()
                    hashcompletion!([hashName : hash])
                }
            },
            completionBlockForAPIResponse: { [weak self] offerDetails, errorMsg, _ in
                print("offerDetails......\(offerDetails)")
            })
```
</Accordion>

</Accordion>

<Accordion title="Validate Offer Details API" icon="fa-code">
Use the **Validate Offer Details** API to validate the offer available for the merchant.

> 📘 Hash Generation Logic
>
> In `completionBlockForHashGeneration`. you will get hash string without salt so you need to append the salt at the end of this hash string and convert using sha512 and pass that value in hash completion as passing below in the code.

<Accordion title="Integration" icon="fa-code">
1. Set amount and userToken inside your payment parameters for instance

```swift Swift
        paymentParamForPassing.amount = "amount"
        paymentParamForPassing.cardNumber = "Card Number"
        paymentParamForPassing.offerParams = PayUModelOfferParams()
        paymentParamForPassing.offerParams?.userToken = "Any default Value"
        paymentParamForPassing.offerParams?.offerKeys = ["Offer Key"]
        paymentParamForPassing.offerParams?.paymentCode = "CC/DC/NB"
        paymentParamForPassing.category = "CREDITCARD"
```

2. Call the `validateOfferDetails()` method to integrate this API as described in the following code block

```swift Swift
webServiceResponse?.validateOfferDetails(paymentParamForPassing, completionBlockForHashGeneration: { json, hashcompletion in
            if let hashDict = json as? [String: String] {
            let hashName = hashDict["hashName"] ?? ""
            let hashStringWithoutSalt = hashDict["hashString"] ?? ""
            let hashWithSalt = hashStringWithoutSalt.appending(kSalt)
            let hash = hashWithSalt.sha512()
            hashcompletion!([hashName : hash])
            }
        }, completionBlockForAPIResponse: { [weak self] offerDetails, errorMsg, json in
            print("offerDetails......\(offerDetails)")
        })
```
</Accordion>

</Accordion>

<Accordion title="Get EMI According to Interest API" icon="fa-code">
The **Get EMI According to Interest** API helps you get details of all the available EMIs.

To integrate this API:

1. Set the amount in the payment parameter for this API as described in the following code block.

```swift Swift
self.paymentParamForPassing.amount = @"100"; self.paymentParamForPassing.hashes.EMIDetailsHash = @"hash";
```
```objectivec Objective-C
[webServiceResponse getOfferStatus:self.paymentParamForPassing withCompletionBlock:^(PayUModelOfferStatus *offerStatus, NSString *errorMessage, id extraParam) {
    if (errorMessage == nil) {
        //It is good to go & offerStatus.discount contains the discounted amount if there is any offer & offerStatus.msg contains the message why offer is not available
    }
    else{
        // Something went wrong errorMessage is having the Detail
    }
}];
```

2. Call the `getEMIAmountAccordingToInterest` method to integrate this API as described in the following code block:

```swift Swift
[webServiceResponse
getEMIAmountAccordingToInterest:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictEMIDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictEMIDetails is having the EMI detail
      }
    }];
```
```objectivec Objective-C
[webServiceResponse
getEMIAmountAccordingToInterest:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictEMIDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictEMIDetails is having the EMI detail
      }
    }];
```
</Accordion>

<Accordion title="Verify Payment API" icon="fa-code">
The Verify Payment API is used to reconcile the transaction with PayU. When PayU posts back the final response to you (merchant), PayU provides a list of parameters (including the status of the transaction). For example, success, failure, etc. On a few occasions, the transaction response is initiated from our end, but it does not reach you due to network issues or user activity (like refreshing the browser, etc.).

The command name and var1 for this API integration are:

* Command Name - verify_payment
* Var1 - txnId

> 📘 Note:
>
> PayU strongly recommends that this API is used to reconcile with PayU's database once you receive the response. This will protect you from any tampering by the user and help in ensuring safe and secure transaction experience.

> 📘 Hash logic
>
> The hash will be in the format of:
>
> `Sha512(Key|Command|Var1|Salt)`
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Accordion>

<Accordion title="Integration" icon="fa-code">
1. Set `transactionID` inside your payment parameters for instance:

```swift Swift
self.paymentParamForPassing.transactionID = "tnxID";
self.paymentParamForPassing.hashes.verifyTransactionHash = "hash";
```
```objectivec Objective-C
self.paymentParamForPassing.transactionID = @"tnxID1|txnID2|txnID3";
self.paymentParamForPassing.hashes.verifyTransactionHash = @"hash";
```

> Note: You can send multiple txnIDs (transaction IDs) using the pipe symbol(|) as a separator.

2. Call the `verifyPayment()` method to integrate this API as described in the following code block:

```swift Swift
webServiceResponse?.verifyPayment(paymentParamForPassing, withCompletionBlock: { result, error, json in
            completion(result,error,json)
          if (error){

                // Something went wrong errorMessage is having the Detail

            }else{

                // It is good to go & paymentRelatedDetails is having the full detail of it

            }
        })
```
```objectivec Objective-C
[webServiceResponse
verifyPayment:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictVerifyPayment, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictVerifyPayment is having the verifyPayment detail
      }
    }];
```
</Accordion>

<Accordion title="Check is Domestic API" icon="fa-code">
The **Check is Domestic** API is used to get the following using the BIN number, that is, the first six digits of a credit card or debit card:

* BIN information
* Detect whether a particular BIN number is international or domestic.
* Determine the card's issuing bank, the card type brand, that is, Visa, Master, etc.,
* Determine the card category, that is, credit, debit, etc.

The command name and var1 will be:

* Command Name - check_isDomestic
* Var1 - Card Number(Like. "5123456789012346")

> 📘 Hash logic
>
> The hash will be in the format of:
>
> `Sha512(Key|Command|Var1|Salt)`
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Accordion>

<Accordion title="Integration" icon="fa-code">
1. Set `cardNumber` in the payment params similar to the following code block:

```swift Swift
self.paymentParamForPassing.cardNumber = "5123456789012346";
self.paymentParamForPassing.hashes.checkIsDomesticHash = "hash";
```
```objectivec Objective-C
self.paymentParamForPassing.cardNumber = @"5123456789012346";
self.paymentParamForPassing.hashes.checkIsDomesticHash = @"hash";
```

2. Call the checkIsDomestic method to integrate this API as described in the following code block:

```swift Swift
   webServiceResponse?.checkIsDomestic(paymentParamForPassing, withCompletionBlock: { result, error, json in 
          completion(result, error, json)
            
     if (error){

                // Something went wrong errorMessage is having the Detail

            }else{

                // It is good to go & paymentRelatedDetails is having the full detail of it

            }
        })
```
```objectivec Objective-C
[webServiceResponse
verifyPayment:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictVerifyPayment, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // dictVerifyPayment is having the verifyPayment detail
      }
    }];
```
</Accordion>

<Accordion title="Get Transaction Info API" icon="fa-code">
The **Get Transaction Info** API is used to extract the transaction details between two given time periods. The API takes the input as two dates and the time (initial and final) between which the transaction details are needed. The output would consist of the status of the API (success or failed) and all the transaction details in an array format.
</Accordion>

<Accordion title="Integration" icon="fa-code">
1. Set `startTime` and `endTime` in the payment params as described in the following code block:

```objectivec Objective-C
self.paymentParamForPassing.startTime = @"2014-01-12 16:00:00";
self.paymentParamForPassing.endTime = @"2014-01-12 16:00:50";
self.paymentParamForPassing.hashes.getTransactionInfoHash = @"hash";
```

1. Call the `getTransactionInfo` method to integrate with this API as described in the following code block:

```objectivec Objective-C
[webServiceResponse
getTransactionInfo:self.paymentParamForPassing withCompletionBlock:^(NSArray *arrOfGetTxnInfo, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // arrOfGetTxnInfo is the array of PayUModelGetTxnInfo which is having detail of transaction
      }
    }];
```
</Accordion>

<Accordion title="Get BIN Info API" icon="fa-code">
The **Get Bin Info** API is used to detect whether a particular BIN number is international or domestic. In addition, it is useful to determine the card's issuing bank, the card type brand, that is, Visa, Mastercard, etc., and the card category, that is, credit card, debit card, etc. The BIN number is the first six digits of a credit or debit card. This API is also helpful in knowing whether the card BIN is eligible for Standing Instructions. For this API, you need to set the card number in the payment parameters.

The command name and var1 for this API integration are:

* Command Name - getBinInfo
* Var1 - 1
* Var5 - 1  if you want to check card supports SI and pass the isSIInfo as true.

> 📘 Hash format
>
> The hash will be in the format of:
>
> `Sha512(Key|Command|Var1|Salt)`
>
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Accordion>

<Accordion title="Integration" icon="fa-code">
1. Set the following parameter in the payment params similar to the following code block:

```swift Swift
self.paymentParamForPassing.cardNumber = "5123456789012346"
self.paymentParamForPassing.isSIInfo = true
self.paymentParamForPassing.hashes.getBinInfoHash = "hash"
```
```objectivec Objective-C
self.paymentParamForPassing.cardNumber = @"5123456789012346";
self.paymentParamForPassing.isSIInfo = @"true";
self.paymentParamForPassing.hashes.getBinInfoHash = @"hash";
```

2. Call the GetBINInfo method to integrate with this API as described in the following code block:

```swift Swift
 webServiceResponse?.getBinInfo(paymentParamForPassing, withCompletionBlock: { result, error, json in
            completion(result, error, json)
          
     if (error){

                // Something went wrong errorMessage is having the Detail

            }else{

                // It is good to go & paymentRelatedDetails is having the full detail of it

            }

        })
```
```objectivec Objective-C
[webServiceResponse
getTransactionInfo:self.paymentParamForPassing withCompletionBlock:^(NSArray *arrOfGetTxnInfo, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // arrOfGetTxnInfo is the array of PayUModelGetTxnInfo which is having detail of transaction
      }
    }];
```
</Accordion>

<Accordion title="Get Checkout Details API" icon="fa-code">
The **Get Checkout Details** API provides information on `additionalCharges`, `bankDownStatus`, `taxSpecification`, `offerDetails`, `customerEligibility`, `merchantDetails`, `extendedPaymentDetails`, and pg id information for payment options on a merchant key.

To integrate this API:

1. Call this API is similar to other Web Services, the only difference is that it requires a JSON in var1. Check the following code block for more details. Here, requestId is a unique random number passed in the request.

```json JSON Response
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

```objectivec Objective-C
self.paymentParamForPassing.getExtendedPaymentDetails = true; 
self.paymentParamForPassing.checkTaxSpecification = true;      
self.paymentParamForPassing.checkDownStatus = true;   self.paymentParamForPassing.checkAdditionalCharges = true;      
self.paymentParamForPassing.checkOfferDetails = true;   self.paymentParamForPassing.getPgIdForEachOption = true;     self.paymentParamForPassing.checkCustomerEligibility = true;   
self.paymentParamForPassing.getMerchantDetails = true;          self.paymentParamForPassing.getPaymentDetailsWithExtraFields = true;     
self.paymentParamForPassing.amount = @"<Amount>";   self.paymentParamForPassing.hashes.getCheckoutDetailsHash = @"hash";         PayUModelGetCheckoutAPIFilters *getCheckoutAPIFilters = [PayUModelGetCheckoutAPIFilters new];         getCheckoutAPIFilters.dcEMIBankCode = @"<BankCode>";         getCheckoutAPIFilters.cardlessEMIBankCode = @"<BankCode>";         getCheckoutAPIFilters.bnplBankCode = @"<BankCode>";        self.paymentParamForPassing.getCheckoutAPIFilters = getCheckoutAPIFilters;
```

3. Call the `getCheckoutDetail` to integrate this API:

```objectivec Objective-C
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

The **Lookup** API is used when integrating multi-currency payments. To use Lookup API for iOs, follow these subsections:

* [Prerequisites](#Prerequisites)
* [Request parameters](#Request-parameters)
* [Calculate the signature for Hash](#calculate-the-signature-for-hash)

<Accordion title="Prerequisites for Lookup API" icon="fa-code">
> 📘 Before you begin
>
> Connect with your Key Account Manager at PayU to get the following credentials:
>
> * Merchant Access Key
> * Merchant Secret Key

Lookup API needs a JSON request. Product types need to be passed either as DCC or MCP. Direct Currency Conversion (DCC) returns the conversion prices for card currency only. To get all enabled currencies on Merchant Access Key along with their conversion prices, use product type as MCP. For DCC, cardBin is mandatory, while for MCP cardBin is not required

The following example is to request for MCP as a product type:

```json JSON
{   
  "merchantAccessKey":"E5ABOXOWAAZNXB6JEF5Z", 
  "baseAmount":
  {     
    "value":10000.00,      
     "currency":"INR"   
   },   
    "merchantOrderId":"OBE-JU89-13151-110",   
    "productType":"MCP",   
    "signature":"be5a56667354d9e2ea5ea1c6af78b0afc1894eb2"
  }
```

For this API you need to set the `amount`, `lookupAPIHash`, and `lookuprequestId` parameters in the payment parameters for instance.

```objectivec Objective-C
self.paymentParamForPassing.amount = @"Total amount";
self.paymentParamForPassing.hashes.lookupApiHash = @"HMACSHA1 Signature";
self.paymentParamForPassing.lookupRequestId = @"Any unique id";
```
</Accordion>

<Accordion title="Request parameters" icon="fa-code">
The details of the parameters used in the **Lookup** API are:

| Parameter           | `Description`                                                                                                         |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| Amount              | Transaction Amount                                                                                                    |
| Card Bin            | First 6 digits of the card number                                                                                     |
| Currency            | Base Currency of Transaction ("INR")                                                                                  |
| Merchant Access Key | Merchant Access Key provided by PayU                                                                                  |
| Merchant OrderId    | A unique request id for the Lookup API request                                                                        |
| Product Type        | Use MCP to get all enabled currency on Merchant Access Key or DCC to get direct currency conversion for card currency |
| Signature           | Hmac SHA1 hash created with formula explained below                                                                   |
</Accordion>

<Accordion title="Calculate the signature for hash" icon="fa-code">
Use the following data to calculate the signature for creating the HmacSHA1 hash.

* `Signature` =HMAC-SHA1(data, key);
* `Data` = baseCurrency+merchantOrderId+baseAmount
* `Key` = Secret Key shared with the merchant at the time of onboarding
* `Example`: INROBE-JU89-13151-11010000.00

To integrate this API, call the `mcpLookup `method for instance:

```objectivec Objective-C
[webServiceResponse
mcpLookup:self.paymentParamForPassing withCompletionBlock:^(PayUModelMultiCurrencyPayment *paymentRelatedDetails, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // PayUModelMultiCurrencyPayment object is having the required detail
      }
}];
```

> 📘 Reference:
>
> For more information on Static Hashing, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Accordion>

</Accordion>

<Accordion title="Check Pluxee Card Balance API" icon="fa-code">
The **Check Pluxee Card Balance** API can be used to fetch detail of the Sodexo card with the source ID.

1. Set the sodexoSourceId and checkBalanceApiHash parameter for instance:

```objectivec Objective-C
self.paymentParamForPassing.sodexoSourceId = @"<Sodexo source id>;
self.paymentParamForPassing.hashes.checkBalanceApiHash =  @"hash";
```

2. Call the `fetchSodexoCardDetails` method to integrate with this API similar to the following code block:

```objectivec Objective-C
[webServiceResponse
fetchSodexoCardDetails.paymentParamForPassing withCompletionBlock:^(PayUModelSodexoCardDetail *sodexoCardDetail, NSString *errorMessage, id extraParam) {
      if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
      }
      else{
        // sodexoCardDetail object is having the required detail
      }
    }];
```
</Accordion>

<Accordion title="Tokenized Payment Integration" icon="fa-code">
You can store and get stored card details from the vault.

<Accordion title="Get Tokenized Payment details" icon="fa-code">
1. Get details of the stored card to make payment on another PG.

```objectivec Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParam.cardToken = @"<cardToken>";    
self.paymentParam.amount = @"100";  
self.paymentParam.currency = @"INR";
self.paymentParamForPassing.hashes.getTokenizedPaymentDetailHash = @"hash";
```

2. Call the `getTokenizedPaymentDetails` method to integrate this similar to the following:

```objectivec Objective-C
[webServiceResponse getTokenizedPaymentDetails.paymentParamForPassing withCompletionBlock:^(PayUModelTokenizedPaymentDetails *tokenizedPaymentdetails,NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```
</Accordion>

<Accordion title="Get tokenized store Cards" icon="fa-code">
The Get tokenized store cards is helpful in getting all the stored cards for a particular user.

1. Set the`userCredentials` in the payment params similar to the following:

```objectivec Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParamForPassing.hashes.getTokenizeddStoredCardHash = @"hash";
```

2. Call the getTokenizedStoredCards method to integrate this API similar to the following:

```objectivec Objecitve-C
[webServiceResponse getTokenizedStoredCards:self.paymentParamForPassing withCompletionBlock:^(NSDictionary *dictStoredCard,NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```
</Accordion>

<Accordion title="Delete tokenised stored cards" icon="fa-code">
This API is helpful in deleting stored cards.

1. Set the`userCredentials` in the payment params similar to the following:

```objectivec Objective-C
self.paymentParam.userCredentials = @"<user_credentials>";  
self.paymentParam.cardToken = @"<cardToken>";    
self.paymentParam.networkToken = @"<networkToken>";  
self.paymentParam.issuerToken = @"<issuerToken>";
self.paymentParamForPassing.hashes.deleteTokenizedStoredCardHash = @"hash";
```

2. Call the `deleteTokenizedStoredCard` method to integrate this API similar to the following:

```objectivec Objective-C
[webServiceResponse deleteTokenizedStoredCard:self.paymentParamForPassing withCompletionBlock:^(NSString *deleteStoredCardStatus, NSString *deleteStoredCardMessage, NSString *errorMessage, id extraParam) {
            if (errorMessage) {
        // Something went wrong errorMessage is having the Detail
            }
            else{
        //It is good to go & deleteStoredCardMessage is having the full detail of it
            }
        }];
```
</Accordion>

</Accordion>