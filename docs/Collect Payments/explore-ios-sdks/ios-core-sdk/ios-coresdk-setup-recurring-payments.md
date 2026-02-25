---
title: Set up Recurring Payments
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
This section describes how to set up subscriptions or recurring payments on iOS Core SDK platform.

<Cards>
  <Card title="Step 1: Calculate hash" href="#step-1-calculate-hash" icon="fa-code">
    Calculate hash as the hash calculation formula is different from the result type of payment
  </Card>

  <Card title="Step 2: Make payment" href="#step-2-make-payment" icon="fa-card">
    Create `PayUSIParams` object
  </Card>

  <Card title="Step 3: Handle Response" href="#step-3-handle-response" icon="fa-reply">
    Handle the response from PayU
  </Card>
</Cards>

## Step 1: Calculate hash

For SI transactions, the hash calculation formula is different from the normal type of payment:

**Hash Formula**

```
siDetail = "{"billingAmount": "150.00","billingCurrency": "INR","billingCycle": "WEEKLY","billingInterval": 1,"paymentStartDate": "2019-09-18","paymentEndDate": "2020-10-20"}"
beneficiaryDetail = "{"beneficiaryAccountNumber":"1234567890"}"
// Hash calculation for Cards & StoreCards
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||siDetail|SALT)
// Hash calculation for NB
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||siDetail|beneficiaryDetail|SALT)
```

<Callout icon="📘" theme="info">
  **Reference**: For more information on static hashing, refer to [Generate Static Hash](doc:generate-static-hash-ios).
</Callout>

## Step 2: Make payment

For Net Banking, StoreCard, and Card, create an object of `PayUSIParams` and pass in the payment parameter object:

```swift Swift
let siParam = PayUSIParams(billingAmount: <#T##String#>,
paymentStartDate: <#T##Date#>,
paymentEndDate: <#T##Date#>,
billingCycle: <#T##PayUBillingCycle#>,
billingInterval: <#T##NSNumber#>)
paymentParamForPassing.siParams = siParam
```

For more details on `PayUSIParams`, refer to PayU Standing Instructions Parameters. For Net Banking payment, you have to give beneficiary details using the following code snippet:

```swift Swift
let beneficiaryParams = PayUBeneficiaryParams(beneficiaryName: <#T##String#>,
beneficiaryAccountNumber: <#T##String#>,
beneficiaryAccountType: <#T##BeneficiaryAccountType#>)
paymentParamForPassing.beneficiaryParams = beneficiaryParams
```

After setting the above parameters, create the request object. For more information, refer to Seamless Integration.

## Handle response

The procedure for Response handling is similar to how you handle for other payment options.
