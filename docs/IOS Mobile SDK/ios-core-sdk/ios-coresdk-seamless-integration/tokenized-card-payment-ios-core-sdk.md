---
title: Tokenized Card Payment Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Tokenized Card Integration - iOS Core SDK
  description: ''
  keywords:
    - iOS Tokeinized Card Integration
    - ' Tokenized Card Integration for iOS Core SDK'
  robots: index
next:
  description: ''
---
To collect payments using cards tokenized outside the PayU platform: 

1. Pass the parameters similar to the following code block:

```Text Swift
paymentParam.cardTokenType = "1"
paymentParam.additionalInfo = AdditionalInfo(last4Digits: "1234", tavv: "1234", trid: "1234", tokenRefNo: "1234")
```
```Text Objective-C
    self.paymentParam.cardTokenType = @"1";
    self.paymentParam.additionalInfo = [[AdditionalInfo alloc] initWithLast4Digits:@"1234" tavv:@"1234" trid:@"1234" tokenRefNo:@"1234"];
```

2. Get the request by using the`createRequestWithPaymentParam`.
