---
title: On-Hold Settlements - Cross-Border Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
When processing outward settlements from India, authorized banks (AD-1) require additional information as per RBI regulations. Sometimes, settlements are **put on hold** or **rejected by the bank**. This section explains:

* Why settlements may be on hold
* How to identify such transactions
* Steps to resolve and unblock them

Also, this section describes the step-by-step procedure to process on-hold transactions. The integration involves retrieving transactions that require additional information and submitting the required details to release settlements.

## Transaction Statuses & Next Steps

| Transaction Status   | Description                                                                                                         | Next Steps                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Needs Response**   | Settlement is temporarily on hold because mandatory information is missing.                                         | Provide the missing details before the due date shown in the **Submit before** column. For more information, refer to [Types of Settlement Holds](types-of-settlement-holds) table. |
| **Rejected by Bank** | The bank identified an anti-money laundering or sanction screening match on the buyer. Settlement is non-compliant. | Refund the transaction.                                                                                                                                                             |
| **Due Date Expired** | The time window (~7 days) for providing information has elapsed.                                                    | Contact your Account Manager for deadline extension.                                                                                                                                |
| **Settled**          | Settlement is completed. You can check the "Unique Transaction Reference."                                          | No action needed.                                                                                                                                                                   |

## Types of Settlement Holds

If the transaction status is **Needs Response**, additional information is required. Below are common scenarios and resolution steps:

| **Scenario**                                   | **Description**                                                         | **Required Information & Resolution Steps**                                                                                                                                                                                |
| ---------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Provide valid invoice number**               | Invoice number is mandatory for compliance on imports to India.         | You can provide the invoice number via:<br />1. **PayU Dashboard** → **On-hold Settlements** tab<br />2. Update `udf-5` (one-time payment) or `udf-3` parameters using the UDF Update API. <br />3. Use Invoice Upload API |
| **Provide complete name of buyer**             | Missing First Name or Last Name of the buyer.                           | Update buyer details in your system and resubmit.                                                                                                                                                                          |
| **Provide complete name and address of buyer** | Missing buyer's full name or address.                                   | Ensure full name and buyer's "zip-code" are captured and updated.                                                                                                                                                          |
| **Provide PAN and DOB of buyer**               | There is a potential AML / sanction screening match on the buyer        | Provide PAN (Permanent Account Number) and Date of Birth of the buyer                                                                                                                                                      |
| **Non-Individual cases cannot be processed**   | Transactions involving entities other than individuals are not allowed. | B2B transactions are not enabled for the MID. Contact your Account Manager to enable the same & get the settlements completed.                                                                                             |
| **AMLOCK match found and cannot be processed** | Buyer is a potential sanction entity, transaction cannot be processed.  | Issue a refund for these transactions via dashboard or API.                                                                                                                                                                |

### Key Tips for Merchants

* Always ensure **buyer details** (name, address, PAN, DOB) are accurate before initiating settlements.
* Keep **invoice numbers** ready and update them promptly.
* Monitor the **PayU dashboard** for any "Needs Response" alerts.
* Act within the **7-day window** to avoid delays or expired deadlines.

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

**Environment**

| Environment | URL                                                | Method |
| :---------- | :------------------------------------------------- | :----- |
| Production  | `https://oneapi.payu.in/opgsp/getOnHoldTxnDetails` | GET    |

<Accordion title="Request headers" icon="fa-heading">
  | Parameter                      | Description                                 | Example                                                             |
  | :----------------------------- | :------------------------------------------ | :------------------------------------------------------------------ |
  | mid<br />`mandatory`           | `String` - Merchant ID of the merchant      | 8763182                                                             |
  | Authorization<br />`mandatory` | `String` - HMAC SHA512 authorization header | Refer to  [Authorization field format](#authorization-field-format) |
  | Date<br />`mandatory`          | `String` - Current UTC date in HTTP format  | Wed, 28 Jun 2023 11:25:19 GMT                                       |

  ### Authorization field format

  The **Authorization** field format is similar to the following example:

  ```java
  hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="
  ```

  Where, the fields in this example are:

  * **username**: The merchant key of the merchant.
  * **algorithm**: This must have the value as hmac-sha256 that is used for this API.
  * **headers**: This must have the value as date digest.
  * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
    * **signing\_string**: It must be in the following format. Here, the dateVale and digestValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT\ndigest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="

  ```
  "date: {dateValue}"+"\\n"+"digest: {digestValue}"
    - **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.
  ```

  The following sample Java code contains the logic used to encrypt as described in the above table:

  ```java
  import com.google.gson.Gson;
  import com.google.gson.JsonObject;
  import org.apache.commons.codec.binary.Base64;
  import org.joda.time.DateTime;
  import org.joda.time.format.DateTimeFormat;

  import javax.crypto.Mac;
  import javax.crypto.spec.SecretKeySpec;
  import java.security.InvalidKeyException;
  import java.security.MessageDigest;
  import java.security.NoSuchAlgorithmException;

  public class HmacAuth {

      public static String getSha256(String input) {
          try {
              MessageDigest md = MessageDigest.getInstance("SHA-256");
              byte[] digest = md.digest(input.getBytes());
              return Base64.encodeBase64String(digest);
          } catch (NoSuchAlgorithmException ignored) {}
          return null;
      }

      public static JsonObject getRequestBody(){
          JsonObject requestJson = new JsonObject();
          requestJson.addProperty("firstname","John");
          requestJson.addProperty("lastname","Doe");
          return requestJson;
      }

      public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
          String key = "smsplus";
          String secret = "admin";
          Gson gson = new Gson();
          String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
          System.out.println(date);
          JsonObject requestJson = getRequestBody();
          String digest = getSha256(gson.toJson(requestJson));
          System.out.println(digest);
          String signingString = new StringBuilder()
              .append("date: " + date)
              .append("\ndigest: " + digest).toString();
          Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
          SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
          sha256_HMAC.init(secret_key);
          String signature = Base64.encodeBase64String(sha256_HMAC.doFinal(signingString.getBytes()));
          String authorization = new StringBuilder()
              .append("hmac username=\"")
              .append(key)
              .append("\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"")
              .append(signature)
              .append("\"").toString();
          System.out.println(authorization);
      }
  }
  ```

  The sample header is similar to the following:

  > 📘 **Note:**
  >
  > You need to include the current date and time in the **Date** field of the header.

  ```java
  'Date: Tue, 09 Aug 2022 12:14:51 GMT'
  'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0= '
  'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=""'
  ```
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
  | Parameter                      | Description                                 | Example                                                            |
  | :----------------------------- | :------------------------------------------ | :----------------------------------------------------------------- |
  | mid<br />`mandatory`           | `String` - Merchant ID of the merchant      | 180012                                                             |
  | accept<br />`mandatory`        | `String` - Type of JSON required in the API | application/json                                                   |
  | Content-Type<br />`mandatory`  | `String` - Content type of the request body | application/json                                                   |
  | Authorization<br />`mandatory` | `String` - HMAC SHA512 authorization header | Refer to [Authorization field format](#authorization-field-format) |
  | Date<br />`mandatory`          | `String` - Current UTC date in HTTP format  | Wed, 28 Jun 2023 11:25:19 GMT                                      |

  ### Authorization field format

  The **Authorization** field format is similar to the following example:

  ```java
  hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="CkGfgbho69uTMMOGU0mHWf+1CUAlIp3AjvsON9n9/E4="
  ```

  Where, the fields in this example are:

  * **username**: The merchant key of the merchant.
  * **algorithm**: This must have the value as hmac-sha256 that is used for this API.
  * **headers**: This must have the value as date digest.
  * **signature**: This must contain the hmacsha256 of (signing\_string, merchant\_secret), where:
    * **signing\_string**: It must be in the following format. Here, the dateVale and digestValue is the same values in the fields listed in this table For example, "date: Thu, 17 Feb 2022 08:17:59 GMT\ndigest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0="

  ```
  "date: {dateValue}"+"\\n"+"digest: {digestValue}"
    - **merchant_secret**: The merchant Salt of the merchant. For more information on getting the merchant Salt, refer to Generate Merchant Key and Salt.
  ```

  The following sample Java code contains the logic used to encrypt as described in the above table:

  ```java
  import com.google.gson.Gson;
  import com.google.gson.JsonObject;
  import org.apache.commons.codec.binary.Base64;
  import org.joda.time.DateTime;
  import org.joda.time.format.DateTimeFormat;

  import javax.crypto.Mac;
  import javax.crypto.spec.SecretKeySpec;
  import java.security.InvalidKeyException;
  import java.security.MessageDigest;
  import java.security.NoSuchAlgorithmException;

  public class HmacAuth {

      public static String getSha256(String input) {
          try {
              MessageDigest md = MessageDigest.getInstance("SHA-256");
              byte[] digest = md.digest(input.getBytes());
              return Base64.encodeBase64String(digest);
          } catch (NoSuchAlgorithmException ignored) {}
          return null;
      }

      public static JsonObject getRequestBody(){
          JsonObject requestJson = new JsonObject();
          requestJson.addProperty("firstname","John");
          requestJson.addProperty("lastname","Doe");
          return requestJson;
      }

      public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
          String key = "smsplus";
          String secret = "admin";
          Gson gson = new Gson();
          String date = DateTimeFormat.forPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'").withZoneUTC().print(new DateTime());
          System.out.println(date);
          JsonObject requestJson = getRequestBody();
          String digest = getSha256(gson.toJson(requestJson));
          System.out.println(digest);
          String signingString = new StringBuilder()
              .append("date: " + date)
              .append("\ndigest: " + digest).toString();
          Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
          SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
          sha256_HMAC.init(secret_key);
          String signature = Base64.encodeBase64String(sha256_HMAC.doFinal(signingString.getBytes()));
          String authorization = new StringBuilder()
              .append("hmac username=\"")
              .append(key)
              .append("\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"")
              .append(signature)
              .append("\"").toString();
          System.out.println(authorization);
      }
  }
  ```

  The sample header is similar to the following:

  > 📘 **Note:**
  >
  > You need to include the current date and time in the **Date** field of the header.

  ````java
  'Date: Tue, 09 Aug 2022 12:14:51 GMT'
  'Digest: vpGay5D/dmfoDupALPplYGucJAln9gS29g5Orn+8TC0= '
  'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="zGmP5Zeqm1pxNa+d68DWfQFXhxoqf3st353SkYvX8HI=""'

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
  ````

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
