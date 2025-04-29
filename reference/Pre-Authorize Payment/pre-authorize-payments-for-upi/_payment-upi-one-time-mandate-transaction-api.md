---
title: UPI One-Time Mandate API - Merchant Hosted
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
This section describes the request and response parameters with sample request and response for UPI One-Time mandate Intent and Collect flow. For more information on integration, refer to [UPI One-Time Mandate](doc:upi-one-time-mandate-consent).

> 📘 Note
> 
> Currently, PayU supports UPI One-Time Mandate only for the Seamless integration.

<PaymentAPIEnvironment />

## Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "key  \n`mandatory`",
    "0-1": "`varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.",
    "0-2": "Your Test Key",
    "1-0": "txnid  \n`mandatory`",
    "1-1": "`varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.  \n`Character limit`: 25  \n**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’",
    "1-2": "fd3e847h2",
    "2-0": "amount  \n`mandatory`",
    "2-1": "`float` This parameter should contain the payment amount of the particular transaction.  \n  \n**Note**: Type-cast the amount to float type",
    "2-2": "1000",
    "3-0": "productinfo  \n`mandatory`",
    "3-1": "`varchar` This parameter should contain a brief product description. It should be a string describing the product.  \n`Character limit`: 100",
    "3-2": "Time Magazine Subscription",
    "4-0": "firstname  \n`mandatory`",
    "4-1": "`varchar` Must contain the first name of the customer.  \n`Character limit`: 60",
    "4-2": "Ashish",
    "5-0": "email  \n`mandatory`",
    "5-1": "`varchar` Must contain the email of the customer.  \nThis information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.  \nAlso, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  \nCharacter limit: 50",
    "5-2": "[Ashish@test.com](mailto:Ashish@test.com)",
    "6-0": "phone  \n`mandatory`",
    "6-1": "`varchar` Must contain the phone number of the customer.  \n  \nThis information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  \nCharacter limit: 50",
    "6-2": "9843176540",
    "7-0": "surl  \n`mandatory`",
    "7-1": "surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.",
    "7-2": "",
    "8-0": "furl  \n`mandatory`",
    "8-1": "furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.",
    "8-2": "",
    "9-0": "pg  \n`mandatory`",
    "9-1": "It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**",
    "9-2": "UPI",
    "10-0": "bankcode  \n`mandatory`",
    "10-1": "It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case.",
    "10-2": "- **UPI**: Used for UPI Collect\n- **INTENT**: Used for UPI Intent",
    "11-0": "vpa  \n`mandatory`",
    "11-1": "This parameter contains the customer’s VPA handle. For the list UPI handles supported, refer to UPI Handles  \n  \nThe merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to  [Validate VPA API](ref:validate_vpa_api).",
    "11-2": "abc@payu",
    "12-0": "txn_s2s_flow  \n`mandatory`",
    "12-1": "This parameter must be passed with the values as **4** for UPI Intent.",
    "12-2": "4",
    "13-0": "pre_authorize  \n`mandatory for Pre-Auth`",
    "13-1": "This parameter is set to** 1** to pre-authorize payment.",
    "13-2": "",
    "14-0": "si_Details",
    "14-1": "This parameter contains the following information in JSON format:  \n  \n- paymentStartDate\n- paymentEndDate  \n  **Example**:  {\"paymentStartDate\":\"2024-07-24\",\"paymentEndDate\":\"2024-07-28\"}",
    "14-2": "{\"paymentStartDate\":\"2024-07-24\",\"paymentEndDate\":\"2024-07-28\"}",
    "15-0": "hash  \n`mandatory`",
    "15-1": "Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  \n  \nIt is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.  \n  \nIn the case of registration transaction, the formula is used to calculate this hash is similar to the following:  \n`HASH = SHA512(sha512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\||\\||\\||SALT))`",
    "15-2": ""
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

### Intent Flow

```
ample request: 
curl --request POST  

--url https://test.payu.in/_payment  
--header 'accept: text/plain'  
--header 'content-type: application/x-www-form-urlencoded'  
--data key=JPM7Fg  
--data pg=UPI  
--data bankcode=INTENT 
--data txn_s2s_flow=4  
--data txnid=aso6787  
--data siDetails="{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}"  
--data pre_authorize=1 \ 
 --data amount=100.00  
--data productinfo=iPhone  
--data firstname=Ashish  
--data email=ashish@abc.com  
--data phone=9876543210  
--data surl=https://apiplayground-response.herokuapp.com/  
--data furl=https://apiplayground-response.herokuapp.com/  
--data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b 
```

<br />

### Collect Flow

```
curl --request POST  
--url https://test.payu.in/_payment  
--header 'accept: text/plain'  
--header 'content-type: application/x-www-form-urlencoded'  
--data key=JPM7Fg  
--data pg=UPI  
--data bankcode=UPI  
--data vpa=anything@payu  
--data txn_s2s_flow=4  
--data txnid=aso6787  
--data siDetails="{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}"  
--data pre_authorize=1 \ 
 --data amount=100.00  
--data productinfo=iPhone  
--data firstname=Ashish  
--data email=ashish@abc.com  
--data phone=9876543210  
--data surl=https://apiplayground-response.herokuapp.com/  
--data furl=https://apiplayground-response.herokuapp.com/  
--data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b 
```

## Sample response

### Intent Flow

#### Success scenario

For Intent, as part of response, Intent URL is returned. Now, merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

```curl
{
  "metaData": {
    "message": null,
    "referenceId": "c5161bae370de1bd4fb886c6c66567a8",
    "statusCode": null,
    "txnId": "a7440cc636e747b635df",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "99900000000001875",
    "merchantName": "Name409208872",
    "merchantVpa": "paytmqr@icici",
    "amount": "10000.00",
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHA3OHNlY3VyZS5wYXl1LmluLzY1OWFjNWRhNWUyZjlmNzM1NzhkZWYwYzVjNDM2MWFmOWJhMGVkYmExYjk3NDg2Mjg3ZDI2MzBjZDg1YmU3NWEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5..."
    },
    "otpPostUrl": "https://pp78secure.payu.in/ResponseHandler.php"
  }
}

```

### Failure scenario

For Intent, as part of response, Intent URL is returned. Now merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end  

Once the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the merchant as webhook

```
{
  "metaData": {
    "message": "Transaction failed due to invalid params shared by the merchant",
    "referenceId": "dde7096af9db932a9fd09b9b4383d8be",
    "statusCode": "E1101",
    "txnId": "0c4931ddee7a4f69227f",
    "txnStatus": "failed",
    "intentURIData": "upi://mandate?pa=payu24@icici&pn=Payu&tr=EZM2024042211452400151942&am=10000.00&cu=INR&orgid=400011&mc=6012&purpose=01&tn=Upi%20Mandate&validitystart=22042024&validityend=21052024&amrule=MAX&Recur=ONETIME&Rev=N&Share=Y&Block=Y&txnType=CREATE&mode=13",
    "unmappedStatus": "failure"
  },
  "result": {}
}

```

### Collect Flow

#### Success scenario

```curl
{ 
   "metaData":{ 
      "message":null, 
      ""referenceId":"c5161bae370de1bd4fb886c6c66567a8", 
      "statusCode":null, 
      ""txnId":"a7440cc636e747b635df", 
      ""txnStatus":"pending", 
      ""unmappedStatus":"pending" 
   }, 
   "result":{ 
      "postToBank":{ 
         "useMethodGet":true 
      }, 
      "issuerUrl":"https://api.payu.in/ public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader" 
   } 
} 
 
```

#### Failure scenarios

```
{ 
   "metaData":{ 
      "message":"Transaction failed due to invalid params shared by the merchant", 
      "referenceId":"dde7096af9db932a9fd09b9b4383d8be", 
      "statusCode":"E1101", 
      "txnId":"0c4931ddee7a4f69227f", 
      "txnStatus":"failed", 
      "unmappedStatus":"failure" 
   }, 
   "result":{ 
       
   } 
} 
```