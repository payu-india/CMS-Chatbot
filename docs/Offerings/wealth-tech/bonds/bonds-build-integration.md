---
title: Build the Bond Payment Request
excerpt: >-
  POST a bond payment with api_version 21, one nse_bonds product object,
  beneficiarydetail, and the bond SHA-512 hash.
deprecated: false
hidden: false
metadata:
  title: Build a PayU Wealth Tech Bond Payment
  description: >-
    Bond _payment request for OBPPs: api_version 21, a single bond product
    object, TPV beneficiarydetail, and the SHA-512 hash.
  keywords:
    - bond payment request PayU
    - nse_bonds products
    - api_version 21 OBPP
    - NSE Clearing payment
    - beneficiarydetail bonds
    - Wealth Tech bond hash
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

Send a `POST` with form data (`application/x-www-form-urlencoded`) for a lump-sum bond payment. Generate the hash on your server.

<Callout theme="warning">
TPV is mandatory. `beneficiarydetail` is required on every bond request.
</Callout>

<Callout theme="error">
Set `api_version` to `21`. Send one product object with `type` `bond` and `mf_partner` `nse_bonds`. The hash string on this page is the one PayU checks.
</Callout>

## Environments

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

## Request parameters

<Accordion title="Bond payment parameters" icon="fa-table">
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
  | `products` | Yes | One bond product object, as a JSON array. See [Product object](./bonds-product-object.md). |
  | `hash` | Yes | SHA-512 hash. Use the formula below. |
</Accordion>

## Hash formula

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|beneficiarydetail|si_details|user_token|offer_key|offer_auto_apply|cart_details|products|SALT)
```

Keep a field empty in the hash string if you do not send it. Keep every `|` separator. The `products` value in the hash must be the same string you post.

[Generate Hash](doc:hashing-request-and-response) documents the standard payment hash. Bond requests use the longer string above.

## beneficiarydetail format

```json
{"beneficiaryAccountNumber":"1579105002472|50100650144897","ifscCode":"HDFC0001579|HDFC0000145"}
```

Separate multiple account numbers with `|` and keep the IFSC codes in the same order. Maximum four accounts. These account numbers are sample values.

## products sample

```json
[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]
```

The product `amount` must equal the order `amount`. Field rules are on [Product object](./bonds-product-object.md).

## Sample request

```bash
curl -X POST 'https://test.payu.in/_payment' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_KEY' \
  --data-urlencode 'txnid=bond_txn_0001' \
  --data-urlencode 'amount=101.00' \
  --data-urlencode 'productinfo=Bond purchase' \
  --data-urlencode 'firstname=Ravi' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'surl=https://merchant.example.com/success' \
  --data-urlencode 'furl=https://merchant.example.com/failure' \
  --data-urlencode 'api_version=21' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"1579105002472","ifscCode":"HDFC0001579"}' \
  --data-urlencode 'products=[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]' \
  --data-urlencode 'hash=YOUR_SHA512_HASH'
```

## Test before production

Use your test key against `https://test.payu.in/_payment`. Continue with [Test the bond integration](./bonds-test-integration.md).

A later debit of a registered mandate is on [Recurring bond debit](./bonds-recurring-debit.md). The callback is on [Bond payment response](./bonds-payment-response.md).
