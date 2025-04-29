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
> You can download the Go web SDK from the following GitHub link: <https://github.com/payu-india/web-sdk-go>

## Create a PayU account

First, create a PayU account. See [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

## Install the SDK

To install the PayU GO SDK using go get , run the following command:

```go
go get github.com/payu-india/web-sdk-go
```

***

## Build the PayU object

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

***