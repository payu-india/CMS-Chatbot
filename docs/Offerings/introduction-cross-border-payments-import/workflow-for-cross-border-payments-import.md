---
title: Workflow for Import
excerpt: ''
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
Different parties are involved in the settlement for Cross-Border Payments - Import merchants. Transactional flow has no changes.

<Image align="center" border={false} src="https://files.readme.io/c051d23-cross-border-import-workflow.png" />

PayU has tied up with **AD-1 CATEGORY bank** to do the settlement. This account is owned/controlled by PayU and acts as an “**Outward Collection Account (OCA)**.”

1. Funds will be transferred by acquirers into PayU’s Nodal only. This is an automated process.
2. PayU instructs the AD-1 category bank to make the transfer to merchants over a file shared through SFTP. After it is transferred, the AD-1 category bank shares a response file and marks the UTR.
3. Invoice copies are shared with the AD-1 category bank team every fortnight for the transaction to be settled.

Transactional flows & integrations remain the same for PACB merchants, and merchants need to perform the following:

* Merchant has to share invoice numbers in the UDF5 field while doing transactions in real-time.
* Post successful transaction, invoice/AWB copy has to be submitted.
