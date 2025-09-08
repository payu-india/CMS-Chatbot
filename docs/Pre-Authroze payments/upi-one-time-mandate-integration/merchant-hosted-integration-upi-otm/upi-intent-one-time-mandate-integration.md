---
title: UPI Intent One-Time Mandate Integration
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
The merchant initiates a call to PayU with the SI details, pg., bankcode, and pre-authorization amount. This amount is considered the Block Amount.
Using these details, Payu will then relay the callback with the current status to the merchant.

The **pre_authorize** parameter is used for pre-authorize payments using the seamless integration with the _payment API

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout. For API Reference, refer to [UPI One-Time Mandate Transaction API](ref:_payment-upi-tpv-one-time-mandate-consent-transaction-api).

**Environment**

|                            |                                                                        |
| :------------------------- | :--------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/_payment>](https://secure.payu.in/_payment>) |

The **pre_authorize** parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **_payment** API.


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

## Step 2: Check the response from PayU

### Success scenario

For Intent, as part of response, Intent URL is returned. Now, merchant needs to use data received in intentURIData parameter, JSON decode the response and use URL to invoke intent at their end

```curl
{
  "metaData": {
    "message": null,
    "referenceId": "test123",
    "statusCode": null,
    "txnId": "test989",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "99999999",
    "merchantName": "abc",
    "merchantVpa": "abc@sbi",
    "amount": "166.00",
    "intentURIData": "upi://mandate?pa=abc@upi&pn=abc&mn=ONETIME&tid=test123&validitystart=02102024&validityend=15112024&am=166.00&amrule=MAX&recur=ONETIME&tr=test989&cu=INR&mc=6300&tn=UPIIntent&mode=13&purpose=01&orgid=400011&rev=N&block=Y&txnType=CREATE",
    "acsTemplate": "PGh0bWw+PGJvZH... (truncated for brevity)",
    "otpPostUrl": "https://pp78secure.payu.in/ResponseHandler.php"
  }
}

```

### Failure scenarios

After the transaction is authorised by the customer, PayU will receive confirmation. Same will be passed to the merchant as webhook.

```
{
  "metaData": {
    "message": "Transaction failed due to invalid params shared by the merchant",
    "referenceId": "dde7096af9db932a9fd09b9b4383d8be",
    "statusCode": "E1101",
    "txnId": "0c4931ddee7a4f69227f",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {}
}
```

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.=

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

To check the status of the transaction, use the verify_payment API. For more information, refer to [Verify Payment API](ref:verify_payment_api).
