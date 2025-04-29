---
title: Lookup API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Lookup API - iOS Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Lookup** API is used when integrating multi-currency payments. To use Lookup API for iOs, follow these subsections:

- [Prerequisites](#Prerequisites)
- [Request parameters](#Request-parameters)
- [Calculate the signature for Hash](#calculate-the-signature-for-hash)

## Prerequisites

> 📘 Before you begin
> 
> Connect with your Key Account Manager at PayU to get the following credentials:
> 
> - Merchant Access Key
> - Merchant Secret Key

Lookup API needs a JSON request. Product types need to be passed either as DCC or MCP. Direct Currency Conversion (DCC) returns the conversion prices for card currency only. To get all enabled currencies on Merchant Access Key along with their conversion prices, use product type as MCP. For DCC, cardBin is mandatory, while for MCP cardBin is not required

The following example is to request for MCP as a product type:

```Text JSON
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

```Text Objective-C
self.paymentParamForPassing.amount = @"Total amount";
self.paymentParamForPassing.hashes.lookupApiHash = @"HMACSHA1 Signature";
self.paymentParamForPassing.lookupRequestId = @"Any unique id";
```

## Request parameters

The details of the parameters used in the **Lookup** API are:

| Parameter           | `Description`                                                                                                         |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| Amount              | Transaction Amount                                                                                                    |
| Card Bin            | First 6 digits of the card number                                                                                     |
| Currency            | Base Currency of Transaction (“INR”)                                                                                  |
| Merchant Access Key | Merchant Access Key provided by PayU                                                                                  |
| Merchant OrderId    | A unique request id for the Lookup API request                                                                        |
| Product Type        | Use MCP to get all enabled currency on Merchant Access Key or DCC to get direct currency conversion for card currency |
| Signature           | Hmac SHA1 hash created with formula explained below                                                                   |

## Calculate the signature for hash

Use the following data to calculate the signature for creating the HmacSHA1 hash.

- `Signature` =HMAC-SHA1(data, key);
- `Data` = baseCurrency+merchantOrderId+baseAmount
- `Key` = Secret Key shared with the merchant at the time of onboarding
- `Example`: INROBE-JU89-13151-11010000.00

To integrate this API, call the `mcpLookup `method for instance:

```Text Objective-C
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