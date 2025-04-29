---
title: Integrated Static Bharat QR Generation API
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
The **Static QR Generation** API is used to generate Static UPI or Bharat QR. The QR generated through this API is interoperable and can be used by any UPI application like Google Pay, PhonePe, etc. These QR codes can be used for accepting multiple transactions where customers can select the exact amount by themselves before making the payment. Bharat QR can also be scanned using mobile banking and credit card applications like (iMobile, SBI cards, etc.) to make transactions using debit cards and credit cards.

| Environments | URL                                             |
| :----------- | :---------------------------------------------- |
| Production   | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "`string` This parameter must include the merchant key that was provided by PayU",
    "0-2": "vDy3i7",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, `generate_integrated_static_qr` must be posted.",
    "1-2": "generate_integrated_static_qr",
    "2-0": "hash  \n`mandatory`",
    "2-1": "`string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \n  \nsha512(key|command|var1|salt)  \nsha512 is the encryption method used here.",
    "2-2": "ajh84babvav",
    "3-0": "var1  \n`mandatory`",
    "3-1": "json This parameter will include a JSON format of the transaction details. For more information, refer to the >.",
    "3-2": "Refer the <<var Sample>> section."
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


### Description of var1 parameter fields

[block:parameters]
{
  "data": {
    "h-0": "Key",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "customerId   \n`conditional`",
    "0-1": "`numeric` Merchant Transaction Identifier. Should be unique & numeric special (less than or equal to 20 characters & Only \".\" is allowed)",
    "0-2": "1234abcd",
    "1-0": "merchantVpa customerId  \n`conditional`",
    "1-1": "`string` Merchant's VPA in which payment will be collected.VPA to be embedded in QR. Should be unique & alphanumeric special (less than or equal to 50 characters & Only \"@\", \".\", \",\" are allowed). The variable part of the VPA series can only be numeric, for eg. if the series configured is _.payu@hdfc then the VPA can only be 123445.payu@hdfc and not a13s.payu@hdfc (_ part of the series will always be numeric)",
    "1-2": "instadummy.001@hdfcbank",
    "2-0": "name customerId  \n`optional`",
    "2-1": "`string` Customer details, to be embedded in QR (less than or equal to 20 characters).If not sent, merchant’s name registered during the onboarding process will be used.",
    "2-2": "Test User",
    "3-0": "city   \n`optional`",
    "3-1": "`string` Customer details, to be embedded in QR (less than or equal to 15 characters).If not sent, merchant’s city registered during the onboarding process will be used",
    "3-2": "Gurgaon",
    "4-0": "pinCode   \n`optional`",
    "4-1": "`string` Customer details, to be embedded in the QR(less than or equal to 10 characters). If not sent, merchant’s pincode registered during the onboarding process will be used.",
    "4-2": "122001",
    "5-0": "instaProduct   \n`mandatory`",
    "5-1": "`string` QR generation flag. Fixed value - qr",
    "5-2": "qr",
    "6-0": "address  \n`optional`",
    "6-1": "`string` Customer address(less than or equal to 100 characters).",
    "6-2": "Payu, Bestech Business Tower, Gurgaon",
    "7-0": "udf1 - udf5   \n`optional`",
    "7-1": "`string` udf1, udf2, udf3, udf4 and udf5 can be sent in request to include any transactional information.",
    "7-2": "",
    "8-0": "outputType  \n`optional`",
    "8-1": "`string` outputType can be '', 'string' and 'base64'. By default, base64 json encoded qrSting in response is sent.",
    "8-2": "string",
    "9-0": "submerchantRegistration   \n`optional`",
    "9-1": "`string` submerchantRegistration can be '1'or '0'. If '1' is passed then the request is passed to the acquiring bank and if '0' is passed the request is processed internally at PayU end.",
    "9-2": "1 or 0",
    "10-0": "mebussname   \n`optional`",
    "10-1": "`string` mebussname will be visible to the customers upon scanning this QR.  \nFor non-aggregator merchants, the mebussname will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \nFor aggregator-merchants, the mebussname passed in this key should largely match with the name on the PAN card of the details passed in the panNo key.  \nThis key is mandatory for the aggregator-merchants",
    "10-2": "PayU",
    "11-0": "strCntMobile   \n`conditional`",
    "11-1": "`string` This will be the phone number associated for the entity for whom VPA is being created.  \nFor non-aggregator merchants, it will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored. For aggregator-merchants, the strCntMobile is mandatory.",
    "11-2": "9833270176",
    "12-0": "panNo   \n`conditional`",
    "12-1": "`string` This will be the pan number associated for the entity for whom VPA is being created.  \nFor non-aggregator merchants, the panNo will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored  \nFor aggregator-merchants, the panNo of the actual beneficiary needs to be passed. This key is mandatory for the aggregator-merchants.",
    "12-2": "BPEPK5437G",
    "13-0": "legalStrName   \n`conditional`",
    "13-1": "`string` This will be the legal name associated for the entity for whom VPA is being created.  \nFor non-aggregator merchants, it will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \nFor aggregator-merchants, the legalStrName should largely match with the name on the PAN card of the details passed in the panNo key. This key is mandatory for the aggregator-merchants.",
    "13-2": "PayU payments pvt ltd",
    "14-0": "awlmcc   \n`conditional`",
    "14-1": "`string` Merchant Category code is as per NPCI guidelines and is typically a numeric value of length = 4.  \nFor non-aggregator merchants, the merchant category code will be picked up from the details registered with PayU. Any detail passed by the merchant would be ignored.  \nFor aggregator-merchants, the merchant category code of the actual beneficiary needs to be passed.  \nThis key is mandatory for the aggregator-merchants",
    "14-2": "7999"
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## var1 sample

The `var1` parameter is similar to the following JSON format and description of fields in the JSON is described in the following table:

```Text JSON
{
  "vendorKey": "test",
  "qrName": "ronaldo",
  "qrCity": "madrid",
  "qrPinCode": "28001"
}
```

## Response parameters

| Parameter | Description                                                                                                                                                                                                                       |
| :-------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| image     | Image of the QR code will be returned, either BQR or UPI QR                                                                                                                                                                       |
| string    | QR String is plain text will be returned in response along with QR ID & VPA associated to the QR, the QR string can be converted into image and used for accepting transactions.                                                  |
| base64    | Base 64 encoded string will be returned in response along with QR ID & VPA associated to the QR, the encoded string provides a layer of security which can be eventually converted into image and used for accepting transactions |

> 🚧 Callout
> 
> - The QrName, qrCity and qrPincode parameters are optional. The following values for these parameters are embedded in the QR when these parameters is empty or not set, merchant details are used as follows:
>   - **qrName**: Merchant’s name registered during the onboarding process.
>   - **qrCity**: Merchant’s city registered during the onboarding process.
>   - **qrPinCode**: Merchant’s PIN code registered during the onboarding process.
> - The customer details are optional. If not posted, the default value is null. The following rules are to be followed while sending customer details:
>   - Phone number and email address are to be sent in their respective formats.
>   - **customerAddress** can be up to 100 characters. The first 100 characters will be truncated if the value is more than 100 characters for this parameter.
> - VendorKey should always be unique and different for every new QR generated. The parameter should be alphanumeric & less than or equal to 10 characters.
> - The response sent for QR generation request is JSON encoded and will be a base64 encoded string of the actual QR image, so to obtain the actual QR image, first decode the json encoded response and then convert the base64 encoded string to actual QR image.
> - For every QR generation request, in the response PayU will share back the unique identifier, qrId, embedded in the QR. This reference id is generated based on the vendor key shared in the QR generation request.
> - Map the QR image to this qrId and with respective terminal at which you will use this QR. These details need to be sent to PayU during payment initiation request sent for a particular terminal.

## Sample request

- **Static UPI QR**

```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "command=generate_dynamic_bharat_qr&key=vDy3i7&hash=87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846&var1={\"transactionId\":\"DBQR1981\",\"transactionAmount\":\"1\",\"merchantVpa\":\"gauravdua1.payu@indus\",\"expiryTime\":\"3600\",\"qrName\":\"payu\",\"qrCity\":\"Gurgaon\",\"qrPinCode\":\"122001\",\"customerName\":\"Ravi\",\"customerCity\":\"Ranchi\",\"customerPinCode\":\"834001\",\"customerPhoe\":\"7800078000\",\"customerEmail\":\"hello@payu.in\",\"customerAddress\":\"Ggn\",\"udf3\":\"deliveryboy1\",\"udf4\":\"sector14\",\"udf5\":\"cod\",\"outputType\":\"string\"}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```
```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'command=generate_dynamic_bharat_qr' \
--data-urlencode 'key=vDy3i7' \
--data-urlencode 'hash=87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846' \
--data-urlencode 'var1={"transactionId":"DBQR1981","transactionAmount":"1","merchantVpa":"gauravdua1.payu@indus","expiryTime":"3600","qrName":"payu","qrCity":"Gurgaon","qrPinCode":"122001","customerName":"Ravi","customerCity":"Ranchi","customerPinCode":"834001","customerPhoe":"7800078000","customerEmail":"hello@payu.in","customerAddress":"Ggn","udf3":"deliveryboy1","udf4":"sector14","udf5":"cod","outputType":"string"}'
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'command=generate_dynamic_bharat_qr&key=vDy3i7&hash=87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846&var1=%7B%22transactionId%22%3A%22DBQR1981%22%2C%22transactionAmount%22%3A%221%22%2C%22merchantVpa%22%3A%22gauravdua1.payu%40indus%22%2C%22expiryTime%22%3A%223600%22%2C%22qrName%22%3A%22payu%22%2C%22qrCity%22%3A%22Gurgaon%22%2C%22qrPinCode%22%3A%22122001%22%2C%22customerName%22%3A%22Ravi%22%2C%22customerCity%22%3A%22Ranchi%22%2C%22customerPinCode%22%3A%22834001%22%2C%22customerPhoe%22%3A%227800078000%22%2C%22customerEmail%22%3A%22hello%40payu.in%22%2C%22customerAddress%22%3A%22Ggn%22%2C%22udf3%22%3A%22deliveryboy1%22%2C%22udf4%22%3A%22sector14%22%2C%22udf5%22%3A%22cod%22%2C%22outputType%22%3A%22string%22%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('https://info.payu.in/merchant/postservice.php');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'command' => 'generate_dynamic_bharat_qr',
  'key' => 'vDy3i7',
  'hash' => '87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846',
  'var1' => '{"transactionId":"DBQR1981","transactionAmount":"1","merchantVpa":"gauravdua1.payu@indus","expiryTime":"3600","qrName":"payu","qrCity":"Gurgaon","qrPinCode":"122001","customerName":"Ravi","customerCity":"Ranchi","customerPinCode":"834001","customerPhoe":"7800078000","customerEmail":"hello@payu.in","customerAddress":"Ggn","udf3":"deliveryboy1","udf4":"sector14","udf5":"cod","outputType":"string"}'
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
```Text Ruby
require "uri"
require "net/http"

url = URI("https://info.payu.in/merchant/postservice.php")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request.body = "command=generate_dynamic_bharat_qr&key=vDy3i7&hash=87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846&var1=%7B%22transactionId%22%3A%22DBQR1981%22%2C%22transactionAmount%22%3A%221%22%2C%22merchantVpa%22%3A%22gauravdua1.payu%40indus%22%2C%22expiryTime%22%3A%223600%22%2C%22qrName%22%3A%22payu%22%2C%22qrCity%22%3A%22Gurgaon%22%2C%22qrPinCode%22%3A%22122001%22%2C%22customerName%22%3A%22Ravi%22%2C%22customerCity%22%3A%22Ranchi%22%2C%22customerPinCode%22%3A%22834001%22%2C%22customerPhoe%22%3A%227800078000%22%2C%22customerEmail%22%3A%22hello%40payu.in%22%2C%22customerAddress%22%3A%22Ggn%22%2C%22udf3%22%3A%22deliveryboy1%22%2C%22udf4%22%3A%22sector14%22%2C%22udf5%22%3A%22cod%22%2C%22outputType%22%3A%22string%22%7D"

response = https.request(request)
puts response.read_body
```

## Sample response

- Static UPI QR

```Text JSON
{
  "qrString": "upi://pay?pa=gauravdua1.payu@indus&pn=smsplus&mc=7399&tr=DYQ13845198863&ver=01&mode=15&orgid=000000&qrMedium=06&cu=INR&purpose=02&pinCode=122002&am=1.00&QRexpire=2021-08-20T17:48:19+05:30"
}
```

- Static Bharat QR

```Text JSON
{
    "qrString": "000201010211021644038470007469080415522024070007469061661000307000746960825HDFC00006225020001855322626470010A0000005240129yellowqr.payutest.94@hdfcbank27370010A0000005240119STQ9y45z1cv3z5450925204569153033565802IN5910vendorName6010vendorCity610650017262350519STQ9y45z1cv3z545092070870007469630417EF",
}
```