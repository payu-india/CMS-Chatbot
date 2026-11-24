---
api:
  file: partner-static-qr-callback-api.yaml
  operationId: partnerStaticQrCallback
hidden: false
---

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/staticQrCallback
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



> 📘 **PayU receives this postback**
>
> PayU receives this post on POST /partner/staticQrCallback. `field4` is the merchant VPA. `key` is the merchant key used to verify the response hash.

## Callback Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `txnid` | String | Transaction id. A repeat txnid returns HTTP 200 |
| `field4` | String | Merchant VPA. Required |
| `key` | String | Merchant key. Required for hash verification |
| `mihpayid` | String | PayU payment id |
| `amount` | String | Amount |
| `status` | String | Payment status |
| `mode` | String | Payment mode |
| `hash` | String | PayU response hash |
| `bank_ref_num` | String | Bank reference |


## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json
{ "note": "HTTP 200 with an empty body." }
```
</Accordion>
