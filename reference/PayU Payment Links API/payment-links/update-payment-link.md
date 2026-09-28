---
api:
  file: pl-test-oas.yaml
  operationId: UpdatePaymentLinkAPI
hidden: false
metadata:
  title: Update a Payment Link
next:
  description: Explore related information and resources.
---
Use this endpoint to modify the configuration of an existing active payment link.<br />

Only send the fields you want to change. Your omitted fields retain their current values.

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Restrictions**

  You cannot:

  - Update a cancelled link (`active: false`).
  - Update a link that has been fully paid.
  - Reduce `subAmount` below the amount already collected on a partial payment link.
</Callout>

***

<Cards>
  <Card title="Method">
    PUT
  </Card>

  <Card title="Endpoint">
    /payment-links/{invoiceNumber}
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
    curl -X POST "https://uatoneapi.payu.in/payment-links" \
      -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      -H "merchantId: YOUR_MERCHANT_ID" \
      -H "Content-Type: application/json" \
      -d '{
      "subAmount": 2000,
      "description": "Update link testing",
      "expiryDate": "2026-11-30 23:59:59",
      "isPartialPaymentAllowed": true,
      "minAmountForCustomer": 500,
      "viaEmail": true,
      "viaSms": true,
      "viaWhatsapp": true
    }'
    ```
    ```python
    import requests

    url = "https://uatoneapi.payu.in/payment-links"

    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "merchantId": "YOUR_MERCHANT_ID",
        "Content-Type": "application/json"
    }

    payload = {
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
    }

    response = requests.post(url, headers=headers, json=payload)
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
    const url = "https://uatoneapi.payu.in/payment-links";

    const headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "merchantId": "YOUR_MERCHANT_ID",
        "Content-Type": "application/json"
    };

    const payload = {
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
    };

    fetch(url, {
        method: "POST",
        headers: headers,
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
    ```
    ```java
    import okhttp3.*;
    import org.json.JSONObject;

    public class PaymentLinkExample {
        public static void main(String[] args) throws Exception {
            String url = "https://uatoneapi.payu.in/payment-links";

            JSONObject payload = new JSONObject({"subAmount": 1499, "description": "Order #ORD-2026-88421", "source": "API", "invoiceNumber": "ORD-2026-88421", "expiryDate": "2026-10-15 23:59:59", "currency": "INR", "tax": 0, "shippingCharge": 0, "discount": 0, "adjustment": 0, "maxPaymentsAllowed": 1, "isAmountFilledByCustomer": false, "isPartialPaymentAllowed": false, "minAmountForCustomer": 500, "viaEmail": true, "viaSms": true, "viaWhatsapp": false, "enforcePayMethod": "", "dropCategory": "", "successURL": "https://yoursite.com/success", "failureURL": "https://yoursite.com/failure", "customer": {"name": "Arjun Mehta", "email": "arjun.mehta@example.com", "phone": "9876543210"}, "address": {"line1": "123 MG Road", "line2": "Apt 4B", "city": "Bengaluru", "state": "Karnataka", "zipCode": "560001"}, "udf": {"udf1": "electronics", "udf2": "app-checkout", "udf3": "", "udf4": "", "udf5": ""}, "siDetails": {"billingAmount": 999, "billingCycle": "MONTHLY", "billingInterval": 12, "paymentStartDate": "2026-10-01", "paymentEndDate": "2027-09-30", "isNoExpiry": false, "isFreeTrial": false, "remarks": "Monthly subscription", "billingCurrency": "INR", "bankDetails": {"bankCode": "HDFC", "bankAccountNumber": "50100123456789", "ifsc": "HDFC0001234", "accountType": "SAVINGS"}}, "paymentDeadline": "2026-10-20 23:59:59", "reminder": {"isScheduled": true, "type": 0, "channels": ["email", "phone"]}, "whatsappRecipients": [{"phone": "9876543210"}], "whatsappTemplateName": "payment_link_template", "offerKey": "FEST20OFF", "blockDaysForPreAuthorizeLinks": 3, "beneficiarydetail": {"beneficiaryAccountNumber": ["123456789012"], "ifscCode": ["HDFC0001234"], "beneficiaryName": ["Arjun Mehta"], "beneficiaryAccountType": ["SAVINGS"]}, "batchId": "BATCH-2026-001", "notes": "Internal reference note", "transactionId": "TXN-2026-88421", "customAttributes": [{"key": "orderId", "value": "ORD-88421"}], "additionalDetails": {"amountStatus": "UNPAID", "sendWhatsapp": false, "partnerWebhookSuccessUrls": "https://partner.example.com/webhook/success", "partnerWebhookFailureUrls": "https://partner.example.com/webhook/failure"}});

            OkHttpClient client = new OkHttpClient();
            RequestBody body = RequestBody.create(
                payload.toString(),
                MediaType.parse("application/json")
            );

            Request request = new Request.Builder()
                .url(url)
                .addHeader("Authorization", "Bearer YOUR_ACCESS_TOKEN")
                .addHeader("merchantId", "YOUR_MERCHANT_ID")
                .addHeader("Content-Type", "application/json")
                .post(body)
                .build();

            Response response = client.newCall(request).execute();
            System.out.println(response.body().string());
        }
    }
    ```
    ```php
    <?php
    $url = "https://uatoneapi.payu.in/payment-links";

    $headers = [
        "Authorization: Bearer YOUR_ACCESS_TOKEN",
        "merchantId: YOUR_MERCHANT_ID",
        "Content-Type: application/json"
    ];

    $payload = [
        "subAmount" => 1499,
        "description" => "Order #ORD-2026-88421",
        "source" => "API",
        "invoiceNumber" => "ORD-2026-88421",
        "expiryDate" => "2026-10-15 23:59:59",
        "currency" => "INR",
        "tax" => 0,
        "shippingCharge" => 0,
        "discount" => 0,
        "adjustment" => 0,
        "maxPaymentsAllowed" => 1,
        "isAmountFilledByCustomer" => false,
        "isPartialPaymentAllowed" => false,
        "minAmountForCustomer" => 500,
        "viaEmail" => true,
        "viaSms" => true,
        "viaWhatsapp" => false,
        "enforcePayMethod" => "",
        "dropCategory" => "",
        "successURL" => "https://yoursite.com/success",
        "failureURL" => "https://yoursite.com/failure",
        "customer" => [
            "name" => "Arjun Mehta",
            "email" => "arjun.mehta@example.com",
            "phone" => "9876543210"
        ],
        "address" => [
            "line1" => "123 MG Road",
            "line2" => "Apt 4B",
            "city" => "Bengaluru",
            "state" => "Karnataka",
            "zipCode" => "560001"
        ],
        "udf" => [
            "udf1" => "electronics",
            "udf2" => "app-checkout",
            "udf3" => "",
            "udf4" => "",
            "udf5" => ""
        ],
        "siDetails" => [
            "billingAmount" => 999,
            "billingCycle" => "MONTHLY",
            "billingInterval" => 12,
            "paymentStartDate" => "2026-10-01",
            "paymentEndDate" => "2027-09-30",
            "isNoExpiry" => false,
            "isFreeTrial" => false,
            "remarks" => "Monthly subscription",
            "billingCurrency" => "INR",
            "bankDetails" => [
                "bankCode" => "HDFC",
                "bankAccountNumber" => "50100123456789",
                "ifsc" => "HDFC0001234",
                "accountType" => "SAVINGS"
            ]
        ],
        "paymentDeadline" => "2026-10-20 23:59:59",
        "reminder" => [
            "isScheduled" => true,
            "type" => 0,
            "channels" => [
                "email",
                "phone"
            ]
        ],
        "whatsappRecipients" => [
            [
                "phone" => "9876543210"
            ]
        ],
        "whatsappTemplateName" => "payment_link_template",
        "offerKey" => "FEST20OFF",
        "blockDaysForPreAuthorizeLinks" => 3,
        "beneficiarydetail" => [
            "beneficiaryAccountNumber" => [
                "123456789012"
            ],
            "ifscCode" => [
                "HDFC0001234"
            ],
            "beneficiaryName" => [
                "Arjun Mehta"
            ],
            "beneficiaryAccountType" => [
                "SAVINGS"
            ]
        ],
        "batchId" => "BATCH-2026-001",
        "notes" => "Internal reference note",
        "transactionId" => "TXN-2026-88421",
        "customAttributes" => [
            [
                "key" => "orderId",
                "value" => "ORD-88421"
            ]
        ],
        "additionalDetails" => [
            "amountStatus" => "UNPAID",
            "sendWhatsapp" => false,
            "partnerWebhookSuccessUrls" => "https://partner.example.com/webhook/success",
            "partnerWebhookFailureUrls" => "https://partner.example.com/webhook/failure"
        ]
    ];

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($payload),
        CURLOPT_HTTPHEADER => $headers
    ]);

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
      "message": "paymentLink generated",
      "result": {
        "subAmount": 1499,
        "tax": 0,
        "shippingCharge": 0,
        "totalAmount": 1499,
        "invoiceNumber": "ORD-2026-88421",
        "paymentLink": "https://pp72.pmny.in/WxYzAbCdEfGh",
        "description": "Order #ORD-2026-88421 – Wireless Headphones",
        "active": true,
        "isPartialPaymentAllowed": false,
        "expiryDate": "2026-10-15 23:59:59",
        "emailStatus": "sent",
        "smsStatus": "sent"
      },
      "errorCode": null,
      "guid": null
    }
    ```
    ```json Error Response
    {
      "status": -1,
      "message": "description is required.",
      "result": null,
      "errorCode": null,
      "guid": null
    }
    ```
  </Tab>

  <Tab title="Parameter Description">
    Refer to the [Response](ref:create-payment-links#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>
