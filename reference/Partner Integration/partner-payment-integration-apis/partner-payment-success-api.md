---
api:
  file: partner-payment-success-api.yaml
  operationId: partnerPaymentSuccess
hidden: false
---

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/paymentSuccess
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



> 📘 **PayU receives this postback**
>
> PayU receives the hosted-checkout result on this route after a successful payment. This is not a URL the partner hosts. The customer is then sent to the surl from the payment request. Return handling is a redirect, not `{ status: ok }`.

## Callback Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `mihpayid` | String | PayU payment id |
| `txnid` | String | Transaction id posted by the merchant |
| `amount` | String | Transaction amount |
| `status` | String | `success` on this route |
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
{ "note": "No JSON body. PayU redirects the customer to surl." }
```
</Accordion>
