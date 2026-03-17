---
title: Verify Payment API
api:
  file: verify_payment.json
  operationId: verifypayment
hidden: false
metadata:
  title: Verify Payment API
  description: >-

    The Verify Payment API provides transaction status information, including
    details such as payment source, card type, and offer availed at cart or
    transaction level. It also includes response parameters like status,
    message, and transaction details in JSON format.
  keywords:
    - verify_payment
    - verify_payment command
    - Verify Payment API
    - Check Transaction Status API
---
The Verify Payment (**verify_payment**) API gives you the status of the transaction. PayU recommends using this API to reconcile with PayU's database after you receive the response, where var1 is your transaction ID.

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```bash
curl --request POST   --url 'https://test.payu.in/merchant/postservice?form=2'   --header 'Content-Type: application/x-www-form-urlencoded'   --data key=JPM7Fg   --data command=verify_payment   --data var1=IhfgcZnXR4o4nB   --data hash=a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9
```
```python
import requests

try:
    url = "https://test.payu.in/merchant/postservice?form=2"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'key': 'JPM7Fg',
        'command': 'verify_payment',
        'var1': 'IhfgcZnXR4o4nB',
        'hash': 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
    }
    
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        try
        {
            using var client = new HttpClient();
            var url = "https://test.payu.in/merchant/postservice?form=2";
            
            var postData = new List<KeyValuePair<string, string>>
            {
                new("key", "JPM7Fg"),
                new("command", "verify_payment"),
                new("var1", "IhfgcZnXR4o4nB"),
                new("hash", "a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9")
            };
            
            var content = new FormUrlEncodedContent(postData);
            content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
            
            var response = await client.PostAsync(url, content);
            var responseContent = await response.Content.ReadAsStringAsync();
            
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

**JavaScript (Async/Await Fetch)**
```javascript
async function makeRequest() {
    try {
        const url = 'https://test.payu.in/merchant/postservice?form=2';
        
        const postData = new URLSearchParams({
            'key': 'JPM7Fg',
            'command': 'verify_payment',
            'var1': 'IhfgcZnXR4o4nB',
            'hash': 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
        });
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: postData
        });
        
        const responseText = await response.text();
        
        console.log(`Status Code: ${response.status}`);
        console.log(`Response: ${responseText}`);
        
    } catch (error) {
        console.error('Error:', error);
    }
}

makeRequest();
```
```java
import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class PaymentVerification {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://test.payu.in/merchant/postservice?form=2");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            connection.setDoOutput(true);
            
            String postData = "key=" + URLEncoder.encode("JPM7Fg", StandardCharsets.UTF_8) +
                            "&command=" + URLEncoder.encode("verify_payment", StandardCharsets.UTF_8) +
                            "&var1=" + URLEncoder.encode("IhfgcZnXR4o4nB", StandardCharsets.UTF_8) +
                            "&hash=" + URLEncoder.encode("a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9", StandardCharsets.UTF_8);
            
            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = postData.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }
            
            int statusCode = connection.getResponseCode();
            System.out.println("Status Code: " + statusCode);
            
            BufferedReader reader;
            if (statusCode >= 200 && statusCode < 300) {
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            } else {
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            }
            
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();
            
            System.out.println("Response: " + response.toString());
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
```php
<?php
$url = 'https://test.payu.in/merchant/postservice?form=2';

$postData = array(
    'key' => 'JPM7Fg',
    'command' => 'verify_payment',
    'var1' => 'IhfgcZnXR4o4nB',
    'hash' => 'a0ae79fdd66c875af6e9b21c4a67f1822deb00f2df5e9f0b1948f3222f536a9bf741b24efbb1874ca0f84f76b036e6c0d641581d0100f7abe4aeed2f3264f5c9'
);

$ch = curl_init();

curl_setopt_array($ch, array(
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query($postData),
    CURLOPT_HTTPHEADER => array(
        'Content-Type: application/x-www-form-urlencoded'
    )
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

if (curl_error($ch)) {
    echo 'Error: ' . curl_error($ch) . "\n";
} else {
    echo "Status Code: " . $httpCode . "\n";
    echo "Response: " . $response . "\n";
}

curl_close($ch);
?>
```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  * If credit card payment is made, the response is similar to the following:

  ```plaintext
  {
  "status":0,
  "msg":"0 out of 1 Transactions Fetched Successfully",
  "transaction_details":
  {
    "IhfgcZnXR4o4nB":
    {
      "mihpayid":"Not Found",
      "status":"Not Found"
    }
  }
  }
  ```

  * Offer availed on cart level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1036-f0cf85f2": {
              "mihpayid": "21564143078",
              "request_id": "",
              "bank_ref_num": "431998369241",
              "amt": "2.00",
              "transaction_amount": "2.00",
              "txnid": "1036-f0cf85f2",
              "additional_charges": "0.00",
              "productinfo": "EXPRESS",
              "firstname": "guest",
              "bankcode": "TEZOMNI",
              "udf1": "Magento2",
              "udf2": "",
              "udf3": "",
              "udf4": "",
              "udf5": "qs8rbc1ng2hmqtakk381en6j2p",
              "field2": "114390824407",
              "field9": "SUCCESS|Completed Using Callback",
              "error_code": "E000",
              "addedon": "2024-11-14 16:06:40",
              "payment_source": "express",
              "card_type": null,
              "error_Message": "NO ERROR",
              "net_amount_debit": 2.00,
              "disc": "0.00",
              "mode": "UPI",
              "PG_TYPE": "UPI-PG",
              "card_no": "",
              "status": "success",
              "unmappedstatus": "captured",
              "Merchant_UTR": null,
              "Settled_At": "0000-00-00 00:00:00",
              "App_Name": "GooglePay",
              "card_token": null,
              "field4": null,
              "offerAvailed": null,
              "cart_details": {
                  "id": "2446425",
                  "payu_id": "21564143078",
                  "total_items": "1",
                  "total_cart_amount": "2.00",
                  "offer_applied": null,
                  "offer_availed": null,
                  "offer_auto_apply": "0",
                  "instant_discount": "0.00",
                  "cashback_discount": "0.00",
                  "total_discount": "0.00",
                  "net_cart_amount": "2.00",
                  "created_at": "2024-11-14 16:06:40",
                  "updated_at": "2024-11-14 16:06:40",
                  "sku_details": [
                      {
                          "id": "3468748",
                          "cart_id": "2446425",
                          "payu_id": "21564143078",
                          "mid": "2",
                          "sku_id": "Sample Sofa Design-Red",
                          "sku_name": "Sample Sofa Designtest?=!name",
                          "amount_per_sku": "2.00",
                          "quantity": "1",
                          "amount_before_discount": "2.00",
                          "discount": "0.00",
                          "amount_after_discount": "2.00",
                          "offer_applied": null,
                          "offer_availed": null,
                          "offer_status": null,
                          "offer_type": null,
                          "offer_auto_apply": "0",
                          "is_nce": "0",
                          "failure_reason": null,
                          "created_at": "2024-11-14 16:06:40",
                          "updated_at": "2024-11-14 16:06:40",
                          "offer_title": null,
                          "offer_description": null,
                          "instant_discount": null,
                          "cashback_discount": null,
                          "offers_raw_response": null,
                          "raw_response": null
                      }
                  ]
              }
          }
      }
  }
  ```

  * Offer availed at Transaction level

  ```
  {
      "status": 1,
      "msg": "1 out of 1 Transactions Fetched Successfully",
      "transaction_details": {
          "1725950872187": {
              "mihpayid": "20911942990",
              "request_id": null,
              "bank_ref_num": null,
              "amt": "9900.00",
              "transaction_amount": "10000.00",
              "txnid": "1725950872187",
              "additional_charges": "0.00",
              "productinfo": "Macbook Pro",
              "firstname": "Abc",
              "bankcode": "MAST",
              "udf1": "udf1",
              "udf2": "udf2",
              "udf3": "udf3",
              "udf4": "udf4",
              "udf5": "udf5",
              "field2": null,
              "field9": "You have reached credit card load limit. Please use other payment options to continue.",
              "error_code": "E4936",
              "addedon": "2024-09-10 12:18:20",
              "payment_source": "payu",
              "card_type": "MAST",
              "error_Message": "Bank was unable to authenticate.",
              "net_amount_debit": "0.00",
              "disc": "100.00",
              "mode": "DC",
              "PG_TYPE": "DC-PG",
              "card_no": "XXXXXXXXXXXX9528",
              "status": "failure",
              "unmappedstatus": "failed",
              "Merchant_UTR": null,
              "Settled_At": null,
              "cardhash": "31056eb2112b68cdc90896f1953ca26605bb525249096172c178881bcd45ac93",
              "name_on_card": null,
              "card_token": null,
              "field4": null,
              "offerApplied": "LoadTest1@m3phN7YptAA6",
              "offerAvailed": "LoadTest1@m3phN7YptAA6",
              "transactionOffer": "{"offer_data":[{"offer_key":"LoadTest1@m3phN7YptAA6","discount":100,"offer_type":"INSTANT","isNoCost":false,"flag_to_fail":false,"status":"SUCCESS","failure_code":null,"failure_reason":"Offer Applied Successfully","offer_description":"Load Test 1","offer_title":"Load Test 1","record_type":"OFFER","parent_offer_key":null,"offer_category":null,"isDpEmi":false}],"discount_data":{"total_discount":100,"cashback_discount":0,"instant_discount":100,"total_nce_discount":0,"instant_nce_discount":0,"cashback_nce_discount":0,"gstSubventedViaOffer":false,"downPaymentAmount":0}}",
              "offerType": "instant",
              "offerLevel": "TRANSACTION_LEVEL"
          }
      }
  }
  ```

  #### Failure Responses

  * If txnID is not found, the response is similar to the following:

  ```plaintext
  {
  "status":0,"msg":"0 out of 1 Transactions Fetched

  Successfully","transaction_details":{"IhfgcZnXR4o4nB":{"mihpayid":"Not Found","status":"Not Found"}}
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          **Parameter**
        </th>

        <th style={{ textAlign: "left" }}>
          **Description**
        </th>

        <th style={{ textAlign: "left" }}>
          **Example**
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          status
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the status of web service call. The status can be any of the following:

          * 0 - If web service call failed.
          * 1 - If web service call succeeded
        </td>

        <td style={{ textAlign: "left" }}>
          0
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          msg
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the reason string.
        </td>

        <td style={{ textAlign: "left" }}>
          For example, any of the following messages are displayed:

          * Parameter missing
          * Token is empty
          * Amount is empty
          * Transaction not exists
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          transaction\_details
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter contains the response in a JSON format. For more information refer to the next table.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          request\_id
        </td>

        <td style={{ textAlign: "left" }}>
          PayU Request ID for a request in a Transaction. For example, a transaction can have a refund request.
        </td>

        <td style={{ textAlign: "left" }}>
          7800456
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          bank\_ref\_num
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter returns the bank reference number. If the bank provides after a successful action.
        </td>

        <td style={{ textAlign: "left" }}>
          204519474956
        </td>
      </tr>
    </tbody>
  </Table>

  <Accordion title="Transaction_details JSON Object Fields Description " icon="fa-flask">
    <Transaction_detailsResponseParameter />
  </Accordion>

  To learn more about the possible error codes and their description, refer to [Error Codes](https://docs.payu.in/reference/error-codes).
</Accordion>

## Request parameters

<Accordion title="Sample values" icon="fa-flask">
  Use the following sample values while trying out the API:

  * `var1` (your transaction ID/order ID): 7fa6c4783a363b3da573
</Accordion>

<Recipe slug="parse-the-verify-payment-api-response" title="Parse the Verify Payment API response" />
