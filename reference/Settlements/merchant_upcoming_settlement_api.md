---
title: ' Merchant Upcoming and Pending Settlement API'
deprecated: false
hidden: true
metadata:
  robots: index
---
Retrieve information about upcoming and pending settlements for a merchant. This API provides visibility into future settlements, helping merchants with cash flow planning and financial forecasting.

**Environment**

|                        |                                                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/settlement/v1/merchantUpcomingSettlement](https://test.payu.in/settlement/v1/merchantUpcomingSettlement) |
| Production Environment | [https://info.payu.in/settlement/v1/merchantUpcomingSettlement](https://info.payu.in/settlement/v1/merchantUpcomingSettlement) |

**HTTP Method**: POST

<Accordion title="Request Parameters" icon="fa-table">
  ### Request Header

  <HeaderAuthentication />

  ### Other Header Parameters

  | Parameter                        | Description                                                                      | Example                       |
  | -------------------------------- | -------------------------------------------------------------------------------- | ----------------------------- |
  | mid<br /><code>mandatory</code>  | <code>String</code> Merchant identifier that the integration was registered with | \<MerchantId>                 |
  | Date<br /><code>mandatory</code> | <code>String</code> Request date header in RFC-1123 format                       | Tue, 07 Apr 2026 06:14:56 GMT |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/settlement/v1/merchantUpcomingSettlement' \
  --header 'Authorization: hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"' \
  --header 'mid: <MerchantId>' \
  --header 'Date: Tue, 07 Apr 2026 06:14:56 GMT’
  ```
  ```python
  import requests

  url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement"
  headers = {
      "Authorization": 'hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"',
      "mid": "<MerchantId>",
      "Date": "Tue, 07 Apr 2026 06:14:56 GMT"
  }

  response = requests.get(url, headers=headers)
  print(f"Status Code: {response.status_code}")
  print(f"Response: {response.text}")
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
          
          string url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
          
          client.DefaultRequestHeaders.Add("Authorization", "hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"");
          client.DefaultRequestHeaders.Add("mid", "<MerchantId>");
          client.DefaultRequestHeaders.Add("Date", "Tue, 07 Apr 2026 06:14:56 GMT");
          
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
  async function makeRequest() {
      const url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
      
      const headers = {
          "Authorization": 'hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"',
          "mid": "<MerchantId>",
          "Date": "Tue, 07 Apr 2026 06:14:56 GMT"
      };
      
      try {
          const response = await fetch(url, {
              method: "GET",
              headers: headers
          });
          
          const responseText = await response.text();
          
          console.log(`Status Code: ${response.status}`);
          console.log(`Response: ${responseText}`);
      } catch (error) {
          console.error("Request error:", error);
      }
  }

  makeRequest();
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;

  public class PayURequest {
      public static void main(String[] args) {
          String url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("Authorization", "hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"")
                  .header("mid", "<MerchantId>")
                  .header("Date", "Tue, 07 Apr 2026 06:14:56 GMT")
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
  $url = "https://info.payu.in/settlement/v1/merchantUpcomingSettlement";

  $headers = array(
      "Authorization: hmac username="Fa2IFz", algorithm="sha512", headers="date", signature="ca98fa63b2780d2306f721fde8c5667ec11ca7821396c54bbef18681a227f2751b3a80f8254696baae3917bb478c29d60b613c25a95469bb5942cabecc2fe949"",
      "mid: <MerchantId>",
      "Date: Tue, 07 Apr 2026 06:14:56 GMT"
  );

  $curl = curl_init();

  curl_setopt_array($curl, array(
      CURLOPT_URL => $url,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => $headers,
      CURLOPT_CUSTOMREQUEST => "GET"
  ));

  $response = curl_exec($curl);
  $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

  if (curl_errno($curl)) {
      echo "cURL Error: " . curl_error($curl);
  } else {
      echo "Status Code: " . $httpCode . "
  ";
      echo "Response: " . $response . "
  ";
  }

  curl_close($curl);
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
        "lastSettledAmount": 2197.19,
        "lastSettlementTime": "2026-04-06 14:22:12",
        "upcomingSettlementAmount": 235129.81,
        "upcomingSettlementTime": "2026-04-08 09:15:00",
        "totalSettlementPendingAmount": 73224295.78,
        "currencyType": "USD",
        "merchantId": 8515874,
        "pendingSettlementBreakdown": {
            "saleAmount": 77328963.90,
            "adjustmentAmount": 0.00,
            "refundAmount": -975745.51,
            "chargebackAmount": -120622.04,
            "refundReversalAmount": 0.00,
            "chargebackReversalAmount": 0.00,
            "serviceFee": -2778968.71,
            "serviceTax": -226059.93,
            "convenienceFee": 0.00,
            "convenienceTax": 0.00,
            "additionalServiceFee": -158.58,
            "additionalServiceTax": -28.54,
            "txnCount": 53057
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
  | `serviceFee`               | Service fees charged                                          |
  | `serviceTax`               | Tax on service fee                                            |
  | `convenienceFee`           | Convenience fees charged to customer (affect settlement)      |
  | `convenienceTax`           | Tax on convenience fee                                        |
  | `additionalServiceFee`     | Any additional service fees                                   |
  | `additionalServiceTax`     | Tax on additional service fee                                 |
  | `txnCount`                 | Number of transactions contributing to the breakdown          |
</Accordion>
