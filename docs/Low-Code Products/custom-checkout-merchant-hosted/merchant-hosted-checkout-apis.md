---
title: Merchant Hosted Checkout APIs
excerpt: The collect and postservice APIs named in the Merchant Hosted source
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout APIs | PayU Developer Docs
  description: >-
    APIs for Merchant Hosted Checkout: POST _payment, verify_payment, getBinInfo, validateVPA, and the refund and transaction-info commands. Formulas are included.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Merchant Hosted Checkout APIs

Merchant Hosted Checkout collects a payment with one browser form POST. Status, BIN, VPA, and refunds are separate command APIs.

## Payment APIs

<Cards columns={2}>
  <Card title="Collect Payment" icon="fa-credit-card" href="https://docs.payu.in/reference/_payment_merchant_hosted">
    Browser form POST to _payment. Test https://test.payu.in/_payment. Production https://secure.payu.in/_payment.
  </Card>
  <Card title="getBinInfo" icon="fa-credit-card" href="https://docs.payu.in/reference/get_bin_info_api">
    Card BIN lookup before a card payment. command=getBinInfo on the postservice URL.
  </Card>
  <Card title="validateVPA" icon="fa-mobile-screen" href="https://docs.payu.in/reference/validate_vpa_api">
    VPA check before UPI Collect. command=validateVPA.
  </Card>
  <Card title="Fetch Balance (Pluxee)" icon="fa-wallet" href="https://docs.payu.in/reference/fetch-balance-api-sodexo">
    check_balance, linked from the Pluxee page. The request is not copied here.
  </Card>
  <Card title="getNetBankingStatus" icon="fa-building-columns" href="https://docs.payu.in/reference/get_net_banking_status_api">
    Linked from the net-banking page. The request is not in this folder.
  </Card>
</Cards>

<!-- DOCUMENTATION GAP: EMI eligibility and BNPL commands are linked from the EMI and BNPL pages and are not named as command values in this folder. -->

## Post-Payment APIs

The current APIs page names these commands. It says the postservice endpoint is `POST https://info.payu.in/merchant/postservice.php?form=2` and the hash is `sha512(key|command|var1|SALT)`.

<Cards columns={2}>
  <Card title="Verify Payment" icon="fa-circle-check" href="https://docs.payu.in/reference/verify_payment_api">
    command verify_payment.
  </Card>
  <Card title="Check Action Status" icon="fa-magnifying-glass" href="https://docs.payu.in/reference/check_action_status_api_with_payu_id">
    command check_action_status. The source titles this "with PayU ID".
  </Card>
  <Card title="Get Transaction Info" icon="fa-receipt" href="https://docs.payu.in/reference/get_transaction_info_api">
    command get_transaction_info. The source says this fetches a transaction by txnid.
  </Card>
  <Card title="Refund Transaction" icon="fa-rotate-left" href="https://docs.payu.in/reference/refund_transaction_api">
    command cancel_refund_transaction.
  </Card>
</Cards>

<!-- VALIDATION NEEDED: Postservice URL.
- APIs page: POST https://info.payu.in/merchant/postservice.php?form=2 (no test URL).
- Cards BIN: test https://test.payu.in/merchant/postservice?form=2 (no .php), production https://info.payu.in/merchant/postservice?form=2 (no .php).
- Validate VPA sample: https://test.payu.in/merchant/postservice?form=2 (no .php).
- The shared Verify Payment block uses postservice.php?form=2 on both test.payu.in and info.payu.in.
Confirm the host and whether the path includes .php. -->

## API Quick Reference

| API | Command or path | Hash in the source | Link |
| --- | --- | --- | --- |
| Collect Payment | `POST /_payment` | `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|Salt)` on the method pages | [Reference](https://docs.payu.in/reference/_payment_merchant_hosted) |
| getBinInfo | `getBinInfo` | Not written next to the sample. Command-API formula below is the candidate | [BIN API](https://docs.payu.in/reference/get_bin_info_api) |
| validateVPA | `validateVPA` | Not written next to the sample | [Validate VPA](https://docs.payu.in/reference/validate_vpa_api) |
| Verify Payment | `verify_payment` | `sha512(key\|command\|var1\|SALT)` | [Verify Payment](https://docs.payu.in/reference/verify_payment_api) |
| Check Action Status | `check_action_status` | `sha512(key\|command\|var1\|SALT)` | [Check Action Status](https://docs.payu.in/reference/check_action_status_api_with_payu_id) |
| Get Transaction Info | `get_transaction_info` | `sha512(key\|command\|var1\|SALT)` | [Get Transaction Info](https://docs.payu.in/reference/get_transaction_info_api) |
| Refund | `cancel_refund_transaction` | `sha512(key\|command\|var1\|SALT)` | [Refund](https://docs.payu.in/reference/refund_transaction_api) |
| Pluxee balance | `check_balance` (name used in prose) | Not in this folder | [Fetch Balance](https://docs.payu.in/reference/fetch-balance-api-sodexo) |
| Net banking health | Not named as a command string beyond getNetBankingStatus | Not in this folder | [Get Net Banking Status](https://docs.payu.in/reference/get_net_banking_status_api) |

<!-- DOCUMENTATION GAP: The APIs page says card and other modes can require an extended or different hash sequence. No alternate sequence is written in this folder. Do not invent one. -->

<!-- VALIDATION NEEDED: The collect-payment hash in the table is the method-page formula. The overview contains a second, shorter Python string. See How It Works. -->

## Specs in this repository

These files are in `reference/`. This page does not extract operations from them.

- `merchant-hosted-_payment.openapi.yaml`
- `merchant-hosted-checkout-postservice.openapi.yaml`
- `merchant-hosted-card-postservice-form2.openapi.yaml`
- `updated_cards_merchant_hosted.json`
- `updated_upi_merchant_hosted.json`
- `updated_wallets_merchant_hosted.json`
- `updated_emi_merchant_hosted.json`
- `updated_bnpl_merchant_hosted.json`
- `Updated_Merchant_Hosted_Card_Checkout_API_with_LRS_Final.json`
- `eft-neft-payu.json`
- `cb_merchant_hosted_cards.json`
- `cb_merchant_hosted_upi.json`
- `cb_merchant_hosted_net_banking.json`
- `Merchant Hosted Checkout.postman_collection_9th_June.json`
- `Merchant Hosted Checkout.postman_collection (2).json`
- `reference/Collect Payment/_payment_merchant_hosted/` (per-method reference pages)
- `reference/Sodexo/fetch-balance-api-sodexo.md`

<!-- DOCUMENTATION GAP: Numbered dumps merchant-hosted-13.json, merchant-hosted-16.json, merchant-hosted-21.json, merchant-hosted-25.json, merchant-hosted-26.json, merchant-hosted-34.json, merchant-hosted-36.json, merchant-hosted-40.json, merchant-hosted-41.json, and merchant-hosted-42.json are in reference/. This folder does not say which dump is current. They are not wired in as the spec. -->
