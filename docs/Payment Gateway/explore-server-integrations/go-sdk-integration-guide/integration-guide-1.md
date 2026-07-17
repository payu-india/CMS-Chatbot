---
title: Accept Payments with the PayU Go SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
The PayU Go SDK enables you to integrate PayU's Payment Gateway into applications built with Go (Golang). Instead of handling low-level API requests, request signing, and response parsing manually, you can use the SDK to interact with PayU APIs through a simple and consistent interface.

## PayU Go Web SDK

Download the <Anchor target="_blank" href="https://github.com/payu-india/web-sdk-go/archive/refs/heads/main.zip">PayU Go</Anchor> sample app and go through the below folder structure.

| **File** | **Content** |
| -------- | ----------- |
|          |             |
|          |             |

***

## Prerequisites

Go through these prerequisites and dependencies before starting the integration.

***

## Integration Steps

<Callout icon="✋" theme="info">
  ### **Payment Flow**

  Before you start integrating, it’s important to understand how payment flow works in <Anchor target="_blank" href="https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/payu-payment-gateway-workflow">PayU Payment Gateway</Anchor>.
</Callout>

Follow these steps to integrate PayU Go SDK and accept payments.

<HoverCardGrid
  columns={3}
  items={[
    {
      title: '1. Build Integration',
      href: 'https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/integration-guide2#1-build-integration',
      icon: 'fa-code',
      target: '_self',
      text: 'Build your test integration for PayU Go SDK.',
    },
    {
      title: '2. Test Integration',
      href: 'https://docs.payu.in/docs/integration-guide2#2-test-integration',
      icon: 'fa-flask',
      target: '_self',
      text: 'Validate your PayU Go SDK integration by testing transactions in the sandbox environment.',
    },
    {
      title: '3. Production Checklist',
      href: 'https://docs.payu.in/docs/integration-guide2#3-go-live-checklist',
      icon: 'fa-check-circle',
      target: '_self',
      text: 'Follow this checklist to ensure your integration is ready before going live.',
    },
  ]}
/>

## 1. Build Integration

Below are the steps to build the integration:

### Step 1.1 Install Go in Your System

You should check whether Go is installed in your system by running the following command.

<Accordion title="Check If Go is Installed" icon="fa-info-circle">
<Terminal>{`
go version
`}</Terminal>
</Accordion>

If not installed, run the following command in the terminal to install Go in your system.

<Accordion title="Go Installation Code" icon="fa-code">
<Terminal>{`
  brew install go
`}</Terminal>
</Accordion>

#### Expected Outcome

You should see the latest version of the Go installed in your system when you run the `go version` command.

***

### Step 1.2 Create a Module and Install the PayU SDK

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

#### Expected Outcome

A new Go module is created and the PayU web SDK is added in the module.

***

### Step 1.3 Build the PayU Client

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

| **Parameter**             | **Description**                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `YOUR_TEST_MERCHANT_KEY`  | Your merchant key retrieved from the dashboard. We recommend you to use the test key.   |
| `YOUR_TEST_MERCHANT_SALT` | Your merchant salt retrieved from the dashboard. We recommend you to use the test salt. |

</Accordion>

#### Expected Outcome

A PayU client is added with your merchant key and salt.

***

### Step 1.4 Create a Payment Request

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

2\. Navigate to the `payu-go-integration` folder and run the following code to create the `pay.html` file.

<Terminal>{`
go run .
`}</Terminal>

</Accordion>

#### Expected Outcome

This&#x20;

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

This will create the `pay.html` file.

<br />
