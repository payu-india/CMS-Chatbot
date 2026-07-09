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

## Integrate and Make Your Test Payment

Follow the below steps to integrate Go SDK and make your first test payment.

### Step 1 Install Go

You should first install Go (if not installed) to proceed withe the integration. Additionally run the following command to check the whether Go is installed in your system.

<Terminal>{`
go version
`}</Terminal>

<Accordion title="Installation Steps" icon="fa-download">
Execute the below command to install the Go in your system.

<Terminal>{`
  brew install go
`}</Terminal>
</Accordion>

### Step 2 Install the PayU Go SDK

After you install Go in your system, you should now install the PayU Go SDK to create a module.

<Accordion title="PayU Go SDK Installation Steps" icon="fa-info-circle">
1. Download the PayU Go SDK from GitHub.
2. Navigate to the the folder that contains the downloaded PayU Go SDK in the terminal and run the follwing command to install the SDK

<Terminal>{`
 go install
`}</Terminal>
</Accordion>

### Step 3 Build the PayU Client

The next step after installing the PayU Go SDK is to build the PayU client.

<Accordion title="Steps to Build the Client" icon="fa-info-circle">
Use the following code to build the client.

```go
import (
 payu "github.com/payu-india/web-sdk-go"
)

payuClient, err := payu.NewClient(
  <YOUR_MERCHANT_KEY>,
  <YOUR_MERCHANT_SALT>,
  <ENVIRONMENT>,                
) 
```

| **Parameter**        | **Description**                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| `YOUR_MERCHANT_KEY`  | Your merchant key retrieved from the dashboard. We recommend you to use the test key.   |
| `YOUR_MERCHANT_SALT` | Your merchant salt retrieved from the dashboard. We recommend you to use the test salt. |
| `ENVIRONMENT`        | The environment used. We recommend to use the test environment.                         |
</Accordion>

<br />
