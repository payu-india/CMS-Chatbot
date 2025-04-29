---
title: Insta Deactivate VPA API
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
The **Insta Deactivate VPA** API is used to deactivate the VPA embedded in the insta static QR permanently. After the VPA is deactivated using this API, the QR cannot be scanned from any UPI application like Google Pay, PhonePe etc and transactions cannot be done through UPI in future.

## Environment

| Environment | URL                                             |
| :---------- | :---------------------------------------------- |
| Production  | <https://info.payu.in/merchant/postservice.php> |

## Request parameter

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Value",
    "0-0": "key",
    "0-1": "This parameter must contain the merchant key provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \n**Production**: Generate Production Merchant Key and Sat.  \n**Test**: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command",
    "1-1": "This parameter must have the API command name.",
    "1-2": "expire_insta_account",
    "2-0": "hash",
    "2-1": "This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash as follows:  \n  \nsha512(key|command|var1|salt)",
    "2-2": "c24ee06c7cf40314ede424 b1fcc2b97a12f97a7d3dd2 06876eef16660eb09fd374 fd82861f66d8152e",
    "3-0": "var1",
    "3-1": "This parameter must contain the fields in a JSON format. For more information, refer to <<Description of var1 Parameter Fields>>.",
    "3-2": "Refer to <<Sample var1 >>section."
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


### Fields in var1 parameter description

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Description",
    "h-2": "Sample",
    "0-0": "merchantVpa  \n`mandatory`",
    "0-1": "Merchant's VPA is the VPA which needs to be deactivated/blocked permanently",
    "0-2": "smsplustestqr789@indus",
    "1-0": "instaProduct  \n`mandatory`",
    "1-1": "QR generation flag. Fixed value - qr",
    "1-2": "qr",
    "2-0": "remarks  \n`optional`",
    "2-1": "This can be used for audit trail later",
    "2-2": "Account closed"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Sample var1

```Text JSON
{
  "merchantVpa": "smsplustestqr789@indus",
  "instaProduct": "qr"
}
```

### Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=J****g' \
--data-urlencode 'command=expire_insta_account' \
--data-urlencode 'hash=d4d166daed5252d9ae592f65b54b4d38a4f4c1daa24bd5d8902c58960f6556240859398417b1634da3ed4f92f4e88f7c9426e78efdb69aae26ad95d97266f8d5' \
--data-urlencode 'var1={"merchantVpa":"smsplustestqr789@indus","instaProduct":"qr"}'
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J****g&command=expire_insta_account&hash=d4d166daed5252d9ae592f65b54b4d38a4f4c1daa24bd5d8902c58960f6556240859398417b1634da3ed4f92f4e88f7c9426e78efdb69aae26ad95d97266f8d5&var1=%7B%22merchantVpa%22%3A%22smsplustestqr789%40indus%22%2C%22instaProduct%22%3A%22qr%22%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text PHP
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://info.payu.in/merchant/postservice.php',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'key=J****g&command=expire_insta_account&hash=d4d166daed5252d9ae592f65b54b4d38a4f4c1daa24bd5d8902c58960f6556240859398417b1634da3ed4f92f4e88f7c9426e78efdb69aae26ad95d97266f8d5&var1=%7B%22merchantVpa%22%3A%22smsplustestqr789%40indus%22%2C%22instaProduct%22%3A%22qr%22%7D',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/x-www-form-urlencoded'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
```Text Java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "key=J****g&command=expire_insta_account&hash=d4d166daed5252d9ae592f65b54b4d38a4f4c1daa24bd5d8902c58960f6556240859398417b1634da3ed4f92f4e88f7c9426e78efdb69aae26ad95d97266f8d5&var1={\"merchantVpa\":\"smsplustestqr789@indus\",\"instaProduct\":\"qr\"}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n0 - If web service call failed.  \n1 - If web service call succeeded",
    "1-0": "msg",
    "1-1": "The following message is displayed to indicate that the VPA is permanently blocked now, and the QR cannot be scanned to make any UPI transactions.  \n`merchantVpa deactivated`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample response

```Text JSON
{
  "status": "1",
  "msg": "merchantVpa deactivated"
}
```