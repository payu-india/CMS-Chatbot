---
title: Get Checkout Details API
excerpt: Display bank down status, tax info, and offers enabled on a merchant key
deprecated: false
hidden: false
metadata:
  title: Get Checkout Details API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
The **Get Check Out Details** API provides information on the bank down status, tax info, and offers enabled on a merchant key. You can call this API is similar to other Web Services. The only difference is that it requires a JSON in var1 as in the following code block:

```Text JSON
{
   "requestId":"1614595430980",
   "transactionDetails":{
      "amount":5000
   },
    "customerDetails": {
      // optional
      "mobile": "9999999999" // optional
    },
   "useCase":{
      "getAdditionalCharges":true,
      "getTaxSpecification":true,
      "checkDownStatus":true,
      "getExtendedPaymentDetails":true,
      "getOfferDetails":true
   }
}
```

Where the `requestId` is a unique random number passed in the request.

## Step 1: Create the var1

Mobile SDK has a Utility class to create a JSON, as explained above. The implementation is similar to the following code snippet:

```Text JAVA
  Usecase.Builder usecase = new Usecase.Builder()
  .setCheckCustomerEligibility(true)
  .shouldCheckDownStatus(true) // set it to true to fetch bank down status for each payment option 
  .shouldGetAdditionalCharges(true) // set it to true to fetch additional charges applicable on each payment option
  .shouldGetOfferDetails(true) // set it to true to fetch offers enabled on merchant key 
  .shouldGetExtendedPaymentDetails(true) // set it to true to get extended payment details
  .shouldGetTaxSpecification(true) // set it to true to fetch tax info applicable on each payment mode 
  .build();
  
  GetTransactionDetails.Builder transactionDetails = new GetTransactionDetails.Builder()
  .setAmount(1000.0)//transaction amount in double
  .build();
  
  //Passing Customer Details is optional and can be used 
  //to check EMI eligibility based on mobile number
  CustomerDetails.Builder customerDetails = new CustomerDetails.Builder()
  .setMobile("9999999999") //pass the mobile number if want to get eligibility status in payment option
  .build();
  
  String var1 = new GetCheckoutDetailsRequest.Builder()
            .setUsecase(usecase)
            .setCustomerDetails(customerDetails)
            .setTransactionDetails(transactionDetails)
            .build().prepareJSON();
```

After getting var1, pass that in Merchant Web Service with the command as PayuConstants.GET\_CHECKOUT\_DETAILS. 

## Step 2: Get API response

PayuResponse is received in the `onCheckoutDetailsResponse()` callback method of `CheckoutDetailsListener` as mentioned in the API Commands Supported table.

### Get additional charges, bank down status, and offers

Additional Charges are returned in the PaymentDetails object for each payment option. The following example code snippet is for fetching Additional Charges for Net Banking:

```Text JAVA
//if netbanking is available on merchant key
if(payuResponse.isNetBanksAvailable()){
ArrayList<PaymentDetails> netbanks = payuResponse.getNetbanks();
}
```

* Additional Charge is available inside each `PaymentDetails` object and can be accessed using the `paymentDetails.getAdditionalCharge()` method
* Similarly, bank health is available inside each `PaymentDetails` object and can be accessed using the `paymentDetails.isBankDown()` method.
* For Offers, An `ArrayList<PayuOffer>` is available inside each `PaymentDetails` object. To get the offers list, use the `paymentDetails.getOfferDetailsList()`.

### Get tax info

Tax is not applied on individual Net Banking or card schemes but instead applied at the payment mode level for all CC(Credit Card), DC(Debit Card), NB(Net Banking), Wallets, etc. So, to fetch the Tax Specification, use the following code block:

```Text JAVA
if(payuResponse.isTaxSpecificationAvailable())
TaxSpecification taxSpecification = payuResponse.getTaxSpecification();

taxSpecification.getCcTaxValue() //tax applicable on CC transactions
taxSpecification.getDcTaxValue() //tax applicable on DC transactions
taxSpecification.getNbTaxValue() //tax applicable on NB transactions
taxSpecification.getCashTaxValue() //tax applicable on Wallet transactions
...
```