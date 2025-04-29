---
title: UPI Intent One-Time Mandate Integration - PayU Hosted
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
The pre\_authorize parameter is used to pre-authorize payments using the PayU Hosted Checkout integration with the \_payment API.

> 📘 Note:
>
> You need to activate the Pre-authorize payments before you start using this integration. Contact your PayU Key Account Manager (KAM) to activate Pre-authorize Payments.

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout. For API Reference, refer to [UPI One-Time Mandate Transaction API](ref:upi-one-time-mandate-transaction-api-payu-hosted).

<PaymentAPIEnvironment />

The **pre\_authorize** parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **\_payment** API. 

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
        txnid\
        `mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.\
        `Character limit`: 25  

        * \*Note\*\*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount\
        `mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction.  

        * \*Note\*\*: Type-cast the amount to float type
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        productinfo\
        `mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product.\
        `Character limit`: 100
      </td>

      <td>
        Time Magazine Subscription
      </td>
    </tr>

    <tr>
      <td>
        firstname\
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the first name of the customer.\
        `Character limit`: 60
      </td>

      <td>
        Ashish
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the email of the customer.\
        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.\
        Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.\
        Character limit: 50
      </td>

      <td>
        [Ashish@test.com](mailto:Ashish@test.com)
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `mandatory`
      </td>

      <td>
        `varchar` Must contain the phone number of the customer.  

        This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information\
        Character limit: 50
      </td>

      <td>
        9843176540
      </td>
    </tr>

    <tr>
      <td>
        surl\
        `mandatory`
      </td>

      <td>
        surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        furl\
        `mandatory`
      </td>

      <td>
        furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pre\_authorize\
        `mandatory for Pre-Auth`
      </td>

      <td>
        This parameter is set to**1** to pre-authorize payment.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        si\_details
      </td>

      <td>
        This parameter contains the following information in JSON format:  

        * paymentStartDate
        * paymentEndDate  
          * \*Example\*\*:  \{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}
      </td>

      <td>
        \{"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"}
      </td>
    </tr>

    <tr>
      <td>
        hash\
        `mandatory`
      </td>

      <td>
        Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  

        It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si\_details by merchant salt.  

        In the case of registration transaction, the formula is used to calculate this hash is similar to the following:\
        `HASH = SHA512(sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\||\||\||SALT))`
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

### Hashing

You must hash the request parameters using the following hash logic: 

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

### Sample request

```
curl --request POST   

--url https://test.payu.in/_payment   
--header 'accept: text/plain'   
--header 'content-type: application/x-www-form-urlencoded'   
--data key=JPM7Fg   
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

## Step 2: Check the response from PayU

### Success scenario

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
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vcHA3OHNlY3VyZS5wYXl1LmluLzY1OWFjNWRhNWUyZjlmNzM1NzhkZWYwYzVjNDM2MWFmOWJhMGVkYmExYjk3NDg2Mjg3ZDI2MzBjZDg1YmU3NWUvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjIxNjU0RTEyLUY5N0QtM0MxRS0zNjlFLTg5RDdGMzREODkyMSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMTAwMDAuMDAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1paHBheWlkIiB2YWx1ZT0iNjU5YWM1ZGE1ZTJmOWY3MzU3OGRlZjBjNWM0MzYxYWY0ZmY4N2VjNzAwOTVmYmQzNjcyMTQ5MzAzMWQyNTYyMiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iZGlzYWJsZUludGVudFNlYW1sZXNzRmFpbHVyZSIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlVnBhIiB2YWx1ZT0icGF5dG1xckBpY2ljaSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iTmFtZTQwOTIwODg3MiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYWRkaXRpb25hbENoYXJnZXMiIHZhbHVlPSIiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMTAwMDAuMDAiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg==",
    "otpPostUrl": "https:\/\/pp78secure.payu.in\/ResponseHandler.php"
  }
}

```

### Failure scenarios

For Intent, as part of response, Intent URL is returned. Now,  you need to use data received in **intentURIData** parameter, JSON decode the response and use URL to invoke intent at your end.

After the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the you as webhook.

```
{ 
 "metaData": { "message": "Transaction failed due to invalid params shared by the merchant", "referenceId": "dde7096af9db932a9fd09b9b4383d8be", 
 "statusCode": "E1101", 
 "txnId": "0c4931ddee7a4f69227f", "txnStatus": "failed", "intentURIData":"upi:\/\/mandate?pa=payu24@icici&pn=Payu&tr=EZM2024042211452400151 942&am=10000.00&cu=INR&orgid=400011&mc=6012&purpose=01&tn=Upi%20Mandate&validitystart=22042024&validityend=21052024&amrule=MAX&Recur=ONETIME&Rev=N&Share=Y &Block=Y&txnType=CREATE&mode=13", "unmappedStatus": "failure" }, "result": {} 
}  
```

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.=

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key ```

        mandatory
        ```
      </td>

      <td>
        This parameter is the unique Merchant Key provided by PayU for your merchant account. The Merchant Key acts as the unique identifier (primary key) to identify a Merchant Account in our database. <br> *Sample value* – YbfVda
      </td>
    </tr>

    <tr>
      <td>
        command ```

        mandatory
        ```
      </td>

      <td>
        For initiating a capture transaction, the value of the parameter will be passed as - **capture\_transaction**
      </td>
    </tr>

    <tr>
      <td>
        hash ```

        mandatory
        ```
      </td>

      <td>
        This parameter must contain the hash value to be calculated at merchant end. Hash logic for this API is:\
        sha512(key|command|var1|salt) sha512
      </td>
    </tr>

    <tr>
      <td>
        var1```

        mandatory
        ```
      </td>

      <td>
        This parameter must contain the payuId that was generated by PayU as part of pre-authorize operation.
      </td>
    </tr>

    <tr>
      <td>
        var2 ```

        mandatory
        ```
      </td>

      <td>
        This parameter contains the token, that is, merchant unique reference number.
      </td>
    </tr>

    <tr>
      <td>
        var3```

        mandatory
        ```
      </td>

      <td>
        This parameter must contain the amount to be captured.
      </td>
    </tr>
  </tbody>
</Table>

### Sample request

```
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'key="JF***g"' \
--form 'command="capture_transaction"' \
--form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \
--form 'var1="15246574846"' \
--form 'var2="authorizeTransaction123"' \
--form 'var3="1"'

```

### Sample response

```
{  
    "status": 1,  
    "msg": "Capture Request Queued",  
    "request_id": "Request ID",  
    "bank_ref_num": "Bank Reference Number"  
} 
```

### Step 4: Check Transaction Status

To check the status of the transaction, use the verify\_payment API. For more information, refer to [Verify Payment API](ref:verify_payment_api).
