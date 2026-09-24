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

<Accordion title="Standard Payment Link" icon="fab fa-stripe-s">
  Use the this payload to create and send a payment link with fixed-amount and one-time payment via SMS, email, or WhatsApp. You can use it for order payments, invoices, and on-demand payment requests.

  <Tabs>
    <Tab title="Succes and Error Response">

    </Tab>

    <Tab title="Response Parameter Description">

    </Tab>
  </Tabs>



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
    </Tab>

    <Tab title="Request Parameter Description">
      Refer to the [Body Params](ref:create-payment-links#body-params) section for a full description of all request parameters and use cases.
    </Tab>
  </Tabs>
</Accordion>
