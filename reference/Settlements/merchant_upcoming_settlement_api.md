---
title: '[OLD]Merchant Upcoming and Pending Settlement API'
api:
  file: updated_settlement_devguide_api_postman_collection_v1.json
  operationId: get_settlement-v1-merchantupcomingsettlement
hidden: true
---
Retrieve information about upcoming and pending settlements for a merchant. This API provides visibility into future settlements, helping merchants with cash flow planning and financial forecasting.

**Environment**

|                        |                                                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/settlement/v1/merchantUpcomingSettlement](https://test.payu.in/settlement/v1/merchantUpcomingSettlement) |
| Production Environment | [https://info.payu.in/settlement/v1/merchantUpcomingSettlement](https://info.payu.in/settlement/v1/merchantUpcomingSettlement) |

**HTTP Method**: POST

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --request GET \
     --url https://test.payu.in/settlement/v1/merchantUpcomingSettlement \
     --header 'accept: application/json' \
     --header 'mid: <your_merchant_mid>'
  ```
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
  "code": "2000",
  "message": "Success",
  "status": 0,
  "result": {
  "holdSettlementStatus": 0,
  "lastSettledAmount": 0,
  "upcomingSettlementAmount": 0,
  "upcomingSettlementTime": "2026-03-20 12:00:00",
  "totalSettlementPendingAmount": 579.00,
  "currencyType": "INR",
  "merchantId": 100005,
  "pendingSettlementBreakdown": {
   "saleAmount": 2000.00,
   "adjustmentAmount": 100.00,
   "refundAmount": -1500.00,
   "chargebackAmount": 0.00,
   "refundReversalAmount": 50.00,
   "chargebackReversalAmount": 25.00,
   "serviceFee": -30.00,
   "serviceTax": -5.40,
   "convenienceFee": -1.00,
   "convenienceTax": 0.00,
   "additionalServiceFee": -10.00,
   "additionalServiceTax": 0.00,
   "txnCount": 10
  }
  }
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Type    | Description                                                                                                                                    |
  | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  | status    | Integer | Response status (1 = success, 0 = failure)                                                                                                     |
  | msg       | String  | Response message                                                                                                                               |
  | result    | Object  | Main response data container in JSON format. For more information, refer to  [result JSON Field Descriptions](#result-json-field-descriptions) |

  ### result JSON Field Descriptions

  | Field                          | Description                                                                                                                                                                                                                                                                                                          |
  | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `holdSettlementStatus`         | Indicator whether merchant settlements are on hold. Values: `1` = on hold, `0` = not on hold                                                                                                                                                                                                                         |
  | `lastSettledAmount`            | Monetary amount that was settled in the most recent settlement                                                                                                                                                                                                                                                       |
  | `upcomingSettlementAmount`     | Monetary amount expected to be settled in the next settlement cycle                                                                                                                                                                                                                                                  |
  | `upcomingSettlementTime`       | Timestamp (IST date-time format) of the next scheduled settlement                                                                                                                                                                                                                                                    |
  | `totalSettlementPendingAmount` | Total monetary amount still pending settlement (aggregate outstanding balance)                                                                                                                                                                                                                                       |
  | `currencyType`                 | Currency code for amounts (e.g., "INR")                                                                                                                                                                                                                                                                              |
  | `merchantId`                   | Identifier of the merchant for whom the snapshot is returned                                                                                                                                                                                                                                                         |
  | `pendingSettlementBreakdown`   | JSON Object providing a component-wise breakdown of the pending/upcoming settlement amount. Numeric amounts may be 0 or omitted; negative values denote deductions/credits. For more information, refer to [pendingSettlementBreakdown JSON Fields Description](#pendingSettlementBreakdown-json-fields-description) |

  #### pendingSettlementBreakdown JSON Fields Description

  | Field                      | Description                                                   |
  | -------------------------- | ------------------------------------------------------------- |
  | `saleAmount`               | Total transaction (sales) amount                              |
  | `adjustmentAmount`         | Adjustments applied (positive or negative adjustments)        |
  | `refundAmount`             | Total refunds (usually negative when reducing payable amount) |
  | `chargebackAmount`         | Total chargebacks (reductions due to disputes)                |
  | `refundReversalAmount`     | Amounts from reversed refunds (restored to merchant)          |
  | `chargebackReversalAmount` | Amounts from reversed chargebacks                             |
  | `serviceFee`               | Service fees charged                   |
  | `serviceTax`               | Tax on service fee                                            |
  | `convenienceFee`           | Convenience fees charged to customer (affect settlement)      |
  | `convenienceTax`           | Tax on convenience fee                                        |
  | `additionalServiceFee`     | Any additional service fees                                   |
  | `additionalServiceTax`     | Tax on additional service fee                                 |
  | `txnCount`                 | Number of transactions contributing to the breakdown          |

  ***

  This table structure clearly separates the root-level fields from the nested `pendingSettlementBreakdown` object fields, making it easy to understand the complete response structure. All descriptions are based on the reference document you provided. 📋✨
</Accordion>