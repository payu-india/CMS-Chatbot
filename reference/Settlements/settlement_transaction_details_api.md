---
title: Settlement Transaction Details API
api:
  file: updated_settlement_devguide_api_postman_collection_v1.json
  operationId: get_settlement-transactiondetails
hidden: true
---
This API is retrieve detailed information about a specific transaction using the merchant transaction ID. This API provides comprehensive transaction data including status, amount, settlement details, and associated metadata.

<Callout icon="📘" theme="info">
  **Note**: This API uses Bearer token for authentication and Bearer token must be generated using **Get Access Token**API. For more information, refer to [Get Access Token ](ref:get-token-api-for-general-apis)API.
</Callout>

### Environment

|                        |                                                                                                                |
| :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://apitest.payu.in/settlement/transactionDetails](https://apitest.payu.in/settlement/transactionDetails) |
| Production Environment | [https://info.payu.in/settlement/transactionDetails](https://info.payu.in/settlement/transactionDetails)       |

**HTTP Method**: POST

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location 'http://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=W49OV6KQXR4H' \
  --header 'mid: 180012'
  --header 'Authorization: Bearer <token>'
  ```
  ```python
  import requests
  import json

  url = "https://apitest.payu.in/settlement/transactionDetails"
  headers = {
      'Authorization': 'Bearer <your_token>',
      'mid': '<your_merchant_id>',
      'Accept': 'application/json'
  }
  params = {
      'merchantTransactionId': 'TXN123456789'
  }

  try:
      response = requests.get(url, headers=headers, params=params)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          var client = new HttpClient();
          var url = "https://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=TXN123456789";
          
          client.DefaultRequestHeaders.Add("Authorization", "Bearer <your_token>");
          client.DefaultRequestHeaders.Add("mid", "<your_merchant_id>");
          client.DefaultRequestHeaders.Add("Accept", "application/json");
          
          try
          {
              var response = await client.GetAsync(url);
              var content = await response.Content.ReadAsStringAsync();
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {content}");
          }
          catch (Exception e)
          {
              Console.WriteLine($"Error: {e.Message}");
          }
      }
  }
  ```
  ```javascript
  async function getTransactionDetails() {
      const url = "https://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=TXN123456789";
      
      try {
          const response = await fetch(url, {
              method: 'GET',
              headers: {
                  'Authorization': 'Bearer <your_token>',
                  'mid': '<your_merchant_id>',
                  'Accept': 'application/json'
              }
          });
          
          const data = await response.text();
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${data}`);
      } catch (error) {
          console.error(`Error: ${error.message}`);
      }
  }

  getTransactionDetails();
  ```
  ```java
  import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;

  public class TransactionDetailsAPI {
      public static void main(String[] args) {
          try {
              String urlString = "https://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=TXN123456789";
              URL url = new URL(urlString);
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              connection.setRequestMethod("GET");
              connection.setRequestProperty("Authorization", "Bearer <your_token>");
              connection.setRequestProperty("mid", "<your_merchant_id>");
              connection.setRequestProperty("Accept", "application/json");
              
              int statusCode = connection.getResponseCode();
              BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
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
  $url = "https://apitest.payu.in/settlement/transactionDetails?merchantTransactionId=TXN123456789";

  $headers = [
      'Authorization: Bearer <your_token>',
      'mid: <your_merchant_id>',
      'Accept: application/json'
  ];

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

  if (curl_errno($ch)) {
      echo 'Error: ' . curl_error($ch);
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response;
  }

  curl_close($ch);
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ### Success Scenarios

  #### Capture Only

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      }
    ]
  }
  ```

  #### Capture + Refund + Chargeback

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "refund",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargeback",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      }
    ]
  }
  ```

  #### Capture + Chargeback + Chargeback Reversal

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": [
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "capture",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargeback",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": -8.0
      },
      {
        "merchantId": 180012,
        "merchantTransactionId": "W49OV6KQXR4H",
        "payuId": "943323893640",
        "transactionType": "chargebackreversal",
        "settlementStatus": "Settled",
        "settlementUTR": "TESTUTR001",
        "settlementDate": "2025-12-10T15:58:43",
        "settlementId": "180012202512101738",
        "settlementAmount": 8.0
      }
    ]
  }
  ```

  #### Empty Response (No Settlement Records)

  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": []
  }
  ```

  ### Failure scenario

  | Code  | Status   | Meaning                       |
  | ----- | -------- | ----------------------------- |
  | 4000  | Failure  | Invalid request parameters    |
  | 4001  | Failure  | Unauthorized / access denied  |
  | 500   | Failure  | Internal server error         |
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Description                                                                                                                                      |
  | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
  | status    | Response status and it returns either 1 or 0, where 1=Success and 0=Failure.                                                                     |
  | msg       | Response message                                                                                                                                 |
  | result    | Main response data container in a JSON format. For more information, refer to [result JSON Fields Description](#result-json-fields-descriptions) |

  ## result JSON Fields Descriptions

  | Parameter             | Description                                                                                                                                                                                      |
  | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | merchantId            | **Merchant identifier** assigned by PayU to uniquely identify the merchant account. This is the same ID used for authentication and API access.                                                  |
  | merchantTransactionId | **Merchant's unique transaction reference** provided during the original payment request. This is the merchant-generated identifier used to track the transaction in their system.               |
  | payuId                | **PayU's internal unique transaction identifier**. This is generated by PayU for every transaction and can be used for future transaction inquiries, refunds, or support requests.               |
  | transactionType       | **Type of transaction action** processed. Common values include: `capture` (successful payment), `refund`, `chargeback`, `adjustment`, `cancel`, etc.                                            |
  | settlementStatus      | **Current settlement status** of the transaction. Possible values: `Settled` (amount transferred to merchant), `Pending` (awaiting settlement), `On Hold`, `Failed`, etc.                        |
  | settlementUTR         | **Unique Transaction Reference (UTR)** number generated by the bank for the settlement transfer. This is the bank reference for the actual money transfer to the merchant's account.             |
  | settlementDate        | **Date and time when the settlement was completed**. Format: `YYYY-MM-DDTHH:MM:SS`. Represents when the funds were actually transferred to the merchant's bank account.                          |
  | settlementId          | **PayU's internal settlement batch identifier**. This groups multiple transactions that were settled together in the same batch. Format typically includes merchant ID + date + sequence number. |
  | settlementAmount      | **Final amount settled to the merchant** after deducting all applicable fees, taxes, and adjustments. This is the net amount that was actually transferred to the merchant's account.            |
</Accordion>

## Request Parameters

<Callout icon="📘" theme="info">
  **Note**: This API uses Bearer token for authentication and Bearer token must be generated using **Get Access Token**API. For more information, refer to [Get Access Token ](ref:get-token-api-for-general-apis)API.
</Callout>
