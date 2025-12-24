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

|                            |                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in/payment-links](https://uatoneapi.payu.in/payment-links)> |
| **Production Environment** | \<[https://oneapi.payu.in/payment-links](https://oneapi.payu.in/payment-links)>       |

<Callout icon="📘" theme="info">
  **Note**: The access token with the scope as **read_payment_links** is required on the header. For more information on getting the access token, refer to [Get Access Token](ref:get-token-api-for-payment-links).
</Callout>

## Request headers

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mid<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This contains the merchant identifier.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Authorization<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Bearer <code>String</code> This contains the client_token. For getting a token, refer to <a href="https://docs.payu.in/reference/get-token-api-for-payment-links">Get Access Token API</a> .</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Query parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameters</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pageOffset</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The parameter needs to include the page offset in terms of the rows.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>pageSize</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The parameter needs to include the number of rows to be displayed per page in the response.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>20</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderBy</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter can contain any of the following column names by which the rows in the API response are sorted:<br><strong>addedOn</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>addedOn</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>order</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter can contain any of the following values:  </p>
<ul>
<li><strong>asc</strong>-The payment links are arranged in ascending order in the API response.</li>
<li><strong>des</strong>-The payment links are arranged in descending order in the API response.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>asc</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>dateFrom<code> </code><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the date from which the payment links are required. This must be in &quot;yyyy-MM-dd&quot; format.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-01-22</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>searchText</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This parameter contains the description of payment link that must be searched for.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Insurance Premium Payment</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>dateTo<code> </code><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter must contain the date to which the payment links are required. This must be in &quot;yyyy-MM-dd&quot; format.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-01-28</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>active</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code>This parameter can include any of the following status as the value:<br>    - active  </p>
<ul>
<li>inactive</li>
<li>expired</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>active</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

```json
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
