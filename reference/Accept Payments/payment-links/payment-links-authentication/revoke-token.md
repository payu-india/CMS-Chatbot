---
api:
  file: pl-test-oas.yaml
  operationId: RevokeTokenAPI
hidden: true
link:
  new_tab: false
metadata:
  title: Revoke a Token
next:
  description: Explore related information and resources.
---
Invalidate a Bearer token before its natural expiry. Use this endpoint when rotating credentials or if you suspect a token has been exposed.<br />

The revoked token becomes invalid immediately. After revoking, generate a newtoken via the Get A Access Token API.

***

## Environments

| Environment    | Base URL                       |
| :------------- | :----------------------------- |
| **Test**       | `https://uat-accounts.payu.in` |
| **Production** | `https://accounts.payu.in`     |

<Callout icon="📘" theme="info">
  ### **When Should I Revoke a Token?**

  Revoke your token only when you need to invalidate a token early. For example, on user logout, credential rotation, or if a token may have been exposed.
</Callout>

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --location 'https://uat-accounts.payu.in/oauth/revoke' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      -d 'client_id={{client_id}}' \
      -d 'client_secret={{client_secret}}' \
      -d 'token={{access_token}}'
    ```
    ```python
    import requests

    url = "https://uat-accounts.payu.in/oauth/revoke"

    payload = {
        "client_id":     "{{client_id}}",
        "client_secret": "{{client_secret}}",
        "token":         "{{access_token}}"
    }

    response = requests.post(url, data=payload)
    # A 200 with an empty body means the token was successfully revoked
    print(response.status_code)
    ```
    ```javascript
    const axios = require('axios');
    const qs = require('querystring');

    const response = await axios.post(
      'https://uat-accounts.payu.in/oauth/revoke',
      qs.stringify({
        client_id:     '{{client_id}}',
        client_secret: '{{client_secret}}',
        token:         '{{access_token}}'
      }),
      { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
    );

    // 200 with empty body = success
    console.log(response.status);
    ```
    ```csharp
    using var client = new HttpClient();

    var request = new HttpRequestMessage(
        HttpMethod.Post,
        "https://uat-accounts.payu.in/oauth/revoke"
    );

    request.Content = new FormUrlEncodedContent(new[]
    {
        new KeyValuePair<string, string>("client_id", "{{client_id}}"),
        new KeyValuePair<string, string>("client_secret", "{{client_secret}}"),
        new KeyValuePair<string, string>("token", "{{access_token}}")
    });

    var response = await client.SendAsync(request);
    var responseBody = await response.Content.ReadAsStringAsync();
    ```
    ```java
    import java.net.URI;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;

    HttpClient client = HttpClient.newHttpClient();

    String formData =
        "client_id={{client_id}}" +
        "&client_secret={{client_secret}}" +
        "&token={{access_token}}";

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://uat-accounts.payu.in/oauth/revoke"))
        .header("Content-Type", "application/x-www-form-urlencoded")
        .POST(HttpRequest.BodyPublishers.ofString(formData))
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
        CURLOPT_URL => 'https://uat-accounts.payu.in/oauth/revoke',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/x-www-form-urlencoded'
        ],
        CURLOPT_POSTFIELDS => [
            'client_id' => '{{client_id}}',
            'client_secret' => '{{client_secret}}',
            'token' => '{{access_token}}'
        ]
    ]);

    $response = curl_exec($curl);

    curl_close($curl);

    echo $response;
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Form Data](https://docs.payu.in/reference/revoke-token#body-params) section for a full description of all request parameters and use cases.
  </Tab>
</Tabs>

***

## Sample Response

<Tabs>
  <Tab title="Success and Error Response">
    ```json Success Response
    HTTP/1.1 200 OK
    Content-Length: 0
    ```
    ```json Error Response - Invalid client credentials
    {
      "error": "invalid_client",
      "error_description": "Client authentication failed due to unknown client, no client authentication included, or unsupported authentication method."
    }
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Responses](https://docs.payu.in/v3.0/reference/revoke-token#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
