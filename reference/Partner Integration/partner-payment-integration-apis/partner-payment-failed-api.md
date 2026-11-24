---
api:
  file: partner-payment-failed-api.yaml
  operationId: partnerPaymentFailed
hidden: false
---

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/paymentFailed
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



> 📘 **PayU receives this postback**
>
> PayU receives the hosted-checkout result on this route when the payment fails. error and error_Message carry the gateway reason. The customer is then sent to furl.

## Callback Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `mihpayid` | String | PayU payment id |
| `txnid` | String | Transaction id posted by the merchant |
| `amount` | String | Transaction amount |
| `status` | String | `failure` on this route |
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
{ "note": "No JSON body. PayU redirects the customer to furl." }
```
</Accordion>
