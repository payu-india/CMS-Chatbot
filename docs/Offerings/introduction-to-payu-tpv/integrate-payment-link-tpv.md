---
title: '[OLD]Integrate Payment Link TPV'
deprecated: false
hidden: true
metadata:
  robots: index
---
This section describes the steps to integrate Payment Link TPV (Third Party Verification) - from payment link creation to payment processing.

<Callout icon="📘" theme="info">
  **Note**: Ensure Payment Link with TPV is activated for your account. Contact your PayU account manager if this configuration is not active.
</Callout>

<Accordion title="Customer Journey" icon="fa-info-circle">
  **Step 1**:  Merchant creates a payment link with TPV details.

  **Step 2**: The API returns a short URL (e.g. [https://v.payu.in/PAYUMN/fIishvrkWhFD](https://v.payu.in/PAYUMN/fIishvrkWhFD)).

  **Step 3**: Customer opens this link, fills relevant details and clicks make payment (similar to the following screenshot)

  <Image align="center" src="https://files.readme.io/117c859ee1b0d4cd3c2f25635ee1d14eba547e86da0a839f3e197669b8ea9c77-tpv_payment_link_customer_link.png" width="450px" />

  **Step 4**: Customer is redirected to checkout page.

  <Image align="center" src="https://files.readme.io/82462bb510803c6a5bc11d082578828e39ade3175773cf6835634822f4ccbff6-tpv_payment_link_checkout_page.png" width="450px" />

  **Step 5**: Merchant can view the transaction status in the **PayU Dashboard** > **Payment Links** tab.
</Accordion>

<Cards columns={3}>
  <Card title="1. Create Payment Link" href="#step-1-create-payment-link">
    Create a payment link with beneficiary account details for TPV verification.

    <br />
  </Card>

  <Card title="2. Check Response from PayU" href="#step-2-check-response-from-payu">
    Check and handle the response received from PayU after payment processing.

    <br />
  </Card>

  <Card title="3. Verify the Payment" href="#step-5-verify-the-payment">
    Verify the payment status using webhooks or Verify Payments API.

    <br />
  </Card>
</Cards>

## Step 1: Create Payment Link

Create a payment link with beneficiary account details using the Create Payment Link API.

<Accordion title="Environment" icon="fa-globe">
  | Environment | URL                                       |
  | ----------- | ----------------------------------------- |
  | Test        | `https://test.payu.in/paymentlink/create` |
  | Production  | `https://info.payu.in/paymentlink/create` |
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                           | Description                                                                   | Example                |
  | ----------------------------------- | ----------------------------------------------------------------------------- | ---------------------- |
  | amount<br />`mandatory`             | `Decimal`<br />The payment amount.                                            | `5000.00`              |
  | maxPaymentsAllowed<br />`mandatory` | `Integer`<br />Must be 1 for TPV flow (single payment only).                  | `1`                    |
  | invoiceNumber<br />`mandatory`      | `String`<br />Unique invoice number for the payment link.                     | `INV123456789012`      |
  | description<br />`optional`         | `String`<br />Description of the payment.                                     | `Payment for services` |
  | customerName<br />`optional`        | `String`<br />Customer's name.                                                | `John Doe`             |
  | customerEmail<br />`optional`       | `String`<br />Customer's email address.                                       | `john.doe@example.com` |
  | customerPhone<br />`optional`       | `String`<br />Customer's phone number.                                        | `9876543210`           |
  | maxPaymentsAllowed<br />`optional`  | `String`<br />This parameter must contain maximum number of payments allowed. | `1`                    |

  \| beneficiarydetail<br />`optional`   | `Object`<br />Object containing beneficiary account details for TPV. | Refer to  [beneficiarydetail Object Parameters](#beneficiarydetail-object-parameters)      |
  \| source<br />`optional`              | `String`<br />Source of the payment link creation.                   | `API`                  |

  <Accordion title="beneficiarydetail Object Parameters" icon="fa-code">
    | Parameter                                 | Description                                                                   | Example                          |
    | ----------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------- |
    | beneficiaryAccountNumber<br />`mandatory` | `List<String>`<br />Array of beneficiary account numbers. Maximum 4 accounts. | `["917732227242", "72522762"]`   |
    | ifscCode<br />`mandatory`                 | `List<String>`<br />Array of IFSC codes corresponding to each account number. | `["SBIN0007001", "HDFC0001234"]` |
  </Accordion>
</Accordion>

<Callout icon="📘" theme="info">
  **Notes:**

  * Account numbers and IFSC codes in the `beneficiarydetail` object must have equal count
  * `maxPaymentsAllowed` must be 1 (single payment only)
</Callout>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.payu.in/paymentlink/create' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <access_token>' \
  --data '{
      "amount": 5000.00,
      "maxPaymentsAllowed": 1,
      "invoiceNumber": "INV123456789012",
      "description": "Payment for services",
      "customerName": "John Doe",
      "customerEmail": "john.doe@example.com",
      "customerPhone": "9876543210",
      "beneficiarydetail": {
          "beneficiaryAccountNumber": ["917732227242", "72522762"],
          "ifscCode": ["SBIN0007001", "HDFC0001234"]
      },
      "source": "API"
  }'
  ```
  ```python
  import requests
  import json

  url = "https://test.payu.in/paymentlink/create"

  payload = {
      "amount": 5000.00,
      "maxPaymentsAllowed": 1,
      "invoiceNumber": "INV123456789012",
      "description": "Payment for services",
      "customerName": "John Doe",
      "customerEmail": "john.doe@example.com",
      "customerPhone": "9876543210",
      "beneficiarydetail": {
          "beneficiaryAccountNumber": ["917732227242", "72522762"],
          "ifscCode": ["SBIN0007001", "HDFC0001234"]
      },
      "source": "API"
  }

  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer <access_token>"
  }

  response = requests.post(url, json=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var payload = @"{
              ""amount"": 5000.00,
              ""maxPaymentsAllowed"": 1,
              ""invoiceNumber"": ""INV123456789012"",
              ""description"": ""Payment for services"",
              ""customerName"": ""John Doe"",
              ""customerEmail"": ""john.doe@example.com"",
              ""customerPhone"": ""9876543210"",
              ""beneficiarydetail"": {
                  ""beneficiaryAccountNumber"": [""917732227242"", ""72522762""],
                  ""ifscCode"": [""SBIN0007001"", ""HDFC0001234""]
              },
              ""source"": ""API""
          }";
          
          var content = new StringContent(payload, Encoding.UTF8, "application/json");
          client.DefaultRequestHeaders.Add("Authorization", "Bearer <access_token>");
          
          var response = await client.PostAsync("https://test.payu.in/paymentlink/create", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const createPaymentLinkTPV = async () => {
      const url = "https://test.payu.in/paymentlink/create";
      
      const payload = {
          amount: 5000.00,
          maxPaymentsAllowed: 1,
          invoiceNumber: "INV123456789012",
          description: "Payment for services",
          customerName: "John Doe",
          customerEmail: "john.doe@example.com",
          customerPhone: "9876543210",
          beneficiarydetail: {
              beneficiaryAccountNumber: ["917732227242", "72522762"],
              ifscCode: ["SBIN0007001", "HDFC0001234"]
          },
          source: "API"
      };
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer <access_token>"
          },
          body: JSON.stringify(payload)
      });
      
      const data = await response.json();
      console.log(data);
  };

  createPaymentLinkTPV();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class CreatePaymentLinkTPV {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/paymentlink/create";
          
          String payload = "{"
              + "\"amount\": 5000.00,"
              + "\"maxPaymentsAllowed\": 1,"
              + "\"invoiceNumber\": \"INV123456789012\","
              + "\"description\": \"Payment for services\","
              + "\"customerName\": \"John Doe\","
              + "\"customerEmail\": \"john.doe@example.com\","
              + "\"customerPhone\": \"9876543210\","
              + "\"beneficiarydetail\": {"
              + "\"beneficiaryAccountNumber\": [\"917732227242\", \"72522762\"],"
              + "\"ifscCode\": [\"SBIN0007001\", \"HDFC0001234\"]"
              + "},"
              + "\"source\": \"API\""
              + "}";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/json");
          conn.setRequestProperty("Authorization", "Bearer <access_token>");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(payload.getBytes(StandardCharsets.UTF_8));
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
  $url = "https://test.payu.in/paymentlink/create";

  $payload = array(
      "amount" => 5000.00,
      "maxPaymentsAllowed" => 1,
      "invoiceNumber" => "INV123456789012",
      "description" => "Payment for services",
      "customerName" => "John Doe",
      "customerEmail" => "john.doe@example.com",
      "customerPhone" => "9876543210",
      "beneficiarydetail" => array(
          "beneficiaryAccountNumber" => array("917732227242", "72522762"),
          "ifscCode" => array("SBIN0007001", "HDFC0001234")
      ),
      "source" => "API"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "Content-Type: application/json",
      "Authorization: Bearer <access_token>"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

## Step 2: Check Response from PayU

The Payment Link is Generated and you must share it with your customer.

<Accordion title="Sample Response" icon="fa-check">
  ```json
  {
  "status": 0,
  "message": "PaymentLink generated",
  "result": {
    "subAmount": 10,
    "tax": 0,
    "shippingCharge": 0,
    "totalAmount": 10,
    "invoiceNumber": "INV123456789012",
    "paymentLink": "https://v.payu.in/PAYUMN/fIishvrkWhFD",
    "description": "Payment for services",
    "active": true,
    "isPartialPaymentAllowed": false,
    "expiryDate": "2026-12-16 13:30:19",
    "udf": {
      "udf1": null,
      "udf2": null,
      "udf3": null,
      "udf4": null,
      "udf5": null
    },
    "address": {
      "line1": null,
      "line2": null,
      "city": null,
      "state": null,
      "country": null,
      "zipCode": null
    },
    "emailStatus": "not opted",
    "smsStatus": "not opted",
    "currency": "INR",
    "addedOn": "2025-12-16 13:30:19",
    "status": "active",
    "maxPaymentsAllowed": 1,
    "customerName": "testexample.comLine\nLine",
    "customerPhone": "6397510365",
    "customerEmail": "ritwik.singh@payu.in",
    "notes": null,
    "amountCollected": 0,
    "dueAmount": 10,
    "minAmountForCustomer": 1,
    "adjustment": 0,
    "discount": 0,
    "customParams": null,
    "transactionId": null
  },
  "errorCode": null,
  "guid": "4546173a-7432-48e5-9e62-4782a1e48371"
  }
  ```
</Accordion>

## Step 3: Verify the Payment

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

<br />