---
title: Payment Journey & Workflow for Merchants
excerpt: >-
  Illustrative example of the payment journey in a Cross-Border Transaction
  (Outward)
deprecated: false
hidden: false
metadata:
  title: Cross-Border Payments Workflow
  description: ''
  keywords:
    - Cross-Border Payments Workflow
    - Workflow for Cross-Border Payments
  robots: index
next:
  description: ''
---
<br />

<Image align="center" border={false} src="https://files.readme.io/c051d23-cross-border-import-workflow.png" />

PayU has partnered with **AD-1 CATEGORY Bank** to complete the settlement via SWIFT. This account is owned/controlled by PayU and acts as an “**Outward Collection Account (OCA)**.” (erstwhile Import Collection Account)

1. Funds will be transferred by acquirers into PayU’s domestic pool account ("Nodal Bank Account"). This is an automated process.
2. PayU instructs the AD-1 category bank to make the transfer to merchants over a file shared through SFTP. After the cross-border settlement is completed, the AD-1 category bank shares a response file and a unique transaction reference.

<br />