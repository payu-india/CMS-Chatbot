---
title: Bond Payment Response
excerpt: >-
  Read the bond surl and furl response, verify the reverse hash, and confirm
  the payment with Verify Payment before you update the order.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Bond Payment Response
  description: >-
    Bond payment response fields and reverse hash for PayU OBPP payments.
    Confirm the payment before you treat the order as paid.
  keywords:
    - bond payment response PayU
    - OBPP reverse hash
    - surl furl bonds
    - verify_payment bonds
    - NSE Clearing callback
    - Wealth Tech bond response
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

After the payment, PayU sends the result to your `surl` (success) or `furl` (failure) as form data. Bonds add no fields to the response.

<Callout theme="error">
Verify the response hash before you update the order. If the hash does not match, do not accept the payment.
</Callout>

## Response parameters

<Accordion title="Bond response parameters" icon="fa-reply">
  | Parameter | Description |
  | --- | --- |
  | `mihpayid` | PayU transaction ID. |
  | `txnid` | Your transaction ID from the request. |
  | `status` | `success`, `failure`, or `pending`. Treat only `success` as a successful payment. |
  | `unmappedstatus` | PayU internal status, for example `captured`, `auth`, `dropped`, or `pending`. |
  | `mode` | Payment mode used. |
  | `bankcode` | Code of the payment option used. |
  | `amount` | Amount from the request. |
  | `net_amount_debit` | Amount debited from the customer. |
  | `bank_ref_num` | Bank reference number for a successful payment. |
  | `error` | Error code for a failed payment. |
  | `error_Message` | Error description. |
  | `addedon` | Date and time of the transaction. |
  | `productinfo`, `firstname`, `email`, `phone`, `udf1`–`udf10` | Values from the request. |
  | `hash` | Response hash. Verify it before you update the order. |
</Accordion>

## Sample response

```text
mihpayid=403993715537000168&mode=UPI&status=success&key=YOUR_KEY&txnid=bond_txn_0001&amount=101.00&addedon=2026-03-17 14:48:25&productinfo=Bond purchase&firstname=Ravi&email=test@example.com&phone=9999999999&error=E000&error_Message=No Error&net_amount_debit=101.00&unmappedstatus=captured&hash=RESPONSE_HASH&bank_ref_num=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bankcode=INTENT&surl=https://merchant.example.com/success&furl=https://merchant.example.com/failure
```

`hash` in this sample is a placeholder. PayU calculates it with your salt. The posted body also includes the other PayU response fields echoed from the request.

## Verify the response hash

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

Do not include `beneficiarydetail` or `products` in the response hash.

## Verify the payment

- **Webhooks.** See [Webhooks](doc:webhooks).
- **Verify Payment API.** `POST` to `https://info.payu.in/merchant/postservice.php?form=2` (test: `https://test.payu.in/merchant/postservice.php?form=2`) with `command=verify_payment` and `var1` set to your `txnid`. Hash: `sha512(key|command|var1|SALT)`. See [Verify Payment API](ref:verify_payment_api).
