---
title: Qucik Start Guide
deprecated: false
hidden: true
metadata:
  robots: index
---
## Integration Steps Overview

Test your Go SDK integrations within minutes by performing these steps:

1. Install Go & create module — go mod init
2. Install SDK — go get or download from GitHub
3. Build client — NewClient(key, salt, "TEST")
4. Initiate payment — GeneratePaymentForm() with mandatory params: txnid, amount, productinfo, firstname, email, phone, surl, furl
5. Handle callbacks — CheckReversehash() on surl/furl
6. Verify payment — VerifyPayment(txnid)

***

## Make Your First Payment

<br />

<Accordion title="GO Module Installation Steps" icon="fa-download">
Execute the below command to install the GO module.

<Terminal>{`
  go get github.com/payu-india/web-sdk-go
  go mod tidy
`}</Terminal>
</Accordion>

<br />
