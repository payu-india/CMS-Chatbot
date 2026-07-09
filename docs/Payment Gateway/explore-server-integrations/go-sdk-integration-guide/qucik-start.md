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

## Make Your Test Payment

Follow the below steps to integrate Go SDK and make your first test payment.

### Step 1 Install Go

<Accordion title="Installation Steps" icon="fa-download">
Execute the below command to install the GO module.

<Terminal>{`
  brew install go
`}</Terminal>
</Accordion>

### Step 2 Install the PayU Go SDK

<Accordion title="PayU Go SDK Installation Steps" icon="fa-info-circle">
1. Download the PayU Go SDK from GitHub.
2. Navigate to the the folder that contains the downloaded PayU Go SDK in the terminal and run the follwing command to install the SDK
<Terminal>{`
  go install
`}</Terminal>
</Accordion>

<br />
