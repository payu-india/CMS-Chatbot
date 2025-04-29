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

| Environment | URI                                                                                            |
| :---------- | :--------------------------------------------------------------------------------------------- |
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
        string This parameter must include the merchant key that was provided by PayU.\
        Reference: For more information on how to generate the Key and Salt, refer to any of the following:\
        Production: Generate Production Merchant Key and Sat.\
        Test: Generate Test Merchant Key and Salt.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        command\
        `mandatory`
      </td>

      <td>
        `string` The parameter must contain the name of the web service. For this API, `generate_upi_intent` must be posted.
      </td>

      <td>
        generate\_upi\_intent
      </td>
    </tr>

    <tr>
      <td>
        hash\
        `mandatory`
      </td>

      <td>
        string This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:\
        `sha512(key\|command\|var1\|salt)`\
        sha512 is the encryption method used here.
      </td>

      <td>
        ajh84babvav
      </td>
    </tr>

    <tr>
      <td>
        var1\
        `mandatory`
      </td>

      <td>
        json This parameter will include a JSON format of the transaction details. For more information, refer to the >.
      </td>

      <td>
        Refer the <var Sample section.>
      </td>
    </tr>
  </tbody>
</Table>

### Description of var1 Parameter Fields

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
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        transactionId
        `mandatory`
      </td>

      <td>
        `string`  This must contain the merchant transaction Identifier. This must be unique (after a successful transaction) & alphanumeric special (less than 40 characters & excluding >,\<, &, ‘)
      </td>

      <td>
        1234\_abcdedf
      </td>
    </tr>

    <tr>
      <td>
        transactionAmount\
        `mandatory`
      </td>

      <td>
        `float`  This must contain the amount for which QR needs to be generated. This must be greater than or equal to 1.00.
      </td>

      <td>
        1005, 1042.23, 95494.4, 10000.00
      </td>
    </tr>

    <tr>
      <td>
        merchantVpa\
        `optional`
      </td>

      <td>
        `string`  This must contain the merchant's VPA in which payment will be collected. If not sent, VPA registered against given merchant Key is used.
      </td>

      <td>
        yellowqr. payu\@hdfc
      </td>
    </tr>

    <tr>
      <td>
        txnNote\
        `optional`
      </td>

      <td>
        `string` This must contain the transaction note to be embedded in the link. This will be visible to customer at the time of payment.
      </td>

      <td>
        collect
      </td>
    </tr>

    <tr>
      <td>
        expiryTime\
        `optional`
      </td>

      <td>
        `numeric` This must contain the  time in seconds for which the QR is active. If empty, merchant level expiry is used. If there is no merchant level value, the global value is used.
      </td>

      <td>
        3600
      </td>
    </tr>

    <tr>
      <td>
        name\
        `optional`
      </td>

      <td>
        `string` This field must contain the customer name.
      </td>

      <td>
        Ravi
      </td>
    </tr>

    <tr>
      <td>
        city\
        `optional`
      </td>

      <td>
        `string` This field must contain the customer's city.
      </td>

      <td>
        122001
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `optional`
      </td>

      <td>
        `string` This field must contain the customer phone number.
      </td>

      <td>
        9833207164
      </td>
    </tr>

    <tr>
      <td>
        email\
        `optional`
      </td>

      <td>
        `string` This field must contain the customer email address.
      </td>

      <td>
        [hello@payu.in](mailto:hello@payu.in)
      </td>
    </tr>

    <tr>
      <td>
        pincode
      </td>

      <td>
        `string` This field must contain the PIN code in customer's address.
      </td>

      <td>
        560032
      </td>
    </tr>

    <tr>
      <td>
        address\
        `optional`
      </td>

      <td>
        `string`  This field must contain the customer's address. It can be up to 100 characters. Anything after the first 100 characters will be ignored
      </td>

      <td>
        Payu, Bestech Business Tower, Gurgaon
      </td>
    </tr>

    <tr>
      <td>
        udf3 - udf5\
        `optional`
      </td>

      <td>
        `string` This field must contain the user-defined fields such as udf3, udf4 and udf5 can be sent in request to include any transactional information.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        gst\
        `optional`
      </td>

      <td>
        `string`  This must contain the applicable GST amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.
      </td>

      <td>
        100.25
      </td>
    </tr>

    <tr>
      <td>
        cgst\
        `optional`
      </td>

      <td>
        `string`  This must contain the applicable CFST amount for that transaction. Only applicable in case you want to embed GST specific details.
      </td>

      <td>
        25.45
      </td>
    </tr>

    <tr>
      <td>
        sgst\
        `optional`
      </td>

      <td>
        `string` This must contain the SGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        25.45
      </td>
    </tr>

    <tr>
      <td>
        igst\
        `optional`
      </td>

      <td>
        `string`  This must contain the IGST amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        50.9
      </td>
    </tr>

    <tr>
      <td>
        cess\
        `optional`
      </td>

      <td>
        `string` This must contain the cess amount for that transaction. Only applicable in case you want to embed gst specific details in the QR.
      </td>

      <td>
        10.2
      </td>
    </tr>

    <tr>
      <td>
        gstIncentive\
        `optional`
      </td>

      <td>
        `string` This must contain the GST Incentive amount for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        10.2
      </td>
    </tr>

    <tr>
      <td>
        gstPercentage\
        `optional`
      </td>

      <td>
        `string` This must contain the GST percentage for that transaction. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        18
      </td>
    </tr>

    <tr>
      <td>
        gstIn\
        `optional`
      </td>

      <td>
        `string`  This is the GSTIN of the legal entity of the merchant. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        24AAACC1206D1ZM
      </td>
    </tr>

    <tr>
      <td>
        invoiceName\
        `optional`
      </td>

      <td>
        `string` This must contain the name of the invoice for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        Bill
      </td>
    </tr>

    <tr>
      <td>
        invoiceNo\
        `optional`
      </td>

      <td>
        `string` This is the invoice number for which QR will be used. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        78457637
      </td>
    </tr>

    <tr>
      <td>
        invoiceDate\
        `optional`
      </td>

      <td>
        `string`  This is the invoice date for which QR will be used. It should always be in GMT format. Only applicable in case you want to embed GST specific details in the QR.
      </td>

      <td>
        2021-05-21T13:21:50+05:30
      </td>
    </tr>

    <tr>
      <td>
        purpose\
        `optional`
      </td>

      <td>
        `string` This is the purpose for which QR will be used. This param will have fixed values basis your business type. Please take the value from our integration team.
      </td>

      <td>
        3
      </td>
    </tr>

    <tr>
      <td>
        refUrl\
        `optional`
      </td>

      <td>
        `string` This field can be used to share invoice copy or any other transaction related information/documents to customer for their reference.
      </td>

      <td>
        [https://payu.in/](https://payu.in/)
      </td>
    </tr>

    <tr>
      <td>
        category\
        `optional`
      </td>

      <td>
        `string`  This field is mandatory when refUrl is passed. Use 01 for advertisement & 02 for invoice.
      </td>

      <td>
        01 or 02
      </td>
    </tr>
  </tbody>
</Table>

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
> * The customer details are optional. If not posted, the default value is null. The following rules are to be followed while sending customer details:
>   * Phone number and email address are to be sent in their respective formats.
>   * customerAddress can be up to 100 characters. The first 100 characters will be truncated if the value is more than 100 characters for this parameter.
> * VendorKey should always be unique and different for every new QR generated. The parameter should be alphanumeric & less than or equal to 10 characters.
> * The response sent for QR generation request is JSON encoded and will be a base64 encoded string of the actual QR image, so to obtain the actual QR image, first decode the json encoded response and then convert the base64 encoded string to actual QR image.
> * For every QR generation request, in the response PayU will share back the unique identifier, qrId, embedded in the QR. This reference id is generated based on the vendor key shared in the QR generation request.
> * Map the QR image to this qrId and with respective terminal at which you will use this QR. These details need to be sent to PayU during payment initiation request sent for a particular terminal.

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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        This parameter returns the status of web service call. The status can be any of the following:  

        0 - If web service call failed.\
        1 - If web service call succeeded
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter returns the following message if the offline intent link was generated successfully:\
        `Intent link generated`
      </td>
    </tr>

    <tr>
      <td>
        link
      </td>

      <td>
        This parameter returns the link if the offline intent link is generated successfully.
      </td>
    </tr>
  </tbody>
</Table>

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

* **Amount mismatch**

```Text JSON
{
    "status": "failed",
    "message": "link already exists but amount mismatch with existing link amount",
    "errorCode": "E2030"
}
```

* **Intent Link Already Exists**

```Text JSON
{
  "status": "success",
  "message": "Intent Link already exists",
  "link": "https://secure.payu.in/omni?id=000F"
}
```

* **Already Used Transaction ID**

```Text JSON
{
  "status": "failed",
  "message": "TransactionId already used. Please use a different one.",
  "errorCode": "E2012"
}
```
