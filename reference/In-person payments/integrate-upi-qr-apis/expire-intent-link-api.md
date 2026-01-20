---
title: Expire Intent Link API
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
The **Expire Intent Link** API is used to expire UPI Intent link.

#### Environment

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
        `string` This parameter must include the merchant key that was provided by PayU
      </td>

      <td>
        vDy3i7
      </td>
    </tr>

    <tr>
      <td>
        command  
        `mandatory`
      </td>

      <td>
        `string` The parameter must contain the name of the web service. For this API, `expire_intent_link` must be posted.
      </td>

      <td>
        expire_intent_link
      </td>
    </tr>

    <tr>
      <td>
        hash  
        `mandatory`
      </td>

      <td>
        `string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  
        sha512(key|command|var1|salt)  
        sha512 is the encryption method used here.
      </td>

      <td>
        ajh84babvav
      </td>
    </tr>

    <tr>
      <td>
        var1  
        `mandatory`
      </td>

      <td>
        `JSON` This parameter will include the transactionIds in an array format (comma separated).

        * *Note**: Only 100 transactions can be processed for a request,
      </td>

      <td>
        \{"transactionIds":"intent210,intent211"}
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```Text cURL
curl --location -g --request POST 'https://info.payu.in/merchant/postservice.php?command=expire_intent_link&key=vDy3i7&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1={"transactionIds":"intent210,intent211"}' \
--data-urlencode 'command=Mandatory' \
--data-urlencode 'key=Mandatory' \
--data-urlencode 'hash=Mandatory' \
--data-urlencode 'var1=Mandatory'
```
```Text Python
import http.client

conn = http.client.HTTPSConnection("info.payu.in")
payload = 'command=Mandatory&key=Mandatory&hash=Mandatory&var1=Mandatory'
headers = {}
conn.request("POST", "/merchant/postservice.php?command=expire_intent_link&key=vDy3i7&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionIds%22:%22intent210,intent211%22%7D", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```Text php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://info.payu.in/merchant/postservice.php?command=expire_intent_link&key=vDy3i7&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1=%7B%22transactionIds%22:%22intent210,intent211%22%7D',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'command=Mandatory&key=Mandatory&hash=Mandatory&var1=Mandatory',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```
```Text Ruby
require "uri"
require "net/http"

url = URI("https://info.payu.in/merchant/postservice.php?command=expire_intent_link&key=vDy3i7&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1={\"transactionIds\":\"intent210,intent211\"}")

https = Net::HTTP.new(url.host, url.port)
https.use_ssl = true

request = Net::HTTP::Post.new(url)
request.body = "command=Mandatory&key=Mandatory&hash=Mandatory&var1=Mandatory"

response = https.request(request)
puts response.read_body
```
```Text JAVA
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "command=Mandatory&key=Mandatory&hash=Mandatory&var1=Mandatory");
Request request = new Request.Builder()
  .url("https://info.payu.in/merchant/postservice.php?command=expire_intent_link&key=vDy3i7&hash=c8aa5dc5f2139936227bc1daf21dd2cad79fc32a623b66098667e6ebfc0f7aec0005f4e19e4296c79cf1f92077db60a20635a572342f5377972c469137db6bf1&var1={\"transactionIds\":\"intent210,intent211\"}")
  .method("POST", body)
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

        0 - If web service call failed  
        1 - If web service call succeeded
      </td>
    </tr>

    <tr>
      <td>
        msg
      </td>

      <td>
        This parameter returns the following message if the offline intent link was generated successfully:  
        `Intent link generated`
      </td>
    </tr>

    <tr>
      <td>
        details
      </td>

      <td>
        This parameter returns the message in following JSON format if the request was successful:

        txnId: The transaction ID of the offline intent link.  
        status: The status can be any of the following based on whether intent link was expired:  
        1: Successfully link got expired  
        0: Link had got already expired or not active intent link.  
        msg: Any of the following message is displayed based on the link was expired by this API or no active link.  
        Intent link has expired  
        No active intent link against this transaction ID
      </td>
    </tr>
  </tbody>
</Table>

## Sample response

```Text JSON
{
  "status": "success",
  "message": "processed",
  "details": [
    {
      "txnId": "intent210",
      "status": 0,
      "msg": "No active Intent Link against this txnid"
    },
    {
      "txnId": "intent211",
      "status": 1,
      "msg": "Intent Link expired"
    }
  ]
}
```
