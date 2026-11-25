---
title: Equity Payment Response
excerpt: >-
  Read the equity surl and furl response, verify the reverse hash, and confirm
  the payment before you update the order.
deprecated: false
hidden: false
metadata:
  title: PayU Wealth Tech Equity Payment Response
  description: >-
    Equity payment response fields, reverse hash, and Verify Payment API checks
    for PayU Wealth Tech stock-broker payments.
  keywords:
    - equity payment response PayU
    - reverse hash equity
    - surl furl TPV
    - verify_payment equity
    - mihpayid txnid
    - Wealth Tech callback
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

After the payment, PayU sends the result to your `surl` (success) or `furl` (failure) as form data. Equity adds no fields to the response.

<Callout theme="error">
Verify the response hash before you update the order. If the hash does not match, do not accept the payment.
</Callout>

## Response parameters

<Accordion title="Equity response parameters" icon="fa-reply">
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

The values you sent for `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl` come back unchanged. `hash` is calculated by PayU with your salt.

```text
mihpayid=403993715537000168&mode=UPI&status=success&key=YOUR_KEY&txnid=eq_tpv_12345&amount=10000.00&addedon=2026-03-17 14:48:25&productinfo=Add funds&firstname=Ravi&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test@example.com&phone=9999999999&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=&card_no=&field0=&field1=9999999999@upi&field2=&field3=ps@paytm&field4=&field5=403993715537000168&field6=&field7=00|APPROVED OR COMPLETED SUCCESSFULLY&field8=&field9=Transaction Successful|Completed Using Callback&payment_source=payu&PG_TYPE=UPI-PG&error=E000&error_Message=No Error&net_amount_debit=10000.00&discount=0.00&unmappedstatus=captured&hash=RESPONSE_HASH&bank_ref_num=ICI9TI0Y06S0HCGA1DDHTN3ZH7YL0MPYBRUQ&bankcode=INTENT&surl=https://merchant.example.com/success&furl=https://merchant.example.com/failure
```

## Verify the response hash

Calculate this hash with your salt. Compare it with `hash` in the response. If the values differ, do not accept the payment.

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

Do not include `beneficiarydetail` in the response hash.

## Verify the payment

Confirm the payment from your server before you fulfil the order. Use either method:

- **Webhooks.** PayU sends the payment status to your server. See [Webhooks](doc:webhooks).
- **Verify Payment API.** `POST` to `https://info.payu.in/merchant/postservice.php?form=2` (test: `https://test.payu.in/merchant/postservice.php?form=2`) with `command=verify_payment` and `var1` set to your `txnid`. Hash: `sha512(key|command|var1|SALT)`. See [Verify Payment API](ref:verify_payment_api).

<Callout theme="info">
The browser redirect alone is not confirmation. Prefer the webhook or Verify Payment when you update the order.
</Callout>
