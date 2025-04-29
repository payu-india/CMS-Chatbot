---
title: Lookup API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Lookup API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Lookup** API is used when integrating Multi-Currency Payments on Android Core SDK.

## Step 1: Create request

The Lookup API needs a JSON request. Product type needs to be passed either as DCC or MCP. DCC means Direct Currency Conversion, that is, it returns the conversion prices for card currency only. To get all enabled currencies on Merchant Access Key and their conversion prices, use product type as MCP. For DCC, cardBin is mandatory, but cardBin is not required for MCP.  
The following example is a request for DCC as the product type:

```Text JSON
{
   "merchantAccessKey":"E5ABOXOWAAZNXB6JEF5Z",
   "baseAmount":{
      "value":10000.00,
      "currency":"INR"
   },
   "cardBin":"513382",
   "merchantOrderId":"OBE-JU89-13151-110",
   "productType":"DCC",
   "signature":"be5a56667354d9e2ea5ea1c6af78b0afc1894eb2"
}
```

To create the Lookup API request as above, use the LookupApiRequestBuilder class similar to the following code block:

```Text JAVA
String postData = new LookupRequest.LookupApiRequestBuilder()
                .setAmount("10000.00")
                .setCardBin("513382")
                .setCurrency("INR")
                .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                .setMerchantOrderId("OBE-JU89-13151-110")
                .setProductType(LookupRequest.ProductType.DCC)
                .setSignature(hash)
                .build().prepareJSON();
```
```Text Kotlin
 val postData = LookupRequest.LookupApiRequestBuilder()
                .setAmount("10000.00")
                .setCardBin("513382")
                .setCurrency("INR")
                .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                .setMerchantOrderId("OBE-JU89-13151-110")
                .setProductType(LookupRequest.ProductType.DCC)
                .setSignature(hash)
                .build().prepareJSON()
```

The following example request is for MCP as the product type.

```Text JSON
{
   "merchantAccessKey":"E5ABOXOWAAZNXB6JEF5Z",
   "baseAmount":{
      "value":10000.00,
      "currency":"INR"
   },
   "merchantOrderId":"OBE-JU89-13151-110",
   "productType":"MCP",
   "signature":"be5a56667354d9e2ea5ea1c6af78b0afc1894eb2"
}
```

To create the Lookup API request for MCP, use the LookupApiRequestBuilder class similar to the following code block:

```Text JAVA
String postData = new LookupRequest.LookupApiRequestBuilder()
                .setAmount("10000.00")
                .setCurrency("INR")
                .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                .setMerchantOrderId("OBE-JU89-13151-110")
                .setProductType(LookupRequest.ProductType.MCP)
                .setSignature(hash)
                .build().prepareJSON();
```
```Text Kotlin
 val postData = LookupRequest.LookupApiRequestBuilder()
                .setAmount("10000.00")
                .setCurrency("INR")
                .setMerchantAccessKey("E5ABOXOWAAZNXB6JEF5Z")
                .setMerchantOrderId("OBE-JU89-13151-110")
                .setProductType(LookupRequest.ProductType.MCP)
                .setSignature(hash)
                .build().prepareJSON()
```

| Parameter Name      | Description                                                                                                           |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| Amount              | Transaction Amount                                                                                                    |
| Card Bin            | First 6 digits of card number                                                                                         |
| Currency            | Base Currency of Transaction                                                                                          |
| Merchant Access Key | Merchant Access Key provided by PayU                                                                                  |
| Merchant OrderId    | A unique request id for Lookup API request                                                                            |
| Product Type        | Use MCP to get all enabled currency on Merchant Access Key or DCC to get direct currency conversion for card currency |
| Signature           | Hmac SHA1 hash created with formula explained below                                                                   |

To calculate signature, create the `HmacSHA1` hash of the following data:

```
Signature =HMAC-SHA1(data, key);
Data = baseCurrency+merchantOrderId+baseAmount
Key = Secret Key shared with the merchant at the time of on-boarding
Example data,
baseCurrency = "INR"
merchantOrderId = "OBE-JU89-13151-110"
baseAmount = "10000.00"
hashString = INROBE-JU89-13151-11010000.00
```

## Step 2: Call LookupTask

Here, this is an object of a class that implements `LookupApiListener`. The following is a signature of LookupApiListener:

```Text JAVA
public interface LookupApiListener {
    void onLookupApiResponse(PayuResponse payuResponse);
}
```
```Text Kotlin
interface LookupApiListener {
    fun onLookupApiResponse(payuResponse: PayuResponse?)   
}
```

## Step 3: Get LookUp API response

After you execute LookupTask, the `onLookupApiResponse` callback method is called:

```Text JAVA
@Override
public void onLookupApiResponse(PayuResponse payuResponse){    
    
    //Fetch lookup Details using below code
    LookupDetails lookupDetails = payuResponse.getLookupDetails();     
    }
```
```Text Kotlin
override fun onLookupApiResponse(payuResponse: PayuResponse?){    
    
    //Fetch lookup Details using below code
    val lookupDetails = payuResponse.lookupDetails
    }
```