---
title: 1. Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
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
