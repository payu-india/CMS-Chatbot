---
title: Equity
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

Collect payments for equity trading as a stock broker. Equity payments use the standard PayU payment request with TPV. You do not send a product object, and PayU does not report equity payments to an exchange.

1. Your customer adds funds or places an order on your platform.
2. You send a payment request to PayU with the customer's bank account details.
3. PayU collects the payment only from the bank account you specified (TPV).
4. PayU sends the funds to your bank account.

<Callout icon="⚠️" theme="warning">
  ### Before you start

  - Ask your PayU Key Account Manager (KAM) to set your merchant type to **equity**.
  - Register a validated UPI handle on the SEBI portal. Use the `.brk` suffix with the `@valid` handle.
  - Use a separate UPI handle for UPI Autopay — the same handle cannot be used for both.
  - **Accepted payment modes:** UPI, UPI Autopay, eNACH, and Net Banking only.
  - **TPV is mandatory.** Send the customer's bank account number and IFSC in `beneficiarydetail` with every request.
  - **Refunds are not available.** Direct customers with a dispute to the <Anchor target="_blank" href="https://help.payu.in/query">PayU care channel</Anchor>.
</Callout>

***

## Payment Request

Send a `POST` request with form data (`application/x-www-form-urlencoded`).

**Environments**

| Environment | Endpoint                          |
| ----------- | --------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

<Accordion title="Request Parameters" icon="far fa-table">
  | Parameter           | Required | Description                                                                                     |
  | ------------------- | -------- | ----------------------------------------------------------------------------------------------- |
  | `key`               | Yes      | Your merchant key.                                                                              |
  | `txnid`             | Yes      | Your unique transaction ID.                                                                     |
  | `amount`            | Yes      | Payment amount.                                                                                 |
  | `productinfo`       | Yes      | Short description of the payment.                                                               |
  | `firstname`         | Yes      | First name of the customer.                                                                     |
  | `email`             | Yes      | Email address of the customer.                                                                  |
  | `phone`             | Yes      | Phone number of the customer.                                                                   |
  | `surl`              | Yes      | URL that receives the response for a successful payment.                                        |
  | `furl`              | Yes      | URL that receives the response for a failed payment.                                            |
  | `api_version`       | Yes      | Set to `6`.                                                                                     |
  | `beneficiarydetail` | Yes      | Bank account and IFSC of the customer, for TPV. JSON object. Max. 4 accounts. See format below. |
  | `hash`              | Yes      | SHA-512 hash. See formula below.                                                                |
</Accordion>

### Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
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
  --data-urlencode 'hash=<sha512_hash>'
```

***

## Recurring Debit (UPI Autopay or eNACH)

Equity recurring debits use the standard PayU standing instruction (SI) flow with TPV. Equity adds no new fields and does not use a product object.

<Callout icon="📘" theme="info">
  ### Reference

  See <Anchor target="_blank" href="doc:introduction-recurring-payments-integration">Recurring Payments Integration</Anchor> for the full SI flow — mandate registration, pre-debit notification, and the `si_transaction` call.
</Callout>

***

## Payment Response

After the payment, PayU sends the result to your `surl` (success) or `furl` (failure) as form data. Equity adds no new fields to the standard PayU response.

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

- **Webhooks:** PayU sends the payment status to your server in real time. See [Webhooks for Payments](doc:webhooks).
- **Verify Payment API:** Send a `POST` request with `command=verify_payment` and `var1=<txnid>`. Hash: `sha512(key|command|var1|SALT)`.

| Environment | Verify Payment API endpoint                            |
| ----------- | ------------------------------------------------------ |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

***

## Errors

PayU stops at the first failed check and sends one error to your `furl`.

| Condition                                                    | Result           |
| ------------------------------------------------------------ | ---------------- |
| Customer pays from a bank account not in `beneficiarydetail` | Payment rejected |
| `beneficiarydetail` is missing or not valid JSON             | Payment rejected |
| Hash does not match                                          | Payment rejected |

<Callout icon="📘" theme="info">
  ### **Contact PayU Support**

  Contact your PayU Key Account Manager with the transaction ID if you encounter TPV or hash errors during integration testing.
</Callout>
