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

You should first install Go (if not installed) to proceed withe the integration. Additionally run the following command to check whether Go is installed in your system.

<Accordion title="Check If Go is Installed" icon="fa-info-circle">
<Terminal>{`
go version
`}</Terminal>
</Accordion>

If not installed, execute the following command in the terminal to install Go in your system.

<Accordion title="Go Installation Code" icon="fa-code">
<Terminal>{`
  brew install go
`}</Terminal>
</Accordion>

### Step 2 Create a Module and Install the PayU SDK

After you install Go in your system, you should now create a project module and install the PayU Go SDK.

<Accordion title="Steps to Create a Module and Install the PayU Go SDK" icon="fa-list">
1. Run the follwing command to create a project module.

<Terminal>{`
mkdir payu-go-integration
`}</Terminal>

2. Navigate to the the project module folder and run the following command to install the PayU Go SDK.

<Terminal>{`
 cd payu-go-integration // Navigates to the project folder.<br/>
 go mod init payu-go-integration // Creates a new Go module in the project folder.<br/>
 go get github.com/payu-india/web-sdk-go // Adds the PayU SDK.<br/>
 go mod tidy // cleans up your project's dependencies in go.mod and go.sum.
`}</Terminal>
</Accordion>

### Step 3 Build the PayU Client

The next step after installing the PayU Go SDK is to build the PayU client.

<Accordion title="Steps to Build the Client" icon="fa-info-circle">
Use the following code to build the client.

```go
package main

import (
	"fmt"
	"log"

	payu "github.com/payu-india/web-sdk-go"
)

func main() {
	payuClient, err := payu.NewClient(
		"YOUR_TEST_MERCHANT_KEY",
		"YOUR_TEST_MERCHANT_SALT",
		"TEST",
	)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("PayU client created:", payuClient != nil)
}
```

| **Parameter**        | **Description**                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| `YOUR_MERCHANT_KEY`  | Your merchant key retrieved from the dashboard. We recommend you to use the test key.   |
| `YOUR_MERCHANT_SALT` | Your merchant salt retrieved from the dashboard. We recommend you to use the test salt. |
| `ENVIRONMENT`        | The environment used. We recommend to use the test environment.                     |
</Accordion>

<br />
