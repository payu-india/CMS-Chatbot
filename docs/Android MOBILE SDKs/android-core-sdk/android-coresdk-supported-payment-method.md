---
title: Supported Payment Methods
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
SDK supports the following payment types, and additional parameters are supported. The additional parameters that can be configured in the PaymentParams object created earlier are described in this section.

- Credit Card/Debit Card/Stored Card (Use PayuConstants.CC)
- NetBanking (Use PayUConstants.NB)
- EMI (Use PayUConstants.EMI)
- No Cost EMI (Use PayUConstants.EMI)
- Cash Cards/Wallets (Use PayUConstants.CASH)
- UPI (Use PayUConstants.UPI)
- LazyPay (Use PayUConstants.LAZYPAY)
- TwidPay (Use PayUConstants.PAY_BY_REWARDS)
- Sodexo (Use PayUConstans.PAYMENT_PG_SODEXO)

Also, the following payment methods are supported:

- PayU Money (Use PayUConstants.PAYU_MONEY)
- Intent (Use PayUConstants.UPI_INTENT)
- Google Pay (Use PayUConstants.TEZ)
- PhonePe (Use PayUConstants.PHONEPE_INTENT)

## Credit card/debit card

### Card transaction

```Text Node
mPaymentParams.setCardNumber(cardNumber);
mPaymentParams.setCardName(cardName);
mPaymentParams.setNameOnCard(cardholderName);
mPaymentParams.setExpiryMonth(expiryMonth);// MM
mPaymentParams.setExpiryYear(expiryYear);// YYYY
mPaymentParams.setCvv(cvv);
```

### Store credit/debit card

```Text Node
mPaymentParams.setCardNumber(cardNumber);
mPaymentParams.setCardName(cardName);
mPaymentParams.setNameOnCard(cardholderName);
mPaymentParams.setExpiryMonth(expiryMonth);// MM
mPaymentParams.setExpiryYear(expiryYear);// YYYY
mPaymentParams.setCvv(cvv);
 
mPaymentParam.setUserCredentials(userCredentials);
mPaymentParam.setStoreCard(1);
```

### Recurring payments in credit/debit card

For Recurring payments in CC/DC, you need to collect the following details: Set this `siParams` in the payment parameters created. For more information, refer to [integration steps](https://docs.payu.in/docs/android-core-sdk) for Android Core SDK. 

### Store Cards

```Text Node
mPaymentParams.setCardToken(cardToken);
mPaymentParams.setCvv(cvv);
mPaymentParams.setNameOnCard(cardName);
mPaymentParams.setExpiryMonth(expiryMonth);// MM
mPaymentParams.setExpiryYear(expiryYear);// YYYY 
mPaymentParams.setCardName(storedCard.getCardName());
```

### Tokenization

For cards tokenized outside the PayU platform merchant needs to pass the below parameters.

```Text Node
mPaymentParams.setCardTokenType(1); //it should be passed as 1
TokenizedCardAdditionalParam additionalParam = new TokenizedCardAdditionalParam();
additionalParam.setLast4Digits("1234"); //last 4 digits of card
additionalParam.setTavv("1234"); //tavv -> will be given by tokenisation partner
additionalParam.setTrid("1234"); //trid -> will be given by tokenisation partner
additionalParam.setTokenRefNo("1234"); //tokenRefNo -> will be given by tokenisation partner
mPaymentParams.setTokenizedCardAdditionalParam(additionalParam);
```

## Net Banking

Get the bankCode (String) of the selected bank from your spinner or list view adapter and add it to mPaymentParams created earlier.

```Text Node
mPaymentParams.setBankCode(bankCode);
```

### Recurring Payments in NetBanking

For recurring payments in Net Banking, you need to collect the following details:

```Text Node

BeneficiaryDetails beneficiaryDetails = new BeneficiaryDetails();
beneficiaryDetails.setBeneficiaryName("John Doe");
beneficiaryDetails.setBeneficiaryAccountNumber("51234567890");
beneficiaryDetails.setBeneficiaryAccountType(BeneficiaryAccountType.SAVINGS);
beneficiaryDetails.setBeneficiaryIfsc("ICIC0006621")
SIParams siParams = new SIParams();
siParams.setBeneficiarydetail(beneficiaryDetails);
```

### Beneficiary Details Parameters Definition

| Parameter                  | Description                                                                                                          |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| Beneficiary Name           | `String` Account Holder Beneficiary name.                                                                            |
| Beneficiary Account Number | `String` Account number of Beneficiary.                                                                              |
| Beneficiary Account Type   | `Enum of BeneficiaryAccountType` Accepted values are BeneficiaryAccountType.SAVINGS, BeneficiaryAccountType.CURRENT. |
| Beneficiary IFSC           | `String` Valid IFSC.                                                                                                 |

## EMI

Get the bankCode (String) of the selected bank from your spinner or list view adapter and add it to mPaymentParams along with the following card details:

```Text Node
mPaymentParams.setCardNumber(“5123456789012346”); 
mPaymentParams.setNameOnCard(“test”); 
mPaymentParams.setExpiryMonth(“06”); 
mPaymentParams.setExpiryYear(“2023”); 
mPaymentParams.setCvv(“123”); 
mPaymentParams.setBankCode(“EMI03”); 
```

### Cardless EMI

For doing CardLess EMI transactions, `setCardLess `must be set to true along with setting the bank code in the payment parameters similar to the following code snippet:

```Text Node
mPaymentParams.setBankCode("ZESTMON"); //For Zestmoney CardLess EMI
mPaymentParams.setCardlessEMI(true);
```

For the Zestmoney CardLess EMI transactions, the phone number must also be set in payment parameters similar to the following code snippet:

```Text Node
mPaymentParams.setPhone("9000000000");
```

## No-Cost EMI

For posting No-Cost EMI transactions, the subvention amount needs to be sent along with the above EMI parameters similar to the following code snippet:

```
mPaymentParams.setCardNumber(“5123456789012346”); 
mPaymentParams.setNameOnCard(“test”); 
mPaymentParams.setExpiryMonth(“06”); 
mPaymentParams.setExpiryYear(“2023”); 
mPaymentParams.setCvv(“123”); 
mPaymentParams.setBankCode(“EMI03”); 
mPaymentParams.setSubventionAmount(“4000”);
```

To get a list of No-Cost EMI supporting banks, pass var2 as “all” in the Merchant Web Service for GetPaymentRelatedDetailsTask.

**Hash Formula**

If the subvention amount is passed, the hash formula for payment hash will be similar to the following:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|SubventionAmount)
```

## Cash card

```Text Node
mPaymentParams.setBankCode(bankCode);
```

## UPI

```Text Node
mPaymentParams.setVpa(virtualPaymentAddress);
```

You need to validate the following for the virtual payment address (VPA):

- VPA length should be less than or equal to 50 characters
- Regex for VPA: value.match(/^([A-Za-z0-9.])+@[A-Za-z0-9]+$/)

## LazyPay

Notify(callback) the URL of the merchant where notification of transaction status will be sent on completion of the transaction. It should be HTTPS.

```Text Node
mPaymentParams.setNotifyURL(<Merchant Callback Url>);
```

## TwidPay

To Pay using TwidPay, create the post data with PayuConstants.PAY_BY_REWARDS.

After a successful payment, you will get the Twid customer hash in field5 params of PayuResponse, which would use for the next transaction to skip authentication.

```Text Node
mPaymentParams.setTwidCustomerHash("Twid customer hash");
```

## Sodexo

To pay using Sodexo, create the post data with PAYMENT_PG_SODEXO:

```Text Node
mPaymentParams.setCardNumber(cardNumber);
  mPaymentParams.setCardName(cardName);
  mPaymentParams.setNameOnCard(cardholderName);
  mPaymentParams.setExpiryMonth(expiryMonth);// MM
  mPaymentParams.setExpiryYear(expiryYear);// YYYY  
  mPaymentParams.setCvv(cvv);
```

After a successful payment, you would get the Sodexo source ID in the field3 param of PayU response, which can be used to show and get stored Sodexo card details and also can be used for initiating payment.

```Text Node
mPaymentParams.setsodexoSourceId("srcid123");
```