---
title: Wealth Tech Quick Start
excerpt: >-
  Prepare a Wealth Tech merchant account, the correct merchant type, a SEBI UPI
  handle, and customer bank accounts before you build the payment request.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Quick Start
  description: >-
    Prerequisites for PayU Wealth Tech: merchant type, SEBI UPI handle, TPV
    bank accounts, and links to each product build guide.
  keywords:
    - Wealth Tech quick start
    - PayU merchant type equity
    - SEBI UPI handle registration
    - TPV bank account collection
    - Wealth Tech prerequisites
    - UPI Autopay handle
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

Complete these steps before you build a payment request. They apply to equity, mutual funds, and bonds.

## 1. PayU merchant account with Wealth Tech enabled

You need a PayU merchant account with Wealth Tech enabled. Ask your Key Account Manager to enable it. Test and live keys are different. Retrieve them from the PayU Dashboard. See [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt) and [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).

<KeySaltReference />

Generate the request hash on your server. Do not put your salt in a browser, a mobile app, or a repository.

## 2. Merchant type set by your Key Account Manager

PayU sets the merchant type on the account. Your type decides which product object you send and where the funds settle.

| If you are | Ask PayU to set | Then build |
| --- | --- | --- |
| A stock broker | Equity | [Equity build integration](./equity/equity-build-integration.md) |
| A mutual fund broker | Mutual fund broker | [Mutual funds build integration](./mutual-funds/mutual-funds-build-integration.md) |
| A direct AMC | Direct AMC | [Mutual funds build integration](./mutual-funds/mutual-funds-build-integration.md) |
| An OBPP | Bonds (OBPP) | [Bonds build integration](./bonds/bonds-build-integration.md) |

Use a different merchant account for each merchant type. A value of `mf_partner` that does not match the account is rejected.

## 3. SEBI-registered UPI handle

Register a validated UPI handle on the SEBI portal.

- Use the `@valid` handle.
- Brokers and OBPPs use the `.brk` suffix. Example shape: `<merchant>.payu1.brk@validaxis`.
- AMCs use the `.mf` suffix. Example shape: `<merchant>.payu1.mf@validaxis`.
- Register one handle for UPI and a different handle for UPI Autopay.

<Callout theme="error">
A one-time UPI handle cannot be reused for UPI Autopay. Register both handles before you test those modes.
</Callout>

## 4. Collect the customer's bank account for TPV

TPV is mandatory. Before you create the payment, collect the account number and IFSC the customer will pay from. Send them in `beneficiarydetail`.

- You can send up to four accounts.
- Separate account numbers with `|`.
- Send IFSC codes in the same order as the account numbers.
- PayU rejects a payment from an account that is not in this list.

```json
{"beneficiaryAccountNumber":"1579105002472|50100650144897","ifscCode":"HDFC0001579|HDFC0000145"}
```

The account numbers above are sample values. Send the accounts your customer will pay from.

## 5. Build the request for your product

Payment modes for all three products are UPI, UPI Autopay, eNACH, and Net Banking. Refunds are not available.

| Product | `api_version` | Product object | Build page |
| --- | --- | --- | --- |
| Equity | `6` | Do not send `products` | [Build the equity request](./equity/equity-build-integration.md) |
| Mutual funds | `21` | `products` array, `type` `mutual_fund` | [Build the mutual fund request](./mutual-funds/mutual-funds-build-integration.md) |
| Bonds | `21` | `products` array with one `bond` object | [Build the bond request](./bonds/bonds-build-integration.md) |

<Callout theme="info">
The parameter order in the Wealth Tech request hash is not the standard payment hash. Use the formula on the build page for your product.
</Callout>
