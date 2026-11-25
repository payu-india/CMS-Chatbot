---
title: Build the Equity Payment Request
excerpt: >-
  POST an equity payment with api_version 6, beneficiarydetail, and the equity
  SHA-512 hash. Do not send a product object.
deprecated: false
hidden: false
metadata:
  title: Build a PayU Wealth Tech Equity Payment
  description: >-
    Equity _payment request for PayU Wealth Tech: parameters, beneficiarydetail,
    api_version 6, and the SHA-512 hash that includes beneficiarydetail.
  keywords:
    - equity payment request PayU
    - api_version 6 hash
    - beneficiarydetail TPV
    - equity SHA-512
    - test.payu.in _payment
    - stock broker payment integration
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

Send a `POST` with form data (`application/x-www-form-urlencoded`). Generate the hash on your server.

<Callout theme="warning">
TPV is mandatory. `beneficiarydetail` is required on every equity request.
</Callout>

<Callout theme="error">
Set `api_version` to `6`. Do not send `products`. The equity hash includes `beneficiarydetail` and does not use the mutual fund and bond hash string.
</Callout>

## Environments

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

## Request parameters

<Accordion title="Equity payment parameters" icon="fa-table">
  | Parameter | Required | Description |
  | --- | --- | --- |
  | `key` | Yes | Your merchant key. |
  | `txnid` | Yes | Your unique transaction ID. |
  | `amount` | Yes | Payment amount. |
  | `productinfo` | Yes | Short description of the payment. |
  | `firstname` | Yes | First name of the customer. |
  | `email` | Yes | Email address of the customer. |
  | `phone` | Yes | Phone number of the customer. |
  | `surl` | Yes | URL that receives the response for a successful payment. |
  | `furl` | Yes | URL that receives the response for a failed payment. |
  | `api_version` | Yes | Set to `6`. |
  | `beneficiarydetail` | Yes | Bank account and IFSC of the customer, for TPV. JSON. Maximum 4 accounts. |
  | `hash` | Yes | SHA-512 hash. Use the formula below. |
</Accordion>

## Hash formula

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

Keep a field empty in the hash string if you do not send it. Keep every `|` separator. The six pipes after `udf5` are five empty fields, then `beneficiarydetail`, then your salt.

Use the exact `beneficiarydetail` string you post in the form. Hash on your server with your salt. The standard payment hash in [Generate Hash](doc:hashing-request-and-response) stops before the salt and does not include `beneficiarydetail`. Use the equity string on this page.

<Callout theme="error">
A hash that omits `beneficiarydetail`, or that uses `api_version=21`, does not match this request. PayU rejects the payment.
</Callout>

## beneficiarydetail format

To send more than one bank account, separate the values with `|`. Send the IFSC codes in the same order as the accounts. Maximum four accounts.

```json
{"beneficiaryAccountNumber":"1579105002472|50100650144897","ifscCode":"HDFC0001579|HDFC0000145"}
```

These account numbers are sample values.

## Sample request

```bash
curl -X POST 'https://test.payu.in/_payment' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_KEY' \
  --data-urlencode 'txnid=eq_tpv_12345' \
  --data-urlencode 'amount=10000.00' \
  --data-urlencode 'productinfo=Add funds' \
  --data-urlencode 'firstname=Ravi' \
  --data-urlencode 'email=test@example.com' \
  --data-urlencode 'phone=9999999999' \
  --data-urlencode 'surl=https://merchant.example.com/success' \
  --data-urlencode 'furl=https://merchant.example.com/failure' \
  --data-urlencode 'api_version=6' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"1579105002472","ifscCode":"HDFC0001579"}' \
  --data-urlencode 'hash=YOUR_SHA512_HASH'
```

Replace `YOUR_KEY` and `YOUR_SHA512_HASH`. Do not send a `products` field.

## Recurring debit

For UPI Autopay or eNACH, use the standard TPV standing-instruction flow. Equity adds no fields. Follow [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout).

## Test before production

Post the sample to `https://test.payu.in/_payment` with your test key and salt. Then follow [Test the equity integration](./equity-test-integration.md).

The response fields and the reverse hash are on [Equity payment response](./equity-payment-response.md).
