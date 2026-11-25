---
title: Errors and Troubleshooting
excerpt: >-
  Fix Wealth Tech TPV failures, hash mismatches, rejected product objects, and
  payment modes PayU does not accept on these accounts.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Errors and Troubleshooting
  description: >-
    Common PayU Wealth Tech errors for TPV, hash mismatch, product object
    validation, and unsupported payment modes. Refunds are not available.
  keywords:
    - Wealth Tech errors
    - mf_partner invalid
    - TPV payment rejected
    - hash mismatch PayU
    - product amount mismatch
    - PayU care dispute
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

PayU stops at the first failed check and returns one error. On a `_payment` request, PayU sends that error to your `furl`. On a recurring debit, PayU returns the error in the `si_transaction` response.

<Callout theme="warning">
Refunds are not available for equity, mutual funds, or bonds. PayU care is the path for a customer dispute. Do not call a refund API for these payments.
</Callout>

## Product object errors

These messages apply to mutual funds and bonds. Equity does not send `products`.

| Condition | Error message | What to change |
| --- | --- | --- |
| A required field is missing | `Mandatory parameter '<field>' is missing` | Add the field named in the message. For an AMC, `plan`, `folio`, `option`, `scheme`, and `mf_amc_code` are required. |
| `type` is not `mutual_fund` or `bond` | `Type must be one of: mutual_fund, bond` | Send `mutual_fund` or `bond` in lowercase. |
| `mf_partner` is not a known value | `mf_partner '<value>' is invalid. Allowed values: bse, bse2, nse_mf, nse_bonds, kfin, cams` | Send a known value. Case-sensitive. |
| `mf_partner` does not match the merchant type | `"mf_partner" value is not allowed for this merchant` | Broker: `bse`. AMC: `kfin`. OBPP: `nse_bonds`. |
| A broker or OBPP sends more than one object | `Multi-product array is not allowed for this merchant` | Send one object. |
| An AMC sends more than 10 objects | `Too many products. Maximum allowed: 10` | Split the order. |
| Product amounts do not equal the order amount | `Sum of product amounts (<total>) does not match order amount (<order_amount>)` | Make the sum of `products[].amount` equal `amount`. For bonds, the single amount must equal the order amount. |
| An AMC omits a scheme field | `'<field>' is mandatory for segment <segment>` | Send `plan`, `folio`, `option`, `scheme`, and `mf_amc_code`. |

<Callout theme="warning">
`bse2`, `nse_mf`, and `cams` appear in the allowed-values list and are not available yet. Contact your Key Account Manager before you send them.
</Callout>

## TPV errors

| Condition | What you see | What to change |
| --- | --- | --- |
| The customer pays from a bank account you did not send | PayU rejects the payment | Add that account to `beneficiarydetail`, or ask the customer to pay from a listed account. Maximum four accounts, IFSC codes in the same order. |
| `beneficiarydetail` is missing or is not valid JSON | PayU rejects the payment | Send a JSON object with `beneficiaryAccountNumber` and `ifscCode`. |

<Callout theme="warning">
PayU has not published a stable error code for the equity TPV rejection or for an invalid equity `beneficiarydetail`. Use `error_Message` on the `furl` response, and contact your Key Account Manager if the message is empty.
</Callout>

## Hash mismatch

| Condition | What to change |
| --- | --- |
| Equity hash does not match | Use `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|beneficiarydetail\|SALT)`. Include `beneficiarydetail`. Do not use the mutual fund string. |
| Mutual fund or bond hash does not match | Include `udf1` through `udf10`, then `beneficiarydetail\|si_details\|user_token\|offer_key\|offer_auto_apply\|cart_details\|products\|SALT`. The `products` string in the hash must match the posted field, including key order. |
| Response hash does not match | Use `sha512(SALT\|status\|\|\|\|\|\|udf5\|udf4\|udf3\|udf2\|udf1\|email\|firstname\|productinfo\|amount\|txnid\|key)`. Leave `beneficiarydetail` and `products` out. |
| Recurring hash does not match | Use `sha512(key\|command\|var1\|SALT)` with `command=si_transaction` and the exact `var1` body. |

<Callout theme="warning">
PayU has not published a stable error code for an equity hash mismatch. Compare your string with the formula before you retry. Do not reuse a `txnid` after you change the amount or the product object.
</Callout>

## Payment mode not available

Wealth Tech accepts UPI, UPI Autopay, eNACH, and Net Banking only. Cards, wallets, and EMI are not part of this integration. If the hosted page does not show a mode you expect, confirm with your Key Account Manager that the mode is enabled on this merchant type.

UPI and UPI Autopay also need the SEBI handle: `.brk` for brokers and OBPPs, `.mf` for AMCs, and a separate handle for UPI Autopay.

## api_version

| Product | Value |
| --- | --- |
| Equity | `6` |
| Mutual funds and bonds | `21` |

A mutual fund or bond request sent as `api_version=6` will not carry the `products` contract these pages describe. An equity request sent as `21` uses the wrong hash string.

## Still stuck

Contact your Key Account Manager or the PayU care channel. Include `txnid`, `mihpayid` if you have it, the merchant type, and `error_Message`. Do not send the salt.
