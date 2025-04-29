---
title: Get All Payment Links API
excerpt: 'Resource: **payment-links**'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The** Get All Payment Links** API is used to get all the payment links generated for a given date range, and you can specify how many records are to be displayed per page in the response.

HTTP Method: **GET**

**Environment**

|                            |                                           |
| -------------------------- | ----------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payment-links> |
| **Production Environment** | <https://oneapi.payu.in/payment-links>    |

> 📘 Note:
> 
> The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links).

## Request headers

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "mid  \n**mandatory**",
    "0-1": "`String` This contains the merchant identifier.",
    "1-0": "Authorization  \n**mandatory**",
    "1-1": "Bearer `String` This contains the client\\_token. For getting a token, refer to [Get Token API - Payment Links](ref:get-token-api-payment-links) ."
  },
  "cols": 2,
  "rows": 2,
  "align": [
    null,
    null
  ]
}
[/block]


## Query parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "pageOffset",
    "0-1": "The parameter needs to include the page offset in terms of the rows.",
    "0-2": "2",
    "1-0": "pageSize",
    "1-1": "The parameter needs to include the number of rows to be displayed per page in the response.",
    "1-2": "20",
    "2-0": "orderBy",
    "2-1": "This parameter can contain any of the following column names by which the rows in the API response are sorted:  \n**addedOn**",
    "2-2": "addedOn",
    "3-0": "order",
    "3-1": "This parameter can contain any of the following values:  \n  \n- **asc**-The payment links are arranged in ascending order in the API response.\n- **des**-The payment links are arranged in descending order in the API response.",
    "3-2": "asc",
    "4-0": "dateFrom`\n`**mandatory**",
    "4-1": "`String`This parameter must contain the date from which the payment links are required. This must be in \"yyyy-MM-dd\" format.",
    "4-2": "2022-01-22",
    "5-0": "searchText",
    "5-1": "`String` This parameter contains the description of payment link that must be searched for.",
    "5-2": "Insurance Premium Payment",
    "6-0": "dateTo`\n`**mandatory**",
    "6-1": "`String`This parameter must contain the date to which the payment links are required. This must be in \"yyyy-MM-dd\" format.",
    "6-2": "2022-01-28",
    "7-0": "active",
    "7-1": "`String`This parameter can include any of the following status as the value:  \n    - active  \n  \n- inactive\n- expired",
    "7-2": "active"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample request

```curl
curl --location -g --request GET 'https://uatoneapi.payu.in/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22' \
--header 'merchantId: {{merchantId}}' \
--header 'Authorization: Bearer {{access_token}}'
```
```python
import http.client

conn = http.client.HTTPSConnection("{{stagingurl}}")
payload = ''
headers = {
  'merchantId': '{{merchantId}}',
  'Authorization': 'Bearer {{access_token}}'
}
conn.request("GET", "/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
```ruby
require "uri"
require "net/http"

url = URI("{{stagingurl}}/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["merchantId"] = "{{merchantId}}"
request["Authorization"] = "Bearer {{access_token}}"

response = http.request(request)
puts response.read_body
```
```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("{{stagingurl}}/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22")
  .method("GET", null)
  .addHeader("merchantId", "{{merchantId}}")
  .addHeader("Authorization", "Bearer {{access_token}}")
  .build();
Response response = client.newCall(request).execute();
```

## Sample response

```
{
  "status": 0,
  "message": null,
  "result": {
    "pageSize": 20,
    "pages": 1,
    "rows": 1,
    "pageOffset": 0,
    "paymentLinksList": [
      {
        "invoiceNumber": "INV8446471886220",
        "description": "paymentLink for testing",
        "createDate": "2022-03-21T14:53:53.000+0530",
        "paymentLinkURL": "http://pp72.pmny.in/4IwlctBtwp2V",
        "customerName": null,
        "amount": 2,
        "active": true,
        "expiry": "2022-03-21T16:12:12.000+0530",
        "isAmountFilledByCustomer": false,
        "status": "active",
        "isScheduled": 0,
        "reminderCount": 0
      }
    ]
  },
  "errorCode": null,
  "guid": null
}
```