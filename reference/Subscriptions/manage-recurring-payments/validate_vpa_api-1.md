---
api:
  file: paritalgeneral-apis-15.json
  operationId: validateVPA-1
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Validate VPA or UPI Handle API
  description: >-
    Learn how to validate Virtual Payment Addresses (VPA) using PayU's Validate
    VPA API. This documentation provides detailed instructions for integrating
    VPA validation, ensuring secure and accurate UPI transactions for your
    customers.
  keywords:
    - PayU Validate VPA API
    - Validate Virtual Payment Address
    - PayU UPI handle validation
    - UPI VPA validation
    - Check UPI Handle
    - Check UPI VPA
  robots: index
---
Use this API to check whether a VPA is valid.

<Callout icon="👍" theme="okay">
  **Handy Tips**

  You should poll this API after a customer enters a VPA on the merchant page to check for its validation. If VPA is valid only then, the second call should be made.
</Callout>

<GENERALAPIsEnvironment />

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  **Validate VPA**

  <Validate_VPA />

  **Validate VPA for Recurring Payment**

  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
    -H "accept: application/json" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=JP***g" \
    -d "command=validateVPA" \
    -d "var1=9999999999@upi" \
    -d "var2={\"validateAutoPayVPA\":\"1\"}" \
    -d "hash=75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
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
      "key": "JP***g",
      "command": "validateVPA",
      "var1": "9999999999@upi",
      "var2": var2_json,
      "hash": "75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e"
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
          params.put("key", "JP***g");
          params.put("command", "validateVPA");
          params.put("var1", "9999999999@upi");
          params.put("var2", var2Json);
          params.put("hash", "75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e");
          
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
          System.out.println("Response: " + response.body());
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
      hash: '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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
      'hash' => '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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
      hash    => '75uy573dce34375a5fa2970afa21023d53e1cf5b8cd80a6472poy9b7c964c7a5da9146c9007df8b7391cbaf2d7d7d91dcaae8bf1d19d1837315a3376d6dc827e'
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

<Accordion title="Sample response" icon="fa-reply">
  **Success scenario**

  if successfully validated:

  ```plaintext
  {
     "status":"SUCCESS",
     "vpa":"9999999999@upi",
     "isVPAValid":1,
     "isAutoPayVPAValid":1,
     "isAutoPayBankValid":"NA",
     "payerAccountName":"ABC"
  }
  ```

  > 📘 Notes:
  >
  > * The **payerAccountName** parameter can be empty or NA or will have a payer name based on the value given by the bank.
  > * If both **isVPAValid** and **isAutoPayVPAValid** is 1, you must initiate payment for Recurring Payments.
  > * Ignore the **isAutoPayBankValid** parameter in the response.

  **Failure scenarios**

  * If invalid VPA, the response is similar to the following:

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"payerAccountName":"NA"
  }  
  ```

  * Invalid VPA but handle supporting SI (Autopay):

  ```plaintext
  {
   "status":"SUCCESS","vpa":"abc@upi","isVPAValid":0,"isAutoPayVPAValid":1,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```

  * Customer valid but handle not supporting SI (Autopay):

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":1,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"XYZ"
  }
  ```

  * Neither customer valid nor handle supporting Autopay:

  ```plaintext
  {
    "status":"SUCCESS","vpa":"xyz@freecharge","isVPAValid":0,"isAutoPayVPAValid":0,"isAutoPayBankValid":"NA","payerAccountName":"NA"
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  {/* Properly formatted JSX Table */}

  <Table>
    <thead>
      <tr>
        <th>
          **Parameter**
        </th>

        <th>
          **Description**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>
          status
        </td>

        <td>
          This parameter returns any of the following based on whether the API was successful or failure:

          * Successful
          * Failure
        </td>
      </tr>

      <tr>
        <td>
          vpa
        </td>

        <td>
          This parameter returns the VPA ID.
        </td>
      </tr>

      <tr>
        <td>
          isVPAValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the VPA is valid or not:

          * **1**: Indicates that VPA is valid
          * **0**: Indicates the VPA is invalid
        </td>
      </tr>

      <tr>
        <td>
          isAutoPayVPAValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the VPA has registered for Recurring Payments or Autopay:

          * **1**: Indicates that VPA has registered for Recurring Payments
          * **0**: Indicates that VPA has not registered for Recurring Payments
        </td>
      </tr>

      <tr>
        <td>
          isAutoPayBankValid
        </td>

        <td>
          This parameter returns any of the following to indicate whether the corresponding bank account has registered for Recurring Payments or Autopay:

          * **1**: Indicates that bank account has registered for Recurring Payments
          * **0**: Indicates that bank account has not registered for Recurring Payments
        </td>
      </tr>

      <tr>
        <td>
          payerAccountName
        </td>

        <td>
          This parameter returns the name of the account holder (corresponding VPA).
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>

## Request parameters

You can use any valid VPA while trying out the API:

<Accordion title="Additional information for request parameters" icon="fa-flask">
  {/* Properly formatted JSX Table with align attribute */}

  <Table align={["left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Reference
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          {/* Properly formatted JSX component */}

          <Glossary>key</Glossary>
        </td>

        <td style={{ textAlign: "left" }}>
          For more information on how to generate the Key and Salt, refer to any of the following:

          * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
          * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          {/* Properly formatted JSX component */}

          <Glossary>hash</Glossary>
        </td>

        <td style={{ textAlign: "left" }}>
          Hash logic for this API is:

          ```
          sha512(key|command|var1|salt) sha512
          ```
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          var1
        </td>

        <td style={{ textAlign: "left" }}>
          For JSON fields description, refer to [Additional Info for General APIs](ref:addl-info-general-apis)
        </td>
      </tr>
    </tbody>
  </Table>
</Accordion>
