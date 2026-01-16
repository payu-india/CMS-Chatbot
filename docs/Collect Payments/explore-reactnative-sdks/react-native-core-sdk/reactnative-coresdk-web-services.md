---
title: Web Services
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
---
title: Web Services
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
React Native Core SDK consists of the following APIs:

* [Get Bin Info](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-bin-info)
* [Get Card Information (Check isDomestic)](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-card-information-check-isdomestic)
* [Get Checkout Details](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-checkout-details)
* [Get EMI Information](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-emi-information)
* [Validate Offer](https://docs.payu.in/docs/reactnative-coresdk-web-services#validate-offer)
* [Fetch Offer Details](https://docs.payu.in/docs/reactnative-coresdk-web-services#fetch-offer-details)
* [Get Tokenised Card](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-tokenised-card)
* [Get Tokenised Card Details](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-tokenised-card-details)
* [Delete Tokenised Card](https://docs.payu.in/docs/reactnative-coresdk-web-services#delete-tokenised-card)
* [Get Ibibo Codes](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-ibibo-codes)
* [Get Config](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-config)
* [Fetch IFSC Details](https://docs.payu.in/docs/reactnative-coresdk-web-services#fetch-ifsc-details)
* [Check Balance – Sodexo](https://docs.payu.in/docs/reactnative-coresdk-web-services#check-balance--sodexo)
* [Verify Payment](https://docs.payu.in/docs/reactnative-coresdk-web-services#verify-payment)
* [Get Value-Added Service](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-value-added-service)
* [Lookup API](https://docs.payu.in/docs/reactnative-coresdk-web-services#lookup-api)
* [Build Payment Request Data](https://docs.payu.in/docs/reactnative-coresdk-web-services#build-payment-request-data-7)
* [Get Transaction Data](https://docs.payu.in/docs/reactnative-coresdk-web-services#get-transaction-data)
* [Fetch Payment Options](https://docs.payu.in/docs/reactnative-coresdk-web-services#fetch-payment-options)

***

## Get Bin Info

Use this API to get the details of the `cardBin` passed in the request. When you call this API, you get the card\_type, category, issuing\_bank, `is_atmpin_card` as the response.

To integrate this API, call the getBinInfo  command and pass the payment `requestdata` and the payment hash as parameters as shown in the code snippet below:

```javascript
const response  =  await PayUSdk.getBinInfo({  
  ...requestData,    
  hash: getBinInfoHash(requestData)  
});
```

<Accordion title="Build Request Data Object" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {
  ...requestData,
  isBinInfo: '1',
  cardNumber: '555676',  
  command: 'getBinInfo'
}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getBinInfoHash = (payUData) => {
  payUData.var1 = (payUData.isBinInfo)? payUData.isBinInfo : DEFAULT
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Card Information (Check isDomestic)

Use this API to check if the card (passed in cardBin info API) is domestic or international. This API returns the following parameters: card\_type, category, issuing\_bank, is\_atmpin\_card, etc.

To integrate this API call the method getBinInfo and pass the`requestData` and Hash as parameters  as shown in the code snippet below:

```javascript
const response  =  await PayUSdk.checkIsDomestic({  
  ...requestData,  
  hash: getCheckIsDomesticHash(requestData)  
});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {
  ...requestData,
  cardNumber: <first 6 of card numbe>, //6 digit bin 
  command: 'check_isDomestic'
}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getCheckIsDomesticHash = (payUData) => {
  payUData.var1 = (payUData.cardNumber)? payUData.cardNumber : DEFAULT
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Checkout Details

Use this API to get the checkout details for the merchant. The merchant can pass specific parameters such as axSpecification, DownStatus, and AdditionalCharges and build the payment parameters accordingly.

To integrate this API call the method getCheckoutDetails and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.getCheckoutDetails({
    ...requestData,
    hash: getCheckoutDetailsHash(requestData)
});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata `object as shown in the code snippet below:

```javascript
requestData = {
          ...requestData,
          var1: JSON.stringify({"useCase":
          {"getExtendedPaymentDetails":true,
          "getTaxSpecification":true,
          "checkDownStatus":true,
          "getAdditionalCharges":true,
          "getOfferDetails":true,
          "getPgIdForEachOption":true,
          "checkCustomerEligibility":true,
          "getMerchantDetails":true,
          "getPaymentDetailsWithExtraFields":true,
          "getSdkDetails":true},
          "requestId":"211219214632",
          "customerDetails":{"mobile":"9876543210"},
          "transactionDetails":{"amount":"1"}
    }),
 command: GET_CHECKOUT_DETAILS
}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getCheckoutDetailsHash = (payUData) => {
  payUData.var1 = (payUData.var1)? payUData.var1 : DEFAULT
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get EMI Information

Use this API to get information to get details related to EMI such as EMI amount, tenure in month, interest rate, etc.

To integrate this API call the method getEMIDetails and pass the`requestData` and Hash as a parameter as shown in the code snippet below:

```javascript
const response  =  await PayUSdk.getEMIDetails({  
  ...requestData,  
  hash: getEMIDetailHash(requestData)  
});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData  =  {  
  ...requestData,  
  amount: '2000',  
  command: 'getEmiAmountAccordingToInterest' 
}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getEMIDetailHash = (payUData) => {
  payUData.var1 = (payUData.amount)? payUData.amount : DEFAULT
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Validate Offer

Use this API to validate the offer for the merchants.

To integrate this API call the method validateOfferDetails and pass the `requestData` as parameters as shown in the code snippet below:

```javascript
const response  =  await PayUSdk.getEMIDetails({  
  ...requestData,  
  hash: getEMIDetailHash(requestData)  
});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData  =  {  
  ...requestData,  
  amount: '2000',  
  command: 'getEmiAmountAccordingToInterest' 
}
```
</Accordion>

***

## Fetch Offer Details

Use this API to fetch the offer list available for the merchant.

To integrate this API call the method fetchOfferDetails and pass the `requestData `as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.fetchOfferDetails({  

  ...requestData,  

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

 ...requestData,
 
  amount : 1,
  
  userCredential : "rahul:hooda",
  
  command : "get_all_offer_details"
}
```
</Accordion>

***

## Get Tokenised Card

Use this API to fetch the tokenized card based on the user\_credential for the merchant.

To integrate this API call the method getTokenisedCard and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.fetchOfferDetails({  

  ...requestData,  

});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

 ...requestData,
 
  amount : 1,
  
  userCredential : "rahul:hooda",
  
  command : "get_all_offer_details"
}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getTokenisedCardDetailsHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Tokenised Card Details

Use this API to fetch `one_click_status`, `card_name`, `card_token`, `token_reference_id`, `network_token`, `card_type`, `card_no`, etc.

To integrate this API call the method getTokenisedCardDetails and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.getTokenisedCardDetails({  

  ...requestData,  
  
  hash:getTokenisedCardDetailsHash(requestData)  

});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"rahul:hooda", //User Credential 
  
  var2:"67b442491a8f50793356a6", //Card Token
  
  var3:"100", //Amount 
  
  var4:"INR", //INR 
  
  command: 'get_payment_details'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getTokenisedCardDetailsHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Delete Tokenised Card

Use this API to delete tokenized cards from the saved card list for the merchant.

To integrate this API call the method deleteTokenisedCard and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.getTokenisedCardDetails({  
  ...requestData,  
  hash:getTokenisedCardDetailsHash(requestData)  
});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"rahul:hooda", //User Credential 
  
  var2:"67b442491a8f50793356a6", //Card Token
  
  var3:"100", //Amount 
  
  var4:"INR", //INR 
  
  command: 'get_payment_details'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getTokenisedCardDetailsHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Ibibo Codes

Use this API to fetch the list of Ibibo codes for the merchant along with information such as `pg_id`, `bank_id`, `priority`, `title`, etc.

To integrate this API call the method getIbiboCodes and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.getIbiboCodes({  

  ...requestData,  
  
  hash:getIbiboCodesHash(requestData)  

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"default" ,
  
  command: 'get_merchant_ibibo_codes'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getIbiboCodesHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Config

Use this API to fetch the config for the merchant.

To integrate this API call the method getConfig and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.getIbiboCodes({  

  ...requestData,  
  
  hash:getIbiboCodesHash(requestData)  

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"default" ,
  
  command: 'get_merchant_ibibo_codes'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getIbiboCodesHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Fetch IFSC Details

Use this API to fetch the IFSC details of the IFSC code from the merchant.

To integrate this API call the method fetchIFSCDetails and pass the `requestData` as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.fetchIFSCDetails({  
  
  ...requestData
  
});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the` requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"PUNB0387200"  //IFSC code
}
```
</Accordion>

***

## Check Balance – Sodexo

Use the API to check Sodexo card details, such as:

* Card balance
* Name on the card
* Card number

To integrate this API call the method `checkBalance()` and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.checkBalance({  

  ...requestData,  
  
  hash: getCheckBalanceHash(requestData)  

});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  var1:"{\"sodexoSourceId\":\"src_dcda7c39-47b2-45c4-8656-38d2d67d1715\"}" ,
  
  command: 'check_balance'  

}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getCheckBalanceHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Verify Payment

Use this API to fetch the transaction status of the transactionId passed in the request.

To integrate this API call the method `verifyPayment` and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.verifyPayment({  
  
  ...requestData,  
  
  hash: getVerifyHash(requestData)  

});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  txnId: '1628684808250payusdk',
  
  command: 'verify_payment'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getVerifyHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.txnId}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Get Value-Added Service

Use this API to fetch upStatus/downStatus for different payment modes.

To integrate this API call the method vas and pass the `requestData` and Hash as parameters as shown in the code snippet below:

```javascript
const response = await PayUSdk.verifyPayment({  
  
  ...requestData,  
  
  hash: getVerifyHash(requestData)  

});
```

<Accordion title="Build Payment Parameters" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData = {  

  ...requestData,  
  
  txnId: '1628684808250payusdk',
  
  command: 'verify_payment'  

}
```
</Accordion>

<Accordion title="Generate Payment Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getVerifyHash = (payUData) => {
  var hashString = `${payUData.key}|${payUData.command}|${payUData.txnId}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Lookup API

Use this API to fetch lookUp information for the merchant.

To integrate this API call the method lookupAPI and pass requestData and Hash as parameter as shown in the code snippet below:

```javascript
const response = await PayUSdk.lookupAPI({  
  ...requestData,
  var1: JSON.stringify({
    ...lookupRequestData,
    signature: lookupHash
  }),
  hash: lookupHash

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
lookupRequestData= {  

  "merchantAccessKey": "E5ABOXOWAAZNXB6JEF5Z",
  "baseAmount": {
            "value": "10000",
            "currency": "INR"
          },
  // "cardBin":"513382", // Need cardbin for DCC product
  "merchantOrderId": "OBE-JU89-13151-11009002,
  "productType": "MCP" // Use product DCC or MCP
  command: 'check_balance'  

}
```
</Accordion>

***

## Get Transaction Data

Use this API to fetch transaction information for the merchant according to the request passed in the parameters.

To integrate this API call the method getTransactionInfo and pass the`requestData` and Hash as `parameter` as shown in the code snippet below:

```javascript
const response = await PayUSdk.lookupAPI({  
  ...requestData,
  var1: JSON.stringify({
    ...lookupRequestData,
    signature: lookupHash
  }),
  hash: lookupHash

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
lookupRequestData= {  

  "merchantAccessKey": "E5ABOXOWAAZNXB6JEF5Z",
  "baseAmount": {
            "value": "10000",
            "currency": "INR"
          },
  // "cardBin":"513382", // Need cardbin for DCC product
  "merchantOrderId": "OBE-JU89-13151-11009002,
  "productType": "MCP" // Use product DCC or MCP
  command: 'check_balance'  

}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getGetTransactionInfoHash = (payUData) => {
  payUData.var1 = (payUData.startTime)? payUData.startTime : DEFAULT
  var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
  return sha512(hashString);
}
```
</Accordion>

***

## Fetch Payment Options

Use this API to fetch the available payment options for a customer based on the `userCredential`. In response, this API fetches `savedCard` options, ibiboCodes, and different payment modes for available transactions.

To integrate this API call the method fetchPaymentOptions and pass the`requestData` and Hash as a parameter as shown in the code snippet below:

```javascript
const response  =  await PayUSdk.fetchPaymentOptions({  

  ...requestData,  
  
  hash: getWebHash(requestData)  

});
```

<Accordion title="Build Payment Request Data" icon="fa-code">
Build the `requestdata` object as shown in the code snippet below:

```javascript
requestData  =  {  

  ...requestData,  
  
  userCredentials: "rahul:hooda",  
  
  command: 'payment_related_details_for_mobile_sdk'  

}
```
</Accordion>

<Accordion title="Generate the Hash" icon="fa-key">
Generate the hash with the code snippet shown below:

```javascript
export const getWebHash = (payUData) => {
    payUData.var1 = (payUData.userCredentials)? payUData.userCredentials : DEFAULT
    var hashString = `${payUData.key}|${payUData.command}|${payUData.var1}|${payUData.salt}`;
    return sha512(hashString);
}
```
</Accordion>
