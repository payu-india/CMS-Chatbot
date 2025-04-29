---
title: Payment Modes  and Required Parameters
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
| **Payment mode** | **Description**                   | **Required for Params** |
| ---------------- | --------------------------------- | ----------------------- |
| CC               | Credit Card                       | cardNumber, authCode    |
| DC               | Debit Card                        | cardNumber. authCode    |
| NB               | Net Banking                       | accountNumber, IFSC     |
| NEFT             | National Electronic Fund Transfer | accountNumber, IFSC     |
| UPI              | Unified Payments Interface        | VPA                     |
| AEPS             | Aadhar Enabled Payment System     | aadhaar, IIN            |
| IMPS             | Immediate Payment Service         | MMID                    |
| WALLET           | Wallet                            | walletName              |
