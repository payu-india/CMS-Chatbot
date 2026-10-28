---
title: Update Invoice API
deprecated: false
hidden: true
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

### Request Header

| Parameter     | Description                                                                                                         | Example                   |
| :------------ | :------------------------------------------------------------------------------------------------------------------ | :------------------------ |
| Content-Type  | The format of the request body.                                                                                     | `application/json`        |
| Authorization | The Bearer access token used to authenticate the API request. The token must have the `create_payment_links` scope. | `Bearer {{access_token}}` |
| merchantId    | The unique merchant identifier provided by PayU.                                                                    | `4825038`                 |

### Request Parameter

| Parameter | Description                                                    | Example |
| :-------- | :------------------------------------------------------------- | :------ |
| active    | Post it as `false` to indicate the payment link is not active. | `false` |

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

```json
{
  "status": 0,
  "message": "paymentLink updated",
  "result": null,
  "errorCode": null,
  "guid": null
}

```

<br />

<br />
