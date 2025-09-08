---
title: Refund Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Refund Status** API is used to fetch the status of a previously initiated refund.the Refund status flow involves:
1. Initiate the refund using the **Refund** API
2. Capture the `loyaltyRefundId` from the response
3. Use the **Refund Status** API to check the status of the refund using the `loyaltyRefundId`


## Environment
\{\{loyalty-service-url}}/refund/v1/\{loyaltyRefundId}

HTTP Method: **GET* 


## Request path parameters

## Sample request

### Non-seamless integration
```bash
curl -X GET "https://apitest.payu.in/loyalty-points/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "mid: YOUR_MERCHANT_ID"
```

### Seamless integration
```bash
curl -X GET "https://apitest.payu.in/loyalty-points/refund/v1/1213" \
  -H "Content-Type: application/json" \
  -H "Date: Wed, 08 Sep 2025 13:22:43 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\""
```
## Response parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| message | `String` - Refund process status \(`Success`, `Failed`, or `Pending`) | `"Success"` / `"Failed"` / `"Pending"` |
| loyaltyRefundId | `String` - Loyalty refund ID | `"1213"` |
| rewardPartnerRefId | `String` - Reference ID provided by the reward partner (if successful) | `"7251637276230479872"` |


## Sample response
###Success scenario
```json
{
  "message": "Success",
  "loyaltyRefundId": 83,
  "rewardPartnerRefId": "7251637276230479872"
}
```

### Failure scenario
* Failed refund
```json
{
  "message": "Failed",
  "loyaltyRefundId": "1213"
}
```

* Pending refund
```json
{
  "message": "Pending",
  "loyaltyRefundId": "1213"
}
```

## Response States
- **Success**: Refund is processed successfully
- **Pending**: Refund is still under process
- **Failed**: Refund could not be processed

## Notes
- Both APIs are part of the **Loyalty Points Network** and must be called within a secure server-to-server (S2S) framework
- Regular status checks are recommended for pending refunds

