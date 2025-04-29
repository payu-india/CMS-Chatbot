---
title: PaymentAmountExactness Scenario
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
The **paymentAmountExactness** tag in the Biller MDM Response is applicable only when **fetchOption** value is **MANDATORY** and

**isAdhoc** value is false.

For example, if fetch response amount is Rs. 100 then the payment amount can be the following.

1. **EXACT** – Only Rs. 100 can be paid.
2. **EXACT\_AND\_ABOVE** – Rs. 100 or more can be paid.
3. **EXACT\_AND\_BELOW** – Rs. 100 or less can be paid.

There might be a scenario where a Biller may pass on various amount values as part of Bill Fetch Response like Early or Late Payment.

These values are applicable only when all the conditions below hold true for a biller.

1. fetchOption is MANDATORY.
2. isAdhoc field is false.
3. Biller accepts EXACT payment.
