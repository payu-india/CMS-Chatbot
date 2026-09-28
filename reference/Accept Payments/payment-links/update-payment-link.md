---
api:
  file: pl-test-oas.yaml
  operationId: UpdatePaymentLinkAPI
hidden: true
metadata:
  title: Update a Payment Link | Payment Links API
next:
  description: Explore related information and resources.
---
Use this endpoint to modify the configuration of an existing active payment link.<br />

Only send the fields you want to change. Your omitted fields retain their current values.

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Restrictions**

  You cannot:

  - Update a cancelled link (`active: false`).
  - Update a link that has been fully paid.
  - Reduce `subAmount` below the amount already collected on a partial payment link.
</Callout>

***

<Cards>
  <Card title="Method">
    PUT
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

<Callout icon="🔑" theme="default">
  ### **Get your Bearer token before calling this endpoint**

  This API uses OAuth 2.0 authentication.

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
    curl -X POST "https://uatoneapi.payu.in/payment-links" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "merchantId: YOUR_MERCHANT_ID" \
      -H "Content-Type: application/json" \
      -d '{
      "subAmount": 2000,
      "description": "Update link testing",
      "expiryDate": "2026-11-30 23:59:59",
      "isPartialPaymentAllowed": true,
      "minAmountForCustomer": 500,
      "viaEmail": true,
      "viaSms": true,
      "viaWhatsapp": true
    }'
    ```
    ```csharp
    using System.Net.Http;
    using System.Text;

    using var client = new HttpClient();

    var request = new HttpRequestMessage(
        HttpMethod.Post,
        "https://uatoneapi.payu.in/payment-links"
    );

    request.Headers.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
    request.Headers.Add("merchantId", "YOUR_MERCHANT_ID");

    request.Content = new StringContent(
        """
        {
          "subAmount": 2000,
          "description": "Update link testing",
          "expiryDate": "2026-11-30 23:59:59",
          "isPartialPaymentAllowed": true,
          "minAmountForCustomer": 500,
          "viaEmail": true,
          "viaSms": true,
          "viaWhatsapp": true
        }
        """,
        Encoding.UTF8,
        "application/json"
    );

    var response = await client.SendAsync(request);
    var responseBody = await response.Content.ReadAsStringAsync();

    Console.WriteLine(responseBody);
    ```
    ```python
    import requests

    url = "https://uatoneapi.payu.in/payment-links"

    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "merchantId": "YOUR_MERCHANT_ID",
        "Content-Type": "application/json"
    }

    payload = {
        "subAmount": 2000,
        "description": "Update link testing",
        "expiryDate": "2026-11-30 23:59:59",
        "isPartialPaymentAllowed": True,
        "minAmountForCustomer": 500,
        "viaEmail": True,
        "viaSms": True,
        "viaWhatsapp": True
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.text)
    ```
    ```javascript
    const response = await fetch(
      "https://uatoneapi.payu.in/payment-links",
      {
        method: "POST",
        headers: {
          "Authorization": "Bearer YOUR_ACCESS_TOKEN",
          "merchantId": "YOUR_MERCHANT_ID",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          subAmount: 2000,
          description: "Update link testing",
          expiryDate: "2026-11-30 23:59:59",
          isPartialPaymentAllowed: true,
          minAmountForCustomer: 500,
          viaEmail: true,
          viaSms: true,
          viaWhatsapp: true
        })
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

    String jsonBody = """
    {
      "subAmount": 2000,
      "description": "Update link testing",
      "expiryDate": "2026-11-30 23:59:59",
      "isPartialPaymentAllowed": true,
      "minAmountForCustomer": 500,
      "viaEmail": true,
      "viaSms": true,
      "viaWhatsapp": true
    }
    """;

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://uatoneapi.payu.in/payment-links"))
        .header("Authorization", "Bearer YOUR_ACCESS_TOKEN")
        .header("merchantId", "YOUR_MERCHANT_ID")
        .header("Content-Type", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
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
        CURLOPT_URL => 'https://uatoneapi.payu.in/payment-links',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer YOUR_ACCESS_TOKEN',
            'merchantId: YOUR_MERCHANT_ID',
            'Content-Type: application/json'
        ],
        CURLOPT_POSTFIELDS => json_encode([
            'subAmount' => 2000,
            'description' => 'Update link testing',
            'expiryDate' => '2026-11-30 23:59:59',
            'isPartialPaymentAllowed' => true,
            'minAmountForCustomer' => 500,
            'viaEmail' => true,
            'viaSms' => true,
            'viaWhatsapp' => true
        ])
    ]);

    $response = curl_exec($curl);

    curl_close($curl);

    echo $response;
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Path Params,](https://docs.payu.in/reference/update-payment-link#path-params) [Headers](https://docs.payu.in/reference/update-payment-link#header-params), and [Body Params](https://docs.payu.in/reference/update-payment-link#body-params) sections for a full description of all request parameters and use cases.
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
    Refer to the [Response](https://docs.payu.in/reference/update-payment-link#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
