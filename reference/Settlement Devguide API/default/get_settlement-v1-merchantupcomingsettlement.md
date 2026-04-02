---
title: Merchant Upcoming And Pending Settlement API
api:
  file: updated_settlement_devguide_api_postman_collection_v1.json
  operationId: get_settlement-v1-merchantupcomingsettlement
hidden: true
---
Retrieve information about upcoming and pending settlements for a merchant. This API provides visibility into future settlements, helping merchants with cash flow planning and financial forecasting.

**Environment**

|                        |                                                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | https://test.payu.in/settlement/v1/merchantUpcomingSettlement                                                                  |
| Production Environment | [https://info.payu.in/settlement/v1/merchantUpcomingSettlement](https://info.payu.in/settlement/v1/merchantUpcomingSettlement) |

<Accordion title="Sample Request" icon="fa-code">
  ```python
  import requests

  url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement"
  headers = {
      'mid': '<your_merchant_id>',
      'Accept': 'application/json'
  }

  try:
      response = requests.get(url, headers=headers)
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
          var url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
          
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
  async function getUpcomingSettlements() {
      const url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
      
      try {
          const response = await fetch(url, {
              method: 'GET',
              headers: {
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

  getUpcomingSettlements();
  ```
  ```java
  import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.net.HttpURLConnection;
  import java.net.URL;

  public class UpcomingSettlementAPI {
      public static void main(String[] args) {
          try {
              String urlString = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
              URL url = new URL(urlString);
              HttpURLConnection connection = (HttpURLConnection) url.openConnection();
              
              connection.setRequestMethod("GET");
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
  $url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";

  $headers = [
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

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
      "status": 1,
      "msg": "Upcoming settlements retrieved successfully",
      "result": {
          "upcomingSettlements": [
              {
                  "expectedSettlementDate": "2023-06-30",
                  "expectedAmount": "25000.00",
                  "transactionCount": 50,
                  "settlementCycle": "T+2",
                  "transactionDateRange": {
                      "from": "2023-06-28",
                      "to": "2023-06-28"
                  },
                  "estimatedFees": "500.00",
                  "estimatedTax": "90.00",
                  "netExpectedAmount": "24410.00"
              },
              {
                  "expectedSettlementDate": "2023-07-01",
                  "expectedAmount": "18500.00",
                  "transactionCount": 37,
                  "settlementCycle": "T+2",
                  "transactionDateRange": {
                      "from": "2023-06-29",
                      "to": "2023-06-29"
                  },
                  "estimatedFees": "370.00",
                  "estimatedTax": "66.60",
                  "netExpectedAmount": "18063.40"
              }
          ],
          "pendingSettlements": [
              {
                  "originalSettlementDate": "2023-06-29",
                  "transactionDate": "2023-06-27",
                  "pendingAmount": "12000.00",
                  "reason": "Bank holiday",
                  "reasonCode": "BANK_HOLIDAY",
                  "expectedClearanceDate": "2023-07-03",
                  "transactionCount": 24,
                  "estimatedFees": "240.00",
                  "estimatedTax": "43.20",
                  "netPendingAmount": "11716.80"
              }
          ],
          "summary": {
              "totalUpcomingAmount": "43500.00",
              "totalPendingAmount": "12000.00",
              "totalExpectedNet": "42473.80",
              "nextSettlementDate": "2023-06-30"
          }
      }
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Type    | Description                                |
  | --------- | ------- | ------------------------------------------ |
  | status    | Integer | Response status (1 = success, 0 = failure) |
  | msg       | String  | Response message                           |
  | result    | Object  | Main response data container               |

  ### result JSON Field Descriptions

  | Parameter                                        | Type    | Description                                                     |
  | ------------------------------------------------ | ------- | --------------------------------------------------------------- |
  | upcomingSettlements                              | Array   | Array of upcoming settlement schedules                          |
  | upcomingSettlements\[].expectedSettlementDate    | String  | Expected date for settlement (YYYY-MM-DD)                       |
  | upcomingSettlements\[].expectedAmount            | String  | Expected gross settlement amount                                |
  | upcomingSettlements\[].transactionCount          | Integer | Number of transactions to be settled                            |
  | upcomingSettlements\[].settlementCycle           | String  | Settlement cycle (T+1, T+2, etc.)                               |
  | upcomingSettlements\[].transactionDateRange      | Object  | Date range of transactions included                             |
  | upcomingSettlements\[].transactionDateRange.from | String  | Start date of transaction range (YYYY-MM-DD)                    |
  | upcomingSettlements\[].transactionDateRange.to   | String  | End date of transaction range (YYYY-MM-DD)                      |
  | upcomingSettlements\[].estimatedFees             | String  | Estimated processing fees to be deducted                        |
  | upcomingSettlements\[].estimatedTax              | String  | Estimated tax on fees                                           |
  | upcomingSettlements\[].netExpectedAmount         | String  | Expected net amount after fees and tax                          |
  | pendingSettlements                               | Array   | Array of delayed/pending settlements                            |
  | pendingSettlements\[].originalSettlementDate     | String  | Originally scheduled settlement date                            |
  | pendingSettlements\[].transactionDate            | String  | Date of transactions that are pending settlement                |
  | pendingSettlements\[].pendingAmount              | String  | Gross amount pending settlement                                 |
  | pendingSettlements\[].reason                     | String  | Human-readable reason for delay                                 |
  | pendingSettlements\[].reasonCode                 | String  | System code for delay reason (BANK\_HOLIDAY, TECH\_ISSUE, etc.) |
  | pendingSettlements\[].expectedClearanceDate      | String  | Expected date when settlement will be processed                 |
  | pendingSettlements\[].transactionCount           | Integer | Number of transactions pending settlement                       |
  | pendingSettlements\[].estimatedFees              | String  | Estimated fees for pending transactions                         |
  | pendingSettlements\[].estimatedTax               | String  | Estimated tax on fees for pending transactions                  |
  | pendingSettlements\[].netPendingAmount           | String  | Expected net amount for pending settlement                      |
  | summary                                          | Object  | Overall summary of upcoming and pending settlements             |
  | summary.totalUpcomingAmount                      | String  | Total gross amount in upcoming settlements                      |
  | summary.totalPendingAmount                       | String  | Total gross amount in pending settlements                       |
  | summary.totalExpectedNet                         | String  | Total expected net amount after all deductions                  |
  | summary.nextSettlementDate                       | String  | Date of the next scheduled settlement                           |
</Accordion>
