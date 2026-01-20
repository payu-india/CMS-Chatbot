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

| Environment | URL                                                                                            |
| :---------- | :--------------------------------------------------------------------------------------------- |
| Production  | [https://info.payu.in/merchant/postservice.php](https://info.payu.in/merchant/postservice.php) |

## Request parameters

<HTMLBlock>{`
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
        Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        key
      </td>

      <td>
        This parameter must contain the merchant key provided by PayU. For more information, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Access Production Key and Salt</a>.
      </td>

      <td>
        Your Test Key
      </td>
    </tr>

    <tr>
      <td>
        command
      </td>

      <td>
        This parameter must have the API command name.
      </td>

      <td>
        expire_insta_account
      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
        This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash as follows:

        sha512(key|command|var1|salt)
      </td>

      <td>
        c24ee06c7cf40314ede424 b1fcc2b97a12f97a7d3dd2 06876eef16660eb09fd374 fd82861f66d8152e
      </td>
    </tr>

    <tr>
      <td>
        var1
      </td>

      <td>
        This parameter must contain the fields in a JSON format. For more information, refer to <a href="https://docs.payu.in/reference/insta-deactivate-vpa-api#var1-json-fields-description">var1 JSON fields description</a> section..
      </td>

      <td>
        Refer to <a href="https://docs.payu.in/reference/insta-deactivate-vpa-api#var1-json-fields-description">var1 JSON fields description</a> section..
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>

### var1 JSON fields description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Key
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
        merchantVpa
        `mandatory`
      </td>

      <td>
        Merchant's VPA is the VPA which needs to be deactivated/blocked permanently
      </td>

      <td>
        smsplustestqr789@indus
      </td>
    </tr>

    <tr>
      <td>
        instaProduct  
        `mandatory`
      </td>

      <td>
        QR generation flag. Fixed value - qr
      </td>

      <td>
        qr
      </td>
    </tr>

    <tr>
      <td>
        remarks  
        `optional`
      </td>

      <td>
        This can be used for audit trail later
      </td>

      <td>
        Account closed
      </td>
    </tr>
  </tbody>
</Table>

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

        0 - If web service call failed.  
        1 - If web service call succeeded
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        The following message is displayed to indicate that the VPA is permanently blocked now, and the QR cannot be scanned to make any UPI transactions.  
        `merchantVpa deactivated`
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

```Text JSON
{
  "status": "1",
  "msg": "merchantVpa deactivated"
}
```
