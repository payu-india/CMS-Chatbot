---
title: Merchant Upcoming and Pending Settlement API
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Merchant Upcoming and Pending Settlement API
excerpt: Retrieve a near real-time settlement balance snapshot for a merchant.
deprecated: false
hidden: false
metadata:
  title: Merchant Upcoming and Pending Settlement API
  description: >-
    Get pending settlement balance, upcoming cycle amount and time, and a
    component-wise breakdown to plan cash flow and operations.
  robots: index
---

Authorized clients can use the **Merchant Upcoming and Pending Settlement API** to retrieve a settlement balance snapshot for a single merchant. The response includes the total amount still to be settled, the amount expected in the next settlement cycle, the next settlement date and time, and a breakdown of the pending settlement amount—so merchants can plan cash flow and operations.

There is no request body for this API.

**Environment**

|                        |                                                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/settlement/v1/merchantUpcomingSettlement](https://test.payu.in/settlement/v1/merchantUpcomingSettlement) |
| Production Environment | [https://info.payu.in/settlement/v1/merchantUpcomingSettlement](https://info.payu.in/settlement/v1/merchantUpcomingSettlement) |

**HTTP Method**: GET

<Accordion title="Request Parameters" icon="fa-table">
  ### Request Header

  <HeaderAuthentication />

  ### Other Header Parameters

  | Parameter                       | Description                                                                                                      | Example |
  | ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------- |
  | mid<br /><code>mandatory</code> | <code>String</code> Merchant identifier that the integration was registered with (the merchant ID in the system). | 100003  |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --request GET \
    --url 'https://test.payu.in/settlement/v1/merchantUpcomingSettlement' \
    --header 'mid: 100003' \
    --header 'Authorization: {{authorization}}' \
    --header 'Date: {{date}}'
  ```
  ```python
  import requests

  url = "https://test.payu.in/settlement/v1/merchantUpcomingSettlement"
  headers = {
      "Authorization": "{{authorization}}",
      "mid": "100003",
      "Date": "{{date}}",
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
      static async Task Main(string[] args)
      {
          using var client = new HttpClient();

          string url = "https://test.payu.in/settlement/v1/merchantUpcomingSettlement";

          client.DefaultRequestHeaders.Add("Authorization", "{{authorization}}");
          client.DefaultRequestHeaders.Add("mid", "100003");
          client.DefaultRequestHeaders.Add("Date", "{{date}}");

          try
          {
              HttpResponseMessage response = await client.GetAsync(url);
              string responseBody = await response.Content.ReadAsStringAsync();

              Console.WriteLine($"Status Code: {(int)response.StatusCode}");
              Console.WriteLine($"Response: {responseBody}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Request error: {e.Message}");
          }
      }
  }
  ```
  ```javascript
  async function getUpcomingSettlement() {
      const url = "https://test.payu.in/settlement/v1/merchantUpcomingSettlement";

      const headers = {
          Authorization: "{{authorization}}",
          mid: "100003",
          Date: "{{date}}",
      };

      try {
          const response = await fetch(url, {
              method: "GET",
              headers: headers,
          });

          const responseText = await response.text();

          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
      } catch (error) {
          console.error("Request error:", error);
      }
  }

  getUpcomingSettlement();
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public class MerchantUpcomingSettlementApi {
      public static void main(String[] args) {
          String url = "https://test.payu.in/settlement/v1/merchantUpcomingSettlement";

          HttpClient client = HttpClient.newHttpClient();

          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Authorization", "{{authorization}}")
                  .header("mid", "100003")
                  .header("Date", "{{date}}")
                  .GET()
                  .build();

          try {
              HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

              System.out.println("Status Code: " + response.statusCode());
              System.out.println("Response: " + response.body());
          } catch (IOException | InterruptedException e) {
              System.err.println("Request error: " + e.getMessage());
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.payu.in/settlement/v1/merchantUpcomingSettlement";

  $headers = [
      "Authorization: {{authorization}}",
      "mid: 100003",
      "Date: {{date}}",
  ];

  $curl = curl_init();

  curl_setopt_array($curl, [
      CURLOPT_URL => $url,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => $headers,
      CURLOPT_CUSTOMREQUEST => "GET",
  ]);

  $response = curl_exec($curl);
  $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

  if (curl_errno($curl)) {
      echo "cURL Error: " . curl_error($curl);
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response;
  }

  curl_close($curl);
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  **Success Scenario**

  Figures in the example below are illustrative.

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
      "totalSettlementPendingAmount": 579.0,
      "currencyType": "INR",
      "merchantId": 100005,
      "pendingSettlementBreakdown": {
        "saleAmount": 2000.0,
        "adjustmentAmount": 100.0,
        "refundAmount": -1500.0,
        "chargebackAmount": 0.0,
        "refundReversalAmount": 50.0,
        "chargebackReversalAmount": 25.0,
        "serviceFee": -30.0,
        "serviceTax": -5.4,
        "convenienceFee": -1.0,
        "convenienceTax": 0.0,
        "additionalServiceFee": -10.0,
        "additionalServiceTax": 0.0,
        "txnCount": 10
      }
    }
  }
  ```

  **Merchant not found**

  Returned when the request uses an invalid `mid` (or when empty `mid` is handled the same way).

  ```json
  {
    "code": "4000",
    "message": "no Merchant found for id: 200 in settlement",
    "status": 1,
    "traceId": "69bce2a7ad788d0baf213c845011e9b8"
  }
  ```

  **Internal server error**

  Returned when an unexpected failure occurs while processing a valid request.

  ```json
  {
    "timestamp": 1773980487215,
    "status": 500,
    "error": "Internal Server Error"
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Type    | Description                                                                                                                                    |
  | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  | code      | String  | Business result code; success is typically `2000`.                                                                                             |
  | message   | String  | Short response text, for example `Success`.                                                                                                    |
  | status    | Integer | Application status: `0` = success, `1` = failure.                                                                                              |
  | result    | Object  | Settlement balance object. For field descriptions, refer to [result JSON Field Descriptions](#result-json-field-descriptions).                  |
  | traceId   | String  | Trace identifier included on some business error responses (for example, merchant not found).                                                  |

  ### result JSON Field Descriptions

  | Field                          | Description                                                                                                                                                                                                                                                                                                          |
  | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `holdSettlementStatus`         | Settlement hold indicator for the merchant. `1` = settlement on hold, `0` = not on hold.                                                                                                                                                                                                                               |
  | `lastSettledAmount`            | Amount settled in the most recent settlement.                                                                                                                                                                                                                                                                          |
  | `lastSettlementTime`           | Timestamp of the last settlement in IST date-time format. May be present for reconciliation.                                                                                                                                                                                                                           |
  | `upcomingSettlementAmount`     | Amount expected to be settled in the next settlement cycle.                                                                                                                                                                                                                                                          |
  | `upcomingSettlementTime`       | Timestamp of the next settlement in IST date-time format (for example, `2026-03-20 12:00:00`).                                                                                                                                                                                                                         |
  | `totalSettlementPendingAmount` | Total amount still to be settled across outstanding settlement entries (overall pending balance).                                                                                                                                                                                                                    |
  | `currencyType`                 | Currency of the amounts (for example, `INR`).                                                                                                                                                                                                                                                                          |
  | `merchantId`                   | Identifier of the merchant for this response.                                                                                                                                                                                                                                                                          |
  | `pendingSettlementBreakdown`   | Component-wise breakdown of the pending settlement amount. Numeric amounts may be `0` or omitted depending on serialization; negative values denote deductions or credits. For field descriptions, refer to [pendingSettlementBreakdown JSON Fields Description](#pendingsettlementbreakdown-json-fields-description). |

  #### pendingSettlementBreakdown JSON Fields Description

  | Field                      | Description                                                   |
  | -------------------------- | ------------------------------------------------------------- |
  | `saleAmount`               | Transactions (sale) amount.                                   |
  | `adjustmentAmount`         | Adjustment amount.                                            |
  | `refundAmount`             | Refund amount.                                                |
  | `chargebackAmount`         | Chargeback amount.                                            |
  | `refundReversalAmount`     | Refund reversal amount.                                       |
  | `chargebackReversalAmount` | Chargeback reversal amount.                                   |
  | `serviceFee`               | Service fee.                                                  |
  | `serviceTax`               | Service tax.                                                  |
  | `convenienceFee`           | Convenience fee.                                              |
  | `convenienceTax`           | Convenience tax.                                              |
  | `additionalServiceFee`     | Additional service fee.                                       |
  | `additionalServiceTax`     | Additional service tax.                                       |
  | `txnCount`                 | Number of transactions contributing to the breakdown.         |

  ### HTTP status summary

  | Situation                              | HTTP | Body shape                                      |
  | -------------------------------------- | ---- | ----------------------------------------------- |
  | Success                                | 200  | `code` `2000`, `result` populated               |
  | Merchant not found / business error    | 200  | `code` `4000`, `status` `1`, optional `traceId` |
  | Other server errors                    | 500  | Default error JSON (`timestamp`, `status`, `error`) |
</Accordion>
