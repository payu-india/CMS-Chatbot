---
title: Go SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Go SDK for Server-side integration
  description: ''
  keywords:
    - Go SDK for Server-side integration
    - Server-side integration Go SDK
    - Integrate Server-side with Go SDK
  robots: index
next:
  description: ''
---
Use PayU GO SDK to integrate PayU payment in your website which is built using GO. PayU GO SDK takes care of the low-level details of the API integration and help you to start collecting payment with just a few lines of code and a function call.


## Supported Payment Features

With this GO SDK you can:

* Collect Payments — Create a Payment form to collect payment.
* Verify Payments — Verify the transaction or check the transaction status
* Handle Refunds — Initiate/cancel refunds and check the status of a refund.
* Check Settlements — Retrieve settlement details that the bank has to settle you.
* Check Bank downtime Status — Get information on eligible payment options and PG/BANK downtime details.
* Check Eligibility — Check the customer’s eligibility for EMI and get the amount according to the EMI interest.
* Manage Invoices — Create/Expire invoice link through the function.

## Steps to integrate

Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

***

> 🚧 Download Go SDK
>
> You can download the Go web SDK from the following GitHub link: [https://github.com/payu-india/web-sdk-go](https://github.com/payu-india/web-sdk-go)

<Accordion title="Create a PayU account" icon="fa-code">
  First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

  ***
</Accordion>

<Accordion title="Install the SDK" icon="fa-code">
  To install the PayU GO SDK using go get , run the following command:

  ```go
  go get github.com/payu-india/web-sdk-go
  ```
</Accordion>

<Accordion title="Build the PayU object" icon="fa-code">
  Use the following sample code for creating an instance of the PayU Object:

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
</Accordion>

## Test and Go-live

<Test_your_integration />
<br />
<Go_Live_Checklist />

