---
title: Bond Go-Live Checklist
excerpt: >-
  Confirm the OBPP merchant type, SEBI UPI handle, nse_bonds product object,
  TPV, and webhooks before live bond payments.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Bond Go-Live Checklist
  description: >-
    Go-live checklist for PayU OBPP bond payments: nse_bonds, NSE Clearing
    settlement, TPV, production keys, and webhooks.
  keywords:
    - bond go live PayU
    - OBPP production checklist
    - nse_bonds live
    - NSE Clearing settlement
    - SEBI UPI handle .brk
    - Wealth Tech bonds
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

Complete this checklist before you send live bond traffic to `https://secure.payu.in/_payment`.

## Checklist

- [ ] Your Key Account Manager has set this merchant account to Bonds (OBPP).
- [ ] You expect settlement at NSE Clearing Ltd (NCL), not in your own bank account.
- [ ] Each request sends one object with `type=bond`, `mf_partner=nse_bonds`, and `mf_investment_type=L`.
- [ ] The product amount equals the order amount.
- [ ] A SEBI-validated UPI handle with the `.brk` suffix and the `@valid` handle is registered.
- [ ] A separate UPI handle is registered for UPI Autopay.
- [ ] Live key and salt are the production values, stored on the server. See [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
- [ ] The production payment endpoint is `https://secure.payu.in/_payment`. Recurring debits use `https://info.payu.in/merchant/postservice.php?form=2`.
- [ ] `api_version` is `21`.
- [ ] TPV was tested with an account inside `beneficiarydetail` and an account outside it.
- [ ] The request hash uses the bond string, including `products`, and the response hash omits `beneficiarydetail` and `products`.
- [ ] Verify Payment or a webhook confirms the payment. See [Webhooks](doc:webhooks).
- [ ] Your team knows refunds are not available and that disputes go to the PayU care channel.
- [ ] You have a support contact at PayU for this merchant account.

<Callout theme="warning">
Bond payments are supported through NSE only. Do not send a product object for another exchange.
</Callout>
