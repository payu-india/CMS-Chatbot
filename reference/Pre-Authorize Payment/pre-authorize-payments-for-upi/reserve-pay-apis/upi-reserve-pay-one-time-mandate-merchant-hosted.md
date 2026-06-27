---
title: UPI Reserve Pay One-Time Mandate - Merchant Hosted
deprecated: false
hidden: false
metadata:
  title: UPI Reserve Pay OTM using Merchant Hosted Integration
  keywords:
    - UPI Reserve Pay OTM using Merchant Hosted Integration
    - Reserve Pay OTM
    - OTM Reserve Pay
    - Reserve Pay Merchant Hosted
  robots: index
---
This section includes the API reference for UPI Reserve Paym OTM integration. For more information on UPI Reserve Pay, refer to [UPI Reserve Pay](doc:upi-reserve-pay).

## Request Parameters

<PaymentAPIEnvironment />

<br />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.
        `Character limit`: 25

        - _Note_\*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount<br />`mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.

        - _Note_\*: Type-cast the amount to float type
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo<br />`mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product.<br />`Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname<br />`mandatory`
      </td>

      <td>
        `varchar` Must contain the first name of the customer.<br />`Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email<br />`mandatory`
      </td>

      <td>
        `varchar` Must contain the email of the customer.<br />This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.
        Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone<br />`mandatory`
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is require to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.<br />Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl<br />`mandatory`
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl<br />`mandatory`
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pg<br />`mandatory`
      </td>

      <td>
        It defines the payment category for which you wish to perform UPI One-Time Mandate. For UPI, **pg= UPI**
      </td>

      <td>
        UPI
      </td>
    </tr>

    <tr>
      <td>
        bankcode<br />`mandatory`
      </td>

      <td>
        It defines the bank with which you wish to perform UPI using the bank code. Use **UPI** or **INTENT** according to the use case.
      </td>

      <td>
        - **UPI**: Used for UPI Collect
        - **INTENT**: Used for UPI Intent
      </td>
    </tr>

    <tr>
      <td>
        vpa<br />`mandatory`
      </td>

      <td>
        This parameter contains the customer’s VPA handle. For the list UPI handles supported, refer to UPI Handles

        The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to  [Validate VPA API](ref:validate_vpa_api).
      </td>

      <td>
        abc\@payu
      </td>
    </tr>

    <tr>
      <td>
        txn\_s2s\_flow<br />`mandatory`
      </td>

      <td>
        This parameter must be passed with the values as **4** for UPI Intent.
      </td>

      <td>
        4
      </td>
    </tr>

    <tr>
      <td>
        pre\_authorize<br />`mandatory for Pre-Auth`
      </td>

      <td>
        This parameter is set to**1** to pre-authorize payment.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        si\_Details
      </td>

      <td>
        This parameter contains the following information in JSON format:

        - paymentStartDate
        - paymentEndDate
        - multiCapture
      </td>

      <td>
        {"paymentStartDate": "2025-09-27","paymentEndDate": "2025-10-01","multiCapture": "Y"}
      </td>
    </tr>

    <tr>
      <td>
        hash<br />`mandatory`
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:<br />`HASH = SHA512(sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT))`
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Sample request

### Intent Flow

```bash
curl --request POST  
--url https://test.payu.in/_payment  
--header 'accept: text/plain'  
--header 'content-type: application/x-www-form-urlencoded'  
--data key=JPM7Fg  
--data pg=UPI  
--data bankcode=INTENT 
--data txn_s2s_flow=4  
--data txnid=aso6787  
--data siDetails='{"paymentStartDate": "2025-09-27","paymentEndDate": "2025-10-01","multiCapture": "Y"}'  
--data pre_authorize=1  
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

```bash
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
--data siDetails='{"paymentStartDate": "2025-09-27","paymentEndDate": "2025-10-01","multiCapture": "Y"}'  
--data pre_authorize=1  
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

Once the transaction is authorised by the customer, PayU will receive confirmation. PayU will be pass the confirmation to the merchant as webhook

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

<br />
