---
title: Wealth Tech APIs
excerpt: >-
  Endpoints for a Wealth Tech payment, a recurring debit, and Verify Payment,
  with the hash each call uses.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech APIs
  description: >-
    Wealth Tech endpoints for _payment, si_transaction, and verify_payment,
    including test and production URLs and hash formulas.
  keywords:
    - Wealth Tech API
    - _payment api_version
    - si_transaction wtParams
    - verify_payment PayU
    - test.payu.in postservice
    - info.payu.in merchant
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

Use the build page for your product for the field list. This page is the endpoint map.

<Callout theme="error">
Build the `_payment` hash from the equity, mutual fund, or bond build page. The standard payment hash is a different string. Equity uses `api_version=6`. Mutual funds and bonds use `api_version=21`.
</Callout>

## Endpoints

| API | Method and command | Test | Production | Hash |
| --- | --- | --- | --- | --- |
| Collect a payment | `POST` form to `_payment` | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` | Equity: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|beneficiarydetail\|SALT)`. Mutual funds and bonds: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|beneficiarydetail\|si_details\|user_token\|offer_key\|offer_auto_apply\|cart_details\|products\|SALT)` |
| Recurring debit | `POST` form, `command=si_transaction` | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `sha512(key\|command\|var1\|SALT)` |
| Verify payment | `POST` form, `command=verify_payment`, `var1` = `txnid` | `https://test.payu.in/merchant/postservice.php?form=2` | `https://info.payu.in/merchant/postservice.php?form=2` | `sha512(key\|command\|var1\|SALT)` |

## Where to implement each call

| Call | Guide |
| --- | --- |
| Equity `_payment` | [Build the equity payment request](./equity/equity-build-integration.md) |
| Mutual fund `_payment` | [Build the mutual fund payment request](./mutual-funds/mutual-funds-build-integration.md) |
| Mutual fund SIP instalment | [Recurring SIP debit](./mutual-funds/mutual-funds-recurring-sip.md) |
| Bond `_payment` | [Build the bond payment request](./bonds/bonds-build-integration.md) |
| Bond recurring debit | [Recurring bond debit](./bonds/bonds-recurring-debit.md) |
| Equity mandate registration | [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout). Equity adds no product object. |
| Verify Payment | [Verify Payment API](ref:verify_payment_api) |
| Webhooks | [Webhooks](doc:webhooks) |

Response hash for every `_payment` callback:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

Do not put `beneficiarydetail` or `products` in the response hash.

<Callout theme="info">
Mutual fund and bond investment details go in the `products` form field on `_payment`, and in `var1.more_info[0].wtParams` on `si_transaction`. Equity does not send either structure.
</Callout>
