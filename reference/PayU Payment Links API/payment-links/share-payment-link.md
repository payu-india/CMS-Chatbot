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
