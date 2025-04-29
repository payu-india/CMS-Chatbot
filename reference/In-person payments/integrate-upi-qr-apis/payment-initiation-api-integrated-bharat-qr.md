---
title: Payment Initiation API – Integrated Bharat QR
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
The **Payment Initiation** API is used to initiate payment towards an Integrated Static QR.

| Environment | URI                                |
| :---------- | :--------------------------------- |
| Production  | <https://secure.payu.in/QrPayment> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "key  \n`mandatory`",
    "0-1": "string This parameter must contain the merchant key for the merchant’s account at PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \nProduction: Generate Production Merchant Key and Sat.  \nTest: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "txnid  \n`mandatory`",
    "1-1": "`string` This parameter must contain the transaction ID value posted by the merchant during the transaction request.",
    "1-2": "f7f48de5853f4ebdacef",
    "2-0": "amount  \n`mandatory`",
    "2-1": "`string` This parameter must contain the original amount which was sent in the transaction request by the merchant.",
    "2-2": "10",
    "3-0": "qrId  \n`mandatory`",
    "3-1": "`string` This parameter must contain the unique reference id embedded in the QR using which you want to collect payment from the customer. Remember that at any one point of time, you can collect only 1 payment using a single QR. In case there is a previous payment which is in inprogress status for that QR, either that payment should be completed or cancelled before initiating a new payment on the same QR Take a note that every QR should be mapped to a particular unique counter/terminal in your system for better order reconciliation.",
    "3-2": "STQI-test-2",
    "4-0": "productinfo  \n`mandatory`",
    "4-1": "`string` This parameter must contain the same value of product information which was sent in the transaction request from merchant’s end to PayU.",
    "4-2": "Integrated Static QR",
    "5-0": "expirytime  \n`mandatory`",
    "5-1": "`string` This parameter must contain the expiry time of the transaction & will always be in seconds",
    "5-2": "3600",
    "6-0": "udf3  \n`optional`",
    "6-1": "`string` This parameter must contain the same value of udf3 which was sent in the transaction request from merchant’s end to PayU.",
    "6-2": "",
    "7-0": "udf4  \n`optional`",
    "7-1": "`string` This parameter must contain the same value of udf4 which was sent in the transaction request from merchant’s end to PayU",
    "7-2": "",
    "8-0": "udf5  \n`optional`",
    "8-1": "`string` This parameter must contain the same value of udf5 which was sent in the transaction request from merchant’s end to PayU",
    "8-2": "",
    "9-0": "firstname  \n`optional`",
    "9-1": "`string` This parameter must contain the value of customer firstname who is paying the transaction amount using QR",
    "9-2": "Ravi",
    "10-0": "lastname  \n`optional`",
    "10-1": "`string` This parameter must contain the value of customer last name who is paying the transaction amount using Q",
    "10-2": "",
    "11-0": "email  \n`optional`",
    "11-1": "`string` This parameter must contain the value of customer Email who is paying the transaction amount using QR",
    "11-2": "[test@example.com](mailto:test@example.com)",
    "12-0": "phone  \n`optional`",
    "12-1": "`string` This parameter must contain the value of customer phone number who is paying the transaction amount using QR",
    "12-2": "1234567890",
    "13-0": "hash  \n`mandatory`",
    "13-1": "`string` This parameter must be include absolutely crucial and is similar to the hash parameter used in the transaction request send by the merchant to PayU. PayU calculates the hash using a string of other parameters and returns to the merchant. The merchant must verify the hash and then only mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with. The hash calculation is in the following format: `sha512(SALT\\|status\\||\\||\\||udf5\\|udf4\\|udf3\\|udf2\\|udf1\\|email\\|firstname\\|productinfo \\|amount\\|txnid\\|key)  `  \nThe handling of udf1 – udf5 parameters remains similar to the hash calculation when the merchant sends it in the transaction request to PayU.  \nIf any of the udf (udf1- udf5) was posted in the transaction request, it must be taken in hash calculation also. If none of the udf parameters were posted in the transaction request, they should be left empty in the hash calculation too.",
    "13-2": "`5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21`"
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```Text cURL
curl --location --request POST 'https://secure.payu.in/QrPayment' \
--data-urlencode 'key=J****g' \
--data-urlencode 'txnid=txn1234' \
--data-urlencode 'amount=100' \
--data-urlencode 'qrId=qr123' \
--data-urlencode 'productinfo=Integrated Static QR' \
--data-urlencode 'expirytime=3600' \
--data-urlencode 'UDF3=Gurgaon' \
--data-urlencode 'UDF4=120001' \
--data-urlencode 'UDF5=India' \
--data-urlencode 'firstname=Payu' \
--data-urlencode 'lastname=user' \
--data-urlencode 'email=test@payu.in' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'hash=5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21'
```
```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "key=J****g&txnid=txn1234&amount=100&qrId=qr123&productinfo=Integrated Static QR&expirytime=3600&UDF3=Gurgaon&UDF4=120001&UDF5=India&firstname=Payu&lastname=user&email=test@payu.in&phone=1234567890&hash=5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21");
Request request = new Request.Builder()
  .url("https://secure.payu.in/QrPayment")
  .method("POST", body)
  .build();
Response response = client.newCall(request).execute();
```
```Text Python
import requests

url = "https://secure.payu.in/QrPayment"

payload='key=J****g&txnid=txn1234&amount=100&qrId=qr123&productinfo=Integrated%20Static%20QR&expirytime=3600&UDF3=Gurgaon&UDF4=120001&UDF5=India&firstname=Payu&lastname=user&email=test%40payu.in&phone=1234567890&hash=5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21'
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
```Text php
<?php
$curl = curl_init();
curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://secure.payu.in/QrPayment',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'key=J****g&txnid=txn1234&amount=100&qrId=qr123&productinfo=Integrated%20Static%20QR&expirytime=3600&UDF3=Gurgaon&UDF4=120001&UDF5=India&firstname=Payu&lastname=user&email=test%40payu.in&phone=1234567890&hash=5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
```Text Ruby
require "uri"
require "net/http"

url = URI("https://secure.payu.in/QrPayment")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request.body = "key=J****g&txnid=txn1234&amount=100&qrId=qr123&productinfo=Integrated%20Static%20QR&expirytime=3600&UDF3=Gurgaon&UDF4=120001&UDF5=India&firstname=Payu&lastname=user&email=test%40payu.in&phone=1234567890&hash=5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21"

response = https.request(request)
puts response.read_body
```