---
title: Test the Bond Integration
excerpt: >-
  Test a bond TPV payment on test.payu.in with one nse_bonds product object,
  api_version 21, and your test key.
deprecated: false
hidden: false
metadata:
  title: Test PayU Wealth Tech Bond Payments
  description: >-
    Test OBPP bond payments on test.payu.in. Check nse_bonds, a single product
    object, TPV, and the request hash.
  keywords:
    - test bond payment PayU
    - nse_bonds sandbox
    - api_version 21 test
    - OBPP TPV test
    - PayU test key
    - bond products validation
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

Test on the test endpoint with your test key and salt.

| Environment | Endpoint |
| --- | --- |
| Test payment | `https://test.payu.in/_payment` |
| Test recurring debit and verify | `https://test.payu.in/merchant/postservice.php?form=2` |

<KeySaltReference />

## What to send

- `api_version=21`
- One object with `type` `bond`, `mf_partner` `nse_bonds`, and `mf_investment_type` `L`
- Product `amount` equal to the order `amount`
- `beneficiarydetail` for the account the test payment will come from
- The bond hash, with the same `products` string you post

This guide does not publish Wealth Tech test bank accounts or test VPAs. Pay from an account listed in `beneficiarydetail`.

## Checks

| Check | Pass condition |
| --- | --- |
| Single object | A second object returns `Multi-product array is not allowed for this merchant`. |
| Partner | `mf_partner` is `nse_bonds`. Another partner returns `"mf_partner" value is not allowed for this merchant`. |
| Amount | A product amount that differs from the order amount is rejected. |
| TPV | A debit from an account you did not send is rejected. |
| Recurring | `command` is `si_transaction` and `mf_investment_type` remains `L`. |
| Response | Reverse hash matches, then Verify Payment returns the same `txnid`. |

## After the test payment

Confirm the payment server-side, then complete the [go-live checklist](./bonds-go-live-checklist.md).
