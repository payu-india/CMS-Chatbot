---
title: Recurring Bond Debit
excerpt: >-
  Debit a registered bond mandate with si_transaction. Put one bond product
  object in wtParams and keep mf_investment_type as L.
deprecated: false
hidden: false
metadata:
  title: PayU Bond Recurring Debit
  description: >-
    Recurring bond debit for PayU OBPPs using si_transaction and wtParams.
    Mandate registration is unchanged. mf_investment_type stays L.
  keywords:
    - bond recurring debit
    - si_transaction nse_bonds
    - UPI Autopay bonds
    - eNACH OBPP
    - wtParams bond
    - Wealth Tech recurring
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

Use this call to debit a registered mandate. Mandate registration and pre-debit notification do not change for bonds. The product object still uses `mf_investment_type` `L`.

<Callout theme="warning">
Refunds are not available. TPV still applies to the mandate: debit a bank account you sent for that customer.
</Callout>

## Environments

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

## Parameters

<Accordion title="Recurring debit parameters" icon="fa-rotate">
  | Parameter | Required | Description |
  | --- | --- | --- |
  | `key` | Yes | Your merchant key. |
  | `command` | Yes | Set to `si_transaction`. |
  | `var1` | Yes | JSON with the debit details. Put the product object in `more_info[0].wtParams`. |
  | `hash` | Yes | `sha512(key\|command\|var1\|SALT)`. Hash the exact `var1` string you post. |
</Accordion>

## var1 sample

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

The identifiers in this sample are examples. `authpayuid` is the PayU id of the successful mandate. Send one object. `amount` inside `wtParams` must equal `amount` on the debit.

## Sample request

```bash
curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_KEY' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'var1={"authpayuid":"999990000005920","amount":"101.00","txnid":"a79d6318-afcb-4a87-820c-681b53215866","invoiceDisplayNumber":"f53edcd3-7c08-49d6-9a2f-e67e4dc4eea7","more_info":[{"wtParams":[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]}]}' \
  --data-urlencode 'hash=YOUR_SHA512_HASH'
```

## Sample response

```json
{
  "status": 1,
  "message": "Transaction Processed successfully",
  "details": {
    "a79d6318-afcb-4a87-820c-681b53215866": {
      "authpayuid": "999990000005920",
      "transactionid": "a79d6318-afcb-4a87-820c-681b53215866",
      "amount": "101.00",
      "user_credentials": "YOUR_KEY:11b341595c4d7dacb167",
      "card_token": "195748c0f4ec4b3093af",
      "payuid": "999990000006473",
      "status": "captured",
      "udf1": "Y",
      "field9": "Transaction is Successful",
      "udf2": "",
      "udf3": "",
      "udf4": "",
      "udf5": "",
      "phone": "",
      "email": "",
      "paymentgatewayid": 462,
      "addedon": "2025-09-03 10:40:19",
      "card_no": "XXXXXXXXXXXXXXXX"
    }
  }
}
```

`status` `1` with `details.<txnid>.status` of `captured` means PayU processed the debit. Confirm with [Verify Payment](ref:verify_payment_api) before you record it. A failed product check is returned in this response. See [Errors and troubleshooting](../wealth-tech-errors-and-troubleshooting.md).
