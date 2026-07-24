---
title: Calculate EMI API
deprecated: false
hidden: true
metadata:
  robots: index
---
Calculates EMI (Equated Monthly Installment) options and amounts for selected banks/tenures, optionally applying offer discounts. Supports No Cost EMI (NCE) calculations.

## Endpoint

| Environment | Base URL |
|-------------|----------|
| UAT / Test | `https://apitest.payu.in/v1/calculateEMI` |
| Production | `https://api.payu.in/v1/calculateEMI` |

## Sample Request

```bash
curl -X POST 'https://apitest.payu.in/v1/calculateEMI' \
  -H 'accessToken: <access_token>' \
  -H 'orderId: <encrypted_order_id>' \
  -H 'X-Credential-Username: <merchant_key>' \
  -H 'Content-Type: application/json' \
  -d '{
    "offerKeys": ["of1", "of2"],
    "autoApplyOffer": false,
    "bankCodes": null,
    "emiCodes": [
      "EMIA3",
      "EMIA6",
      "EMIY06",
      "SBI06",
      "IDFC06"
    ],
    "disableOverrideNceConfig": true,
    "skus": null
  }'
```

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "YES": {
      "EMIY18": {
        "transactionAmount": 10000.0,
        "emiAmount": 555.56,
        "emiBankInterest": 15.0,
        "cardType": "credit card",
        "tenure": "18 months",
        "loanAmount": 10000.0,
        "offerDiscount": {
          "total": 0.0,
          "instant": 0.0,
          "cashback": 0.0
        },
        "nceDiscount": {
          "total": 1266.78,
          "instant": 1266.78,
          "cashback": 0.0
        },
        "totalPayableAmount": 10000.0,
        "nceDiscountAmount": 1266.78,
        "gstSubvention": true,
        "bankCode": "YESB",
        "emi_value": 555.55,
        "emi_interest_paid": 1266.78
      }
    }
  }
}
```

## Request Parameters
### Header Authentication Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| accessToken<br/>`mandatory` | `string` Access token from the Create Order response (`transaction.accessToken`). | `<access_token>` |
| orderId<br/>`mandatory` | `string` Encrypted order ID from the Create Order response (`transaction.orderid`). | `<encrypted_order_id>` |
| X-Credential-Username<br/>`mandatory` | `string` Merchant key configured for Air India. | `<merchant_key>` |
| Content-Type<br/>`mandatory` | `string` Media type of the JSON request body. | `application/json` |

## Body Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| offerKeys<br/>`optional` | `array` Offers explicitly selected by customer. | `["of1", "of2"]` |
| promocode<br/>`optional` | `array` Promocode against the offer. | `["PROMO123"]` |
| autoApplyOffer<br/>`mandatory` | `boolean` If `true`, system auto-selects eligible offers. | `false` |
| bankCodes<br/>`optional` | `array` Filter offers by bank codes; `null` = no filter. | `null` |
| emiCodes<br/>`optional` | `array` Filter offers by EMI program codes (e.g., `EMIA3` = Axis Bank 3-month EMI). | `["EMIA3", "EMIA6"]` |
| disableOverrideNceConfig<br/>`optional` | `boolean` Disables NCE (No Cost EMI) override configuration. | `true` |
| skus<br/>`optional` | `array` SKU-level offer evaluation; `null` = order-level. | `null` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| message | `string` Response message. | `Success` |
| status | `number` `1` = success, `0` = failure. | `1` |
| result | `object` EMI calculation results grouped by bank. See [result object description](#result-object-description) for details. | - |

### result object description

The result object contains bank names as keys (e.g., `YES`, `ICICI`, `AXIS`), and each bank has EMI codes as keys (e.g., `EMIY18`, `EMIA6`).

| Parameter | Description | Example |
|-----------|-------------|---------|
| transactionAmount | `number` Original transaction amount. | `10000.0` |
| emiAmount | `number` **Monthly EMI amount**. | `555.56` |
| payBackAmount | `number` Total payback amount. | `0.0` |
| additionalCost | `string` Additional processing cost. | `0.0` |
| emiMdrNote | `number` EMI MDR (Merchant Discount Rate). | `0.0` |
| emiBankInterest | `number` **Bank interest rate (annual %)** | `15.0` |
| bankRate | `number` Bank processing rate. | `0.0` |
| bankCharge | `number` Bank processing charge. | `0.0` |
| cardType | `string` Card type: `credit card` or `debit card`. | `credit card` |
| tenure | `string` EMI tenure. | `18 months` |
| loanAmount | `number` Loan principal amount. | `10000.0` |
| offerKeys | `array` Applied offer keys. | `null` |
| offerDiscount | `object` Offer discount breakdown with fields: total, instant, cashback. | - |
| nceDiscount | `object` **No Cost EMI discount** (interest subvented by merchant) with fields: total, instant, cashback. | - |
| totalPayableAmount | `number` **Total amount payable by customer**. | `10000.0` |
| nceDiscountAmount | `number` **Total interest subvented by merchant**. | `1266.78` |
| revisedPrincipal | `number` Revised principal after discounts. | `10000.0` |
| subventionAmount | `number` Subvention amount. | `10000.0` |
| gstSubvention | `boolean` Whether GST is subvented. | `true` |
| nceViaConfig | `boolean` Whether NCE is via configuration. | `true` |
| bankCode | `string` Bank code. | `YESB` |
| emi_value | `number` EMI per month. | `555.55` |
| emi_interest_paid | `number` **Total interest paid over tenure**. | `1266.78` |
| sku | `array` SKU-level breakdown (if skus parameter was provided). Each SKU contains: skuId, amount, emiAmount, emiInterestPaid, offerDiscount, nceDiscount. | - |