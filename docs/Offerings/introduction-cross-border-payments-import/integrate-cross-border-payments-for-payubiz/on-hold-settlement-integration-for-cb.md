---
title: On-Hold Settlement Integration for CB
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes the step-by-step procedure to process on-hold transactions. The integration involves retrieving transactions that require additional information and submitting the required details to release settlements.

<Cards columns={2}>
  <Card title="1. Get On-Hold Transactions" href="https://docs.payu.in/docs/on-hold-settlement-integration#step-1-get-on-hold-transactions">
    Retrieve list of transactions requiring additional information

    <br />
  </Card>

  <Card title="2. Update Transaction Details" href="https://docs.payu.in/docs/on-hold-settlement-integration#step-2-update-transaction-details">
    Submit required customer information to release settlement

    <br />
  </Card>
</Cards>

***

## Step 1: Get On-Hold Transactions

Retrieve on-hold transactions using the GET API to identify which transactions require additional information.

<Accordion title="API endpoint" icon="fa-globe">
  | Environment | URL                                                | Method |
  | :---------- | :------------------------------------------------- | :----- |
  | Production  | `https://oneapi.payu.in/opgsp/getOnHoldTxnDetails` | GET    |
</Accordion>

<Accordion title="Request headers" icon="fa-heading">
  | Parameter                      | Description                                 | Example                       |
  | :----------------------------- | :------------------------------------------ | :---------------------------- |
  | mid<br />`mandatory`           | `String` - Merchant ID of the merchant      | 8763182                       |
  | Authorization<br />`mandatory` | `String` - HMAC SHA512 authorization header | See overview                  |
  | Date<br />`mandatory`          | `String` - Current UTC date in HTTP format  | Wed, 28 Jun 2023 11:25:19 GMT |
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                  | Description                                                                         | Example    |
  | :------------------------- | :---------------------------------------------------------------------------------- | :--------- |
  | startDate<br />`mandatory` | `String` - The start date from which you need to check the data. Format: YYYY-MM-DD | 2025-01-22 |
  | endDate<br />`mandatory`   | `String` - The end date up to which you need the data. Format: YYYY-MM-DD           | 2025-01-25 |
  | pageSize<br />`optional`   | `Integer` - Number of records per page. Default: 50                                 | 10         |
  | pageOffset<br />`optional` | `Integer` - Page number for pagination. Default: 0                                  | 0          |
  | orderBy<br />`optional`    | `String` - Field to order results by                                                | addedOn    |
  | order<br />`optional`      | `String` - Sort order. Values: ASC, DESC                                            | ASC        |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0' \
  --header 'mid: 8763182' \
  --header 'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"' \
  --header 'Date: Wed, 28 Jun 2023 11:25:19 GMT'
  ```

  ```python
  import requests

  url = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails"

  params = {
      'startDate': '2025-01-22',
      'endDate': '2025-01-25',
      'orderBy': 'addedOn',
      'order': 'ASC',
      'pageSize': '10',
      'pageOffset': '0'
  }

  headers = {
      'mid': '8763182',
      'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
      'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
  }

  try:
      response = requests.get(url, headers=headers, params=params)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.json()}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```

  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          try
          {
              string baseUrl = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails";
              string queryParams = "?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0";
              string url = baseUrl + queryParams;

              client.DefaultRequestHeaders.Clear();
              client.DefaultRequestHeaders.Add("mid", "8763182");
              client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
              client.DefaultRequestHeaders.Add("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

              HttpResponseMessage response = await client.GetAsync(url);
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
  async function getOnHoldTransactions() {
      const baseUrl = 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails';
      const params = new URLSearchParams({
          startDate: '2025-01-22',
          endDate: '2025-01-25',
          orderBy: 'addedOn',
          order: 'ASC',
          pageSize: '10',
          pageOffset: '0'
      });

      const url = `${baseUrl}?${params.toString()}`;

      const requestOptions = {
          method: 'GET',
          headers: {
              'mid': '8763182',
              'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
              'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
          }
      };

      try {
          const response = await fetch(url, requestOptions);
          const responseJson = await response.json();

          console.log(`Status: ${response.status}`);
          console.log('Response:', responseJson);

          return responseJson;
      } catch (error) {
          console.error('Error:', error);
          throw error;
      }
  }

  getOnHoldTransactions()
      .then(result => console.log('Request complete'))
      .catch(error => console.error('Failed:', error));
  ```

  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class GetOnHoldTransactions {

      public static void main(String[] args) {
          try {
              String baseUrl = "https://oneapi.payu.in/opgsp/getOnHoldTxnDetails";
              String queryParams = "?startDate=2025-01-22&endDate=2025-01-25&orderBy=addedOn&order=ASC&pageSize=10&pageOffset=0";
              String url = baseUrl + queryParams;

              URL urlObj = new URL(url);
              HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();

              connection.setRequestMethod("GET");
              connection.setRequestProperty("mid", "8763182");
              connection.setRequestProperty("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
              connection.setRequestProperty("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

              int responseCode = connection.getResponseCode();
              System.out.println("Status Code: " + responseCode);

              try (BufferedReader br = new BufferedReader(new InputStreamReader(
                      connection.getInputStream(), StandardCharsets.UTF_8))) {

                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }
                  System.out.println("Response: " + response.toString());
              }

              connection.disconnect();
          } catch (Exception e) {
              e.printStackTrace();
          }
      }
  }
  ```

  ```php
  <?php

  $baseUrl = 'https://oneapi.payu.in/opgsp/getOnHoldTxnDetails';
  $params = http_build_query([
      'startDate' => '2025-01-22',
      'endDate' => '2025-01-25',
      'orderBy' => 'addedOn',
      'order' => 'ASC',
      'pageSize' => '10',
      'pageOffset' => '0'
  ]);

  $url = $baseUrl . '?' . $params;

  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'mid: 8763182',
      'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
      'Date: Wed, 28 Jun 2023 11:25:19 GMT'
  ));

  $response = curl_exec($ch);

  if (curl_errno($ch)) {
      echo 'cURL Error: ' . curl_error($ch);
  } else {
      $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      echo "HTTP Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);

  $responseData = json_decode($response, true);
  if ($responseData !== null) {
      echo "Parsed Response:\n";
      print_r($responseData);
  }
  ?>
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ```json
  {
      "code": "2000",
      "message": "Success",
      "status": 0,
      "result": {
          "pageSize": 10,
          "pages": 1,
          "rows": 1,
          "pageOffset": 0,
          "data": [
              {
                  "requestId": "15916911884",
                  "action": "capture",
                  "displayMessage": "Please provide additional customer information to release settlement from on-hold by 2025-01-27 00:00:00 IST. Your prompt response is greatly appreciated.",
                  "dueDate": "2025-01-27 00:00:00",
                  "status": "needsResponse",
                  "keyMapping": "{\"invoice_id\":\"\",\"first_name\":\"\",\"last_name\":\"\"}",
                  "merchantTransactionId": "31017154721",
                  "dateOfTransaction": "2025-01-21 13:15:27",
                  "dateOfFirstSettlementTransaction": "2025-01-23 17:17:40",
                  "keyMappingList": [
                      {
                          "key": "first_name",
                          "displayName": "First name",
                          "value": "",
                          "order": 1,
                          "validationRegex": "^[A-Za-z]*$"
                      },
                      {
                          "key": "last_name",
                          "displayName": "Last name",
                          "value": "",
                          "order": 2,
                          "validationRegex": "^[A-Za-z]*$"
                      },
                      {
                          "key": "invoice_id",
                          "displayName": "Invoice ID",
                          "value": "",
                          "order": 5,
                          "validationRegex": "^[a-zA-Z0-9]*$"
                      }
                  ],
                  "editable": 1
              }
          ]
      }
  }
  ```
</Accordion>

<Accordion title="Understanding the response" icon="fa-info-circle">
  After receiving the response, check the following:

  1. **status**: Look for transactions with `status: "needsResponse"` - these require action
  2. **editable**: Only transactions with `editable: 1` can be updated
  3. **keyMappingList**: Contains the list of required fields you need to submit
  4. **dueDate**: Submit the information before this date to avoid automatic refund
  5. **requestId**: Use this as `transactionId` in the POST API

  **Transaction Status Values:**

  | Status         | Description                     | Action                                      |
  | :------------- | :------------------------------ | :------------------------------------------ |
  | needsResponse  | Additional information required | Submit required fields via POST API         |
  | rejected       | Rejected by bank authority      | Review rejection reason, no action possible |
  | dueDateExpired | Due date has passed             | Transaction will be refunded automatically  |
</Accordion>

***

## Step 2: Update Transaction Details

Submit the required customer information using the POST API to release the on-hold settlement.

<Accordion title="API endpoint" icon="fa-globe">
  | Environment | URL                                                   | Method |
  | :---------- | :---------------------------------------------------- | :----- |
  | Production  | `https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails` | POST   |
</Accordion>

<Accordion title="Request headers" icon="fa-heading">
  | Parameter                      | Description                                 | Example                       |
  | :----------------------------- | :------------------------------------------ | :---------------------------- |
  | mid<br />`mandatory`           | `String` - Merchant ID of the merchant      | 180012                        |
  | accept<br />`mandatory`        | `String` - Type of JSON required in the API | application/json              |
  | Content-Type<br />`mandatory`  | `String` - Content type of the request body | application/json              |
  | Authorization<br />`mandatory` | `String` - HMAC SHA512 authorization header | See overview                  |
  | Date<br />`mandatory`          | `String` - Current UTC date in HTTP format  | Wed, 28 Jun 2023 11:25:19 GMT |
</Accordion>

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                                   | Description                                                          | Example     |
  | :------------------------------------------ | :------------------------------------------------------------------- | :---------- |
  | transactionId<br />`mandatory`              | `String` - The PayU transaction ID (requestId from GET API response) | 15916911884 |
  | amlockTxnRequestMappingDto<br />`mandatory` | `Array` - Array of key-value pairs containing the required fields    | See below   |

  **amlockTxnRequestMappingDto Object:**

  | Parameter              | Description                                     | Example     |
  | :--------------------- | :---------------------------------------------- | :---------- |
  | key<br />`mandatory`   | `String` - Field key name (from keyMappingList) | first\_name |
  | value<br />`mandatory` | `String` - Value for the field                  | John        |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  Based on the GET API response above, submit the required fields:

  ```bash
  curl --location 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails' \
  --header 'accept: application/json' \
  --header 'mid: 180012' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"' \
  --header 'Date: Wed, 28 Jun 2023 11:25:19 GMT' \
  --data '[
      {
          "transactionId": "15916911884",
          "amlockTxnRequestMappingDto": [
              {
                  "key": "first_name",
                  "value": "John"
              },
              {
                  "key": "last_name",
                  "value": "Doe"
              },
              {
                  "key": "invoice_id",
                  "value": "INV123456"
              }
          ]
      }
  ]'
  ```

  ```python
  import requests
  import json

  url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails"

  headers = {
      'accept': 'application/json',
      'mid': '180012',
      'Content-Type': 'application/json',
      'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
      'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
  }

  data = [
      {
          "transactionId": "15916911884",
          "amlockTxnRequestMappingDto": [
              {
                  "key": "first_name",
                  "value": "John"
              },
              {
                  "key": "last_name",
                  "value": "Doe"
              },
              {
                  "key": "invoice_id",
                  "value": "INV123456"
              }
          ]
      }
  ]

  try:
      response = requests.post(url, headers=headers, json=data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.json()}")
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
              string url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails";

              string jsonData = @"[
                  {
                      ""transactionId"": ""15916911884"",
                      ""amlockTxnRequestMappingDto"": [
                          {
                              ""key"": ""first_name"",
                              ""value"": ""John""
                          },
                          {
                              ""key"": ""last_name"",
                              ""value"": ""Doe""
                          },
                          {
                              ""key"": ""invoice_id"",
                              ""value"": ""INV123456""
                          }
                      ]
                  }
              ]";

              var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

              client.DefaultRequestHeaders.Clear();
              client.DefaultRequestHeaders.Add("accept", "application/json");
              client.DefaultRequestHeaders.Add("mid", "180012");
              client.DefaultRequestHeaders.Add("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
              client.DefaultRequestHeaders.Add("Date", "Wed, 28 Jun 2023 11:25:19 GMT");

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
  async function updateOnHoldTransaction() {
      const url = 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails';

      const data = [
          {
              transactionId: "15916911884",
              amlockTxnRequestMappingDto: [
                  {
                      key: "first_name",
                      value: "John"
                  },
                  {
                      key: "last_name",
                      value: "Doe"
                  },
                  {
                      key: "invoice_id",
                      value: "INV123456"
                  }
              ]
          }
      ];

      const requestOptions = {
          method: 'POST',
          headers: {
              'accept': 'application/json',
              'mid': '180012',
              'Content-Type': 'application/json',
              'Authorization': 'hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
              'Date': 'Wed, 28 Jun 2023 11:25:19 GMT'
          },
          body: JSON.stringify(data)
      };

      try {
          const response = await fetch(url, requestOptions);
          const responseJson = await response.json();

          console.log(`Status: ${response.status}`);
          console.log('Response:', responseJson);

          return responseJson;
      } catch (error) {
          console.error('Error:', error);
          throw error;
      }
  }

  updateOnHoldTransaction()
      .then(result => console.log('Update complete'))
      .catch(error => console.error('Failed:', error));
  ```

  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class UpdateOnHoldTransaction {

      public static void main(String[] args) {
          try {
              String url = "https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails";

              String jsonData = "[\n" +
                  "    {\n" +
                  "        \"transactionId\": \"15916911884\",\n" +
                  "        \"amlockTxnRequestMappingDto\": [\n" +
                  "            {\n" +
                  "                \"key\": \"first_name\",\n" +
                  "                \"value\": \"John\"\n" +
                  "            },\n" +
                  "            {\n" +
                  "                \"key\": \"last_name\",\n" +
                  "                \"value\": \"Doe\"\n" +
                  "            },\n" +
                  "            {\n" +
                  "                \"key\": \"invoice_id\",\n" +
                  "                \"value\": \"INV123456\"\n" +
                  "            }\n" +
                  "        ]\n" +
                  "    }\n" +
                  "]";

              URL urlObj = new URL(url);
              HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();

              connection.setRequestMethod("POST");
              connection.setRequestProperty("accept", "application/json");
              connection.setRequestProperty("mid", "180012");
              connection.setRequestProperty("Content-Type", "application/json");
              connection.setRequestProperty("Authorization", "hmac username=\"<key>\", algorithm=\"sha512\", headers=\"date\", signature=\"<hash>\"");
              connection.setRequestProperty("Date", "Wed, 28 Jun 2023 11:25:19 GMT");
              connection.setDoOutput(true);

              try (OutputStream os = connection.getOutputStream()) {
                  byte[] input = jsonData.getBytes(StandardCharsets.UTF_8);
                  os.write(input, 0, input.length);
              }

              int responseCode = connection.getResponseCode();
              System.out.println("Status Code: " + responseCode);

              try (BufferedReader br = new BufferedReader(new InputStreamReader(
                      connection.getInputStream(), StandardCharsets.UTF_8))) {

                  StringBuilder response = new StringBuilder();
                  String responseLine;
                  while ((responseLine = br.readLine()) != null) {
                      response.append(responseLine.trim());
                  }
                  System.out.println("Response: " + response.toString());
              }

              connection.disconnect();
          } catch (Exception e) {
              e.printStackTrace();
          }
      }
  }
  ```

  ```php
  <?php

  $url = 'https://oneapi.payu.in/opgsp/updateOnHoldTxnDetails';

  $data = [
      [
          "transactionId" => "15916911884",
          "amlockTxnRequestMappingDto" => [
              [
                  "key" => "first_name",
                  "value" => "John"
              ],
              [
                  "key" => "last_name",
                  "value" => "Doe"
              ],
              [
                  "key" => "invoice_id",
                  "value" => "INV123456"
              ]
          ]
      ]
  ];

  $ch = curl_init();

  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'accept: application/json',
      'mid: 180012',
      'Content-Type: application/json',
      'Authorization: hmac username="<key>", algorithm="sha512", headers="date", signature="<hash>"',
      'Date: Wed, 28 Jun 2023 11:25:19 GMT'
  ));

  $response = curl_exec($ch);

  if (curl_errno($ch)) {
      echo 'cURL Error: ' . curl_error($ch);
  } else {
      $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
      echo "HTTP Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }

  curl_close($ch);

  $responseData = json_decode($response, true);
  if ($responseData !== null) {
      echo "Parsed Response:\n";
      print_r($responseData);
  }
  ?>
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ### Success Response

  ```json
  {
      "transactionId": "15916911884",
      "action": "capture",
      "responseDTO": {
          "code": "2000",
          "message": "Success",
          "status": 0,
          "result": "Successfully update the fields and run the settlement fallback"
      }
  }
  ```

  ### Failure Responses

  **Invalid Merchant ID:**

  ```json
  {
      "transactionId": "15916911884",
      "action": "capture",
      "responseDTO": {
          "message": "Invalid Merchant Id",
          "status": 1,
          "traceId": "24916044faeafc41f750c7fe63939e47"
      }
  }
  ```

  **No Data Found:**

  ```json
  {
      "transactionId": "15916911884",
      "action": null,
      "responseDTO": {
          "code": "4000",
          "message": "No data found for given payuId",
          "status": 1,
          "traceId": "21df514339749b538e91102982073f0a"
      }
  }
  ```
</Accordion>

<Accordion title="Response status codes" icon="fa-list-ol">
  | Value | Meaning                                                        | Action to Take                                                        |
  | :---- | :------------------------------------------------------------- | :-------------------------------------------------------------------- |
  | 0     | Response not received yet / Fields updated successfully        | Wait for processing or proceed                                        |
  | 1     | Successfully update the fields and run the settlement fallback | No action required - success                                          |
  | -1    | Invalid key value pair passed                                  | Verify the key names and values match the keyMappingList from GET API |
  | -2    | Failed to call PayU API opgsp\_update\_transaction             | Retry the request or contact support                                  |
  | -3    | Exception occurred in updateFieldsForAmlockTxnRetry            | Contact support with traceId                                          |
</Accordion>

***

<br />
