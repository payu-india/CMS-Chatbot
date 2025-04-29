---
title: Offline Intent Link Generation API
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
The **Offline Intent Link Generation** API is used to generate UPI Intent link. The link can be shared with the customers for payment acceptance through UPI.

| Environment | URI                                             |
| :---------- | :---------------------------------------------- |
| Production  | <https://info.payu.in/merchant/postservice.php> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Sample Value",
    "0-0": "key  \n`mandatory`",
    "0-1": "string This parameter must include the merchant key that was provided by PayU.  \nReference: For more information on how to generate the Key and Salt, refer to any of the following:  \nProduction: Generate Production Merchant Key and Sat.  \nTest: Generate Test Merchant Key and Salt.",
    "0-2": "Your Test Key",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, `generate_upi_intent` must be posted.",
    "1-2": "generate_upi_intent",
    "2-0": "hash  \n`mandatory`",
    "2-1": "string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \n`sha512(key\\|command\\|var1\\|salt)`  \nsha512 is the encryption method used here.",
    "2-2": "ajh84babvav",
    "3-0": "var1  \n`mandatory`",
    "3-1": "json This parameter will include a JSON format of the transaction details. For more information, refer to the >.",
    "3-2": "Refer the <var Sample section.>"
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


### Description of var1 Parameter Fields

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "transactionId  \n`mandatory`",
    "0-1": "`string`  This must contain the merchant transaction Identifier. This must be unique (after a successful transaction) & alphanumeric special (less than 40 characters & excluding >,\\<, &, ‘)",
    "0-2": "1234_abcdedf",
    "1-0": "transactionAmount  \n`mandatory`",
    "1-1": "`float`  This must contain the amount for which QR needs to be generated. This must be greater than or equal to 1.00.",
    "1-2": "1005, 1042.23, 95494.4, 10000.00",
    "2-0": "merchantVpa  \n`optional`",
    "2-1": "`string`  This must contain the merchant's VPA in which payment will be collected. If not sent, VPA registered against given merchant Key is used.",
    "2-2": "yellowqr. payu@hdfc",
    "3-0": "txnNote  \n`optional`",
    "3-1": "`string` This must contain the transaction note to be embedded in the link. This will be visible to customer at the time of payment.",
    "3-2": "collect",
    "4-0": "expiryTime  \n`optional`",
    "4-1": "`numeric` This must contain the  time in seconds for which the QR is active. If empty, merchant level expiry is used. If there is no merchant level value, the global value is used.",
    "4-2": "3600",
    "5-0": "name  \n`optional`",
    "5-1": "`string` This field must contain the customer name.",
    "5-2": "Ravi",
    "6-0": "city  \n`optional`",
    "6-1": "`string` This field must contain the customer's city.",
    "6-2": "122001",
    "7-0": "phone  \n`optional`",
    "7-1": "`string` This field must contain the customer phone number.",
    "7-2": "9833207164",
    "8-0": "email  \n`optional`",
    "8-1": "`string` This field must contain the customer email address.",
    "8-2": "[hello@payu.in](mailto:hello@payu.in)",
    "9-0": "pincode",
    "9-1": "`string` This field must contain the PIN code in customer's address.",
    "9-2": "560032",
    "10-0": "address  \n`optional`",
    "10-1": "`string`  This field must contain the customer's address. It can be up to 100 characters. Anything after the first 100 characters will be ignored",
    "10-2": "Payu, Bestech Business Tower, Gurgaon",
    "11-0": "udf3 - udf5  \n`optional`",
    "11-1": "`string` This field must contain the user-defined fields such as udf3, udf4 and udf5 can be sent in request to include any transactional information.",
    "11-2": "",
    "12-0": "gst  \n`optional`",
    "12-1": "`string`  This must contain the applicable GST amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.",
    "12-2": "100.25",
    "13-0": "cgst  \n`optional`",
    "13-1": "`string`  This must contain the applicable CFST amount for that transaction. Only applicable in case you want to embed GST specific details.",
    "13-2": "25.45",
    "14-0": "sgst  \n`optional`",
    "14-1": "`string` This must contain the SGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "14-2": "25.45",
    "15-0": "igst  \n`optional`",
    "15-1": "`string`  This must contain the IGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "15-2": "50.9",
    "16-0": "cess  \n`optional`",
    "16-1": "`string` This must contain the cess amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.",
    "16-2": "10.2",
    "17-0": "gstIncentive  \n`optional`",
    "17-1": "`string` This must contain the GST Incentive amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "17-2": "10.2",
    "18-0": "gstPercentage  \n`optional`",
    "18-1": "`string` This must contain the GST percentage for that transaction. Only applicable in case you want to embed GST specific details in the QR.",
    "18-2": "18",
    "19-0": "gstIn  \n`optional`",
    "19-1": "`string`  This is the GSTIN of the legal entity of the merchant. Only applicable in case you want to embed GST specific details in the QR.",
    "19-2": "24AAACC1206D1ZM",
    "20-0": "invoiceName  \n`optional`",
    "20-1": "`string` This must contain the name of the invoice for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.",
    "20-2": "Bill",
    "21-0": "invoiceNo  \n`optional`",
    "21-1": "`string` This is the invoice number for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.",
    "21-2": "78457637",
    "22-0": "invoiceDate  \n`optional`",
    "22-1": "`string`  This is the invoice date for which QR will be used. It should always be in GMT format. Only applicable in case you want to embed GST specific details in the QR.",
    "22-2": "2021-05-21T13:21:50+05:30",
    "23-0": "purpose  \n`optional`",
    "23-1": "`string` This is the purpose for which QR will be used. This param will have fixed values basis your business type. Please take the value from our integration team.",
    "23-2": "3",
    "24-0": "refUrl  \n`optional`",
    "24-1": "`string` This field can be used to share invoice copy or any other transaction related information/documents to customer for their reference.",
    "24-2": "<https://payu.in/>",
    "25-0": "category  \n`optional`",
    "25-1": "`string`  This field is mandatory when refUrl is passed. Use 01 for advertisement & 02 for invoice.",
    "25-2": "01 or 02"
  },
  "cols": 3,
  "rows": 26,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### var1 sample

The var1 parameter is similar to the following JSON format and description of fields in the JSON is described in the following table:

```Text JSON
{
  "transactionId": "Intenttest4vfr",
  "transactionAmount": "1",
  "expiryTime": "360000000000000"
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
> - The customer details are optional. If not posted, the default value is null. The following rules are to be followed while sending customer details:
>   - Phone number and email address are to be sent in their respective formats.
>   - customerAddress can be up to 100 characters. The first 100 characters will be truncated if the value is more than 100 characters for this parameter.
> - VendorKey should always be unique and different for every new QR generated. The parameter should be alphanumeric & less than or equal to 10 characters.
> - The response sent for QR generation request is JSON encoded and will be a base64 encoded string of the actual QR image, so to obtain the actual QR image, first decode the json encoded response and then convert the base64 encoded string to actual QR image.
> - For every QR generation request, in the response PayU will share back the unique identifier, qrId, embedded in the QR. This reference id is generated based on the vendor key shared in the QR generation request.
> - Map the QR image to this qrId and with respective terminal at which you will use this QR. These details need to be sent to PayU during payment initiation request sent for a particular terminal.

## Sample request

```Text cURL
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--data-urlencode 'key=J****g' \
--data-urlencode 'command=generate_upi_intent' \
--data-urlencode 'hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1' \
--data-urlencode 'var1={"transactionId":"0fd9829f68", "transactionAmount":"190","expiryTime":"10000","refUrl":"http://www.payu.in"}'
```
```Text Python
import http.client
conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J****g&command=generate_upi_intent&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionId%22%3A%220fd9829f68%22%2C%20%22transactionAmount%22%3A%22190%22%2C%22expiryTime%22%3A%2210000%22%2C%22refUrl%22%3A%22http%3A%2F%2Fwww.payu.in%22%7D'
headers = {}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text php
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
  CURLOPT_POSTFIELDS => 'key=vDy3i7&command=generate_upi_intent&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionId%22%3A%220fd9829f68%22%2C%20%22transactionAmount%22%3A%22190%22%2C%22expiryTime%22%3A%2210000%22%2C%22refUrl%22%3A%22http%3A%2F%2Fwww.payu.in%22%7D',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "command=generate_dynamic_bharat_qr&key=J****g&hash=87617bd37d7f2d627c5117ce0f1a97839200870c3281764bad542c90fc9684a2e2108257dfebbb32cfc4c2a83aa4b9bfe7761da745b14b3df2525e75a4eb6846&var1={\"transactionId\":\"DBQR1981\",\"transactionAmount\":\"1\",\"merchantVpa\":\"gauravdua1.payu@indus\",\"expiryTime\":\"3600\",\"qrName\":\"payu\",\"qrCity\":\"Gurgaon\",\"qrPinCode\":\"122001\",\"customerName\":\"Ravi\",\"customerCity\":\"Ranchi\",\"customerPinCode\":\"834001\",\"customerPhoe\":\"7800078000\",\"customerEmail\":\"hello@payu.in\",\"customerAddress\":\"Ggn\",\"udf3\":\"deliveryboy1\",\"udf4\":\"sector14\",\"udf5\":\"cod\",\"outputType\":\"string\"}");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```
```Text Ryby
require "uri"
require "net/http"

url = URI("https://info.payu.in/merchant/postservice.php")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request.body = "key=J****g&command=generate_upi_intent&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionId%22%3A%220fd9829f68%22%2C%20%22transactionAmount%22%3A%22190%22%2C%22expiryTime%22%3A%2210000%22%2C%22refUrl%22%3A%22http%3A%2F%2Fwww.payu.in%22%7D"

response = https.request(request)
puts response.read_body
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
    "1-1": "This parameter returns the following message if the offline intent link was generated successfully:  \n`Intent link generated`",
    "2-0": "link",
    "2-1": "This parameter returns the link if the offline intent link is generated successfully."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample response

### Success Scenario

```Text JSON
{
  "status": "success",
  "message": "Intent Link generated",
  "link": "https://secure.payu.in/omni?id=000H"
}
```

### Failure Scenarios

- **Amount mismatch**

```Text JSON
{
    "status": "failed",
    "message": "link already exists but amount mismatch with existing link amount",
    "errorCode": "E2030"
}
```

- **Intent Link Already Exists**

```Text JSON
{
  "status": "success",
  "message": "Intent Link already exists",
  "link": "https://secure.payu.in/omni?id=000F"
}
```

- **Already Used Transaction ID**

```Text JSON
{
  "status": "failed",
  "message": "TransactionId already used. Please use a different one.",
  "errorCode": "E2012"
}
```