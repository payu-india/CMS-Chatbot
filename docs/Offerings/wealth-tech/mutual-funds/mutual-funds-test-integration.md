---
title: Test the Mutual Fund Integration
excerpt: >-
  Test a mutual fund TPV payment on test.payu.in with api_version 21 and a
  products array that matches your merchant type.
deprecated: false
hidden: false
metadata:
  title: Test PayU Wealth Tech Mutual Fund Payments
  description: >-
    Test mutual fund Wealth Tech payments on test.payu.in. Check api_version
    21, the products array, TPV, and the request hash.
  keywords:
    - test mutual fund payment
    - api_version 21 test
    - products JSON test
    - TPV mutual fund sandbox
    - PayU test key salt
    - SIP debit test
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
- `beneficiarydetail` for the account the test payment will come from
- `products` for your merchant type: one `bse` object for a broker, or one to 10 `kfin` objects for a direct AMC
- The mutual fund hash, with the same `products` string you post

This guide does not publish Wealth Tech test bank accounts or test VPAs. Pay from an account listed in `beneficiarydetail`. The account numbers in the samples are examples.

<Callout theme="warning">
Do not send `bse2`, `nse_mf`, or `cams` in a test until your Key Account Manager confirms that partner is enabled.
</Callout>

## Checks

| Check | Pass condition |
| --- | --- |
| Broker payload | One object, `type` `mutual_fund`, `mf_partner` `bse`. A second object returns `Multi-product array is not allowed for this merchant`. |
| AMC payload | `mf_partner` `kfin`, and `plan`, `folio`, `option`, `scheme`, and `mf_amc_code` are present. The scheme amounts sum to `amount`. |
| Case | `mutual_fund`, `bse`, `kfin`, `L`, and `S` are lowercase as specified. |
| TPV | A debit from an account you did not send is rejected. |
| Hash | Empty optional fields stay empty in the pipe string. `products` in the hash matches the posted string. |
| SIP instalment | `command` is `si_transaction`, `mf_investment_type` is `S`, and `receipt` is the SIP registration number. |

## After the test payment

Verify the reverse hash, then call Verify Payment with the same `txnid`. Continue to the [go-live checklist](./mutual-funds-go-live-checklist.md) after a `success` you have confirmed server-side.
