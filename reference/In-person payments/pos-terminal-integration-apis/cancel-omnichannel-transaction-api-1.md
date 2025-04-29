---
title: Cancel Omnichannel Transaction API
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
The **Cancel Omnichannel Transaction** API is used to cancel the auth transaction with PayU when the merchant needs to cancel a transaction after successfully accepting the customer’s payment due to internal reasons.

> 👍 Callouts
> 
> - Only transactions that are in auth status and added on the same day can only be marked as canceled.
> - Only transactions that are collected by Credit Card and Debit Card can only be canceled.
> - Pre Auth transactions cannot be canceled.
> - The same merchant key should be used to cancel the payment which was used to initiate the payment.

## Environment

| Environment | URL                                             |
| :---------- | :---------------------------------------------- |
| Test        | <https://test.payu.in/merchant/postservice.php> |
| Production  | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "`string` The merchant key that was provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n**Production**: Generate Production Merchant Key and Sat.  \n  \n**Test**: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, the value must be cancel_omni_payment.",
    "1-2": "string The parameter must contain the name of the web service. For this API, the value must be cancel_omni_payment.",
    "2-0": "hash  \n`mandatory`",
    "2-1": "string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below: `sha512(key\\|command\\|var1\\|salt)`",
    "2-2": "",
    "3-0": "var1  \n`mandatory`",
    "3-1": "json This parameter is in JSON format. For the description of fields in JSON Format, refer to the next table.",
    "3-2": "Refer the next table."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Var1**

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Sample",
    "0-0": "transactionId  \nmandatory",
    "0-1": "String This is the transactionId with which initial transaction is initiated.",
    "0-2": "cancel1234",
    "1-0": "product_type   \noptional",
    "1-1": "String This parameter indicates the product if the merchant has initiated multiple in-progress transactions with the same txnid. For this API, you must specify only the values as POS.",
    "1-2": "POS"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--data-urlencode 'command=cancel_omni_payment' \
--data-urlencode 'key=J****g' \
--data-urlencode 'hash=9463f811a44015fbe65455854fe4a496cbaff7a04af88ab795c3f7ee0b6ba213461339fcc3d0ce5be7b1d157d61082a341e35850ca4ac3fd33170a4b3dba3f17' \
--data-urlencode 'var1={"id":"412345678912370941","mode":"POS"}'
```
```Text Python
import http.client
conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J****g&command=cancel_qr_payment&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1=%7B%22transactionId%22%3A%22%22%2C%E2%80%9Dproduct_type%E2%80%9D%3A%E2%80%9DDBQR%E2%80%9D%7D'
headers = {}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text Php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('https://info.payu.in/merchant/postservice.php');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->addPostParameter(array(
  'key' => 'J****g',
  'command' => 'cancel_qr_payment',
  'hash' => '8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860',
  'var1' => '{"transactionId":"",”product_type”:”DBQR”}'
));
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}
```
```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "key=J****g&command=cancel_qr_payment&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1={\"transactionId\":\"\",”product_type”:”DBQR”}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .build();
Response response = client.newCall(request).execute();
```

## Sample response

```Text Success
{
    "status": "1",
    "msg": "Transaction is succesfully voided.",
    "txn_update_id": "7826786786",
    "bank_ref_num": "7252",
    "mihpayid": "412345678912370941"
}
```
```Text Empty transaction ID
{
  "status": "failed",
  "message": "transactionId is empty",
  "errorCode": "E2003"
}
```
```Text Invalid transaction
{
  "status": 0,
  "msg": "Transaction is not eligible for void"
}
```
```Text Cancellation Failed
{
  "status": 0,
  "msg": "Unable to void transaction. Please try again."
}
```
```
{
  "status": 0,
  "msg": "Merchant is not eligible for void"
}
```