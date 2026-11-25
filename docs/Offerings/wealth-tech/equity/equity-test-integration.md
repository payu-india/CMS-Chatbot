---
title: Test the Equity Integration
excerpt: >-
  Test an equity TPV payment on test.payu.in with your test key, api_version 6,
  and a beneficiarydetail account you control.
deprecated: false
hidden: false
metadata:
  title: Test PayU Wealth Tech Equity Payments
  description: >-
    Test equity Wealth Tech payments on test.payu.in. Check api_version 6, TPV,
    and the equity hash before production.
  keywords:
    - test equity payment PayU
    - test.payu.in _payment
    - equity TPV test
    - Wealth Tech sandbox
    - test merchant key salt
    - api_version 6 test
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

Test on the test endpoint with your test key and salt. Do not use the production key on this endpoint.

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/_payment` |

<KeySaltReference />

## What to send

- `api_version=6`
- `beneficiarydetail` with the account number and IFSC the test payment will come from
- The equity hash, including `beneficiarydetail`
- No `products` field

The account numbers in the build sample are examples. This guide does not publish a separate list of Wealth Tech test bank accounts or test VPAs. Pay from an account you included in `beneficiarydetail`.

## Checks

| Check | Pass condition |
| --- | --- |
| Endpoint | The request goes to `https://test.payu.in/_payment`. |
| Version | `api_version` is `6`. |
| TPV | The debit account is one of the accounts in `beneficiarydetail`. A different account is rejected. |
| Hash | The hash string matches the equity formula, with empty fields left empty. |
| Response | You verify the reverse hash on `surl` or `furl`, then call Verify Payment with the same `txnid`. |
| Amount | You do not fulfil the order on `pending` or `failure`. |

Payment modes to cover: UPI, Net Banking, and, after the mandate exists, UPI Autopay and eNACH. Recurring equity debits use [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout).

## After the test payment

1. Compare the response hash with `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)`.
2. Call Verify Payment on `https://test.payu.in/merchant/postservice.php?form=2` with `command=verify_payment`.
3. Move to the [go-live checklist](./equity-go-live-checklist.md) only after a successful test payment and a matching Verify Payment status.
