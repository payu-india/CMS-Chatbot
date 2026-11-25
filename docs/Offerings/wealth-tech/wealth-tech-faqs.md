---
title: Wealth Tech FAQs
excerpt: >-
  Answers on merchant type, UPI handles, TPV bank accounts, product object
  checks, SIP versus lump sum, settlement, and testing.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech FAQs
  description: >-
    FAQs for PayU Wealth Tech: merchant setup, SEBI UPI handles, TPV accounts,
    product validation, SIP, and how to test.
  keywords:
    - Wealth Tech FAQ
    - SEBI UPI handle
    - TPV multiple bank accounts
    - SIP versus lump sum
    - mf_partner validation
    - Wealth Tech settlement
    - PayU test key
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

## Getting started

1. #### Who can use Wealth Tech?

<Accordion title="Answer" icon="fa-user">
  SEBI-registered platforms that PayU has set up as a stock broker, a mutual fund broker, a direct AMC, or an Online Bond Platform Provider. Ask your Key Account Manager to set the merchant type. Use one merchant account for each type.
</Accordion>

2. #### Which payment modes can I offer?

<Accordion title="Answer" icon="fa-credit-card">
  UPI, UPI Autopay, eNACH, and Net Banking. Refunds are not available on any Wealth Tech product.
</Accordion>

3. #### How do I register the UPI handle?

<Accordion title="Answer" icon="fa-at">
  Register a validated handle on the SEBI portal. Use the `@valid` handle. Brokers and OBPPs use the `.brk` suffix. AMCs use the `.mf` suffix. Example shapes: `<merchant>.payu1.brk@validaxis` and `<merchant>.payu1.mf@validaxis`. Register a second handle for UPI Autopay. The one-time handle is not the Autopay handle.
</Accordion>

## TPV and the payment request

4. #### Can I send more than one bank account?

<Accordion title="Answer" icon="fa-building-columns">
  Yes. `beneficiarydetail` accepts up to four accounts. Separate account numbers with `|` and send IFSC codes in the same order. PayU collects only from an account in that list.

  ```json
  {"beneficiaryAccountNumber":"1579105002472|50100650144897","ifscCode":"HDFC0001579|HDFC0000145"}
  ```
</Accordion>

5. #### Which api_version do I send?

<Accordion title="Answer" icon="fa-code-branch">
  Equity uses `api_version=6` and does not send `products`. Mutual funds and bonds use `api_version=21` and must send `products`. The request hash is different for equity and for mutual funds and bonds. Use the formula on the build page for your product.
</Accordion>

6. #### Where do I put the investment details?

<Accordion title="Answer" icon="fa-list">
  On `_payment`, send a JSON array in the `products` form field. On a recurring debit, put that array in `var1.more_info[0].wtParams`. Equity never sends a product object.
</Accordion>

## Product object

7. #### Why was my product object rejected?

<Accordion title="Answer" icon="fa-triangle-exclamation">
  Values are case-sensitive. Brokers send one `mutual_fund` object with `mf_partner` `bse`. Direct AMCs send one to 10 objects with `mf_partner` `kfin` and must include `plan`, `folio`, `option`, `scheme`, and `mf_amc_code`. The sum of the product amounts must equal the order amount. OBPPs send one `bond` object with `mf_partner` `nse_bonds`. `bse2`, `nse_mf`, and `cams` are not available yet.
</Accordion>

8. #### What is the difference between lump sum and SIP?

<Accordion title="Answer" icon="fa-rotate">
  `mf_investment_type` `L` is lump sum. `S` is a SIP instalment. For a SIP instalment, `receipt` is the SIP registration number. Bond debits, including a recurring bond debit, send `L`. Mandate registration and pre-debit notification use the existing PayU recurring flow. The Wealth Tech addition is the product object on the debit.
</Accordion>

## Settlement and disputes

9. #### Where does PayU settle the money?

<Accordion title="Answer" icon="fa-money-bill-transfer">
  | Merchant type | Destination |
  | --- | --- |
  | Stock broker | Your bank account |
  | Mutual fund broker | ICCL for `bse` and `bse2`. NCL for `nse_mf` |
  | Direct AMC | Your bank account |
  | OBPP | NSE Clearing Ltd (NCL) |

  PayU does not settle bond payments to your account. Bond payments are supported through NSE only. This guide does not publish a settlement clock. Ask your Key Account Manager for the settlement schedule on your account.
</Accordion>

10. #### Can I refund a Wealth Tech payment?

<Accordion title="Answer" icon="fa-ban">
  No. Refunds are not available for equity, mutual funds, or bonds. Send the customer to the PayU care channel.
</Accordion>

## Testing

11. #### How do I test?

<Accordion title="Answer" icon="fa-flask">
  Use your test key and salt from [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt). Post to `https://test.payu.in/_payment`. Pay from an account you listed in `beneficiarydetail`. This guide does not publish a separate set of Wealth Tech test VPAs or test bank accounts. Verify the reverse hash, then call Verify Payment on the test `postservice` endpoint.
</Accordion>

12. #### The hash matches the standard payment sample and PayU still rejects it. What is wrong?

<Accordion title="Answer" icon="fa-key">
  Wealth Tech does not use the standard payment hash. Equity inserts `beneficiarydetail` before the salt. Mutual funds and bonds continue the string through `udf10`, `beneficiarydetail`, `si_details`, `user_token`, `offer_key`, `offer_auto_apply`, `cart_details`, and `products`. Copy the formula from the build page and hash the exact field strings you post.
</Accordion>
