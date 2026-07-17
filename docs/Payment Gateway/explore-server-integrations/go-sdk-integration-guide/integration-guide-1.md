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

This will create the `pay.html` file.

***

### Step 1.5 Complete the Test Payment

<Accordion title="Steps to Complete the Test Payment" icon="fa-info-circle">
1. Open the `payu.html` file or run the following command to open the checkout.

<Terminal>{`
  open pay.html
`}</Terminal>

2. Choose any payment method and provide the <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets" title="Access Test Credentials">test credentials</a>.
3. Complete the payment.
</Accordion>

#### Expected Outcome

You will complete the test payment and receives the response.

<Accordion title="Success and Error Response" icon="fa-circle-check">
Below are the payment method wise success and error responses received.<br/>

**NetBanking**<br/>

```json Success Response
mihpayid=403993715537565049
mode=NB
status=success
unmappedstatus=captured
key=PRiQvJ
txnid=756609e32e92add4b5f2
amount=10.00
discount=0.00
net_amount_debit=10
addedon=2026-05-29 18:49:30
productinfo=Product Info
firstname=Payu-Admin
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@example.com
phone=1234567890
udf1=
udf2=
udf3=
udf4=
udf5=
udf6=
udf7=
udf8=
udf9=
udf10=
hash=79d14afc4a3998a627d8fb431b2ee648b16fd6e31252397109ad5f44d77f7630daaaeedf0bbd5b3e7a81342c96bc087beb43125c0619cac1e5408243fdc29a04
field1=
field2=
field3=
field4=
field5=
field6=
field7=
field8=
field9=Transaction Completed Successfully
payment_source=payu
PG_TYPE=NB-PG
bank_ref_num=ddb199f9-5f43-4441-8648-ce2bcb244568
bankcode=TESTPGNB
error=E000
error_Message=No Error
```
**Credit Cards**<br/>

```json Success Response
mihpayid=403993715537573401
mode=CC
status=success
unmappedstatus=captured
key=a4vGC2
txnid=TXN_NS_1780294871_5566
amount=1500.00
discount=0.00
net_amount_debit=1500
addedon=2026-06-01 11:51:47
productinfo=Subscription
firstname=Sunit
lastname=Kumar
address1=FIRST FLOOR
address2=NEW ASHOK NAGAR
city=Delhi
state=Delhi
country=INDIA
zipcode=201303
email=sunit.kumar@mail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=6ee1e1f743089ce38c79473f19af24371fe80e6249968f1bcbc6d31935afa79c0325d649fa7610a642e694475b33d65011b51b5d7d2a6a46e2b38895e4c27a28
field1=888758893639
field2=599738
field3=1500.00
field4=
field5=00
field6=02
field7=AUTHPOSITIVE
field8=AUTHORIZED
field9=Transaction is Successful
payment_source=payu
PG_TYPE=CC-PG
bank_ref_num=920539478106419300
bankcode=CC
error=E000
error_Message=No Error
cardCategory=domestic
cardnum=XXXXXXXXXXXX2346
cardhash=This field is no longer supported in postback params.
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
```
```json Error Response - 3DS challenge is negative
mihpayid=403993715537573353
mode=CC
status=failure
unmappedstatus=failed
key=a4vGC2
txnid=TXN_NS_1780294680_1316
amount=15000.00
discount=0.00
net_amount_debit=0.00
addedon=2026-06-01 11:48:38
productinfo=DESKTOP
firstname=Sunit
lastname=Kumar
address1=FIRST FLOOR
address2=NEW ASHOK NAGAR
city=Delhi
state=Delhi
country=INDIA
zipcode=201303
email=sunit.kumar@mail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=9ae9baa17a0ca25fd1f860f49022606d1d9d3d9650a639a8656f843a02acc3282157e7997e03734547027789599832e9ac8366dc7c21815e0e226ce6ebe216d4
field1=677160001457370800
field2=
field3=
field4=
field5=
field6=00
field7=3DS_CHALLENGE_NEGATIVE
field8=Transaction failed in Authorization
field9=Transaction Failed at bank end.
payment_source=payu
PG_TYPE=CC-PG
bank_ref_num=
bankcode=CC
error=E308
error_Message=Transaction Failed at bank end.
cardCategory=domestic
cardnum=XXXXXXXXXXXX2346
cardhash=This field is no longer supported in postback params.
splitInfo={"splitStatus":"","splitSegments":[]}
```
**UPI**<br/>

```json Success Response
mihpayid=403993715537577186
mode=UPI
status=success
key=ISgdHG
txnid=cb278c37e5982039ffa0
amount=10.00
addedon=2026-06-01 16:30:23
productinfo=Product Info
firstname=CARDHOLDERXXXXXXXXNAME-Admin
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@example.com
phone=1234567890
udf1=
udf2=
udf3=
udf4=
udf5=
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=
field0=
field1=_mobilenum_@upi
field2=cb278c37e5982039ffa0
field3=
field4=Payu-Admin
field5=AXIuo5ge4DYgb1spEEp038EuZkdbcm229hR
field6=
field7=Transaction completed successfully
field8=generic
field9=Transaction completed successfully
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=UPI-PG
error=E000
error_Message=No Error
net_amount_debit=10
discount=0.00
offer_key=
offer_availed=
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=0981fbaf891fdf6384f35b_mobilenum_a91ec205beeb259f65ec45974c1010039efb1d2e3d4a420c1b75121eb88ecbafbb4d9496071dda27f7ffe1ded0af34a1
bank_ref_no=cb278c37e5982039ffa0
bank_ref_num=cb278c37e5982039ffa0
bankcode=UPI-Intent
surl=https://test.payu.in/admin/test_response
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
```
```json Error Response - Transaction Cancelled or Dropped
mihpayid=403993715537573890
mode=UPI
status=failure
unmappedstatus=userCancelled
key=a4vGC2
txnid=TXN_NS_1780296905_7692
amount=15000.00
discount=0.00
net_amount_debit=0.00
addedon=2026-06-01 12:25:18
productinfo=DESKTOP
firstname=Sunit
lastname=Kumar
address1=FIRST FLOOR
address2=NEW ASHOK NAGAR
city=Delhi
state=Delhi
country=INDIA
zipcode=201303
email=sunit.kumar@mail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=fd3149767139dfda1146aef578cdfef38da79bffe81db64ab8a046de3d349014eb95e9848a003616b79aa6ee61b9c46e5f47403463ae4434ede19e7b6caa71f3
field1=anything@payu
field2=
field3=
field4=
field5=
field6=
field7=
field8=generic
field9=User interrupted by pressing back button
payment_source=payu
PG_TYPE=UPI-PG
bank_ref_num=
bankcode=UPI-Intent
error=E1206
error_Message=Transaction interrupted by pressing back button
splitInfo={"splitStatus":"","splitSegments":[]}
```
**Wallet**<br/>

```json Success Response
mihpayid=403993715537573912
mode=CASH
status=success
unmappedstatus=captured
key=a4vGC2
txnid=TXN_NS_1780296990_7590
amount=15000.00
discount=0.00
net_amount_debit=15000
addedon=2026-06-01 12:26:38
productinfo=DESKTOP
firstname=Aarav
lastname=Raj
address1=Banglore
address2=Banglore
city=Banglore
state=Banglore
country=INDIA
zipcode=201303
email=aarav.raj@testmail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=db7052bf227001b9f02aa675b1a161e633eac2b5712f85c0d466d9b1023e739b0a57e8e61926f047c2efcb19279caf834951e3ff3c9cab99353043af1db2a71f
field1=
field2=
field3=
field4=
field5=
field6=
field7=
field8=
field9=Transaction Completed Successfully
payment_source=payu
PG_TYPE=CASH-PG
bank_ref_num=a92fe2c9-4fc8-4f73-8740-9b292fe4a634
bankcode=FREC
error=E000
error_Message=No Error
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
```
**BNPL**<br/>

```json Success Response
mihpayid=403993715537577231
mode=BNPL
status=success
key=ISgdHG
txnid=6decc0fffa5c60c7cbce
amount=10.00
addedon=2026-06-01 16:34:20
productinfo=Product Info
firstname=Payu-Admin
lastname=
address1=
address2=
city=
state=
country=
zipcode=
email=test@example.com
phone=1234567890
udf1=
udf2=
udf3=
udf4=
udf5=
udf6=
udf7=
udf8=
udf9=
udf10=
card_token=
card_no=
field0=
field1=7715995865
field2=EMI1072289140999791193
field3=Transaction is successful
field4=
field5=iMUvX5VOqXMzv5Nq
field6=TXN558633373
field7=PAYMENT_SUCCESSFUL
field8=SUCCESS
field9=Transaction is successful
payment_source=payu
cardToken=
authenticationMethod=
PG_TYPE=BNPL-PG
error=E000
error_Message=No Error
net_amount_debit=10
discount=0.00
offer_key=
offer_availed=
splitInfo={"splitStatus":"splitNotReceived","splitSegments":[]}
unmappedstatus=captured
hash=caa5b6398fe72ae9a07bc5e2d140fb2872db8f95bfe997de214f7f4cbc14e0933c153db986f029f76b69c12a37589d59ce9fe4c56d1bc713ac9851593563425e
bank_ref_no=TXN558633373
bank_ref_num=TXN558633373
bankcode=LAZYPAY
surl=https://test.payu.in/admin/test_response
curl=https://test.payu.in/admin/test_response
furl=https://test.payu.in/admin/test_response
```
```json Error Response - Transaction Cancelled During OTP Flow
mihpayid=403993715537573947
mode=BNPL
status=failure
unmappedstatus=userCancelled
key=a4vGC2
txnid=TXN_NS_1780297112_4289
amount=1500.00
discount=0.00
net_amount_debit=0.00
addedon=2026-06-01 12:28:44
productinfo=Test
firstname=Sunit
lastname=Kumar
address1=FIRST FLOOR
address2=NEW ASHOK NAGAR
city=Delhi
state=Delhi
country=INDIA
zipcode=201303
email=sunit.kumar@mail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=79c624327255af38af22d10005f43a6afaaa9cf212ddb2998becd56d1dd9c1f5eae1d587ab82543f53ed005eb3d752f67b445a8523153f4bea969cb3e765b5dd
field1=9876543210
field2=EMI775701587506297063
field3=Hola!! Avail LazyPay Credit with just an OTP
field4=
field5=zA0oORMOEt3RrWHg
field6=TXN983658033
field7=OTP_GENERATION_SUCCESSFUL
field8=LP_ELIGIBLE
field9=cancelled by user
payment_source=payu
PG_TYPE=BNPL-PG
bank_ref_num=TXN983658033
bankcode=LAZYPAY
error=
error_Message=
splitInfo={"splitStatus":"","splitSegments":[]}
```

**NEFT/RTGS**<br/>

For security reasons, the success response sample or URL is not included here. Only the error response is recorded.<br/>

```json Error Response
mihpayid=403993715537574750
mode=NEFTRTGS
status=pending
unmappedstatus=pending
key=a4vGC2
txnid=TXN_NS_1780300270_2797
amount=10.00
discount=0.00
net_amount_debit=0.00
addedon=2026-06-01 13:21:24
productinfo=DESKTOP
firstname=Sunit
lastname=Kumar
address1=FIRST FLOOR
address2=NEW ASHOK NAGAR
city=Delhi
state=Delhi
country=INDIA
zipcode=201303
email=sunit.kumar@mail.com
phone=9876543210
udf1=Testing UDF 1
udf2=Testing UDF2
udf3=
udf4=
udf5=Sample_Invoice_11
udf6=
udf7=
udf8=
udf9=
udf10=
hash=ed4dbb911f9bfee507362e2e053c16c07063a55302ea58cf3f026f5daeefbd52da8f316d51911c891a13a1bb648a26b24b8005a84af30904d78c13a54b4d35bf
field1=
field2=
field3=
field4=
field5=
field6=
field7=
field8=02
field9=Transaction is pending
payment_source=payu
PG_TYPE=NEFTRTGS-PG
bank_ref_num=
bankcode=EFTAXIS
error=E227
error_Message=Transaction is Pending
splitInfo={"splitStatus":"","splitSegments":[]}
```
Refer to the Errors section for the parameters and description.


</Accordion>

#### What Next - Customer Journey

Customer selects a payment method and completes the payment. PayU then sends the transaction response parameters.

<Accordion title="Customer Journey Outcome" icon="fa-route">
**Expected Output**

These are the expected outcomes of the transaction.

- Success
- Failure
- Pending
- Cancelled

PayU then redirects to:

- `surl` for success
- `furl` for failure
</Accordion>

#### Step 1.3.1 Customize PayU Payment Page _(Optional)_

<Accordion title="Customize Checkout" icon="fa-gear">
You can customize the following in the Checkout page:<br/>

* Enforce Pay Method or Remove Category
* Change the Language
* Configure Payment Method and Checkout Settings

Refer to the <a href="https://docs.payu.in/docs/payu-payment-page-customization" target="_blank">Customize PayU Payment Page</a> for more information about cutomizing the PayU payment page.
</Accordion>

***

### Step 1.6 Verify Response via Reverse Hashing

Response verification ensures that the response originated from PayU and has not been modified. It protects against:

\- Tampered responses
\- Spoofed requests
\- Fraudulent status updates

After the payment is successful or failed, PayU POSTs back to your `surl` or `furl` respectively with URL-encoded fields (form post). This payload includes the transaction status, `txnid`, `mihpayid`, and a hash you must verify (reverse hashing) for verification. Below is how the reverse hashing works.

<Callout icon="✅" theme="okay">
  ### **Validation Rules:**

  - Generated hash must match response hash
  - Amount must match original order
  - Transaction ID must exist
  - Order should not already be paid
</Callout>

<Accordion title="Reverse Hashing Logic" icon="fa-arrow-rotate-left">
Create a hash using the following logic.<br/>
```json Reverse Hash Logic
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```
<br/>

You should compare the hash value you got from the above logic with the hash value you received in the response. The payment is verified if the hash values match and update the order state.
</Accordion>

<Callout icon="⚠️" theme="warn">
  ### **Watch Out!**

  If hash mismatches:

  - Reject callback
  - Log security event
  - Do not mark payment successful
</Callout>

You can also use the <Anchor target="_blank" href="https://payu-hashverificationtool.onrender.com/">PayU's Hash Verification System</Anchor> to generate a hash (reverse hash) for payment verification.

<br />

***

### Step 1.7 Verify the Payment

After the transaction is complete, you should check the payment status. Use PayU verification mechanisms for reconciliation. This is the recommended verification order:

1\. Reverse hash validation (_step 1.4)_
2\. Webhooks
3\. Verify Payment API
4\. PayU Dashboard

<Accordion title="Verify Payment Methods" icon="fa-check-double">
  <Tabs>
  <Tab title="1. Verify using Webhooks">
    Configure the webhooks to monitor the status of payments.<br/>
    
    Webhooks enable a server to communicate with another server by sending an HTTP callback or message.<br/>

    These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level.<br/>

    Know how to <a href="https://docs.payu.in/docs/webhook-events-and-sample-payloads" target="_blank">manage Webhooks</a> for Payments.<br/>
  </Tab>

  <Tab title="2. Verify using APIs">
    You can poll the <a href="https://docs.payu.in/reference/verify_payment_api" target="_blank">Verify Payment API</a> to verify the payment.
  </Tab>

  <Tab title="3. Verify from Dashboard">
    To verify the payment from the PayU Dashboard:<br/>
    1. Log in to the <a href="https://onboarding.payu.in/app/account/signin" target="_blank">PayU Dashboard</a> and click **Transactions** from the left menu.
    2. Check if a **Payu ID (Transaction ID)** is created for the recent transaction and if the payment is successful, the status is marked as **Success**.<br/>
    <Image       src="https://files.readme.io/30840455deadfe76c808f4954f9d18dcdb2a949d9e6851ee8566e9f58094bd3d-varify_payment_dashboard.png" align="center" caption="_Verify the Payment from Dashboard_" border={true} framed={false} />
  </Tab>
</Tabs>
</Accordion>

<br />

***

## 2. Test Integration

After you build the integration, you should test it thoroughly before going live.<br />

<Callout icon="⚠️" theme="warn">
  ### **Watch out!**

  This is a test page. Before making the payment:

  - **Verify API Credentials:** Double-check that you are using the correct key and salt for the test environment.

  - **Validate Hash Calculation:** The most common point of failure is an incorrect hash.
    - Temporarily print the string that you are passing into the hash function on your server.
    - Ensure the order of the parameters exactly matches the format specified in the documentation.
    - Verify that there are no empty or null values for mandatory parameters in the hash string.
</Callout>

***

### Step 2.1 Simulate a Successful Transaction

<Accordion title="Successful Transaction Steps" icon="fa-circle-check">
After you post a form and save the html file and perform the following steps:
1. Open the file to initiate the transaction.
2. Select the payment method and make a test transaction to ensure the integration is working as expected.
</Accordion>

#### Supported Payment Methods

You can use the following default payment methods and their test details to make the payment.

<Accordion title="NetBanking" icon="fa-building-columns">
  Use the following credentials if you choose NetBanking as a payment method:<br/>
  
  **user name:** payu
  **password:** payu
  **OTP:** 123456
</Accordion>

<Accordion title="Debit Card" icon="fa-credit-card">
  | Card Number         | Network    | Expiry | CVV | OTP    |
  | :------------------ | :--------- | :----- | :-- | :----- |
  | 5118-7000-0000-0003 | Mastercard | 05/30  | 123 | 123456 |
  | 4594-5380-5063-9999 | VISA       | 05/30  | 123 | 123456 |
</Accordion>

<Accordion title="Credit Card" icon="fa-credit-card">
  | **Payment Flow**              | **Card Number**  | **Network** | **Expiry** | **CVV** | **OTP** |
  | ----------------------------- | ---------------- | ----------- | ---------- | ------- | ------- |
  | PayU/Merchant Hosted Checkout | 5123456789012346 | Mastercard  | 05/30      | 123     | 123456  |
  | PayU/Merchant Hosted Checkout | 4012001037141112 | VISA        | 05/30      | 123     | 123456  |
  | Server-to-Server              | 5497774415170603 | Mastercard  | 05/30      | 412     | 123456  |
  | PayU/Merchant Hosted Checkout | 6082015309577308 | RUPAY       | 05/30      | 123     | 123456  |
  | PayU/Merchant Hosted Checkout | 370295061673669  | AMEX        | 03/30      | 1234    | 725356  |
</Accordion>

<Accordion title="UPI" icon="fa-mobile-screen-button">
  You can use `anything@payu` or `999999999@payu` as VPA to test your integration.<br/>

  > 📘 Notes:
  >
  > - The **anything\@payu** VPA can be used in the sandbox or [Merchant Hosted > Collect Payment - UPI](ref:_payment_merchant_hosted_upi) API reference page and any other VPA will not work for the **_payment** only.
  > - For the [Validate VPA Handle API](ref:validate_vpa_api), you can use any valid VPA.
</Accordion>

<Accordion title="Wallet" icon="fa-wallet">
  | Vendor | Mobile Number                                                     | OTP    |
  | ------ | ----------------------------------------------------------------- | ------ |
  | PayTM  | 7777777777 or use card mentioned under [Test Cards](#test-cards). | 888888 |
  | Amazon | You can test using your original Amazon account details.          |        |
  | Airtel | You can use your mobile number.                                   |        |
</Accordion>

<Callout icon="📘" theme="info">
  ### **Handy Tips**

  Apart from the above default payment methods, you can <Anchor target="_blank" href="https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings">enable the following payment methods</Anchor> in the checkout:

  - BNPL
  - EMI
  - International Payments
</Callout>

***

### Step 2.2 Simulate a Failed Transaction

It is equally important to test the failed transaction. Perform the following steps to simulate the failed transaction.

<Accordion title="Failed Transaction Steps" icon="fa-vial">
1. Open the HTML file to initiate the transaction.
2. Select any payment method and simulate a failed transaction by providing a invalid test credentials.
</Accordion>

<Callout icon="✅" theme="okay">
  ### **Verify**

  Verify the following during a failed transaction:

  - [x] Failure URL is triggered

  - [x] Customer receives appropriate messaging

  - [x] Order remains unpaid
</Callout>

***

## 3. Go-live Checklist

Now that you successfully tested the integration, check the go-live checklist for PayU hosted checkout integration. Consider these steps before taking the integration live.

<Accordion title="Production Credentials" icon="fa-user-lock">
Replace test merchant key and salt with live credentials. Know how to <a href="https://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard" target="_blank">create live merchant key and salt</a>
</Accordion>

<Accordion title="Production Environment" icon="fa-link">
Make sure you update the test environment with the production environment.
</Accordion>

<Accordion title="Security Checklist" icon="fa-shield-check">
- [x] Hash generation occurs server-side

- [x] Salt is never exposed

- [x] HTTPS is enforced

- [x] Sensitive information is not logged
</Accordion>

<Accordion title="Webhooks" icon="fa-info-circle">
Make sure the <a href="https://docs.payu.in/docs/webhook-events-and-sample-payloads" target="_blank">webhook is configured</a>.
</Accordion>

<Accordion title="Production Readiness" icon="fa-clipboard-check">
- [x] Hash validation implemented

- [x] Reverse hash validation implemented

- [x] Callback retries handled

- [x] Duplicate processing prevented

- [x] Failure URL is triggered

- [x] Alerting configured

- [x] Failure URL is triggered
</Accordion>

***

## Errors and Troubleshooting

<Accordion title="Invalid Hash" icon="fa-fingerprint">
**Error Causes**

* Wrong parameter order
* Missing pipe (`|`) separators
* Incorrect salt
* Missing empty UDF placeholders
* Extra spaces in input values

**Recommended Fix**

* Verify hash sequence exactly matches PayU documentation.
* Ensure all empty UDF fields still include separators (`|||||||||||`).
* Confirm merchant key and salt are correct.
* Remove leading/trailing spaces from all parameters.
* Generate hash using SHA-512 only.
* Generate hash on backend, never frontend.
</Accordion>

<Accordion title="Payment Page Not Loading" icon="fa-circle-xmark">
**Error Causes**

* Wrong endpoint URL
* Request sent using GET instead of POST
* Missing mandatory parameters
* Browser JavaScript error
* Firewall/network issue

**Recommended Fix**

* Ensure to use the correct environment endpoint.
* Ensure the form method is POST
* Validate all mandatory parameters.
* Remove leading/trailing spaces from all parameters.
* Check browser developer console.
* Inspect browser network requests.
</Accordion>

<Accordion title="Callback Not Triggered (surl / furl)" icon="fa-link-slash">
**Error Causes**

* Invalid callback URL
* Localhost used
* Firewall restriction
* SSL/TLS issue
* Callback endpoint inaccessible

**Recommended Fix**

* Ensure callback URL is publicly accessible
* Use HTTPS only
* Do not use localhost
* Verify endpoint accepts POST requests
* Return HTTP 200 after processing callback
</Accordion>

<Accordion title="Reverse Hash Mismatch" icon="fa-fingerprint">
**Error Causes**

* Wrong reverse hash sequence
* Missing UDF placeholders
* Wrong salt
* Using request hash logic instead of reverse hash logic

**Recommended Fix**

* Use reverse hash sequence exactly as documented
* Ensure UDF fields are included in reverse order
* Verify status field is included
* Confirm salt matches merchant configuration
</Accordion>

<Accordion title="Duplicate Order Processing" icon="fa-copy">
**Error Causes**

* Callback retries
* No idempotency checks
* Order state not verified before processing

**Recommended Fix**

* Implement idempotency checks before processing
</Accordion>

<Accordion title="Amount Mismatch" icon="fa-fingerprint">
**Error Causes**

* Order modified after checkout started
* Incorrect amount formatting
* Wrong order fetched from database

**Recommended Fix**

* Compare callback amount with original transaction amount
* Normalize decimal precision
* Reject mismatched callbacks
* Log mismatch for investigation
</Accordion>

<br />
