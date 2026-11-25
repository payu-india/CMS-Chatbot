---
title: Bonds
excerpt: >-
  Collect bond payments as an Online Bond Platform Provider (OBPP) through PayU.
  Send bond details in a product object. PayU settles to NSE Clearing.
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

Use this guide to collect bond payments as an Online Bond Platform Provider (OBPP). With each payment request, you send the bond details in a `products` object. PayU uses these details to report the payment to NSE Clearing Ltd (NCL).

<Callout icon="⚠️" theme="warning">
  ### Settlement goes to NSE Clearing, not to your account

  PayU settles every bond payment directly to NSE Clearing Ltd (NCL). You do not receive the funds in your merchant bank account.
</Callout>

1. You place the bond order on the exchange.
2. You send the payment request to PayU with the customer's bank account details and the `products` object.
3. PayU collects the payment from the verified bank account of the customer (TPV).
4. PayU settles the funds to NSE Clearing Ltd (NCL). PayU supports bond payments through NSE only.

<Callout icon="⚠️" theme="warning">
  ### Before you start

  - Ask your PayU Key Account Manager (KAM) to set your merchant type to **Bonds (OBPP)**.
  - Register a validated UPI handle on the SEBI portal. Use the `.brk` suffix with the `@valid` handle. Example: `<merchant>.payu1.brk@validaxis`.
  - Use a separate UPI handle for UPI Autopay — the same handle cannot be used for both.
  - **Accepted payment modes:** UPI, UPI Autopay, eNACH, and Net Banking only.
  - **TPV is mandatory.** Send the customer's bank account and IFSC in `beneficiarydetail` with every request.
  - **Refunds are not available.** Direct customers with a dispute to the [PayU care channel](https://help.payu.in/query).
</Callout>

***

## Payment Request (Lump Sum)

Send a `POST` request with form data (`application/x-www-form-urlencoded`).

**Environments**

| Environment | Endpoint                          |
| ----------- | --------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

<Accordion title="Request Parameters" icon="far fa-table">
  | Parameter           | Required | Description                                                                                                                                    |
  | ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  | `key`               | Yes      | Your merchant key.                                                                                                                             |
  | `txnid`             | Yes      | Your unique transaction ID.                                                                                                                    |
  | `amount`            | Yes      | Order amount. Must equal the `amount` in the product object.                                                                                   |
  | `productinfo`       | Yes      | Short description of the order.                                                                                                                |
  | `firstname`         | Yes      | First name of the customer.                                                                                                                    |
  | `email`             | Yes      | Email address of the customer.                                                                                                                 |
  | `phone`             | Yes      | Phone number of the customer.                                                                                                                  |
  | `surl`              | Yes      | URL that receives the response for a successful payment.                                                                                       |
  | `furl`              | Yes      | URL that receives the response for a failed payment.                                                                                           |
  | `api_version`       | Yes      | Set to `21`.                                                                                                                                   |
  | `beneficiarydetail` | Yes      | Bank accounts and IFSC codes of the customer, for TPV. JSON object. Max. 4 accounts. See format below.                                         |
  | `products`          | Yes      | Bond product object, as a JSON array with exactly one object. See [Product Object](https://docs.payu.in/docs/bonds#bond-product-object) below. |
  | `hash`              | Yes      | SHA-512 hash. See formula below.                                                                                                               |
</Accordion>

### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|beneficiarydetail|si_details|user_token|offer_key|offer_auto_apply|cart_details|products|SALT)
```

Leave a field empty in the hash string if you do not send it. Keep the `|` separators.

### `beneficiarydetail` Format

Send up to 4 bank accounts. Separate multiple account numbers with `|` and send the IFSC codes in the same order.

```json
{
  "beneficiaryAccountNumber": "1579105002472|50100650144897",
  "ifscCode": "HDFC0001579|HDFC0000145"
}
```

### Sample Request

```curl
curl -X POST 'https://test.payu.in/_payment' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=<merchant_key>' \
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
  --data-urlencode 'hash=<sha512_hash>'
```

***

## Recurring Debit (UPI Autopay or eNACH)

Use this call to debit a registered mandate. Mandate registration and pre-debit notification follow the standard PayU SI flow — no changes are needed for bonds.

**Environments**

| Environment | Endpoint                                               |
| ----------- | ------------------------------------------------------ |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

<Accordion title="Request Parameters" icon="far fa-table">
  | Parameter | Required | Description                                                                           |
  | --------- | -------- | ------------------------------------------------------------------------------------- |
  | `key`     | Yes      | Your merchant key.                                                                    |
  | `command` | Yes      | Set to `si_transaction`.                                                              |
  | `var1`    | Yes      | JSON with the debit details. Place the product object inside `more_info[0].wtParams`. |
  | `hash`    | Yes      | `sha512(key\|command\|var1\|SALT)`                                                    |
</Accordion>

### `var1` Sample

```json
{
  "authpayuid": "999990000005920",
  "amount": "101.00",
  "txnid": "a79d6318-afcb-4a87-820c-681b53215866",
  "invoiceDisplayNumber": "f53edcd3-7c08-49d6-9a2f-e67e4dc4eea7",
  "more_info": [
    {
      "wtParams": [
        {
          "type": "bond",
          "amount": "101.00",
          "receipt": "1234556789012",
          "mf_member_id": "12345",
          "mf_user_id": "77407",
          "mf_partner": "nse_bonds",
          "mf_investment_type": "L"
        }
      ]
    }
  ]
}
```

### Sample Response

```json
{
  "status": 1,
  "message": "Transaction Processed successfully",
  "details": {
    "a79d6318-afcb-4a87-820c-681b53215866": {
      "authpayuid": "999990000005920",
      "transactionid": "a79d6318-afcb-4a87-820c-681b53215866",
      "amount": "101.00",
      "payuid": "999990000006473",
      "status": "captured",
      "field9": "Transaction is Successful",
      "addedon": "2025-09-03 10:40:19"
    }
  }
}
```

***

## Bond Product Object

Send exactly one product object per payment request. PayU rejects a request with more than one object for bonds. All values are case-sensitive.

| Field                                              | Required | Format                                    | Rule                                           |
| -------------------------------------------------- | -------- | ----------------------------------------- | ---------------------------------------------- |
| `type`                                             | Yes      | String                                    | Must be `bond`.                                |
| `mf_partner`                                       | Yes      | String                                    | Must be `nse_bonds`.                           |
| `amount`                                           | Yes      | Numeric string — e.g. `5000` or `5000.50` | Must be equal to the order `amount`.           |
| `receipt`                                          | Yes      | Alphanumeric, max. 25 characters          | Your unique reference number for this payment. |
| `mf_member_id`                                     | Yes      | Max. 20 characters                        | Your member ID on the exchange.                |
| `mf_user_id`                                       | Yes      | Alphanumeric, max. 10 characters          | Unique client code (UCC) of the customer.      |
| `mf_investment_type`                               | Yes      | `L`                                       | Send `L` (lump sum).                           |
| `plan`, `option`, `scheme`, `folio`, `mf_amc_code` | No       | String                                    | Not used for bonds. You can omit these fields. |

***

## Payment Response

After the payment, PayU sends the result to your `surl` (success) or `furl` (failure) as form data. Bonds add no new fields to the standard PayU response.

<Accordion title="Response Parameters" icon="far fa-table">
  | Parameter                                                    | Description                                                                      |
  | ------------------------------------------------------------ | -------------------------------------------------------------------------------- |
  | `mihpayid`                                                   | PayU transaction ID.                                                             |
  | `txnid`                                                      | Your transaction ID from the request.                                            |
  | `status`                                                     | `success`, `failure`, or `pending`. Treat only `success` as a confirmed payment. |
  | `unmappedstatus`                                             | PayU internal status — for example `captured`, `auth`, `dropped`, or `pending`.  |
  | `mode`                                                       | Payment mode used.                                                               |
  | `bankcode`                                                   | Code of the payment option used.                                                 |
  | `amount`                                                     | Amount from the request.                                                         |
  | `net_amount_debit`                                           | Amount debited from the customer.                                                |
  | `bank_ref_num`                                               | Bank reference number for a successful payment.                                  |
  | `error`                                                      | Error code for a failed payment.                                                 |
  | `error_Message`                                              | Error description.                                                               |
  | `addedon`                                                    | Date and time of the transaction.                                                |
  | `productinfo`, `firstname`, `email`, `phone`, `udf1`–`udf10` | Values from the request.                                                         |
  | `hash`                                                       | Response hash. Verify before updating the order.                                 |
</Accordion>

### Verify the Response Hash

Calculate this hash with your salt and compare it with the `hash` value in the response. If they do not match, do not accept the payment.

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Callout icon="📘" theme="info">
  ### **Tips:**

  Do not include `beneficiarydetail` in the response hash formula.
</Callout>

### Verify the Payment

Before you confirm the order, verify the payment status with PayU using one of these methods:

- **Webhooks:** PayU sends the payment status to your server in real time. See <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">Webhooks for Payments</Anchor>.
- **Verify Payment API:** Send a `POST` request with `command=verify_payment` and `var1=<txnid>`. Hash: `sha512(key|command|var1|SALT)`.

| Environment | Verify Payment API endpoint                            |
| ----------- | ------------------------------------------------------ |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

***

## Errors

PayU stops at the first failed check and returns one error. For a payment request, PayU sends the error to your `furl`. For a recurring debit, PayU returns the error in the response.

| Condition                                              | Error message                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| A required field is missing                            | `Mandatory parameter '<field>' is missing`                                                  |
| `type` is not a valid value                            | `Type must be one of: mutual_fund, bond`                                                    |
| `mf_partner` is not a valid value                      | `mf_partner '<value>' is invalid. Allowed values: bse, bse2, nse_mf, nse_bonds, kfin, cams` |
| `mf_partner` is not `nse_bonds` for your merchant type | `"mf_partner" value is not allowed for this merchant`                                       |
| More than one product object                           | `Multi-product array is not allowed for this merchant`                                      |
| Product `amount` does not equal order `amount`         | `Sum of product amounts (<total>) does not match order amount (<order_amount>)`             |