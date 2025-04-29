---
title: Instant Refunds
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Instant Refunds
  description: >-
    This document outlines the parameters and modes for instant refunds,
    including mandatory parameters and different refund modes with their
    corresponding descriptions and limits. It also provides a sample request and
    response for refund transactions.
  keywords:
    - Instant Refunds Parameters
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: refund_transaction_api
      title: Refund Transaction API
---
## Parameters and modes

These are the parameter and modes posted for instant refunds:

```plaintext
{"refund_mode":"1","beneficiary_full_name":"","beneficiary_account":"","beneficiary_ifsc":""}
```

```plaintext
{"refund_mode":"2","beneficiary_full_name":"Test","beneficiary_account":"test@ybl","beneficiary_ifsc":""}
```

```plaintext
{"refund_mode":"3","beneficiary_full_name":"Test","beneficiary_account":"12344","beneficiary_ifsc":"HDFC000 0001"}
```

```plaintext
{"refund_mode":"4","beneficiary_full_name":"test","beneficiary_account":"12344","beneficiary_ifsc":"HDFC0000 001"}
```

## Mandatory parameters

| **refund\_mode** | **beneficiary\_full\_name** | **beneficiary\_account** | **beneficiary\_ifsc** | **Mode** |
| ---------------- | --------------------------- | ------------------------ | --------------------- | -------- |
| 1                | N                           | N                        | N                     | PayU     |
| 2                | Y                           | Y                        | N                     | UPI      |
| 3                | Y                           | Y                        | Y                     | IMPS     |
| 4                | Y                           | Y                        | Y                     | NEFT     |

## Modes

| Mode | Channel | Amount Limit | Description                                                                                                                                   |
| ---- | ------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | PayU    |              | PayU will internally check for any alternate instant refund channel available. If not present, it will be processed through a normal channel. |
| 2    | UPI     | \<= 1,00,00  | PayU will push funds on the shared VPA                                                                                                        |
| 3    | IMPS    | \<= 2,00,000 | PayU will push funds through IMPS into the account number shared                                                                              |
| 4    | NEFT    | \>= 2,00,000 | PayU will push funds through NEFT into the account number shared.                                                                             |

> 📘 Note:
>
> ​Priority order followed by PayU if the mode **1** is passed: Instant Refund Through PG > Instant Refund Through UPI > Instant Refund Through IMPS > Instant Refund Through NEFT > Normal PG Refunds.

## Sample request

```
curl --location -g --request POST '{{http_endpoint}}/merchant/postservice.php?form=2'
--form 'key="testsms"'
--form 'command="cancel_refund_transaction"'
--form 'hash="3931b114a5884f6ef2023745a4698369cf694e5a0a31861ab5458bd878b55a82fdd8d01845b3 157fe78f60253094ec9319e0b9a6bcdee35d1338bb78e7678ab6 "'
--form 'var1="43873219"'
--form 'var2="R003242NFE2AHF"'
--form 'var3="160.0"'
--form 'var4=""'
--form 'var5=""'
--form 'var6=""'
--form 'var7="{ "test_sms_child_1": { "amount": 100, aggreatorRefundAmount: 40 }, "test_sms_child_2": {"amount": 20, aggreatorCommission: 0 }}"'
```

## Sample response

### Success response

```plaintext
{ "status": 1, "msg": "Refund Request Queued", "request_id": "6582898821", "bank_ref_num": null, "mihpayid": 7043873219, "error_code": 102 }
```

> 📘 Note:
>
> In the case of Aggregator merchants, the sample success response will be as follows:

```plaintext
{ 7043873219 => { "status": 1, "msg": "Refund Request Queued", "request_id": "6582898821", "bank_ref_num": null, "mihpayid": 7043873219, "error_code": 102 }, 7043873220 => { "status": 1, "msg": "Refund Request Queued", "request_id": "6582898821", "bank_ref_num": null, "mihpayid": 7043873220, "error_code": 102 }}
```

### Error response

```plaintext
{ "Status":0, "msg":"Invalid Hash." }
```
