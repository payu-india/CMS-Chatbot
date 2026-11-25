---
title: Bonds
excerpt: >-
  Collect bond payments as an OBPP. Send one bond product object with
  mf_partner nse_bonds. PayU settles the funds to NSE Clearing.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Bond Payments
  description: >-
    Bond payments for Online Bond Platform Providers on PayU. TPV is mandatory
    and settlement goes to NSE Clearing (NCL).
  keywords:
    - PayU bond payments
    - OBPP nse_bonds
    - NSE Clearing settlement
    - api_version 21 bonds
    - Wealth Tech OBPP
    - bond TPV payment
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

Use this guide to collect bond payments as an Online Bond Platform Provider (OBPP). With each payment you send the bond details in a `products` array. PayU uses those details to report the payment to NSE Clearing Ltd (NCL).

PayU supports bond payments through NSE only. PayU settles every bond payment to NCL. PayU does not settle bond payments to your account.

## Merchant type

| Merchant type | `mf_partner` | Product object | Where PayU sends the funds |
| --- | --- | --- | --- |
| OBPP | `nse_bonds` | `type` = `bond`. One object | NSE Clearing Ltd (NCL) |

Ask your Key Account Manager to set the merchant type to Bonds (OBPP).

## Payment flow

1. You place the bond order on the exchange.
2. You send the payment request to PayU with `api_version=21`, `beneficiarydetail`, and one `bond` product object.
3. PayU collects the payment from a bank account you sent (TPV).
4. PayU settles the funds to NSE Clearing Ltd (NCL).
5. Verify the response hash, then confirm the payment before you treat the order as paid.

## Before you start

<Callout theme="warning">
TPV is mandatory. Send the customer's bank account and IFSC in `beneficiarydetail` on every bond payment.
</Callout>

<Callout theme="warning">
Refunds are not available for bond payments. Send a customer with a dispute to the PayU care channel.
</Callout>

<Callout theme="info">
PayU does not settle bond payments to your bank account. The destination is NSE Clearing Ltd (NCL).
</Callout>

- Register a validated UPI handle on the SEBI portal. Use the `.brk` suffix and the `@valid` handle. Example shape: `<merchant>.payu1.brk@validaxis`.
- Use one UPI handle for UPI and a different UPI handle for UPI Autopay.
- Payment modes are UPI, UPI Autopay, eNACH, and Net Banking only.
- Set `api_version` to `21`. Send `mf_investment_type` as `L`.

## Next steps

<Cards columns="3">
  <Card title="Build integration" href="./bonds-build-integration.md" icon="fa-code">
    Endpoints, parameters, the bond hash, and a sample products array.
  </Card>
  <Card title="Test integration" href="./bonds-test-integration.md" icon="fa-flask">
    Post to the test endpoint with one nse_bonds object and TPV.
  </Card>
  <Card title="Go-live checklist" href="./bonds-go-live-checklist.md" icon="fa-list-check">
    OBPP merchant type, SEBI handle, production keys, and NCL settlement checks.
  </Card>
</Cards>
