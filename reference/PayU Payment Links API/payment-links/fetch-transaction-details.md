---
api:
  file: pl-test-oas.yaml
  operationId: GetTransactionDetailsAPI
hidden: false
metadata:
  title: Fetch Transaction Details
next:
  description: Explore related information and resources.
---
Use this endpoint to fetch all payment attempts such as successful, failed, and pending recorded against a payment link.<br />

Use this to verify payment completion, reconcile partial payments, or displaypayment history. An empty `result` array is a valid success response when no payments have been attempted yet.

***

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /payment-links/{invoiceNumber}/transactions
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
      curl --location '
      https://uatoneapi.payu.in/payment-links/INV2669646610062/txns?pageSize=10&dateFrom=2024-10-16&dateTo=2024-10-17'
      \
      --header 'merchantId: 8237736' \
      --header 'Authorization: Bearer 8e400beadad72c5d00c22d98df690bcf04cff2eff4be51cc30e0783492bd8091'
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
