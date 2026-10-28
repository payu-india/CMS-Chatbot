---
title: Update Invoice API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to update a payment link’s status and expiry date.

<Callout icon="📘" theme="info">
  ### Note:

  The access token with the scope as **update_payment_links** from using the User Token APIs is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:partner-integration-user-token-apis).
</Callout>

### Environment

|                            |                                                             |
| :------------------------- | :---------------------------------------------------------- |
| **Test Environment**       | \<[https://uat-partner.payu.in](https://uatoneapi.payu.in)> |
| **Production Environment** | \<[https://partner.payu.in](https://oneapi.payu.in)>        |

## Request Parameters

<br />

## Sample Request

```curl
curl --request PUT \
  'https://uat-partner.payu.in/api/payment-links/<invoice_number>' \
  --header 'Authorization: Bearer <access_token>' \
  --header 'merchantId: <merchant_id>' \
  --header 'Content-Type: application/json' \
  --data '{
    "active": false
  }'

```

## Sample Response

* Success Scenaio

```text
{
  "status": 0,
  "message": "paymentLink updated",
  "result": null,
  "errorCode": null,
  "guid": null
}

```

* Failure Scenario

```text
```
