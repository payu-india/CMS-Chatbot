---
title: Wealth Tech
excerpt: >-
  Collect TPV payments for equity, mutual funds, and bonds. Compare merchant
  types, settlement destinations, and the rules every Wealth Tech payment uses.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech — Equity, Mutual Funds, and Bonds
  description: >-
    PayU Wealth Tech for SEBI-registered platforms. TPV payments for equity,
    mutual funds, and bonds, with settlement by merchant type.
  keywords:
    - PayU Wealth Tech
    - equity payments TPV
    - mutual fund payments PayU
    - online bond platform payments
    - SEBI UPI handle
    - ICCL NCL settlement
    - api_version 21
    - beneficiarydetail
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

Wealth Tech lets a SEBI-registered investment platform collect payments for equity, mutual funds, and bonds through PayU. Every payment uses third-party validation (TPV). For mutual funds and bonds, you also send the investment details in a `products` array. PayU uses that array to route the funds and to report the payment.

PayU sets your merchant type when it opens the account. That type decides which `mf_partner` values you can send. Use a separate merchant account for each merchant type.

## Merchant types

| Merchant type | What you sell | Product object | `mf_partner` | Where PayU sends the funds | Dev guide |
| --- | --- | --- | --- | --- | --- |
| Stock broker | Equity trading | Do not send `products` | Not used | Your bank account | [Equity](./equity/index.md) |
| Mutual fund broker | Mutual funds and other investment products | `type` = `mutual_fund`. One object per payment | `bse`. `bse2` and `nse_mf` are not available yet | ICCL for `bse` and `bse2`. NCL for `nse_mf` | [Mutual Funds](./mutual-funds/index.md) |
| Direct AMC | Schemes of your own AMC | `type` = `mutual_fund`. One to 10 objects | `kfin`. `cams` is not available yet | Your bank account | [Mutual Funds](./mutual-funds/index.md) |
| Online Bond Platform Provider (OBPP) | Bonds | `type` = `bond`. One object per payment | `nse_bonds` | NSE Clearing Ltd (NCL) | [Bonds](./bonds/index.md) |

<Callout theme="warning">
`bse2`, `nse_mf`, and `cams` are not available yet. Contact your Key Account Manager before you send those values.
</Callout>

## Rules for every Wealth Tech merchant

<Callout theme="warning">
TPV is mandatory. Send the customer's bank account and IFSC in `beneficiarydetail` on every payment. PayU collects the payment only from an account you send.
</Callout>

<Callout theme="warning">
Refunds are not available on Wealth Tech. Send a customer with a dispute to the PayU care channel.
</Callout>

- **Payment modes.** UPI, UPI Autopay, eNACH, and Net Banking only.
- **UPI handle.** Register a validated UPI handle on the SEBI portal. Use the `@valid` handle. Brokers and OBPPs use the `.brk` suffix. AMCs use the `.mf` suffix. Register one handle for UPI and a different handle for UPI Autopay.
- **API version.** Set `api_version` to `6` for equity. Set it to `21` for mutual funds and bonds.
- **Case.** Every value in a product object is case-sensitive.
- **Reporting.** PayU reports mutual fund and bond payments from the product object. PayU does not report equity payments.

## Choose a product

<Cards columns="3">
  <Card title="Equity" href="./equity/index.md" icon="fa-chart-line">
    Stock brokers. Standard payment request with TPV. No product object. Funds settle to your bank account.
  </Card>
  <Card title="Mutual Funds" href="./mutual-funds/index.md" icon="fa-building-columns">
    Mutual fund brokers and direct AMCs. Send a mutual_fund product object. Brokers settle to ICCL or NCL. AMCs settle to their own bank.
  </Card>
  <Card title="Bonds" href="./bonds/index.md" icon="fa-file-contract">
    OBPPs. Send one bond product object with mf_partner nse_bonds. PayU settles every bond payment to NSE Clearing (NCL).
  </Card>
</Cards>

## Terms

| Term | Meaning |
| --- | --- |
| AMC | Asset management company. It manages mutual fund schemes. |
| ICCL | Indian Clearing Corporation Ltd, the clearing corporation of BSE. |
| NCL | NSE Clearing Ltd, the clearing corporation of NSE. |
| OBPP | Online Bond Platform Provider, a SEBI-registered platform that sells bonds. |
| RTA | Registrar and transfer agent, for example KFintech or CAMS. |
| TPV | Third-party validation. PayU accepts the payment only from a bank account you send. |
| UCC | Unique client code of the customer on the exchange. |

## Next steps

- [How Wealth Tech payments work](./wealth-tech-how-it-works.md)
- [Quick start](./wealth-tech-quick-start.md)
