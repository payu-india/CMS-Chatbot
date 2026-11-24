---
api:
  file: partner-get-eligible-bins-api.yaml
  operationId: partnerGetEligibleBins
hidden: false
---

List EMI bins. PartnerService requires `merchant_id`, `type`, and `var2`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/getEligibleBins
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



## Sample Request

<Accordion title="Request Payload" icon="fa-code">
```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/getEligibleBins' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": "8739528",
  "type": "YOUR_TYPE",
  "var2": "YOUR_VAR2"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The HTTP 200 body is the eligible-bins service payload."
}
```
```json Error Response
{
  "error": "merchant_id, type and var2 param are mandatory params"
}
```
</Accordion>
