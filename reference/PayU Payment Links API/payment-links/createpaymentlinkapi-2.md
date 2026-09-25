---
api:
  file: pl-test-oas.yaml
  operationId: CreatePaymentLinkAPI
hidden: false
---
Use this endpoint to generate a shareable payment link and optionally deliver it to your customer via SMS, email, or WhatsApp.

***

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /payment-links
  </Card>
</Cards>

***

## Environments

| Environment                | URL                                       |
| :------------------------- | :---------------------------------------- |
| **Test Environment**       | `https://uatoneapi.payu.in/payment-links` |
| **Production Environment** | `https://oneapi.payu.in/payment-links`    |

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

  <Tab title="Request Parameter Description">
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

  <Tab title="Response Parameter Description">
    Refer to the [Response](ref:create-payment-links#response-schemas) section for a full description of all response fields.
  </Tab>
</Tabs>

***

## Supported Payment Link Types

PayU's Create Payment Link API supports five distinct link types, all from the same POST /payment-links endpoint. Each section below includes a ready-to-use payload.

<Accordion title="Standard Payment Link" icon="fab fa-stripe-s">
  Use the this payload to create and send a payment link with fixed-amount and one-time payment via SMS, email, or WhatsApp. You can use it for order payments, invoices, and on-demand payment requests.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 1499,
        "description": "Order #ORD-2026-88421 – Wireless Headphones",
        "source": "API",
        "invoiceNumber": "ORD-2026-88421",
        "expiryDate": "2026-10-15 23:59:59",
        "customer": {
          "name": "Arjun Mehta",
          "email": "arjun.mehta@example.com",
          "phone": "9876543210"
        },
        "udf": {
          "udf1": "electronics",
          "udf2": "app-checkout"
        },
        "viaEmail": true,
        "viaSms": true,
        "isPartialPaymentAllowed": false
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
        "description": "Order #ORD-2026-88421 \u2013 Wireless Headphones",
        "source": "API",
        "invoiceNumber": "ORD-2026-88421",
        "expiryDate": "2026-10-15 23:59:59",
        "customer": {
          "name": "Arjun Mehta",
          "email": "arjun.mehta@example.com",
          "phone": "9876543210"
        },
        "udf": {
          "udf1": "electronics",
          "udf2": "app-checkout"
        },
        "viaEmail": true,
        "viaSms": true,
        "isPartialPaymentAllowed": false
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
        "description": "Order #ORD-2026-88421 \u2013 Wireless Headphones",
        "source": "API",
        "invoiceNumber": "ORD-2026-88421",
        "expiryDate": "2026-10-15 23:59:59",
        "customer": {
          "name": "Arjun Mehta",
          "email": "arjun.mehta@example.com",
          "phone": "9876543210"
        },
        "udf": {
          "udf1": "electronics",
          "udf2": "app-checkout"
        },
        "viaEmail": true,
        "viaSms": true,
        "isPartialPaymentAllowed": false
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
        "description": "Order #ORD-2026-88421 \u2013 Wireless Headphones",
        "source": "API",
        "invoiceNumber": "ORD-2026-88421",
        "expiryDate": "2026-10-15 23:59:59",
        "customer": {
          "name": "Arjun Mehta",
          "email": "arjun.mehta@example.com",
          "phone": "9876543210"
        },
        "udf": {
          "udf1": "electronics",
          "udf2": "app-checkout"
        },
        "viaEmail": true,
        "viaSms": true,
        "isPartialPaymentAllowed": false
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

              JSONObject payload = new JSONObject({"subAmount": 1499, "description": "Order #ORD-2026-88421 \u2013 Wireless Headphones", "source": "API", "invoiceNumber": "ORD-2026-88421", "expiryDate": "2026-10-15 23:59:59", "customer": {"name": "Arjun Mehta", "email": "arjun.mehta@example.com", "phone": "9876543210"}, "udf": {"udf1": "electronics", "udf2": "app-checkout"}, "viaEmail": true, "viaSms": true, "isPartialPaymentAllowed": false});

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
          "description" => "Order #ORD-2026-88421 – Wireless Headphones",
          "source" => "API",
          "invoiceNumber" => "ORD-2026-88421",
          "expiryDate" => "2026-10-15 23:59:59",
          "customer" => [
              "name" => "Arjun Mehta",
              "email" => "arjun.mehta@example.com",
              "phone" => "9876543210"
          ],
          "udf" => [
              "udf1" => "electronics",
              "udf2" => "app-checkout"
          ],
          "viaEmail" => true,
          "viaSms" => true,
          "isPartialPaymentAllowed" => false
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Open Amount Payment Link" icon="fad fa-envelope-open-dollar">
  Use the this payload to create and send a payment link with an option for the customer to enter the amount at checkout. This link is ideal for donations, tips, charity collections, and flexible pricing scenarios.

  <Callout icon="fad fa-brake-warning" theme="error">
    ### **Watch Out!**

    Do not include `subAmount` when `isAmountFilledByCustomer` is true. If both are present, `subAmount` takes precedence and the link will not be open-amount.
  </Callout>

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "description": "Donate to Green Earth Foundation",
        "source": "API",
        "invoiceNumber": "DONATION-2026-00123",
        "expiryDate": "2026-12-31 23:59:59",
        "isAmountFilledByCustomer": true,
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true
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
        "description": "Donate to Green Earth Foundation",
        "source": "API",
        "invoiceNumber": "DONATION-2026-00123",
        "expiryDate": "2026-12-31 23:59:59",
        "isAmountFilledByCustomer": true,
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true
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
        "description": "Donate to Green Earth Foundation",
        "source": "API",
        "invoiceNumber": "DONATION-2026-00123",
        "expiryDate": "2026-12-31 23:59:59",
        "isAmountFilledByCustomer": true,
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true
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
        "description": "Donate to Green Earth Foundation",
        "source": "API",
        "invoiceNumber": "DONATION-2026-00123",
        "expiryDate": "2026-12-31 23:59:59",
        "isAmountFilledByCustomer": true,
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true
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

              JSONObject payload = new JSONObject({"description": "Donate to Green Earth Foundation", "source": "API", "invoiceNumber": "DONATION-2026-00123", "expiryDate": "2026-12-31 23:59:59", "isAmountFilledByCustomer": true, "customer": {"name": "Priya Nair", "email": "priya.nair@example.com", "phone": "9123456789"}, "viaEmail": true});

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
          "description" => "Donate to Green Earth Foundation",
          "source" => "API",
          "invoiceNumber" => "DONATION-2026-00123",
          "expiryDate" => "2026-12-31 23:59:59",
          "isAmountFilledByCustomer" => true,
          "customer" => [
              "name" => "Priya Nair",
              "email" => "priya.nair@example.com",
              "phone" => "9123456789"
          ],
          "viaEmail" => true
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Partial Payment Link" icon="fad fa-display-chart-up-circle-dollar">
  Use this payload to create and send a payment link for a customer to pay the total amount in multiple instalments. The link stays active and accepts payments until the full amount is collected or the link expires.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 5000,
        "description": "Laptop purchase — INR 5,000 total",
        "source": "API",
        "invoiceNumber": "LAPTOP-2026-007",
        "expiryDate": "2026-11-30 23:59:59",
        "isPartialPaymentAllowed": true,
        "minAmountForCustomer": 1000,
        "maxPaymentsAllowed": 5,
        "customer": {
          "name": "Kiran Joshi",
          "email": "kiran.joshi@example.com",
          "phone": "9765432100"
        },
        "viaEmail": true,
        "viaSms": true
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
        "subAmount": 5000,
        "description": "Laptop purchase \u2013 INR 5,000 total",
        "source": "API",
        "invoiceNumber": "LAPTOP-2026-007",
        "expiryDate": "2026-11-30 23:59:59",
        "isPartialPaymentAllowed": true,
        "minAmountForCustomer": 1000,
        "maxPaymentsAllowed": 5,
        "customer": {
          "name": "Kiran Joshi",
          "email": "kiran.joshi@example.com",
          "phone": "9765432100"
        },
        "viaEmail": true,
        "viaSms": true
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
        "subAmount": 5000,
        "description": "Laptop purchase \u2013 INR 5,000 total",
        "source": "API",
        "invoiceNumber": "LAPTOP-2026-007",
        "expiryDate": "2026-11-30 23:59:59",
        "isPartialPaymentAllowed": true,
        "minAmountForCustomer": 1000,
        "maxPaymentsAllowed": 5,
        "customer": {
          "name": "Kiran Joshi",
          "email": "kiran.joshi@example.com",
          "phone": "9765432100"
        },
        "viaEmail": true,
        "viaSms": true
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
        "subAmount": 5000,
        "description": "Laptop purchase \u2013 INR 5,000 total",
        "source": "API",
        "invoiceNumber": "LAPTOP-2026-007",
        "expiryDate": "2026-11-30 23:59:59",
        "isPartialPaymentAllowed": true,
        "minAmountForCustomer": 1000,
        "maxPaymentsAllowed": 5,
        "customer": {
          "name": "Kiran Joshi",
          "email": "kiran.joshi@example.com",
          "phone": "9765432100"
        },
        "viaEmail": true,
        "viaSms": true
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

              JSONObject payload = new JSONObject({"subAmount": 5000, "description": "Laptop purchase \u2013 INR 5,000 total", "source": "API", "invoiceNumber": "LAPTOP-2026-007", "expiryDate": "2026-11-30 23:59:59", "isPartialPaymentAllowed": true, "minAmountForCustomer": 1000, "maxPaymentsAllowed": 5, "customer": {"name": "Kiran Joshi", "email": "kiran.joshi@example.com", "phone": "9765432100"}, "viaEmail": true, "viaSms": true});

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
          "subAmount" => 5000,
          "description" => "Laptop purchase – INR 5,000 total",
          "source" => "API",
          "invoiceNumber" => "LAPTOP-2026-007",
          "expiryDate" => "2026-11-30 23:59:59",
          "isPartialPaymentAllowed" => true,
          "minAmountForCustomer" => 1000,
          "maxPaymentsAllowed" => 5,
          "customer" => [
              "name" => "Kiran Joshi",
              "email" => "kiran.joshi@example.com",
              "phone" => "9765432100"
          ],
          "viaEmail" => true,
          "viaSms" => true
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="SI Recurring Payment Link" icon="fad fa-space-station-moon-construction">
  Registers a standing instruction (SI) mandate for automated recurring debits on a fixed schedule. The customer completes mandate registration via card or UPI on first interaction. All subsequent debits happen server-to-server with no customer action required.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 999,
        "description": "Monthly SaaS subscription — Pro Plan",
        "source": "si_payment_link",
        "invoiceNumber": "SUB-2026-00291",
        "expiryDate": "2026-12-31 23:59:59",
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 999,
          "billingCycle": "MONTHLY",
          "billingInterval": 12,
          "paymentStartDate": "2026-10-01",
          "paymentEndDate": "2027-09-30",
          "isNoExpiry": false,
          "isFreeTrial": false,
          "remarks": "Monthly Pro plan",
          "billingCurrency": "INR"
        }
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
        "subAmount": 999,
        "description": "Monthly SaaS subscription \u2013 Pro Plan",
        "source": "si_payment_link",
        "invoiceNumber": "SUB-2026-00291",
        "expiryDate": "2026-12-31 23:59:59",
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 999,
          "billingCycle": "MONTHLY",
          "billingInterval": 12,
          "paymentStartDate": "2026-10-01",
          "paymentEndDate": "2027-09-30",
          "isNoExpiry": false,
          "isFreeTrial": false,
          "remarks": "Monthly Pro plan",
          "billingCurrency": "INR"
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
        "subAmount": 999,
        "description": "Monthly SaaS subscription \u2013 Pro Plan",
        "source": "si_payment_link",
        "invoiceNumber": "SUB-2026-00291",
        "expiryDate": "2026-12-31 23:59:59",
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 999,
          "billingCycle": "MONTHLY",
          "billingInterval": 12,
          "paymentStartDate": "2026-10-01",
          "paymentEndDate": "2027-09-30",
          "isNoExpiry": false,
          "isFreeTrial": false,
          "remarks": "Monthly Pro plan",
          "billingCurrency": "INR"
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
        "subAmount": 999,
        "description": "Monthly SaaS subscription \u2013 Pro Plan",
        "source": "si_payment_link",
        "invoiceNumber": "SUB-2026-00291",
        "expiryDate": "2026-12-31 23:59:59",
        "customer": {
          "name": "Priya Nair",
          "email": "priya.nair@example.com",
          "phone": "9123456789"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 999,
          "billingCycle": "MONTHLY",
          "billingInterval": 12,
          "paymentStartDate": "2026-10-01",
          "paymentEndDate": "2027-09-30",
          "isNoExpiry": false,
          "isFreeTrial": false,
          "remarks": "Monthly Pro plan",
          "billingCurrency": "INR"
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

              JSONObject payload = new JSONObject({"subAmount": 999, "description": "Monthly SaaS subscription \u2013 Pro Plan", "source": "si_payment_link", "invoiceNumber": "SUB-2026-00291", "expiryDate": "2026-12-31 23:59:59", "customer": {"name": "Priya Nair", "email": "priya.nair@example.com", "phone": "9123456789"}, "viaEmail": true, "siDetails": {"billingAmount": 999, "billingCycle": "MONTHLY", "billingInterval": 12, "paymentStartDate": "2026-10-01", "paymentEndDate": "2027-09-30", "isNoExpiry": false, "isFreeTrial": false, "remarks": "Monthly Pro plan", "billingCurrency": "INR"}});

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
          "subAmount" => 999,
          "description" => "Monthly SaaS subscription – Pro Plan",
          "source" => "si_payment_link",
          "invoiceNumber" => "SUB-2026-00291",
          "expiryDate" => "2026-12-31 23:59:59",
          "customer" => [
              "name" => "Priya Nair",
              "email" => "priya.nair@example.com",
              "phone" => "9123456789"
          ],
          "viaEmail" => true,
          "siDetails" => [
              "billingAmount" => 999,
              "billingCycle" => "MONTHLY",
              "billingInterval" => 12,
              "paymentStartDate" => "2026-10-01",
              "paymentEndDate" => "2027-09-30",
              "isNoExpiry" => false,
              "isFreeTrial" => false,
              "remarks" => "Monthly Pro plan",
              "billingCurrency" => "INR"
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="eNACH Recurring Payment Link" icon="fad fa-calendar-check">
  Routes the customer through the NACH bank debit mandate registration form instead of a card or UPI flow. Identical to SI Recurring in structure. The only difference is `enforcePayMethod`: `enach` and the optional `siDetails.bankDetails` object to pre-fill the customer's bank details.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 2500,
        "description": "Annual insurance premium — auto-debit",
        "source": "si_payment_link",
        "enforcePayMethod": "enach",
        "invoiceNumber": "INS-2026-ENACH-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 2500,
          "billingCycle": "YEARLY",
          "billingInterval": 3,
          "paymentStartDate": "2026-11-01",
          "paymentEndDate": "2029-10-31",
          "remarks": "Annual insurance renewal",
          "billingCurrency": "INR",
          "bankDetails": {
            "bankCode": "HDFC",
            "bankAccountNumber": "50100123456789",
            "ifsc": "HDFC0001234",
            "accountType": "SAVINGS"
          }
        }
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
        "subAmount": 2500,
        "description": "Annual insurance premium \u2013 auto-debit",
        "source": "si_payment_link",
        "enforcePayMethod": "enach",
        "invoiceNumber": "INS-2026-ENACH-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 2500,
          "billingCycle": "YEARLY",
          "billingInterval": 3,
          "paymentStartDate": "2026-11-01",
          "paymentEndDate": "2029-10-31",
          "remarks": "Annual insurance renewal",
          "billingCurrency": "INR",
          "bankDetails": {
            "bankCode": "HDFC",
            "bankAccountNumber": "50100123456789",
            "ifsc": "HDFC0001234",
            "accountType": "SAVINGS"
          }
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
        "subAmount": 2500,
        "description": "Annual insurance premium \u2013 auto-debit",
        "source": "si_payment_link",
        "enforcePayMethod": "enach",
        "invoiceNumber": "INS-2026-ENACH-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 2500,
          "billingCycle": "YEARLY",
          "billingInterval": 3,
          "paymentStartDate": "2026-11-01",
          "paymentEndDate": "2029-10-31",
          "remarks": "Annual insurance renewal",
          "billingCurrency": "INR",
          "bankDetails": {
            "bankCode": "HDFC",
            "bankAccountNumber": "50100123456789",
            "ifsc": "HDFC0001234",
            "accountType": "SAVINGS"
          }
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
        "subAmount": 2500,
        "description": "Annual insurance premium \u2013 auto-debit",
        "source": "si_payment_link",
        "enforcePayMethod": "enach",
        "invoiceNumber": "INS-2026-ENACH-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "siDetails": {
          "billingAmount": 2500,
          "billingCycle": "YEARLY",
          "billingInterval": 3,
          "paymentStartDate": "2026-11-01",
          "paymentEndDate": "2029-10-31",
          "remarks": "Annual insurance renewal",
          "billingCurrency": "INR",
          "bankDetails": {
            "bankCode": "HDFC",
            "bankAccountNumber": "50100123456789",
            "ifsc": "HDFC0001234",
            "accountType": "SAVINGS"
          }
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

              JSONObject payload = new JSONObject({"subAmount": 2500, "description": "Annual insurance premium \u2013 auto-debit", "source": "si_payment_link", "enforcePayMethod": "enach", "invoiceNumber": "INS-2026-ENACH-001", "expiryDate": "2026-10-31 23:59:59", "customer": {"name": "Amit Bose", "email": "amit.bose@example.com", "phone": "9900123456"}, "viaEmail": true, "siDetails": {"billingAmount": 2500, "billingCycle": "YEARLY", "billingInterval": 3, "paymentStartDate": "2026-11-01", "paymentEndDate": "2029-10-31", "remarks": "Annual insurance renewal", "billingCurrency": "INR", "bankDetails": {"bankCode": "HDFC", "bankAccountNumber": "50100123456789", "ifsc": "HDFC0001234", "accountType": "SAVINGS"}}});

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
          "subAmount" => 2500,
          "description" => "Annual insurance premium – auto-debit",
          "source" => "si_payment_link",
          "enforcePayMethod" => "enach",
          "invoiceNumber" => "INS-2026-ENACH-001",
          "expiryDate" => "2026-10-31 23:59:59",
          "customer" => [
              "name" => "Amit Bose",
              "email" => "amit.bose@example.com",
              "phone" => "9900123456"
          ],
          "viaEmail" => true,
          "siDetails" => [
              "billingAmount" => 2500,
              "billingCycle" => "YEARLY",
              "billingInterval" => 3,
              "paymentStartDate" => "2026-11-01",
              "paymentEndDate" => "2029-10-31",
              "remarks" => "Annual insurance renewal",
              "billingCurrency" => "INR",
              "bankDetails" => [
                  "bankCode" => "HDFC",
                  "bankAccountNumber" => "50100123456789",
                  "ifsc" => "HDFC0001234",
                  "accountType" => "SAVINGS"
              ]
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Payment Reminder" icon="fad fa-alarm-exclamation">
  Schedule an automatic notification to the customer before or after a payment deadline. The reminder fires independently of the link expiry date, giving you control over when the customer is nudged to pay.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 2500,
        "description": "Invoice INV-2026-00456 Consulting Services",
        "source": "API",
        "invoiceNumber": "INV-2026-00456",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Rahul Sharma",
          "email": "rahul.sharma@example.com",
          "phone": "9000012345"
        },
        "viaEmail": true,
        "paymentDeadline": "2026-10-20 23:59:59",
        "reminder": {
          "isScheduled": true,
          "type": 0,
          "channels": [
            "email",
            "phone"
          ]
        }
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
        "subAmount": 2500,
        "description": "Invoice INV-2026-00456 Consulting Services",
        "source": "API",
        "invoiceNumber": "INV-2026-00456",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Rahul Sharma",
          "email": "rahul.sharma@example.com",
          "phone": "9000012345"
        },
        "viaEmail": true,
        "paymentDeadline": "2026-10-20 23:59:59",
        "reminder": {
          "isScheduled": true,
          "type": 0,
          "channels": [
            "email",
            "phone"
          ]
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
        "subAmount": 2500,
        "description": "Invoice INV-2026-00456 Consulting Services",
        "source": "API",
        "invoiceNumber": "INV-2026-00456",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Rahul Sharma",
          "email": "rahul.sharma@example.com",
          "phone": "9000012345"
        },
        "viaEmail": true,
        "paymentDeadline": "2026-10-20 23:59:59",
        "reminder": {
          "isScheduled": true,
          "type": 0,
          "channels": [
            "email",
            "phone"
          ]
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
        "subAmount": 2500,
        "description": "Invoice INV-2026-00456 Consulting Services",
        "source": "API",
        "invoiceNumber": "INV-2026-00456",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Rahul Sharma",
          "email": "rahul.sharma@example.com",
          "phone": "9000012345"
        },
        "viaEmail": true,
        "paymentDeadline": "2026-10-20 23:59:59",
        "reminder": {
          "isScheduled": true,
          "type": 0,
          "channels": [
            "email",
            "phone"
          ]
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

              JSONObject payload = new JSONObject({"subAmount": 2500, "description": "Invoice INV-2026-00456 Consulting Services", "source": "API", "invoiceNumber": "INV-2026-00456", "expiryDate": "2026-10-31 23:59:59", "customer": {"name": "Rahul Sharma", "email": "rahul.sharma@example.com", "phone": "9000012345"}, "viaEmail": true, "paymentDeadline": "2026-10-20 23:59:59", "reminder": {"isScheduled": true, "type": 0, "channels": ["email", "phone"]}});

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
          "subAmount" => 2500,
          "description" => "Invoice INV-2026-00456 Consulting Services",
          "source" => "API",
          "invoiceNumber" => "INV-2026-00456",
          "expiryDate" => "2026-10-31 23:59:59",
          "customer" => [
              "name" => "Rahul Sharma",
              "email" => "rahul.sharma@example.com",
              "phone" => "9000012345"
          ],
          "viaEmail" => true,
          "paymentDeadline" => "2026-10-20 23:59:59",
          "reminder" => [
              "isScheduled" => true,
              "type" => 0,
              "channels" => [
                  "email",
                  "phone"
              ]
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Multiple WhatsApp Recipients" icon="fab fa-square-whatsapp">
  Send the same payment link to up to 4 WhatsApp numbers simultaneously at the moment of creation. This type of link is useful for shared invoices, group collections, or notifying both a customer and a guarantor.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 500,
        "description": "Group event registration fee",
        "source": "API",
        "invoiceNumber": "EVENT-2026-099",
        "expiryDate": "2026-11-15 23:59:59",
        "customer": {
          "name": "Kiran Joshi",
          "phone": "9876512345"
        },
        "viaWhatsapp": true,
        "whatsappTemplateName": "event_payment_link",
        "whatsappRecipients": [
          {
            "phone": "9876512345"
          },
          {
            "phone": "9765432100"
          },
          {
            "phone": "9988776655"
          }
        ]
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
        "subAmount": 500,
        "description": "Group event registration fee",
        "source": "API",
        "invoiceNumber": "EVENT-2026-099",
        "expiryDate": "2026-11-15 23:59:59",
        "customer": {
          "name": "Kiran Joshi",
          "phone": "9876512345"
        },
        "viaWhatsapp": true,
        "whatsappTemplateName": "event_payment_link",
        "whatsappRecipients": [
          {
            "phone": "9876512345"
          },
          {
            "phone": "9765432100"
          },
          {
            "phone": "9988776655"
          }
        ]
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
        "subAmount": 500,
        "description": "Group event registration fee",
        "source": "API",
        "invoiceNumber": "EVENT-2026-099",
        "expiryDate": "2026-11-15 23:59:59",
        "customer": {
          "name": "Kiran Joshi",
          "phone": "9876512345"
        },
        "viaWhatsapp": true,
        "whatsappTemplateName": "event_payment_link",
        "whatsappRecipients": [
          {
            "phone": "9876512345"
          },
          {
            "phone": "9765432100"
          },
          {
            "phone": "9988776655"
          }
        ]
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
        "subAmount": 500,
        "description": "Group event registration fee",
        "source": "API",
        "invoiceNumber": "EVENT-2026-099",
        "expiryDate": "2026-11-15 23:59:59",
        "customer": {
          "name": "Kiran Joshi",
          "phone": "9876512345"
        },
        "viaWhatsapp": true,
        "whatsappTemplateName": "event_payment_link",
        "whatsappRecipients": [
          {
            "phone": "9876512345"
          },
          {
            "phone": "9765432100"
          },
          {
            "phone": "9988776655"
          }
        ]
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

              JSONObject payload = new JSONObject({"subAmount": 500, "description": "Group event registration fee", "source": "API", "invoiceNumber": "EVENT-2026-099", "expiryDate": "2026-11-15 23:59:59", "customer": {"name": "Kiran Joshi", "phone": "9876512345"}, "viaWhatsapp": true, "whatsappTemplateName": "event_payment_link", "whatsappRecipients": [{"phone": "9876512345"}, {"phone": "9765432100"}, {"phone": "9988776655"}]});

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
          "subAmount" => 500,
          "description" => "Group event registration fee",
          "source" => "API",
          "invoiceNumber" => "EVENT-2026-099",
          "expiryDate" => "2026-11-15 23:59:59",
          "customer" => [
              "name" => "Kiran Joshi",
              "phone" => "9876512345"
          ],
          "viaWhatsapp" => true,
          "whatsappTemplateName" => "event_payment_link",
          "whatsappRecipients" => [
              [
                  "phone" => "9876512345"
              ],
              [
                  "phone" => "9765432100"
              ],
              [
                  "phone" => "9988776655"
              ]
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Add Offers to the Payment Link" icon="fad fa-arrow-left-from-line">
  Attach a promotional discount or coupon to the payment link so it is applied automatically when the customer reaches the checkout. No additional customer action is required to redeem the offer.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 3999,
        "description": "Festival sale Bluetooth Speaker",
        "source": "API",
        "invoiceNumber": "SALE-2026-7821",
        "expiryDate": "2026-10-25 23:59:59",
        "customer": {
          "name": "Deepa Krishnan",
          "email": "deepa.krishnan@example.com",
          "phone": "9123000456"
        },
        "viaEmail": true,
        "offerKey": "FEST20OFF"
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
        "subAmount": 3999,
        "description": "Festival sale Bluetooth Speaker",
        "source": "API",
        "invoiceNumber": "SALE-2026-7821",
        "expiryDate": "2026-10-25 23:59:59",
        "customer": {
          "name": "Deepa Krishnan",
          "email": "deepa.krishnan@example.com",
          "phone": "9123000456"
        },
        "viaEmail": true,
        "offerKey": "FEST20OFF"
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
        "subAmount": 3999,
        "description": "Festival sale Bluetooth Speaker",
        "source": "API",
        "invoiceNumber": "SALE-2026-7821",
        "expiryDate": "2026-10-25 23:59:59",
        "customer": {
          "name": "Deepa Krishnan",
          "email": "deepa.krishnan@example.com",
          "phone": "9123000456"
        },
        "viaEmail": true,
        "offerKey": "FEST20OFF"
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
        "subAmount": 3999,
        "description": "Festival sale Bluetooth Speaker",
        "source": "API",
        "invoiceNumber": "SALE-2026-7821",
        "expiryDate": "2026-10-25 23:59:59",
        "customer": {
          "name": "Deepa Krishnan",
          "email": "deepa.krishnan@example.com",
          "phone": "9123000456"
        },
        "viaEmail": true,
        "offerKey": "FEST20OFF"
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

              JSONObject payload = new JSONObject({"subAmount": 3999, "description": "Festival sale Bluetooth Speaker", "source": "API", "invoiceNumber": "SALE-2026-7821", "expiryDate": "2026-10-25 23:59:59", "customer": {"name": "Deepa Krishnan", "email": "deepa.krishnan@example.com", "phone": "9123000456"}, "viaEmail": true, "offerKey": "FEST20OFF"});

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
          "subAmount" => 3999,
          "description" => "Festival sale Bluetooth Speaker",
          "source" => "API",
          "invoiceNumber" => "SALE-2026-7821",
          "expiryDate" => "2026-10-25 23:59:59",
          "customer" => [
              "name" => "Deepa Krishnan",
              "email" => "deepa.krishnan@example.com",
              "phone" => "9123000456"
          ],
          "viaEmail" => true,
          "offerKey" => "FEST20OFF"
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

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Hold the Pre-authorisation" icon="fad fa-circle-pause">
  Place a hold on the customer's payment method without immediately capturing funds. The hold remains active for the number of days you specify, after which funds must be captured separately via the capture API.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 10000,
        "description": "Hotel stay pre-authorisation hold",
        "source": "API",
        "invoiceNumber": "HOTEL-2026-338",
        "expiryDate": "2026-11-01 12:00:00",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "blockDaysForPreAuthorizeLinks": 3
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
        "subAmount": 10000,
        "description": "Hotel stay pre-authorisation hold",
        "source": "API",
        "invoiceNumber": "HOTEL-2026-338",
        "expiryDate": "2026-11-01 12:00:00",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "blockDaysForPreAuthorizeLinks": 3
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
        "subAmount": 10000,
        "description": "Hotel stay pre-authorisation hold",
        "source": "API",
        "invoiceNumber": "HOTEL-2026-338",
        "expiryDate": "2026-11-01 12:00:00",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "blockDaysForPreAuthorizeLinks": 3
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
        "subAmount": 10000,
        "description": "Hotel stay pre-authorisation hold",
        "source": "API",
        "invoiceNumber": "HOTEL-2026-338",
        "expiryDate": "2026-11-01 12:00:00",
        "customer": {
          "name": "Amit Bose",
          "email": "amit.bose@example.com",
          "phone": "9900123456"
        },
        "viaEmail": true,
        "blockDaysForPreAuthorizeLinks": 3
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

              JSONObject payload = new JSONObject({"subAmount": 10000, "description": "Hotel stay pre-authorisation hold", "source": "API", "invoiceNumber": "HOTEL-2026-338", "expiryDate": "2026-11-01 12:00:00", "customer": {"name": "Amit Bose", "email": "amit.bose@example.com", "phone": "9900123456"}, "viaEmail": true, "blockDaysForPreAuthorizeLinks": 3});

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
          "subAmount" => 10000,
          "description" => "Hotel stay pre-authorisation hold",
          "source" => "API",
          "invoiceNumber" => "HOTEL-2026-338",
          "expiryDate" => "2026-11-01 12:00:00",
          "customer" => [
              "name" => "Amit Bose",
              "email" => "amit.bose@example.com",
              "phone" => "9900123456"
          ],
          "viaEmail" => true,
          "blockDaysForPreAuthorizeLinks" => 3
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
</Accordion>

<Accordion title="Add Payout Beneficiaries" icon="fad fa-building-shield">
  Specify up to 4 bank accounts for NEFT or IMPS disbursement after the payment is collected. All four arrays must have the same number of entries, where each index position represents one beneficiary.

  <Tabs>
    <Tab title="Request Payload">
      ```curl
      curl -X POST "https://uatoneapi.payu.in/payment-links" \
        -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
        -H "merchantId: YOUR_MERCHANT_ID" \
        -H "Content-Type: application/json" \
        -d '{
        "subAmount": 5000,
        "description": "Freelancer payment Project Delta",
        "source": "API",
        "invoiceNumber": "PAY-2026-FL-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Sana Mirza",
          "email": "sana.mirza@example.com",
          "phone": "9811234567"
        },
        "viaEmail": true,
        "beneficiarydetail": {
          "beneficiaryAccountNumber": [
            "123456789012"
          ],
          "ifscCode": [
            "HDFC0001234"
          ],
          "beneficiaryName": [
            "Sana Mirza"
          ],
          "beneficiaryAccountType": [
            "SAVINGS"
          ]
        }
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
        "subAmount": 5000,
        "description": "Freelancer payment Project Delta",
        "source": "API",
        "invoiceNumber": "PAY-2026-FL-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Sana Mirza",
          "email": "sana.mirza@example.com",
          "phone": "9811234567"
        },
        "viaEmail": true,
        "beneficiarydetail": {
          "beneficiaryAccountNumber": [
            "123456789012"
          ],
          "ifscCode": [
            "HDFC0001234"
          ],
          "beneficiaryName": [
            "Sana Mirza"
          ],
          "beneficiaryAccountType": [
            "SAVINGS"
          ]
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
        "subAmount": 5000,
        "description": "Freelancer payment Project Delta",
        "source": "API",
        "invoiceNumber": "PAY-2026-FL-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Sana Mirza",
          "email": "sana.mirza@example.com",
          "phone": "9811234567"
        },
        "viaEmail": true,
        "beneficiarydetail": {
          "beneficiaryAccountNumber": [
            "123456789012"
          ],
          "ifscCode": [
            "HDFC0001234"
          ],
          "beneficiaryName": [
            "Sana Mirza"
          ],
          "beneficiaryAccountType": [
            "SAVINGS"
          ]
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
        "subAmount": 5000,
        "description": "Freelancer payment Project Delta",
        "source": "API",
        "invoiceNumber": "PAY-2026-FL-001",
        "expiryDate": "2026-10-31 23:59:59",
        "customer": {
          "name": "Sana Mirza",
          "email": "sana.mirza@example.com",
          "phone": "9811234567"
        },
        "viaEmail": true,
        "beneficiarydetail": {
          "beneficiaryAccountNumber": [
            "123456789012"
          ],
          "ifscCode": [
            "HDFC0001234"
          ],
          "beneficiaryName": [
            "Sana Mirza"
          ],
          "beneficiaryAccountType": [
            "SAVINGS"
          ]
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

              JSONObject payload = new JSONObject({"subAmount": 5000, "description": "Freelancer payment Project Delta", "source": "API", "invoiceNumber": "PAY-2026-FL-001", "expiryDate": "2026-10-31 23:59:59", "customer": {"name": "Sana Mirza", "email": "sana.mirza@example.com", "phone": "9811234567"}, "viaEmail": true, "beneficiarydetail": {"beneficiaryAccountNumber": ["123456789012"], "ifscCode": ["HDFC0001234"], "beneficiaryName": ["Sana Mirza"], "beneficiaryAccountType": ["SAVINGS"]}});

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
          "subAmount" => 5000,
          "description" => "Freelancer payment Project Delta",
          "source" => "API",
          "invoiceNumber" => "PAY-2026-FL-001",
          "expiryDate" => "2026-10-31 23:59:59",
          "customer" => [
              "name" => "Sana Mirza",
              "email" => "sana.mirza@example.com",
              "phone" => "9811234567"
          ],
          "viaEmail" => true,
          "beneficiarydetail" => [
              "beneficiaryAccountNumber" => [
                  "123456789012"
              ],
              "ifscCode" => [
                  "HDFC0001234"
              ],
              "beneficiaryName" => [
                  "Sana Mirza"
              ],
              "beneficiaryAccountType" => [
                  "SAVINGS"
              ]
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
</Accordion>
