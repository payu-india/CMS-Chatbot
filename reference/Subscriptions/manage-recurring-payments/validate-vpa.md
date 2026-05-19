---
api:
  file: validate-vpa-api.yaml
  operationId: validateVPA
hidden: true
---
Use this API to check whether a VPA is valid. For UPI Autopay or recurring payments, pass `var2` with a JSON string containing `validateAutoPayVPA` as `1`.

<Callout icon="👍" theme="okay">
  **Handy Tips**

  You should poll this API after a customer enters a VPA on the merchant page to check for its validation. If VPA is valid only then, the second call should be made.
</Callout>

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  <Validate_VPA />
</Accordion>

### Sample Request - Recurring Payments

Below is the validate VPA sample code for recurring payments.

<Accordion title="Request Payload" icon="fa-code">
  ```curl
    curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
        -H "accept: application/json" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "key=JP***g" \
        -d "command=validateVPA" \
        -d "var1=9999999999@upi" \
        -d "var2={\"validateAutoPayVPA\":\"1\"}" \
        -d "hash=YOUR_HASH_VALUE"
  ```
  ```python
  import requests
  import json

  url = "https://test.payu.in/merchant/postservice"

  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  var2_json = json.dumps({"validateAutoPayVPA": "1"})

  data = {
      "key":     "JP***g",
      "command": "validateVPA",
      "var1":    "9999999999@upi",
      "var2":    var2_json,
      "hash":    "YOUR_HASH_VALUE"
  }

  response = requests.post(url, headers=headers, data=data, params={"form": "2"})

  print("Status Code:", response.status_code)
  print("Response:", response.json())
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class ValidateAutoPayVPA {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://test.payu.in/merchant/postservice?form=2";

          String var2Json = "{\"validateAutoPayVPA\":\"1\"}";

          Map<String, String> params = new HashMap<>();
          params.put("key",     "JP***g");
          params.put("command", "validateVPA");
          params.put("var1",    "9999999999@upi");
          params.put("var2",    var2Json);
          params.put("hash",    "YOUR_HASH_VALUE");

          String formData = params.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                      + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));

          HttpClient client = HttpClient.newHttpClient();

          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("accept", "application/json")
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formData))
              .build();

          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: "     + response.body());
      }
  }
  ```
  ```javascript
  const axios = require('axios');
    const qs = require('qs');

    const url = 'https://test.payu.in/merchant/postservice?form=2';

    const var2Json = JSON.stringify({ validateAutoPayVPA: '1' });

    const data = {
        key: 'JP***g',
        command: 'validateVPA',
        var1: '9999999999@upi',
        var2: var2Json,
        hash: 'YOUR_HASH_VALUE'
    };

    const config = {
        headers: {
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };

    axios.post(url, qs.stringify(data), config)
        .then(response => {
            console.log('Status Code:', response.status);
            console.log('Response:', response.data);
        })
        .catch(error => {
            console.error('Error:', error.response ? error.response.data : error.message);
        });
  ```
  ```php
  <?php

  $url = "https://test.payu.in/merchant/postservice?form=2";

  $var2Json = json_encode(array('validateAutoPayVPA' => '1'));

  $data = array(
      'key' => 'JP***g',
      'command' => 'validateVPA',
      'var1' => '9999999999@upi',
      'var2' => $var2Json,
      'hash' => 'YOUR_HASH_VALUE'
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'accept: application/json',
      'Content-Type: application/x-www-form-urlencoded'
  ));

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  echo "Status Code: " . $httpCode . "\n";
  echo "Response: " . $response . "\n";

  $jsonResponse = json_decode($response, true);
  print_r($jsonResponse);
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common;
  use JSON;

  my $url = "https://test.payu.in/merchant/postservice?form=2";

  my $var2_json = encode_json({ validateAutoPayVPA => '1' });

  my %data = (
      key     => 'JP***g',
      command => 'validateVPA',
      var1    => '9999999999@upi',
      var2    => $var2_json,
      hash    => 'YOUR_HASH_VALUE'
  );

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my $response = $ua->post($url,
      Content_Type => 'application/x-www-form-urlencoded',
      Content => \%data
  );

  if ($response->is_success) {
      print "Status Code: " . $response->code . "\n";
      print "Response: " . $response->decoded_content . "\n";
  } else {
      print "Error: " . $response->status_line . "\n";
  }
  ```
</Accordion>

<Callout icon="👍" theme="okay">
  **Request Parameter Description**

  Refer to the [Form Data](https://docs.payu.in/reference/validate-vpa#body-params) section for request parameters, their descriptions and examples.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
    {
      "status":"SUCCESS",
      "vpa":"9999999999@upi",
      "isVPAValid":1,
      "isAutoPayVPAValid":1,
      "isAutoPayBankValid":"NA",
      "payerAccountName":"ABC"
    }
  ```
  ```json Error Response
  {
    "status":"SUCCESS",
    "vpa":"abc@upi",
    "isVPAValid":0,
    "payerAccountName":"NA"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  **Handy Tips**

  * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
  * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
  * Ignore the **isAutoPayBankValid** parameter in the response.
</Callout>

<Callout icon="👍" theme="okay">
  **Response Parameter Description**

  Refer to the [Response](https://docs.payu.in/reference/validate-vpa#response-schemas) section for response parameters and their descriptions.
</Callout>

## Generate Hash

<HTMLBlock>{`
<p>Use this button to generate the hash value.</p><br/>

<style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://payu-india.github.io/CMS-Chatbot/', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to generate hash.">
                    Generate Hash
                </button>
`}</HTMLBlock>

## Errors

<br />
