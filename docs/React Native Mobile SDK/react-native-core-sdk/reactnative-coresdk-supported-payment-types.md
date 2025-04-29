---
title: Supported Payment Types
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
You can integrate with the following types of payments using React Native Core API:

- Credit/Debit Card
- Sodexo
- Saved Card
- Net Banking
- Cashcard/Wallet
- EMI
- No-cost EMI/Subvention EMI
- InApps UPIs

## Generate URL request for payment

To generate the URL Request (and post parameters) for payment, create a JSON as shown in the code snippet below:

```Text React.js
let props = {  
        merchantKey,  
        salt,  
        isSandbox,  
        environment,  
        productInfo,  
        amount,  
        txnId,  
        firstName,  
        phone,  
        email,  
        surl,  
        furl,  
        userCredentials,  
} ;
```

The callbacks give your URLRequest as well as post parameters (NSString format). You can use these post parameters to initialize the Custom Browser Instance.

***

## Build Request Data Objects for Payment Types

### Credit/Debit Card

To pay using a credit/debit card, set the parameters as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,  
      key: props.merchantKey,  
      paymentType: 'Credit / Debit Cards',  
      nameOnCard,
      cardNumber,
      expiryYear,
      expiryMonth,
      cvv,
      cardToken,//not mandatory
};
```

### Sodexo

To Pay using Sodexo, set the Sodexo parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,  
      key: props.merchantKey,  
      paymentType: 'Sodexo',  
      nameOnCard,
      cardNumber,
      expiryYear,
      expiryMonth,
      cvv,
};
```

After a successful payment, you will get the Sodexo source ID in the field3 param of PayU response that can be used to show and get stored Sodexo card details and can also be used for initiating payment.

### SavedCard

To Pay using  SavedCard, set the`SavedCard` parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,  
        key: props.merchantKey,  
        paymentType: 'Credit / Debit Cards',  
        nameOnCard,
        cvv,
        cardToken,
}
```

### Net Banking

To Pay using NetBanking, set the`NetBanking `parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
    ...props,  
    key: props.merchantKey,  //"smsplus"
    paymentType: 'Net Banking',  
    bankCode,  //"SBIB"
}
```

### Cashcard/Wallet

To Pay using CashCard, set the`cashcard` parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
 ...props,
      key: props.merchantKey, //"smsplus"
      bankCode:BankCode,      //"AMZPAY"
      paymentType:"CASH",
}
```

### EMI

To Pay using EMI, set the EMI parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,
      key: props.merchantKey, //"smsplus" //Mandatory
      paymentType: 'EMI',                 //Mandatory
      nameOnCard,
      cardNumber,
      expiryYear,
      expiryMonth,
      cvv,
      bankCode,//"HDFCD06"                //Mandatory
      phone: phoneNumber
}
```

The following are the mandatory parameters for EMI:

- **Credit Card EMI**
  - **All Banks**: cardNumber, expiryYear, expiryMonth, Cvv\\
- **Debit Card EMI**
  - **Axis Bank and ICICI Bank**: cardNumber, expiryYear, expiryMonth, Cvv, phone
  - **Bank of Baroda, HDFC Bank, Kotak Mahindra Banks, SBI**: cardNumber, phone
- **Cardless EMI**
  - **ZestMoney**: Phone

### UPI

To Pay using UPI, set the UPI parameter as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,  
        key: props.merchantKey,  
        paymentType: 'upi',  
        vpa  
}
```

### No Cost EMI / Subvention EMI 

To Pay using Subvention EMI, set the `subventionAmount` parameter of paymentParams as shown in the code snippet below:

```Text React.js
const requestData = {  
  ...props,  
        key: props.merchantKey,  
        paymentType: 'No Cost EMI',  
        nameOnCard,  
        cardNumber,  
        expiryYear,  
        expiryMonth,  
        cvv,  
        bankCode,  
        subventionAmount  
}
```

If subventionAmount is passed in the request then use the following formula to calculate the hash: `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|SubventionAmount)`

### InApps UPI

For UPI inApps, set `paymentparameters` as shown in the code snippet below:

```Text React.js
const requestData = {  
 ...props,
      key: props.merchantKey, //"smsplus"
      bankCode:BankCode,      
      paymentType:"",
}
```

***

## Make the payment

After building the payment request data, use the `makePaymen`t method to create the request body as shown in the code snippet below:

```Text React.js
PayUSdk.makePayment(  

{  

...requestData,  

hash: getHash(requestData)  

},  

(response) => {  

const responseData = JSON.parse(response);  

if (responseData?.data) {  

//you get data and url in responseData  

}  

},  

(err) => {  

Alert.alert('Error', JSON.stringify(err));  

}  

);  
```