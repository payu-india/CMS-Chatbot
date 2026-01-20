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

#### Environment

| Environment | URI                                                                                            |
| :---------- | :--------------------------------------------------------------------------------------------- |
| Production  | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

## Request parameters

| Parameter           | Description                                                                                                                                                                                                                                                                         | Sample Value                  |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| key `mandatory`     | string This parameter must include the merchant key that was provided by PayU. Reference: For more information on how to generate the Key and Salt, refer to any of the following: Production: Generate Production Merchant Key and Sat. Test: Generate Test Merchant Key and Salt. | Your Test Key                 |
| command `mandatory` | `string` The parameter must contain the name of the web service. For this API, `generate_upi_intent` must be posted.                                                                                                                                                                | generate_upi_intent           |
| hash `mandatory`    | string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below: `sha512(key\|command\|var1\|salt)` sha512 is the encryption method used here.                                                          | ajh84babvav                   |
| var1 `mandatory`    | json This parameter will include a JSON format of the transaction details. For more information, refer to the >.                                                                                                                                                                    | Refer the var Sample section. |

### Description of var1 Parameter Fields

| Field                         | Description                                                                                                                                                                                   | Example                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| transactionId `mandatory`     | `string`  This must contain the merchant transaction Identifier. This must be unique (after a successful transaction) & alphanumeric special (less than 40 characters & excluding >,\<, &, ') | 1234_abcdedf                          |
| transactionAmount `mandatory` | `float`  This must contain the amount for which QR needs to be generated. This must be greater than or equal to 1.00.                                                                         | 1005, 1042.23, 95494.4, 10000.00      |
| merchantVpa `optional`        | `string`  This must contain the merchant's VPA in which payment will be collected. If not sent, VPA registered against given merchant Key is used.                                            | yellowqr.payu@hdfc                    |
| txnNote `optional`            | `string` This must contain the transaction note to be embedded in the link. This will be visible to customer at the time of payment.                                                          | collect                               |
| expiryTime `optional`         | `numeric` This must contain the  time in seconds for which the QR is active. If empty, merchant level expiry is used. If there is no merchant level value, the global value is used.          | 3600                                  |
| name `optional`               | `string` This field must contain the customer name.                                                                                                                                           | Ravi                                  |
| city `optional`               | `string` This field must contain the customer's city.                                                                                                                                         | 122001                                |
| phone `optional`              | `string` This field must contain the customer phone number.                                                                                                                                   | 9833207164                            |
| email `optional`              | `string` This field must contain the customer email address.                                                                                                                                  | [hello@payu.in](mailto:hello@payu.in) |
| pincode                       | `string` This field must contain the PIN code in customer's address.                                                                                                                          | 560032                                |
| address `optional`            | `string`  This field must contain the customer's address. It can be up to 100 characters. Anything after the first 100 characters will be ignored                                             | Payu, Bestech Business Tower, Gurgaon |
| udf3 - udf5 `optional`        | `string` This field must contain the user-defined fields such as udf3, udf4 and udf5 can be sent in request to include any transactional information.                                         |                                       |
| gst `optional`                | `string`  This must contain the applicable GST amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.                                         | 100.25                                |
| cgst `optional`               | `string`  This must contain the applicable CFST amount for that transaction. Only applicable in case you want to embed GST specific details.                                                  | 25.45                                 |
| sgst `optional`               | `string` This must contain the SGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.                                                    | 25.45                                 |
| igst `optional`               | `string`  This must contain the IGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.                                                   | 50.9                                  |
| cess `optional`               | `string` This must contain the cess amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.                                                    | 10.2                                  |
| gstIncentive `optional`       | `string` This must contain the GST Incentive amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.                                           | 10.2                                  |
| gstPercentage `optional`      | `string` This must contain the GST percentage for that transaction. Only applicable in case you want to embed GST specific details in the QR.                                                 | 18                                    |
| gstIn `optional`              | `string`  This is the GSTIN of the legal entity of the merchant. Only applicable in case you want to embed GST specific details in the QR.                                                    | 24AAACC1206D1ZM                       |
| invoiceName `optional`        | `string` This must contain the name of the invoice for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.                                       | Bill                                  |
| invoiceNo `optional`          | `string` This is the invoice number for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.                                                      | 78457637                              |
| invoiceDate `optional`        | `string`  This is the invoice date for which QR will be used. It should always be in GMT format. Only applicable in case you want to embed GST specific details in the QR.                    | 2021-05-21T13:21:50+05:30             |
| purpose `optional`            | `string` This is the purpose for which QR will be used. This param will have fixed values basis your business type. Please take the value from our integration team.                          | 3                                     |
| refUrl `optional`             | `string` This field can be used to share invoice copy or any other transaction related information/documents to customer for their reference.                                                 | [https://payu.in/](https://payu.in/)  |
| category `optional`           | `string`  This field is mandatory when refUrl is passed. Use 01 for advertisement & 02 for invoice.                                                                                           | 01 or 02                              |

### var1 sample

The var1 parameter is similar to the following JSON format and description of fields in the JSON is described in the following table:

```json
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
> * The customer details are optional. If not posted, the default value is null. The following rules are to be followed while sending customer details:
>   * Phone number and email address are to be sent in their respective formats.
>   * customerAddress can be up to 100 characters. The first 100 characters will be truncated if the value is more than 100 characters for this parameter.
> * VendorKey should always be unique and different for every new QR generated. The parameter should be alphanumeric & less than or equal to 10 characters.
> * The response sent for QR generation request is JSON encoded and will be a base64 encoded string of the actual QR image, so to obtain the actual QR image, first decode the json encoded response and then convert the base64 encoded string to actual QR image.
> * For every QR generation request, in the response PayU will share back the unique identifier, qrId, embedded in the QR. This reference id is generated based on the vendor key shared in the QR generation request.
> * Map the QR image to this qrId and with respective terminal at which you will use this QR. These details need to be sent to PayU during payment initiation request sent for a particular terminal.

## Sample request

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php' \
--data-urlencode 'key=J****g' \
--data-urlencode 'command=generate_upi_intent' \
--data-urlencode 'hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1' \
--data-urlencode 'var1={"transactionId":"0fd9829f68", "transactionAmount":"190","expiryTime":"10000","refUrl":"http://www.payu.in"}'
```
```python
import http.client
conn = http.client.HTTPSConnection("info.payu.in")
payload = 'key=J****g&command=generate_upi_intent&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionId%22%3A%220fd9829f68%22%2C%20%22transactionAmount%22%3A%22190%22%2C%22expiryTime%22%3A%2210000%22%2C%22refUrl%22%3A%22http%3A%2F%2Fwww.payu.in%22%7D'
headers = {}
conn.request("POST", "/merchant/postservice.php", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```php
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
```java
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
```ruby
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

| Parameter | Description                                                                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status    | This parameter returns the status of web service call. The status can be any of the following:  0 - If web service call failed. 1 - If web service call succeeded |
| msg       | This parameter returns the following message if the offline intent link was generated successfully: `Intent link generated`                                       |
| link      | This parameter returns the link if the offline intent link is generated successfully.                                                                             |

## Sample response

### Success Scenario

```json
{
  "status": "success",
  "message": "Intent Link generated",
  "link": "https://secure.payu.in/omni?id=000H"
}
```

### Failure Scenarios

* **Amount mismatch**

```json
{
    "status": "failed",
    "message": "link already exists but amount mismatch with existing link amount",
    "errorCode": "E2030"
}
```

* **Intent Link Already Exists**

```json
{
  "status": "success",
  "message": "Intent Link already exists",
  "link": "https://secure.payu.in/omni?id=000F"
}
```

* **Already Used Transaction ID**

```json
{
  "status": "failed",
  "message": "TransactionId already used. Please use a different one.",
  "errorCode": "E2012"
}
```
