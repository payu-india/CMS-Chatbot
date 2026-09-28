---
api:
  file: pl-test-oas.yaml
  operationId: CancelPaymentLinkAPI
hidden: false
---
Use this endpoint to deactivate an existing payment link so it can no longer accept payments. You should pass the `active` parameter value as `false` permanently to cancel a link.

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Restrictions**

  You cannot:

  - Reactivate a cancelled link
  - Cancel a link that has already been fully paid
</Callout>

***

<Cards>
  <Card title="Method">
    Delete
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
    curl --request DELETE \
         --url https://uatoneapi.payu.in/payment-links/ORD-2026-88421 \
         --header 'Authorization: Bearer {{access_token}}' \
         --header 'accept: application/json' \
         --header 'merchantId: {{merchantId}}'
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
  </Tab>
</Tabs>
