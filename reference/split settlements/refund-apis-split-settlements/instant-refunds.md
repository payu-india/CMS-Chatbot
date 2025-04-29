---
title: Instant Refunds
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
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

Mandatory parameters

| **refund\_mode** | **beneficiary\_full\_name** | **beneficiary\_account** | **beneficiary\_ifsc** | **Mode** |
| ---------------- | --------------------------- | ------------------------ | --------------------- | -------- |
| 1                | N                           | N                        | N                     | PayU     |
| 2                | Y                           | Y                        | N                     | UPI      |
| 3                | Y                           | Y                        | Y                     | IMPS     |
| 4                | Y                           | Y                        | Y                     | NEFT     |

**Modes**

| **Mode** | **Channel** | **Amount Limit** | **Description**                                                                                                                               |
| -------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | PayU        |                  | PayU will internally check for any alternate instant refund channel available. If not present, it will be processed through a normal channel. |
| 2        | UPI         | \<= 1,00,00      | PayU will push funds on the shared VPA                                                                                                        |
| 3        | IMPS        | \<= 2,00,000     | PayU will push funds through IMPS into the account number shared                                                                              |
| 4        | NEFT        | \>= 2,00,000     | PayU will push funds through NEFT into the account number shared.                                                                             |

> 📘 Note:
>
> ​Priority order followed by PayU if the mode **1** is passed: Instant Refund Through PG > Instant Refund Through UPI > Instant Refund Through IMPS > Instant Refund Through NEFT > Normal PG Refunds.

## Sample request

```
{"5XAPG8":{"subvention_refund_status":0,"msg":"Please initiate or get
processed the original refund of this
transaction."},"73gAMf":{"subvention_refund_status":0,"msg":"Please
initiate or get processed the original refund of
this transaction."},"mihpayid":"999000000001122"}
```

## **Sample response**

### **Success response**

```plaintext
{ "status": 1, "msg": "Refund Request Queued", "request_id": "6582898821", "bank_ref_num": null, "mihpayid": 7043873219, "error_code": 102 }
```
