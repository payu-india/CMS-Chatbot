---
title: Wealth Tech
excerpt: >-
  Collect payments for equity, mutual funds, and bonds through PayU. For  
  SEBI-registered investment platforms — stock brokers, mutual fund brokers,  
  direct AMCs, and OBPPs.
deprecated: false
hidden: true
metadata:
  robots: index
---
Wealth Tech lets SEBI-registered investment platforms collect payments for equity, mutual funds, and bonds through PayU. All Wealth Tech payments use third-party validation (TPV) — PayU collects the payment only from the bank account your customer provides at the time of payment.

***

<Callout icon="⚠️" theme="warning">
  ### Rules for all Wealth Tech merchants

  - **Payment modes:** UPI, UPI Autopay, eNACH, and Net Banking only. Cards and wallets are not supported.
  - **TPV is mandatory.** Send the customer's bank account number and IFSC in `beneficiarydetail` with every payment request.
  - **Refunds are not available.** Direct customers with a dispute to the [PayU care channel](https://help.payu.in/query).
  - **UPI handle:** Register a validated UPI handle on the SEBI portal before going live. Use `.brk` for brokers and OBPPs; `.mf` for AMCs. Use separate handles for UPI and UPI Autopay.
  - **Product object values are case-sensitive.**
</Callout>

***

## Who Can Use Wealth Tech

Find your merchant type and their guides in the following table.

| Merchant type                        | What you sell                              | `type`                | `mf_partner`       | Where PayU sends the funds | Guide                                                                                       |
| ------------------------------------ | ------------------------------------------ | --------------------- | ------------------ | -------------------------- | ------------------------------------------------------------------------------------------- |
| Stock broker                         | Equity trading                             | _(no product object)_ | _(not applicable)_ | Your bank account          | <Anchor target="_blank" href="https://docs.payu.in/docs/equity">Equity</Anchor>             |
| Mutual fund broker                   | Mutual funds and other investment products | `mutual_fund`         | `bse`, `bse2`      | ICCL or NCL                | <Anchor target="_blank" href="https://docs.payu.in/docs/mutual-funds">Mutual Funds</Anchor> |
| Direct AMC                           | Mutual fund schemes of your own AMC        | `mutual_fund`         | `kfin`             | Your bank account          | [Mutual Funds](https://docs.payu.in/docs/mutual-funds)                                      |
| Online Bond Platform Provider (OBPP) | Bonds                                      | `bond`                | `nse_bonds`        | NSE Clearing Ltd (NCL)     | <Anchor target="_blank" href="https://docs.payu.in/docs/bonds">Bonds</Anchor>               |

PayU sets your merchant type when it opens your account. Your merchant type determines which `mf_partner` values you can use. Use a separate merchant account for each merchant type.

***

## How a Wealth Tech Payment Works

1. Your customer places an order on your platform.
2. You send a payment request to PayU, including the customer's bank account details. For mutual funds and bonds, you also send a `products` object with the investment details.
3. PayU collects the payment only from the bank account you specified (TPV).
4. PayU sends the funds to the clearing corporation or your bank account, depending on your merchant type. See the table above.
5. For mutual funds and bonds, PayU reports the payment using the details in the `products` object. PayU does not report equity payments.

***

## Choose Your Dev Guide

<Cards>
  <Card title="Equity" href="https://docs.payu.in/docs/equity" icon="far fa-chart-line" target="_blank">
    For stock brokers. Collect payments for equity trading with TPV. No product object required.
  </Card>

  <Card title="Mutual Funds" href="https://docs.payu.in/docs/mutual-funds" icon="far fa-coins" target="_blank">
    For mutual fund brokers and direct AMCs. Send fund details in a product object with each payment.
  </Card>

  <Card title="Bonds" href="https://docs.payu.in/docs/bonds" icon="far fa-file-contract" target="_blank">
    For Online Bond Platform Providers (OBPPs). Send bond details in a product object. PayU settles to NSE Clearing.
  </Card>
</Cards>

***

## Terms

| Term | Meaning                                                                           |
| ---- | --------------------------------------------------------------------------------- |
| AMC  | Asset management company. Manages mutual fund schemes.                            |
| ICCL | Indian Clearing Corporation Ltd — the clearing corporation of BSE.                |
| NCL  | NSE Clearing Ltd — the clearing corporation of NSE.                               |
| OBPP | Online Bond Platform Provider — a SEBI-registered platform that sells bonds.      |
| RTA  | Registrar and transfer agent, for example KFintech or CAMS.                       |
| TPV  | Third-party validation. PayU accepts payment only from the bank account you send. |
| UCC  | Unique client code of the customer on the exchange.                               |