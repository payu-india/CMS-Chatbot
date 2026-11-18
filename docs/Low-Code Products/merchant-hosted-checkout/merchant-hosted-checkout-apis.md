---
title: Merchant Hosted Checkout APIs
excerpt: Payment, pre-payment, and post-payment APIs named in the Merchant Hosted Checkout guides
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout APIs | PayU Developer Docs
  description: >-
    APIs for PayU Merchant Hosted Checkout: _payment, getBinInfo, validateVPA, verify_payment, and the post-service hash sha512(key|command|var1|SALT).
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Merchant Hosted Checkout APIs

These are the APIs named in the Merchant Hosted integration pages. Field-level detail stays on the method pages and in the existing API reference. This page does not add parameters from the OpenAPI files.

## Payment APIs

<Cards columns={2}>
  <Card title="Collect Payment — _payment" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Browser form POST. Test `https://test.payu.in/_payment`. Production `https://secure.payu.in/_payment`.
  </Card>
  <Card title="Cards" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">
    Merchant Hosted cards reference, including the Try-it page linked from the cards guide.
  </Card>
  <Card title="UPI" icon="fa-mobile-screen" href="https://docs.payu.in/reference/_payment_merchant_hosted_upi">
    Merchant Hosted UPI reference.
  </Card>
  <Card title="Wallets" icon="fa-wallet" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">
    Merchant Hosted wallets reference. The PayPal page points here for Try-it.
  </Card>
  <Card title="Net Banking" icon="fa-building-columns" href="https://docs.payu.in/reference/_payment_merchant_hosted_netbanking">
    Merchant Hosted net banking reference.
  </Card>
  <Card title="EMI" icon="fa-calendar" href="https://docs.payu.in/reference/_payment_merchant_hosted_emi">
    Linked from the API reference index. The EMI steps are not in this folder.
  </Card>
  <Card title="BNPL" icon="fa-clock" href="https://docs.payu.in/reference/_payment_merchant_hosted_bnpl">
    Linked from the API reference index. The BNPL steps are not in this folder.
  </Card>
</Cards>

OpenAPI and collection files in this repo, for the reference pages to link. Do not mine them for fields that the guides do not already state:

- `reference/merchant-hosted-_payment.openapi.yaml`
- `reference/updated_cards_merchant_hosted.json`
- `reference/updated_upi_merchant_hosted.json`
- `reference/updated_wallets_merchant_hosted.json`
- `reference/updated_emi_merchant_hosted.json`
- `reference/updated_bnpl_merchant_hosted.json`
- `reference/Merchant Hosted Checkout.postman_collection (2).json`

Cross-border specs are out of scope for this guide.

## Pre-payment APIs

<Cards columns={2}>
  <Card title="getBinInfo" icon="fa-magnifying-glass" href="https://docs.payu.in/reference/get_bin_info_api">
    Card BIN lookup before `_payment`. Sample command is `getBinInfo`.
  </Card>
  <Card title="validateVPA" icon="fa-at" href="https://docs.payu.in/reference/validate_vpa_api">
    VPA check before UPI Collect. Sample command is `validateVPA`.
  </Card>
  <Card title="check_balance" icon="fa-wallet" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">
    Pluxee balance check. The request body is not in this folder.
  </Card>
  <Card title="getNetBankingStatus" icon="fa-heart-pulse" href="https://docs.payu.in/reference/get_net_banking_status_api">
    Net banking health check. The request body is not in this folder.
  </Card>
</Cards>

<!-- DOCUMENTATION GAP: check_balance and getNetBankingStatus request and response bodies are not in the Merchant Hosted pages. -->

## Post-Payment APIs

The legacy APIs page says post-service calls go to:

```
POST https://info.payu.in/merchant/postservice.php?form=2
```

Hash:

```
sha512(key|command|var1|SALT)
```

<!-- VALIDATION NEEDED: BIN and validateVPA samples use https://test.payu.in/merchant/postservice?form=2 without .php. The BIN production URL on the cards page also omits .php. -->

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    `command=verify_payment`. Confirm status before you fulfil the order.
  </Card>
  <Card title="Check Action Status" icon="fa-list-check" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">
    `command=check_action_status`.
  </Card>
  <Card title="Get Transaction Info" icon="fa-receipt" href="https://docs.payu.in/reference/get_transaction_info_api">
    `command=get_transaction_info`.
  </Card>
  <Card title="Refund Transaction" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    `command=cancel_refund_transaction`.
  </Card>
</Cards>

## API Quick Reference

| API | command or path | Hash | Link |
| --- | --- | --- | --- |
| Collect Payment | `POST /_payment` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` | [Reference](https://docs.payu.in/reference/_payment_merchant_hosted) |
| Verify Payment | `verify_payment` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/verify_payment_api) |
| Check Action Status | `check_action_status` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/check_action_status_api_with_payu_id) |
| Get Transaction Info | `get_transaction_info` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/get_transaction_info_api) |
| Refund | `cancel_refund_transaction` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/refund_transaction_api) |
| BIN | `getBinInfo` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/get_bin_info_api) |
| Validate VPA | `validateVPA` | `sha512(key\|command\|var1\|SALT)` | [Reference](https://docs.payu.in/reference/validate_vpa_api) |

<!-- VALIDATION NEEDED: The legacy APIs page says the _payment hash base sequence matches hosted checkout, and that card and other modes can require a different sequence. It does not print the alternate sequence. The post-service hash above is applied to getBinInfo and validateVPA because the APIs page states that formula for post-service commands. Confirm it for those two commands. -->

Related OpenAPI for post-service, not used to add fields on this page:

- `reference/merchant-hosted-checkout-postservice.openapi.yaml`
- `reference/merchant-hosted-card-postservice-form2.openapi.yaml`
