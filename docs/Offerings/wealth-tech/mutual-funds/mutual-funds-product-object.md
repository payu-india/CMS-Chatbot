---
title: Mutual Fund Product Object
excerpt: >-
  Field reference for the mutual fund products array, including broker and
  direct AMC rules, lump sum and SIP samples, and validation limits.
deprecated: false
hidden: false
metadata:
  title: PayU Mutual Fund Product Object
  description: >-
    products JSON for PayU mutual fund payments. Required fields for brokers
    and direct AMCs, lump sum and SIP values, and validation rules.
  keywords:
    - mutual fund products JSON
    - mf_partner bse kfin
    - mf_investment_type L S
    - mf_user_id UCC
    - direct AMC scheme folio
    - Wealth Tech product object
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

`products` is a JSON array. Every value is case-sensitive. If you send more than one object, the sum of the product `amount` values must equal the order `amount`.

A mutual fund broker sends one object. A direct AMC sends one to 10 objects.

<Callout theme="warning">
`bse2`, `nse_mf`, and `cams` are not available yet. Contact your Key Account Manager before you send those `mf_partner` values.
</Callout>

## Fields

| Field | Broker | Direct AMC | Format | Rule |
| --- | --- | --- | --- | --- |
| `type` | Required | Required | String | Must be `mutual_fund`. |
| `mf_partner` | Required | Required | String | Broker: `bse`. AMC: `kfin`. `bse2`, `nse_mf`, and `cams` are not available yet. |
| `amount` | Required | Required | Numeric string, for example `5000` or `5000.50` | Amount for this scheme. |
| `receipt` | Required | Required | Alphanumeric, maximum 25 characters | Your unique reference. For a SIP instalment, the SIP registration number. |
| `mf_member_id` | Required | Required | Maximum 20 characters | Unique member ID issued by the mutual fund platform. |
| `mf_user_id` | Required | Required | Alphanumeric, maximum 10 characters | Unique client code (UCC) of the customer. |
| `mf_investment_type` | Required | Required | `L` or `S` | `L` for lump sum. `S` for SIP. |
| `plan` | Optional | Required | String | Plan of the scheme, for example `GD`. |
| `folio` | Optional | Required | String | Folio number of the customer. |
| `option` | Optional | Required | String | Option of the plan, for example `G` (growth). |
| `scheme` | Optional | Required | String | Scheme code, for example `LT`. |
| `mf_amc_code` | Optional | Required | Alphanumeric, maximum 5 characters | AMC code of the scheme. |

## Samples

<Tabs>
  <Tab title="Broker lump sum">
    ```json
    [
      {
        "type": "mutual_fund",
        "amount": "5000.00",
        "receipt": "REC001",
        "mf_member_id": "12345",
        "mf_user_id": "USR001",
        "mf_partner": "bse",
        "mf_investment_type": "L"
      }
    ]
    ```
  </Tab>
  <Tab title="Direct AMC, two schemes">
    The order `amount` for this payload is `8000`.

    ```json
    [
      {
        "type": "mutual_fund",
        "amount": "5000",
        "receipt": "REC001",
        "mf_member_id": "12345",
        "mf_user_id": "USR001",
        "mf_partner": "kfin",
        "mf_investment_type": "L",
        "plan": "GD",
        "folio": "FOL001",
        "option": "G",
        "scheme": "LT",
        "mf_amc_code": "AXIS"
      },
      {
        "type": "mutual_fund",
        "amount": "3000",
        "receipt": "REC002",
        "mf_member_id": "12345",
        "mf_user_id": "USR001",
        "mf_partner": "kfin",
        "mf_investment_type": "L",
        "plan": "GR",
        "folio": "FOL002",
        "option": "G",
        "scheme": "BP",
        "mf_amc_code": "AXIS"
      }
    ]
    ```
  </Tab>
  <Tab title="SIP instalment">
    Send this shape inside the recurring debit, and use it on the first SIP debit when that debit is a `_payment` request. `receipt` is the SIP registration number. `mf_investment_type` is `S`.

    ```json
    [
      {
        "type": "mutual_fund",
        "amount": "500.00",
        "receipt": "SIPREG12345",
        "mf_member_id": "12345",
        "mf_user_id": "USR001",
        "mf_partner": "bse",
        "mf_investment_type": "S"
      }
    ]
    ```
  </Tab>
</Tabs>

## Validation rules

PayU stops at the first failed check.

| Condition | Error message |
| --- | --- |
| A required field is missing | `Mandatory parameter '<field>' is missing` |
| `type` is not valid | `Type must be one of: mutual_fund, bond` |
| `mf_partner` is not a known value | `mf_partner '<value>' is invalid. Allowed values: bse, bse2, nse_mf, nse_bonds, kfin, cams` |
| `mf_partner` is not allowed for your merchant type | `"mf_partner" value is not allowed for this merchant` |
| A broker sends more than one object | `Multi-product array is not allowed for this merchant` |
| An AMC sends more than 10 objects | `Too many products. Maximum allowed: 10` |
| The sum of product amounts does not equal the order amount | `Sum of product amounts (<total>) does not match order amount (<order_amount>)` |
| An AMC omits `plan`, `folio`, `option`, `scheme`, or `mf_amc_code` | `'<field>' is mandatory for segment <segment>` |

The allowed-values message lists partners that are not available on your account yet. Send only the partner your merchant type can use today: `bse` or `kfin`.
