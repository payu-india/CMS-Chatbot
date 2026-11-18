---
title: Merchant Hosted Checkout APIs
excerpt: >-
  Collect Payment and Verify Payment for Merchant Hosted Checkout, plus the
  pre-payment checks named in the method pages.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout APIs
  description: >-
    APIs for PayU Merchant Hosted Checkout: _payment, verify_payment, getBinInfo,
    and validateVPA.
  keywords:
    - payu merchant hosted api
    - payu _payment api
    - payu verify payment api
  robots: index
next:
  description: Explore related information and resources.
---
These are the APIs used in a Merchant Hosted Checkout integration.

***

## Collect Payment

| API | Description |
| --- | --- |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted">Collect Payment API — Merchant Hosted Checkout</Anchor> | Browser form POST. Test `https://test.payu.in/_payment`. Production `https://secure.payu.in/_payment`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_cards">Cards</Anchor> | `pg=CC` plus the card fields. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_netbanking">Net Banking</Anchor> | Bank `bankcode`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets">Wallets</Anchor> | `pg=CASH`. The PayPal Try-it link points here. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_upi">UPI</Anchor> | UPI Collect uses `pg=UPI`, `bankcode=UPI`, and `vpa`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_emi">EMI</Anchor> | Listed in the API index. Steps are not in this folder. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_merchant_hosted_bnpl">BNPL</Anchor> | Listed in the API index. Steps are not in this folder. |

***

## Verify Payment

| API | Description |
| --- | --- |
| <Anchor target="_blank" href="https://docs.payu.in/reference/verify_payment_api">Verify Payment API</Anchor> | `command=verify_payment`. Hash from the APIs page: `sha512(key\|command\|var1\|SALT)`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">Check Action Status</Anchor> | `command=check_action_status`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/get_transaction_info_api">Get Transaction Info</Anchor> | `command=get_transaction_info`. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/refund_transaction_api">Refund Transaction</Anchor> | `command=cancel_refund_transaction`. |

The legacy APIs page says these commands post to `https://info.payu.in/merchant/postservice.php?form=2`.

<!-- VALIDATION NEEDED: BIN and validateVPA samples use https://test.payu.in/merchant/postservice?form=2 without .php. -->

***

## Pre-payment checks

| API | Description |
| --- | --- |
| <Anchor target="_blank" href="https://docs.payu.in/reference/get_bin_info_api">getBinInfo</Anchor> | Card BIN lookup before a card payment. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/validate_vpa_api">validateVPA</Anchor> | VPA check before UPI Collect. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">check_balance</Anchor> | Pluxee balance. The request body is not in this folder. |
| <Anchor target="_blank" href="https://docs.payu.in/reference/get_net_banking_status_api">getNetBankingStatus</Anchor> | Net banking health. The request body is not in this folder. |
