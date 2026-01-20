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
> * Only transactions that are in auth status and added on the same day can only be marked as canceled.
> * Only transactions that are collected by Credit Card and Debit Card can only be canceled.
> * Pre Auth transactions cannot be canceled.
> * The same merchant key should be used to cancel the payment which was used to initiate the payment.

#### Environment

| Environment | URL                                                                                            |
| :---------- | :--------------------------------------------------------------------------------------------- |
| Test        | [https://test.payu.in/merchant/postservice.php](https://test.payu.in/merchant/postservice.php) |
| Production  | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

## Request parameters

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
        Sample Value
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
        `string` The merchant key that was provided by PayU.  
        Reference: For more information on how to generate the Key and Salt, refer to any of the following:

        * *Production**: Generate Production Merchant Key and Sat.
        * *Test**: Generate Test Merchant Key and Salt.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        command  
        `mandatory`
      </td>

      <td>
        `string` The parameter must contain the name of the web service. For this API, the value must be cancel_omni_payment.
      </td>

      <td>
        string The parameter must contain the name of the web service. For this API, the value must be cancel_omni_payment.
      </td>
    </tr>

    <tr>
      <td>
        hash  
        `mandatory`
      </td>

      <td>
        string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below: `sha512(key|command|var1|salt)`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        var1  
        `mandatory`
      </td>

      <td>
        json This parameter is in JSON format. For the description of fields in JSON Format, refer to the next table.
      </td>

      <td>
        Refer the next table.
      </td>
    </tr>
  </tbody>
</Table>

**Var1**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>
        Sample
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        transactionId
        mandatory
      </td>

      <td>
        String This is the transactionId with which initial transaction is initiated.
      </td>

      <td>
        cancel1234
      </td>
    </tr>

    <tr>
      <td>
        product_type   
        optional
      </td>

      <td>
        String This parameter indicates the product if the merchant has initiated multiple in-progress transactions with the same txnid. For this API, you must specify only the values as POS.
      </td>

      <td>
        POS
      </td>
    </tr>
  </tbody>
</Table>

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
