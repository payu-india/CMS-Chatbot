---
title: Integrate Payment Link TPV
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Integrate Payment Link TPV
deprecated: false
hidden: true
metadata:
  robots: index
---

This section describes the steps to integrate Payment Link TPV (Third Party Verification) - from payment link creation to payment processing.

### Prerequisites

To use the TPV flow for Payment Links, ensure the **enableTpvFlow** configuration is enabled for your merchant account: Contact your PayU Key Account Manager (KAM) or <Anchor label="PayU Support" target="_blank" href="https://help.payu.in">PayU Support</Anchor> to enable this configuration.

### Steps to integrate

<Cards columns={3}>
  <Card title="1. Create Payment Link" href="#step-1-create-payment-link">
    Create a payment link with beneficiary account details for TPV verification.

    <br />
  </Card>

  <Card title="2. Intermediate Page" href="#step-2-intermediate-page">
    Customer opens the payment link and fills relevant details.

    <br />
  </Card>

  <Card title="3. Check Response from PayU" href="#step-4-check-response-from-payu">
    Check and handle the response received from PayU after payment processing.

    <br />
  </Card>

  <Card title="4. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status using webhooks or Verify Payments API.

    <br />
  </Card>
</Cards>

***

## Step 1: Create Payment Link

Create a payment link with beneficiary account details using the Create Payment Link API.

<Accordion title="Environment" icon="fa-globe">
  | Environment | URL                                       |
  | ----------- | ----------------------------------------- |
  | Test        | `https://uatoneapi.payu.in/payment-links` |
  | Production  | `https://oneapi.payu.in/payment-links`    |

  **HTTP Method**: POST

  **Content-Type**: application/json
</Accordion>

<Accordion title="Request Headers" icon="fa-key">
  | Parameter                      | Description                                    | Example                                      |
  | ------------------------------ | ---------------------------------------------- | -------------------------------------------- |
  | Authorization<br />`mandatory` | `String`<br />Bearer token for authentication. | `Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de...` |
  | mid<br />`mandatory`           | `String`<br />Merchant ID.                     | `8237350`                                    |
  | Content-Type<br />`mandatory`  | `String`<br />Content type of the request.     | `application/json`                           |
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                           | Description                                                          | Example                |
  | ----------------------------------- | -------------------------------------------------------------------- | ---------------------- |
  | subAmount<br />`mandatory`          | `Decimal`<br />The payment amount.                                   | `10.00`                |
  | description<br />`mandatory`        | `String`<br />Purpose of payment. Max 250 characters.                | `Payment for services` |
  | source<br />`mandatory`             | `String`<br />Source of the request.                                 | `API`                  |
  | maxPaymentsAllowed<br />`mandatory` | `Integer`<br />Must be `1` for TPV flow (single payment only).       | `1`                    |
  | beneficiarydetail<br />`mandatory`  | `Object`<br />Object containing beneficiary account details for TPV. | See below              |
  | invoiceNumber<br />`optional`       | `String`<br />Unique invoice number for the payment link.            | `INV123456789012`      |
  | customer<br />`optional`            | `Object`<br />Customer details object.                               | See below              |

  <Accordion title="beneficiarydetail Object Parameters" icon="fa-code">
    | Parameter                                 | Description                                                                                                                      | Example                          |
    | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
    | beneficiaryAccountNumber<br />`mandatory` | `List<String>`<br />Array of beneficiary account numbers. Maximum 4 accounts. Alphanumeric, max 50 characters each.              | `["917732227242", "72522762"]`   |
    | ifscCode<br />`mandatory`                 | `List<String>`<br />Array of IFSC codes corresponding to each account number. Exactly 11 characters each: `[A-Z]{4}0[A-Z0-9]{6}` | `["SBIN0007001", "HDFC0001234"]` |
    | beneficiaryName <br />`mandatory`         | `List<String>`<br /> Array of the beneficiary name.                                                                              | `"Ashish","Harish"`              |
    | beneficiaryAccountType <br />`mandatory`  | `List<String>` <br /> Array of the beneficiary account type. It can be "SAVINGS" or "CURRENT"                                    | `"SAVINGS","CURRENT"`            |
  </Accordion>

  <Accordion title="customer Object Parameters" icon="fa-user">
    | Parameter             | Description                             | Example                |
    | --------------------- | --------------------------------------- | ---------------------- |
    | email<br />`optional` | `String`<br />Customer's email address. | `john.doe@example.com` |
    | phone<br />`optional` | `String`<br />Customer's phone number.  | `9876543210`           |
    | name<br />`optional`  | `String`<br />Customer's name.          | `John Doe`             |
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://uatoneapi.payu.in/payment-links' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <Bearer Token>' \
  --header 'mid: 82**3*0' \
  --data-raw '{
      "subAmount": 10,
      "maxPaymentsAllowed": 1,
      "invoiceNumber": "INV123456789012",
      "description": "Payment for services",
      "customer": {
          "email": "john.doe@example.com",
          "phone": "9876543210",
          "name": "John Doe"
      },
      {
  "beneficiarydetail": {
    "beneficiaryAccountNumber": ["account1", "account2"],
    "ifscCode": ["IFSC1234567", "IFSC7654321"],
    "beneficiaryName": ["Beneficiary One", "Beneficiary Two"],
    "beneficiaryAccountType": ["SAVINGS", "CURRENT"]
  }
  }
  ,
      "source": "API"
  }'
  ```
  ```python
  import requests
  import json

  url = "https://uatoneapi.payu.in/payment-links"

  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
      "mid": "8237350"
  }

  payload = {
      "subAmount": 10,
      "maxPaymentsAllowed": 1,
      "invoiceNumber": "INV123456789012",
      "description": "Payment for services",
      "customer": {
          "email": "john.doe@example.com",
          "phone": "9876543210",
          "name": "John Doe"
      },
      "beneficiarydetail": {
          "beneficiaryAccountNumber": ["account1", "account2"],
          "ifscCode": ["IFSC1234567", "IFSC7654321"],
          "beneficiaryName": ["Beneficiary One", "Beneficiary Two"],
          "beneficiaryAccountType": ["SAVINGS", "CURRENT"]
      },
      "source": "API"
  }

  try:
      response = requests.post(url, headers=headers, data=json.dumps(payload))
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          try
          {
              string url = "https://uatoneapi.payu.in/payment-links";
              
              client.DefaultRequestHeaders.Add("Authorization", "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75");
              client.DefaultRequestHeaders.Add("mid", "8237350");

              string jsonPayload = @"{
                  ""subAmount"": 10,
                  ""maxPaymentsAllowed"": 1,
                  ""invoiceNumber"": ""INV123456789012"",
                  ""description"": ""Payment for services"",
                  ""customer"": {
                      ""email"": ""john.doe@example.com"",
                      ""phone"": ""9876543210"",
                      ""name"": ""John Doe""
                  },
                  ""beneficiarydetail"": {
                      ""beneficiaryAccountNumber"": [""account1"", ""account2""],
                      ""ifscCode"": [""IFSC1234567"", ""IFSC7654321""],
                      ""beneficiaryName"": [""Beneficiary One"", ""Beneficiary Two""],
                      ""beneficiaryAccountType"": [""SAVINGS"", ""CURRENT""]
                  },
                  ""source"": ""API""
              }";

              var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");
              
              HttpResponseMessage response = await client.PostAsync(url, content);
              string responseContent = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseContent}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error: {e.Message}");
          }
      }
  }
  ```
  ```javascript
  async function makePaymentLinkRequest() {
      const url = "https://uatoneapi.payu.in/payment-links";
      
      const headers = {
          "Content-Type": "application/json",
          "Authorization": "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
          "mid": "8237350"
      };
      
      const payload = {
          subAmount: 10,
          maxPaymentsAllowed: 1,
          invoiceNumber: "INV123456789012",
          description: "Payment for services",
          customer: {
              email: "john.doe@example.com",
              phone: "9876543210",
              name: "John Doe"
          },
          beneficiarydetail: {
              beneficiaryAccountNumber: ["account1", "account2"],
              ifscCode: ["IFSC1234567", "IFSC7654321"],
              beneficiaryName: ["Beneficiary One", "Beneficiary Two"],
              beneficiaryAccountType: ["SAVINGS", "CURRENT"]
          },
          source: "API"
      };
      
      try {
          const response = await fetch(url, {
              method: 'POST',
              headers: headers,
              body: JSON.stringify(payload)
          });
          
          const responseText = await response.text();
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return response;
      } catch (error) {
          console.error(`Error: ${error.message}`);
      }
  }

  // Call the function
  makePaymentLinkRequest();
  ```
  ```java
  import java.io.*;
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.nio.charset.StandardCharsets;

  public class PaymentLinkRequest {
      public static void main(String[] args) {
          try {
              URL url = new URL("https://uatoneapi.payu.in/payment-links");
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              // Set request method and headers
              connection.setRequestMethod("POST");
              connection.setRequestProperty("Content-Type", "application/json");
              connection.setRequestProperty("Authorization", "Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75");
              connection.setRequestProperty("mid", "8237350");
              connection.setDoOutput(true);
              
              // JSON payload
              String jsonPayload = "{\"subAmount\": 10,\"maxPaymentsAllowed\": 1,\"invoiceNumber\": \"INV123456789012\",\"description\": \"Payment for services\",\"customer\": {\"email\": \"john.doe@example.com\",\"phone\": \"9876543210\",\"name\": \"John Doe\"},\"beneficiarydetail\": {\"beneficiaryAccountNumber\": [\"account1\", \"account2\"],\"ifscCode\": [\"IFSC1234567\", \"IFSC7654321\"],\"beneficiaryName\": [\"Beneficiary One\", \"Beneficiary Two\"],\"beneficiaryAccountType\": [\"SAVINGS\", \"CURRENT\"]},\"source\": \"API\"}";
              
              // Write payload to request body
              try (OutputStream outputStream = connection.getOutputStream()) {
                  byte[] input = jsonPayload.getBytes(StandardCharsets.UTF_8);
                  outputStream.write(input, 0, input.length);
              }
              
              // Get response
              int statusCode = connection.getResponseCode();
              BufferedReader reader = new BufferedReader(new InputStreamReader(
                  statusCode >= 200 && statusCode < 300 ? connection.getInputStream() : connection.getErrorStream()
              ));
              
              StringBuilder response = new StringBuilder();
              String line;
              while ((line = reader.readLine()) != null) {
                  response.append(line);
              }
              reader.close();
              
              System.out.println("Status Code: " + statusCode);
              System.out.println("Response: " + response.toString());
              
          } catch (Exception e) {
              System.out.println("Error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://uatoneapi.payu.in/payment-links";

  $headers = [
      "Content-Type: application/json",
      "Authorization: Bearer 03ddf1ee8d6daf811016c1cc9ce6a3de1771092b1eaeeb936764743888b9eb75",
      "mid: 8237350"
  ];

  $payload = [
      "subAmount" => 10,
      "maxPaymentsAllowed" => 1,
      "invoiceNumber" => "INV123456789012",
      "description" => "Payment for services",
      "customer" => [
          "email" => "john.doe@example.com",
          "phone" => "9876543210",
          "name" => "John Doe"
      ],
      "beneficiarydetail" => [
          "beneficiaryAccountNumber" => ["account1", "account2"],
          "ifscCode" => ["IFSC1234567", "IFSC7654321"],
          "beneficiaryName" => ["Beneficiary One", "Beneficiary Two"],
          "beneficiaryAccountType" => ["SAVINGS", "CURRENT"]
      ],
      "source" => "API"
  ];

  $ch = curl_init();

  curl_setopt_array($ch, [
      CURLOPT_URL => $url,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POST => true,
      CURLOPT_HTTPHEADER => $headers,
      CURLOPT_POSTFIELDS => json_encode($payload),
      CURLOPT_TIMEOUT => 30,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_SSL_VERIFYPEER => false
  ]);

  $response = curl_exec($ch);
  $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);

  curl_close($ch);

  if ($error) {
      echo "Error: " . $error . "\n";
  } else {
      echo "Status Code: " . $statusCode . "\n";
      echo "Response: " . $response . "\n";
  }
  ?>
  ```
</Accordion>

<Accordion title="Validation Rules" icon="fa-check-circle">
  | Validation               | Rule                                            |
  | ------------------------ | ----------------------------------------------- |
  | Max Payments             | `maxPaymentsAllowed = 1`                        |
  | Max Beneficiaries        | ≤ 4 beneficiaries                               |
  | Equal Count              | Account numbers count = IFSC codes count        |
  | Account Format           | Alphanumeric, max 50 characters                 |
  | IFSC Format              | Exactly 11 characters: `[A-Z]{4}0[A-Z0-9]{6}`   |
  | Beneficiary Name         | Alphabetic characters and spaces, max 100 chars |
  | Beneficiary Account Type | Enum values only: SAVINGS, CURRENT              |
</Accordion>

***

## Step 2: Intermediate Page

When the payment link is created, the API returns a short URL (e.g., `https://v.payu.in/PAYUMN/flashvrkWhFD`).

<Accordion title="Customer Flow" icon="fa-user">
  1. Customer receives the payment link via email, SMS, or other channels
  2. Customer opens the link in their browser
  3. Customer fills in relevant details on the intermediate page
  4. Customer clicks "Make Payment" to proceed to the checkout page
</Accordion>

***

<br />

When the customer initiates payment, the backend converts beneficiary details to pipe-separated format and posts to the `_payment` API.

<Accordion title="Environment" icon="fa-globe">
  | Environment | URL                               |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                          | Description                                                                                                                | Example                                                                 |
  | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
  | key<br />`mandatory`               | `String`<br />Merchant key provided by PayU.                                                                               | `JP***g`                                                                |
  | txnid<br />`mandatory`             | `String`<br />Unique transaction ID generated by you.                                                                      | `TtEmKjWF2uGliF`                                                        |
  | amount<br />`mandatory`            | `String`<br />Payment amount.                                                                                              | `5000.00`                                                               |
  | productinfo<br />`mandatory`       | `String`<br />Brief description of the product or service.                                                                 | `Payment for services`                                                  |
  | firstname<br />`mandatory`         | `String`<br />Customer's first name.                                                                                       | `John`                                                                  |
  | email<br />`mandatory`             | `String`<br />Customer's email address.                                                                                    | `john.doe@example.com`                                                  |
  | phone<br />`mandatory`             | `String`<br />Customer's phone number.                                                                                     | `9876543210`                                                            |
  | surl<br />`mandatory`              | `String`<br />Success URL where PayU redirects after successful payment.                                                   | `https://yoursite.com/success`                                          |
  | furl<br />`mandatory`              | `String`<br />Failure URL where PayU redirects after failed payment.                                                       | `https://yoursite.com/failure`                                          |
  | beneficiarydetail<br />`mandatory` | `JSON String`<br />JSON object with pipe-separated beneficiary account numbers and IFSC codes. Up to 4 accounts supported. | Refer to beneficiarydetail JSON object fields section below this table. |
  | api\_version<br />`mandatory`      | `Integer`<br />Must be set to 20 when beneficiary details are present.                                                     | `20`                                                                    |
  | hash<br />`mandatory`              | `String`<br />Hash calculated using the checksum logic. Refer to Hash Generation below this table.                         | Refer to Hash Generation below this table.                              |
  | udf1 - udf5<br />`optional`        | `String`<br />User-defined fields for storing additional information.                                                      | ` `                                                                     |

  <Accordion title="beneficiarydetail JSON object fields" icon="fa-code">
    It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to four account details in this parameter. For example:

    ```json
    {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",
    "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
    ```
  </Accordion>

  <Accordion title="Hash Generation" icon="fa-lock">
    The hash is generated using the following format:

    ```
    key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
    ```

    Where `beneficiarydetail` is the JSON string representation with pipe-separated values:

    ```json
    {"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}
    ```

    > **Note**: The `beneficiarydetail` parameter value will be the last value to be appended before SALT.
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'txnid=TtEmKjWF2uGliF' \
  --data-urlencode 'amount=5000.00' \
  --data-urlencode 'productinfo=Payment for services' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john.doe@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'surl=https://yoursite.com/success' \
  --data-urlencode 'furl=https://yoursite.com/failure' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}' \
  --data-urlencode 'api_version=20' \
  --data-urlencode 'hash=<generated_hash>'
  ```

  ```python
  import requests

  url = "https://test.payu.in/_payment"

  payload = {
      "key": "JP***g",
      "txnid": "TtEmKjWF2uGliF",
      "amount": "5000.00",
      "productinfo": "Payment for services",
      "firstname": "John",
      "email": "john.doe@example.com",
      "phone": "9876543210",
      "surl": "https://yoursite.com/success",
      "furl": "https://yoursite.com/failure",
      "beneficiarydetail": '{"beneficiaryAccountNumber":"917732227242|72522762","ifscCode":"SBIN0007001|HDFC0001234"}',
      "api_version": "20",
      "hash": "<generated_hash>"
  }

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.text)
  ```

  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("txnid", "TtEmKjWF2uGliF"),
              new KeyValuePair<string, string>("amount", "5000.00"),
              new KeyValuePair<string, string>("productinfo", "Payment for services"),
              new KeyValuePair<string, string>("firstname", "John"),
              new KeyValuePair<string, string>("email", "john.doe@example.com"),
              new KeyValuePair<string, string>("phone", "9876543210"),
              new KeyValuePair<string, string>("surl", "https://yoursite.com/success"),
              new KeyValuePair<string, string>("furl", "https://yoursite.com/failure"),
              new KeyValuePair<string, string>("beneficiarydetail", "{\"beneficiaryAccountNumber\":\"917732227242|72522762\",\"ifscCode\":\"SBIN0007001|HDFC0001234\"}"),
              new KeyValuePair<string, string>("api_version", "20"),
              new KeyValuePair<string, string>("hash", "<generated_hash>")
          });
          
          var response = await client.PostAsync("https://test.payu.in/_payment", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```

  ```javascript
  const postPaymentTPV = async () => {
      const url = "https://test.payu.in/_payment";
      
      const params = new URLSearchParams();
      params.append("key", "JP***g");
      params.append("txnid", "TtEmKjWF2uGliF");
      params.append("amount", "5000.00");
      params.append("productinfo", "Payment for services");
      params.append("firstname", "John");
      params.append("email", "john.doe@example.com");
      params.append("phone", "9876543210");
      params.append("surl", "https://yoursite.com/success");
      params.append("furl", "https://yoursite.com/failure");
      params.append("beneficiarydetail", JSON.stringify({
          beneficiaryAccountNumber: "917732227242|72522762",
          ifscCode: "SBIN0007001|HDFC0001234"
      }));
      params.append("api_version", "20");
      params.append("hash", "<generated_hash>");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.text();
      console.log(data);
  };

  postPaymentTPV();
  ```

  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PaymentLinkTPV {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/_payment";
          
          String beneficiarydetail = URLEncoder.encode("{\"beneficiaryAccountNumber\":\"917732227242|72522762\",\"ifscCode\":\"SBIN0007001|HDFC0001234\"}", StandardCharsets.UTF_8);
          
          String params = "key=JP***g"
              + "&txnid=TtEmKjWF2uGliF"
              + "&amount=5000.00"
              + "&productinfo=Payment+for+services"
              + "&firstname=John"
              + "&email=john.doe@example.com"
              + "&phone=9876543210"
              + "&surl=https://yoursite.com/success"
              + "&furl=https://yoursite.com/failure"
              + "&beneficiarydetail=" + beneficiarydetail
              + "&api_version=20"
              + "&hash=<generated_hash>";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```

  ```php
  <?php
  $url = "https://test.payu.in/_payment";

  $data = array(
      "key" => "JP***g",
      "txnid" => "TtEmKjWF2uGliF",
      "amount" => "5000.00",
      "productinfo" => "Payment for services",
      "firstname" => "John",
      "email" => "john.doe@example.com",
      "phone" => "9876543210",
      "surl" => "https://yoursite.com/success",
      "furl" => "https://yoursite.com/failure",
      "beneficiarydetail" => json_encode(array(
          "beneficiaryAccountNumber" => "917732227242|72522762",
          "ifscCode" => "SBIN0007001|HDFC0001234"
      )),
      "api_version" => "20",
      "hash" => "<generated_hash>"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/x-www-form-urlencoded"));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

***

## Step 3: Check Response from PayU

After the payment is processed, PayU sends a response to your success or failure URL. You must validate the hash and handle the response accordingly.

<Accordion title="Hash Validation (Reverse Hashing)" icon="fa-lock">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure.

  The order of the parameters for reverse hashing:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  > **Important**: The `beneficiarydetail` parameter should **NOT** be present in reverse hashing.
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter          | Description                                                                                                                                | Example                                |
  | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
  | mihpayid           | `String`<br />Unique reference number created for each transaction at PayU's end. Store this for future actions like Inquiry or Refund.    | `403993715524308236`                   |
  | mode               | `String`<br />The payment mode used by the customer.                                                                                       | `NB`                                   |
  | status             | `String`<br />Status of the transaction. Possible values: `success`, `failure`, `pending`. Only `success` should be treated as successful. | `success`                              |
  | unmappedstatus     | `String`<br />Detailed status of the transaction.                                                                                          | `captured`                             |
  | key                | `String`<br />The merchant key used for the transaction.                                                                                   | `JP***g`                               |
  | txnid              | `String`<br />The transaction ID posted by the merchant during the transaction request.                                                    | `TtEmKjWF2uGliF`                       |
  | amount             | `String`<br />The transaction amount.                                                                                                      | `5000.00`                              |
  | discount           | `String`<br />The discount amount given by bank on the transaction fee (if any).                                                           | `0.00`                                 |
  | net\_amount\_debit | `String`<br />The net amount debited from the customer's account.                                                                          | `5000`                                 |
  | addedon            | `String`<br />The transaction timestamp.                                                                                                   | `2021-10-05 12:44:06`                  |
  | productinfo        | `String`<br />Product information as sent in the request.                                                                                  | `Payment for services`                 |
  | firstname          | `String`<br />Customer's first name.                                                                                                       | `John`                                 |
  | email              | `String`<br />Customer's email address.                                                                                                    | `john.doe@example.com`                 |
  | phone              | `String`<br />Customer's phone number.                                                                                                     | `9876543210`                           |
  | hash               | `String`<br />Hash for response validation (reverse hash).                                                                                 | `<hash_value>`                         |
  | field9             | `String`<br />Transaction message from the bank.                                                                                           | `Transaction Completed Successfully`   |
  | PG\_TYPE           | `String`<br />The payment gateway type used.                                                                                               | `NB-PG`                                |
  | bank\_ref\_num     | `String`<br />Bank reference number for the transaction.                                                                                   | `30646df4-69b7-43f4-acdd-21e6a593c037` |
  | bankcode           | `String`<br />Bank code used for the transaction.                                                                                          | `TESTPGNB`                             |
  | error              | `String`<br />Error code. `E000` indicates no error.                                                                                       | `E000`                                 |
  | error\_Message     | `String`<br />Error message description.                                                                                                   | `No Error`                             |
  | udf1 - udf5        | `String`<br />User-defined fields as sent in the request.                                                                                  | ` `                                    |
</Accordion>

<Accordion title="Sample Response" icon="fa-check">
  ```php
  Array
  (
      [mihpayid] => 403993715524308236
      [mode] => NB
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => TtEmKjWF2uGliF
      [amount] => 5000.00
      [discount] => 0.00
      [net_amount_debit] => 5000
      [addedon] => 2021-10-05 12:44:06
      [productinfo] => Payment for services
      [firstname] => John
      [lastname] => Doe
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => john.doe@example.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => NB-PG
      [bank_ref_num] => 30646df4-69b7-43f4-acdd-21e6a593c037
      [bankcode] => TESTPGNB
      [error] => E000
      [error_Message] => No Error
  )
  ```

  > **Important**: Store the `mihpayid` and `txnid` parameter values in your server as proof that TPV has been completed for a customer.
</Accordion>

***

## Step 4: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

***

## Key Limitations

| Limitation        | Description                                    |
| ----------------- | ---------------------------------------------- |
| Max Beneficiaries | Maximum 4 beneficiaries per payment link       |
| Max Payments      | `maxPaymentsAllowed = 1` (single payment only) |
| Partial Payment   | Not supported with TPV flow                    |
| Merchant Config   | `enableTpvFlow` must be set to `"1"`           |

<br />
