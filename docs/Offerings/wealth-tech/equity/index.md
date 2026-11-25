---
title: Equity
excerpt: >-
  Collect equity payments as a stock broker. Send a TPV payment request with
  api_version 6. PayU settles the funds to your bank account.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Equity Payments
  description: >-
    Equity payments for stock brokers on PayU Wealth Tech. TPV is mandatory,
    api_version is 6, and there is no product object.
  keywords:
    - PayU equity payments
    - stock broker TPV
    - api_version 6
    - equity UPI handle .brk
    - Wealth Tech equity
    - beneficiarydetail equity
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

Use this guide to collect payments for equity trading as a stock broker. Equity uses the standard PayU payment request with TPV. You do not send a product object, and PayU does not report equity payments to an exchange.

## Merchant type

| Merchant type | What you sell | Product object | Where PayU sends the funds |
| --- | --- | --- | --- |
| Stock broker | Equity trading | Do not send `products` | Your bank account |

Ask your Key Account Manager to set the merchant type to equity. Use this account only for equity.

## Payment flow

1. Your customer adds funds or places an order on your platform.
2. You POST the payment request to PayU with `api_version=6` and the customer's bank account in `beneficiarydetail`.
3. PayU collects the payment only from a bank account you sent (TPV).
4. PayU or the bank sends the funds to your bank account.
5. PayU posts the result to your `surl` or `furl`. Verify the response hash before you update the order.

## Before you start

<Callout theme="warning">
TPV is mandatory. Send the customer's bank account and IFSC in `beneficiarydetail` on every equity payment.
</Callout>

<Callout theme="warning">
Refunds are not available for equity payments. Send a customer with a dispute to the PayU care channel.
</Callout>

- Register a validated UPI handle on the SEBI portal. Use the `.brk` suffix and the `@valid` handle. Example shape: `<merchant>.payu1.brk@validaxis`.
- Use one UPI handle for UPI and a different UPI handle for UPI Autopay.
- Payment modes are UPI, UPI Autopay, eNACH, and Net Banking only.
- Set `api_version` to `6`. Do not send `products`.

## Recurring debit

Equity recurring debits (UPI Autopay and eNACH) are standard TPV standing-instruction payments. Equity adds no fields and no product object. Register and debit the mandate with [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout). Keep `beneficiarydetail` on the mandate, and keep `api_version` at `6` on the equity payment request.

## Next steps

<Cards columns="3">
  <Card title="Build integration" href="./equity-build-integration.md" icon="fa-code">
    Endpoints, request parameters, the equity hash, and a sample request.
  </Card>
  <Card title="Test integration" href="./equity-test-integration.md" icon="fa-flask">
    Post to the test endpoint and confirm TPV, hash, and api_version.
  </Card>
  <Card title="Go-live checklist" href="./equity-go-live-checklist.md" icon="fa-list-check">
    Production key, SEBI handle, webhooks, and the checks to finish before live traffic.
  </Card>
</Cards>
