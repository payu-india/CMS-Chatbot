---
title: Cancel QR Transaction API
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
The **Cancel QR Transaction** API is used to cancel the initiated transaction with PayU. The output will be a JSON.

#### Environment

| Environments | URI                                                                                            |
| :----------- | :--------------------------------------------------------------------------------------------- |
| Production   | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

## Request parameters

| Parameter           | Description                                                                                                                                                                                                                                  | Sample Value      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| key `mandatory`     | `string` Merchant key provided by PayU. Reference: For more information on how to generate the Key and Salt, refer to any of the following: Production: Generate Production Merchant Key and Sat. Test: Generate Test Merchant Key and Salt. | Your Test Key     |
| command `mandatory` | `string` The parameter must contain the name of the web service.                                                                                                                                                                             | cancel_qr_payment |
| hash `mandatory`    | `string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below: `sha512(key\|command\|var1\|salt`. sha512 is the encryption method used here.                 |                   |
| var1 `mandatory`    | json This parameter is in JSON format. For the description of fields in JSON Format, refer to the next table.                                                                                                                                |                   |

The var1 parameter is in a JSON format and the fields are described in the following table:

| Field                     | Description                                                                                                                              | Sample     |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| transactionId `mandatory` | `String` This is the transactionId with which initial transaction is initiated.                                                          | cancel1234 |
| product_type `optional`   | `String` This parameter can be used to indicate the product if merchant has initiated multiple in progress transactions with same txnid. | DBQR       |

## Sample request

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--data-urlencode 'key=J****g' \
--data-urlencode 'command=cancel_qr_payment' \
--data-urlencode 'hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860' \
--data-urlencode 'var1={"transactionId":"","product_type":"DBQR"}'
```

```python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J****g&command=cancel_qr_payment&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1=%7B%22transactionId%22%3A%22%22%2C%E2%80%9Dproduct_type%E2%80%9D%3A%E2%80%9DDBQR%E2%80%9D%7D'
headers = {}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

```php
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
  'var1' => '{"transactionId":"","product_type":"DBQR"}'
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

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "key=J****g&command=cancel_qr_payment&hash=8bb33d0ed43485019eab261cc5f73838149e3bbc1d253e63ca829ff05975c173ec9f308bafe022605aa7fce31821ea3b18df3752accd8a7f50658a96552a0860&var1={\"transactionId\":\"\",\"product_type\":\"DBQR\"}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .build();
Response response = client.newCall(request).execute();
```

## Response structure

### Success response

For every success response based on outputType param:

| Status  | Message                 | Errorcode |
| :------ | :---------------------- | :-------- |
| success | Cancellation Successful | null      |

### Failure response structure

| Status | Message                                                                                                                              | Error Code | Description                                                                     |
| :----- | :----------------------------------------------------------------------------------------------------------------------------------- | :--------- | :------------------------------------------------------------------------------ |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"                                             | -          | Command name is empty                                                           |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"                                             | -          | Merchant key is empty                                                           |
| -      | "if it is invalid, an HTML page is shown with a message : 'Sorry, Some Problem Occurred"                                             | -          | Hash is empty                                                                   |
| failed | transactionId is empty                                                                                                               | E2003      | "transactionId to be sent by the third Party Merchant (limit is 10 characters)" |
| failed | "1. the status of transaction with the given transactionId is not 'in progress' or there is no transaction with given transactionId" | E2019      | "transactionId to be sent by the third Party Merchant (limit is 10 characters)" |
| failed | "1. the status of transaction with the given transactionId is not 'in progress' or there is no transaction with given transactionId" | E2019      | "There is no [in progress] transaction with given transactionId"                |
| failed | Invalid product_type                                                                                                                 | E2051      | value sent in the field 'product_type' does not match with payu's product_type" |
| failed | Amount is empty or less than 1                                                                                                       | E2004      | -                                                                               |
| failed | Amount is less than 1                                                                                                                | E2006      | -                                                                               |

## Sample response

### Empty transaction id

```json
{
  "status": "failed",
  "message": "transactionId is empty",
  "errorCode": "E2003"
}
```

### Invalid transaction id

```json
{
  "status": "failed",
  "message": "There is no [in progress] transaction with given transactionId",
  "errorCode": "E2019"
}
```

### Cancel successful

```json
{
  "status": "success",
  "message": "Cancellation Successful",
  "errorCode": "null"
}
```

### Invalid product type

```json
{
  "status": "failed",
  "message": "Invalid product_type",
  "errorCode": "E2051"
}
```
