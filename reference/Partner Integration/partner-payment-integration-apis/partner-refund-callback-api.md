---
api:
  file: partner-refund-callback-api.yaml
  operationId: partnerRefundCallback
hidden: false
---

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/refundCallback
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



> 📘 **PayU receives this postback**
>
> PayU receives this on POST /partner/refundCallback. Field names follow RefundCallbackDTO and RefundCallbackMigratedDTO. The outline names txnid, amount, refund_amount, hash, error, and merchantId are not fields on those DTOs.

## Callback Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `mihpayid` | String | PayU payment id (non-migrated) |
| `request_id` | String | Refund request id (non-migrated) |
| `amt` | String | Refund amount (non-migrated) |
| `status` | String | `success`, `queued`, or `failure` (non-migrated) |
| `token` | String | Refund token |
| `bank_ref_num` | String | Bank reference |
| `bank_arn` | String | Acquirer reference |
| `merchantTxnId` | String | Merchant transaction id |
| `paymentId` | String | Migrated payment id |
| `refundId` | String | Migrated refund id |
| `refundAmount` | String | Migrated refund amount |
| `refundStatus` | String | Migrated status |


## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json
{ "note": "The handler returns void." }
```
</Accordion>
