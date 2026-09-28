---
api:
  file: pl-test-oas.yaml
  operationId: CancelPaymentLinkAPI
hidden: true
metadata:
  title: Cancel a Payment Link | Payment Links API
next:
  description: Explore related information and resources.
---
Use this endpoint to deactivate an existing payment link so it can no longer accept payments. You should pass the `active` parameter value as `false` permanently to cancel a link.

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Restrictions**

  You cannot:

  - Reactivate a cancelled link
  - Cancel a link that has already been fully paid
</Callout>

***

<Cards>
  <Card title="Method">
    Delete
  </Card>

  <Card title="Endpoint">
    /payment-links/{invoiceNumber}
  </Card>
</Cards>

***

## Environments

| Environment                | URL                         |
| :------------------------- | :-------------------------- |
| **Test Environment**       | `https://uatoneapi.payu.in` |
| **Production Environment** | `https://oneapi.payu.in`    |

***

<PLbearertoken />

<br />

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location --request DELETE 'https://uatoneapi.payu.in/payment-links/{{invoice_number}}' \
      --header 'Authorization: Bearer {{access_token}}' \
      --header 'merchantId: {{merchantId}}' \
      --header 'Accept: application/json'
    ```
    ```csharp
    using var client = new HttpClient();

    var request = new HttpRequestMessage(
        HttpMethod.Delete,
        "https://uatoneapi.payu.in/payment-links/{{invoice_number}}"
    );

    request.Headers.Add("Authorization", "Bearer {{access_token}}");
    request.Headers.Add("merchantId", "{{merchantId}}");
    request.Headers.Add("Accept", "application/json");

    var response = await client.SendAsync(request);
    var responseBody = await response.Content.ReadAsStringAsync();

    Console.WriteLine(responseBody);
    ```
    ```python
    import requests

    url = "https://uatoneapi.payu.in/payment-links/{{invoice_number}}"

    headers = {
        "Authorization": "Bearer {{access_token}}",
        "merchantId": "{{merchantId}}",
        "Accept": "application/json"
    }

    response = requests.delete(url, headers=headers)

    print(response.text)
    ```
    ```javascript
    const response = await fetch(
      "https://uatoneapi.payu.in/payment-links/{{invoice_number}}",
      {
        method: "DELETE",
        headers: {
          "Authorization": "Bearer {{access_token}}",
          "merchantId": "{{merchantId}}",
          "Accept": "application/json"
        }
      }
    );

    const responseBody = await response.text();

    console.log(responseBody);
    ```
    ```java
    import java.net.URI;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create(
            "https://uatoneapi.payu.in/payment-links/{{invoice_number}}"
        ))
        .header("Authorization", "Bearer {{access_token}}")
        .header("merchantId", "{{merchantId}}")
        .header("Accept", "application/json")
        .DELETE()
        .build();

    HttpResponse<String> response = client.send(
        request,
        HttpResponse.BodyHandlers.ofString()
    );

    System.out.println(response.body());
    ```
    ```php
    <?php

    $curl = curl_init();

    curl_setopt_array($curl, [
        CURLOPT_URL => 'https://uatoneapi.payu.in/payment-links/{{invoice_number}}',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CUSTOMREQUEST => 'DELETE',
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer {{access_token}}',
            'merchantId: {{merchantId}}',
            'Accept: application/json'
        ]
    ]);

    $response = curl_exec($curl);

    curl_close($curl);

    echo $response;
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Path Params](https://docs.payu.in/reference/cancel-payment-link#path-params) and [Headers](https://docs.payu.in/reference/cancel-payment-link#header-params) sections for a full description of all parameters and use cases.
  </Tab>
</Tabs>

***

## Sample Response

<Tabs>
  <Tab title="Success and Error Response">
    ```json Success Respone
    {
      "status": 0,
      "message": "string",
      "result": {},
      "errorCode": 170,
      "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
    }
    ```
    ```json Error Response
    {
      "status": -1,
      "message": "expiry cannot be less than the current date",
      "result": null,
      "errorCode": null,
      "guid": null
    }
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Response](https://docs.payu.in/reference/cancel-payment-link#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
