---
api:
  file: pl-test-oas.yaml
  operationId: SharePaymentLinkAPI
hidden: false
metadata:
  title: Share a Payment Link
next:
  description: Explore related information and resources.
---
Use this endpoint to resend a payment link notification to a customer. At least one of `viaEmail`,`viaSms`, or `viaWhatsapp` must be `true`. The customer's contact details are taken from the values stored on the link creation time.

***

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /payment-links/{invoiceNumber}/notify
  </Card>
</Cards>

***

## Environments

| Environment                | URL                         |
| :------------------------- | :-------------------------- |
| **Test Environment**       | `https://uatoneapi.payu.in` |
| **Production Environment** | `https://oneapi.payu.in`    |

***

<Callout icon="🔑" theme="default">
  ### **Get your Bearer token before calling this endpoint**

  This API uses OAuth 2.0 — not the hash-based auth used by other PayU APIs.

  1. Call [Get Access Token](ref:get-token-api-for-payment-links) with `grant_type=client_credentials` and `scope=create_payment_links`
  2. Copy the `access_token` from the response
  3. Pass it as `Authorization: Bearer {access_token}` in every request

  <Columns layout="fixed">
    <Column>
      **Token Expiry:** Check `expires_in` in the token response and refresh before it lapses.
    </Column>
  </Columns>
</Callout>

***

## Sample Request

<Tabs>
  <Tab title="Request Payload">
    ```curl
    curl --request POST \
      --url https://uatoneapi.payu.in/payment-links/INV8446471886220/share \
      --header 'authorization: Bearer fjsdkglfd09845084395' \
      --header 'content-type: application/json' \
      --header 'mid: 5016764' \
      --data '{"channelList": ["ashish@gmail.com", "+919876543210"]}'
    ```
    ```python
    import requests
    import json

    url = "https://uatoneapi.payu.in/payment-links/INV8446471886220/share"
    headers = {
        "authorization": "Bearer fjsdkglfd09845084395",
        "content-type": "application/json",
        "mid": "5016764"
    }
    data = {
        "channelList": ["ashish@gmail.com", "+919876543210"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
    ```
    ```csharp
    using System;
    using System.Net.Http;
    using System.Text;
    using Newtonsoft.Json;

    class Program
    {
        static async Task Main(string[] args)
        {
            var client = new HttpClient();
            var url = "https://uatoneapi.payu.in/payment-links";

            var headers = new Dictionary<string, string>
            {
                { "Authorization", "Bearer YOUR_ACCESS_TOKEN" },
                { "merchantId", "YOUR_MERCHANT_ID" },
                { "Content-Type", "application/json" }
            };

            foreach (var header in headers)
                client.DefaultRequestHeaders.Add(header.Key, header.Value);

            var json = JsonConvert.SerializeObject({
      "subAmount": 1499,
      "description": "Order #ORD-2026-88421",
      "source": "API",
      "invoiceNumber": "ORD-2026-88421",
      "expiryDate": "2026-10-15 23:59:59",
      "currency": "INR",
      "tax": 0,
      "shippingCharge": 0,
      "discount": 0,
      "adjustment": 0,
      "maxPaymentsAllowed": 1,
      "isAmountFilledByCustomer": false,
      "isPartialPaymentAllowed": false,
      "minAmountForCustomer": 500,
      "viaEmail": true,
      "viaSms": true,
      "viaWhatsapp": false,
      "enforcePayMethod": "",
      "dropCategory": "",
      "successURL": "https://yoursite.com/success",
      "failureURL": "https://yoursite.com/failure",
      "customer": {
        "name": "Arjun Mehta",
        "email": "arjun.mehta@example.com",
        "phone": "9876543210"
      },
      "address": {
        "line1": "123 MG Road",
        "line2": "Apt 4B",
        "city": "Bengaluru",
        "state": "Karnataka",
        "zipCode": "560001"
      },
      "udf": {
        "udf1": "electronics",
        "udf2": "app-checkout",
        "udf3": "",
        "udf4": "",
        "udf5": ""
      },
      "siDetails": {
        "billingAmount": 999,
        "billingCycle": "MONTHLY",
        "billingInterval": 12,
        "paymentStartDate": "2026-10-01",
        "paymentEndDate": "2027-09-30",
        "isNoExpiry": false,
        "isFreeTrial": false,
        "remarks": "Monthly subscription",
        "billingCurrency": "INR",
        "bankDetails": {
          "bankCode": "HDFC",
          "bankAccountNumber": "50100123456789",
          "ifsc": "HDFC0001234",
          "accountType": "SAVINGS"
        }
      },
      "paymentDeadline": "2026-10-20 23:59:59",
      "reminder": {
        "isScheduled": true,
        "type": 0,
        "channels": [
          "email",
          "phone"
        ]
      },
      "whatsappRecipients": [
        {
          "phone": "9876543210"
        }
      ],
      "whatsappTemplateName": "payment_link_template",
      "offerKey": "FEST20OFF",
      "blockDaysForPreAuthorizeLinks": 3,
      "beneficiarydetail": {
        "beneficiaryAccountNumber": [
          "123456789012"
        ],
        "ifscCode": [
          "HDFC0001234"
        ],
        "beneficiaryName": [
          "Arjun Mehta"
        ],
        "beneficiaryAccountType": [
          "SAVINGS"
        ]
      },
      "batchId": "BATCH-2026-001",
      "notes": "Internal reference note",
      "transactionId": "TXN-2026-88421",
      "customAttributes": [
        {
          "key": "orderId",
          "value": "ORD-88421"
        }
      ],
      "additionalDetails": {
        "amountStatus": "UNPAID",
        "sendWhatsapp": false,
        "partnerWebhookSuccessUrls": "https://partner.example.com/webhook/success",
        "partnerWebhookFailureUrls": "https://partner.example.com/webhook/failure"
      }
    });
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            var response = await client.PostAsync(url, content);
            var responseContent = await response.Content.ReadAsStringAsync();
            Console.WriteLine(responseContent);
        }
    }
    ```
    ```javascript
    const fetch = require('node-fetch');

    const url = 'https://uatoneapi.payu.in/payment-links/INV8446471886220/share';
    const headers = {
        'authorization': 'Bearer fjsdkglfd09845084395',
        'content-type': 'application/json',
        'mid': '5016764'
    };
    const body = JSON.stringify({
        channelList: ['ashish@gmail.com', '+919876543210']
    });

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: body
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    ```
    ```java
    import java.net.HttpURLConnection;
    import java.net.URL;
    import java.io.OutputStream;
    import java.io.BufferedReader;
    import java.io.InputStreamReader;
    import com.google.gson.Gson;
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;

    public class SharePaymentLink {
        public static void main(String[] args) throws Exception {
            URL url = new URL("https://uatoneapi.payu.in/payment-links/INV8446471886220/share");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("authorization", "Bearer fjsdkglfd09845084395");
            conn.setRequestProperty("content-type", "application/json");
            conn.setRequestProperty("mid", "5016764");
            conn.setDoOutput(true);
            
            Map<String, Object> requestBody = new HashMap<>();
            requestBody.put("channelList", Arrays.asList("ashish@gmail.com", "+919876543210"));
            
            Gson gson = new Gson();
            String jsonInputString = gson.toJson(requestBody);
            
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }
            
            try (BufferedReader br = new BufferedReader(
                    new InputStreamReader(conn.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine = null;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println(response.toString());
            }
        }
    }
    ```
    ```php
    <?php
    $url = "https://uatoneapi.payu.in/payment-links/INV8446471886220/share";
    $data = json_encode([
        "channelList" => ["ashish@gmail.com", "+919876543210"]
    ]);
    $headers = [
        "authorization: Bearer fjsdkglfd09845084395",
        "content-type: application/json",
        "mid: 5016764"
    ];
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    echo $response;
    ?>
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
  </Tab>
</Tabs>

***

## Sample Response

<Tabs>
  <Tab title="Success and Error Response">
    ```json Success Respone
    {
      "status": 0,
      "message": "string",
      "result": {},
      "errorCode": 170,
      "guid": "f529e375-739f-4c8a-b5f5-0e67fa3f533f"
    }
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Response](ref:create-payment-links#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
