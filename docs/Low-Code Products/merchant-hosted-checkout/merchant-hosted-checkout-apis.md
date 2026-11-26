---
title: Merchant Hosted Checkout APIs
excerpt: Collect Payment, BIN and VPA checks, and the post-payment commands used by this integration
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout APIs | PayU Developer Docs
  description: >-
    API index for PayU Merchant Hosted Checkout. _payment, getBinInfo, validateVPA, verify_payment, and the post-service hash sha512(key|command|var1|SALT).
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Merchant Hosted Checkout APIs

These are the APIs named by the Merchant Hosted integration guides. Collect Payment is a browser form POST. The other calls are post-service `command` requests.

## Payment APIs

<Cards columns={2}>
  <Card title="Collect Payment" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Browser form POST to `_payment`. Test `https://test.payu.in/_payment`. Production `https://secure.payu.in/_payment`.
  </Card>
  <Card title="Cards" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">
    Card fields, saved card, and 3DS. The cards guide links here.
  </Card>
  <Card title="Wallets and PayPal" icon="fa-wallet" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">
    The PayPal page points its Try It flow here.
  </Card>
  <Card title="UPI" icon="fa-mobile-screen" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    UPI Collect posts to the same `_payment` URL. The UPI guide links the Collect Payment reference.
  </Card>
</Cards>

OpenAPI files in this repository for the same APIs:

- `reference/merchant-hosted-_payment.openapi.yaml`
- `reference/updated_cards_merchant_hosted.json`
- `reference/updated_upi_merchant_hosted.json`
- `reference/updated_wallets_merchant_hosted.json`
- `reference/updated_emi_merchant_hosted.json`
- `reference/updated_bnpl_merchant_hosted.json`
- `reference/merchant-hosted-checkout-postservice.openapi.yaml`

## Pre-payment APIs

| API | command | Where it is documented |
| --- | --- | --- |
| BIN info | `getBinInfo` | [Cards](./integration-guide/build-integration/cards). Reference: [BIN APIs](https://docs.payu.in/reference/get_bin_info_api). |
| Validate VPA | `validateVPA` | [UPI Collect](./integration-guide/build-integration/upi-collect). Reference: [Validate VPA](https://docs.payu.in/reference/validate_vpa_api). |
| Pluxee balance | `check_balance` | Named on the Pluxee page. Reference: [Fetch Balance API](https://docs.payu.in/reference/fetch-balance-api-sodexo). |
| Net banking status | Not stated as a `command` value in this folder. The guide names the getNetBankingStatus API. | [Net Banking](./integration-guide/build-integration/net-banking). Reference: [Get Net Banking Status API](ref:get_net_banking_status_api). |

<!-- DOCUMENTATION GAP: check_balance and getNetBankingStatus request bodies are not in this folder. getBinInfo has a sample. The prose and the sample disagree on var1. -->

The `getBinInfo` and `validateVPA` samples post to `https://test.payu.in/merchant/postservice?form=2`.

## Post-Payment APIs

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    `command=verify_payment`. Confirm the payment after the callback.
  </Card>
  <Card title="Check Action Status" icon="fa-magnifying-glass" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">
    `command=check_action_status`.
  </Card>
  <Card title="Get Transaction Info" icon="fa-receipt" href="https://docs.payu.in/reference/get_transaction_info_api">
    `command=get_transaction_info`.
  </Card>
  <Card title="Refund Transaction" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    `command=cancel_refund_transaction`. PayPal refunds need funds in the PayPal wallet.
  </Card>
</Cards>

The API index states the post-service endpoint as:

```
POST https://info.payu.in/merchant/postservice.php?form=2
```

<!-- VALIDATION NEEDED: Cards BIN production is https://info.payu.in/merchant/postservice?form=2 (no .php). The line above includes .php, as written on the API index page. -->

Post-service hash stated on that page:

```
sha512(key|command|var1|SALT)
```

## API Quick Reference

| API | command | Hash | Link |
| --- | --- | --- | --- |
| Collect Payment | Browser POST, no `command` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` | [\_payment](https://docs.payu.in/reference/_payment_merchant_hosted) |
| BIN info | `getBinInfo` | `sha512(key\|command\|var1\|SALT)` | [getBinInfo](https://docs.payu.in/reference/get_bin_info_api) |
| Validate VPA | `validateVPA` | `sha512(key\|command\|var1\|SALT)` | [validateVPA](https://docs.payu.in/reference/validate_vpa_api) |
| Verify Payment | `verify_payment` | `sha512(key\|command\|var1\|SALT)` | [verify_payment](https://docs.payu.in/reference/verify_payment_api) |
| Check Action Status | `check_action_status` | `sha512(key\|command\|var1\|SALT)` | [check_action_status](https://docs.payu.in/reference/check_action_status_api_with_payu_id) |
| Get Transaction Info | `get_transaction_info` | `sha512(key\|command\|var1\|SALT)` | [get_transaction_info](https://docs.payu.in/reference/get_transaction_info_api) |
| Refund | `cancel_refund_transaction` | `sha512(key\|command\|var1\|SALT)` | [refund](https://docs.payu.in/reference/refund_transaction_api) |
| Pluxee balance | `check_balance` | Not stated in this folder | [Fetch Balance](https://docs.payu.in/reference/fetch-balance-api-sodexo) |
| Net banking status | Not stated in this folder | Not stated in this folder | [getNetBankingStatus](ref:get_net_banking_status_api) |

EMI, BNPL, and Provision Alt ID are linked from the method pages. Their `command` values are not stated in this folder, so they are not given rows here.

- [EMI with a credit card](doc:collect-payments-with-emi-using-credit-card)
- [Merchant Hosted BNPL workflow](https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted)
- [Provision Alt ID API](https://docs.payu.in/reference/provision-alt-id-api)
