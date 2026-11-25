---
api:
  file: partner-validate-offer-api.yaml
  operationId: partnerValidateOffer
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/validateOffer
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/validateOffer" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": 8739528,
      "reseller_id": "YOUR_RESELLER_UUID",
      "hash": "YOUR_HASH",
      "amount": "1000.00",
      "autoApply": false,
      "merchantNceParamActive": false,
      "offerKeys": [
        "OFFER_KEY_1"
      ],
      "paymentId": 403993715521855092,
      "paymentDetail": {
        "category": "creditcard",
        "paymentCode": "CC",
        "cardNumber": 411111,
        "cardHash": "CARD_HASH",
        "cardToken": "CARD_TOKEN",
        "cardTokenType": 0,
        "cardMask": 1111,
        "vpa": "customer@upi"
      },
      "userDetail": {
        "userToken": "USER_TOKEN",
        "email": "customer@example.com",
        "phoneNo": "9999999999"
      },
      "skusDetail": {
        "skus": [
          {
            "skuId": "SKU1",
            "skuAmount": "100.00",
            "quantity": "1",
            "offerKeys": [
              "OFFER_KEY_1"
            ],
            "autoApply": false
          }
        ]
      }
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-validate-offer-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Offers validate JSON, passed through."
  }
  ```
  ```json Error Response
  {
    "errors": [
      "paymentDetail is mandatory"
    ]
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-validate-offer-api#response-schemas) section for response parameter description.
</Callout>
