---
title: 1. Integration Steps
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
Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

## Create a PayU account

First, create a PayU account. See [Register for a merchant account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

> 🚧 Download NodeJS SDK
> 
> You can download the NodeJS Web SDK from the following GitHub link: <https://github.com/payu-intrepos/web-sdk-nodejs>

## Install the SDK

Run the following command to install the PayU NodeJS SDK using the NPM:

```Text npm
npm install payu-websdk
```

***

## Build the PayU Object

Use the sample code snippet to build an instance of PayU Object:

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE
```

***

## Initiate the payment

This method genereates an auto-submit HTML form to intitiate the transaction. 

Create a JSON with the payment parameters and pass it as the argument of the `paymentInitiate` method of the `payuClient` object 

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.paymentInitiate(<JSON>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Verify the payment

You must implement this method to verify the status of the payment once the payment is done. Pass the `txnID` as the aggument of the `verifyPayment` method of the payuClient object. 

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.verifyPayment(<txnID>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get transaction details

The `get_Transaction_Details` method takes the START_DATE and END_DATE, and returns the details of all transaction happened during that period. The output consists of the status of the API (success or failed) and all the transaction details in an array format.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getTransactionDetails(<START_DATE>,<END_DATE>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get settlement details

You can use this method to retrieve settlement details which the bank has to settle for you. Pass either the date for which you want to get all the settlement details or the UTR ((Unique Transaction Reference number-alphanumeric))number of the transaction as the argument of the `getSettlementDetails` method. 

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getSettlementDetails(<date/UTR nunmber>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get net banking status

The Get Net Banking Status API (getNetbankingStatus) is used to help you in handling the NetBanking Downtime. A few times, one or more Net Banking options may be facing downtime due to issues observed at the bank’s end. This API is used to tell the status of one or all the Net Banking options. The status can be either up or down. If you want to know the status of a specific Net Banking option, the input parameter should contain the corresponding `ibibo_code`. If you want to know the status of all the Net Banking options, the input parameter should contain the value as default.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getNetbankingStatus(<bankcode>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get issuing bank status

The Get Issuing Bank Status API (getIssuingBankStatus) is used to help you handle the credit card or debit card issuing bank downtime.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getIssuingBankStatus(<bin>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get checkout details

The get_checkout_details API is a generic API using which they can get information when you create the custom checkout-pages, that will contain the payment options, offers, recommendations, and downtime details. The API provides the following details: 

- **Payment option details**: The extended details for each payment option available for the merchant.
- **Additional charges**: The additional charges configured for all payment options.  
  eligibility details
- **Downtime details**: The downtime status of the payment options.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getCheckoutDetails(<JSON>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get emi amount according to interest

The Get EMI Amount According to Interest API (getEmiAmountAccordingToInterest) is used to get the EMI interest bank rates for all the enabled EMIs.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.getEmiAmountAccordingToInterest(<amount>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Create an invoice

The Create Invoice API (create_invoice) allows you to create an email invoice for your customer and provides an option to send the email invoice to the customer either immediately or later through automation.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.createInvoice(<JSON>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Expire an invoice

The Expire Invoice API (expire_invoice) is used to expire an invoice link corresponding to the txnID. In few cases, an invoice might be sent to an incorrect email ID by the merchant. In such scenario, you can discard that invoice by expiring it.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.expireInvoice(<txnID>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Get elligible bins for EMI

The Eligible Bin for EMI API (eligibleBinsForEMI) is used only when the merchant needs the EMI feature of PayU. If you are managing card details on your website, this API can tell the issuing bank of the card bin. It also provides the minimum eligible amount for a particular bank.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.eligibleBinsForEMI(<bin>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Check bin type

The checkIsDomestic method is used to detect whether a particular BIN number is international or domestic. It is also useful to determine:

1. card’s issuing bank
2. card type such as, Visa, Master, etc.
3. card category such as Credit/Debit, etc.
4. var1 is bin number which is the first 6 digits of a Credit/Debit card.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.checkIsDomestic(<bin>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Check action status

The Check Action Status API (check_action_status) is used to check the status of the refund or cancel requests. 

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.checkActionStatus(<request_id>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Cancel refund transactions

The Cancel Refund Transaction API (cancel_refund_transaction) can be used for the following purposes:

1. Cancel a transaction that is in ‘auth’ state at the moment
2. Refund a transaction that is in a ‘captured’ state at the moment.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.cancelRefundTransaction(<MIHPAYUD>,<TOKEN_ID>,<AMOUNT>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Validate VPA

This method will let you validate VPA if it is a valid VPA or not.

After the customer enters VPA on the merchant page, you need to call this API to check for VPA validation. If VPA is valid only then, the second call should be made.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.validateVPA(<VPA>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```

***

## Update UDF

The UDF Update API is used to update the UDF1-UDF5 values of a transaction. UDFs are the user-defined fields which are posted from the merchant to PayU. This API is specifically used to update the values in these fields in the PayU database. The return parameters are the updated UDF values of the transaction.

```Text Node.js
const PayU = require("payu");

const payuClient = new PayU({
  key: <YOUR_MERCHANT_KEY>,
  salt: <YOUR_MERCHANT_SALT>,
},<ENVIRONMENT>);     // Possible value  = TEST/LIVE

payuClient.opgsp.udfUpdate(<JSON>).then((res)=>{
    console.log(res)
}).catch((err)=>{
    console.log(err)
});
```