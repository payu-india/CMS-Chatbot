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
 cd payu-go-integration // Navigates to the project folder.

 go mod init payu-go-integration // Creates a new Go module.

 go get github.com/payu-india/web-sdk-go // Adds the PayU SDK.

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
	// Replace with your PayU test credentials
	key := "YOUR_TEST_MERCHANT_KEY"
	salt := "YOUR_TEST_MERCHANT_SALT"

	payuClient, err := payu.NewClient(key, salt, "TEST")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("PayU client created successfully")
	_ = payuClient
}
```

| **Parameter**        | **Description**                                                                         |
| -------------------- | --------------------------------------------------------------------------------------- |
| `YOUR_TEST_MERCHANT_KEY`  | Your merchant key retrieved from the dashboard. We recommend you to use the test key.   |
| `YOUR_TEST_MERCHANT_SALT` | Your merchant salt retrieved from the dashboard. We recommend you to use the test salt. |
</Accordion>

### Step 4 Create a Payment Request

<Accordion title="Steps to Create a Payment Request" icon="fa-info-circle">
1. Save this code in the `payu-go-integration` project folder as `pay.go`.

```go
package main

import (
	"fmt"
	"os"
	"time"

	payu "github.com/payu-india/web-sdk-go"
)

func initiatePayment(client *payu.PayuStruct) (string, error) {
	txnid := fmt.Sprintf("TXN%d", time.Now().Unix())

	params := map[string]interface{}{
		"txnid":       tran_1234,
		"amount":      "10.00",
		"productinfo": "Test product",
		"firstname":   "Test",
		"email":       "test@example.com",
		"phone":       "9876543210",
		"surl":        "https://test.payu.in/test_response",
		"furl":        "https://test.payu.in/test_response",
	}

	htmlForm, err := client.GeneratePaymentForm(params)
	if err != nil {
		return "", err
	}

	if err := os.WriteFile("pay.html", []byte(htmlForm), 0644); err != nil {
		return "", err
	}

	fmt.Println("Payment form saved to pay.html")
	return txnid, nil
}
```
2. Navigate to the `payu-go-integration` folder and run the following code to create the `pay.html` file.

<Terminal>{`
go run .
`}</Terminal><br/>

This will create the `pay.html` file.
</Accordion>

### Step 5 Complete the Test Payment

<Accordion title="Steps to Complete the Test Payment" icon="fa-info-circle">
1. Open the `payu.html` file or run the following command to open the checkout.

<Terminal>{`
  open pay.html
`}</Terminal>

2. Choose any payment method and provide the <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets" title="Access Test Credentials">test credentials</a>.
3. Complete the payment.
</Accordion>

## Errors and Troubleshooting

<Accordion title="Errors and Fixes" icon="fa-info-circle">
*Need Content*
</Accordion>

## What is Next?

After you complete the test payment:

- Handle payment response
- Verify transaction status
- Move to production

## Next Steps

Now that you have created your first test payment go to the

- Integration Guide for the detailed steps.

<br />
