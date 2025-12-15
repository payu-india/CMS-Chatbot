---
title: Registration Mandate for Cards - PACB
deprecated: false
hidden: true
metadata:
  robots: index
---
For Standing Instruction (SI) mandate registrations, append the following parameters to your basic S2S payload.

### Required Parameters

```bash
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'user_credentials=PRiQvJ:customer_1112' \
--data-urlencode 'si_details={"billingAmount":"200.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2025-06-05","paymentEndDate":"2025-12-01","siTokenRequestor":"2"}' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1'
```

### Request Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pg` | Payment gateway type | Yes |
| `bankcode` | Bank code (`CC` for credit cards) | Yes |
| `user_credentials` | Format: `merchant_key:customer_id`. Optional during SI registration. Use if you want customers to pay using the card tokenized during mandate registration. | Optional |
| `si_details` | JSON object containing mandate details. Refer to [SI Parameter JSON Details](ref:si-parameter-json-details). | Yes |
| `api_version` | Must be set to `7` for SI transactions | Yes |
| `si` | Set to `1` to enable Standing Instruction | Yes |

### si_details Object Structure

```json
{
  "billingAmount": "200.00",
  "billingCurrency": "INR",
  "billingCycle": "ADHOC",
  "billingInterval": 1,
  "paymentStartDate": "2025-06-05",
  "paymentEndDate": "2025-12-01",
  "siTokenRequestor": "2"
}
```

| Field | Description | Example |
|-------|-------------|---------|
| `billingAmount` | Maximum amount for recurring transactions | `200.00` |
| `billingCurrency` | Currency code | `INR` |
| `billingCycle` | Billing frequency (`DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ADHOC`) | `ADHOC` |
| `billingInterval` | Interval between billing cycles | `1` |
| `paymentStartDate` | Mandate start date (YYYY-MM-DD) | `2025-06-05` |
| `paymentEndDate` | Mandate end date (YYYY-MM-DD) | `2025-12-01` |
| `siTokenRequestor` | Token requestor ID. Set to `2` for mandate registrations. | `2` |

---

## Hash Generation for SI Transactions

> ⚠️ Important:
>
> When `api_version=7` is passed in the payload, the `hash` must be generated with the following sequence:

```
SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||si_details|SALT)
```

---

## Using Network Tokens with Mandates

For mandate registration using network tokens:

1. Set `siTokenRequestor` to `2` in the `si_details` object
2. Provide network token details using the [Update SI API](ref:update-si-api) after registration

> 📘 Note:
>
> Network token details cannot be passed during mandate registration. Use the Update SI API to add network token information after the mandate is registered.