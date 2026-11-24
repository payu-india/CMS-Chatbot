---
api:
  file: partner-bolt-payment-callback-api.yaml
  operationId: partnerBoltPaymentCallback
hidden: false
---

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/bolt/paymentCallback
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



> 📘 **PayU receives this postback**
>
> PayU receives the Checkout Plus result on this route. The form fields match the standard payment postback. This is not a URL the partner hosts.

## Callback Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `mihpayid` | String | PayU payment id |
| `txnid` | String | Transaction id posted by the merchant |
| `amount` | String | Transaction amount |
| `status` | String | Payment status for this route |
| `mode` | String | Payment mode |
| `productinfo` | String | Product description |
| `firstname` | String | Customer first name |
| `email` | String | Customer email |
| `phone` | String | Customer phone |
| `hash` | String | SHA-512 response hash. Verify before updating the order |
| `bankcode` | String | Bank or instrument code |
| `bank_ref_num` | String | Bank reference number |
| `udf1` to `udf5` | String | User-defined fields echoed from the request |
| `error` | String | Error code when the payment did not succeed |
| `error_Message` | String | Error description |
| `net_amount_debit` | String | Amount debited |
| `PG_TYPE` | String | Payment gateway type |
| `unmappedstatus` | String | PayU status used by the callback handler |
| `key` | String | Merchant key |


## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json
{ "note": "HTTP 200 with an empty body." }
```
</Accordion>
