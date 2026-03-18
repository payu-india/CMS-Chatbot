---
title: Get Token API - Bank Verification
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
---
title: Get Token API - Bank Verification
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

The **Get Token** API returns the authentication token generated using the client ID and client secret where, `grant_type` is **client_credentials** and `scope` is **verify_bank_account**. This must be used along with [Bank Verification API](ref:bank-verification-api).

<Accordion title="Environment" icon="fa-info">
  <span id="environment" />

  | Environment | URL                                                                                  |
  | ----------- | ------------------------------------------------------------------------------------ |
  | Test (UAT)  | [https://uat-accounts.payu.in/oauth/token](https://uat-accounts.payu.in/oauth/token) |
  | Production  | [https://accounts.payu.in/oauth/token](https://accounts.payu.in/oauth/token)         |
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  <span id="request-parameters" />

  | Parameter                                  | Details                                                                                                                                           |
  | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
  | client\_id<br /><code>mandatory</code>     | String: This field is the Client ID that was provided by PayU while onboarding.                                                                   |
  | client\_secret<br /><code>mandatory</code> | String: This field is the Client secret that was provided by PayU while onboarding.                                                               |
  | grant\_type<br /><code>mandatory</code>    | String: This parameter contains a constant value used to get the access token. For Bank Verification API, it is <code>client\_credentials</code>. |
  | scope<br /><code>mandatory</code>          | String: This parameter will vary based on the use case. For Bank Verification API, it is <code>verify\_bank\_account</code>.                      |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  <span id="sample-request" />

  ```curl
  curl --request POST \
       --url https://uat-accounts.payu.in/oauth/token \
       --header 'accept: application/json' \
       --header 'content-type: application/x-www-form-urlencoded' \
       --data grant_type=client_credentials \
       --data scope=verify_bank_account \
       --data 'client_id=<client_id>' \
       --data 'client_secret=<client_secret>'
  ```
  ```python
  import requests

  url = "https://uat-accounts.payu.in/oauth/token"

  headers = {
      "accept": "application/json",
      "content-type": "application/x-www-form-urlencoded"
  }

  data = {
      "grant_type": "client_credentials",
      "scope": "verify_bank_account",
      "client_id": "<client_id>",
      "client_secret": "<client_secret>"
  }

  try:
      response = requests.post(url, headers=headers, data=data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```javascript
  async function makeRequest() {
      const url = "https://uat-accounts.payu.in/oauth/token";
      
      const headers = {
          "accept": "application/json",
          "content-type": "application/x-www-form-urlencoded"
      };

      const formData = new URLSearchParams({
          "grant_type": "client_credentials",
          "scope": "verify_bank_account",
          "client_id": "<client_id>",
          "client_secret": "<client_secret>"
      });

      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: formData
          });
          
          const responseText = await response.text();
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
      } catch (error) {
          console.error(`Error: ${error.message}`);
      }
  }

  makeRequest();
  ```
  ```java
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.time.Duration;

  public class ApiRequest {
      public static void main(String[] args) {
          try {
              String url = "https://uat-accounts.payu.in/oauth/token";
              
              String formData = "grant_type=client_credentials&scope=verify_bank_account&client_id=<client_id>&client_secret=<client_secret>";
              
              HttpClient client = HttpClient.newBuilder()
                  .connectTimeout(Duration.ofSeconds(10))
                  .build();

              HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("accept", "application/json")
                  .header("content-type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formData))
                  .build();

              HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
              
              System.out.println("Status Code: " + response.statusCode());
              System.out.println("Response: " + response.body());
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          try
          {
              string url = "https://uat-accounts.payu.in/oauth/token";
              
              client.DefaultRequestHeaders.Add("accept", "application/json");

              var formData = new List<KeyValuePair<string, string>>
              {
                  new KeyValuePair<string, string>("grant_type", "client_credentials"),
                  new KeyValuePair<string, string>("scope", "verify_bank_account"),
                  new KeyValuePair<string, string>("client_id", "<client_id>"),
                  new KeyValuePair<string, string>("client_secret", "<client_secret>")
              };

              var formContent = new FormUrlEncodedContent(formData);
              HttpResponseMessage response = await client.PostAsync(url, formContent);
              string responseBody = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseBody}");
          }
          catch (HttpRequestException ex)
          {
              Console.WriteLine($"Error: {ex.Message}");
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://uat-accounts.payu.in/oauth/token";

  $headers = [
      "accept: application/json",
      "content-type: application/x-www-form-urlencoded"
  ];

  $postData = [
      "grant_type" => "client_credentials",
      "scope" => "verify_bank_account",
      "client_id" => "<client_id>",
      "client_secret" => "<client_secret>"
  ];

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postData));
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  if (curl_errno($ch)) {
      echo "Error: " . curl_error($ch) . "\n";
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);
  ?>
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-table">
  <span id="response-parameters" />

  | Parameter     | Description                                              |
  | ------------- | -------------------------------------------------------- |
  | access\_token | The access token to be used in Partner Integration APIs. |
  | token\_type   | The token type of the access token.                      |
  | expires\_in   | The expiry time in seconds of the access token.          |
  | scope         | The scope of the access token.                           |
  | created\_at   | The UNIX time stamp when the access token was created.   |

  <Callout icon="📘" theme="info">
    **Note:** The expiry period of the token generated using this API is configurable by you (partner). The expiry period (in seconds) is returned in **expires\_in**. For example, **7200** means the token is valid for 7200 seconds:

    ```json
    {
      "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
      "token_type": "Bearer",
      "expires_in": 7200,
      "scope": "verify_bank_account",
      "created_at": 1595411399
    }
    ```
  </Callout>
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  <span id="sample-response" />

  ```json
  {
    "access_token": "82c38b64e072f3d64da6e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7",
    "token_type": "Bearer",
    "expires_in": 7200,
    "scope": "verify_bank_account",
    "created_at": 1595411399
  }
  ```
</Accordion>
