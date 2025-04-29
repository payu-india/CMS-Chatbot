---
title: TwidPay BNPL Integration - iOS Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: TwidPay BNPL Integration - iOS Core SDK
  description: ''
  keywords:
    - TwidPay BNPL Integration for iOS Core SDK
    - ' iOS TwidPay BNPL Integration'
  robots: index
next:
  description: ''
---
To pay using TwidPay, perform the following steps. 

1. Create the post data with `CASH_CARD_TWID`:

```Text Objective-C
self.paymentParamForPassing.bankCode = CASH_CARD_TWID;//BankCode
```
```Text Swift
paymentParamForPassing.bankCode = CASH_CARD_TWID //BankCode
```

2. Get the Twid customer hash in the `field5` param of PayuResponse, which can be used in the next transactions to skip authentication.

```Text Objective-C
    self.paymentParamForPassing.twidCustomerHash = @"Twid customer hash";
  
```
```Text Swift
paymentParamForPassing.twidCustomerHash = "Twid customer hash"
```
