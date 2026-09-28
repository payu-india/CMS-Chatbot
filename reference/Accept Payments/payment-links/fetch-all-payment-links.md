---
api:
  file: pl-test-oas.yaml
  operationId: FetchAllPaymentLinksAPI
hidden: true
metadata:
  title: Fetch all Payment Links | Payment Links API
next:
  description: Explore related information and resources.
---
Use this endpoint to retrieve a paginated list of all payment links for your merchant account, sorted by creation date (newest first). Use the `status` filter to narrowresults to active, expired, or cancelled links.

***

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /payment-links
  </Card>
</Cards>

***

## Environments

| Environment                | URL                         |
| :------------------------- | :-------------------------- |
| **Test Environment**       | `https://uatoneapi.payu.in` |
| **Production Environment** | `https://oneapi.payu.in`    |

<Callout icon="🔑" theme="default">
  ### **Get your Bearer token before calling this endpoint**

  This API uses OAuth 2.0 — not the hash-based auth used by other PayU APIs.

  1. Call the <Anchor target="_blank" href="https://docs.payu.in/reference/generate-access-token">Generate an Access Token</Anchor> token with `grant_type=client_credentials` and `scope=create_payment_links`
  2. Copy the `access_token` from the response
  3. Pass it as `Authorization: Bearer {access_token}` in every request

  <Columns layout="fixed">
    <Column>
      **Token Expiry:** Check `expires_in` in the token response and refresh before it lapses.
    </Column>
  </Columns>
</Callout>

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location -g 'https://uatoneapi.payu.in/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22' \
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
    ```csharp
    using var client = new HttpClient();

    var request = new HttpRequestMessage(
        HttpMethod.Get,
        "https://uatoneapi.payu.in/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22"
    );

    request.Headers.Add("merchantId", "{{merchantId}}");
    request.Headers.Add("Authorization", "Bearer {{access_token}}");

    var response = await client.SendAsync(request);
    var responseBody = await response.Content.ReadAsStringAsync();
    ```
    ```javascript
    const response = await fetch(
      "https://uatoneapi.payu.in/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22",
      {
        method: "GET",
        headers: {
          "merchantId": "{{merchantId}}",
          "Authorization": "Bearer {{access_token}}"
        }
      }
    );

    const responseBody = await response.text();
    console.log(responseBody);
    ```
    ```php
    <?php

    $curl = curl_init();

    curl_setopt_array($curl, [
        CURLOPT_URL => 'https://uatoneapi.payu.in/payment-links?pageSize=20&pageOffset=0&orderBy=amount&order=desc&dateFrom=2022-03-21&dateTo=2022-03-22',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CUSTOMREQUEST => 'GET',
        CURLOPT_HTTPHEADER => [
            'merchantId: {{merchantId}}',
            'Authorization: Bearer {{access_token}}'
        ]
    ]);

    $response = curl_exec($curl);

    curl_close($curl);

    echo $response;
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Query Params](https://docs.payu.in/reference/fetch-all-payment-links#query-params) and [Headers](https://docs.payu.in/reference/fetch-all-payment-links#header-params) sections for a full description of all request parameters and use cases.
  </Tab>
</Tabs>

***

## Sample Response

<Tabs>
  <Tab title="Success and Error Response">
    ```json Success
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
    ```json Error
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Response](https://docs.payu.in/v3.0/reference/fetchallpaymentlinksapi#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
