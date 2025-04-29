---
title: Create SKU Based Offers for Android Checkout Pro
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
PayU allows merchants to create offers for specific Products/SKUs in the cart and for whole cart. SKU offers will be shown only when the specific product is added by the user and hence can be used by the merchant to promote specific products.

# Create an offer on dashboard

1. Merchant Creates offers on dashboard. For SKU offers they need to provide product details with skuid, sku price range.
2. Merchant pass these sku details and user token when he initialising CheckoutPro SDK.
3. SDK fetch offers from PayU Server and show list of offers.
4. User can select any offer and can see the benefit (instant/ cashback) of offer.
5. If user did not select any offer we will auto apply best offer.
6. User can pay offered amount and can avail offers.

# Steps to integrate

1. [Step 1: Update depencies](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro#step-1-update-dependencies)
2. [Step 2: Initialise the SDK](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro#step-2-initialise-the-sdk)
3. [Step 3: Create SKU Details](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro#step-3-create-sku-details)
4. [Step 4: Set SKU Details](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro#step-4-set-sku-details)
5. [Step 5: Generate Hash](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro#generate-hash)

## Step 1: Update dependencies

Add below dependency in your app level gradle file.

```
implementation 'in.payu:payu-checkout-pro:2.2.1'
```

## Step 2: Initialise the SDK

> 🚧 Make sure you integrate with CheckoutPro SDK for Android
> 
> Refer to [Android CheckoutPro Integration Steps](doc:android-checkoutpro-integration-steps) integrate Checkout Pro in App.

## Step 3: Create SKU Details

 Initalise Object of SKU details with vaild SKU’s.

```Text kotlin
SkuDetails: It contains below properties
SkuDetails(val skus: List<SKU>)
skus: "<ArrayList of SKU>"

SKU(
    val quantity: Int,
    val skuAmount: String,
    val skuId: String,
    val skuName: String,
    var offerKeys:ArrayList<String>?=null
)

skuId: "<Product Id which you use when creating offer on dashboard >"
skuName: "<Name of product>"
skuAmount: "<Amount of product>"
quantity: "<total quantity of product>"
offerKeys: "<Optional - Provide offer keys only if want to restrict offer for mention products, else set null>"

 
```

## Step 4: Set SKU Details

Create list of SKU as per products added in cart and add this list in SKU details. and set sku detials to `PayUPaymentParams`.

```Text kotlin
PayUPaymentParams.Builder()
        .setAmount(<String>)  
        .setIsProduction(<Boolean>)  //set is to true for Production and false for UAT
        .setProductInfo(<String>)   
        .setKey(<String>)      
        .setPhone(<String>)      
        .setTransactionId(<String>)  
        .setFirstName(<String>) 
        .setEmail(<String>) 
        .setSurl(<String>) //Pass your own surl your
        .setFurl(<String>) //Pass your own furl your
        .setUserCredential(<String>) // Optional, 
        .setAdditionalParams(<HashMap<String,Object>>); 
        .setPayUSIParams(<SiDetails>)// only for SI transaction
        .setSkuDetails(<SkuDetails>) // create SKU Details as mention above
        .setUserToken(<String>) // compulsory to fetch offer
        .build()
```

> 🚧 Keep in mind
> 
> if we are adding details of SKU offers, the amount passed in PayUPaymentParam must be equal to the sum of quantities skuAmount of each item.

## Step 5: Generate Hash

This integration requires dynamic hashes. We will get hash string in map again `CP_HASH_STRING `key in generateHash.  We need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to SDK.

```Text kotlin
public void generateHash(@NotNull HashMap map, @NotNull PayUHashGenerationListener hashGenerationListener) { 
}

```