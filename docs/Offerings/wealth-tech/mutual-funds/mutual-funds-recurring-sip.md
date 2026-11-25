---
title: Recurring SIP Debit
excerpt: >-
  Debit a registered mutual fund mandate with si_transaction. Put the SIP
  product object in more_info wtParams and set mf_investment_type to S.
deprecated: false
hidden: false
metadata:
  title: PayU Mutual Fund Recurring SIP Debit
  description: >-
    Recurring SIP debit for PayU mutual funds using si_transaction, wtParams,
    and mf_investment_type S. Mandate registration is unchanged.
  keywords:
    - mutual fund SIP debit
    - si_transaction wtParams
    - UPI Autopay mutual fund
    - eNACH SIP PayU
    - mf_investment_type S
    - recurring mutual fund payment
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

Use this call to debit a registered mandate for each SIP instalment. Mandate registration and pre-debit notification do not change for mutual funds. Register the mandate with the same TPV bank account you will debit.

<Callout theme="warning">
Refunds are not available for a SIP debit. TPV still applies: the mandate must debit a bank account you collected for the customer.
</Callout>

<Callout theme="info">
The first lump-sum or first SIP collection that the customer completes on the hosted page uses [_payment](./mutual-funds-build-integration.md). This page is the later instalment, after the mandate exists.
</Callout>

## Environments

| Environment | Endpoint |
| --- | --- |
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

Send a `POST` with form data.

## Parameters

<Accordion title="Recurring debit parameters" icon="fa-rotate">
  | Parameter | Required | Description |
  | --- | --- | --- |
  | `key` | Yes | Your merchant key. |
  | `command` | Yes | Set to `si_transaction`. |
  | `var1` | Yes | JSON with the debit details. Put the product object in `more_info[0].wtParams`. |
  | `hash` | Yes | `sha512(key\|command\|var1\|SALT)`. Hash the exact `var1` string you post. |
</Accordion>

For a SIP instalment, set `receipt` to the SIP registration number and `mf_investment_type` to `S`.

## var1 sample

```json
{
  "authpayuid": "999990000005920",
  "amount": "500.00",
  "txnid": "a79d6318-afcb-4a87-820c-681b53215866",
  "invoiceDisplayNumber": "f53edcd3-7c08-49d6-9a2f-e67e4dc4eea7",
  "more_info": [
    {
      "wtParams": [
        {
          "type": "mutual_fund",
          "amount": "500.00",
          "receipt": "SIPREG12345",
          "mf_member_id": "12345",
          "mf_user_id": "USR001",
          "mf_partner": "bse",
          "mf_investment_type": "S"
        }
      ]
    }
  ]
}
```

The identifiers in this sample are examples. `authpayuid` is the PayU id of the successful mandate registration. For a direct AMC, add the AMC fields from [Product object](./mutual-funds-product-object.md) and set `mf_partner` to `kfin`.

## Sample request

```bash
curl -X POST 'https://test.payu.in/merchant/postservice.php?form=2' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=YOUR_KEY' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'var1={"authpayuid":"999990000005920","amount":"500.00","txnid":"a79d6318-afcb-4a87-820c-681b53215866","invoiceDisplayNumber":"f53edcd3-7c08-49d6-9a2f-e67e4dc4eea7","more_info":[{"wtParams":[{"type":"mutual_fund","amount":"500.00","receipt":"SIPREG12345","mf_member_id":"12345","mf_user_id":"USR001","mf_partner":"bse","mf_investment_type":"S"}]}]}' \
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
      "amount": "500.00",
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

`status` `1` with `details.<txnid>.status` of `captured` means PayU processed the debit. Confirm with [Verify Payment](ref:verify_payment_api) before you record the instalment. A failed debit returns the error in this response. See [Errors and troubleshooting](../wealth-tech-errors-and-troubleshooting.md).
