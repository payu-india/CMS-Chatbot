---
api:
  file: partner-fetch-offer-api.yaml
  operationId: partnerFetchOffer
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/fetchOffer
  </Card>
</Cards>

## Environments

|                        |                                                        |
| :--------------------- | :----------------------------------------------------- |
| Test Environment       | `https://test-partnerapilayer.payu.in/apilayer` |
| Production Environment | `https://api.payu.in` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/fetchOffer" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": 8739528,
      "reseller_id": "YOUR_RESELLER_UUID",
      "hash": "YOUR_HASH",
      "amount": "1000.00",
      "offerKeys": [
        "OFFER_KEY_1"
      ],
      "paymentId": 403993715521855092,
      "userToken": "USER_TOKEN",
      "skusDetail": [
        {
          "skuId": "SKU1",
          "skuAmount": "100.00",
          "quantity": "1",
          "offerKeys": [
            "OFFER_KEY_1"
          ]
        }
      ]
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-fetch-offer-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Offers service JSON, passed through. The partner layer does not define an offers array schema."
  }
  ```
  ```json Error Response
  {
    "errors": [
      "merchant_id is mandatory"
    ]
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-fetch-offer-api#response-schemas) section for response parameter description.
</Callout>
