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

| Environment | URI                                                                  |
| :---------- | :------------------------------------------------------------------- |
| Production  | [https://secure.payu.in/QrPayment](https://secure.payu.in/QrPayment) |

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
        string This parameter must contain the merchant key for the merchant’s account at PayU.<br />Reference: For more information on how to generate the Key and Salt, refer to any of the following:<br />Production: Generate Production Merchant Key and Sat.<br />Test: Generate Test Merchant Key and Salt.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        txnid<br />`mandatory`
      </td>

      <td>
        `string` This parameter must contain the transaction ID value posted by the merchant during the transaction request.
      </td>

      <td>
        f7f48de5853f4ebdacef
      </td>
    </tr>

    <tr>
      <td>
        amount<br />`mandatory`
      </td>

      <td>
        `string` This parameter must contain the original amount which was sent in the transaction request by the merchant.
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        qrId<br />`mandatory`
      </td>

      <td>
        `string` This parameter must contain the unique reference id embedded in the QR using which you want to collect payment from the customer. Remember that at any one point of time, you can collect only 1 payment using a single QR. In case there is a previous payment which is in inprogress status for that QR, either that payment should be completed or cancelled before initiating a new payment on the same QR Take a note that every QR should be mapped to a particular unique counter/terminal in your system for better order reconciliation.
      </td>

      <td>
        STQI-test-2
      </td>
    </tr>

    <tr>
      <td>
        productinfo<br />`mandatory`
      </td>

      <td>
        `string` This parameter must contain the same value of product information which was sent in the transaction request from merchant’s end to PayU.
      </td>

      <td>
        Integrated Static QR
      </td>
    </tr>

    <tr>
      <td>
        expirytime<br />`mandatory`
      </td>

      <td>
        `string` This parameter must contain the expiry time of the transaction & will always be in seconds
      </td>

      <td>
        3600
      </td>
    </tr>

    <tr>
      <td>
        udf3<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the same value of udf3 which was sent in the transaction request from merchant’s end to PayU.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the same value of udf4 which was sent in the transaction request from merchant’s end to PayU
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf5<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the same value of udf5 which was sent in the transaction request from merchant’s end to PayU
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        firstname<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the value of customer firstname who is paying the transaction amount using QR
      </td>

      <td>
        Ravi
      </td>
    </tr>

    <tr>
      <td>
        lastname<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the value of customer last name who is paying the transaction amount using Q
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        email<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the value of customer Email who is paying the transaction amount using QR
      </td>

      <td>
        [test@example.com](mailto:test@example.com)
      </td>
    </tr>

    <tr>
      <td>
        phone<br />`optional`
      </td>

      <td>
        `string` This parameter must contain the value of customer phone number who is paying the transaction amount using QR
      </td>

      <td>
        1234567890
      </td>
    </tr>

    <tr>
      <td>
        hash<br />`mandatory`
      </td>

      <td>
        `string` This parameter must be included absolutely crucial and is similar to the hash parameter used in the transaction request send by the merchant to PayU. PayU calculates the hash using a string of other parameters and returns to the merchant. The merchant must verify the hash and then only mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with. The hash calculation is in the following format: `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo |amount|txnid|key)  `<br />The handling of udf1 – udf5 parameters remains similar to the hash calculation when the merchant sends it in the transaction request to PayU.<br />If any of the udf (udf1- udf5) was posted in the transaction request, it must be taken in hash calculation also. If none of the udf parameters were posted in the transaction request, they should be left empty in the hash calculation too.
      </td>

      <td>
        `5606747fec73bd7a271748f13c06626d6520b5ba1af9db7338b9a1d2d9d6da77c9291304f7a78fe4bf02319702f56131c868306a5280daf18038a1d8bdbdef21`
      </td>
    </tr>
  </tbody>
</Table>

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

## Sample response

The formatted success response is similar to the following:

```json
{
  "mihpayid": "403993715521937565",
  "mode": "UPI",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "J****g",
  "txnid": "txn1234",
  "amount": "100.00",
  "cardCategory": "",
  "discount": "0.00",
  "net_amount_debit": "100",
  "addedon": "2026-01-20 10:30:45",
  "productinfo": "Integrated Static QR",
  "firstname": "Payu",
  "lastname": "user",
  "address1": "",
  "address2": "",
  "city": "",
  "state": "",
  "country": "",
  "zipcode": "",
  "email": "test@payu.in",
  "phone": "1234567890",
  "udf1": "",
  "udf2": "",
  "udf3": "Gurgaon",
  "udf4": "120001",
  "udf5": "India",
  "udf6": "",
  "udf7": "",
  "udf8": "",
  "udf9": "",
  "udf10": "",
  "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
  "field1": "",
  "field2": "",
  "field3": "",
  "field4": "",
  "field5": "",
  "field6": "",
  "field7": "",
  "field8": "",
  "field9": "Transaction Completed Successfully",
  "payment_source": "payu",
  "PG_TYPE": "UPI-QR",
  "bank_ref_num": "123456789012",
  "bankcode": "UPI",
  "error": "E000",
  "error_Message": "No Error"
}
```

<br />
