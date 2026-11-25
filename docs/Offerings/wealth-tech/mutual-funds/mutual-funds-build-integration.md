---
title: Build the Mutual Fund Payment Request
excerpt: >-
  POST a mutual fund payment with api_version 21, beneficiarydetail, a products
  array, and the mutual fund SHA-512 hash.
deprecated: false
hidden: false
metadata:
  title: Build a PayU Wealth Tech Mutual Fund Payment
  description: >-
    Mutual fund _payment request: api_version 21, products JSON, TPV
    beneficiarydetail, and the SHA-512 hash for brokers and direct AMCs.
  keywords:
    - mutual fund payment request
    - api_version 21 products
    - mf_partner bse
    - mf_partner kfin
    - Wealth Tech hash products
    - beneficiarydetail mutual fund
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

Send a `POST` with form data (`application/x-www-form-urlencoded`) for a lump-sum purchase or the first SIP debit. Generate the hash on your server.

<Callout theme="warning">
TPV is mandatory. `beneficiarydetail` is required on every mutual fund request.
</Callout>

<Callout theme="error">
Set `api_version` to `21`. `products` is required. Use the hash string on this page. The standard payment hash does not include `products` or `beneficiarydetail`.
</Callout>

## Environments

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

## Request parameters

<Accordion title="Mutual fund payment parameters" icon="fa-table">
  | Parameter | Required | Description |
  | --- | --- | --- |
  | `key` | Yes | Your merchant key. |
  | `txnid` | Yes | Your unique transaction ID. |
  | `amount` | Yes | Order amount. |
  | `productinfo` | Yes | Short description of the order. |
  | `firstname` | Yes | First name of the customer. |
  | `email` | Yes | Email address of the customer. |
  | `phone` | Yes | Phone number of the customer. |
  | `surl` | Yes | URL that receives the response for a successful payment. |
  | `furl` | Yes | URL that receives the response for a failed payment. |
  | `api_version` | Yes | Set to `21`. |
  | `beneficiarydetail` | Yes | Bank accounts and IFSC codes of the customer, for TPV. JSON. Maximum 4 accounts. |
  | `products` | Yes | Mutual fund product objects, as a JSON array. See [Product object](./mutual-funds-product-object.md). |
  | `hash` | Yes | SHA-512 hash. Use the formula below. |
</Accordion>

## Hash formula

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|beneficiarydetail|si_details|user_token|offer_key|offer_auto_apply|cart_details|products|SALT)
```

Keep a field empty in the hash string if you do not send it. Keep every `|` separator. Put the same `beneficiarydetail` string and the same `products` string in the hash that you post in the form. Do not rebuild the JSON with different spacing or key order.

[Generate Hash](doc:hashing-request-and-response) documents the standard payment hash. Mutual fund requests use the longer string above.

## beneficiarydetail format

To send more than one bank account, separate the values with `|`. Send the IFSC codes in the same order as the accounts.

```json
{"beneficiaryAccountNumber":"1579105002472|50100650144897","ifscCode":"HDFC0001579|HDFC0000145"}
```

These account numbers are sample values.

## products samples

Field rules are on [Product object](./mutual-funds-product-object.md).

<Tabs>
  <Tab title="Mutual fund broker">
    One object. `mf_partner` is `bse` for a live broker payment. `mf_investment_type` is `L` for lump sum.

    ```json
    [{"type":"mutual_fund","amount":"5000.00","receipt":"REC001","mf_member_id":"12345","mf_user_id":"USR001","mf_partner":"bse","mf_investment_type":"L"}]
    ```
  </Tab>
  <Tab title="Direct AMC">
    One to 10 objects. This sample is two schemes whose amounts sum to the order amount `8000`. `mf_partner` is `kfin`. `plan`, `folio`, `option`, `scheme`, and `mf_amc_code` are required for a direct AMC.

    ```json
    [{"type":"mutual_fund","amount":"5000","receipt":"REC001","mf_member_id":"12345","mf_user_id":"USR001","mf_partner":"kfin","mf_investment_type":"L","plan":"GD","folio":"FOL001","option":"G","scheme":"LT","mf_amc_code":"AXIS"},{"type":"mutual_fund","amount":"3000","receipt":"REC002","mf_member_id":"12345","mf_user_id":"USR001","mf_partner":"kfin","mf_investment_type":"L","plan":"GR","folio":"FOL002","option":"G","scheme":"BP","mf_amc_code":"AXIS"}]
    ```
  </Tab>
</Tabs>

<Callout theme="warning">
`bse2`, `nse_mf`, and `cams` are not available yet. Contact your Key Account Manager before you send them.
</Callout>

## Sample request

This sample is a broker lump-sum payment. For an AMC, replace `products` with the AMC array and set `amount` to the sum of the scheme amounts.

```bash
curl -X POST 'https://test.payu.in/_payment' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_KEY' \
  --data-urlencode 'txnid=mf_txn_0001' \
  --data-urlencode 'amount=5000.00' \
  --data-urlencode 'productinfo=Mutual fund purchase' \
  --data-urlencode 'firstname=Ravi' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'surl=https://merchant.example.com/success' \
  --data-urlencode 'furl=https://merchant.example.com/failure' \
  --data-urlencode 'api_version=21' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"1579105002472","ifscCode":"HDFC0001579"}' \
  --data-urlencode 'products=[{"type":"mutual_fund","amount":"5000.00","receipt":"REC001","mf_member_id":"12345","mf_user_id":"USR001","mf_partner":"bse","mf_investment_type":"L"}]' \
  --data-urlencode 'hash=YOUR_SHA512_HASH'
```

## Test before production

Use your test key against `https://test.payu.in/_payment`. Continue with [Test the mutual fund integration](./mutual-funds-test-integration.md).

Later SIP instalments are on [Recurring SIP debit](./mutual-funds-recurring-sip.md). The callback is on [Mutual fund payment response](./mutual-funds-payment-response.md).
