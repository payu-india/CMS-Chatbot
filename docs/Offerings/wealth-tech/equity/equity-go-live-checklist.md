---
title: Equity Go-Live Checklist
excerpt: >-
  Confirm the equity merchant type, SEBI UPI handle, TPV, production hash, and
  webhooks before you switch to secure.payu.in.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Equity Go-Live Checklist
  description: >-
    Go-live checklist for PayU equity Wealth Tech: production keys, api_version
    6, TPV, SEBI UPI handle, and webhooks.
  keywords:
    - equity go live PayU
    - Wealth Tech production checklist
    - secure.payu.in equity
    - SEBI UPI handle broker
    - equity TPV production
    - PayU webhook equity
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

Complete this checklist before you send live equity traffic to `https://secure.payu.in/_payment`.

## Checklist

- [ ] Your Key Account Manager has set this merchant account to equity.
- [ ] You are using this account for equity only.
- [ ] A SEBI-validated UPI handle with the `.brk` suffix and the `@valid` handle is registered.
- [ ] A separate UPI handle is registered for UPI Autopay.
- [ ] Live `key` and salt come from the production dashboard and are stored on the server. See [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
- [ ] The production endpoint is `https://secure.payu.in/_payment`.
- [ ] `api_version` is `6` and the request does not send `products`.
- [ ] TPV was tested: a payment from an account outside `beneficiarydetail` was rejected, and a payment from a listed account succeeded.
- [ ] The request hash is `sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)`, generated on the server.
- [ ] The response hash is verified before the order is updated, and `beneficiarydetail` is not part of that reverse hash.
- [ ] Verify Payment or a webhook is the confirmation path. Webhook setup: [Webhooks](doc:webhooks).
- [ ] Your team knows refunds are not available and that disputes go to the PayU care channel.
- [ ] You have a support contact at PayU for this merchant account.

<Callout theme="error">
Do not commit the live key or salt. Do not point the production form at `test.payu.in`.
</Callout>
