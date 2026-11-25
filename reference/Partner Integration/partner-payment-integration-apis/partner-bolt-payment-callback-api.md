---
api:
  file: partner-bolt-payment-callback-api.yaml
  operationId: partnerBoltPaymentCallback
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/bolt/paymentCallback
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/bolt/paymentCallback" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "mihpayid=403993715521855092" \
    -d "txnid=TXN1001" \
    -d "amount=1000.00" \
    -d "status=success" \
    -d "mode=CC" \
    -d "productinfo=Order" \
    -d "firstname=John" \
    -d "email=customer@example.com" \
    -d "phone=9999999999" \
    -d "hash=YOUR_HASH" \
    -d "bankcode=HDFC" \
    -d "bank_ref_num=1234567890" \
    -d "udf1=custom_value_1" \
    -d "udf2=custom_value_2" \
    -d "udf3=custom_value_3" \
    -d "udf4=custom_value_4" \
    -d "udf5=web" \
    -d "error=E000" \
    -d "error_Message=No Error" \
    -d "net_amount_debit=1000.00" \
    -d "PG_TYPE=CC-PG" \
    -d "unmappedstatus=captured" \
    -d "key=YOUR_MERCHANT_KEY"
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Form Data](https://docs.payu.in/reference/partner-bolt-payment-callback-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "BoltHashController.paymentCallback returns an empty body."
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-bolt-payment-callback-api#response-schemas) section for response parameter description.
</Callout>
