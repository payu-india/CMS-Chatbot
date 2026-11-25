---
title: Mutual Fund Go-Live Checklist
excerpt: >-
  Confirm broker or AMC setup, the SEBI UPI handle, TPV, the products hash, and
  webhooks before you call secure.payu.in.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Mutual Fund Go-Live Checklist
  description: >-
    Go-live checklist for PayU mutual fund payments: merchant type, SEBI UPI
    handle, api_version 21, TPV, and webhooks.
  keywords:
    - mutual fund go live PayU
    - SEBI UPI handle AMC
    - ICCL production payment
    - api_version 21 production
    - Wealth Tech checklist
    - kfin bse go live
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

Complete this checklist before you send live mutual fund traffic to `https://secure.payu.in/_payment`.

## Checklist

- [ ] Your Key Account Manager has set this account to mutual fund broker or direct AMC.
- [ ] You are using a separate account for this merchant type.
- [ ] Brokers send `mf_partner=bse` and one product object. AMCs send `mf_partner=kfin` and the AMC fields `plan`, `folio`, `option`, `scheme`, and `mf_amc_code`.
- [ ] You are not sending `bse2`, `nse_mf`, or `cams` unless your Key Account Manager has confirmed that partner.
- [ ] The SEBI UPI handle is registered: `.brk` for a broker, `.mf` for an AMC, on the `@valid` handle.
- [ ] A separate handle is registered for UPI Autopay.
- [ ] Live key and salt are the production values, stored on the server. See [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
- [ ] The production payment endpoint is `https://secure.payu.in/_payment`. Recurring debits use `https://info.payu.in/merchant/postservice.php?form=2`.
- [ ] `api_version` is `21`.
- [ ] TPV was tested with an account inside `beneficiarydetail` and an account outside it.
- [ ] The request hash includes `udf1` through `udf10`, `beneficiarydetail`, `si_details`, `user_token`, `offer_key`, `offer_auto_apply`, `cart_details`, and `products`, in that order, then the salt.
- [ ] The response hash is verified, and it does not include `beneficiarydetail` or `products`.
- [ ] SIP instalments set `mf_investment_type` to `S` and `receipt` to the SIP registration number.
- [ ] Verify Payment or a webhook confirms the payment. See [Webhooks](doc:webhooks).
- [ ] Your team knows refunds are not available and that disputes go to the PayU care channel.
- [ ] You have a support contact at PayU for this merchant account.
