---
title: Bond Product Object
excerpt: >-
  Field reference for the bond products array. Send one object with type bond,
  mf_partner nse_bonds, and mf_investment_type L.
deprecated: false
hidden: false
metadata:
  title: PayU Bond Product Object
  description: >-
    products JSON for PayU bond payments. One nse_bonds object, amount equal to
    the order, and the validation messages PayU returns.
  keywords:
    - bond products JSON
    - nse_bonds mf_partner
    - type bond PayU
    - mf_investment_type L
    - OBPP product object
    - UCC mf_user_id
  robots: index
---

<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#E74C3C"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Send one product object on each bond payment. PayU rejects a request with more than one object. Every value is case-sensitive. The product `amount` must equal the order `amount`.

## Fields

| Field | Required | Format | Rule |
| --- | --- | --- | --- |
| `type` | Yes | String | Must be `bond`. |
| `mf_partner` | Yes | String | Must be `nse_bonds`. |
| `amount` | Yes | Numeric string, for example `5000` or `5000.50` | Must equal the order `amount`. |
| `receipt` | Yes | Alphanumeric, maximum 25 characters | Your unique reference for this payment. |
| `mf_member_id` | Yes | Maximum 20 characters | Your member ID on the exchange. |
| `mf_user_id` | Yes | Alphanumeric, maximum 10 characters | Unique client code (UCC) of the customer. |
| `mf_investment_type` | Yes | `L` | Send `L` (lump sum). |
| `plan`, `option`, `scheme`, `folio`, `mf_amc_code` | No | String | Not used for bonds. You can omit these fields. |

## Sample

```json
[
  {
    "type": "bond",
    "amount": "101.00",
    "receipt": "1234556789012",
    "mf_member_id": "12345",
    "mf_user_id": "77407",
    "mf_partner": "nse_bonds",
    "mf_investment_type": "L"
  }
]
```

Use the same object inside `more_info[0].wtParams` when you debit a registered mandate. Keep `mf_investment_type` as `L`. See [Recurring bond debit](./bonds-recurring-debit.md).

## Validation rules

PayU stops at the first failed check.

| Condition | Error message |
| --- | --- |
| A required field is missing | `Mandatory parameter '<field>' is missing` |
| `type` is not valid | `Type must be one of: mutual_fund, bond` |
| `mf_partner` is not a known value | `mf_partner '<value>' is invalid. Allowed values: bse, bse2, nse_mf, nse_bonds, kfin, cams` |
| `mf_partner` is not `nse_bonds` for a Bonds merchant | `"mf_partner" value is not allowed for this merchant` |
| More than one product object | `Multi-product array is not allowed for this merchant` |
| Product `amount` does not equal the order `amount` | `Sum of product amounts (<total>) does not match order amount (<order_amount>)` |

The allowed-values list includes partners for other Wealth Tech products. For bonds, send `nse_bonds` only.
