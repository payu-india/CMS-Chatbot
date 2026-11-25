---
title: How Wealth Tech Payments Work
excerpt: >-
  Follow a Wealth Tech payment from the customer order to TPV collection,
  settlement, and reporting. Equity, mutual funds, and bonds diverge after the debit.
deprecated: false
hidden: false
metadata:
  title: How PayU Wealth Tech Payments Work
  description: >-
    End-to-end PayU Wealth Tech flow: TPV collection, equity versus mutual fund
    and bond settlement, UPI handles, and api_version.
  keywords:
    - Wealth Tech payment flow
    - PayU TPV SEBI
    - equity settlement merchant bank
    - mutual fund ICCL settlement
    - bond payment NSE Clearing
    - UPI handle .brk .mf
    - api_version 6 and 21
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

A Wealth Tech payment starts on your platform and is collected by PayU from a bank account you name. Where the money goes, and whether PayU reports the payment, depends on your merchant type.

## Shared payment flow

1. Your customer places an order on your platform.
2. You POST a payment request to PayU. You include the customer's bank account in `beneficiarydetail`. Mutual funds and bonds also send the `products` array.
3. PayU opens the hosted payment page. The customer can pay with UPI, UPI Autopay, eNACH, or Net Banking.
4. PayU collects the payment only from a bank account you sent (TPV).
5. PayU sends the funds to the clearing corporation or to your bank account. See the merchant-type table on [Wealth Tech](./index.md).
6. For mutual funds and bonds, PayU reports the payment with the details from the product object. PayU does not report equity payments.
7. PayU posts the result to your `surl` or `furl`. Verify the response hash, then confirm the status with the Verify Payment API or a webhook before you fulfil the order.

<Callout theme="error">
Equity requests use `api_version=6` and do not send `products`. Mutual fund and bond requests use `api_version=21` and must send `products`. A request with the wrong version or the wrong hash is rejected.
</Callout>

## Equity flow

1. The customer adds funds or places an order on your platform.
2. You send the standard PayU payment request with `api_version=6` and `beneficiarydetail`. Do not send `products`.
3. PayU collects the payment from the named bank account.
4. PayU or the bank sends the funds to your bank account.

Recurring equity debits use the standard PayU standing-instruction flow with TPV. Equity adds no fields and no product object. See [Equity](./equity/index.md) and [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout).

## Mutual fund and bond flow

1. The customer places the order on your platform. For bonds, place the order on the exchange first.
2. You send `api_version=21`, `beneficiarydetail`, and a `products` JSON array.
3. PayU collects the payment from the named bank account.
4. PayU sends the funds to the destination for your merchant type:
   - Mutual fund broker: ICCL when `mf_partner` is `bse` or `bse2`, NCL when `mf_partner` is `nse_mf`.
   - Direct AMC: your bank account.
   - OBPP: NSE Clearing Ltd (NCL). PayU does not settle bond payments to your account. Bond payments are supported through NSE only.
5. PayU reports the payment to the exchange (mutual fund broker), to the RTA (direct AMC), or to NCL (bonds).

A mutual fund broker sends one product object. A direct AMC can send one to 10 objects, and the sum of the product amounts must equal the order amount. A bond payment sends exactly one object.

## Why TPV is mandatory

TPV is mandatory for every Wealth Tech merchant. You send the customer's account number and IFSC in `beneficiarydetail`. PayU accepts the debit only from one of those accounts. You can send up to four accounts. Separate account numbers with `|` and send the IFSC codes in the same order.

This is how PayU keeps the collection on the customer's own account for a SEBI-registered equity, mutual fund, or bond payment. A payment from any other account is rejected.

## UPI handle

Register a validated UPI handle on the SEBI portal before you take live UPI or UPI Autopay payments.

| Merchant | Suffix | Example shape |
| --- | --- | --- |
| Stock broker, mutual fund broker, OBPP | `.brk` | `<merchant>.payu1.brk@validaxis` |
| Direct AMC | `.mf` | `<merchant>.payu1.mf@validaxis` |

Use the `@valid` handle. Register one handle for one-time UPI and a different handle for UPI Autopay.

## After the payment

| Outcome | Callback | What you do |
| --- | --- | --- |
| `success` | `surl` | Verify the response hash, then confirm with Verify Payment or a webhook before you treat the order as paid. |
| `failure` | `furl` | Do not fulfil the order. PayU returns one error for the first check that failed. |
| `pending` | `surl` | Do not fulfil the order. Confirm the final status with Verify Payment. Treat only `success` as a successful payment. |

The browser redirect can be dropped. Use a [webhook](doc:webhooks) or the [Verify Payment API](ref:verify_payment_api) as the confirmation your server trusts.

## Next steps

<Cards columns="2">
  <Card title="Quick start" href="./wealth-tech-quick-start.md" icon="fa-flag">
    Account, merchant type, UPI handle, and the bank accounts you must collect.
  </Card>
  <Card title="Equity, mutual funds, or bonds" href="./index.md" icon="fa-list">
    Open the dev guide for your merchant type.
  </Card>
</Cards>
