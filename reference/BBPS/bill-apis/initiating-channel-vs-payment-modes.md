---
title: Initiating Channel  vs Payment Modes
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
| S. No | Payment Mode     | INT | INS | MOB | MBB | ATM | BNK | KSK | AGT | BSC |
| ----- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1     | Cash             | N   | N   | N   | N   | N   | Y   | Y   | Y   | V   |
| 2     | Internet Banking | Y   | Y   | Y   | Y   | V   | N   | N   | N   | N   |
| 3     | Credit Card      | Y   | Y   | Y   | Y   | Y   | Y   | Y   | Y   | V   |
| 4     | Debit Card       | Y   | Y   | Y   | Y   | Y   | Y   | Y   | Y   | Y   |
| 5     | Prepaid Card     | Y   | Y   | Y   | Y   | \`Y | Y   | Y   | V   | Y   |
| 6     | IMPS             | Y   | Y   | Y   | Y   | N   | Y   | N   | Y   | Y   |
| 7     | NEFT             | Y   | Y   | Y   | Y   | Y   | Y   | N   | Y   | Y   |
| 8     | UPI              | Y   | Y   | Y   | Y   | N   | Y   | N   | V   | V   |
| 9     | Wallet           | Y   | Y   | V   | Y   | N   | Y   | Y   | N.  | Y   |
| 10    | ASPS             | N   | N   | Y   | N   | N   | Y   | N   | Y   | V   |
| 11    | Account Transfer | N   | N   | N   | N   | N   | Y   | N   | N   | N.  |
| 12    | Bharat QR        | N   | N   | Y   | Y   | N   | Y   | N   | Y   | Y   |
| 13    | LISSD            | N   | N   | Y   | Y   | N   | N   | N   | N   | N   |