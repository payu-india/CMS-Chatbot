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
The** Expire Intent Link** API is used to expire UPI Intent link.

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
    "0-1": "`string` This parameter must include the merchant key that was provided by PayU",
    "0-2": "vDy3i7",
    "1-0": "command  \n`mandatory`",
    "1-1": "`string` The parameter must contain the name of the web service. For this API, `expire_intent_link` must be posted.",
    "1-2": "expire_intent_link",
    "2-0": "hash  \n`mandatory`",
    "2-1": "`string` This parameter must contain the hash value to be calculated at your end. The string used for calculating the hash is mentioned below:  \nsha512(key|command|var1|salt)  \nsha512 is the encryption method used here.",
    "2-2": "ajh84babvav",
    "3-0": "var1  \n`mandatory`",
    "3-1": "`JSON` This parameter will include the transactionIds in an array format (comma separated).  \n**Note**: Only 100 transactions can be processed for a request,",
    "3-2": "{\"transactionIds\":\"intent210,intent211\"}"
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "status",
    "0-1": "This parameter returns the status of web service call. The status can be any of the following:  \n  \n0 - If web service call failed  \n1 - If web service call succeeded",
    "1-0": "msg",
    "1-1": "This parameter returns the following message if the offline intent link was generated successfully:  \n`Intent link generated`",
    "2-0": "details",
    "2-1": "This parameter returns the message in following JSON format if the request was successful:  \n  \ntxnId: The transaction ID of the offline intent link.  \nstatus: The status can be any of the following based on whether intent link was expired:  \n1: Successfully link got expired  \n0: Link had got already expired or not active intent link.  \nmsg: Any of the following message is displayed based on the link was expired by this API or no active link.  \nIntent link has expired  \nNo active intent link against this transaction ID"
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