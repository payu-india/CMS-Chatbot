---
title: Offer APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Offer APIs - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The following APIs used for offers with Android Core SDK:

* [Fetch Offer Details](fetch-offer-details)
* [Validate Offer Details](#validate-offer-details)

## Fetch Offer Details

Use this API to fetch the offer list available for the merchant.

To integrate this API call the fetchOfferDetails pass the requestData as parameters as shown in the code snippet below:

```Text Java
payuConfig = new PayuConfig();
payuConfig.setEnvironment(PayuConstants.STAGING_ENV);

V2ApiTask v2ApiTask = new V2ApiTask(merchantKey, payuConfig);
FetchOfferApiRequest fetchOfferApiRequest = new FetchOfferApiRequest.Builder().setAmount(100.00).setUserToken("56789067890").build();
v2ApiTask.getOffers(fetchOfferApiRequest, new HashGenerationListener() {
    @Override
    public void generateSignature(HashMap<String, String> hashMap, HashCompletionListener hashCompletionListener) {
        String hashName = hashMap.get(PayuConstants.CP_HASH_NAME);
        String hashData = hashMap.get(PayuConstants.CP_HASH_STRING);
        Log.d(TAG, "generateSignature: " + hashName);
        Log.d(TAG, "generateSignature: " + hashData);
        String hash = HashGenerationUtils.generateHashFromSDK(hashData, salt);
        HashMap hashMap1 = new HashMap();
        hashMap1.put(hashName, hash);
        hashCompletionListener.onSignatureGenerated(hashMap1);  // If you are passing wrong Hash then you will get null response
    }
}, new FetchOfferDetailsListener() {
    @Override
    public void onFetchOfferDetailsResponse(PayuResponse payuResponse) {
        Log.d(TAG, "onFetchOfferDetailsResponse: " + payuResponse.getRawResponse());
    }
});
```

## Validate Offer API

Use this API to validate the offer for the merchants.

To integrate this API call the method  validateOfferDetails and pass the requestData as parameters as shown in the code snippet below:

```Text Java
List<String> offerKey = new ArrayList<>();
offerKey.add("<pass the offer key>");

PaymentDetailsForOffer paymentDetailsForOffer = new PaymentDetailsForOffer.Builder().setPaymentCode("CC").setCardNumber("5123456789012346").setCategory("CREDITCARD").build();

UserDetailsForOffer userDetailsForOffer = new UserDetailsForOffer.Builder().setUserToken("56789067890").build();

payuConfig = new PayuConfig();
payuConfig.setEnvironment(PayuConstants.STAGING_ENV);

V2ApiTask v2ApiTask = new V2ApiTask(merchantKey, payuConfig);
ValidateOfferRequest validateOfferRequest = new ValidateOfferRequest.Builder().setAmount("100.00").setOfferKey(offerKey).setPaymentDetails(paymentDetailsForOffer).setuserDetails(userDetailsForOffer).setAutoApply(false).build();
v2ApiTask.validateOffers(validateOfferRequest, new HashGenerationListener() {
    @Override
    public void generateSignature(HashMap<String, String> hashMap, HashCompletionListener hashCompletionListener) {
        String hashName = hashMap.get(PayuConstants.CP_HASH_NAME);
        String hashData = hashMap.get(PayuConstants.CP_HASH_STRING);
        Log.d(TAG, "generateSignature: " + hashName);
        Log.d(TAG, "generateSignature: " + hashData);
        String hash = HashGenerationUtils.generateHashFromSDK(hashData, salt);
        HashMap hashMap1 = new HashMap();
        hashMap1.put(hashName, hash);
        hashCompletionListener.onSignatureGenerated(hashMap1);  // If you are passing wrong Hash then you will get null response
    }
}, new ValidateOfferApiListener() {
    @Override
    public void onValiDateOfferResponse(PayuResponse payuResponse) {
        Log.d(TAG, "onValiDateOfferResponse: " + payuResponse.getRawResponse());
    }
});
```
