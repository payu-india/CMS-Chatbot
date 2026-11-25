---
title: Mutual Funds
excerpt: >-
  Collect mutual fund payments as a broker or a direct AMC. Send api_version 21
  and a mutual_fund product object with each TPV payment.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Mutual Fund Payments
  description: >-
    Mutual fund payments on PayU for brokers and direct AMCs. TPV, api_version
    21, and settlement to ICCL, NCL, or your bank.
  keywords:
    - PayU mutual fund payments
    - mf_partner bse kfin
    - ICCL settlement PayU
    - direct AMC payments
    - api_version 21
    - Wealth Tech SIP
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

Use this guide to collect mutual fund payments as a mutual fund broker or a direct AMC. With each payment you send the fund details in a `products` array. PayU uses those details to send the funds to the correct entity and to report the payment.

## Merchant types

| Merchant type | `mf_partner` | Where PayU sends the funds | Product objects per payment |
| --- | --- | --- | --- |
| Mutual fund broker | `bse`. `bse2` and `nse_mf` are not available yet | ICCL for `bse` and `bse2`. NCL for `nse_mf` | One |
| Direct AMC | `kfin`. `cams` is not available yet | Your bank account | One to 10 |

<Callout theme="warning">
`bse2`, `nse_mf`, and `cams` are not available yet. Contact your Key Account Manager before you send those values.
</Callout>

Ask your Key Account Manager to set the merchant type to mutual fund broker or direct AMC. Use a different merchant account for each type.

## Payment flow

1. Your customer places the order on your platform.
2. You send the payment request to PayU with `api_version=21`, `beneficiarydetail`, and `products`.
3. PayU collects the payment from a bank account you sent.
4. PayU sends the funds to the clearing corporation (broker) or to your bank account (AMC).
5. PayU reports the payment to the exchange (broker) or to the RTA (AMC).
6. Verify the response hash, then confirm the payment before you treat the order as paid.

A lump-sum purchase and the first SIP debit both use this payment request. Later SIP instalments use [Recurring SIP debit](./mutual-funds-recurring-sip.md).

## Before you start

<Callout theme="warning">
TPV is mandatory. Send the customer's bank account and IFSC in `beneficiarydetail` on every mutual fund payment.
</Callout>

<Callout theme="warning">
Refunds are not available for mutual fund payments. Send a customer with a dispute to the PayU care channel.
</Callout>

- Register a validated UPI handle on the SEBI portal. Brokers use the `.brk` suffix. AMCs use the `.mf` suffix. Example shape for an AMC: `<merchant>.payu1.mf@validaxis`.
- Use one UPI handle for UPI and a different UPI handle for UPI Autopay.
- Payment modes are UPI, UPI Autopay, eNACH, and Net Banking only.
- Set `api_version` to `21`. Product object values are case-sensitive.

## Next steps

<Cards columns="3">
  <Card title="Build integration" href="./mutual-funds-build-integration.md" icon="fa-code">
    Endpoints, parameters, the mutual fund hash, and broker versus AMC samples.
  </Card>
  <Card title="Test integration" href="./mutual-funds-test-integration.md" icon="fa-flask">
    Post to the test endpoint and check the product object, TPV, and hash.
  </Card>
  <Card title="Go-live checklist" href="./mutual-funds-go-live-checklist.md" icon="fa-list-check">
    Merchant type, SEBI handle, production keys, and webhook confirmation.
  </Card>
</Cards>
